# -*- coding: utf-8 -*-
"""
Pruebas de las herramientas con datos 100 % ficticios (COMERCIALIZADORA EJEMPLO SAS, NIT 900.123.456-8).

    python herramientas/pruebas/test_herramientas.py        (sin dependencias extra)
    python -m pytest herramientas/pruebas                   (si tienes pytest)
"""
from __future__ import annotations

import sys
import tempfile
from datetime import date
from pathlib import Path

import openpyxl

H = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(H))
import comun  # noqa: E402
import conciliar_1aN  # noqa: E402
import cruce_token  # noqa: E402
import nuevo_periodo  # noqa: E402
import revisar_entrega  # noqa: E402
import validar_auxiliar  # noqa: E402

NIT = "900123456"


def xlsx(ruta: Path, encabezados: list, filas: list) -> Path:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(encabezados)
    for f in filas:
        ws.append(f)
    wb.save(ruta)
    return ruta


# ------------------------------------------------------------------ comun
def test_dv_y_montos():
    assert comun.dv("900123456") == "8"
    assert comun.dv("800197268") == "4"            # NIT publicado de la DIAN
    assert comun.monto("1.234.567,89") == 1234567.89
    assert comun.monto("1,234,567.89") == 1234567.89
    assert comun.monto("(2.500)") == -2500
    assert comun.monto("$ 46.142.000") == 46142000
    assert comun.pesos(-1500.5) == "-$1.500,50"


# ------------------------------------------------------------------ conciliación
def _datos_conciliacion(tmp: Path):
    ext = xlsx(tmp / "EXTRACTO.xlsx", ["Fecha", "Descripción", "Valor"], [
        [date(2026, 1, 5), "TRANSFERENCIA CLIENTE", 5_000_000],
        [date(2026, 1, 8), "PAGO PSE PROVEEDOR", -2_380_000],
        [date(2026, 1, 12), "CONSIGNACION", 1_200_000],     # tres abonos que
        [date(2026, 1, 12), "CONSIGNACION", 800_000],       # en libros son
        [date(2026, 1, 13), "CONSIGNACION", 500_000],       # un solo recibo de 2.500.000
        [date(2026, 1, 31), "GMF 4X1000", -9_520],
        [date(2026, 1, 31), "CUOTA DE MANEJO", -18_000],
    ])
    lib = xlsx(tmp / "AUX_1110.xlsx", ["Fecha", "Documento", "Descripción", "Débito", "Crédito"], [
        [date(2026, 1, 1), "", "SALDO INICIAL", 0, 0],
        [date(2026, 1, 5), "RC-101", "Recaudo factura FE-1040", 5_000_000, 0],
        [date(2026, 1, 8), "CE-201", "Pago proveedor", 0, 2_380_000],
        [date(2026, 1, 12), "RC-102", "Recaudo facturas FE-1041 a FE-1043", 2_500_000, 0],
        [date(2026, 1, 30), "CE-202", "Transferencia girada no cobrada", 0, 640_000],
    ])
    return ext, lib


def test_conciliacion_cierra_en_cero_con_cruce_varios_a_uno():
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        ext, lib = _datos_conciliacion(tmp)
        banco = conciliar_1aN.cargar_extracto(ext)
        libro = conciliar_1aN.cargar_libro(lib)
        cruces = conciliar_1aN.conciliar(banco, libro)
        assert any(c[1].startswith("3") and len(c[2]) == 3 for c in cruces), "debe encontrar 3 abonos = 1 recibo"
        # saldo inicial 40.000.000 en ambos lados
        saldo_libros = 40_000_000 + 5_000_000 - 2_380_000 + 2_500_000 - 640_000
        saldo_ext = 40_000_000 + 5_000_000 - 2_380_000 + 2_500_000 - 9_520 - 18_000
        codigo = conciliar_1aN.main(["--extracto", str(ext), "--libro", str(lib), "--saldo-extracto", str(saldo_ext),
                                     "--saldo-libros", str(saldo_libros), "--salida", str(tmp / "CONC.xlsx")])
        assert codigo == 0
        wb = openpyxl.load_workbook(tmp / "CONC.xlsx")
        assert wb.sheetnames == ["CONCILIACION", "PARTIDAS CONCILIATORIAS", "CRUCES CONFIRMADOS", "CUADRE POR SENTIDO"]
        assert wb["CONCILIACION"]["A5"].fill.fgColor.rgb.endswith("231F20")   # encabezado negro Ritoré


