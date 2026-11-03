---
tipo: skill
tags: [ritore, skill, cierre-mensual, bucle, pipeline]
estado: borrador
version: 1.0
fecha: 2026-07-03
---

# 🔁 Skill — Bucle de Cierre Mensual de Cliente

> Pipeline central del modelo *Proyecto - RITORE v3 - Sistema Operativo en Bucles*. Es el trabajo más repetido de la firma convertido en un bucle único: **el dato entra una vez, todo lo demás se deriva**. Estado *borrador* hasta completar la primera corrida verificada en un cliente piloto (regla del *00 - Estandar de Skills RITORE*).

Comportamientos comunes heredados de [[Skills Compartidas RITORE]] (cargar perfil de cliente, verificar vigencia normativa, escalar a humano, documentar decisión no trivial); no se re-copian aquí.

## Para qué existe

Eliminar el reproceso del ciclo mensual: hoy cada cliente se cierra con un método distinto, los mismos insumos se copian en varias carpetas, las salidas se editan a mano generando versiones `v1/v2/v3` sin trazabilidad, y las mismas validaciones (NIT/DV, cuadre, materialidad) se repiten manualmente. Esta skill define UN solo camino de ingesta → entrega para todos los clientes, dejando traza de cada corrida.

## Cuándo se activa

- Cron: a partir del día 1 hábil del mes siguiente al período a cerrar, para cada cliente con servicio contable recurrente activo en su `_cliente.yaml`.
- Manual: `/cierre-mensual <cliente> <AAAA-MM>` o cuando llega el último insumo pendiente del período.
- Re-corrida: cuando un insumo del período cambia después de un cierre ya corrido (ajuste, extracto corregido, factura tardía). **La re-corrida ES el mecanismo normal de corrección** — nunca se edita una salida a mano.

## Inputs

| Insumo | Origen | Formato | Obligatorio |
|---|---|---|---|
| `_cliente.yaml` (parámetros y criterios particulares vigentes) | Carpeta raíz del cliente / ficha *MOC - Clientes* | YAML | Sí |
| Token DIAN del período (emitidas + recibidas + DSEL) | Portal DIAN | Excel | Sí |
| Extractos bancarios de todas las cuentas del período | Bancos | PDF/Excel/OFX | Sí |
| Balance de prueba y libro auxiliar del período | Software contable | Excel | Sí |
| Novedades de nómina (si aplica) | Cliente | Excel/correo | Según yaml |
| Soportes adicionales (facturas, contratos) | Cliente | Varios | Según hallazgos |

Todos los insumos se depositan en `TRABAJOS Y REQUERIMIENTOS/<CLIENTE>/<AAAA-MM>/01-INSUMOS/` **tal como llegan y no se editan jamás** (🔴 ROJO).

## Procedimiento

**Fase 1 — INGESTA (el dato se toca una vez)**
1. Verificar completitud de insumos contra el checklist del `_cliente.yaml`. Insumo faltante → regla de espera estándar (24 h hábiles, 1 reiteración, luego escalar).
2. Correr `ritore.ingesta`: normalizar token, extractos y auxiliar a `02-PROCESADO/`.

**Fase 2 — VALIDACIÓN (automática, bloqueante)**
3. Correr `ritore.validar`: cuadre débito=crédito, NIT/DV de terceros, duplicados, fechas dentro del período, año contable cerrado del período anterior (lección D.5 de *Lecciones Aprendidas Exogena*).
4. Correr `ritore.cruzar`: Token ↔ contabilidad (ventas, compras, retenciones practicadas y sufridas) y facturación electrónica ↔ ingresos. Toda diferencia ≥ umbral estándar (≥ 1 UVT o ≥ 0,5% — fuente única: [[00 - Estandar de Agentes RITORE]]) genera fila obligatoria en la tabla de diferencias de `04-TRAZAS/` con causa, ajuste y estado. **Diferencia material sin fila resuelta = el bucle no avanza.**

**Fase 3 — LIQUIDACIÓN (lo que venza en el período)**
5. Según `_cliente.yaml` y [[Plantilla 29 - Control Maestro de Obligaciones]]: liquidar F-350, F-300 (si el bimestre cierra), ReteICA municipal, nómina/PILA. Usa la skill maestra tributaria con los parámetros del formulario; no re-implementa cálculos.
6. Presentación y pago: preparar borradores; **la firma y presentación son siempre del humano titular** (ningún agente firma). Acuses a `03-SALIDA/` y registro en el control de obligaciones.

**Fase 4 — CIERRE Y ENTREGA**
7. Correr `ritore.generar`: EEFF del período, informe gerencial (resultado, caja, cartera, alertas) y cuenta de cobro, desde `02-PROCESADO/` hacia `03-SALIDA/`.
8. Control de cuatro ojos según [[Sistema de Control de Calidad de la Firma]] sobre la salida (no sobre los intermedios).
9. Entregar al cliente; archivar acuse de entrega.

**Fase 5 — APRENDIZAJE (cierra el bucle)**
10. `ritore.traza` consolida el log de la corrida: validaciones falladas, diferencias encontradas, correcciones aplicadas, horas invertidas.
11. Toda corrección de criterio o hallazgo repetible se registra como lección candidata en [[Bitacora de Aprendizajes]]; a la 3ª ocurrencia del mismo problema se cambia el motor o esta skill ([[Registro de Errores Recurrentes]]), no se vuelve a corregir a mano.

## Outputs y criterios de aceptación

