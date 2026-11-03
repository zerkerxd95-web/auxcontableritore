---
tipo: agente
tags: [ritore, agente, operativa]
capa: operativa
nivel: senior
estado: activo
version: 2.0
fecha: 2026-06-11
---

# SKILLS — 02-AuxiliarContable-Senior

**Documento consolidado** · 11 skills · Ecosistema RITORE · v2.0
**Modelo:** claude-opus-4-7

> Refactorización según [[00 - Estandar de Agentes RITORE]] (§2 secciones obligatorias, §3 umbrales, §4 anti-clonación). El contenido técnico de la v1.0 se conserva; se reemplazó toda vaguedad ("material", "significativo") por los umbrales numéricos del §3, se agregaron Inputs/Outputs y tablas de manejo de errores a cada skill, y `contabilizar-factura-electronica-recibida` + `contabilizar-factura-emitida` se consolidaron en una skill base con variantes (compartían > 70 % del procedimiento: cargar perfil → validar CUFE/CUDE → clasificar → IVA/retenciones → asiento → notificaciones). Las reglas universales (tipping-off, escalar a humano, documentar decisiones, verificar vigencia normativa) se heredan de [[Skills Compartidas RITORE]] y no se repiten aquí.

---

## Índice de skills en este documento

- `cerrar-mes-contable`
- `clasificar-partida-NIIF-vs-FISCAL`
- `contabilizar-costos-produccion`
- `contabilizar-depreciacion-mensual`
- `contabilizar-factura-electronica` *(base paramétrica: R — recibida · E — emitida)*
- `contabilizar-movimiento-bancario`
- `contabilizar-nomina-mensual`
- `corregir-asientos-detectados-erroneos`
- `documentar-criterio-contable-aplicado`
- `generar-libros-oficiales`
- `validar-plan-cuentas-cliente`

═══════════════════════════════════════════════════════════════════════

---
name: cerrar-mes-contable
description: Activa el día 5 hábil del mes siguiente como cierre del periodo contable. Valida checklist completo (conciliaciones, nómina, depreciaciones, inventarios, provisiones, marcas NIIF/fiscal), genera balance de prueba y marca el periodo como cerrado en el ERP. Sin esta skill el cierre mensual queda incompleto y los EEFF salen con errores.
agente: RITORE-AuxiliarContable-Senior
categoria: operativo
---

# Skill: cerrar-mes-contable

## Para qué existe
El cierre mensual es la compuerta de calidad de todo el ciclo: si se cierra con partidas abiertas o conciliaciones pendientes, los EEFF, las declaraciones y la exógena heredan el error. Esta skill garantiza que ningún periodo se marque como cerrado sin checklist completo y balance cuadrado.

## Cuándo se activa
- Cron: día 5 hábil del mes siguiente al periodo a cerrar.
- Solicitud de EstadosFinancieros (necesita el periodo cerrado para consolidar) o del Orquestador.
- Reapertura excepcional autorizada por el Contador Titular (cierre de un periodo de ajuste).

## Inputs

| Insumo | De quién | Formato | Si falta |
|---|---|---|---|
| Confirmación de conciliaciones bancarias completas | [[03-AuxiliarConciliacionesBancarias-Senior]] | Papeles de trabajo + estado OK | NO se cierra; reiterar 1 vez en 24 h hábiles, luego escalar al Orquestador |
| Aging de cartera y CxP cuadrado contra mayor | AuxiliarCarteraCxP | Reporte de aging | NO se cierra; mismo protocolo de espera 24 h hábiles |
| Nómina contabilizada + PILA pagada | Nómina (vía `contabilizar-nomina-mensual`) | Confirmación con soporte de pago PILA | NO se cierra hasta confirmación |
| Depreciaciones, inventarios reconciliados, Estado del Costo (si aplica), provisiones | ActivosFijos / AuxiliarInventarios / EspecialistaCostos | Confirmaciones de cada skill | Espera máx. 24 h hábiles; reiterar 1 vez; luego Orquestador |
| Partidas con marca `diferencia_NIIF_fiscal` del periodo | `clasificar-partida-NIIF-vs-FISCAL` | Listado con tags | Generar listado propio desde metadata y validar contra EspecialistaNIIF |

## Procedimiento
1. Verificar checklist completo (todos los inputs anteriores confirmados).
2. Generar balance de prueba pre-cierre.
3. Validar ecuación contable (A = P + Patrimonio) y que la suma de débitos = créditos del periodo.
4. Verificar que no existan partidas abiertas ≥ 1 UVT individual o cuyo acumulado sea ≥ 0,5 % del total de activos del cliente (umbral §3 del estándar; reemplaza el antiguo "partidas materiales").
5. Si todo OK: marcar periodo como cerrado en el ERP del cliente.
6. Notificar: EspecialistaNIIF (criterios complejos del periodo), EstadosFinancieros (puede consolidar), EspecialistaRenta (bases del periodo disponibles).
7. Archivar balance de prueba y acta de cierre vía NotionArquitecto.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Periodo cerrado en ERP | Checklist 100 % confirmado; sin partidas abiertas sobre el umbral del paso 4 |
| Balance de prueba pre-cierre archivado | Débitos = créditos; ecuación contable cumplida |
| Acta de cierre | Lista de verificaciones con responsable, fecha y resultado de cada ítem |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Descuadre en balance de prueba | Asiento descuadrado registrado por interfaz o ajuste manual | NO cerrar; rastrear el asiento por diferencia exacta y fecha | Activar `corregir-asientos-detectados-erroneos`; si no se resuelve en 24 h hábiles, escalar al Orquestador con el periodo bloqueado |
| Conciliación bancaria pendiente al día 5 | Extracto tardío o partidas sin resolver | NO cerrar; coordinar con el Conciliador y fijar nueva fecha (máx. +2 días hábiles) | Escalar al Orquestador; el cierre NO se simula con la cuenta sin conciliar |
| Agente proveedor de insumo no responde | Saturación o falla del bus | Timeout 4 h (§3); usar el último dato verificado con marca `[DATO EN CACHÉ — verificar]` SOLO para pre-cierre, nunca para cierre definitivo | Escalar en paralelo al Orquestador; el periodo queda `pre-cerrado` hasta confirmación |
| Partida abierta ≥ 1 UVT sin explicación | Documento pendiente o error de aplicación | Investigar y documentar antes de cerrar | Si tras investigar persiste y es ≥ 50 UVT, escalar al Contador Titular vía Orquestador con propuesta de tratamiento |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Partida abierta o descuadre | ≥ 1 UVT individual o ≥ 0,5 % del total | Investigar y documentar antes de cerrar (no se cierra) |
| Descuadre o ajuste de cierre | ≥ 50 UVT | EspecialistaNIIF o Master del dominio afectado |
| Descuadre o ajuste de cierre | ≥ 500 UVT | Contador Titular vía Orquestador |
| Cierre retrasado | > día 7 hábil | Orquestador (prioridad alta, SLA 4 h) |

## Reglas críticas
🚫 NUNCA cerrar con partidas abiertas ≥ 1 UVT sin investigar y documentar (umbral §3; prohibido el juicio "material" sin número).
🚫 NUNCA cerrar sin todas las notificaciones a especialistas confirmadas.
✅ SIEMPRE generar y archivar el balance de prueba previo al cierre.

## Métricas
- Cierres completados a más tardar el día 5 hábil: ≥ 95 % (medición mensual).
- Reaperturas de periodo por errores detectados después del cierre: ≤ 1 por trimestre por cliente.
- Checklist documentado en acta de cierre: 100 % de los cierres.

## Tests
### Test 1 — (normal) Checklist completo el día 4 hábil; balance de prueba cuadra; ninguna partida abierta ≥ 1 UVT
**Output:** periodo cerrado en ERP, acta de cierre con 8 verificaciones OK, balance archivado, notificaciones a EspecialistaNIIF, EstadosFinancieros y EspecialistaRenta emitidas.
### Test 2 — (excepción) El día 5 hábil hay un descuadre de 30 UVT y la conciliación de una de tres cuentas bancarias sigue pendiente
**Output:** cierre BLOQUEADO; descuadre rastreado (asiento de interfaz duplicado) y corregido vía `corregir-asientos-detectados-erroneos`; coordinación con el Conciliador con nueva fecha al día 7 hábil; 30 UVT < 50 UVT → no requiere Master, pero queda documentado en el acta; si al día 7 la conciliación siguiera pendiente, escalamiento al Orquestador.