def test_conciliacion_que_no_cierra_devuelve_2():
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        ext, lib = _datos_conciliacion(tmp)
        codigo = conciliar_1aN.main(["--extracto", str(ext), "--libro", str(lib), "--saldo-extracto", "1",
                                     "--saldo-libros", "2", "--salida", str(tmp / "C.xlsx")])
        assert codigo == 2


# ------------------------------------------------------------------ token
def test_cruce_token_detecta_faltantes_sobrantes_diferencias_y_huecos():
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        enc = ["Tipo de documento", "Prefijo", "Folio", "Fecha Emisión", "NIT Emisor", "Nombre Emisor",
               "NIT Receptor", "Nombre Receptor", "IVA", "Total"]
        tok = xlsx(tmp / "TOKEN.xlsx", enc, [
            ["Factura electrónica", "FE", 1040, "2026-01-05", NIT, "COMERCIALIZADORA EJEMPLO SAS", "901000001", "CLIENTE UNO SAS", 798_319, 5_000_000],
            ["Factura electrónica", "FE", 1041, "2026-01-10", NIT, "COMERCIALIZADORA EJEMPLO SAS", "901000002", "CLIENTE DOS SAS", 159_664, 1_000_000],
            ["Factura electrónica", "FE", 1043, "2026-01-11", NIT, "COMERCIALIZADORA EJEMPLO SAS", "901000002", "CLIENTE DOS SAS", 239_496, 1_500_000],
            ["Factura electrónica", "SETP", 77, "2026-01-08", "901000009", "PROVEEDOR NUEVE SAS", NIT, "COMERCIALIZADORA EJEMPLO SAS", 380_000, 2_380_000],
            ["Factura electrónica", "FV", 9, "2026-01-20", "901000010", "PROVEEDOR DIEZ SAS", NIT, "COMERCIALIZADORA EJEMPLO SAS", 0, 350_000],
        ])
        lib = xlsx(tmp / "DOCS.xlsx", ["Documento", "Fecha", "NIT", "Total", "Descripción"], [
            ["FE-1040", "2026-01-05", "901000001", 5_000_150, "Venta"],      # dentro de ±200
            ["FE 1041", "2026-01-10", "901000002", 1_000_000, "Venta"],
            ["FE-1043", "2026-01-11", "901000002", 1_450_000, "Venta"],      # diferencia de valor
            ["SETP77", "2026-01-08", "901000009", 2_380_000, "Compra"],
            ["CC-55", "2026-01-25", "901000011", 120_000, "Compra sin factura electrónica"],
        ])
        codigo = cruce_token.main(["--token", str(tok), "--libro", str(lib), "--nit-empresa", NIT, "--salida", str(tmp / "CT.xlsx")])
        assert codigo == 2
        token = cruce_token.cargar_token(tok)
        libro = cruce_token.cargar_libro(lib)
        filas, sin_libro, dif, sin_token = cruce_token.cruzar(token, libro, NIT)
        assert [t["clave"] for t in sin_libro] == ["FV-9"]
        assert [d["doc"] for d in sin_token] == ["CC-55"]
        assert [t["clave"] for t, _, _ in dif] == ["FE-1043"]
        assert cruce_token.huecos([1040, 1041, 1043]) == [1042]


# ------------------------------------------------------------------ auxiliar
def test_validar_auxiliar_descarta_totales_y_detecta_terceros():
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        aux = xlsx(tmp / "AUX.xlsx", ["Cuenta", "Descripción", "NIT", "Nombre tercero", "Débito", "Crédito"], [
            ["11100501", "SALDO INICIAL", "", "", 40_000_000, 0],
            ["11100501", "Recaudo", "901000001", "CLIENTE UNO SAS", 5_000_000, 0],
            ["13050501", "Recaudo", "901000001", "CLIENTE UNO SAS", 0, 5_000_000],
            ["TOTAL 1110", "", "", "", 5_000_000, 0],
            ["51352501", "Gasto", "", "", 100_000, 0],
            ["11100501", "Pago", "222222222", "VARIOS", 0, 100_000],
            ["23359501", "Proveedor", "900123456-1", "PROVEEDOR X", 0, 0],
        ])
        assert validar_auxiliar.main(["--libro", str(aux), "--nit-empresa", NIT]) == 2


