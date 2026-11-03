#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anonimiza el TEXTO de libros Excel (.xlsx) sin tocar nunca los valores numéricos.

    python herramientas/anonimizar_xlsx.py --mapa ../_ROJO-NO-SUBIR/mapa-anonimizacion.json RUTA [RUTA ...]

Solo se procesan:
  - xl/sharedStrings.xml: el contenido de cada <t>…</t>
  - xl/worksheets/*.xml: cadenas en línea (<is><t>…</t></is>) y celdas de fórmula con resultado texto (t="str")
  - comentarios, títulos de gráficos, cuadros de texto y la caché de etiquetas de los gráficos (<c:pt><c:v>texto)
Nunca se modifican los <v> numéricos: un resultado de fórmula de diez cifras que empieza por 3 o un NIT guardado como número
pueden parecer un celular o un NIT y el reemplazo dañaría el libro (lección del 3-nov-2026).
Si un NIT real está guardado como número, el script lo REPORTA para corregirlo a mano en la plantilla.
"""
from __future__ import annotations

import argparse
import html
import re
import shutil
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from anonimizar_exportacion import anonimizar_texto, cargar_mapa  # noqa: E402

RX_T = re.compile(r"(<(?:a:)?t(?:\s[^>]*)?>)([^<]*)(</(?:a:)?t>)")
RX_STR = re.compile(r'(<c [^>]*\bt="str"[^>]*>(?:<f[^>]*>.*?</f>|<f[^>]*/>)?<v>)([^<]*)(</v>)', re.S)
RX_PT = re.compile(r"(<(?:c:)?pt [^>]*>\s*<(?:c:)?v>)([^<]*)(</(?:c:)?v>)")   # caché de etiquetas de los gráficos
RX_NUM = re.compile(r'<c ([^>]*)>(?:<f[^>]*>.*?</f>|<f[^>]*/>)?<v>([^<]*)</v>', re.S)


def _anon(fragmento: str, mapa) -> tuple[str, int]:
    plano = html.unescape(fragmento)
    nuevo, k = anonimizar_texto(plano, mapa, permitir_correos=True)
    if not k:
        return fragmento, 0
    return html.escape(nuevo, quote=False), k


def procesar_xml(nombre: str, s: str, mapa, nits_reales: set[str]) -> tuple[str, int, list[str]]:
    total, avisos = 0, []

    def sub(m):
        nonlocal total
        nuevo, k = _anon(m.group(2), mapa)
        total += k
        return m.group(1) + nuevo + m.group(3)

    s = RX_T.sub(sub, s)
    if nombre.startswith("xl/charts/"):
        def sub_pt(m):
            try:
                float(m.group(2))
                return m.group(0)          # valor numérico de la serie: no se toca
            except ValueError:
                return sub(m)
        s = RX_PT.sub(sub_pt, s)
    if nombre.startswith("xl/worksheets/"):
        s = RX_STR.sub(sub, s)
        for m in RX_NUM.finditer(s):
            attrs, v = m.group(1), m.group(2)
            if re.search(r'\bt="(?:s|str|inlineStr|e|b)"', attrs):
                continue
            if v.split(".")[0] in nits_reales:
                ref = re.search(r'r="([A-Z]+\d+)"', attrs)
                avisos.append(f"{nombre} {ref.group(1) if ref else '?'}: NIT real guardado como número ({v})")
    return s, total, avisos


def anonimizar_libro(path: Path, mapa, nits_reales: set[str]) -> tuple[int, list[str]]:
    total, avisos, partes = 0, [], []
    with zipfile.ZipFile(path) as zin:
        for info in zin.infolist():
            data = zin.read(info.filename)
            n = info.filename
            if n.endswith(".xml") and (n == "xl/sharedStrings.xml" or n.startswith(("xl/worksheets/", "xl/comments", "xl/charts/", "xl/drawings/"))):
                s, k, av = procesar_xml(n, data.decode("utf-8"), mapa, nits_reales)
                total += k
                avisos += av
                data = s.encode("utf-8")
            partes.append((info, data))
    if total:
        tmp = path.with_suffix(".tmp")
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
            for info, data in sorted(partes, key=lambda x: x[0].filename != "[Content_Types].xml"):
                zout.writestr(info, data)
        shutil.move(tmp, path)
    return total, avisos


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mapa", required=True)
    ap.add_argument("--nits", help="archivo de texto con NIT reales (uno por línea) para reportar los guardados como número")
    ap.add_argument("rutas", nargs="+")
    a = ap.parse_args(argv)
    mapa = cargar_mapa(Path(a.mapa))
    nits = set()
    if a.nits:
        nits = {re.sub(r"\D", "", x) for x in Path(a.nits).read_text(encoding="utf-8").splitlines() if re.fullmatch(r"[\d.]{9,11}", x.strip())}
    libros = []
    for r in a.rutas:
        p = Path(r)
        libros += sorted(p.rglob("*.xlsx")) if p.is_dir() else [p]
    avisos_tot = []
    for p in libros:
        k, av = anonimizar_libro(p, mapa, nits)
        avisos_tot += [f"{p}: {x}" for x in av]
        if k:
            print(f"  {p}: {k} textos anonimizados")
    for x in avisos_tot:
        print("  AVISO", x)
    return 1 if avisos_tot else 0


if __name__ == "__main__":
    sys.exit(main())