═══════════════════════════════════════════════════════════════════════

---
name: clasificar-partida-NIIF-vs-FISCAL
description: Activa cuando una operación tenga tratamiento NIIF distinto al fiscal — provisiones, valor razonable, deterioro, leasing financiero, anticipos, instrumentos financieros. Identifica la diferencia, la marca y notifica a NIIF + Renta para impuesto diferido. Sin esta skill la diferencia se pierde y el F-2516 sale incorrecto.
agente: RITORE-AuxiliarContable-Senior
categoria: operativo
---

# Skill: clasificar-partida-NIIF-vs-FISCAL

## Para qué existe
El F-2516 (conciliación fiscal) y el impuesto diferido dependen de que cada diferencia contable-fiscal quede marcada en el momento del registro, no reconstruida al cierre del año. Una diferencia sin marcar es una diferencia perdida.

## Cuándo se activa
- Al contabilizar operaciones con divergencia potencial: provisiones, deterioro, valor razonable, leasing (NIIF 16 vs Art. 127-1 ET), anticipos de clientes, instrumentos financieros, depreciaciones con vidas útiles distintas.
- Alerta de otra skill de este perfil que detecte tratamiento divergente.
- Solicitud de EspecialistaRenta o EspecialistaNIIF durante la preparación del F-2516.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Operación a clasificar con su soporte | Skill de origen (factura, nómina, depreciación, etc.) | No se clasifica en abstracto: devolver a la skill de origen |
| Marco NIIF del cliente (plenas / Pymes) y políticas contables | `cargar-perfil-cliente` | Solicitar a NotionArquitecto; espera máx. 24 h hábiles, luego Orquestador |
| Criterio fiscal aplicable vigente | `verificar-vigencia-normativa` (compartida) | Marcar `[VERIFICAR]` y consultar a EspecialistaRenta antes de cerrar el periodo |

## Procedimiento
1. Identificar la operación con tratamientos divergentes potenciales (catálogo del trigger).
2. Asentar bajo NIIF — es lo que firma el Contador Titular; lo fiscal es conciliación, no registro.
3. Marcar la partida con tag `diferencia_NIIF_fiscal=true` en metadata, indicando tipo (temporaria / permanente) y monto estimado.
4. Notificar a EspecialistaNIIF (validación técnica) y a EspecialistaRenta (inclusión en F-2516 e impuesto diferido).
5. Si la diferencia es ≥ 50 UVT, documentar vía `documentar-decision-no-trivial` (compartida).

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Partida asentada bajo NIIF con tag de diferencia | Tag con tipo y monto; recuperable por consulta de metadata |
| Notificación a NIIF y Renta | Emitida en el mismo día hábil del registro |
| Documentación de la decisión (si ≥ 50 UVT) | Registrada con fundamento normativo de ambos tratamientos |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Duda sobre si existe divergencia NIIF/fiscal | Operación atípica o norma reciente | Consultar a EspecialistaNIIF ANTES de asentar (`consultar-a-especialista`) | Si NIIF no responde en 4 h (§3), asentar bajo NIIF con marca `[CRITERIO EN CONSULTA]` y NO emitir la marca fiscal hasta respuesta |
| Partida divergente detectada DESPUÉS de cerrado el periodo | Marca omitida en el registro original | Marcar retroactivamente y notificar a Renta con alcance del periodo afectado | Si el F-2516 ya se presentó, escalar a EspecialistaRenta para evaluar corrección de la declaración |
| Diferencia genera impuesto diferido ≥ 50 UVT | Operación de monto alto (deterioros, leasing) | Escalar a EspecialistaNIIF con prioridad alta (SLA 4 h) | Al 80 % del SLA sin respuesta → alerta al Orquestador; al 100 % → §3 |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia identificada | ≥ 1 UVT | Marcar y notificar (flujo normal) |
| Impuesto diferido estimado | ≥ 50 UVT | EspecialistaNIIF con prioridad alta |
| Diferencia o efecto en F-2516 | ≥ 500 UVT | Contador Titular vía Orquestador |
| Operación ambigua sin precedente | Cualquier monto | EspecialistaNIIF decide criterio (un Senior no crea criterios, §1) |

## Reglas críticas
🚫 NUNCA decidir criterio NIIF por cuenta propia en operación ambigua: se consulta antes de asentar.
🚫 NUNCA asentar bajo criterio fiscal "para simplificar": el registro es NIIF, lo fiscal se concilia.
✅ SIEMPRE marcar la partida con tipo de diferencia (temporaria/permanente) y monto.

## Métricas
- Partidas divergentes marcadas en el mismo día hábil del registro: ≥ 98 % (medición mensual).
- Diferencias detectadas por Renta al preparar F-2516 que NO estaban marcadas: 0.
- Consultas a NIIF resueltas antes del cierre del periodo: 100 %.

## Tests
### Test 1 — (normal) Anticipo de cliente por $20M recibido en diciembre, servicio se presta en enero
**Output:** asentado como pasivo (ingreso diferido) bajo NIIF; fiscalmente puede ser ingreso del periodo según realización → tag `diferencia_NIIF_fiscal=true`, tipo temporaria; notificación a NIIF y Renta el mismo día; monto < 50 UVT individual evaluado contra acumulado.
### Test 2 — (excepción) Provisión de cuentas incobrables por 80 UVT bajo NIIF 9 (pérdida esperada), que difiere del límite fiscal de provisión individual
**Output:** provisión asentada bajo NIIF 9; tag con tipo temporaria y monto; ≥ 50 UVT → escalamiento a EspecialistaNIIF con prioridad alta + `documentar-decision-no-trivial` con ambos fundamentos (NIIF 9 vs Arts. 145-146 ET); Renta recibe la cuantificación para impuesto diferido.

═══════════════════════════════════════════════════════════════════════

---
name: contabilizar-costos-produccion
description: Activa mensualmente cuando EspecialistaCostos entregue el Estado del Costo de Producción del cliente industrial/manufactura/agro/construcción. Asienta costo de ventas, ajustes de inventario en proceso y terminado. Sin esta skill el costo de ventas no es trazable.
agente: RITORE-AuxiliarContable-Senior
categoria: operativo
---

# Skill: contabilizar-costos-produccion

## Para qué existe
Traduce el Estado del Costo (técnico) a asientos contables trazables: sin esta skill el costo de ventas es una cifra sin soporte y la conciliación contable-fiscal de costos se vuelve indefendible ante la DIAN.

## Cuándo se activa
- Entrega mensual del Estado del Costo por EspecialistaCostosInventarios (clientes industriales, manufactura, agro, construcción).
- Reproceso solicitado por EstadosFinancieros o por corrección del Estado del Costo.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Estado del Costo de Producción firmado | EspecialistaCostosInventarios | SIN Estado del Costo firmado NO se contabiliza; reiterar 1 vez en 24 h hábiles, luego Orquestador |
| Saldos de inventarios MP / PEP / PT del periodo | AuxiliarInventarios (kardex) | Timeout 4 h → caché con marca `[DATO EN CACHÉ — verificar]` y escalar en paralelo |
| Centros de costos y estructura de contratos (construcción AIU) | `cargar-perfil-cliente` | Solicitar al perfil; sin centros de costos definidos no se asienta en cliente que los usa |

