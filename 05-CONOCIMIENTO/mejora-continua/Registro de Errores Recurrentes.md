---
tipo: proceso
tags: [ritore, aprendizaje, mejora-continua, errores, calidad]
estado: vigente
fecha: 2026-06-08
---

# Registro de Errores Recurrentes

El mecanismo de **mejora estructural** del *Sistema de Mejora Continua*: cuando un mismo tipo de error o inconsistencia aparece **en 3 o más clientes (o 3+ veces)**, deja de tratarse caso a caso y se eleva a un **cambio estructural** — mejorar un protocolo, un control en un agente fuente, una validación en una plantilla, o una lección de la escuela.

> **La regla del patrón 3+:** un error individual se corrige; un error que se repite se **previene en el sistema**. Es el cierre del ciclo de calidad: *el error individual mejora el sistema*, no solo el caso. Coherente con el "plan de mejora — regla de patrón" del [[Sistema de Control de Calidad de la Firma]] y con la mejora continua de la *Subskill B12 - Documentar y Aprender* ("si la misma inconsistencia aparece en 3+ clientes, propuesta de ajuste estructural").

## Cómo funciona la regla 3+

1. **Detección.** Al capturar una lección (ver [[Proceso de Captura de Lecciones]]), el *30-GestorConocimiento-MejoraContinua* revisa si el error ya aparece en la [[Bitacora de Aprendizajes]].
2. **Conteo.** Si el mismo tipo de error/inconsistencia llega a **3 ocurrencias** (3 clientes o 3 veces), se marca como **recurrente** y entra en este registro.
3. **Propuesta estructural.** El Gestor propone una mejora del sistema (no del caso): un control nuevo, una validación de plantilla, un paso de protocolo, una alerta en un agente fuente, o una lección formativa.
4. **Escalamiento.** Las propuestas de cambio estructural se escalan al **Director Técnico** (y al Contador Titular) para aprobación. No se cambia un protocolo de la firma por decisión unilateral.
5. **Integración.** Aprobada, la mejora se integra a la nota destino (ver *Proceso de Integracion del Conocimiento*) y se difunde.

## Tabla de errores recurrentes conocidos

Patrones ya observados en campañas reales (fuente: *Lecciones Aprendidas Exogena* y *Tablero de Alertas y Pendientes*) con la mejora estructural propuesta. La frecuencia se actualiza con cada nueva ocurrencia capturada.

| Error / inconsistencia | Frecuencia observada | Mejora estructural propuesta | Estado |
|---|---|---|---|
| **Año contable sin cerrar** (saldos antiguos en 41xx/2408xx/511570) | Recurrente (3+ clientes) | Control en el agente fuente: usar SIEMPRE movimientos del periodo; checklist de cierre anual que verifique el cierre contra 36/37. Lección de escuela [[Aux 25 - Cierre Anual y Errores Comunes]]. | Propuesta |
| **Reclasificaciones mal hechas en el auxiliar** (gastos/cuentas reclasificados erróneamente → descuadres) | Recurrente (SERVICIOS SANITARIOS E + otros) | Validación en el [[02-AuxiliarContable-Senior]]: cuadre débitos=créditos y revisión de reclasificaciones antes de entregar el insumo (regla C.8: corregir contabilidad, no el formato). | Propuesta |
| **Gastos personales del socio cargados a la sociedad** (EMPRESA DE TECNOLOGÍA K 539595; patrón en cierres) | Recurrente | Control en cierre + ficha de cliente: marcar cuentas sensibles de socios; no deducible; reclasificar. | Propuesta |
| **Inventario sobre el físico / sin soporte** (AGROPECUARIA $1.923M) | A vigilar | Control de revisoría: conciliar inventario contable vs físico; advertencia Arts. 648 ET / 434A CP. | A vigilar |
| **Excel corruptos en carpetas sincronizadas** (BadZipFile al leer .xlsx abiertos en OneDrive/Drive) | Recurrente (varios clientes) | Validación de integridad (firma EOCD) en todo lector de Excel + protocolo de "Guardar como"; ya en [[Manejo de Archivos Excel Corruptos]] (regla C.1). | Integrado |
| **Plantilla F-2276 desalineada del prevalidador** (40 vs 46 columnas) | 2 ocurrencias | Mejora de plantilla: alinear la estructura de columnas al prevalidador vigente cada año. | A vigilar |
| **Sanción Art. 651 ET desactualizada** en documentos internos (15.000 UVT del régimen anterior) | Transversal | Actualización normativa: corregir *Sancion Art 651 ET* al régimen Ley 2277/2022 (1%/0,7%/0,5%, tope 7.500 UVT) y propagar; control de vigencia con *21-MonitoreoNormativo-Senior*. **Vault corregido el 2026-06-11**; pendiente CLAUDE.md raíz. | Integrado (vault) |
| **Parser del libro auxiliar que pierde el primer movimiento** (EXPORTADORA DE SERVICIOS B y exportados similares) | Recurrente en exportados con código+movimiento en la misma fila | Control en el parser: no hacer `continue` en la fila de código; verificar débitos=créditos tras parsear. Ya en C.1 de *Lecciones Aprendidas Exogena*. | Integrado |

## Qué NO es un error recurrente

- Un **criterio particular de un cliente** (p. ej. regla < $50.000 de EXPORTADORA DE SERVICIOS B) no es un error: va a la ficha del cliente y NUNCA se generaliza. No entra en este registro.
- Un error **único** se corrige y se documenta, pero no dispara cambio estructural hasta llegar al patrón 3+.

## Relacionado

- *Sistema de Mejora Continua* · [[Proceso de Captura de Lecciones]] · *Proceso de Integracion del Conocimiento* · [[Bitacora de Aprendizajes]]
- [[Sistema de Control de Calidad de la Firma]] · *Tablero de Alertas y Pendientes* · *Subskill B12 - Documentar y Aprender*
- *30-GestorConocimiento-MejoraContinua* · [[02-AuxiliarContable-Senior]] · *21-MonitoreoNormativo-Senior*
- *Lecciones Aprendidas Exogena* · [[Manejo de Archivos Excel Corruptos]] · *Sancion Art 651 ET* · [[Aux 25 - Cierre Anual y Errores Comunes]]
