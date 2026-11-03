---
tipo: agente
tags: [ritore, agente, operativa]
capa: operativa
nivel: senior
estado: activo
version: 2.0
fecha: 2026-06-11
---

# SKILLS — 05-AuxiliarCarteraCxP-Senior

**Documento consolidado** · 7 skills · Ecosistema RITORE · v2.0
**Modelo:** claude-opus-4-7

> Reescritura completa según [[00 - Estandar de Agentes RITORE]] (§2 secciones obligatorias, §3 umbrales, §4 anti-clonación). Las 4 skills de aplicación de pagos (1 factura, múltiples facturas, retenciones practicadas, descuento pronto pago) se consolidaron en `aplicar-pago-a-tercero` con variantes paramétricas porque compartían > 70 % del procedimiento. Los dos agings (cliente y proveedor) se consolidaron en `generar-aging-cartera`. Se agregó `calcular-deterioro-cartera` (proceso que existía implícito y carecía de skill). Las reglas universales (no aplicar pago sin soporte, no inventar datos, registro en bus) se heredan de [[Skills Compartidas RITORE]] y no se repiten aquí.

---

## Índice de skills en este documento

- `aplicar-pago-a-tercero` *(base paramétrica: pago a 1 factura · pago a múltiples facturas · retenciones practicadas por la contraparte · descuento pronto pago)*
- `generar-aging-cartera` *(base paramétrica: CxC clientes · CxP proveedores)*
- `alertar-cartera-vencida`
- `calcular-deterioro-cartera`
- `conciliar-con-tercero-externo`
- `detectar-saldos-naturaleza-contraria`
- `gestionar-anticipo-cliente-proveedor`

═══════════════════════════════════════════════════════════════════════

---
name: aplicar-pago-a-tercero
description: Skill base de aplicación de pagos. Cubre 4 variantes paramétricas — imputar pago a 1 factura, imputar pago a múltiples facturas, registrar retenciones practicadas por la contraparte y aplicar descuento por pronto pago. Activa cuando el Conciliador identifica un pago entrante/saliente con NIT del tercero.
agente: RITORE-AuxiliarCarteraCxP-Senior
categoria: operativo
---

# Skill: aplicar-pago-a-tercero

## Para qué existe
Todo pago recibido o emitido debe quedar imputado a facturas concretas del tercero, con sus retenciones y descuentos desagregados. Si la imputación falla, el saldo por tercero deja de ser confiable: el aging miente, la circularización no cuadra y los certificados de retención salen incompletos.

## Cuándo se activa (por variante)

| Variante | Trigger |
|---|---|
| **A — Pago a 1 factura** | Conciliador notifica pago con NIT cuyo monto coincide con UNA factura pendiente (± retenciones) |
| **B — Pago a múltiples facturas** | El monto cubre o excede más de una factura del tercero |
| **C — Retenciones practicadas** | El pago llega neto de retención practicada por la contraparte (diferencia = % de retención aplicable) |
| **D — Descuento pronto pago** | El pago llega dentro del plazo de descuento pactado y el neto coincide con factura − descuento |

Las variantes se combinan en una misma aplicación (un pago puede traer B + C + D simultáneamente).

## Inputs

| Insumo | De quién | Formato | Si falta |
|---|---|---|---|
| Notificación de pago: monto, fecha, NIT del tercero, referencia | Conciliador | Mensaje de bus | Sin notificación NO hay aplicación; si el cliente reporta un pago no notificado, pedir al Conciliador verificación contra extracto (timeout 4 h, luego escalar) |
| Facturas pendientes del tercero con saldo, fecha de vencimiento y condiciones de pago | Módulo CxC/CxP del ERP | Export tabla | Si el módulo no responde en 4 h, usar último estado verificado con marca `[DATO EN CACHÉ — verificar]` y escalar en paralelo |
| Soporte del pago (consignación, transferencia, instrucción de imputación del tercero) | Cliente / AtencionCliente | PDF / correo | Reiterar solicitud 1 vez en 24 h hábiles; mientras tanto el pago queda en cuenta puente `[PAGO POR IDENTIFICAR]`, nunca aplicado a ciegas |
| Política de descuento pronto pago del cliente (variante D) | `cargar-perfil-cliente` | Ficha Notion | Sin política documentada NO se reconoce descuento: la diferencia se trata como saldo abierto y se consulta a AtencionCliente |

## Procedimiento

**Tronco común (toda variante):**
1. Validar identidad del tercero (NIT en maestro de terceros con RUT vigente).
2. Listar facturas pendientes del tercero ordenadas por instrucción de imputación del pagador; si no hay instrucción, FIFO (más antigua primero).
3. Descomponer el pago: valor a capital + retenciones practicadas + descuento pronto pago. El total descompuesto debe ser igual al valor de las facturas afectadas.
4. Ejecutar los pasos de la variante (tabla siguiente).
5. Verificar cuadre: saldo del tercero antes − imputaciones = saldo después. Diferencia tolerada $0.
6. Notificar: Conciliador (confirmación de aplicación), Tesoreria (saldo actualizado), AuxContable (asiento propuesto).

**Pasos específicos por variante:**

