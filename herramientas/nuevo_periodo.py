#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Crea la carpeta estándar de un período para un cliente, con las plantillas de trazas ya diligenciadas
con cliente y período y la hoja de asientos propuestos lista para usar.

    python herramientas/nuevo_periodo.py "RUTA/TRABAJOS" "COMERCIALIZADORA EJEMPLO SAS" 2026-01 --nit 900123456 --auxiliar "Ana Pérez"

Resultado:
    <RUTA>/<CLIENTE>/_cliente.yaml            (solo si no existe: copia de la plantilla, la completa el contador)
    <RUTA>/<CLIENTE>/<AAAA-MM>/ENTREGA.md
    <RUTA>/<CLIENTE>/<AAAA-MM>/01-INSUMOS/SOPORTES/
    <RUTA>/<CLIENTE>/<AAAA-MM>/02-PROCESADO/
    <RUTA>/<CLIENTE>/<AAAA-MM>/03-SALIDA/ASIENTOS_PROPUESTOS_<AAAA-MM>.xlsx
    <RUTA>/<CLIENTE>/<AAAA-MM>/04-TRAZAS/ (checklist, notas, diferencias, corridas, observaciones, solicitud de insumos)
No sobrescribe nada que ya exista.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from comun import hoja, libro_salida, dv  # noqa: E402

PLANTILLAS = AQUI.parent / "02-MANUAL-DE-ENTREGA" / "plantillas"
CHECKLIST = AQUI.parent / "02-MANUAL-DE-ENTREGA" / "03 - Checklist de Cierre Mensual.md"
MESES = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
COLS_ASIENTOS = ["N°", "MES", "COMPROBANTE", "FECHA", "CUENTA", "NOMBRE CUENTA", "TERCERO (NIT)", "DÉBITO", "CRÉDITO", "QUÉ REGISTRA", "SOPORTE"]


def rellenar(texto: str, datos: dict) -> str:
    for k, v in datos.items():
        texto = texto.replace("{{" + k + "}}", str(v))
    return texto


def crear(raiz: Path, cliente: str, periodo: str, nit: str = "", auxiliar: str = "") -> Path:
    if not re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])", periodo):
        raise ValueError("El período va como AAAA-MM, por ejemplo 2026-01")
    anio, mes = int(periodo[:4]), int(periodo[5:])
    base = raiz / cliente
    per = base / periodo
    for sub in ("01-INSUMOS/SOPORTES", "02-PROCESADO", "03-SALIDA", "04-TRAZAS/anteriores"):
        (per / sub).mkdir(parents=True, exist_ok=True)
    datos = {"CLIENTE": cliente, "PERIODO": periodo, "NIT": f"{nit}-{dv(nit)}" if nit else "_________",
             "AUXILIAR": auxiliar or "_________", "FECHA_ENTREGA": "_________", "FECHA": date.today().isoformat(),
             "MES": f"{MESES[mes - 1].lower()} de {anio}", "CONTACTO": "_________", "FECHA_LIMITE": "_________"}
    destinos = {
        "ENTREGA.md": per / "ENTREGA.md",
        "NOTAS-Y-PENDIENTES.md": per / "04-TRAZAS/NOTAS-Y-PENDIENTES.md",
        "TABLA-DE-DIFERENCIAS.md": per / "04-TRAZAS/TABLA-DE-DIFERENCIAS.md",
        "REGISTRO-DE-CORRIDAS.md": per / "04-TRAZAS/REGISTRO-DE-CORRIDAS.md",
        "OBSERVACIONES-DEL-CONTADOR.md": per / "04-TRAZAS/OBSERVACIONES-DEL-CONTADOR.md",
        "SOLICITUD-DE-INSUMOS.md": per / "04-TRAZAS/SOLICITUD-DE-INSUMOS.md",
    }
    for plantilla, destino in destinos.items():
        if not destino.exists():
            destino.write_text(rellenar((PLANTILLAS / plantilla).read_text(encoding="utf-8"), datos), encoding="utf-8")
    chk = per / "04-TRAZAS/CHECKLIST-DE-CIERRE.md"
    if not chk.exists():
        t = CHECKLIST.read_text(encoding="utf-8")
        t = re.sub(r"^---.*?---\s*", "", t, flags=re.S)
        chk.write_text(f"<!-- {cliente} · {periodo} -->\n" + t, encoding="utf-8")
    yml = base / "_cliente.yaml"
    if not yml.exists():
        shutil.copyfile(PLANTILLAS / "_cliente.yaml", yml)
    asientos = per / "03-SALIDA" / f"ASIENTOS_PROPUESTOS_{periodo}.xlsx"
    if not asientos.exists():
        wb = libro_salida()
        ws = hoja(wb, "02 ASIENTOS", COLS_ASIENTOS, [], [6, 8, 13, 11, 12, 30, 18, 15, 15, 40, 22],
                  subtitulo=f"{cliente} · {periodo} · asientos PROPUESTOS: no se registran sin aprobación del contador",
                  columnas_moneda={7, 8})
        ws.cell(4, 1, "Cada comprobante cuadra por separado · cuentas del plan existente · tercero en cada línea · asientos netos")
        for r in range(6, 206):
            for c in (8, 9):
                ws.cell(r, c).number_format = '#,##0.##;[Red]-#,##0.##'
        ws.cell(207, 7, "TOTALES")
        ws.cell(207, 8, "=SUM(H6:H206)").number_format = '#,##0.##'
        ws.cell(207, 9, "=SUM(I6:I206)").number_format = '#,##0.##'
        ws.cell(208, 7, "DIFERENCIA (debe ser 0)")
        ws.cell(208, 8, "=H207-I207").number_format = '#,##0.##'
        wb.save(asientos)
    return per


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("raiz", help="carpeta de trabajos (por ejemplo TRABAJOS Y REQUERIMIENTOS)")
    ap.add_argument("cliente")
    ap.add_argument("periodo", help="AAAA-MM")
    ap.add_argument("--nit", default="")
    ap.add_argument("--auxiliar", default="")
    a = ap.parse_args(argv)
    per = crear(Path(a.raiz), a.cliente, a.periodo, a.nit, a.auxiliar)
    print(f"Período listo: {per}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
