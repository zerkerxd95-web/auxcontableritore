# -*- coding: utf-8 -*-
"""Utilidades compartidas por las herramientas del auxiliar: lectura de tablas, montos, NIT/DV y Excel de salida
con la paleta Ritoré (negro #231F20, dorado #F0BB25, blanco)."""
from __future__ import annotations

import csv
import re
import unicodedata
from datetime import date, datetime
from pathlib import Path

TINTA, ORO, ORO_SUAVE, SUAVE, GRIS = "231F20", "F0BB25", "FDF3DD", "F7F5F1", "5F5C5D"
MONEDA = '#,##0.##;[Red]-#,##0.##'   # regla de la firma: nunca #,##0 (los centavos de un ajuste no se pueden perder)


# ---------------------------------------------------------------- texto y columnas
def norm(s) -> str:
    s = "" if s is None else str(s)
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def buscar_col(encabezados: list[str], *candidatos: str, obligatorio: bool = True) -> int | None:
    """Índice de la primera columna cuyo encabezado normalizado contiene alguno de los candidatos."""
    en = [norm(h) for h in encabezados]
    for c in candidatos:
        c = norm(c)
        for i, h in enumerate(en):
            if h == c:
                return i
    for c in candidatos:
        c = norm(c)
        for i, h in enumerate(en):
            if c and c in h:
                return i
    if obligatorio:
        raise KeyError(f"No encontré ninguna columna parecida a {candidatos} en {encabezados}")
    return None


def leer_tabla(ruta: str | Path, hoja: str | None = None, buscar_encabezado: tuple[str, ...] = ()) -> tuple[list[str], list[list]]:
    """Lee CSV o XLSX. Si se dan palabras en `buscar_encabezado`, toma como encabezado la primera fila que las contenga."""
    ruta = Path(ruta)
    if ruta.suffix.lower() in (".csv", ".txt"):
        texto = ruta.read_text(encoding="utf-8-sig", errors="replace")
        dialecto = csv.Sniffer().sniff(texto[:4000], delimiters=";,\t|")
        filas = [r for r in csv.reader(texto.splitlines(), dialecto)]
    else:
        import openpyxl
        wb = openpyxl.load_workbook(ruta, read_only=True, data_only=True)
        ws = wb[hoja] if hoja else wb.worksheets[0]
        filas = [list(r) for r in ws.iter_rows(values_only=True)]
        wb.close()
    inicio = 0
    if buscar_encabezado:
        for i, f in enumerate(filas[:60]):
            t = " ".join(norm(x) for x in f if x is not None)
            if all(norm(p) in t for p in buscar_encabezado):
                inicio = i
                break
    enc = ["" if x is None else str(x).strip() for x in filas[inicio]]
    datos = [f for f in filas[inicio + 1:] if any(x not in (None, "") for x in f)]
    return enc, datos


# ---------------------------------------------------------------- números y fechas
def monto(v) -> float:
    """Convierte '1.234.567,89', '1,234,567.89', '(1.000)', '$ 2.500' o números a float."""
    if v is None or v == "":
        return 0.0
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace("$", "").replace(" ", "")
    neg = s.startswith("(") and s.endswith(")") or s.startswith("-")
    s = s.strip("()-")
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".") if s.rfind(",") > s.rfind(".") else s.replace(",", "")
    elif "," in s:
        partes = s.split(",")
        s = s.replace(",", ".") if len(partes[-1]) != 3 else s.replace(",", "")
    elif s.count(".") > 1 or (s.count(".") == 1 and len(s.split(".")[-1]) == 3):
        s = s.replace(".", "")
    try:
        x = float(s)
    except ValueError:
        return 0.0
    return -x if neg else x


def fecha(v) -> date | None:
    if v is None or v == "":
        return None
    if isinstance(v, datetime):
        return v.date()
    if isinstance(v, date):
        return v
    s = str(v).strip()[:10]
    for f in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%Y/%m/%d", "%d/%m/%y"):
        try:
            return datetime.strptime(s, f).date()
        except ValueError:
            pass
    return None


def pesos(x: float) -> str:
    s = f"{abs(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    s = s[:-3] if s.endswith(",00") else s
    return ("-$" if x < 0 else "$") + s


# ---------------------------------------------------------------- NIT y DV (Orden Administrativa 4 de 1989)
PESOS_DV = [3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71]


def dv(nit) -> str:
    d = "".join(c for c in str(nit) if c.isdigit())
    if not d:
        return ""
    s = sum(int(c) * PESOS_DV[i] for i, c in enumerate(reversed(d)) if i < len(PESOS_DV))
    r = s % 11
    return str(r if r < 2 else 11 - r)


def solo_digitos(x) -> str:
    return "".join(c for c in str(x or "") if c.isdigit())


# ---------------------------------------------------------------- Excel de salida
def libro_salida():
    import openpyxl
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    return wb


def hoja(wb, titulo: str, encabezados: list[str], filas: list[list], anchos: list[int] | None = None,
         subtitulo: str = "", columnas_moneda: set[int] | None = None, fila_total: bool = False):
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
    ws = wb.create_sheet(titulo[:31])
    ws.sheet_view.showGridLines = False
    linea = Side(style="thin", color="CFCDCE")
    borde = Border(left=linea, right=linea, top=linea, bottom=linea)
    n = max(1, len(encabezados))
    ws.cell(1, 1, "RITORÉ ASESORÍAS CONTABLES").font = Font(name="Calibri", size=9, bold=True, color=GRIS)
    ws.cell(2, 1, titulo).font = Font(name="Calibri", size=13, bold=True, color=TINTA)
    if subtitulo:
        ws.cell(3, 1, subtitulo).font = Font(name="Calibri", size=10, color=GRIS)
    for c in range(1, n + 1):
        ws.cell(3, c).border = Border(bottom=Side(style="medium", color=ORO))
    r0 = 5
    for i, h in enumerate(encabezados, 1):
        c = ws.cell(r0, i, h)
        c.font = Font(name="Calibri", size=9, bold=True, color=ORO)
        c.fill = PatternFill("solid", fgColor=TINTA)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = borde
    columnas_moneda = columnas_moneda or set()
    for j, fila in enumerate(filas, r0 + 1):
        for i, v in enumerate(fila, 1):
            c = ws.cell(j, i, v)
            c.border = borde
            c.font = Font(name="Calibri", size=9, color=TINTA)
            if (i - 1) in columnas_moneda and isinstance(v, (int, float)):
                c.number_format = MONEDA
    if fila_total and filas:
        t = r0 + len(filas) + 1
        ws.cell(t, 1, "TOTAL").font = Font(bold=True, color=TINTA)
        for i in columnas_moneda:
            col = get_column_letter(i + 1)
            c = ws.cell(t, i + 1, f"=SUM({col}{r0 + 1}:{col}{t - 1})")
            c.number_format = MONEDA
            c.font = Font(bold=True, color=TINTA)
        for i in range(1, n + 1):
            ws.cell(t, i).fill = PatternFill("solid", fgColor=ORO_SUAVE)
            ws.cell(t, i).border = borde
    for i in range(1, n + 1):
        ws.column_dimensions[get_column_letter(i)].width = (anchos[i - 1] if anchos and i - 1 < len(anchos) else 16)
    ws.freeze_panes = ws.cell(r0 + 1, 1)
    return ws