| Variante | Pasos propios |
|---|---|
| **A — 1 factura** | (a) Imputar 100 % a la factura. (b) Si el monto difiere del saldo en menos de 1 UVT, cerrar la factura y llevar la diferencia a ajuste menor documentado; si difiere en ≥ 1 UVT, dejar parcial e investigar. |
| **B — Múltiples facturas** | (a) Aplicar instrucción del pagador si existe; si no, FIFO. (b) Cerrar facturas completas; la última puede quedar parcial. (c) Si sobra dinero tras cubrir todo el saldo, tratar el excedente como anticipo → disparar `gestionar-anticipo-cliente-proveedor`. |
| **C — Retenciones practicadas** | (a) Verificar que el % retenido corresponde al concepto y la base (retefuente, reteIVA, reteICA según municipio). (b) Registrar en 1355/135515 (retenciones a favor) la retención que nos practicaron. (c) Notificar a EspecialistaRetenciones (alimenta el cruce de certificados anuales). (d) Si el % no corresponde a ningún concepto aplicable, NO registrar como retención: investigar como diferencia. |
| **D — Descuento pronto pago** | (a) Validar que el pago ocurrió dentro del plazo pactado (fecha valor del banco, no fecha de registro). (b) CxC: reconocer el descuento como menor valor del ingreso o gasto financiero según política NIIF del cliente; CxP: como ingreso financiero o menor costo. (c) Si el tercero tomó el descuento FUERA del plazo, no reconocerlo automáticamente: reportar a AtencionCliente para decisión comercial. |

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Imputación registrada por factura | Capital + retenciones + descuento = valor facturas afectadas, diferencia $0; trazabilidad pago → facturas |
| Asiento propuesto a AuxContable | Cuadrado; retenciones en cuentas 1355/135515/135518 separadas del capital |
| Notificación a EspecialistaRetenciones (variante C) | Incluye NIT, concepto, base, tarifa y valor retenido |
| Actualización del aging | El saldo del tercero en `generar-aging-cartera` refleja la aplicación el mismo día |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| El pago no coincide con ninguna combinación de facturas (± retenciones/descuentos) | Pago de un tercero distinto, abono libre o error del pagador | Pedir a AtencionCliente la instrucción de imputación al tercero (plazo 24 h hábiles) | Mantener en cuenta puente `[PAGO POR IDENTIFICAR]`; al 5.º día hábil escalar al Orquestador |
| Retención registrada con % que no corresponde al concepto | Contraparte aplicó tarifa errada o autorretención mal entendida | Recalcular tarifa correcta; solicitar al tercero certificado o corrección | Registrar la retención efectivamente practicada con marca `[TARIFA EN DISPUTA]` y notificar a EspecialistaRetenciones para el cruce anual |
| Doble aplicación del mismo pago | Notificación duplicada del Conciliador o reproceso | Reversar la segunda aplicación citando la primera (fecha + referencia) | Congelar el saldo del tercero con marca `[DOBLE APLICACIÓN EN REVISIÓN]` y escalar al Conciliador |
| Descuento tomado por el tercero fuera del plazo | Cliente paga tarde pero se descuenta igual | No reconocer el descuento; reportar la diferencia como saldo abierto a AtencionCliente | Si AtencionCliente no responde en 24 h hábiles, dejar el saldo abierto en el aging y registrar el caso |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia entre pago y facturas imputables | ≥ 1 UVT individual o ≥ 0,5 % del pago | Investigar y documentar antes de aplicar |
| Diferencia sin resolver | ≥ 50 UVT | EspecialistaRetenciones (si es de retención) / Conciliador (si es bancaria) |
| Diferencia sin resolver | ≥ 500 UVT | Contador Titular vía Orquestador |
| Pago sin identificar en cuenta puente | > 5 días hábiles | Orquestador |
| Instrucción de imputación faltante | > 24 h hábiles tras reiterar 1 vez | Orquestador |

## Reglas críticas
🚫 NUNCA aplicar un pago "a saldo global" del tercero: siempre a facturas identificadas (o a cuenta puente mientras se identifica).
🚫 NUNCA reconocer descuento por pronto pago sin política documentada y pago dentro del plazo (fecha valor).
🚫 NUNCA conciliar yo contra el extracto bancario (eso es del Conciliador; yo imputo lo que él confirma).
✅ SIEMPRE descomponer el pago en capital + retenciones + descuentos antes de imputar.

## Métricas
- Pagos aplicados el mismo día hábil de la notificación del Conciliador: ≥ 95 % (medición semanal).
- Pagos en cuenta puente `[PAGO POR IDENTIFICAR]` al cierre del mes: ≤ 2 % del valor recaudado del mes.
- Retenciones practicadas registradas y notificadas a EspecialistaRetenciones: 100 % (medición mensual).
- Reversiones por error de imputación propio: ≤ 1 por mes.

## Tests
### Test 1 — (normal, variantes B+C) Cliente paga $11.585.000 que cubre las facturas FV-101 ($5.950.000) y FV-102 ($5.950.000), neto de retefuente del 2,5 % sobre base $10.000.000 ($250.000) y reteICA ($65.000)
**Output:** descomposición capital $11.585.000 + retenciones $315.000 = $11.900.000; FV-101 y FV-102 cerradas al 100 %; retenciones registradas en 1355/135518 con concepto, base y tarifa; notificación a EspecialistaRetenciones; aging actualizado el mismo día; asiento cuadrado a AuxContable.
### Test 2 — (excepción, variante D) Proveedor descuenta 3 % por pronto pago pero la transferencia salió 2 días después del plazo pactado de 10 días
**Output:** descuento NO reconocido automáticamente; diferencia de 3 % reportada a AtencionCliente como saldo abierto con la evidencia de fecha valor; la factura queda parcial por el valor del descuento no aceptado; si el área comercial decide condonarlo, se aplica con esa instrucción escrita como soporte.

═══════════════════════════════════════════════════════════════════════

---
name: generar-aging-cartera
description: Skill base de aging. Variante CxC (clientes, cubetas 0-30/31-60/61-90/91-180/181-360/+360 días) y variante CxP (proveedores, vencido y por vencer a 7/14/30 días). Activa al cierre mensual y ad-hoc por solicitud de Tesoreria, Financiero o el cierre.
agente: RITORE-AuxiliarCarteraCxP-Senior
categoria: operativo
---

# Skill: generar-aging-cartera

## Para qué existe
El aging es el insumo único del que dependen la alerta de cartera vencida, el deterioro NIIF, la circularización y la programación de pagos de Tesoreria. Sin aging confiable, todos esos procesos trabajan sobre saldos ciegos.

## Cuándo se activa (por variante)

| Variante | Trigger |
|---|---|
| **CxC — clientes** | Cron del cierre mensual (D+2); solicitud de Financiero, AtencionCliente o `calcular-deterioro-cartera` |
| **CxP — proveedores** | Cron semanal (lunes, antes de `programar-pagos-semanales` de Tesoreria); cierre mensual |

## Inputs

| Insumo | De quién | Formato | Si falta |
|---|---|---|---|
| Saldos abiertos por tercero y factura con fecha de emisión y vencimiento | Módulo CxC/CxP del ERP | Export tabla | Si el módulo no responde en 4 h, usar último aging verificado con marca `[DATO EN CACHÉ — verificar]` y escalar en paralelo |
| Condiciones de pago por tercero (plazo pactado) | Maestro de terceros | Campo del maestro | Facturas sin plazo: asumir vencimiento = fecha de emisión + 30 días con marca `[PLAZO ASUMIDO]` y pedir corrección del maestro |
| Pagos aplicados hasta la fecha de corte | `aplicar-pago-a-tercero` | Registros propios | Verificar que no haya pagos en cuenta puente que distorsionen; si los hay, revelarlos en el informe |

