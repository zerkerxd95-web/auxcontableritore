---
tipo: conocimiento
tags: [ritore, agente, guia]
estado: activo
fecha: 2026-06-07
---

# GUÍA DE CARGA — Skills del Ecosistema RITORE

**Fecha:** 2026-05-19
**Contenido de esta carpeta:** 29 archivos consolidados (1 por agente + 1 de skills compartidas) + esta guía.

---

## Qué hay aquí

Cada archivo `.md` contiene **todos los skills de un agente** consolidados en un solo documento legible. Los 320 skills individuales se agruparon en 29 archivos:

- `00-SKILLS-COMPARTIDAS.md` — 13 skills heredados por TODOS los agentes (la columna vertebral del comportamiento).
- `01-Orquestador-Master.md` … `28-AsistentePersonalEjecutiva.md` — 28 archivos, uno por agente, con sus skills propios.

Tamaño total: ~640 KB. Ningún archivo supera los 47 KB.

---

## ESCENARIO A — Claude Desktop (app de chat) como Proyecto

Usa esto si quieres conversar con Claude y que conozca el ecosistema RITORE.

### Pasos

1. Abre Claude Desktop → crea un **Proyecto nuevo** (ej: "Ecosistema RITORE").
2. En el Proyecto, ve a **"Conocimiento del proyecto"** (Project Knowledge).
3. Arrastra los archivos. **No los subas uno por uno** — selecciónalos en bloque:
   - En el explorador de archivos, abre esta carpeta.
   - `Ctrl + A` para seleccionar todos, o `Ctrl + click` para elegir varios.
   - Arrastra la selección completa a la ventana del Proyecto.
4. Los 29 archivos pesan ~640 KB en total — caben de sobra en un Proyecto.

### Recomendación de carga por uso

- **Si trabajas con un agente específico:** sube `00-SKILLS-COMPARTIDAS.md` + el archivo de ese agente. Son 2 archivos.
- **Si trabajas un flujo completo (ej: cierre mensual):** sube `00-SKILLS-COMPARTIDAS.md` + los agentes involucrados (Orquestador, AuxiliarContable, Conciliador, etc.).
- **Si quieres todo el ecosistema disponible:** sube los 29. Claude consultará el que aplique según tu pregunta.

### Por qué consolidado y no 320 archivos

320 archivos sueltos son incómodos de gestionar en la interfaz y de actualizar. Con 29 archivos: si cambias un agente, solo recargas su archivo.

---

## ESCENARIO B — n8n / API (el ecosistema productivo de 28 agentes)

Usa esto cuando implementes el ecosistema real con `claude-opus-4-7`.

Aquí los skills **NO se "suben" a una app**. Se integran así:

### Opción B1 — Skills en el prompt de sistema (más simple)

Cada agente en n8n tiene un nodo de LLM con un *system prompt*. La estructura es:

```
[ Sistema-Base.md ]                         ← heredado, todos los agentes
+ [ prompt-sistema del agente ]              ← carpeta output/01-agentes-ajustados/
+ [ 00-SKILLS-COMPARTIDAS.md ]               ← este folder
+ [ archivo de skills del agente ]           ← este folder (ej: 11-EspecialistaIVA-Master.md)
+ [ contexto dinámico de sesión ]            ← inyectado por n8n
```

Concatenas esos bloques en el campo `system` de la llamada al LLM. El agente "tiene" sus skills disponibles en contexto.

### Opción B2 — Skills cargados dinámicamente (más eficiente en tokens)

En lugar de meter TODOS los skills del agente en cada llamada:

1. Guarda cada skill individual (los 320 de la carpeta `SKILLS-CONSOLIDADAS/`) en una tabla PostgreSQL con su `name`, `description` y cuerpo.
2. Cuando llega un mensaje al agente, un paso previo en n8n evalúa qué skill(s) matchean por su `description` triggerable.
3. Solo se inyecta(n) en el prompt el/los skill(s) relevante(s).

Esto ahorra tokens: el EspecialistaIVA no carga sus 13 skills en cada llamada, solo el que aplica a la tarea.

**Para esta opción usa la carpeta `SKILLS-CONSOLIDADAS/` (320 archivos individuales), no esta.** Esta carpeta (consolidada por agente) es para la Opción B1 y para Claude Desktop.

### Recomendación

- **Arranque / Olas 2-3:** usa B1 (más simple, menos piezas móviles).
- **Cuando el volumen crezca:** migra a B2 (optimización de tokens). El sistema de aprendizaje continuo de Misión 6 ya está diseñado para B2.

---

## Resumen rápido

| Tu situación | Qué cargar | Desde dónde |
|--------------|------------|-------------|
| Probar/conversar en Claude Desktop | 29 archivos consolidados (o solo los que necesites) | Esta carpeta `SKILLS-POR-AGENTE/` |
| Implementar n8n — modo simple | Skills del agente en el system prompt | Esta carpeta `SKILLS-POR-AGENTE/` |
| Implementar n8n — modo optimizado | Skills individuales en PostgreSQL + carga dinámica | Carpeta `SKILLS-CONSOLIDADAS/` (320 archivos) |

**En ningún caso cargues archivos uno por uno.** Siempre selección múltiple / carga masiva.

---

## Nota sobre el formato SKILL.md

El frontmatter YAML (`name` / `description`) que tiene cada skill es el formato estándar de skills de Anthropic. La `description` está redactada para ser "triggerable": describe cuándo activar el skill. Esto funciona igual si el motor que lo lee es Claude Desktop, Claude Code, o tu orquestador n8n evaluando qué skill aplica.

## Relacionado
- *MOC - Agentes RITORE*
- *Proyecto - Ecosistema RITORE*