## Procedimiento
1. Recibir y validar el Estado del Costo: cuadre interno (MP consumida + MOD + CIF = costo de producción del periodo ± variación de PEP).
2. Reclasificar materia prima consumida (de inventario MP a inventario PEP).
3. Asentar MOD y CIF a inventario PEP.
4. Transferir productos terminados (de PEP a PT) al costo liquidado.
5. Asentar costo de ventas por productos vendidos (de PT a 6135/6235), por centro de costos o contrato si aplica.
6. En construcción: costos por contrato y tratamiento AIU según Art. 462-1 ET (base gravable especial sobre AIU para los servicios que aplique) — ante duda, `consultar-a-especialista` (EspecialistaIVA).
7. Notificar a EstadosFinancieros (cifra de costo de ventas) y EspecialistaRenta (conciliación contable-fiscal de costos).

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Asientos del ciclo de costos | Suma de movimientos = Estado del Costo, diferencia $0 |
| Saldos MP/PEP/PT actualizados | Ningún inventario con saldo negativo |
| Notificación a EEFF y Renta | Emitida el mismo día hábil del registro |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Saldo de inventario MP queda negativo | Consumos sobreestimados o entradas sin registrar | Suspender el asiento; cruzar consumos contra kardex con AuxiliarInventarios | Escalar a EspecialistaCostos con el detalle; NO asentar con saldo negativo |
| Costo unitario varía > 30 % vs mes anterior sin causa documentada | Error en liquidación, cambio de mezcla o de unidad | Alertar a EspecialistaCostos con ambos costos y pedir confirmación | Congelar la contabilización del ítem afectado; asentar el resto del Estado del Costo y dejar el ítem `pendiente` |
| Estado del Costo no cuadra internamente | Error de fórmula o de saldos iniciales | Devolver a EspecialistaCostos con la diferencia cuantificada | Si no responde en 4 h y el cierre vence, pre-cierre con marca `[ESTADO DEL COSTO EN CORRECCIÓN]` y escalar al Orquestador |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia entre asientos y Estado del Costo | ≥ 1 UVT o ≥ 0,5 % del costo del periodo | Investigar y documentar antes de asentar |
| Ajuste o diferencia | ≥ 50 UVT | EspecialistaCostosInventarios |
| Ajuste o diferencia | ≥ 500 UVT | Contador Titular vía Orquestador |

## Reglas críticas
🚫 NUNCA contabilizar costo sin el Estado del Costo firmado por EspecialistaCostos.
🚫 NUNCA capitalizar gastos administrativos como costo de producción.
✅ SIEMPRE asentar por centro de costos / contrato cuando el cliente los usa.

## Métricas
- Estados del Costo contabilizados dentro de las 48 h siguientes a la entrega: ≥ 95 % (medición mensual).
- Diferencia entre costo de ventas contable y Estado del Costo: $0 al cierre de cada mes.
- Saldos negativos de inventario generados por esta skill: 0.

## Tests
### Test 1 — (normal) Cliente manufactura por procesos: Estado del Costo con MP $120M, MOD $45M, CIF $30M; PT vendido 80 %
**Output:** reclasificación MP→PEP $120M, MOD y CIF a PEP, transferencia PEP→PT por el costo liquidado, costo de ventas (6135) por el 80 % vendido; cuadre $0 contra el Estado del Costo; notificación a EEFF y Renta.
### Test 2 — (excepción) Cliente construcción con contrato AIU: al asentar consumos, el inventario MP del contrato 02 queda en −$8M
**Output:** asiento SUSPENDIDO para el contrato 02; cruce con kardex detecta entradas de MP facturadas al contrato 01 por error; corrección de la imputación entre contratos, re-cuadre y asiento por contrato; tratamiento AIU validado (Art. 462-1 ET) con EspecialistaIVA para la facturación asociada; el resto de contratos se asienta sin bloqueo.

═══════════════════════════════════════════════════════════════════════

---
name: contabilizar-depreciacion-mensual
description: Activa mensualmente cuando ActivosFijos entregue el cálculo de depreciación. Asienta gasto de depreciación y crédito a depreciación acumulada por activo o componente, marcando diferencias contable-fiscales. Sin esta skill PPE no refleja desgaste y los EEFF se distorsionan.
agente: RITORE-AuxiliarContable-Senior
categoria: operativo
---

# Skill: contabilizar-depreciacion-mensual

## Para qué existe
Convierte el cálculo técnico de ActivosFijos en asientos por activo/componente y captura en el origen la diferencia entre depreciación NIIF (vida útil técnica) y fiscal (Art. 137 ET), que de otro modo se pierde para el impuesto diferido.

## Cuándo se activa
- Entrega mensual del cálculo de depreciación por AuxiliarActivosFijos.
- Recalculo por adiciones, retiros, deterioro o cambio de vida útil informado por ActivosFijos.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Cálculo de depreciación con desglose por activo/componente, NIIF y fiscal | [[08-AuxiliarActivosFijos-Senior]] | NO se asienta estimando; reiterar 1 vez en 24 h hábiles, luego Orquestador |
| Centros de costos por activo | `cargar-perfil-cliente` | Asentar a centro general SOLO con autorización del perfil; si el cliente usa centros, esperar el dato |
| Estado de cada activo (activo / retirado / deteriorado) | ActivosFijos | Sin estado confirmado, excluir el activo dudoso del asiento del mes y resolver |

## Procedimiento
1. Recibir cálculo de ActivosFijos con desglose por activo/componente (NIIF y fiscal).
2. Asentar gasto de depreciación (5160/5260) por centro de costos.
3. Acreditar depreciación acumulada (1592/1596) por activo.
4. Comparar depreciación NIIF vs fiscal por activo: si difieren, activar `clasificar-partida-NIIF-vs-FISCAL` (marca + notificación a NIIF y Renta).
5. Confirmar a ActivosFijos el registro (cierre del ciclo).

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Asientos de depreciación por activo/componente | Total asentado = total del cálculo de ActivosFijos, diferencia $0 |
| Marcas de diferencia contable-fiscal | 100 % de los activos con vidas útiles divergentes marcados |
| Confirmación a ActivosFijos | Emitida el mismo día hábil |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Depreciación del mes supera el valor en libros restante del activo | Cálculo no actualizado por retiro o deterioro previo | NO asentar ese activo; recalcular con ActivosFijos | Asentar el resto del lote; el activo queda `pendiente` y si no se resuelve en 48 h, escalar a ActivosFijos vía Orquestador |
| Activo marcado como deteriorado sigue en el cálculo normal | Falta de sincronización con la prueba de deterioro | Validar con EspecialistaNIIF el nuevo valor depreciable antes de continuar | Excluir el activo del asiento del mes con marca `[DETERIORO EN VALIDACIÓN]` |
| Activo retirado aparece con depreciación | Maestro de activos desactualizado | Rechazar la línea y pedir corrección del maestro a ActivosFijos | Documentar el rechazo; si se repite 2 meses seguidos, alertar al Orquestador (falla estructural del maestro) |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia entre cálculo y asiento | ≥ 1 UVT | Investigar y documentar antes de asentar |
| Ajuste por deterioro o recalculo | ≥ 50 UVT | EspecialistaNIIF |
| Ajuste | ≥ 500 UVT | Contador Titular vía Orquestador |

## Reglas críticas
🚫 NUNCA depreciar activos retirados.
🚫 NUNCA usar vida útil distinta a la política contable (NIIF) o fiscal (Art. 137 ET) sin justificación documentada.
✅ SIEMPRE marcar la diferencia contable-fiscal por activo (vía `clasificar-partida-NIIF-vs-FISCAL`).

## Métricas
- Depreciación contabilizada dentro de las 48 h siguientes al cálculo: ≥ 95 % (medición mensual).
- Activos con diferencia NIIF/fiscal marcada: 100 %.
- Activos retirados o deteriorados depreciados por error: 0.

## Tests
### Test 1 — (normal) Cálculo mensual de 45 activos en 3 centros de costos; 12 activos con vida útil fiscal distinta a la NIIF
**Output:** asientos 5160/5260 contra 1592/1596 por activo y centro; total = cálculo de ActivosFijos; 12 marcas `diferencia_NIIF_fiscal` emitidas a NIIF y Renta; confirmación a ActivosFijos.
### Test 2 — (excepción) Una máquina con valor en libros de $1,2M aparece con depreciación mensual de $1,5M y además está marcada como deteriorada
**Output:** línea EXCLUIDA del asiento del mes; recalculo solicitado a ActivosFijos y validación del nuevo valor depreciable con EspecialistaNIIF (la depreciación posterior al deterioro se calcula sobre el valor ajustado); resto del lote asentado sin bloqueo; activo `pendiente` con seguimiento a 48 h.