## Procedimiento
1. Fijar fecha de corte y congelar la base (el aging no se regenera con movimientos posteriores al corte).
2. Calcular edad de cada factura = fecha de corte − fecha de vencimiento (no fecha de emisión).
3. Clasificar por cubeta según la variante: CxC → 0-30 / 31-60 / 61-90 / 91-180 / 181-360 / +360 días de vencida (las cubetas 91-180-360 alimentan el deterioro); CxP → vencido / por vencer 0-7 / 8-14 / 15-30 días.
4. Cruzar el total del aging contra el saldo de las cuentas PUC 13 (CxC) o 22 (CxP) del balance de prueba a la misma fecha. Diferencia tolerada $0.
5. Variante CxC: marcar terceros con cartera +60 días que superen el umbral de `alertar-cartera-vencida` y dispararle el caso; marcar cubetas +90/+180/+360 para `calcular-deterioro-cartera`.
6. Variante CxP: marcar facturas vencidas (riesgo de intereses de mora y bloqueo de proveedor) y vencimientos de los próximos 14 días; entregar a Tesoreria antes del lunes 8 a.m.
7. Publicar el informe a Financiero (CxC mensual) o Tesoreria (CxP semanal) y registrar en el bus.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Aging por tercero y factura con cubetas | Total del aging = saldo PUC 13/22 del balance de prueba a la fecha de corte, diferencia $0 |
| Marcas para skills conexas (alerta, deterioro, pagos) | Cada tercero/cubeta que cruza umbral tiene su skill destino registrada en el bus |
| Listado de excepciones | Facturas con `[PLAZO ASUMIDO]` o pagos en cuenta puente revelados explícitamente |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Aging no cuadra contra balance de prueba | Pagos en cuenta puente, NC sin aplicar o asientos manuales directos a la cuenta 13/22 | Identificar las partidas conciliatorias una a una antes de publicar | Publicar con sección "diferencias identificadas" cuantificada y escalar a AuxContable la depuración |
| Facturas con edad negativa enorme o fecha de vencimiento futura irreal | Error de digitación de fechas en el ERP | Corregir contra el documento fuente (factura/condiciones) | Excluir del aging con marca `[FECHA EN REVISIÓN]` y listar en excepciones |
| Tercero duplicado (mismo NIT con dos códigos) | Maestro de terceros sin depurar | Consolidar saldos bajo un solo código y pedir fusión del maestro | Reportar consolidado manualmente en el informe y registrar la depuración pendiente |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia aging vs balance de prueba | ≥ 1 UVT o ≥ 0,5 % del rubro | Investigar antes de publicar |
| Diferencia sin depurar | ≥ 50 UVT | AuxContable + Conciliador |
| Diferencia sin depurar | ≥ 500 UVT | Contador Titular vía Orquestador |
| Aging CxP no disponible para Tesoreria el lunes 8 a.m. | 1 incumplimiento | Orquestador (bloquea la programación de pagos) |

## Reglas críticas
🚫 NUNCA calcular la edad desde la fecha de emisión: siempre desde el vencimiento.
🚫 NUNCA publicar un aging que no cuadre contra el balance de prueba sin revelar la diferencia.
✅ SIEMPRE congelar la base a la fecha de corte (reproducibilidad del informe).

## Métricas
- Aging CxC publicado a más tardar D+2 del cierre: 100 % de los meses.
- Aging CxP entregado a Tesoreria antes del lunes 8 a.m.: ≥ 95 % de las semanas.
- Cuadre aging vs balance de prueba sin diferencias no explicadas: 100 %.
- Facturas con `[PLAZO ASUMIDO]`: ≤ 1 % del número de facturas (medición mensual).

## Tests
### Test 1 — (normal, variante CxC) Cierre de mayo: 48 facturas abiertas de 12 clientes por $310M; una factura de $18M lleva 95 días vencida
**Output:** aging con cubetas cuadrado contra la cuenta 13 del balance ($310M, diferencia $0); la factura de $18M clasificada en 91-180 y marcada para `calcular-deterioro-cartera`; el cliente correspondiente marcado para `alertar-cartera-vencida` si su +60d supera 5 SMMLV; informe a Financiero D+2.
### Test 2 — (excepción, variante CxP) El lunes, 6 facturas de un proveedor aparecen sin fecha de vencimiento porque el ERP no migró las condiciones de pago
**Output:** vencimiento asumido emisión + 30 días con marca `[PLAZO ASUMIDO]`, listadas en excepciones; aging entregado a Tesoreria a tiempo con la advertencia explícita; solicitud de corrección del maestro al responsable con plazo 24 h hábiles; en la semana siguiente las marcas deben haber desaparecido o se escala.

═══════════════════════════════════════════════════════════════════════

---
name: alertar-cartera-vencida
description: Activa cuando la cartera +60 días de un cliente supera el umbral (default 5 SMMLV ≈ $8.754.525 con SMMLV 2026). Notifica a AtencionCliente para gestión de cobro y escala si no hay gestión.
agente: RITORE-AuxiliarCarteraCxP-Senior
categoria: operativo
---

# Skill: alertar-cartera-vencida

## Para qué existe
La cartera vencida que nadie gestiona se convierte en deterioro y luego en castigo. Esta skill convierte el dato del aging en una acción de cobro con responsable y plazo, y vigila que la gestión ocurra.

## Cuándo se activa
- `generar-aging-cartera` (variante CxC) marca un cliente cuya cartera +60 días supera el umbral del perfil (default **5 SMMLV** = $8.754.525 con SMMLV 2026 $1.750.905; el perfil del cliente puede fijar otro umbral con justificación).
- Reincidencia: cliente ya alertado cuya cartera +60d crece ≥ 20 % entre cortes.
- Solicitud directa de Financiero o del dueño.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Aging CxC del corte con detalle por factura | `generar-aging-cartera` | Sin aging del corte NO se alerta sobre datos viejos: pedir regeneración (espera 24 h hábiles, luego Orquestador) |
| Umbral de alerta del perfil del cliente | `cargar-perfil-cliente` | Aplicar default 5 SMMLV y dejar nota de que se usó el default |
| Historial de gestiones de cobro previas | AtencionCliente | Alertar igual, marcando `[SIN HISTORIAL DE GESTIÓN]` |

