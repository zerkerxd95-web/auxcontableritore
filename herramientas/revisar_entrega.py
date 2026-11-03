#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Revisión automática de la carpeta de un período ANTES de entregarla al contador.

    python herramientas/revisar_entrega.py "RUTA/<CLIENTE>/<AAAA-MM>"

Verifica el estándar de entrega (02-MANUAL-DE-ENTREGA/01): estructura de carpetas, insumos mínimos, papeles de trabajo
de las ocho áreas, asientos propuestos cuadrados, nombres sin sufijos de versión, pendientes con valor, responsable y
fecha, y ENTREGA.md diligenciado. Imprime un semáforo y termina con código 0 (verde), 1 (ámbar) o 2 (rojo).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))

SUFIJOS = re.compile(r"(\bv\d+\b|\bfinal\b|\(limpia\)|\bcopia\b|\bnuevo\b|\bdefinitivo\b|\bok\b)", re.I)
INSUMOS = {"token DIAN": r"^TOKEN", "extracto bancario": r"^EXTRACTO", "balance de prueba": r"^BP_", "libro auxiliar": r"^AUX_"}
PAPELES = {
    "1 · cruce token": r"^01_CRUCE_TOKEN", "2 · conciliaciones": r"^02_CONCILIACIONES", "3-4 · cartera y proveedores": r"^03_CARTERA",
    "5 · cuadre de impuestos": r"^04_CUADRE_IMPUESTOS", "6 · nómina": r"^05_NOMINA", "7-8 · balance revisado": r"^06_BP_REVISADO",
}
TRAZAS = ["NOTAS-Y-PENDIENTES.md", "TABLA-DE-DIFERENCIAS.md", "REGISTRO-DE-CORRIDAS.md"]


class Reporte:
    def __init__(self):
        self.items = []

    def ok(self, t):
        self.items.append(("🟢", t))

    def warn(self, t):
        self.items.append(("🟡", t))

    def err(self, t):
        self.items.append(("🔴", t))

    @property
    def nivel(self):
        return 2 if any(i[0] == "🔴" for i in self.items) else 1 if any(i[0] == "🟡" for i in self.items) else 0


def nombres(carpeta: Path) -> list[str]:
    return [p.name for p in carpeta.iterdir() if p.is_file()] if carpeta.exists() else []


def revisar_asientos(ruta: Path, r: Reporte):
    try:
        import openpyxl
    except ImportError:
        r.warn("openpyxl no instalado: no se revisó la hoja de asientos")
        return
    wb = openpyxl.load_workbook(ruta, data_only=False)
    ws = wb["02 ASIENTOS"] if "02 ASIENTOS" in wb.sheetnames else wb.worksheets[0]
    filas = [row for row in ws.iter_rows(min_row=6, values_only=True) if row and row[4] not in (None, "") and str(row[4]).strip()[:1].isdigit()]
    if not filas:
        r.warn("ASIENTOS_PROPUESTOS sin asientos (si no hay ajustes, escríbelo en ENTREGA.md)")
        return
    por_comp, sin_tercero = {}, 0
    for f in filas:
        comp = str(f[2] or f[0])
        d = float(f[7] or 0)
        c = float(f[8] or 0)
        por_comp.setdefault(comp, [0.0, 0.0])
        por_comp[comp][0] += d
        por_comp[comp][1] += c
        if not f[6]:
            sin_tercero += 1
    descuadrados = [k for k, (d, c) in por_comp.items() if abs(d - c) > 0.01]
    td = sum(v[0] for v in por_comp.values())
    tc = sum(v[1] for v in por_comp.values())
    if descuadrados:
        r.err(f"Comprobantes descuadrados en ASIENTOS_PROPUESTOS: {', '.join(descuadrados[:8])}")
    elif abs(td - tc) > 0.01:
        r.err(f"La hoja de asientos no cuadra: débitos {td:,.2f} vs créditos {tc:,.2f}")
    else:
        r.ok(f"ASIENTOS_PROPUESTOS: {len(filas)} líneas en {len(por_comp)} comprobantes, todos cuadrados")
    if sin_tercero:
        r.warn(f"{sin_tercero} líneas de asientos sin tercero")


def revisar_pendientes(ruta: Path, r: Reporte):
    t = ruta.read_text(encoding="utf-8")
    filas = [l for l in t.splitlines() if l.startswith("|") and not re.match(r"^\|\s*[-#]", l) and "Área" not in l and "Qué falta" not in l]
    incompletas, abiertas = 0, 0
    for l in filas:
        celdas = [c.strip() for c in l.strip("|").split("|")]
        if len(celdas) >= 7 and celdas[2] and not celdas[6].upper().startswith("CERRADO"):
            abiertas += 1
            if not (celdas[3] and celdas[4] and re.search(r"\d{4}-\d{2}-\d{2}", celdas[5] or "")):
                incompletas += 1
    if incompletas:
        r.err(f"NOTAS-Y-PENDIENTES: {incompletas} pendientes sin valor, responsable o fecha (AAAA-MM-DD)")
    else:
        r.ok(f"NOTAS-Y-PENDIENTES: {abiertas} pendientes abiertos, todos con valor, responsable y fecha")


