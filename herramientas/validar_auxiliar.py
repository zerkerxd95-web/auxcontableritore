#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validación del libro auxiliar exportado del software antes de usarlo en cualquier cruce.

    python herramientas/validar_auxiliar.py --libro AUX_2026-01.xlsx [--nit-empresa 900123456] [--salida 02-PROCESADO/VALIDACION_AUX_2026-01.xlsx]

Revisa:
  1. Débitos = créditos (descartando primero filas de SALDO INICIAL y filas que empiezan por TOTAL del formato W).
  2. Movimientos sin tercero.
  3. Terceros genéricos (VARIOS, CLIENTES, PROVEEDORES, GENERAL, SIN NIT, 999999999, 222222222 fuera de exógena).
  4. NIT de la propia empresa usado como tercero de un gasto o ingreso.
  5. Identificación con DV mal calculado (cuando el NIT viene con guion) y cédulas registradas con DV.
  6. Saldos de naturaleza contraria por cuenta (activo y gasto crédito; pasivo, patrimonio e ingreso débito), sobre el
     movimiento neto del período.
Código de salida 0 si no hay hallazgos bloqueantes (1 y 2), 2 si los hay.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from comun import buscar_col, dv, hoja, leer_tabla, libro_salida, monto, pesos, solo_digitos  # noqa: E402

GENERICOS = re.compile(r"\b(VARIOS|CLIENTES? VARIOS|PROVEEDORES? VARIOS|GENERAL|SIN NIT|SIN TERCERO|N/?A)\b", re.I)
NIT_GENERICOS = {"999999999", "9999999999", "111111111", "000000000", "0"}


def naturaleza(cuenta: str) -> str:
    c = cuenta[:1]
    return {"1": "D", "5": "D", "6": "D", "7": "D", "2": "C", "3": "C", "4": "C"}.get(c, "")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--libro", required=True)
    ap.add_argument("--hoja")
    ap.add_argument("--nit-empresa", default="")
    ap.add_argument("--salida")
    a = ap.parse_args(argv)
    enc, filas = leer_tabla(a.libro, a.hoja, buscar_encabezado=("cuenta",))
    cc = buscar_col(enc, "cuenta", "codigo cuenta", "codigo")
    cn = buscar_col(enc, "nit", "tercero", "identificacion", obligatorio=False)
    cnom = buscar_col(enc, "nombre tercero", "nombre", "razon social", obligatorio=False)
    cd = buscar_col(enc, "descripcion", "concepto", "detalle", obligatorio=False)
    cdb = buscar_col(enc, "debito", "debitos", "debe")
    ccr = buscar_col(enc, "credito", "creditos", "haber")
    nit_emp = solo_digitos(a.nit_empresa)[:9]

    hallazgos, td, tc, descartadas = [], 0.0, 0.0, 0
    neto = defaultdict(float)
    for i, f in enumerate(filas, 2):
        cuenta = str(f[cc] or "").strip()
        desc = str(f[cd] or "") if cd is not None else ""
        if cuenta.upper().replace(" ", "").startswith("TOTAL") or desc.upper().startswith(("SALDO INICIAL", "SALDO ANTERIOR")):
            descartadas += 1
            continue
        if not re.match(r"^\d{4,}", cuenta):
            continue
        d, c = monto(f[cdb]), monto(f[ccr])
        td += d
        tc += c
        neto[cuenta] += d - c
        if cn is None:
            continue
        ter_raw = str(f[cn] or "").strip()
        nom = str(f[cnom] or "") if cnom is not None else ""
        ter = solo_digitos(ter_raw.split("-")[0])
        if not ter:
            hallazgos.append([i, cuenta, ter_raw, nom, d - c, "Movimiento sin tercero", "Bloqueante"])
            continue
        if ter in NIT_GENERICOS or GENERICOS.search(nom):
            hallazgos.append([i, cuenta, ter_raw, nom, d - c, "Tercero genérico", "Bloqueante"])
        if nit_emp and ter[:9] == nit_emp and cuenta[:1] in "4567":
            hallazgos.append([i, cuenta, ter_raw, nom, d - c, "NIT de la propia empresa como tercero de resultados", "Revisar"])
        if "-" in ter_raw:
            base, dv_dado = ter_raw.split("-")[0], ter_raw.split("-")[-1].strip()
            base = solo_digitos(base)
            if base and base[:1] in "89" and len(base) == 9 and dv_dado != dv(base):
                hallazgos.append([i, cuenta, ter_raw, nom, d - c, f"DV mal calculado (correcto: {dv(base)})", "Bloqueante"])
            elif base and not (base[:1] in "89" and len(base) == 9):
                hallazgos.append([i, cuenta, ter_raw, nom, d - c, "Cédula registrada con dígito de verificación", "Bloqueante"])

    contrarias = []
    for cuenta, v in sorted(neto.items()):
        n = naturaleza(cuenta)
        if (n == "D" and v < -0.5) or (n == "C" and v > 0.5):
            contrarias.append([cuenta, v, "Movimiento neto del período contrario a la naturaleza: explicar o proponer ajuste"])

    descuadre = round(td - tc, 2)
    if a.salida:
        wb = libro_salida()
        hoja(wb, "RESUMEN", ["Control", "Resultado"], [
            ["Filas descartadas (TOTAL / saldo inicial)", descartadas], ["Total débitos", round(td, 2)], ["Total créditos", round(tc, 2)],
            ["Diferencia débitos − créditos (debe ser 0)", descuadre], ["Hallazgos de terceros", len(hallazgos)],
            ["Cuentas con movimiento contrario a la naturaleza", len(contrarias)]], [52, 20], columnas_moneda={1})
        hoja(wb, "TERCEROS", ["Fila", "Cuenta", "Tercero", "Nombre", "Valor", "Hallazgo", "Severidad"], hallazgos,
             [6, 12, 16, 32, 16, 46, 12], columnas_moneda={4})
        hoja(wb, "NATURALEZA", ["Cuenta", "Movimiento neto", "Qué hacer"], contrarias, [14, 18, 70], columnas_moneda={1})
        Path(a.salida).parent.mkdir(parents=True, exist_ok=True)
        wb.save(a.salida)
    print(f"Filas descartadas (TOTAL/saldo inicial): {descartadas}")
    print(f"Débitos {pesos(td)} · créditos {pesos(tc)} · diferencia {pesos(descuadre)}")
    print(f"Hallazgos de terceros: {len(hallazgos)} · cuentas con movimiento contrario: {len(contrarias)}")
    for h in hallazgos[:40]:
        print(f"   fila {h[0]:>5}  {h[1]:10} {h[2]:16} {h[5]}")
    for c in contrarias[:20]:
        print(f"   cuenta {c[0]:10} neto {pesos(c[1])}")
    bloquea = abs(descuadre) > 0.01 or any(h[6] == "Bloqueante" for h in hallazgos)
    print("AUXILIAR APTO PARA CRUCES" if not bloquea else "CORREGIR EN EL SOFTWARE Y RE-EXPORTAR ANTES DE CRUZAR")
    return 2 if bloquea else 0


if __name__ == "__main__":
    sys.exit(main())
