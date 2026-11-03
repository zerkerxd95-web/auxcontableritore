#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Empaqueta cada skill de `claude-desktop/skills/<nombre>/` en un .zip listo para subir a
Claude Desktop / Cowork (Configuración → Skills → Subir skill) o a un Proyecto de claude.ai.

Uso:
    python empaquetar_skills_desktop.py [--origen claude-desktop/skills] [--salida claude-desktop/zips] [--solo-ritore]

Con --solo-ritore empaqueta únicamente las 12 skills propias de la firma (las de Anthropic ya vienen en Claude).
"""
from __future__ import annotations

import argparse
import os
import sys
import zipfile
from pathlib import Path

RITORE = {"00-skills-compartidas", "01-orquestador-master", "actualizacion-normativa", "auxiliar-senior",
          "conciliacion-master", "estados-financieros", "exogena-master", "iva-master", "retencion-master",
          "revisor-fiscal", "token-dian-master", "tributaria"}


def empaquetar(origen: Path, salida: Path, solo_ritore: bool) -> list[Path]:
    salida.mkdir(parents=True, exist_ok=True)
    hechos: list[Path] = []
    for carpeta in sorted(p for p in origen.iterdir() if p.is_dir() and (p / "SKILL.md").exists()):
        if solo_ritore and carpeta.name not in RITORE:
            continue
        destino = salida / f"{carpeta.name}.zip"
        with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
            for raiz, dirs, archivos in os.walk(carpeta):
                dirs[:] = [d for d in dirs if d not in {"__pycache__", ".git"}]
                for a in archivos:
                    ruta = Path(raiz) / a
                    z.write(ruta, str(Path(carpeta.name) / ruta.relative_to(carpeta)))
        hechos.append(destino)
    return hechos


def main(argv=None) -> int:
    raiz_repo = Path(__file__).resolve().parents[1]
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--origen", default=str(raiz_repo / "claude-desktop" / "skills"))
    ap.add_argument("--salida", default=str(raiz_repo / "claude-desktop" / "zips"))
    ap.add_argument("--solo-ritore", action="store_true")
    a = ap.parse_args(argv)
    hechos = empaquetar(Path(a.origen), Path(a.salida), a.solo_ritore)
    for h in hechos:
        print(f"  {h.name}  ({h.stat().st_size // 1024} KB)")
    print(f"{len(hechos)} skills empaquetadas en {a.salida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