═══════════════════════════════════════════════════════════════════════

---
name: contabilizar-factura-electronica
description: Skill base de contabilización de facturas electrónicas validadas por FacturacionElectronica. Variante R (recibida) clasifica costos/gastos, IVA descontable y retenciones practicadas, genera CxP. Variante E (emitida) registra el ingreso, IVA generado, retenciones que practicó el receptor, genera CxC. Sin esta skill los ingresos y gastos quedan sin registrar o mal clasificados, afectando IVA, retenciones y EEFF.
agente: RITORE-AuxiliarContable-Senior
categoria: operativo
---

# Skill: contabilizar-factura-electronica

## Para qué existe
Es la skill de mayor volumen del AuxContable. Su precisión determina la calidad del IVA (descontable y generado), las retenciones, los costos/gastos deducibles, las CxC/CxP y las bases del cierre fiscal. Recibida y emitida comparten > 70 % del flujo, por eso son variantes de una sola skill (§4 del estándar), con pasos diferenciales documentados abajo.

## Cuándo se activa (por variante)

| Variante | Trigger |
|---|---|
| **R — Recibida** | Mensaje `notificacion` de [[04-AuxiliarFacturacionElectronica-Senior]] con `tipo_documento='factura_recibida_validada'` (CUDE OK, RUT emisor confirmado); batch al cierre del día (cron 7 PM) |
| **E — Emitida** | Mensaje de FacturacionElectronica con `tipo_documento='factura_emitida_validada'` (CUFE OK, transmitida y aceptada por DIAN) |

## Inputs

| Insumo | De quién | Formato | Si falta |
|---|---|---|---|
| Factura validada (CUFE/CUDE OK) | FacturacionElectronica | XML UBL 2.1 + metadata de validación | SIN validación NO se contabiliza; devolver a FacturacionElectronica |
| Perfil del cliente (plan de cuentas, régimen, marco NIIF, calidad de agente retenedor) | `cargar-perfil-cliente` | Ficha Notion | Solicitar a NotionArquitecto; espera máx. 24 h hábiles, luego Orquestador |
| Tarifas de retención aplicables al tercero/concepto | EspecialistaRetenciones | Tabla de tarifas vigente | NUNCA inventar tarifa: consultar y esperar (timeout 4 h → caché `[DATO EN CACHÉ — verificar]` + escalar en paralelo) |
| RUT del tercero actualizado | `consultar-RUT-DIAN-emisor` (FacturacionElectronica) | Estado + calidades | Solicitar antes de aplicar retenciones; la factura queda `en espera de RUT` máx. 24 h hábiles |

## Procedimiento

**Tronco común (ambas variantes):**
1. `cargar-perfil-cliente` (plan de cuentas, régimen, marco NIIF, tarifas del cliente).
2. Validar la factura: CUFE/CUDE validado, RUT de la contraparte activo, IVA discriminado, retenciones explícitas, productos con códigos.
3. Ejecutar los pasos de la variante (tabla siguiente).
4. Generar asiento (validar débitos = créditos antes de registrar) en el ERP del cliente.
5. Notificar según variante y documentar si fue decisión no trivial (`documentar-decision-no-trivial`).

**Pasos específicos por variante:**

| Variante | Pasos propios |
|---|---|
| **R — Recibida** | Clasificar costo/gasto por renglón con centro de costos si aplica; operación atípica (importación, exterior, AIU, exentas) → `consultar-a-especialista` (EspecialistaIVA). Registrar IVA descontable solo si da derecho (Art. 488 ET). Aplicar retenciones (renta + IVA + ICA) que practica el cliente según tarifa de EspecialistaRetenciones. Generar CxP. Notificar: CarteraCxP (CxP), EspecialistaIVA (descontable), EspecialistaRetenciones (practicadas). |
| **E — Emitida** | Clasificar el ingreso por naturaleza (servicios, venta de bienes, arrendamiento, otros). Registrar IVA generado según tarifa (validar tarifa vs producto; duda → EspecialistaIVA). Registrar retención que practicó el receptor SOLO si es agente retenedor (verificar calidad en RUT). Generar CxC vía CarteraCxP. Notificar: EspecialistaIVA (generado para F-300), EspecialistaRetenciones (retenciones a favor para F-350/renta). |

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Asiento registrado en ERP | Débitos = créditos; clasificación por renglón; centro de costos si el cliente los usa |
| CxP (R) o CxC (E) generada | Conciliable contra la factura: tercero, monto, vencimiento |
| Notificaciones emitidas | CarteraCxP + EspecialistaIVA + EspecialistaRetenciones según variante, el mismo día hábil |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Suma de débitos ≠ créditos | Redondeos, renglón omitido, retención mal calculada | NO asentar; recomponer el asiento renglón por renglón contra el XML | Si la diferencia persiste y proviene del XML, devolver a FacturacionElectronica con el detalle |
| IVA discriminado no cuadra con la tarifa aplicable al producto | Tarifa errada del emisor o producto mal codificado | Consultar a EspecialistaIVA ANTES de asentar | Factura `en espera` con marca `[IVA EN CONSULTA]`; si bloquea cierre, escalar al Orquestador |
| Retención en factura emitida de receptor que NO es agente retenedor | Receptor se atribuyó calidad que no tiene | Verificar calidad en RUT; si no es retenedor, registrar la CxC por el total y reportar la inconsistencia | Notificar a FacturacionElectronica para gestionar la corrección con el receptor (NC/ND) |
| RUT del proveedor desactualizado en catálogo | Tercero nuevo o cambio de régimen | Solicitar consulta RUT antes de aplicar retención | Si no llega en 24 h hábiles, asentar el costo/gasto con retención `pendiente` marcada y NO pagar hasta resolver (alerta a Tesorería) |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia en cuadre o en impuestos de la factura | ≥ 1 UVT | Investigar y documentar antes de asentar |
| Operación atípica (exterior, Art. 437-1/437-2 ET, AIU, exenta) | Cualquier monto | EspecialistaIVA decide tratamiento |
| Inconsistencia acumulada con un mismo tercero | ≥ 50 UVT | EspecialistaIVA o EspecialistaRetenciones según el impuesto + nota al Orquestador |
| Efecto en declaraciones ya presentadas | ≥ 500 UVT | Contador Titular vía Orquestador |

## Reglas críticas
🚫 NUNCA contabilizar factura sin validación CUFE/CUDE (recibida) o sin validación RADIAN (emitida).
🚫 NUNCA aplicar IVA descontable a operaciones sin derecho (Art. 488 ET).
🚫 NUNCA inventar tarifas de retención: las define EspecialistaRetenciones.
🚫 NUNCA omitir el centro de costos si el cliente los usa, ni la retención que practicó el receptor (variante E).

## Métricas
- Facturas contabilizadas dentro de las 24 h siguientes a la validación: ≥ 95 % (medición mensual).
- Asientos corregidos posteriormente por mala clasificación: ≤ 2 % del volumen mensual.
- Facturas atípicas resueltas con consulta a especialista (no por criterio propio): 100 %.

## Tests
### Test 1 — (normal, R) Factura recibida de consultoría $5M + IVA 19 %, emisor sociedad responsable, cliente agente retenedor
**Output:** gasto por honorarios $5M con centro de costos, IVA descontable $950.000 (da derecho, Art. 488 ET), retención en la fuente 11 % según tarifa confirmada por EspecialistaRetenciones, CxP por el neto; notificaciones a CarteraCxP, EspecialistaIVA y EspecialistaRetenciones.
### Test 2 — (excepción, E) Factura emitida a un receptor que descontó retención del 11 %, pero la consulta RUT muestra que NO es agente retenedor
**Output:** asiento del ingreso + IVA generado registrado; la retención NO se registra como anticipo; CxC por el valor total; inconsistencia reportada a FacturacionElectronica para coordinar con el receptor (ajuste o NC/ND); EspecialistaRetenciones notificado para excluirla del F-350/anticipos; decisión documentada.

