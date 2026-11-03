#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Checklist de exportación (Política de Separación de Datos y Confidencialidad §4), automatizado.

Recorre un árbol y reporta todo lo que NO debería salir de la firma:
  - NIT con dígito de verificación o precedido de "NIT" que no esté en la lista de permitidos.
  - Wikilinks a material ROJO ([[Cliente - …]], [[AVANCE_…]]).
  - Credenciales: tokens JWT, claves Supabase (sb_publishable_/sb_secret_/service_role), "password=", claves API.
  - Correos electrónicos y teléfonos celulares colombianos.
  - Opcional: una lista de nombres reales (archivo de texto, un nombre por línea, FUERA del repo).

Uso:
    python verificar_exportacion.py RUTA [--nombres ../_ROJO-NO-SUBIR/nombres.txt] [--permitidos 800.197.268 ...]
Termina con código 1 si encuentra hallazgos (sirve como gate en CI o pre-commit).
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

EXT_TEXTO = {".md", ".txt", ".json", ".yaml", ".yml", ".py", ".html", ".htm", ".js", ".css",
             ".sql", ".ps1", ".sh", ".csv", ".webmanifest", ".mjs", ".xml", ".canvas"}
PERMITIDOS_BASE = ["800.197.268", "900.000.000", "900.123.456", "901.111.222", "222.222.222"]

CHEQUEOS = [
    ("NIT con DV", re.compile(r"\b[89]\d{2}\.\d{3}\.\d{3}-\d\b")),
    ("NIT en contexto", re.compile(r"\bNIT[:\s]*N?[°º]?\s*[89]\d{2}\.?\d{3}\.?\d{3}\b", re.IGNORECASE)),
    ("wikilink ROJO", re.compile(r"\[\[(Cliente - (?!COMERCIALIZADORA EJEMPLO SAS)|AVANCE_)[^\]]*\]\]")),
    ("JWT", re.compile(r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")),
    ("clave Supabase", re.compile(r"sb_(publishable|secret)_[A-Za-z0-9_]{10,}|service_role_key\s*[:=]\s*['\"][^'\"]{8,}")),
    ("password literal", re.compile(r"(password|contrase[ñn]a)\s*[:=]\s*['\"](?![^'\"]*(pass|p@ss|secure|test|123|ejemplo|example|xxx))[^'\"\s]{6,}['\"]", re.IGNORECASE)),
    ("clave API", re.compile(r"\b(sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{30,})\b")),
    ("correo", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")),
    ("celular", re.compile(r"(?<![\d.])3\d{9}(?![\d.])")),
]
CORREOS_PERMITIDOS = {"noreply@anthropic.com", "<correo>"}


def nit_permitido(frag: str, permitidos: list[str]) -> bool:
    digitos = re.sub(r"\D", "", frag)[-10:]
    return any(re.sub(r"\D", "", p) in digitos for p in permitidos)


def verificar(ruta: Path, nombres: list[str], permitidos: list[str]) -> list[tuple[str, str, int, str]]:
    hallazgos = []
    rx_nombres = [re.compile(r"\b" + re.escape(n) + r"\b", re.IGNORECASE) for n in nombres if n.strip()]
    for raiz, dirs, archivos in os.walk(ruta):
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules", "__pycache__", ".venv", "vendor"}]
        for nombre in archivos:
            p = Path(raiz) / nombre
            if p.suffix.lower() not in EXT_TEXTO or nombre == "verificar_exportacion.py":
                continue
            try:
                lineas = p.read_text(encoding="utf-8", errors="replace").splitlines()
            except OSError:
                continue
            rel = str(p.relative_to(ruta))
            for i, linea in enumerate(lineas, 1):
                for etiqueta, rx in CHEQUEOS:
                    for m in rx.finditer(linea):
                        frag = m.group(0)
                        if etiqueta.startswith("NIT") and nit_permitido(frag, permitidos):
                            continue
                        if etiqueta == "correo" and frag in CORREOS_PERMITIDOS:
                            continue
                        hallazgos.append((etiqueta, rel, i, frag[:80]))
                for rx in rx_nombres:
                    m = rx.search(linea)
                    if m:
                        hallazgos.append(("nombre real", rel, i, m.group(0)))
    return hallazgos


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ruta")
    ap.add_argument("--nombres", help="archivo con nombres reales, uno por línea (FUERA del repo)")
    ap.add_argument("--permitidos", nargs="*", default=[], help="NIT públicos o ficticios adicionales")
    ap.add_argument("--max", type=int, default=200, help="máximo de hallazgos a listar")
    a = ap.parse_args(argv)
    nombres = Path(a.nombres).read_text(encoding="utf-8").splitlines() if a.nombres else []
    hallazgos = verificar(Path(a.ruta), nombres, PERMITIDOS_BASE + a.permitidos)
    if not hallazgos:
        print("✅ Sin hallazgos: el árbol pasa el checklist §4.")
        return 0
    print(f"❌ {len(hallazgos)} hallazgos (mostrando hasta {a.max}):")
    for etiqueta, rel, i, frag in hallazgos[: a.max]:
        print(f"  [{etiqueta}] {rel}:{i}  →  {frag}")
    por_tipo = {}
    for h in hallazgos:
        por_tipo[h[0]] = por_tipo.get(h[0], 0) + 1
    print("Resumen por tipo:", por_tipo)
    return 1


if __name__ == "__main__":
    sys.exit(main())
