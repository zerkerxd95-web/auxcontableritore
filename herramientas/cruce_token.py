#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cruce del token DIAN contra la contabilidad, documento por documento y en los dos sentidos.

    python herramientas/cruce_token.py --token TOKEN_2026-01.xlsx --libro AUX_2026-01.xlsx \\
        --nit-empresa 900123456 --salida "02-PROCESADO/01_CRUCE_TOKEN_2026-01.xlsx"

Token (export de la DIAN, CSV o XLSX): columnas detectadas por nombre — tipo de documento, prefijo, folio,
fecha de emisión, NIT emisor, nombre emisor, NIT receptor, nombre receptor, IVA, total.
Libro: una fila por documento causado — documento (prefijo+folio, p. ej. "SETP-1043" o "FE 1043"), fecha, NIT tercero,
valor total del documento (o base + IVA). Sirve el resumen por documento que exporta el software (balance de comprobantes)
o una tabla armada a partir del auxiliar.

Reglas: tolerancia ±$200 por documento (redondeos); los emitidos por la empresa son ventas y los recibidos son compras;
la serie de facturas emitidas se revisa para encontrar huecos. Que el total cuadre no prueba nada: la herramienta
reporta cada documento sin pareja.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from comun import buscar_col, fecha, hoja, leer_tabla, libro_salida, monto, norm, pesos, solo_digitos  # noqa: E402

TOL = 200.0


def clave(prefijo, folio) -> str:
    p = re.sub(r"[^A-Z0-9]", "", str(prefijo or "").upper())
    f = re.sub(r"\D", "", str(folio or "")).lstrip("0") or "0"
    return f"{p}-{f}"


def clave_desde_texto(doc: str) -> str:
    s = str(doc or "").upper()
    m = re.search(r"([A-Z]{1,6})\s*[-_ ]?\s*0*(\d{1,12})\b", s)
    if m:
        return f"{m.group(1)}-{int(m.group(2))}"
    m = re.search(r"(\d{1,12})", s)
    return f"-{int(m.group(1))}" if m else s


def cargar_token(ruta, hoja_=None):
    enc, filas = leer_tabla(ruta, hoja_, buscar_encabezado=("folio",))
    c = {k: buscar_col(enc, *v, obligatorio=o) for k, v, o in (
        ("tipo", ("tipo de documento", "tipo documento", "tipo"), False),
        ("pref", ("prefijo",), False), ("folio", ("folio", "numero"), True),
        ("fecha", ("fecha emision", "fecha de emision", "fecha"), True),
        ("nit_e", ("nit emisor", "nit del emisor"), True), ("nom_e", ("nombre emisor", "razon social emisor", "emisor"), False),
        ("nit_r", ("nit receptor", "nit del receptor"), True), ("nom_r", ("nombre receptor", "razon social receptor", "receptor"), False),
        ("iva", ("iva",), False), ("total", ("total", "valor total"), True))}
    docs = []
    for f in filas:
        if not f[c["folio"]]:
            continue
        g = lambda k: f[c[k]] if c[k] is not None else ""
        docs.append(dict(tipo=str(g("tipo")), clave=clave(g("pref"), g("folio")), prefijo=str(g("pref") or ""),
                         folio=str(g("folio")), fecha=fecha(g("fecha")), nit_e=solo_digitos(g("nit_e")), nom_e=str(g("nom_e")),
                         nit_r=solo_digitos(g("nit_r")), nom_r=str(g("nom_r")), iva=monto(g("iva")), total=monto(g("total"))))
    return docs


def cargar_libro(ruta, hoja_=None):
    enc, filas = leer_tabla(ruta, hoja_, buscar_encabezado=("documento",))
    cdoc = buscar_col(enc, "documento", "comprobante", "factura", "numero")
    cfe = buscar_col(enc, "fecha", obligatorio=False)
    cnit = buscar_col(enc, "nit", "tercero", "identificacion")
    ctot = buscar_col(enc, "total", "valor total", obligatorio=False)
    cbase = buscar_col(enc, "base", "subtotal", obligatorio=False)
    civa = buscar_col(enc, "iva", obligatorio=False)
    cdesc = buscar_col(enc, "descripcion", "concepto", "detalle", obligatorio=False)
    docs = []
    for f in filas:
        if not f[cdoc]:
            continue
        tot = monto(f[ctot]) if ctot is not None else monto(f[cbase]) + (monto(f[civa]) if civa is not None else 0)
        docs.append(dict(doc=str(f[cdoc]), clave=clave_desde_texto(f[cdoc]), fecha=fecha(f[cfe]) if cfe is not None else None,
                         nit=solo_digitos(f[cnit]), total=abs(tot), desc=str(f[cdesc]) if cdesc is not None else ""))
    return docs


def huecos(folios: list[int]) -> list[int]:
    if not folios:
        return []
    s = set(folios)
    return [x for x in range(min(folios), max(folios) + 1) if x not in s]


