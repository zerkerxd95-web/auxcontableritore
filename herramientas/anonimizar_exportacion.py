#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anonimizador de exportación — Política de Separación de Datos y Confidencialidad (§2 y §4).

Copia un árbol de notas/archivos de texto aplicando un MAPA de anonimización
(nombre real → descriptor genérico estable) que vive FUERA del repositorio.

Uso:
    python anonimizar_exportacion.py --mapa ../_ROJO-NO-SUBIR/mapa-anonimizacion.json \
        --origen "RUTA/AL/VAULT/03 - Skills" --destino "RUTA/EXPORT/03 - Skills"

Formato del mapa (JSON):
    {
      "reglas": [ {"patron": "<regex>", "reemplazo": "<texto>", "flags": "cs"?}, ... ],
      "nits_permitidos": ["800.197.268", ...],
      "wikilinks_a_texto": ["Cliente - ", "AVANCE_"]
    }

Qué hace, en orden, sobre cada archivo de texto (.md, .txt, .json, .yaml, .py, .html, .js, .css, .sql, .ps1, .sh, .csv):
  1. Aplica las reglas del mapa (regex, sin distinguir mayúsculas salvo flags "cs").
  2. Sustituye NIT reales (patrón 8xx/9xx.xxx.xxx con DV o precedido de "NIT") por 900.000.000-1,
     salvo los de la lista `nits_permitidos` (entidades públicas y ficticios).
  3. Sustituye cédulas precedidas de "C.C."/"cédula" por un número ficticio.
  4. Convierte en texto plano los wikilinks que apunten a material ROJO (prefijos en `wikilinks_a_texto`).
  5. Sustituye correos electrónicos por <correo>.
Los archivos binarios (xlsx, pdf, png, ttf, …) se copian tal cual: el usuario debe verificar que no contengan datos reales.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

EXT_TEXTO = {".md", ".txt", ".json", ".yaml", ".yml", ".py", ".html", ".htm", ".js", ".css",
             ".sql", ".ps1", ".sh", ".csv", ".webmanifest", ".mjs", ".xml", ".canvas"}

RX_NIT_DV = re.compile(r"\b([89]\d{2})\.(\d{3})\.(\d{3})-(\d)\b")
RX_NIT_CTX = re.compile(r"(NIT[:\s]*N?[°º]?\s*)([89]\d{2}\.\d{3}\.\d{3}|[89]\d{8})(-\d)?", re.IGNORECASE)
RX_CEDULA = re.compile(r"(C\.?C\.?\s*N?[°º]?\s*|c[ée]dula\s*(?:de ciudadan[ií]a)?\s*N?[°º]?\s*)(\d{1,2}\.?\d{3}\.?\d{3}|\d{7,10})", re.IGNORECASE)
RX_EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def _lp(p: Path) -> Path:
    """Ruta larga en Windows (prefijo ``\\\\?\\``) para superar el límite de 260 caracteres."""
    if os.name == "nt":
        s = str(p.resolve())
        if not s.startswith("\\\\?\\"):
            return Path("\\\\?\\" + s)
    return p


def cargar_mapa(ruta: Path) -> dict:
    with open(ruta, encoding="utf-8") as f:
        mapa = json.load(f)
    reglas = []
    for r in mapa.get("reglas", []):
        flags = 0 if r.get("flags") == "cs" else re.IGNORECASE
        reglas.append((re.compile(r["patron"], flags), r["reemplazo"]))
    mapa["_compiladas"] = reglas
    mapa.setdefault("nits_permitidos", [])
    mapa.setdefault("wikilinks_a_texto", [])
    return mapa


def _nit_permitido(nit: str, permitidos: list[str]) -> bool:
    base = nit.replace(".", "")[:9]
    return any(p.replace(".", "")[:9] == base for p in permitidos)


