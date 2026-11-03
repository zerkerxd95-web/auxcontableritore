---
tipo: estandar
tags: [ritore, agente, gobernanza, estandar]
estado: vigente
version: 1.0
fecha: 2026-06-11
---

# Estándar de Agentes RITORE (v1.0)

**Documento normativo interno.** Todo perfil de agente del ecosistema RITORE debe cumplir este estándar para considerarse **comercializable, confiable y medible**. Un perfil que no cumpla las secciones obligatorias está en estado *borrador*, no *activo*.

> Origen: auditoría integral del vault (2026-06-11). Problemas que este estándar corrige: copy-paste masivo entre skills, ausencia de inputs/outputs, métricas sin umbral numérico, escalamientos vagos, falta de versionado.

## 1. Niveles de agente (definición única)

| Nivel | Significado | Autoridad |
|---|---|---|
| **Master** | Decide criterios y coordina a otros agentes en su dominio. Sus salidas pueden bloquear un flujo. | Puede devolver trabajo a agentes Senior. Nunca firma: escala a humano. |
| **Senior** | Ejecuta procesos completos de su dominio con autonomía operativa. | Consulta a un Master en casos ambiguos. Nunca decide criterios nuevos. |

Roles sin nivel (DevOps, MejoraContinua) se reclasifican como **Senior** salvo decisión expresa del dueño.

## 2. Secciones obligatorias de cada skill dentro de un perfil

Cada skill debe tener TODAS estas secciones, **con contenido propio** (ver regla anti-clonación, §4):

1. **Para qué existe** — propósito en 1-2 líneas; qué se rompe si la skill no existe.
2. **Cuándo se activa** — triggers concretos (mensaje, evento, fecha, umbral).
3. **Inputs** — qué recibe, de quién, en qué formato, y qué hacer si falta un insumo (acción + plazo de espera).
4. **Procedimiento** — pasos numerados, verificables, específicos de ESTA skill.
5. **Outputs** — entregables concretos + criterios de aceptación verificables.
6. **Manejo de errores** — tabla `Error | Causa probable | Acción | Fallback si la acción falla`. Mínimo: el error más frecuente y el más grave.
7. **Escalamiento** — tabla con umbrales numéricos (ver §3). Prohibido "escalo si es material" sin número.
8. **Reglas críticas** — solo las ESPECÍFICAS de esta skill. Las universales viven en [[Skills Compartidas RITORE]] y se heredan, no se copian.
9. **Métricas** — 2-4 KPIs con meta numérica y frecuencia de medición.
10. **Tests** — mínimo 2 escenarios PROPIOS de la skill: 1 caso normal + 1 excepción/borde. Prohibido reutilizar tests de otra skill.

## 3. Umbrales estándar del ecosistema (fuente única)

Salvo que el perfil declare expresamente un umbral distinto (con justificación), aplican:

| Concepto | Umbral | Acción |
|---|---|---|
| Diferencia material (conciliaciones, cruces) | ≥ 1 UVT individual o ≥ 0,5 % del total acumulado | Investigar y documentar antes de avanzar |
| Diferencia crítica | ≥ 50 UVT | Escalar a Master del dominio |
| Diferencia mayor | ≥ 500 UVT | Escalar a Contador Titular |
| SLA crítico / alto / normal / bajo | 1 h / 4 h / 24 h / 48 h | Al 80 % del SLA → alertar al Orquestador; al 100 % → escalar a humano |
| Insumo faltante | espera máx. 24 h hábiles | Reiterar solicitud 1 vez; luego escalar a Orquestador |
| Agente dependiente no responde | timeout 4 h | Usar caché/último dato verificado con marca `[DATO EN CACHÉ — verificar]` y escalar en paralelo |

## 4. Regla anti-clonación

- Si dos skills comparten > 70 % del procedimiento, **son una sola skill con parámetros** (variantes documentadas en una tabla), no dos skills.
- Auto-corrección, reglas críticas y tests **no se copian entre skills**. Lo común se hereda de [[Skills Compartidas RITORE]]; en la skill solo va lo diferencial.
- Un test que aparezca textualmente en más de una skill se considera inválido en ambas.

## 5. Versionado obligatorio

Cada perfil cierra con:

```markdown
## Historial de versiones
| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | AAAA-MM-DD | Versión inicial | ... |
```

Todo cambio de procedimiento, umbral o regla incrementa la versión y registra el cambio. Sin changelog no hay trazabilidad de producto.

## 6. Frontmatter estándar

```yaml
---
tipo: agente
tags: [ritore, agente, <capa>]
capa: coordinacion | operativa | tributaria | financiera | aseguramiento | cumplimiento | servicio | interfaz | personal
nivel: master | senior
estado: activo | borrador | retirado
version: X.Y
fecha: AAAA-MM-DD   # fecha de la última modificación real
---
```

## 7. Criterio de "listo para comercializar"

Un agente es comercializable cuando: (a) cumple §2 en el 100 % de sus skills; (b) cero clones según §4; (c) todos los umbrales son numéricos o referencian §3; (d) tiene changelog; (e) sus wikilinks resuelven dentro del vault.

## Relacionado
- [[Skills Compartidas RITORE]]
- *00 - Estandar de Skills RITORE*
- [[Guia de Carga de Agentes]]
- *MOC - Agentes RITORE*