═══════════════════════════════════════════════════════════════════════

---
name: contabilizar-movimiento-bancario
description: Activa cuando el Conciliador identifique un movimiento bancario y su contraparte. Genera el asiento contable correspondiente — ingreso, pago, transferencia, comisión, GMF. Sin esta skill los movimientos identificados quedan sin contabilizar y los saldos se desconectan.
agente: RITORE-AuxiliarContable-Senior
categoria: operativo
---

# Skill: contabilizar-movimiento-bancario

## Para qué existe
Cierra el ciclo de la conciliación: el Conciliador identifica, este agente asienta. Sin esta skill los saldos de bancos en libros se desconectan del extracto y la conciliación del mes siguiente arranca rota.

## Cuándo se activa
- Notificación de [[03-AuxiliarConciliacionesBancarias-Senior]] con movimiento identificado (tipo, monto, contraparte) pendiente de asentar.
- Lote de movimientos no contabilizados al preparar el cierre mensual.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Movimiento identificado: tipo, monto, fecha, contraparte, documento soporte | Conciliador | SIN soporte NO se asienta; devolver al Conciliador como `no contabilizable` |
| Factura/obligación a aplicar (si el movimiento paga o cobra una específica) | AuxiliarCarteraCxP | Asentar a cuenta puente de pagos/recaudos por aplicar con marca `[POR APLICAR]`, máx. 5 días hábiles |
| Maestro de terceros actualizado | NotionArquitecto / ERP | Solicitar alta del tercero antes de asentar; espera máx. 24 h hábiles |

## Procedimiento
1. Recibir notificación del Conciliador con tipo de movimiento, monto y contraparte.
2. Identificar cuenta contable según tipo: ingreso, pago a proveedor, pago de impuesto, nómina, comisión bancaria, GMF, transferencia interna.
3. Si requiere aplicación a factura específica, coordinar con CarteraCxP (aplicación a CxC/CxP).
4. Generar asiento; validar débitos = créditos.
5. Notificar al Conciliador (movimiento contabilizado) para que cierre la partida.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Asiento del movimiento | Cuadrado, con tercero y documento soporte referenciado |
| Aplicación a CxC/CxP (si corresponde) | Saldo del tercero actualizado en aging |
| Confirmación al Conciliador | Emitida el mismo día hábil; la partida conciliatoria se cierra |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Monto del movimiento no coincide con la factura referenciada | Pago parcial, descuento no documentado o GMF descontado | Alertar a CarteraCxP ANTES de asentar para definir la aplicación | Asentar a cuenta puente `[POR APLICAR]` con seguimiento; si ≥ 1 UVT de diferencia sin explicar, investigar y documentar antes de aplicar |
| Contraparte marcada como "tercero no registrado" | Tercero nuevo en el ERP | Solicitar alta al maestro antes de proceder | Si no se crea en 24 h hábiles, asentar a cuenta puente con identificación provisional y escalar al Orquestador |
| GMF asentado sobre operación exenta | Marca de exención no consultada | Verificar exención (Art. 879 ET) con el Conciliador y reversar | Si el banco cobró GMF sobre cuenta exenta, el reclamo lo gestiona el Conciliador; el asiento refleja lo cobrado mientras tanto |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia entre movimiento y documento a aplicar | ≥ 1 UVT | Investigar y documentar antes de aplicar |
| Movimientos sin contabilizar acumulados | ≥ 50 UVT o > 5 días hábiles | Orquestador (riesgo de cierre) |
| Diferencia o partida inexplicada | ≥ 500 UVT | Contador Titular vía Orquestador |

## Reglas críticas
🚫 NUNCA contabilizar sin documento soporte del movimiento.
🚫 NUNCA dejar montos en cuenta puente más de 5 días hábiles sin gestión documentada.
✅ SIEMPRE confirmar al Conciliador para que la partida conciliatoria se cierre.

## Métricas
- Movimientos asentados dentro de las 24 h siguientes a la identificación: ≥ 95 % (medición mensual).
- Saldo de cuentas puente al cierre de mes: $0 o 100 % documentado con plan de aplicación.
- Asientos devueltos por el Conciliador por inconsistencia: ≤ 1 % mensual.

## Tests
### Test 1 — (normal) Pago a proveedor por $12M identificado por el Conciliador contra factura específica
**Output:** débito a CxP del tercero, crédito a bancos; aplicación coordinada con CarteraCxP (factura cerrada en aging); confirmación al Conciliador el mismo día.
### Test 2 — (excepción) Cobro de cliente por $9.700.000 contra una CxC de $10.000.000 (diferencia 3 UVT aprox., sin nota de descuento)
**Output:** asiento NO aplicado de inmediato; alerta a CarteraCxP; se identifica retención practicada por el cliente pagador ($300.000) → aplicación correcta: banco + anticipo de retenciones contra la CxC total; diferencia explicada y documentada; si no se hubiera explicado, quedaría en cuenta puente `[POR APLICAR]` con investigación por ser ≥ 1 UVT.

═══════════════════════════════════════════════════════════════════════

---
name: contabilizar-nomina-mensual
description: Activa cuando Nómina entregue la liquidación mensual con desglose. Contabiliza gastos de personal, aportes a seguridad social/parafiscales y provisiones de prestaciones (cesantías/intereses/prima/vacaciones). Sin esta skill los gastos laborales quedan sin reflejar y distorsionan EEFF y renta.
agente: RITORE-AuxiliarContable-Senior
categoria: operativo
---

# Skill: contabilizar-nomina-mensual

## Para qué existe
La nómina concentra gasto recurrente, pasivos laborales y obligaciones de retención: un error se repite cada mes y se acumula en prestaciones mal provisionadas, deducibilidad en riesgo (pagos sin PILA) y pasivos laborales ocultos.

## Cuándo se activa
- Entrega de la liquidación mensual por el agente de Nómina, con PILA confirmada.
- Liquidaciones extraordinarias: primas (jun/dic), cesantías e intereses (feb), liquidaciones finales de contrato.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Liquidación de nómina con desglose por empleado y concepto | Nómina | NO se contabiliza sin liquidación; reiterar 1 vez en 24 h hábiles, luego Orquestador |
| Confirmación de PILA pagada | Nómina | SIN PILA confirmada NO se contabiliza (condición de deducibilidad y regla crítica); esperar confirmación |
| Parámetros del cliente: % ARL por riesgo, exoneración Ley 1607/2012, centros de costos | `cargar-perfil-cliente` | Solicitar; sin % ARL confirmado no se asientan aportes patronales |

## Procedimiento
1. Recibir liquidación de Nómina con desglose por empleado y por concepto.
2. Asentar gasto de personal por concepto (salarios, comisiones, horas extra, auxilios) y centro de costos.
3. Asentar aportes patronales: salud 8,5 %, pensión 12 %, ARL según clase de riesgo, parafiscales 9 % cuando aplique — verificando exoneración de salud y parafiscales (Ley 1607/2012) para empleados < 10 SMMLV en clientes que califican.
4. Provisionar prestaciones sociales: cesantías 8,33 %, intereses sobre cesantías 1 %, prima 8,33 %, vacaciones 4,17 %.
5. Asentar deducciones: salud 4 %, pensión 4 %, retención en la fuente, embargos, libranzas.
6. Notificar: Tesorería (pago neto), EspecialistaRetenciones (retención de fuente laboral), EspecialistaRenta (gastos deducibles condicionados a PILA).

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Asiento de nómina cuadrado | Débitos = créditos; gasto total = liquidación de Nómina |
| Provisiones prestacionales del mes | Las 4 provisiones asentadas sobre las bases correctas |
| Notificaciones a Tesorería/Retenciones/Renta | Emitidas el mismo día hábil del registro |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Total débitos ≠ créditos | Concepto omitido o deducción mal sumada | NO asentar; cuadrar contra la liquidación concepto por concepto | Devolver a Nómina con la diferencia exacta; nómina queda `en corrección` |
| Auxilio de transporte asentado a empleado con salario > 2 SMMLV | Parámetro desactualizado en Nómina | Corregir el asiento y alertar a Nómina para corregir la liquidación | Si Nómina no corrige en el mismo ciclo, escalar al Orquestador (error recurrente afecta PILA y prestaciones) |
| Aporte de salud patronal asentado para empleado cubierto por exoneración Ley 1607/2012 (o al revés) | Calificación del cliente o del empleado mal parametrizada | Verificar la calificación del cliente y el salario del empleado (≥ 10 SMMLV no exonerado); recalcular | Consultar a EspecialistaRenta; asentar según liquidación con marca `[EXONERACIÓN EN VERIFICACIÓN]` y ajustar en el mismo mes |
| PILA no confirmada al cierre | Pago pendiente o falla del operador | NO contabilizar; alertar a Nómina y Tesorería (la deducibilidad depende del pago de aportes) | Si el cierre vence, escalar al Orquestador; el periodo NO cierra con nómina sin PILA |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia entre liquidación y asiento | ≥ 1 UVT | Investigar y documentar antes de asentar |
| Inconsistencia recurrente de Nómina (2+ meses) | Cualquier monto | Orquestador (revisión del agente de Nómina) |
| Pasivo laboral no provisionado detectado | ≥ 50 UVT | EspecialistaNIIF; ≥ 500 UVT → Contador Titular |