def anonimizar_texto(texto: str, mapa: dict, permitir_correos: bool = False) -> tuple[str, int]:
    """Devuelve (texto_anonimizado, numero_de_sustituciones)."""
    n = 0
    for rx, rep in mapa["_compiladas"]:
        texto, k = rx.subn(rep, texto)
        n += k

    permitidos = mapa["nits_permitidos"]

    def _sub_nit_dv(m):
        nonlocal n
        nit = f"{m.group(1)}.{m.group(2)}.{m.group(3)}"
        if _nit_permitido(nit, permitidos):
            return m.group(0)
        n += 1
        return "900.000.000-1"

    texto = RX_NIT_DV.sub(_sub_nit_dv, texto)

    def _sub_nit_ctx(m):
        nonlocal n
        if _nit_permitido(m.group(2), permitidos):
            return m.group(0)
        n += 1
        return f"{m.group(1)}900.000.000-1"

    texto = RX_NIT_CTX.sub(_sub_nit_ctx, texto)

    def _sub_cedula(m):
        nonlocal n
        n += 1
        return f"{m.group(1)}1.000.000.000"

    texto = RX_CEDULA.sub(_sub_cedula, texto)

    # Wikilinks a material ROJO → texto plano
    prefijos = mapa["wikilinks_a_texto"]
    if prefijos:
        def _sub_link(m):
            nonlocal n
            destino, alias = m.group(1), m.group(3)
            if any(destino.startswith(p) for p in prefijos):
                n += 1
                return f"**{alias or destino}**"
            return m.group(0)
        texto = re.sub(r"\[\[([^\]|#]+)(#[^\]|]+)?(?:\|([^\]]+))?\]\]", _sub_link, texto)

    if not permitir_correos:
        texto, k = RX_EMAIL.subn("<correo>", texto)
        n += k
    return texto, n


def anonimizar_arbol(origen: Path, destino: Path, mapa: dict, excluir: set[str] | None = None,
                     permitir_correos: bool = False, verbose: bool = True) -> dict:
    """Copia origen → destino anonimizando archivos de texto. Devuelve estadísticas."""
    excluir = excluir or set()
    stats = {"archivos": 0, "texto": 0, "binarios": 0, "sustituciones": 0, "excluidos": 0}
    for raiz, dirs, archivos in os.walk(origen):
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules", "__pycache__", ".venv", "vendor"}]
        for nombre in archivos:
            src = Path(raiz) / nombre
            rel = src.relative_to(origen)
            if str(rel).replace("\\", "/") in excluir or nombre.startswith(".~lock") or nombre.endswith(".pyc"):
                stats["excluidos"] += 1
                continue
            dst = destino / rel
            _lp(dst.parent).mkdir(parents=True, exist_ok=True)
            src, dst = _lp(src), _lp(dst)
            stats["archivos"] += 1
            if src.suffix.lower() in EXT_TEXTO:
                try:
                    texto = src.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    texto = src.read_text(encoding="latin-1")
                nuevo, k = anonimizar_texto(texto, mapa, permitir_correos)
                dst.write_text(nuevo, encoding="utf-8", newline="\n")
                stats["texto"] += 1
                stats["sustituciones"] += k
                if verbose and k:
                    print(f"  [{k:4d}] {rel}")
            else:
                shutil.copy2(src, dst)
                stats["binarios"] += 1
    return stats


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mapa", required=True, help="JSON con las reglas (vive FUERA del repo)")
    ap.add_argument("--origen", required=True)
    ap.add_argument("--destino", required=True)
    ap.add_argument("--excluir", nargs="*", default=[], help="rutas relativas a omitir")
    ap.add_argument("--permitir-correos", action="store_true")
    ap.add_argument("--silencioso", action="store_true")
    a = ap.parse_args(argv)
    mapa = cargar_mapa(Path(a.mapa))
    stats = anonimizar_arbol(Path(a.origen), Path(a.destino), mapa, set(a.excluir), a.permitir_correos, not a.silencioso)
    print(json.dumps(stats, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