## Procedimiento
1. Verificar el dato antes de alertar: confirmar que no hay pagos en cuenta puente ni NC pendientes que reduzcan el saldo real del tercero (falsos positivos queman la credibilidad de la alerta).
2. Construir la alerta: cliente, facturas vencidas con días y valores, total +60d, umbral superado, gestiones previas.
3. Enviar a AtencionCliente con plazo de primera gestión de cobro: 3 días hábiles.
4. Hacer seguimiento: si a los 3 días hábiles no hay gestión registrada, reiterar 1 vez.
5. Si la cartera cumple +90 días sin acuerdo de pago ni gestión efectiva, escalar al Director Comercial con el expediente (facturas, gestiones, respuesta del cliente).
6. Si hay acuerdo de pago, registrar fechas comprometidas y vigilar cumplimiento en cada corte siguiente; incumplimiento del acuerdo reactiva la alerta en nivel escalado.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Alerta a AtencionCliente | Incluye detalle por factura, total +60d, umbral, historial; verificada contra pagos pendientes de aplicar |
| Registro de seguimiento | Cada alerta tiene estado: gestionada / acuerdo de pago / escalada, con fechas |
| Expediente de escalamiento (+90d) | Cronología completa de gestiones para el Director Comercial |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Cliente alega que ya pagó | Pago en cuenta puente sin identificar o consignación no notificada por el banco | Cruzar con Conciliador y con `aplicar-pago-a-tercero` antes de insistir | Suspender la alerta 48 h con marca `[PAGO ALEGADO EN VERIFICACIÓN]`; si no aparece el pago, reactivar con la evidencia |
| Alerta repetida sobre cartera en disputa comercial (garantías, devoluciones) | La factura está objetada por el cliente | Marcar las facturas en disputa y separarlas del cobro ordinario; notificar a AtencionCliente la disputa | Mantener la disputa visible en cada aging y pedir resolución comercial con plazo; la disputa NO detiene el cómputo de edad para deterioro |
| AtencionCliente no registra gestión | Sobrecarga o caso huérfano | Reiterar 1 vez con copia al Orquestador | Escalar al Orquestador como SLA incumplido (24 h) |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Cartera +60d del cliente | > 5 SMMLV (o umbral del perfil) | AtencionCliente — gestión de cobro, plazo 3 días hábiles |
| Cartera +90d sin gestión efectiva ni acuerdo | Cualquier monto ya alertado | Director Comercial con expediente |
| Cartera +60d de un solo cliente | ≥ 500 UVT (~$26,2M) | Contador Titular vía Orquestador (riesgo de concentración) |
| Incumplimiento de acuerdo de pago | 1.ª cuota incumplida | Director Comercial directamente |

## Reglas críticas
🚫 NUNCA alertar sin verificar antes pagos en cuenta puente y NC pendientes (falsos positivos destruyen la credibilidad del sistema de alertas).
🚫 NUNCA gestionar el cobro directamente con el cliente final (eso es de AtencionCliente; yo alerto y vigilo).
✅ SIEMPRE dejar trazabilidad de cada alerta y su desenlace (gestión, acuerdo o escalamiento).

## Métricas
- Alertas emitidas dentro de las 24 h siguientes al aging que cruza umbral: 100 %.
- Falsos positivos (alertas desmentidas por pagos ya recibidos): ≤ 5 % de las alertas (medición trimestral).
- Casos +90d escalados a Director Comercial con expediente completo: 100 %.
- Cartera +60d sobre cartera total: ≤ 5 % (indicador del proceso completo, medición mensual).

## Tests
### Test 1 — (normal) El aging de corte marca al cliente DISTRIBUIDORA NORTE con $12.300.000 vencidos a +60 días (umbral 5 SMMLV = $8.754.525)
**Output:** verificación previa (sin pagos puente ni NC pendientes); alerta a AtencionCliente con 4 facturas detalladas, total, días de mora y ausencia de gestiones previas; plazo de primera gestión 3 días hábiles; registro de seguimiento abierto.
### Test 2 — (excepción) Cliente alertado responde con copia de consignación de hace 5 días que no aparece aplicada
**Output:** alerta suspendida con marca `[PAGO ALEGADO EN VERIFICACIÓN]`; cruce con el Conciliador encuentra el pago en cuenta puente sin NIT de referencia; se dispara `aplicar-pago-a-tercero`, el saldo +60d cae bajo el umbral y la alerta se cierra como falso positivo documentado (alimenta la métrica y la mejora del proceso de identificación de pagos).

═══════════════════════════════════════════════════════════════════════

---
name: calcular-deterioro-cartera
description: Activa al cierre mensual (cálculo) y al cierre anual (ajuste definitivo) para estimar el deterioro de cartera bajo NIIF — Sección 11 (PYMES, pérdida incurrida) o NIIF 9 (Plenas, pérdida esperada) — usando la matriz de antigüedad de la política del cliente, y para separarlo de la provisión fiscal del Art. 145 ET.
agente: RITORE-AuxiliarCarteraCxP-Senior
categoria: operativo
---

# Skill: calcular-deterioro-cartera

## Para qué existe
Una cartera sin deterioro reconocido sobrevalúa el activo y el resultado. Además, el deterioro contable NIIF y la provisión deducible fiscal (Art. 145 ET) siguen reglas distintas: si no se calculan por separado, la conciliación fiscal y el impuesto diferido salen errados.

## Cuándo se activa
- Cron del cierre mensual (D+3), después de `generar-aging-cartera` variante CxC.
- Cierre anual: ajuste definitivo y papel de trabajo para EspecialistaNIIF y EspecialistaRenta.
- Evento individual: cliente en insolvencia (Ley 1116), liquidación, fallecimiento o incobrabilidad manifiesta, sin importar la edad de la cartera.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Aging CxC por factura con cubetas 91-180 / 181-360 / +360 | `generar-aging-cartera` | Sin aging del corte NO se calcula deterioro; pedir regeneración (24 h hábiles, luego Orquestador) |
| Política de deterioro del cliente (matriz % por edad, marco Plenas/PYMES) | `cargar-perfil-cliente` | Aplicar matriz default del perfil (tabla del procedimiento) con marca `[POLÍTICA DEFAULT]` y escalar a EspecialistaNIIF para que el cliente formalice la suya |
| Evidencia de eventos individuales (autos de insolvencia, comunicaciones de liquidador) | AtencionCliente / cliente | El evento sin evidencia se documenta como indicio y NO se deteriora individualmente hasta soportarlo |
| Garantías o colaterales asociados a la cartera | Cliente | Asumir cartera sin garantía (deterioro más conservador) y dejar nota |

## Procedimiento
1. Tomar el aging congelado del corte y excluir: anticipos, saldos con partes relacionadas que se evalúan aparte, y cartera ya castigada.
2. Aplicar la matriz de la política del cliente. **Matriz default del perfil** (si el cliente no tiene política propia formalizada):