## Reglas críticas
🚫 NUNCA omitir provisiones prestacionales.
🚫 NUNCA contabilizar sin PILA confirmada por Nómina.
✅ SIEMPRE verificar la exoneración Ley 1607/2012 antes de asentar aportes de salud y parafiscales.

## Métricas
- Nóminas contabilizadas dentro de las 48 h siguientes a la liquidación con PILA: ≥ 95 % (medición mensual).
- Diferencia entre provisiones asentadas y bases de liquidación: $0 cada mes.
- Correcciones de asientos de nómina posteriores al cierre: ≤ 1 por semestre por cliente.

## Tests
### Test 1 — (normal) Nómina de 18 empleados, cliente exonerado Ley 1607/2012, PILA confirmada
**Output:** gasto por concepto y centro de costos; aportes patronales sin salud ni parafiscales para empleados < 10 SMMLV (exoneración verificada), con ARL según clase de riesgo; 4 provisiones prestacionales; deducciones (4 % + 4 % + retefuente + libranzas); notificaciones a Tesorería, Retenciones y Renta.
### Test 2 — (excepción) La liquidación incluye auxilio de transporte para un empleado con salario de 3 SMMLV y la PILA del mes aún no está confirmada
**Output:** contabilización RETENIDA por falta de PILA (regla crítica); alerta a Nómina por el auxilio improcedente (> 2 SMMLV) con la corrección cuantificada; al confirmarse PILA y recibir liquidación corregida, asiento completo; el incidente queda documentado para detectar recurrencia.

═══════════════════════════════════════════════════════════════════════

---
name: corregir-asientos-detectados-erroneos
description: Activa cuando el Conciliador, Auditoría interna o un Especialista reporte inconsistencia en asientos contables. Investiga, corrige (reverso + nuevo asiento) y documenta el motivo. Sin esta skill los errores se acumulan y distorsionan periodos.
agente: RITORE-AuxiliarContable-Senior
categoria: operativo
---

# Skill: corregir-asientos-detectados-erroneos

## Para qué existe
Define el único camino válido de corrección (reversar + asentar de nuevo, nunca editar) y protege los periodos cerrados y las declaraciones presentadas de correcciones descoordinadas.

## Cuándo se activa
- Alerta de inconsistencia del Conciliador, un Especialista, el Revisor Fiscal o auditoría interna.
- Error propio detectado por cualquier skill de este perfil después de registrado un asiento.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Detalle de la inconsistencia: asiento, cuenta, monto, motivo | Originador de la alerta | Pedir precisión al originador; no se corrige "a ciegas"; espera máx. 24 h hábiles |
| Asiento original y su documento soporte | ERP | Si el soporte no aparece, la corrección se suspende y se escala (asiento sin soporte es hallazgo en sí mismo) |
| Estado del periodo (abierto / cerrado / declarado) | `cerrar-mes-contable` + EspecialistaRenta | Verificar antes de corregir; nunca asumir que está abierto |

## Procedimiento
1. Recibir la notificación con el detalle del error.
2. Investigar el asiento original (soporte, criterio aplicado, quién lo originó).
3. Verificar el estado del periodo: si está cerrado → registrar en periodo de ajuste; si el periodo fiscal ya fue declarado → coordinar PRIMERO con EspecialistaRenta.
4. Generar asiento de reversión (mismo monto, naturaleza inversa, referencia cruzada al original).
5. Generar el asiento corregido.
6. Documentar vía `documentar-decision-no-trivial`: razón del error, corrección aplicada, originador.
7. Notificar al originador de la alerta; si la corrección es ≥ 50 UVT, copiar al Contador Titular.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Par reversión + asiento corregido | Referencias cruzadas entre original, reverso y corrección; el original queda intacto |
| Documentación del motivo | Causa raíz identificada, no solo el síntoma |
| Notificación de cierre al originador | Emitida con el número de los asientos de corrección |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| La inconsistencia proviene de un criterio NIIF, no de digitación | Criterio mal aplicado en el origen | Consultar a EspecialistaNIIF ANTES de corregir (la corrección podría ser peor que el error) | Asiento marcado `[CRITERIO EN CONSULTA]`; sin respuesta en 4 h, escalar vía Orquestador |
| El periodo del asiento ya está cerrado | Error detectado tarde | Abrir periodo de ajuste y registrar allí la corrección con nota de corte | Si el ERP no permite periodo de ajuste, registrar en el periodo abierto con revelación del efecto retroactivo, validado por EspecialistaNIIF |
| El periodo fiscal ya fue declarado | Error con efecto en declaraciones presentadas | Coordinar con EspecialistaRenta el efecto (corrección de declaración vs ajuste prospectivo) ANTES de tocar nada | Si Renta no responde en 4 h y hay plazo legal corriendo, escalar al Contador Titular vía Orquestador con prioridad alta |
| El mismo tipo de error reaparece (2+ veces en 30 días) | Causa raíz no corregida | Activar `detectar-patron-correccion-recurrente` (compartida) y proponer ajuste del procedimiento de la skill de origen | Reporte al Orquestador con el patrón documentado |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Corrección | ≥ 50 UVT | Notificar al Contador Titular (informativo) |
| Corrección con efecto en declaración presentada | ≥ 1 UVT | EspecialistaRenta SIEMPRE antes de corregir |
| Corrección | ≥ 500 UVT | Contador Titular decide (posible reexpresión / corrección de declaración) |

## Reglas críticas
🚫 NUNCA modificar el asiento original: siempre reversar + asentar de nuevo.
🚫 NUNCA corregir asientos de periodos fiscales ya declarados sin coordinar con EspecialistaRenta.
✅ SIEMPRE documentar la causa raíz, no solo la corrección.

## Métricas
- Correcciones completadas dentro de las 48 h siguientes a la alerta: ≥ 90 % (medición mensual).
- Correcciones con documentación de causa raíz: 100 %.
- Errores recurrentes del mismo tipo tras una corrección: 0 en los 90 días siguientes.

## Tests
### Test 1 — (normal) El Conciliador reporta una comisión bancaria asentada como gasto de papelería (periodo abierto, 0,4 UVT)
**Output:** investigación (error de clasificación en lote), reverso + asiento corregido a gastos bancarios con referencias cruzadas, documentación del motivo, notificación al Conciliador; < 50 UVT → sin copia al Contador Titular.
### Test 2 — (excepción) EspecialistaIVA detecta IVA descontable tomado sin derecho por 120 UVT en un bimestre cuyo F-300 ya se presentó
**Output:** corrección SUSPENDIDA hasta coordinar con EspecialistaRenta/EspecialistaIVA el mecanismo (corrección de la declaración); con la decisión, reverso + asiento corregido en periodo de ajuste; ≥ 50 UVT → Contador Titular notificado; causa raíz (clasificación de operación sin derecho, Art. 488 ET) documentada y alimenta a `contabilizar-factura-electronica`.