| Output | Ubicación | Criterio de aceptación |
|---|---|---|
| Datos normalizados del período | `02-PROCESADO/` | Reproducibles: re-correr la ingesta da el mismo resultado |
| Declaraciones del período + acuses | `03-SALIDA/` | Presentadas dentro del plazo; cero diferencias materiales abiertas |
| EEFF + informe gerencial + cuenta de cobro | `03-SALIDA/` | Cuatro ojos aprobado; cifras trazables al procesado |
| Traza de la corrida | `04-TRAZAS/` | Existe SIEMPRE, incluso en corridas fallidas; incluye horas invertidas |
| Lecciones candidatas | [[Bitacora de Aprendizajes]] | Toda corrección de criterio quedó capturada |

Aceptación global del cierre: **ningún archivo de salida editado a mano, ninguna diferencia material sin fila resuelta, ningún archivo duplicado fuera de su carpeta única.**

## Manejo de errores y fallback

| Error | Causa probable | Acción | Fallback |
|---|---|---|---|
| Insumo ilegible/corrupto | Excel dañado, PDF escaneado | Protocolo de [[Manejo de Archivos Excel Corruptos]]; pedir reenvío | Captura manual mínima documentada en traza |
| Cuadre D≠C en balance | Asiento descuadrado en el software | NO avanzar; reportar al cliente/auxiliar para corregir en origen | Escalar si no se corrige en 48 h |
| Diferencia material Token ↔ contabilidad sin causa | Facturas no contabilizadas, NC omitidas, terceros contra NIT propio | Investigar y documentar fila por fila; corregir contabilidad, **nunca el reporte** (regla C.8) | Escalar a humano si implica cambio de criterio |
| Cambio de insumo post-cierre | Ajuste tardío | Corregir insumo → re-correr pipeline completo | Prohibido parchar la salida a mano |
| Vencimiento en riesgo (< 48 h) sin insumos | Cliente no envía | Alerta en *Tablero de Alertas y Pendientes* + comunicación formal al cliente | Presentación con la mejor información disponible SOLO con aprobación del titular, documentada |

## Escalamiento

- Diferencia crítica ≥ 50 UVT → titular del dominio tributario. Diferencia mayor ≥ 500 UVT → Contador Titular (umbrales estándar del ecosistema, fuente única).
- Indicios de irregularidad (gastos personales de socios, inventarios sin soporte, EEFF "no reales") → Contador Titular de inmediato; registrar en la ficha del cliente. Nunca normalizar en silencio.
- Firma, presentación y decisiones de criterio material: SIEMPRE humano.

## Reglas críticas

1. Los insumos de `01-INSUMOS/` son inmutables; la corrección se hace en el origen y se re-ingiere.
2. Prohibido el sufijo de versión en archivos (`v2`, `final`, `LIMPIA`): la versión es la corrida, trazada en `04-TRAZAS/`.
3. Un archivo vive en una sola carpeta; se referencia, no se copia.
4. Criterios de cliente solo desde `_cliente.yaml`/ficha; jamás hardcodeados aquí (§3 del estándar).
5. Toda cifra entregada debe ser trazable: salida ← procesado ← insumo.
6. Clientes con antecedente sancionatorio (vigilancia reforzada en su yaml): verificación explícita de períodos presentados ANTES de cerrar el mes.

## Métricas

- **Horas por cierre** (la métrica que vende el producto): medida automática por corrida; meta ≤ 1 día por cliente al tercer mes.
- % de cierres dentro de los 5 primeros días hábiles (meta ≥ 90%).
- Diferencias materiales detectadas ANTES de presentar (a mayor detección temprana, menor riesgo sancionatorio).
- Re-corridas por cierre (meta: tendencia decreciente = insumos mejor la primera vez).
- Lecciones integradas / lecciones capturadas (alimenta la meta 80% del *Sistema de Mejora Continua*).

## Tests

**Test 1 (caso normal):** Cliente con IVA bimestral en mes de cierre de bimestre; todos los insumos llegan completos el día 3. Resultado esperado: pipeline completo en una corrida, F-350 + F-300 presentados en plazo, EEFF e informe entregados, traza con cero diferencias materiales abiertas, ninguna salida editada a mano.

**Test 2 (caso borde):** El día 12, tras entregar el cierre, el cliente reporta una factura de compra de 80 UVT no contabilizada del período. Resultado esperado: se contabiliza en el origen, se re-corre el pipeline completo (no se parcha el EEFF), la diferencia queda con fila resuelta en trazas, se evalúa corrección de la declaración afectada con aprobación del titular, y la omisión queda como lección candidata en la bitácora.

## Relacionado

- *Proyecto - RITORE v3 - Sistema Operativo en Bucles* — arquitectura y motor `ritore/`
- [[Skills Compartidas RITORE]] · *00 - Estandar de Skills RITORE*
- *Skill Maestra - Desarrollar Informacion Exogena Completa* — consume los procesados mensuales de esta skill
- [[Sistema de Control de Calidad de la Firma]] · *Sistema de Mejora Continua* · [[Bitacora de Aprendizajes]] · [[Registro de Errores Recurrentes]]
- [[Plantilla 29 - Control Maestro de Obligaciones]] · *Tablero de Alertas y Pendientes* · *Lecciones Aprendidas Exogena*

## Historial de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-07-03 | Creación como pipeline central del rediseño v3. Estado borrador hasta la primera corrida verificada en cliente piloto. |