# ------------------------------------------------------------------ período y entrega
def test_nuevo_periodo_y_revision_de_entrega():
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        per = nuevo_periodo.crear(tmp, "COMERCIALIZADORA EJEMPLO SAS", "2026-01", NIT, "Auxiliar de prueba")
        assert (per / "03-SALIDA/ASIENTOS_PROPUESTOS_2026-01.xlsx").exists()
        assert (per / "04-TRAZAS/NOTAS-Y-PENDIENTES.md").exists()
        assert "{{CLIENTE}}" not in (per / "ENTREGA.md").read_text(encoding="utf-8")
        assert revisar_entrega.main([str(per)]) == 2          # carpeta recién creada: no se entrega

        # se completa el período como lo haría el auxiliar
        for n in ("TOKEN_2026-01.xlsx", "EXTRACTO_BANCO_2026-01.pdf", "BP_2026-01.xlsx", "AUX_2026-01.xlsx"):
            (per / "01-INSUMOS" / n).write_bytes(b"x")
        for n in ("01_CRUCE_TOKEN", "02_CONCILIACIONES", "03_CARTERA_Y_PROVEEDORES", "04_CUADRE_IMPUESTOS", "05_NOMINA", "06_BP_REVISADO"):
            (per / "02-PROCESADO" / f"{n}_2026-01.xlsx").write_bytes(b"x")
        (per / "03-SALIDA" / "BORRADOR F-350 2026-01.html").write_text("<html></html>", encoding="utf-8")
        ruta_as = per / "03-SALIDA/ASIENTOS_PROPUESTOS_2026-01.xlsx"
        wb = openpyxl.load_workbook(ruta_as)
        ws = wb["02 ASIENTOS"]
        for r, fila in enumerate([[1, "ENE", "AJ-01", "2026-01-31", "53050501", "GMF", "800197268", 9_520, 0, "GMF enero", "Extracto"],
                                  [2, "ENE", "AJ-01", "2026-01-31", "11100501", "Banco", "800197268", 0, 9_520, "GMF enero", "Extracto"]], 6):
            for c, v in enumerate(fila, 1):
                ws.cell(r, c, v)
        wb.save(ruta_as)
        entrega = per / "ENTREGA.md"
        def con_estado(linea: str) -> str:
            celdas = linea.split("|")
            celdas[3] = " 🟢 "
            return "|".join(celdas)
        t = entrega.read_text(encoding="utf-8")
        t = "\n".join(con_estado(l) if l.startswith("| ") and l[2:3].isdigit() else l for l in t.splitlines())
        entrega.write_text(t, encoding="utf-8")
        notas = per / "04-TRAZAS/NOTAS-Y-PENDIENTES.md"
        notas.write_text(notas.read_text(encoding="utf-8").replace(
            "| 1 | | | | | | ABIERTO |", "| 1 | Bancos | Extracto de la cuenta de ahorros | $0 | Cliente | 2026-02-10 | ABIERTO |"), encoding="utf-8")
        assert revisar_entrega.main([str(per)]) == 0

        # un archivo con sufijo de versión fuera de 'anteriores' vuelve a bloquear
        (per / "02-PROCESADO" / "02_CONCILIACIONES_2026-01 v2.xlsx").write_bytes(b"x")
        assert revisar_entrega.main([str(per)]) == 2


if __name__ == "__main__":
    pruebas = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    fallas = 0
    for p in pruebas:
        try:
            p()
            print(f"OK    {p.__name__}")
        except Exception as e:  # noqa: BLE001
            fallas += 1
            print(f"FALLA {p.__name__}: {type(e).__name__}: {e}")
    print(f"\n{len(pruebas) - fallas}/{len(pruebas)} pruebas pasaron")
    sys.exit(1 if fallas else 0)