═══════════════════════════════════════════════════════════════════════

---
name: documentar-criterio-contable-aplicado
description: Activa cuando apliques un criterio contable no estándar — interpretación NIIF, política específica del cliente, tratamiento por sector. Documenta para consistencia futura y defensa ante auditoría. Sin esta skill los criterios aplicados se pierden en la memoria.
agente: RITORE-AuxiliarContable-Senior
categoria: operativo
---

# Skill: documentar-criterio-contable-aplicado

## Para qué existe
Convierte decisiones puntuales en precedentes consultables: garantiza consistencia entre periodos (misma operación → mismo tratamiento) y deja la defensa lista ante auditoría o requerimiento.

## Cuándo se activa
- Al aplicar un criterio no estándar: interpretación NIIF, política propia del cliente, tratamiento sectorial.
- Cuando una skill de este perfil resuelve una operación atípica tras consultar a un especialista (la respuesta se cristaliza como criterio).
- Al recibir una corrección del dueño o de un Master que cambia un tratamiento.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Criterio aplicado: tema, operación, tratamiento elegido | Skill de origen | Sin caso concreto no se documenta doctrina abstracta |
| Fundamento (norma NIIF / ET / política del cliente) | Skill de origen + `verificar-vigencia-normativa` | Marcar `[VERIFICAR]` y validar el fundamento con EspecialistaNIIF antes de activar el criterio |
| Validación del especialista (si la operación es compleja) | EspecialistaNIIF | El criterio queda en estado `propuesto`, no `activo`, hasta validación |

## Procedimiento
1. Identificar el criterio aplicado (NIIF, política, sector) y el caso que lo originó.
2. Documentar en `aprendizaje.criterios_aplicados`: tema, descripción, fundamento normativo, ejemplo de aplicación, fecha y cliente.
3. Generar embedding para RAG (recuperable en operaciones similares).
4. Notificar a EspecialistaNIIF para validación si es operación compleja o de juicio.
5. Activar como criterio consultable (`activo`) solo tras validación cuando aplique el paso 4.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Criterio documentado en `aprendizaje.criterios_aplicados` | Contiene tema, fundamento, ejemplo y estado (`propuesto`/`activo`/`rechazado`) |
| Embedding RAG generado | El criterio aparece al consultar operaciones similares |
| Validación de NIIF (si compleja) | Registrada con fecha y resultado |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| EspecialistaNIIF objeta el criterio | Interpretación incorrecta o norma más reciente | Marcar `status='rechazado'`, reaplicar el criterio aprobado y corregir los asientos afectados vía `corregir-asientos-detectados-erroneos` | Si hay asientos en periodos declarados, ese flujo coordina con Renta |
| Dos criterios documentados se contradicen | Casos similares resueltos distinto en el tiempo | Detectar la colisión, escalar ambos a EspecialistaNIIF para unificación | Mientras se unifica, usar el más reciente validado y marcar el otro `en revisión` |
| Corrección posterior del dueño/Master sobre un criterio activo | Evolución de la política | Marcar versión anterior como `lecciones_aprendidas` y documentar el nuevo con referencia al cambio | — |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Criterio con efecto acumulado en EEFF | ≥ 50 UVT | EspecialistaNIIF valida obligatoriamente |
| Criterio con efecto | ≥ 500 UVT | Contador Titular (es quien firma los EEFF) |
| Criterio contradice el Sistema-Base | Cualquier caso | NO se aplica; escalar al Orquestador |

## Reglas críticas
🚫 NUNCA aplicar criterios contradictorios al Sistema-Base.
🚫 NUNCA activar como `activo` un criterio complejo sin validación de EspecialistaNIIF.
✅ SIEMPRE versionar: el criterio reemplazado queda como `lecciones_aprendidas`, no se borra.

## Métricas
- Operaciones atípicas resueltas que quedan documentadas como criterio: 100 %.
- Criterios reutilizados vía RAG en operaciones posteriores: ≥ 70 % de los casos similares (medición trimestral).
- Criterios activos sin fundamento normativo registrado: 0.

## Tests
### Test 1 — (normal) Se adopta política de no capitalizar activos menores a 50 UVT para un cliente (gasto directo), validada con su política contable
**Output:** criterio documentado con fundamento (política contable del cliente + marco NIIF de materialidad), ejemplo de aplicación, embedding generado; estado `activo` (no requiere NIIF por estar en política escrita del cliente); aplicado consistentemente en compras siguientes.
### Test 2 — (excepción) Se documenta un tratamiento sectorial agropecuario (activos biológicos medidos a valor razonable) y EspecialistaNIIF lo objeta para este cliente (Pymes, párrafo de costo aplicable)
**Output:** criterio marcado `rechazado` con la objeción registrada; criterio aprobado por NIIF documentado en su lugar y activado; asientos del trimestre afectado corregidos vía `corregir-asientos-detectados-erroneos`; la versión rechazada queda como `lecciones_aprendidas`.

═══════════════════════════════════════════════════════════════════════

---
name: generar-libros-oficiales
description: Activa trimestralmente para generar Libro Diario y Libro Mayor, y anualmente el Libro de Inventarios y Balances. Es obligación legal del comerciante (Arts. 48-58 C.Co.). Sin esta skill el cliente queda expuesto a sanciones.
agente: RITORE-AuxiliarContable-Senior
categoria: operativo
---

# Skill: generar-libros-oficiales

## Para qué existe
Los libros oficiales son la contabilidad legalmente oponible del comerciante (Arts. 48-58 C.Co.): sin ellos, el cliente pierde valor probatorio de su contabilidad y queda expuesto a sanciones e indefensión ante la DIAN.

## Cuándo se activa
- Cron trimestral (Libro Diario y Libro Mayor del trimestre cerrado).
- Cron anual tras el cierre fiscal (Libro de Inventarios y Balances).
- Solicitud del Contador Titular o del Revisor Fiscal.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Periodos del trimestre cerrados | `cerrar-mes-contable` | NO se generan libros sobre periodos abiertos; esperar cierre o escalar el retraso al Orquestador |
| Asientos del periodo desde el ERP | ERP del cliente | Timeout 4 h → reintentar; sin acceso, escalar a NotionArquitecto (incidencia técnica) |
| Saldos iniciales validados (continuidad con libros anteriores) | Libros del trimestre anterior archivados | Reconstruir desde el último libro oficial archivado; si hay brecha, escalar al Contador Titular |

## Procedimiento
1. Verificar que los tres meses del trimestre estén cerrados.
2. Generar Libro Diario con todos los asientos del trimestre, numeración continua.
3. Generar Libro Mayor con movimientos y saldos por cuenta; validar que Mayor = suma del Diario y que los saldos iniciales = saldos finales del libro anterior.
4. Anualmente: generar Libro de Inventarios y Balances con el detalle de cierre.
5. Archivar vía NotionArquitecto con convención canónica de nombres y versión oficial inmutable.
6. Notificar al Contador Titular para revisión.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Libro Diario del trimestre | Numeración continua, sin huecos ni asientos posteriores a la fecha de generación |
| Libro Mayor del trimestre | Cuadra con el Diario; continuidad de saldos con el trimestre anterior |
| Libro de Inventarios y Balances (anual) | Cuadra con los EEFF de cierre |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Inconsistencia entre Diario y Mayor | Asiento modificado después del cierre o falla de extracción | NO generar; identificar el asiento divergente y su origen | Activar `corregir-asientos-detectados-erroneos`; los libros se generan solo tras resolver |
| Cliente cambió de sistema contable a mitad de periodo | Migración | Validar continuidad de saldos entre sistemas (saldo final sistema viejo = saldo inicial nuevo, cuenta por cuenta) | Diferencias de migración ≥ 1 UVT se investigan; ≥ 50 UVT escalan al Contador Titular antes de generar libros |
| Brecha en numeración o trimestre sin libros previos | Periodos sin generar en el pasado | Generar retroactivamente en orden cronológico | Escalar al Contador Titular: la generación tardía se documenta (riesgo sancionatorio es decisión del humano) |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia Diario vs Mayor o de continuidad de saldos | ≥ 1 UVT | Investigar antes de generar |
| Diferencia de migración o brecha histórica | ≥ 50 UVT | Contador Titular |
| Libros con retraso | > 1 trimestre | Contador Titular (exposición sancionatoria) |

