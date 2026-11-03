#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conciliación bancaria con el método de la firma: cuadre agregado por sentido mes a mes, cruce 1-1 y cruces
uno-a-varios / varios-a-uno (subset-sum) sobre lo que sobra. Entrega el Excel en formato contable con
diferencia CERO o dice exactamente qué falta.

    python herramientas/conciliar_1aN.py --extracto EXTRACTO.xlsx --libro AUX_1110.xlsx \\
        --saldo-extracto 46142000 --saldo-libros 45950000 --salida "02-PROCESADO/02_CONCILIACIONES_2026-01.xlsx"

Entradas (CSV o XLSX), columnas detectadas por nombre:
  extracto: fecha · descripción · valor (con signo: + abono, − cargo)  [o columnas separadas débito/crédito o cargos/abonos]
  libro   : fecha · documento/comprobante · descripción · débito · crédito  (movimientos de la cuenta de banco)
Convención: un ABONO del banco corresponde a un DÉBITO en libros; un CARGO del banco a un CRÉDITO en libros.

Parámetros: --dias (ventana de fecha, por defecto 6) · --tolerancia (pesos, por defecto 1) · --max-grupo (hasta cuántos
movimientos combinar, por defecto 5) · --hoja-extracto / --hoja-libro.
"""
from __future__ import annotations

import argparse
import itertools
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from comun import buscar_col, fecha, hoja, leer_tabla, libro_salida, monto, pesos  # noqa: E402


@dataclass
class Mov:
    origen: str          # "banco" | "libro"
    idx: int
    fecha: object
    desc: str
    valor: float         # con signo: + entra dinero, − sale dinero (visto desde el banco)
    doc: str = ""
    cruce: str = ""      # id del cruce
    capa: str = ""


def cargar_extracto(ruta, hoja_=None) -> list[Mov]:
    enc, filas = leer_tabla(ruta, hoja_, buscar_encabezado=("fecha",))
    cf = buscar_col(enc, "fecha")
    cd = buscar_col(enc, "descripcion", "concepto", "detalle", "referencia", obligatorio=False)
    cv = buscar_col(enc, "valor", "monto", "importe", obligatorio=False)
    ca = buscar_col(enc, "abono", "credito", "creditos", "abonos", "ingreso", obligatorio=False)
    cc = buscar_col(enc, "cargo", "debito", "debitos", "cargos", "egreso", obligatorio=False)
    movs = []
    for i, f in enumerate(filas):
        d = fecha(f[cf])
        if d is None:
            continue
        if cv is not None and (ca is None or cc is None):
            v = monto(f[cv])
        else:
            v = monto(f[ca]) - abs(monto(f[cc]))
        if abs(v) < 0.005:
            continue
        movs.append(Mov("banco", i, d, str(f[cd] if cd is not None else ""), round(v, 2)))
    return movs


def cargar_libro(ruta, hoja_=None) -> list[Mov]:
    enc, filas = leer_tabla(ruta, hoja_, buscar_encabezado=("fecha",))
    cf = buscar_col(enc, "fecha")
    cdoc = buscar_col(enc, "documento", "comprobante", "doc", "numero", obligatorio=False)
    cd = buscar_col(enc, "descripcion", "concepto", "detalle", "nota", obligatorio=False)
    cdb = buscar_col(enc, "debito", "debitos", "debe")
    ccr = buscar_col(enc, "credito", "creditos", "haber")
    movs = []
    for i, f in enumerate(filas):
        desc = str(f[cd] if cd is not None else "")
        if desc.upper().startswith(("SALDO INICIAL", "TOTAL", "SALDO ANTERIOR")):
            continue
        d = fecha(f[cf])
        if d is None:
            continue
        v = monto(f[cdb]) - monto(f[ccr])
        if abs(v) < 0.005:
            continue
        movs.append(Mov("libro", i, d, desc, round(v, 2), str(f[cdoc] if cdoc is not None else "")))
    return movs


def agregado_por_sentido(banco: list[Mov], libro: list[Mov]) -> list[list]:
    acc = defaultdict(lambda: [0.0, 0.0, 0.0, 0.0])
    for m in banco:
        k = m.fecha.strftime("%Y-%m")
        acc[k][0 if m.valor > 0 else 2] += abs(m.valor)
    for m in libro:
        k = m.fecha.strftime("%Y-%m")
        acc[k][1 if m.valor > 0 else 3] += abs(m.valor)
    filas = []
    for k in sorted(acc):
        ab, db, cg, cr = acc[k]
        filas.append([k, round(ab, 2), round(db, 2), round(ab - db, 2), round(cg, 2), round(cr, 2), round(cg - cr, 2)])
    return filas


def conciliar(banco: list[Mov], libro: list[Mov], dias: int = 6, tol: float = 1.0, max_grupo: int = 5) -> list[tuple]:
    cruces = []
    n = 0
    # Capa 1: uno a uno (mismo valor, fecha cercana); se prefiere la fecha más cercana
    libres_l = [m for m in libro]
    for b in sorted(banco, key=lambda m: m.fecha):
        cand = [l for l in libres_l if not l.cruce and abs(l.valor - b.valor) <= tol and abs((l.fecha - b.fecha).days) <= dias]
        if cand:
            l = min(cand, key=lambda x: abs((x.fecha - b.fecha).days))
            n += 1
            b.cruce = l.cruce = f"C{n:04d}"
            b.capa = l.capa = "1 · uno a uno"
            cruces.append((b.cruce, b.capa, [b], [l]))

    # Capa 3: uno a varios y varios a uno (subset-sum sobre residuales del mismo sentido)
    def buscar(objetivo: Mov, pool: list[Mov]):
        cand = [m for m in pool if not m.cruce and (m.valor > 0) == (objetivo.valor > 0)
                and abs((m.fecha - objetivo.fecha).days) <= max(dias, 31) and abs(m.valor) <= abs(objetivo.valor) + tol]
        cand.sort(key=lambda m: abs((m.fecha - objetivo.fecha).days))
        cand = cand[:22]
        for r in range(2, min(max_grupo, len(cand)) + 1):
            for comb in itertools.combinations(cand, r):
                if abs(sum(m.valor for m in comb) - objetivo.valor) <= tol:
                    return list(comb)
        return None

    for l in sorted([m for m in libro if not m.cruce], key=lambda m: -abs(m.valor)):
        if l.cruce:
            continue
        comb = buscar(l, banco)
        if comb:
            n += 1
            for m in comb + [l]:
                m.cruce, m.capa = f"C{n:04d}", "3 · varios del banco = uno del libro"
            cruces.append((l.cruce, l.capa, comb, [l]))
    for b in sorted([m for m in banco if not m.cruce], key=lambda m: -abs(m.valor)):
        if b.cruce:
            continue
        comb = buscar(b, libro)
        if comb:
            n += 1
            for m in comb + [b]:
                m.cruce, m.capa = f"C{n:04d}", "3 · varios del libro = uno del banco"
            cruces.append((b.cruce, b.capa, [b], comb))
    return cruces


def clasificar(m: Mov) -> str:
    d = m.desc.upper()
    if m.origen == "banco":
        if any(k in d for k in ("4X1000", "GMF", "GRAVAMEN", "IMPTO GOBIERNO")):
            return "Cargo del banco no registrado: GMF (causar)"
        if any(k in d for k in ("COMISION", "CUOTA DE MANEJO", "CUOTA MANEJO", "IVA COMISION", "PORTES")):
            return "Cargo del banco no registrado: comisión o cuota de manejo (causar)"
        if any(k in d for k in ("INTERES", "RENDIMIENTO")) and m.valor > 0:
            return "Abono del banco no registrado: rendimientos (causar)"
        return "Abono del banco no registrado: investigar con cartera antes de causar" if m.valor > 0 else "Cargo del banco no registrado: identificar soporte"
    if m.valor < 0:
        return "Registrado en libros, no en el banco: cheque o transferencia girada no cobrada (controlar)"
    return "Registrado en libros, no en el banco: consignación en tránsito (controlar)"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--extracto", required=True)
    ap.add_argument("--libro", required=True)
    ap.add_argument("--saldo-extracto", type=float, required=True)
    ap.add_argument("--saldo-libros", type=float, required=True)
    ap.add_argument("--salida", required=True)
    ap.add_argument("--cuenta", default="Cuenta bancaria")
    ap.add_argument("--dias", type=int, default=6)
    ap.add_argument("--tolerancia", type=float, default=1.0)
    ap.add_argument("--max-grupo", type=int, default=5)
    ap.add_argument("--hoja-extracto")
    ap.add_argument("--hoja-libro")
    a = ap.parse_args(argv)

    banco = cargar_extracto(a.extracto, a.hoja_extracto)
    libro = cargar_libro(a.libro, a.hoja_libro)
    agregado = agregado_por_sentido(banco, libro)
    cruces = conciliar(banco, libro, a.dias, a.tolerancia, a.max_grupo)
    sin_b = [m for m in banco if not m.cruce]
    sin_l = [m for m in libro if not m.cruce]

    # Formato contable: saldo libros + (abonos banco no registrados) − (cargos banco no registrados)
    #                   − (débitos libro no en banco) + (créditos libro no en banco) = saldo extracto
    ab_nr = sum(m.valor for m in sin_b if m.valor > 0)
    cg_nr = -sum(m.valor for m in sin_b if m.valor < 0)
    db_nb = sum(m.valor for m in sin_l if m.valor > 0)
    cr_nb = -sum(m.valor for m in sin_l if m.valor < 0)
    calculado = a.saldo_libros + ab_nr - cg_nr - db_nb + cr_nb
    diferencia = round(calculado - a.saldo_extracto, 2)

    wb = libro_salida()
    formato = [["Saldo según libros", a.saldo_libros],
               ["(+) Abonos del banco no registrados en libros", ab_nr],
               ["(−) Cargos del banco no registrados en libros", -cg_nr],
               ["(−) Débitos en libros que el banco no refleja (consignaciones en tránsito)", -db_nb],
               ["(+) Créditos en libros que el banco no refleja (cheques/transferencias no cobrados)", cr_nb],
               ["= Saldo conciliado", round(calculado, 2)],
               ["Saldo según extracto", a.saldo_extracto],
               ["DIFERENCIA (debe ser 0)", diferencia]]
    hoja(wb, "CONCILIACION", ["Concepto", "Valor"], formato, [70, 20], subtitulo=a.cuenta, columnas_moneda={1})
    hoja(wb, "PARTIDAS CONCILIATORIAS", ["Origen", "Fecha", "Documento", "Descripción", "Valor", "Clasificación y tratamiento"],
         [[m.origen, m.fecha, m.doc, m.desc, m.valor, clasificar(m)] for m in sin_b + sin_l],
         [8, 11, 14, 40, 16, 60], columnas_moneda={4}, fila_total=True)
    filas_c = []
    for cid, capa, bs, ls in cruces:
        for m in bs + ls:
            filas_c.append([cid, capa, m.origen, m.fecha, m.doc, m.desc, m.valor])
    hoja(wb, "CRUCES CONFIRMADOS", ["Cruce", "Capa", "Origen", "Fecha", "Documento", "Descripción", "Valor"], filas_c,
         [8, 32, 8, 11, 14, 40, 16], columnas_moneda={6})
    hoja(wb, "CUADRE POR SENTIDO", ["Mes", "Abonos banco", "Débitos libros", "Dif. entradas", "Cargos banco", "Créditos libros", "Dif. salidas"],
         agregado, [10, 16, 16, 16, 16, 16, 16], subtitulo="Capa 0: si cada sentido cuadra, el mes está cerrado", columnas_moneda={1, 2, 3, 4, 5, 6})
    Path(a.salida).parent.mkdir(parents=True, exist_ok=True)
    wb.save(a.salida)

    print(f"Movimientos: banco {len(banco)} · libros {len(libro)} · cruces {len(cruces)} "
          f"(1-1: {sum(1 for c in cruces if c[1].startswith('1'))}, 1-a-N: {sum(1 for c in cruces if c[1].startswith('3'))})")
    print(f"Partidas conciliatorias: {len(sin_b) + len(sin_l)}")
    for m in sin_b + sin_l:
        print(f"   {m.origen:5} {m.fecha} {m.doc:10} {m.desc[:38]:38} {pesos(m.valor):>16}  {clasificar(m)}")
    print(f"Saldo conciliado {pesos(calculado)} vs extracto {pesos(a.saldo_extracto)} → diferencia {pesos(diferencia)}")
    print("CONCILIACIÓN CERRADA" if abs(diferencia) < 0.01 else "NO CIERRA: faltan cruces o hay un saldo mal digitado")
    print(f"Excel: {a.salida}")
    return 0 if abs(diferencia) < 0.01 else 2


if __name__ == "__main__":
    sys.exit(main())