def revisar_entrega(ruta: Path, r: Reporte):
    t = ruta.read_text(encoding="utf-8")
    if "{{" in t:
        r.err("ENTREGA.md tiene campos sin diligenciar ({{…}})")
    semaforo = re.findall(r"^\|\s*\d\s*\|[^|]+\|\s*([^|]*)\|", t, flags=re.M)
    sin_estado = [s for s in semaforo if not any(e in s for e in ("🟢", "🟡", "🔴"))]
    if sin_estado or len(semaforo) < 8:
        r.err("ENTREGA.md: el semáforo de las ocho áreas no está completo (deja un solo color por área)")
    elif any("/" in s for s in semaforo):
        r.err("ENTREGA.md: en el semáforo quedó la opción de plantilla; deja un solo color por área")
    else:
        rojos = sum(1 for s in semaforo if "🔴" in s)
        (r.warn if rojos else r.ok)(f"ENTREGA.md: semáforo completo ({rojos} áreas en rojo)")


def main(argv=None) -> int:
    if not argv:
        argv = sys.argv[1:]
    if not argv:
        print(__doc__)
        return 2
    per = Path(argv[0])
    r = Reporte()
    if not re.fullmatch(r"\d{4}-\d{2}", per.name):
        r.err(f"La carpeta del período debe llamarse AAAA-MM (es '{per.name}')")
    for sub in ("01-INSUMOS", "02-PROCESADO", "03-SALIDA", "04-TRAZAS"):
        (r.ok if (per / sub).is_dir() else r.err)(f"Carpeta {sub}" + ("" if (per / sub).is_dir() else " no existe"))
    if not (per.parent / "_cliente.yaml").exists():
        r.warn("No hay _cliente.yaml en la carpeta del cliente: los criterios particulares no están a la vista")

    ins = nombres(per / "01-INSUMOS")
    for nombre, patron in INSUMOS.items():
        (r.ok if any(re.match(patron, n, re.I) for n in ins) else r.err)(f"Insumo: {nombre}" + ("" if any(re.match(patron, n, re.I) for n in ins) else " FALTA en 01-INSUMOS"))

    pap = nombres(per / "02-PROCESADO")
    for nombre, patron in PAPELES.items():
        if any(re.match(patron, n, re.I) for n in pap):
            r.ok(f"Papel de trabajo {nombre}")
        elif nombre.startswith("6"):
            r.warn(f"Papel de trabajo {nombre} no está (si el cliente no tiene nómina, decirlo en ENTREGA.md)")
        else:
            r.err(f"Papel de trabajo {nombre} FALTA en 02-PROCESADO")

    sal = list((per / "03-SALIDA").glob("ASIENTOS_PROPUESTOS_*.xlsx"))
    if sal:
        revisar_asientos(sal[0], r)
    else:
        r.err("Falta 03-SALIDA/ASIENTOS_PROPUESTOS_<AAAA-MM>.xlsx")
    if not any(n.upper().startswith("BORRADOR") for n in nombres(per / "03-SALIDA")):
        r.warn("No hay borradores de impuestos en 03-SALIDA (si nada vence este mes, decirlo en ENTREGA.md)")

    for t in TRAZAS:
        (r.ok if (per / "04-TRAZAS" / t).exists() else r.err)(f"Traza {t}" + ("" if (per / "04-TRAZAS" / t).exists() else " FALTA"))
    if (per / "04-TRAZAS" / "NOTAS-Y-PENDIENTES.md").exists():
        revisar_pendientes(per / "04-TRAZAS" / "NOTAS-Y-PENDIENTES.md", r)
    if (per / "ENTREGA.md").exists():
        revisar_entrega(per / "ENTREGA.md", r)
    else:
        r.err("Falta ENTREGA.md en la raíz del período")

    con_sufijo = [p.name for p in per.rglob("*") if p.is_file() and "anteriores" not in p.parts and SUFIJOS.search(p.stem)]
    if con_sufijo:
        r.err("Archivos con sufijo de versión (mover a 04-TRAZAS/anteriores): " + ", ".join(con_sufijo[:6]))
    else:
        r.ok("Sin archivos con sufijos v2/final/copia")
    bloqueos = [p.name for p in per.rglob("~$*")] + [p.name for p in per.rglob(".~lock*")]
    if bloqueos:
        r.warn("Hay archivos de Office abiertos (bloqueo): " + ", ".join(bloqueos[:4]))

    print(f"\nRevisión de entrega · {per.parent.name} · {per.name}\n")
    for icono, texto in r.items:
        print(f"  {icono} {texto}")
    print("\n" + {0: "🟢 LISTA PARA ENTREGAR", 1: "🟡 SE PUEDE ENTREGAR: los pendientes en ámbar deben quedar explicados en ENTREGA.md",
                  2: "🔴 NO SE ENTREGA: corrige los puntos en rojo"}[r.nivel])
    return r.nivel


if __name__ == "__main__":
    sys.exit(main())