## Reglas críticas
🚫 NUNCA generar libros con inconsistencias internas o sobre periodos abiertos.
🚫 NUNCA regenerar un libro oficial ya archivado: las correcciones van en libros posteriores.
✅ SIEMPRE archivar la versión oficial con convención canónica e inmutable.

## Métricas
- Libros trimestrales generados dentro de los 15 días siguientes al cierre del trimestre: 100 %.
- Libros con inconsistencias detectadas por el Contador Titular o RF tras la entrega: 0.
- Clientes con libros al día: 100 % (medición trimestral).

## Tests
### Test 1 — (normal) Trimestre con los tres meses cerrados; continuidad de saldos verificada
**Output:** Libro Diario y Libro Mayor generados, cuadre Diario=Mayor verificado, archivo con convención canónica vía NotionArquitecto, notificación al Contador Titular.
### Test 2 — (excepción) Cliente migró de ERP en el segundo mes del trimestre y el saldo inicial del nuevo sistema difiere en 60 UVT en la cuenta de inventarios
**Output:** generación BLOQUEADA; validación cuenta por cuenta detecta inventarios migrados sin un lote en tránsito; diferencia ≥ 50 UVT → Contador Titular antes de generar; con la corrección de la migración asentada, libros generados con nota de continuidad entre sistemas y archivados.

═══════════════════════════════════════════════════════════════════════

---
name: validar-plan-cuentas-cliente
description: Activa al onboarding del cliente y semestralmente para validar que el plan de cuentas está alineado con su sector, la normativa vigente y los requerimientos de exógena. Sin esta skill el cliente opera con plan obsoleto y se generan inconsistencias.
agente: RITORE-AuxiliarContable-Senior
categoria: operativo
---

# Skill: validar-plan-cuentas-cliente

## Para qué existe
El plan de cuentas es la infraestructura de todo lo demás: si faltan cuentas (retenciones, ICA, AIU) o sobran duplicadas, cada skill de registro hereda el problema y la exógena se arma con reclasificaciones manuales.

## Cuándo se activa
- Onboarding de cliente nuevo (antes del primer registro).
- Cron semestral de revisión.
- Alerta de cualquier skill de este perfil que no encuentre cuenta apropiada para una operación.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Plan de cuentas actual del cliente | ERP / Onboarding | Solicitar a Onboarding; sin plan no hay validación (espera 24 h hábiles, luego Orquestador) |
| Perfil del cliente: sector, obligaciones (IVA, retenciones, ICA, exógena), marco NIIF | `cargar-perfil-cliente` | Solicitar; la validación sin perfil queda `parcial` y se reporta |
| Formatos de exógena que reporta el cliente | EspecialistaExogena / perfil | Validar al menos contra PUC y obligaciones básicas; marcar exógena `pendiente` |

## Procedimiento
1. Comparar el plan actual contra el PUC (Decreto 2650/1993) y las particularidades del marco NIIF aplicable.
2. Verificar que existan cuentas para todas las obligaciones del cliente: IVA (generado/descontable por tarifa), retenciones (renta/IVA/ICA, practicadas y a favor), ICA por municipio, GMF.
3. Verificar granularidad suficiente para los formatos de exógena que reporta el cliente.
4. Si falta una cuenta necesaria, proponer la adición al ERP (nunca crearla sin autorización).
5. Si hay cuentas obsoletas o sin movimiento > 2 años, proponer archivarlas; si hay duplicadas en intención, proponer consolidación.
6. Notificar las propuestas al cliente vía AtencionCliente y registrar su decisión.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Informe de validación del plan | Cobertura de obligaciones 100 % verificada; hallazgos con propuesta concreta |
| Propuestas de adición/archivo/consolidación | Enviadas vía AtencionCliente con respuesta registrada |
| Plan marcado como `validado` con fecha | Vigencia semestral |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Falta cuenta para una obligación activa (p. ej. ICA de un municipio nuevo) | Cliente expandió operaciones sin avisar | Proponer adición con prioridad alta; mientras tanto, registrar en cuenta transitoria documentada | Si el cliente no autoriza en 5 días hábiles, escalar al Orquestador: hay riesgo de declaración mal soportada |
| Cuentas duplicadas en intención (dos cuentas para el mismo concepto) | Creación histórica sin gobierno | Proponer consolidación con plan de reclasificación | Si el cliente rechaza sin justificación, documentar el rechazo y revalidar en la próxima revisión semestral |
| Cliente usa plan sectorial distinto al PUC comercial (financiero, solidario) | Sector con plan propio | Validar contra el plan sectorial correcto, no forzar PUC comercial | Ante duda del plan aplicable, `[VERIFICAR]` con EspecialistaNIIF antes de emitir el informe |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Operaciones registradas en cuenta transitoria por falta de cuenta | ≥ 50 UVT acumulado | Orquestador (presionar autorización del cliente) |
| Plan sin validar | > 8 meses desde la última validación | Orquestador |
| Cambio masivo de plan (migración / re-sectorización) | Cualquier caso | Contador Titular aprueba el mapeo |

## Reglas críticas
🚫 NUNCA modificar el plan de cuentas sin autorización del cliente.
🚫 NUNCA dejar operaciones en cuenta transitoria sin propuesta de cuenta definitiva.
✅ SIEMPRE notificar las propuestas vía AtencionCliente y registrar la decisión del cliente.

## Métricas
- Clientes con plan validado en los últimos 6 meses: 100 %.
- Hallazgos de "cuenta faltante" detectados en operación (no en revisión): ≤ 2 por cliente por semestre.
- Propuestas con respuesta del cliente registrada: 100 %.

## Tests
### Test 1 — (normal) Onboarding de cliente de construcción
**Output:** plan validado contra PUC + marco NIIF; propuestas de cuentas para AIU, costos por contrato y retención de ICA en los municipios donde opera; envío vía AtencionCliente, autorización registrada, plan marcado `validado`.
### Test 2 — (excepción) Revisión semestral encuentra dos cuentas de "honorarios" usadas indistintamente y el cliente rechaza la consolidación sin justificación
**Output:** propuesta de consolidación con plan de reclasificación documentada; rechazo registrado con fecha y sin justificación; regla operativa interna definida (cuál cuenta usar en adelante) para no agravar la duplicidad; punto re-presentado en la siguiente revisión semestral; sin impacto en exógena verificado (ambas mapean al mismo concepto).

═══════════════════════════════════════════════════════════════════════

## Relacionado
- *MOC - Agentes RITORE*
- *Proyecto - Ecosistema RITORE*
- [[00 - Estandar de Agentes RITORE]]
- [[Skills Compartidas RITORE]]
- [[03-AuxiliarConciliacionesBancarias-Senior]]
- [[04-AuxiliarFacturacionElectronica-Senior]]
- [[05-AuxiliarCarteraCxP-Senior]]
- [[06-AuxiliarTesoreria-Senior]]
- [[08-AuxiliarActivosFijos-Senior]]
- [[10-EspecialistaCostosInventarios-Master]]
- *11-EspecialistaIVA-Master*
- *12-EspecialistaRetenciones-Senior*
- *13-EspecialistaRenta-Senior*
- *15-EspecialistaNIIF-Senior*
- *16-EstadosFinancieros-Senior*
- *22-AtencionCliente-Senior*
- *25-Onboarding-Senior*
- *26-NotionArquitecto-DevOps-Senior*

## Historial de versiones
| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-05-19 | Versión inicial consolidada (12 skills) | RITORE |
| 2.0 | 2026-06-11 | Refactorización según Estandar de Agentes v1.0: 12 → 11 skills (facturas recibida + emitida consolidadas en `contabilizar-factura-electronica` con variantes); umbrales numéricos §3 en lugar de "material"; Inputs/Outputs, tablas de manejo de errores y escalamiento, métricas y tests propios en todas las skills | RITORE |