def cruzar(token, libro, nit_empresa: str):
    por_clave = defaultdict(list)
    for d in libro:
        por_clave[d["clave"]].append(d)
    filas, sin_libro, dif_valor = [], [], []
    usados = set()
    for t in token:
        sentido = "VENTA (emitido)" if t["nit_e"] == nit_empresa else "COMPRA (recibido)"
        tercero = t["nit_r"] if sentido.startswith("VENTA") else t["nit_e"]
        nombre = t["nom_r"] if sentido.startswith("VENTA") else t["nom_e"]
        cand = [d for d in por_clave.get(t["clave"], []) if not d["nit"] or d["nit"].startswith(tercero[:9]) or tercero.startswith(d["nit"][:9])]
        if not cand:
            # mismo folio, otro formato de prefijo
            folio = t["clave"].split("-")[-1]
            cand = [d for k, v in por_clave.items() if k.split("-")[-1] == folio for d in v if d["nit"][:9] == tercero[:9]]
        cand = [d for d in cand if id(d) not in usados]
        if not cand:
            estado = "EN TOKEN, NO EN LIBROS"
            sin_libro.append(t)
            filas.append([sentido, t["tipo"], t["clave"], t["fecha"], tercero, nombre, t["total"], None, None, estado])
            continue
        d = cand[0]
        usados.add(id(d))
        dif = round(t["total"] - d["total"], 2)
        estado = "OK" if abs(dif) <= TOL else "DIFERENCIA DE VALOR"
        if estado != "OK":
            dif_valor.append((t, d, dif))
        filas.append([sentido, t["tipo"], t["clave"], t["fecha"], tercero, nombre, t["total"], d["total"], dif, estado])
    sin_token = [d for d in libro if id(d) not in usados]
    return filas, sin_libro, dif_valor, sin_token


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--token", required=True)
    ap.add_argument("--libro", required=True)
    ap.add_argument("--nit-empresa", required=True, help="NIT del cliente sin DV")
    ap.add_argument("--salida", required=True)
    ap.add_argument("--hoja-token")
    ap.add_argument("--hoja-libro")
    a = ap.parse_args(argv)
    nit = solo_digitos(a.nit_empresa)[:9]
    token = cargar_token(a.token, a.hoja_token)
    libro = cargar_libro(a.libro, a.hoja_libro)
    filas, sin_libro, dif_valor, sin_token = cruzar(token, libro, nit)

    emitidas = [t for t in token if t["nit_e"] == nit and "nota" not in norm(t["tipo"])]
    por_pref = defaultdict(list)
    for t in emitidas:
        p, f = t["clave"].split("-")
        if f.isdigit():
            por_pref[p].append(int(f))
    faltan = [(p, h) for p, fs in por_pref.items() for h in huecos(fs)]

    wb = libro_salida()
    hoja(wb, "CRUCE", ["Sentido", "Tipo", "Documento", "Fecha", "NIT tercero", "Tercero", "Total token", "Total libros", "Diferencia", "Estado"],
         filas, [16, 18, 14, 11, 14, 32, 16, 16, 14, 24], subtitulo=f"Token vs contabilidad · tolerancia ±${TOL:,.0f} por documento".replace(",", "."),
         columnas_moneda={6, 7, 8})
    hoja(wb, "EN TOKEN NO EN LIBROS", ["Sentido", "Documento", "Fecha", "NIT", "Tercero", "IVA", "Total", "Acción"],
         [["VENTA" if t["nit_e"] == nit else "COMPRA", t["clave"], t["fecha"], t["nit_r"] if t["nit_e"] == nit else t["nit_e"],
           t["nom_r"] if t["nit_e"] == nit else t["nom_e"], t["iva"], t["total"],
           "Causar: afecta ingresos, IVA generado y autorretención" if t["nit_e"] == nit else "Causar: revisar retención (base del día) e IVA descontable"]
          for t in sin_libro], [10, 14, 11, 14, 32, 14, 16, 60], columnas_moneda={5, 6}, fila_total=True)
    hoja(wb, "EN LIBROS NO EN TOKEN", ["Documento", "Fecha", "NIT", "Descripción", "Total", "Acción"],
         [[d["doc"], d["fecha"], d["nit"], d["desc"], d["total"], "Verificar documento soporte o factura no electrónica; si no hay soporte válido: no deducible y sin IVA descontable"]
          for d in sin_token], [16, 11, 14, 40, 16, 70], columnas_moneda={4}, fila_total=True)
    hoja(wb, "DIFERENCIAS DE VALOR", ["Documento", "NIT", "Total token", "Total libros", "Diferencia"],
         [[t["clave"], t["nit_e"] if t["nit_e"] != nit else t["nit_r"], t["total"], d["total"], dif] for t, d, dif in dif_valor],
         [14, 14, 16, 16, 14], columnas_moneda={2, 3, 4})
    hoja(wb, "SERIE SIN HUECOS", ["Prefijo", "Folio faltante en la serie emitida"], [[p, h] for p, h in faltan], [12, 30])
    Path(a.salida).parent.mkdir(parents=True, exist_ok=True)
    wb.save(a.salida)

    ok = sum(1 for f in filas if f[-1] == "OK")
    print(f"Token: {len(token)} documentos · libros: {len(libro)} documentos · OK: {ok}")
    print(f"En token y no en libros: {len(sin_libro)}  · en libros y no en token: {len(sin_token)}  · diferencias de valor: {len(dif_valor)}  · huecos en la serie: {len(faltan)}")
    for t in sin_libro:
        print(f"   TOKEN SIN CAUSAR  {t['clave']:12} {t['fecha']}  {pesos(t['total']):>16}  {(t['nom_r'] if t['nit_e'] == nit else t['nom_e'])[:30]}")
    for d in sin_token:
        print(f"   LIBRO SIN TOKEN   {d['doc']:12} {d['fecha']}  {pesos(d['total']):>16}  {d['desc'][:30]}")
    for t, d, dif in dif_valor:
        print(f"   DIFERENCIA        {t['clave']:12} token {pesos(t['total'])} libros {pesos(d['total'])} → {pesos(dif)}")
    for p, h in faltan:
        print(f"   HUECO EN SERIE    {p}-{h}")
    limpio = not (sin_libro or sin_token or dif_valor or faltan)
    print("CRUCE LIMPIO" if limpio else "CRUCE CON HALLAZGOS: cada uno va a la tabla de diferencias con su acción")
    print(f"Excel: {a.salida}")
    return 0 if limpio else 2


if __name__ == "__main__":
    sys.exit(main())