| Edad de vencida | % de deterioro |
|---|---|
| 91–180 días | 25 % |
| 181–360 días | 50 % |
| > 360 días | 100 % |

   `[VERIFICAR]` La matriz default es guía práctica de la firma, no norma: la política formal de cada cliente prevalece, y bajo NIIF 9 (Plenas) la matriz debe calibrarse con pérdida histórica + información prospectiva, no solo edad.
3. Deterioro individual por evento: cliente en insolvencia/liquidación → evaluar 100 % del saldo expuesto (neto de garantías reales soportadas) sin esperar la edad.
4. Comparar el deterioro requerido contra el saldo de la cuenta correctora (1399): el ajuste del periodo es la diferencia (gasto si sube, recuperación si baja).
5. Calcular EN PARALELO la provisión fiscal deducible (Art. 145 ET y DUR 1625/2016: provisión individual hasta 33 % anual o general por edades 5 %/10 %/15 %) — solo para cartera de operaciones productoras de renta, con más de un año de vencida en la individual. `[VERIFICAR aplicación por cliente con EspecialistaRenta]`.
6. Documentar la diferencia contable vs fiscal como diferencia temporaria para impuesto diferido (papel a EspecialistaNIIF y EspecialistaRenta).
7. Proponer asiento a AuxContable (gasto deterioro 5199 contra 1399, o reversión). El castigo definitivo (retiro de la cartera) NO es de esta skill: requiere aprobación del Contador Titular y soportes de cobro agotado.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Papel de deterioro por tercero y factura | Cada factura deteriorada tiene edad, % aplicado y fuente del % (política del cliente o default marcado) |
| Asiento de ajuste del periodo | Movimiento de 1399 = deterioro requerido − saldo previo, cuadrado |
| Papel contable vs fiscal | Deterioro NIIF y provisión Art. 145 ET calculados por separado; diferencia temporaria cuantificada |
| Marcas de eventos individuales | Casos de insolvencia con evidencia referenciada |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Cartera en disputa comercial dentro de la base de cálculo | Cliente objeta facturas (devoluciones, garantías) | Mantenerla en la base (la disputa no mejora la recuperabilidad) pero revelarla por separado | Escalar el criterio a EspecialistaNIIF si la disputa supera 50 UVT |
| Cliente de la firma pide "no deteriorar este año" para no afectar resultados | Presión sobre el resultado | Explicar que el deterioro es de norma, no opcional; calcular y presentar igual | Presentar el cálculo a EspecialistaNIIF y al Contador Titular con la solicitud del cliente documentada; el cálculo NO se omite |
| Recuperación de cartera ya deteriorada al 100 % | Pago inesperado de un tercero deteriorado | Reversar el deterioro contra resultados en el periodo del pago (no reexpresar) | Si el monto ≥ 50 UVT, validar el tratamiento con EspecialistaNIIF |
| Matriz fiscal aplicada como contable (o viceversa) | Confusión 145 ET vs política NIIF | Recalcular por separado; corregir el papel | Escalar a EspecialistaNIIF + EspecialistaRenta con ambos cálculos |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Ajuste de deterioro del periodo | ≥ 50 UVT | EspecialistaNIIF antes de asentar |
| Ajuste del periodo o deterioro individual por insolvencia | ≥ 500 UVT | Contador Titular vía Orquestador |
| Castigo definitivo de cartera (retiro del activo) | Cualquier monto | Contador Titular (decisión fuera del alcance de esta skill) |
| Cliente sin política de deterioro formalizada | Tras 2.º cierre usando default | EspecialistaNIIF para formalizar la política |

## Reglas críticas
🚫 NUNCA mezclar el deterioro contable NIIF con la provisión fiscal del Art. 145 ET: son dos cálculos, dos papeles.
🚫 NUNCA castigar cartera (retirarla) desde esta skill: solo deterioro; el castigo lo aprueba el Contador Titular.
🚫 NUNCA omitir el cálculo por solicitud del cliente: se calcula, se presenta y la decisión escalada queda documentada.
✅ SIEMPRE deteriorar individualmente y de inmediato la cartera de terceros en insolvencia o liquidación, sin esperar la edad.

## Métricas
- Cierres mensuales con deterioro calculado a D+3: 100 %.
- Facturas +360 días sin deterioro al 100 % (o sin justificación de garantía documentada): 0.
- Diferencia temporaria contable-fiscal documentada en el papel anual: 100 %.
- Eventos de insolvencia evaluados dentro de los 5 días hábiles de conocidos: 100 %.

## Tests
### Test 1 — (normal) Corte de junio: factura de $18M con 200 días de vencida y factura de $7M con 95 días, cliente PYMES con matriz default; saldo previo de la 1399: $2.500.000
**Output:** deterioro requerido = $18M × 50 % + $7M × 25 % = $10.750.000; ajuste del periodo = $10.750.000 − $2.500.000 = $8.250.000 a gasto; papel por factura con marca `[POLÍTICA DEFAULT]`; cálculo fiscal Art. 145 ET por separado (solo la factura > 360 días calificaría a individual 33 % — aquí ninguna, se evalúa la general); diferencia temporaria documentada; como el ajuste supera 50 UVT ($2.618.700), validación de EspecialistaNIIF antes de asentar.
### Test 2 — (excepción) AtencionCliente informa que un cliente con $40M de cartera de solo 45 días de vencida fue admitido a reorganización (Ley 1116)
**Output:** deterioro individual evaluado de inmediato pese a la edad < 90 días; con el auto de admisión como evidencia, propuesta de deterioro del 100 % del saldo no garantizado; por superar 500 UVT, escalamiento a Contador Titular vía Orquestador antes de asentar; marca del tercero para excluirlo de la matriz por edades (no duplicar deterioro); notificación a EspecialistaRenta (la deducción fiscal sigue reglas propias y no es automática).

═══════════════════════════════════════════════════════════════════════

---
name: conciliar-con-tercero-externo
description: Activa al cierre mensual para terceros con saldo ≥ 50 UVT, al cierre anual para la circularización formal (top de terceros y muestra del Revisor Fiscal), y ad-hoc ante disputas. Solicita confirmación de saldos, cruza las respuestas y resuelve diferencias.
agente: RITORE-AuxiliarCarteraCxP-Senior
categoria: operativo
---

# Skill: conciliar-con-tercero-externo

## Para qué existe
El saldo que el tercero confirma es la mejor evidencia externa de que la cartera y las CxP existen y están completas. La circularización detecta facturas no recibidas, pagos no aplicados por la contraparte y disputas latentes antes de que lleguen al cierre o al dictamen.

