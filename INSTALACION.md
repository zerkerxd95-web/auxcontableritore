# Instalación

## Lo que necesitas

| Programa | Para qué | Obligatorio |
|---|---|---|
| [Git](https://git-scm.com/downloads) | descargar el repositorio y recibir actualizaciones | sí |
| [Python 3.10 o superior](https://www.python.org/downloads/) (marca *Add to PATH*) | las herramientas de `herramientas/` | sí |
| [Claude Code](https://claude.com/claude-code) o la app de escritorio de Claude | la IA que trabaja con el método | recomendado |
| [Obsidian](https://obsidian.md) | leer la escuela y el manual como un vault enlazado | opcional |
| Excel o LibreOffice | plantillas y papeles de trabajo | sí |

## Pasos

### Windows

```powershell
git clone <URL-DEL-REPOSITORIO> "$env:USERPROFILE\Desktop\ESCUELA-AUXILIAR"
```

```powershell
cd "$env:USERPROFILE\Desktop\ESCUELA-AUXILIAR"; powershell -ExecutionPolicy Bypass -File .\install.ps1
```

### macOS / Linux

```bash
git clone <URL-DEL-REPOSITORIO> ~/ESCUELA-AUXILIAR && cd ~/ESCUELA-AUXILIAR && bash install.sh
```

El instalador:

1. Verifica Python e instala las librerías de `requirements.txt` (openpyxl).
2. Crea la carpeta de trabajo **`TRABAJOS/`** dentro del repositorio. Ahí van los clientes reales
   (`TRABAJOS/<CLIENTE>/<AAAA-MM>/`); está en `.gitignore`, así que **nunca se sube**.
3. Corre las pruebas de las herramientas con datos ficticios.
4. Empaqueta las skills de Claude Desktop en `claude-desktop/zips/` para subirlas en *Configuración → Skills*.

Si prefieres guardar los clientes en otra ruta (por ejemplo una carpeta compartida de la firma), usa
`-Trabajos "D:\Firma\TRABAJOS"` en Windows o `TRABAJOS=/ruta bash install.sh` en macOS/Linux, y da esa ruta a las herramientas.

## Primer uso con Claude Code

```bash
claude
```

Ábrelo **en la carpeta del repositorio**. Claude lee `CLAUDE.md`, carga los subagentes (`.claude/agents/`) y las skills
(`.claude/skills/`). Prueba:

- *"Crea el período 2026-01 del cliente de práctica en TRABAJOS y guíame en el cierre."*
- *"Concilia este extracto contra el auxiliar de la cuenta 11100501."*
- *"Revisa si la entrega de 2026-01 está lista para el contador."*

## Con otra IA

- **Codex, Cursor, Gemini CLI, Copilot:** abren el repositorio y leen [AGENTS.md](AGENTS.md).
- **ChatGPT, Gemini, claude.ai (chat):** copia [PROMPT-SISTEMA.md](PROMPT-SISTEMA.md) en las instrucciones del proyecto y
  adjunta el manual de entrega y las reglas de la casa.

## Actualizar

```bash
git pull
```

Tus clientes en `TRABAJOS/` no se tocan con la actualización.
