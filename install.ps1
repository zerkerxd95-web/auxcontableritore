<#
.SYNOPSIS
  Prepara esta máquina para trabajar con la Escuela del Auxiliar Contable de RITORÉ (Windows).

.DESCRIPTION
  1. Verifica Python e instala las dependencias de requirements.txt.
  2. Crea la carpeta de trabajo de clientes (por defecto .\TRABAJOS, que git ignora).
  3. Corre las pruebas de las herramientas con datos ficticios.
  4. Empaqueta las skills de Claude Desktop en claude-desktop\zips.

.PARAMETER Trabajos
  Carpeta donde vivirán los clientes reales. Por defecto: <repositorio>\TRABAJOS

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File .\install.ps1
  powershell -ExecutionPolicy Bypass -File .\install.ps1 -Trabajos "D:\Firma\TRABAJOS"
#>
[CmdletBinding()]
param(
    [string]$Trabajos = ""
)

$ErrorActionPreference = "Stop"
$Repo = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if (-not $Trabajos) { $Trabajos = Join-Path $Repo "TRABAJOS" }
$env:PYTHONIOENCODING = "utf-8"

Write-Host "`n== Escuela del Auxiliar Contable :: instalación ==" -ForegroundColor Yellow

# 1. Python
Write-Host "`n[1/4] Python y dependencias"
$py = Get-Command python -ErrorAction SilentlyContinue
if (-not $py) { $py = Get-Command py -ErrorAction SilentlyContinue }
if (-not $py) { throw "No encontré Python. Instálalo desde https://www.python.org/downloads/ marcando 'Add to PATH' y vuelve a correr." }
$pyExe = $py.Source
& $pyExe -c "import sys; assert sys.version_info >= (3, 10), sys.version"
if ($LASTEXITCODE -ne 0) { throw "Se necesita Python 3.10 o superior." }
& $pyExe -m pip install --user -q --disable-pip-version-check -r (Join-Path $Repo "requirements.txt")
if ($LASTEXITCODE -ne 0) { throw "pip no pudo instalar las dependencias." }

# 2. Carpeta de trabajo
Write-Host "[2/4] Carpeta de clientes: $Trabajos"
New-Item -ItemType Directory -Force -Path $Trabajos | Out-Null
$leeme = Join-Path $Trabajos "LEEME.txt"
if (-not (Test-Path $leeme)) {
    Set-Content -Path $leeme -Encoding utf8 -Value @"
Aquí van los clientes reales: <CLIENTE>\_cliente.yaml y <CLIENTE>\<AAAA-MM>\...
Esta carpeta es CONFIDENCIAL (ROJO). No se sube a GitHub ni se comparte fuera de la firma.
Crear un período:  python herramientas\nuevo_periodo.py "$Trabajos" "CLIENTE" AAAA-MM --nit NIT
"@
}

# 3. Pruebas
Write-Host "[3/4] Pruebas de las herramientas"
& $pyExe (Join-Path $Repo "herramientas\pruebas\test_herramientas.py") | Select-String -Pattern "^(OK|FALLA|\d+/)"
if ($LASTEXITCODE -ne 0) { Write-Warning "Alguna prueba falló: revisa el mensaje de arriba antes de usar las herramientas." }

# 4. Skills de Claude Desktop
Write-Host "[4/4] Skills de Claude Desktop -> claude-desktop\zips"
& $pyExe (Join-Path $Repo "herramientas\empaquetar_skills_desktop.py") | Out-Null

Write-Host "`nListo." -ForegroundColor Yellow
Write-Host "  - Abre Claude Code en: $Repo"
Write-Host "  - Empieza por: 00-EMPIEZA-AQUI\RUTA-DE-FORMACION.md"
Write-Host "  - Clientes reales en: $Trabajos (nunca dentro de otra carpeta del repositorio)"