## Cuándo se activa
- Cierre mensual: terceros con saldo ≥ 50 UVT o con movimientos inusuales en el mes.
- Cierre anual: circularización formal — el top de terceros que acumule ≥ 80 % del saldo de CxC y de CxP, más la muestra que pida el Revisor Fiscal.
- Ad-hoc: disputa de saldo reportada por AtencionCliente o por el tercero.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Estado de cuenta del tercero a la fecha de corte (facturas, pagos, NC/ND, saldo) | Módulo CxC/CxP + registros propios | Caché con marca `[DATO EN CACHÉ — verificar]` si el módulo no responde en 4 h |
| Datos de contacto del tercero | Maestro de terceros / AtencionCliente | Pedir a AtencionCliente; sin contacto válido, registrar el intento fallido y usar procedimiento alternativo (paso 6) |
| Respuesta del tercero (confirmación o detalle de diferencias) | Tercero vía AtencionCliente | Reiterar a los 5 días hábiles; segunda reiteración a los 10; sin respuesta, procedimiento alternativo |

## Procedimiento
1. Generar el estado de cuenta del tercero a la fecha de corte desde los registros propios (nunca pedirle al tercero que "mande su saldo" sin enviar el nuestro: la confirmación es contra nuestra cifra).
2. Enviar vía AtencionCliente con solicitud de confirmación o detalle de diferencias, plazo de respuesta 5 días hábiles (cierre mensual) o el plazo del calendario de circularización (anual).
3. Recibir respuesta y clasificar: conforme / diferencia.
4. Si hay diferencia, construir la conciliación partida a partida: facturas que el tercero no tiene registradas, pagos que nosotros no hemos aplicado, NC/ND pendientes, diferencias de fecha de corte (pagos en tránsito).
5. Resolver lo propio (disparar `aplicar-pago-a-tercero` o solicitar registro de NC a AuxContable) y solicitar al tercero corrección de lo suyo.
6. Sin respuesta tras 2 reiteraciones: aplicar procedimiento alternativo — validar el saldo contra movimientos posteriores al corte (pagos recibidos/efectuados que confirman la existencia del saldo) y documentarlo como "confirmación alternativa".
7. Archivar la conciliación con el soporte de la respuesta (o del procedimiento alternativo) y reportar el resultado consolidado a Financiero (mensual) o al expediente de cierre (anual).

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Acta de conciliación por tercero | Saldo propio, saldo del tercero, diferencias partida a partida, responsable de cada corrección |
| Resolución de diferencias propias | Cada partida nuestra tiene skill destino disparada o asiento solicitado |
| Consolidado de circularización (anual) | % de cobertura del saldo confirmado ≥ 80 % en valor; no respondidos con procedimiento alternativo documentado |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| El tercero confirma un saldo mayor (facturas que no tenemos registradas) | Facturas no recibidas o no causadas por AuxContable | Solicitar copia de las facturas y disparar la causación con AuxContable | Registrar la diferencia como pasivo estimado si hay evidencia suficiente y escalar a AuxContable; nunca ignorarla |
| El tercero confirma un saldo menor (pagos que no hemos aplicado) | Pagos en cuenta puente o consignaciones sin identificar | Cruzar con Conciliador y `aplicar-pago-a-tercero` | Mantener la diferencia abierta con marca y plazo; si supera 50 UVT, escalar |
| Respuesta del tercero llega de un contacto no verificable | Riesgo de confirmación apócrifa (fraude) | Validar el remitente contra el contacto del maestro; pedir confirmación por canal conocido | Marcar la confirmación como `[NO VERIFICADA]` y no usarla como evidencia de cierre |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia confirmada con tercero | ≥ 1 UVT o ≥ 0,5 % del saldo del tercero | Investigar y conciliar partida a partida |
| Diferencia sin resolver tras conciliación | ≥ 50 UVT | AuxContable + Conciliador según el origen |
| Diferencia sin resolver | ≥ 500 UVT | Contador Titular vía Orquestador |
| Cobertura de circularización anual < 80 % del saldo en valor | Al cierre del calendario | Orquestador + nota al Revisor Fiscal |

## Reglas críticas
🚫 NUNCA dar por conciliado un saldo con una respuesta de contacto no verificado.
🚫 NUNCA ajustar registros propios solo porque el tercero dice otra cifra: toda corrección exige soporte documental.
✅ SIEMPRE enviar nuestro estado de cuenta como base de la confirmación (la carga de la diferencia queda explícita).

## Métricas
- Terceros ≥ 50 UVT circularizados en el cierre mensual: 100 %.
- Tasa de respuesta de circularización anual: ≥ 70 % en número, con cobertura ≥ 80 % del saldo en valor.
- Diferencias resueltas (o escaladas con plan) antes del siguiente corte: ≥ 90 %.

## Tests
### Test 1 — (normal) Circularización mensual: proveedor con saldo CxP de $35M responde confirmando $38,2M
**Output:** conciliación partida a partida detecta una factura de $3,2M emitida el 28 del mes que no llegó a causación; se solicita copia, se dispara la causación con AuxContable y se confirma el saldo conciliado; acta archivada con la respuesta del proveedor como soporte y diferencia resuelta antes del siguiente corte.
### Test 2 — (excepción) Cliente con saldo CxC de $60M no responde tras 2 reiteraciones en 10 días hábiles
**Output:** procedimiento alternativo: se validan pagos posteriores al corte por $22M que confirman la existencia de la cartera, y se documenta la confirmación alternativa por esa porción; el saldo restante queda `[NO CONFIRMADO]` en el consolidado; como el tercero está en el top de circularización anual, nota al expediente de cierre y al Revisor Fiscal; AtencionCliente registra la falta de respuesta como insumo de la relación comercial.

═══════════════════════════════════════════════════════════════════════

---
name: detectar-saldos-naturaleza-contraria
description: Activa al cierre mensual (D+2) para detectar saldos crédito en cuentas de clientes (13) o saldos débito en proveedores (22) — señal de anticipo no legalizado, pago duplicado, NC sin procesar o error de imputación. Investiga, clasifica y resuelve cada caso.
agente: RITORE-AuxiliarCarteraCxP-Senior
categoria: operativo
---

# Skill: detectar-saldos-naturaleza-contraria

## Para qué existe
Un cliente con saldo crédito o un proveedor con saldo débito es siempre un síntoma: anticipo sin legalizar, pago duplicado, nota crédito sin aplicar o imputación errada. Si no se investiga, los EEFF presentan activos y pasivos compensados indebidamente y los errores se vuelven invisibles.

