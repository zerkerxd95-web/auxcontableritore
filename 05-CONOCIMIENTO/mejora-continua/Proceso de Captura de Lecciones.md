---
tipo: proceso
tags: [ritore, aprendizaje, mejora-continua, captura]
estado: vigente
fecha: 2026-06-08
---

# Proceso de Captura de Lecciones

El **paso 1** del ciclo del *Sistema de Mejora Continua*: cómo, cuándo y con qué formato se captura una lección para que no se pierda. **Capturar es de TODOS** (cualquier agente o auxiliar al cerrar su tarea); **validar e integrar es del *30-GestorConocimiento-MejoraContinua***.

> **Regla:** se captura **en caliente**, al cerrar la tarea, no "cuando haya tiempo". Una lección no capturada en el momento se pierde o se distorsiona. Mejor un registro imperfecto hoy que uno perfecto que nunca llega.

## Cuándo capturar

Al cerrar **cualquier** tarea en la que se active un disparador del *Sistema de Mejora Continua* (cierre de proyecto, presentación de impuesto, entrega de reporte, corrección, requerimiento DIAN, error detectado, concepto/oficio/resolución nuevo, criterio particular de cliente nuevo, pregunta que no supimos responder).

En la práctica, el cierre de cada campaña ya obliga a documentar (Paso 10 del [[Protocolo Elaboracion de Impuestos]], regla C.9 de *Lecciones Aprendidas Exogena*, *Subskill B12 - Documentar y Aprender*). Este proceso lo **generaliza** a todo encargo, no solo a la exógena.

## Con qué formato — la Plantilla de Lección Aprendida

Cada lección se captura con la [[Plantilla - Leccion Aprendida]] (en `99 - Plantillas`), que estructura los campos. El registro cronológico vive en la [[Bitacora de Aprendizajes]].

### Campos de una lección

| Campo | Qué contiene |
|---|---|
| **Fecha** | Día de la captura. |
| **Fuente / disparador** | Cuál de los disparadores la originó (cierre, corrección, requerimiento, concepto nuevo…). |
| **Cliente / proyecto** | A qué encargo pertenece (o "transversal" si aplica a la firma). |
| **Qué pasó** | Descripción breve y objetiva del hecho. |
| **Causa raíz** | El porqué real, no el síntoma (p. ej. "año contable sin cerrar", no "las cifras no cuadraban"). |
| **Qué aprendimos** | El criterio o la regla destilada, aplicable hacia adelante. |
| **Acción de mejora** | Qué cambia: actualizar una nota, una plantilla, un protocolo, una ficha de cliente. |
| **Nota destino a actualizar** | El wikilink de la nota del vault donde se integrará (ver *Proceso de Integracion del Conocimiento*). |
| **Responsable** | Quién integrará (por defecto el Gestor de Conocimiento). |
| **Estado** | Capturada / Validada / Integrada / Descartada. |

La causa raíz es el campo más importante: sin causa raíz no hay aprendizaje, solo descripción. **Cero "explicado de palabra"** — coherente con la regla del [[Sistema de Control de Calidad de la Firma]] de que cada diferencia material se documenta con su causa.

## Dónde se registra

- **Registro cronológico:** [[Bitacora de Aprendizajes]] (índice) + la plantilla Excel estructurada *Plantilla 30 - Bitacora de Aprendizajes y Mejoras* `[VERIFICAR — plantilla a crear]` (registro + dashboard).
- **Conceptos nuevos:** si la lección incorpora un término o concepto, se añade además al [[Glosario de Conceptos Nuevos]].

## Ejemplos reales del vault (lecciones ya documentadas)

Estos son errores y criterios reales capturados en campañas, que ilustran cómo se ve una lección bien formada (detalle en *Lecciones Aprendidas Exogena* y *Tablero de Alertas y Pendientes*):

| Disparador | Qué pasó (resumen) | Causa raíz | Qué aprendimos | Nota destino |
|---|---|---|---|---|
| Error detectado | **Año contable sin cerrar:** cuentas 41xx/2408xx arrastraban saldos antiguos | No se cerró el ejercicio contra utilidades acumuladas (36/37) | Trabajar con MOVIMIENTOS del periodo, nunca con el saldo final acumulado | *Lecciones Aprendidas Exogena* (regla D.5) + ficha del cliente |
| Corrección | **Reclasificaciones SERVICIOS SANITARIOS E:** descuadres por reclasificaciones mal hechas en el aux | Error contable de origen, no del formato | NUNCA maquillar el formato; corregir la contabilidad y escalar | *Conciliacion Exogena vs Declaraciones* (regla C.8) |
| Requerimiento / acta | **Gastos del socio EMPRESA DE TECNOLOGÍA K:** $273,8M de gastos personales del socio en la 539595 | Gasto personal cargado al gasto de la sociedad | Reclasificar gasto de socio; no es deducible; revisar 539595 | **Cliente - EMPRESA DE TECNOLOGÍA K** + *Tablero de Alertas y Pendientes* |
| Acta de revisoría | **Inventario AGROPECUARIA D:** inventarios $1.923M sobre el físico | Inventario sin soporte / sobre el conteo físico | Verificar inventario contra físico; advertencia Arts. 648 ET / 434A CP | **Cliente - AGROPECUARIA D** + *Tablero de Alertas y Pendientes* |
| Error de plantilla | **F-2276: 40 vs 46 columnas** de la plantilla | Plantilla interna desalineada del prevalidador vigente | Verificar la estructura de columnas contra el prevalidador vigente | *Formato 2276 - Rentas de Trabajo* |
| Concepto / norma nuevo | **Sanción 651 ET desactualizada:** documentos citaban 15.000 UVT (régimen anterior) | Ley 2277/2022 cambió el régimen a 1%/0,7%/0,5%, tope 7.500 UVT | Actualizar la sanción vigente y su reducción por subsanación voluntaria | *Sancion Art 651 ET* + CLAUDE.md raíz |

Cada uno de estos, capturado, validado e integrado, deja de ser un tropiezo aislado y se vuelve un control de la firma.

## Quién hace qué

- **Captura:** el agente/auxiliar que cerró la tarea (o quien detectó el error). Llena la plantilla y la registra en la bitácora con estado **Capturada**.
- **Valida e integra:** el *30-GestorConocimiento-MejoraContinua* (con *21-MonitoreoNormativo-Senior* si es normativo y el Contador Titular si es material). Sin esta separación, la captura se convierte en autocertificación — lo que el SGC prohíbe.

## Relacionado

- *Sistema de Mejora Continua* · *Proceso de Integracion del Conocimiento* · [[Bitacora de Aprendizajes]] · [[Glosario de Conceptos Nuevos]] · [[Registro de Errores Recurrentes]]
- *30-GestorConocimiento-MejoraContinua* · *21-MonitoreoNormativo-Senior*
- *Subskill B12 - Documentar y Aprender* · *Lecciones Aprendidas Exogena* · *Tablero de Alertas y Pendientes*
- [[Plantilla - Leccion Aprendida]] · *Plantilla 30 - Bitacora de Aprendizajes y Mejoras*
- [[Sistema de Control de Calidad de la Firma]] · [[Protocolo Elaboracion de Impuestos]]
