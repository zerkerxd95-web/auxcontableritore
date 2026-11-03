#!/usr/bin/env bash
# Prepara esta máquina para trabajar con la Escuela del Auxiliar Contable de RITORÉ (macOS / Linux).
#   bash install.sh                       -> clientes en ./TRABAJOS (git la ignora)
#   TRABAJOS=/ruta/compartida bash install.sh
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TRABAJOS="${TRABAJOS:-$REPO/TRABAJOS}"
PY="$(command -v python3 || command -v python || true)"
export PYTHONIOENCODING=utf-8

echo
echo "== Escuela del Auxiliar Contable :: instalación =="

echo "[1/4] Python y dependencias"
[ -n "$PY" ] || { echo "No encontré Python 3. Instálalo y vuelve a correr."; exit 1; }
"$PY" -c "import sys; assert sys.version_info >= (3, 10), sys.version" || { echo "Se necesita Python 3.10 o superior."; exit 1; }
"$PY" -m pip install --user -q --disable-pip-version-check -r "$REPO/requirements.txt"

echo "[2/4] Carpeta de clientes: $TRABAJOS"
mkdir -p "$TRABAJOS"
if [ ! -f "$TRABAJOS/LEEME.txt" ]; then
  cat > "$TRABAJOS/LEEME.txt" <<EOF
Aquí van los clientes reales: <CLIENTE>/_cliente.yaml y <CLIENTE>/<AAAA-MM>/...
Esta carpeta es CONFIDENCIAL (ROJO). No se sube a GitHub ni se comparte fuera de la firma.
Crear un período:  python3 herramientas/nuevo_periodo.py "$TRABAJOS" "CLIENTE" AAAA-MM --nit NIT
EOF
fi

echo "[3/4] Pruebas de las herramientas"
if ! "$PY" "$REPO/herramientas/pruebas/test_herramientas.py" | grep -E "^(OK|FALLA|[0-9]+/)"; then
  echo "AVISO: alguna prueba falló; revisa el mensaje antes de usar las herramientas."
fi

echo "[4/4] Skills de Claude Desktop -> claude-desktop/zips"
"$PY" "$REPO/herramientas/empaquetar_skills_desktop.py" >/dev/null

echo
echo "Listo."
echo "  - Abre Claude Code en: $REPO"
echo "  - Empieza por: 00-EMPIEZA-AQUI/RUTA-DE-FORMACION.md"
echo "  - Clientes reales en: $TRABAJOS"