## Cuándo se activa
- Cron del cierre mensual (D+2, junto con el aging).
- En línea: `aplicar-pago-a-tercero` deja un tercero con saldo contrario tras una aplicación.
- Solicitud de AuxContable, Financiero o el Revisor Fiscal.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Saldos por tercero de cuentas 13 (CxC) y 22 (CxP) a la fecha de corte | Módulo CxC/CxP | Caché con marca `[DATO EN CACHÉ — verificar]` si no responde en 4 h, y escalar en paralelo |
| Movimientos del tercero del periodo (facturas, pagos, NC/ND) | Módulo + `aplicar-pago-a-tercero` | Investigar con lo disponible y marcar el caso `incompleto` |
| Política de presentación del cliente (reclasificación de anticipos) | `cargar-perfil-cliente` | Reclasificar según PUC estándar (2805 anticipos de clientes / 1330 anticipos a proveedores) y dejar nota |

## Procedimiento
1. Query de saldos por tercero; filtrar clientes con saldo crédito y proveedores con saldo débito (a nivel de tercero Y a nivel de factura: un tercero puede netear internamente errores).
2. Clasificar cada caso por causa probable: (a) anticipo no legalizado, (b) pago duplicado del tercero, (c) NC/ND sin procesar, (d) imputación errada, (e) factura propia sin causar.
3. Resolver según la causa: (a) → disparar `gestionar-anticipo-cliente-proveedor` para reclasificar y legalizar; (b) → confirmar con Conciliador y notificar a Tesoreria/AtencionCliente la devolución o cruce; (c) → solicitar procesamiento a AuxContable; (d) → corregir la imputación en `aplicar-pago-a-tercero` con trazabilidad; (e) → disparar causación.
4. Para presentación de EEFF: los saldos contrarios legítimos (anticipos) se reclasifican a su cuenta correcta (2805/1330) — no se presentan neteados.
5. Emitir informe del corte: casos detectados, causa, acción, casos resueltos vs pendientes con responsable y plazo.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Informe de saldos contrarios del corte | 100 % de los casos con causa clasificada y acción disparada |
| Reclasificaciones propuestas a AuxContable | Anticipos legítimos en 2805/1330; ningún neteo indebido en presentación |
| Seguimiento de pendientes | Cada caso no resuelto tiene responsable y plazo ≤ siguiente corte |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Saldo contrario "histórico" que nadie explica (arrastrado varios cierres) | Error de ejercicios anteriores sin depurar | Reconstruir el movimiento del tercero hacia atrás hasta el origen | Si el origen está en ejercicios cerrados, escalar a AuxContable/EspecialistaNIIF (posible corrección NIC 8) en vez de "ajustar contra resultados" |
| Pago duplicado que el tercero pide aplicar a facturas futuras | Cliente prefiere cruce a devolución | Documentar la instrucción escrita del tercero y reclasificar a anticipo | Sin instrucción escrita, mantener como pasivo (pago duplicado por devolver) y notificar a Tesoreria |
| El mismo caso reaparece cada mes (causa raíz no corregida) | Proceso de imputación o causación con defecto recurrente | Documentar el patrón y proponer corrección de proceso al Orquestador | Registrar en el informe como `recurrente` con conteo de meses |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Saldo contrario individual | ≥ 1 UVT | Investigar y clasificar antes del cierre |
| Saldo contrario sin causa identificada al cierre | ≥ 50 UVT | AuxContable + Conciliador |
| Saldo contrario sin resolver | ≥ 500 UVT | Contador Titular vía Orquestador |
| Casos recurrentes (mismo origen ≥ 3 cierres) | — | Orquestador (defecto de proceso) |

## Reglas críticas
🚫 NUNCA netear saldos contrarios en la presentación de EEFF: los anticipos van a su cuenta (2805/1330).
🚫 NUNCA "ajustar contra resultados" un saldo contrario inexplicado: sin causa identificada no hay asiento.
✅ SIEMPRE revisar a nivel de factura, no solo de tercero (los neteos internos esconden errores).

## Métricas
- Cierres con barrido de saldos contrarios ejecutado a D+2: 100 %.
- Casos clasificados con causa en el mismo corte: ≥ 95 %.
- Casos pendientes que cruzan más de 2 cierres: 0.
- Reclasificaciones de anticipos propuestas antes de la emisión de EEFF del mes: 100 %.

## Tests
### Test 1 — (normal) En el corte aparece el cliente FERRETERÍA SUR con saldo crédito de $4.200.000
**Output:** investigación encuentra consignación del cliente del día 28 por pedido aún no facturado; clasificación: anticipo no legalizado; disparo de `gestionar-anticipo-cliente-proveedor` para reclasificar a 2805; informe del corte con el caso resuelto; al facturarse el pedido el mes siguiente, el anticipo se legaliza contra la factura.
### Test 2 — (excepción) Proveedor con saldo débito de $9.800.000 arrastrado desde hace 4 cierres sin explicación; la reconstrucción muestra un pago duplicado de noviembre del año anterior (ejercicio ya cerrado)
**Output:** causa identificada: pago duplicado en ejercicio cerrado; NO se ajusta contra resultados del periodo actual por cuenta propia; caso escalado a AuxContable/EspecialistaNIIF para evaluar tratamiento (cuenta por cobrar al proveedor vs corrección de ejercicios anteriores); a Tesoreria/AtencionCliente se solicita gestionar la devolución o cruce con el proveedor; el caso queda `recurrente` con responsable y deja de arrastrarse sin dueño.

═══════════════════════════════════════════════════════════════════════

---
name: gestionar-anticipo-cliente-proveedor
description: Activa cuando se recibe un anticipo de cliente (pasivo 2805) o se entrega un anticipo a proveedor (activo 1330). Registra, controla la antigüedad y legaliza contra la factura cuando la operación se ejecuta.
agente: RITORE-AuxiliarCarteraCxP-Senior
categoria: operativo
---

# Skill: gestionar-anticipo-cliente-proveedor

## Para qué existe
Un anticipo es dinero que aún no es ingreso (recibido) o que aún no es costo/gasto (entregado). Si no se controla, los anticipos envejecen sin legalizar: ingresos que se reconocen tarde, IVA que se factura tarde y anticipos a proveedores que terminan siendo cartera incobrable disfrazada de activo.

