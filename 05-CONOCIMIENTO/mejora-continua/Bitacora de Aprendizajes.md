---
tipo: proceso
tags: [ritore, aprendizaje, mejora-continua, bitacora]
estado: vigente
fecha: 2026-06-08
---

# Bitácora de Aprendizajes

Nota índice de la **bitácora viva** del *Sistema de Mejora Continua*: el **registro cronológico** de todas las lecciones de la firma, desde que se capturan hasta que se integran. Es la **trazabilidad** del módulo — el lugar donde se ve, de un vistazo, qué se aprendió, cuándo, de qué encargo, y si ya se integró a la fuente.

> **Importante:** la bitácora **registra y traza**; **no es donde vive el conocimiento para trabajar**. El conocimiento útil vive en la nota de fondo (protocolo, plantilla, ficha de cliente, normativa, lección de escuela) — ver *Proceso de Integracion del Conocimiento*. La bitácora responde "¿qué aprendimos y dónde quedó?"; la fuente responde "¿cómo se hace?".

## Qué es y cómo se relaciona con la plantilla Excel

- Esta nota es el **índice navegable** (en el vault) de la bitácora.
- El **registro estructurado + dashboard** vive en la plantilla Excel *Plantilla 30 - Bitacora de Aprendizajes y Mejoras* `[VERIFICAR — plantilla a crear]`: base de datos de lecciones con filtros (por fuente, cliente, estado, nota destino) y tablero de KPIs (lecciones capturadas/integradas, % de integración, errores recurrentes, tiempo de integración).
- Cada lección se captura con la [[Plantilla - Leccion Aprendida]] (los campos: fecha, fuente/disparador, cliente/proyecto, qué pasó, causa raíz, qué aprendimos, acción de mejora, nota destino, responsable, estado) — ver [[Proceso de Captura de Lecciones]].

## Estados de una lección

| Estado | Significado |
|---|---|
| **Capturada** | Registrada en caliente; aún sin validar. |
| **Validada** | El *30-GestorConocimiento-MejoraContinua* (con MonitoreoNormativo / Titular si aplica) confirmó que es correcta y vigente. |
| **Integrada** | ★ Ya se actualizó la nota destino del vault citando el origen. **Solo aquí la lección está cerrada.** |
| **Descartada** | Tras validar, no procede (duplicada, errónea, o criterio particular que no aplica). Se deja registrada con el motivo. |

## Registro de lecciones (ejemplos reales ya capturados)

Muestra de lecciones reales de las campañas, en el formato de la bitácora:

| Fecha | Fuente / disparador | Cliente / proyecto | Qué aprendimos (resumen) | Nota destino | Estado |
|---|---|---|---|---|---|
| 2025 | Error detectado | SERVICIOS SANITARIOS E + otros | Año contable sin cerrar: trabajar con MOVIMIENTOS del periodo, no con el saldo acumulado | *Lecciones Aprendidas Exogena* (D.5) | Integrada |
| 2025 | Error / parser | **Cliente - EXPORTADORA DE SERVICIOS B** | El parser perdía el primer movimiento de cada cuenta: no hacer `continue` en la fila de código; verificar D=C | *Lecciones Aprendidas Exogena* (C.1) | Integrada |
| 2025 | Criterio técnico | **Cliente - EXPORTADORA DE SERVICIOS B** | Cesantías efectivamente pagadas = saldo inicial 2510+2515 (criterio de caja) | *Formato 2276 - Rentas de Trabajo* (C.7) | Integrada |
| 2026 | Acta de revisoría | **Cliente - AGROPECUARIA D** | Inventarios $1.923M sobre el físico; pasivo $1.342M sin soporte → advertencia Arts. 648 ET / 434A CP | *Tablero de Alertas y Pendientes* | Capturada |
| 2026 | Concepto / norma nuevo | Transversal (firma) | Sanción 651 ET vigente: Ley 2277/2022, 1%/0,7%/0,5%, tope 7.500 UVT; reducción 10% por subsanación voluntaria | *Sancion Art 651 ET* | Validada |
| 2026 | Error de plantilla | Proyecto Exógena | F-2276: discrepancia 40 vs 46 columnas; alinear plantilla al prevalidador vigente | *Formato 2276 - Rentas de Trabajo* | Capturada |

> Los ejemplos ilustran los cuatro estados: integradas (ya viven en la fuente), validada (pendiente de integrar), capturadas (pendientes de validar). El módulo trabaja para que todo lo Validado pase a **Integrado**.

## Cómo se usa la bitácora

1. **Al cerrar una tarea:** el agente captura la lección aquí (estado Capturada) — [[Proceso de Captura de Lecciones]].
2. **Periódicamente:** el *30-GestorConocimiento-MejoraContinua* revisa las Capturadas, valida, integra y actualiza estados.
3. **Para detectar patrones:** se filtra por tipo de error; al llegar a 3+ ocurrencias se eleva a [[Registro de Errores Recurrentes]].
4. **Para medir:** el dashboard de la plantilla Excel reporta los KPIs del módulo.

## Relacionado

- *Sistema de Mejora Continua* · [[Proceso de Captura de Lecciones]] · *Proceso de Integracion del Conocimiento* · [[Registro de Errores Recurrentes]] · [[Glosario de Conceptos Nuevos]]
- *Plantilla 30 - Bitacora de Aprendizajes y Mejoras* · [[Plantilla - Leccion Aprendida]]
- *30-GestorConocimiento-MejoraContinua* · *Subskill B12 - Documentar y Aprender*
- *Lecciones Aprendidas Exogena* · *Tablero de Alertas y Pendientes* · *Sancion Art 651 ET* · *Formato 2276 - Rentas de Trabajo*