## Cuándo se activa
- Recepción de anticipo de cliente confirmada por el Conciliador (o excedente de `aplicar-pago-a-tercero`).
- Entrega de anticipo a proveedor aprobada por Tesoreria (orden de compra o contrato que lo pacta).
- Legalización: emisión/recepción de la factura de la operación anticipada.
- Cron mensual: revisión de antigüedad de anticipos sin legalizar.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Soporte del anticipo (contrato, orden de compra, cotización aceptada, instrucción del tercero) | Cliente / Tesoreria / AtencionCliente | Sin soporte el dinero recibido queda en cuenta puente `[PAGO POR IDENTIFICAR]`, no en anticipos; reiterar 1 vez en 24 h hábiles, luego Orquestador |
| Confirmación del pago (recibido o efectuado) | Conciliador / Tesoreria | Sin confirmación bancaria NO se registra el anticipo |
| Factura de legalización | AuxContable / proveedor | Mientras no llegue, el anticipo permanece en 2805/1330 con su antigüedad corriendo |

## Procedimiento
1. Registrar el anticipo: de cliente → crédito 2805 (pasivo); a proveedor → débito 1330 (activo). Asociar siempre el soporte (contrato/OC) y el tercero.
2. Anticipo de cliente: validar con EspecialistaIVA si el anticipo pactado genera obligación de facturar (anticipo que es pago anticipado del precio vs anticipo para gastos por cuenta del cliente — tratamiento distinto). `[VERIFICAR caso a caso]`.
3. Al ejecutarse la operación: legalizar — aplicar el anticipo contra la factura emitida/recibida; el remanente se factura/paga, o se devuelve si la operación fue menor.
4. Si la operación se cancela: gestionar devolución vía Tesoreria (cliente) o recuperación del anticipo al proveedor; nunca dejar el saldo "durmiendo".
5. Cron mensual de antigüedad: listar anticipos sin legalizar > 90 días; pedir estado de la operación a AtencionCliente (clientes) o al área de compras del cliente (proveedores).
6. Anticipos a proveedor > 180 días sin avance de la operación: evaluar como cuenta de difícil recuperación → marcar para `calcular-deterioro-cartera` (evaluación individual) y escalar.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Registro del anticipo | En 2805/1330 con soporte asociado y tercero identificado; nunca neteado contra cartera/CxP del mismo tercero |
| Legalización | Anticipo aplicado contra factura; remanente facturado, pagado o devuelto; saldo del anticipo en $0 al cerrar la operación |
| Informe mensual de antigüedad | 100 % de anticipos > 90 días con estado y acción |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Anticipo de cliente facturado dos veces (al recibirlo y al legalizar) | Confusión sobre el momento de facturación del IVA | Validar tratamiento con EspecialistaIVA; anular el documento duplicado con NC | Escalar a EspecialistaIVA con ambos documentos antes del cierre del periodo de IVA |
| Proveedor recibió anticipo y no entrega ni responde | Riesgo de incumplimiento contractual | Reportar a AtencionCliente/cliente para gestión contractual; documentar gestiones | A los 180 días sin avance, marcar para evaluación de deterioro individual y escalar al Contador Titular si ≥ 50 UVT |
| Anticipo legalizado contra una factura de otra operación | Imputación cruzada entre proyectos/OC del mismo tercero | Corregir la legalización referenciando la OC correcta | Congelar ambos registros con marca `[LEGALIZACIÓN EN REVISIÓN]` y resolver antes del cierre |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Anticipo sin legalizar | > 90 días | AtencionCliente / área de compras — estado de la operación |
| Anticipo a proveedor sin avance de operación | > 180 días o ≥ 50 UVT | Evaluación de deterioro individual + Contador Titular si ≥ 50 UVT |
| Anticipo individual | ≥ 500 UVT | Contador Titular vía Orquestador (registro y seguimiento reforzado) |
| Soporte del anticipo faltante | > 24 h hábiles tras reiterar 1 vez | Orquestador |

## Reglas críticas
🚫 NUNCA registrar como anticipo un dinero sin soporte de la operación pactada (eso es `[PAGO POR IDENTIFICAR]`).
🚫 NUNCA netear anticipos contra cartera o CxP del mismo tercero en presentación.
✅ SIEMPRE correr el reloj de antigüedad desde el registro y revisarlo cada cierre mensual.

## Métricas
- Anticipos registrados con soporte asociado: 100 %.
- Anticipos > 90 días sin legalizar sobre el total de anticipos: ≤ 10 % en valor (medición mensual).
- Anticipos > 180 días sin plan de acción documentado: 0.
- Legalizaciones aplicadas dentro del mes de emisión de la factura: ≥ 95 %.

## Tests
### Test 1 — (normal) Cliente consigna $15M como anticipo del 50 % de un pedido según OC aceptada; 40 días después se factura el pedido por $30M + IVA
**Output:** registro inicial crédito 2805 con la OC como soporte; validación del tratamiento de IVA del anticipo con EspecialistaIVA; al facturar, legalización del anticipo contra la factura ($15M aplicados, saldo por cobrar $15M + IVA según el caso); 2805 en $0 para esa operación; notificación a AuxContable y Tesoreria.
### Test 2 — (excepción) El cron mensual encuentra un anticipo a proveedor de $22M con 200 días de antigüedad; compras informa que el proveedor incumplió y no responde
**Output:** el anticipo NO permanece como activo sano: gestiones documentadas (reclamaciones, correos), marca para evaluación de deterioro individual en `calcular-deterioro-cartera`; por superar 50 UVT, escalamiento al Contador Titular con el expediente (OC, pagos, gestiones de cobro) para decidir acción contractual/jurídica; el informe mensual lo presenta como riesgo cuantificado, no como anticipo corriente.

═══════════════════════════════════════════════════════════════════════

## Relacionado
- *MOC - Agentes RITORE*
- *Proyecto - Ecosistema RITORE*
- [[00 - Estandar de Agentes RITORE]]
- [[Skills Compartidas RITORE]]
- [[06-AuxiliarTesoreria-Senior]]
- *12-EspecialistaRetenciones-Senior*
- *22-AtencionCliente-Senior*

## Historial de versiones
| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-05-19 | Versión inicial consolidada (10 skills) | RITORE |
| 2.0 | 2026-06-11 | Refactorización según Estandar de Agentes v1.0: deduplicación (10 → 7; aplicación de pagos consolidada en `aplicar-pago-a-tercero` con 4 variantes y aging en `generar-aging-cartera` con 2), nueva skill `calcular-deterioro-cartera` (matriz >90/180/360 días, NIIF vs Art. 145 ET), tests propios por skill, inputs/outputs, manejo de errores y umbrales numéricos §3 | RITORE |
