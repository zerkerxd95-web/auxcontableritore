---
tipo: agente
tags: [ritore, agente, operativa]
capa: operativa
nivel: senior
estado: activo
version: 2.0
fecha: 2026-06-11
---

# SKILLS — 09-AuxiliarInventarios-Senior

**Documento consolidado** · 6 skills · Ecosistema RITORE · v2.0
**Modelo:** claude-opus-4-7

> Reescritura completa según [[00 - Estandar de Agentes RITORE]] (§2 secciones obligatorias, §3 umbrales, §4 anti-clonación). Entradas, salidas y valorización del kardex se consolidaron en una skill base con tabla de variantes (compartían > 95 % del procedimiento); el conteo físico y el tratamiento de faltantes/sobrantes se unificaron porque son fases del mismo flujo. Las reglas universales se heredan de [[Skills Compartidas RITORE]].
>
> **Casos de referencia del dominio:** **Cliente - AGROPECUARIA D** — inventario contable **$1.923M por encima del físico** (Arts. 59, 64, 65 ET; advertencia Arts. 648 ET / 434A CP): costo de ventas subestimado → utilidad inflada → más renta → patrimonio y exógena distorsionados. **Cliente - COMERCIO DE BICICLETAS A** — auxiliares/inventario no confiables que obligaron a reconstruir saldos (SF = SI + Débitos − Créditos) y re-exportar a la misma fecha de corte. Ambos casos justifican las reglas de conteo y conciliación de este perfil.

---

## Índice de skills en este documento

- `gestionar-movimiento-kardex` *(base paramétrica: entradas · salidas · valorización PEPS / promedio ponderado / identificación específica)*
- `realizar-inventario-fisico-y-tratar-diferencias` *(consolida conteo periódico + faltantes/sobrantes)*
- `documentar-merma-deterioro`
- `evaluar-VNR-NIC-2`
- `gestionar-inventario-en-consignacion`
- `escalar-criterio-costos-master`

═══════════════════════════════════════════════════════════════════════

---
name: gestionar-movimiento-kardex
description: Skill base de movimientos de inventario. Registra toda entrada (compra, importación, devolución de cliente, producción terminada, transferencia, ajuste +) y toda salida (venta, consumo interno, devolución a proveedor, ajuste −) valorizando según el método del cliente — PEPS, promedio ponderado o identificación específica (NIC 2 / Sección 13). Activa con cada documento de movimiento.
agente: RITORE-AuxiliarInventarios-Senior
categoria: operativo
---

# Skill: gestionar-movimiento-kardex

## Para qué existe
El kardex es la fuente del costo de ventas y del saldo de inventarios en EEFF, renta y exógena (F-1012). Un movimiento mal registrado o mal valorizado descuadra el kardex y propaga el error a todo el ciclo — el caso **Cliente - AGROPECUARIA D** muestra el costo de perder esta disciplina.

## Cuándo se activa (por variante)

| Variante | Trigger |
|---|---|
| **E — Entrada** | Factura de compra (nacional o importación), remisión de devolución de cliente, orden de producción terminada, traslado entre bodegas, ajuste positivo aprobado |
| **S — Salida** | Factura de venta, vale de consumo interno, nota de devolución a proveedor, baja aprobada, ajuste negativo aprobado |
| **V — Valorización** | Implícita en cada E/S; explícita al recalcular el kardex de un periodo o migrar de sistema |

## Inputs

| Insumo | De quién | Formato | Si falta |
|---|---|---|---|
| Perfil del cliente (método de valorización, sistema permanente/periódico Art. 62 ET, marco NIIF) | `cargar-perfil-cliente` | Ficha Notion | Solicitar a NotionArquitecto; espera máx. 24 h hábiles, luego escalar a Orquestador |
| Documento soporte del movimiento (factura XML, remisión, orden de producción, acta de ajuste) | AuxContable / FacturacionElectronica / cliente | XML FE o PDF | SIN soporte NO se registra; reiterar 1 vez en 24 h hábiles, luego Orquestador |
| Costos adicionales de compra: transporte, seguros, aranceles y nacionalización (importaciones) | CarteraCxP / agencia de aduanas | Documentos de importación | Registrar la entrada al valor factura con marca `[COSTO INCOMPLETO]` y completar al llegar; no liberar la venta del lote a costo incompleto |
| Kardex vigente del ítem | Módulo de inventarios del ERP | Tabla | Si el módulo no responde en 4 h, usar último kardex verificado con marca `[DATO EN CACHÉ — verificar]` y escalar en paralelo |

## Procedimiento

**Tronco común (toda variante):**
1. `cargar-perfil-cliente`: método de valorización, sistema de inventarios, política contable.
2. Validar documento soporte: existencia, coherencia aritmética, tercero y fecha dentro del periodo abierto.
3. Ejecutar los pasos de la variante (tabla siguiente).
4. Actualizar kardex (cantidades + valores) con trazabilidad por lote/fecha/documento.
5. Notificar: AuxContable (asiento), EspecialistaCostos (alimenta Estado del Costo), EspecialistaIVA (si la operación tiene IVA — recordar tarifas reales por factura: 19 %, 5 %, exentos, excluidos y mixtas, caso **Cliente - COMERCIO DE BICICLETAS A** sector bicicletas).

**Pasos específicos por variante:**

| Variante | Pasos propios |
|---|---|
| **E — Compra nacional** | Costo = valor factura sin IVA descontable + fletes y seguros hasta bodega. Genera CxP (notificar CarteraCxP). |
| **E — Importación** | Costo = FOB + flete + seguro + aranceles + gastos de nacionalización; convertir a COP con TRM de la fecha de la operación; IVA de importación a descontable, no al costo. |
| **E — Devolución de cliente** | Reingreso AL COSTO ORIGINAL de la salida (no al precio de venta); reversa proporcional del costo de ventas. |
| **E — Producción terminada** | Costo recibido de la orden de producción liquidada por EspecialistaCostos; no estimar costos propios. |
| **S — Venta** | Descargar al costo según método; asiento doble: ingreso (factura) + costo de ventas (kardex). |
| **S — Consumo interno / muestras** | Descargar al costo contra gasto del área consumidora; evaluar con EspecialistaIVA si procede reintegro de IVA descontable. |
| **S — Devolución a proveedor** | Salida al costo de la entrada original; nota crédito esperada → notificar CarteraCxP. |
| **V — PEPS** | Consumir capas más antiguas primero; mantener tabla de capas por ítem. |
| **V — Promedio ponderado** | Recalcular costo unitario tras CADA entrada: (saldo $ + entrada $) / (saldo q + entrada q). |
| **V — Identificación específica** | Solo para ítems no intercambiables (seriales, proyectos); exigir serial/lote en cada movimiento. |

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Kardex actualizado | Saldo en cantidades ≥ 0 en todo ítem; saldo en $ = Σ capas (PEPS) o q × costo promedio vigente |
| Asiento propuesto a AuxContable | Cuadrado; costo de la salida = valor descargado del kardex, diferencia $0 |
| Trazabilidad | Cada movimiento referencia documento soporte, lote y fecha |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Saldo de inventario negativo tras una salida | Venta facturada antes de registrar la compra; entrada perdida | Suspender el registro y buscar la entrada faltante (facturas pendientes, remisiones) | Registrar la salida con costo de la última capa conocida marcada `[COSTO PROVISIONAL]` solo si el cierre lo exige, y resolver antes de emitir EEFF |
| Costo unitario varía > 30 % vs el periodo anterior sin causa documentada | Error de digitación, cambio de presentación/unidad, factura en otra moneda | Verificar unidad de medida y conversión; pedir confirmación al emisor del documento | Alertar a EspecialistaCostos con ambos costos y congelar el ítem para nuevas salidas hasta resolver |
| Documento soporte duplicado (misma factura dos veces) | Reproceso del XML o doble digitación | Anular el movimiento duplicado citando el original | Si ya afectó cierres, cuantificar y escalar según umbrales |
| Movimiento con fecha de un periodo ya cerrado | Documento llegó tarde | Registrar en el periodo abierto con nota de corte; evaluar materialidad del desfase | Si ≥ 50 UVT, escalar a EspecialistaCostos para decidir reapertura o ajuste |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia de costo o cuadre | ≥ 1 UVT individual o ≥ 0,5 % del rubro acumulado | Investigar y documentar antes de avanzar |
| Diferencia o ajuste | ≥ 50 UVT | EspecialistaCostosInventarios (Master del dominio) vía `escalar-criterio-costos-master` |
| Diferencia o ajuste | ≥ 500 UVT | Contador Titular vía Orquestador |
| Cliente solicita cambiar método de valorización | Cualquier caso | EspecialistaCostosInventarios + EspecialistaNIIF (cambio de política NIC 8, solo desde inicio de periodo) |

## Reglas críticas
🚫 NUNCA registrar movimiento sin documento soporte.
🚫 NUNCA cambiar el método de valorización a mitad de periodo (NIC 8).
🚫 NUNCA omitir transporte, seguros y nacionalización en el costo de la entrada.
✅ SIEMPRE reingresar devoluciones de clientes al costo original de la salida, no al precio de venta.

## Métricas
- Movimientos registrados dentro de las 48 h siguientes al documento: ≥ 95 % (medición mensual).
- Ítems con saldo negativo al cierre de mes: 0.
- Diferencia entre costo de ventas contable y descargue del kardex: $0 al cierre de cada mes.

## Tests
### Test 1 — (normal, E+V promedio) Compra de 100 unidades a $50.000 + flete $500.000; saldo previo 50 unidades a $48.000
**Output:** costo de entrada $55.000/unidad (incluye flete); nuevo promedio ponderado = (50×48.000 + 100×55.000) / 150 = $52.667; kardex actualizado, IVA descontable a EspecialistaIVA, CxP a CarteraCxP, asiento a AuxContable.
### Test 2 — (excepción, S) Factura de venta de 80 unidades con saldo en kardex de 60
**Output:** registro SUSPENDIDO por saldo insuficiente; búsqueda de entradas pendientes detecta remisión de compra sin factura; entrada registrada con soporte de remisión marcada `[FACTURA PENDIENTE]`, luego la salida; si la entrada no apareciera, el faltante de 20 unidades se trataría vía `realizar-inventario-fisico-y-tratar-diferencias`, nunca forzando el kardex a negativo.

═══════════════════════════════════════════════════════════════════════

---
name: realizar-inventario-fisico-y-tratar-diferencias
description: Activa trimestral o anualmente (y siempre antes del cierre fiscal) para la toma física de inventarios — conteo, corte de documentos, conciliación físico vs kardex — y el tratamiento de faltantes y sobrantes, incluido su efecto fiscal (Art. 64 ET). Consolida las antiguas skills de conteo y de detección de diferencias, que eran fases del mismo flujo.
agente: RITORE-AuxiliarInventarios-Senior
categoria: operativo
---

# Skill: realizar-inventario-fisico-y-tratar-diferencias

## Para qué existe
El kardex sin confrontación física degenera en cifras de papel. **Cliente - AGROPECUARIA D** llegó con inventario contable **$1.923M por encima del físico**: utilidad inflada, renta sobrepagada en riesgo de sanción (Arts. 648 ET / 434A CP) y exógena distorsionada. Esta skill existe para que eso no se repita: la corrección va a la contabilidad con acta, nunca a "cuadrar el papel de trabajo".

## Cuándo se activa
- Cron trimestral (conteos cíclicos por familias ABC) y conteo general anual antes del cierre.
- Solicitud del Revisor Fiscal, EspecialistaCostos o el cliente.
- Alerta de `gestionar-movimiento-kardex` (saldos negativos recurrentes o costos congelados sin resolver).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Kardex valorizado a la fecha de corte | Módulo de inventarios | Sin kardex confiable, el conteo se hace igual y se reconstruye el saldo teórico (SF = SI + entradas − salidas del auxiliar, método caso **Cliente - COMERCIO DE BICICLETAS A**); escalar la no-confiabilidad a EspecialistaCostos |
| Corte de documentos: últimas facturas de compra/venta, remisiones y traslados antes del conteo | AuxContable / FacturacionElectronica | El conteo NO arranca sin corte documentado; reiterar 1 vez en 24 h hábiles |
| Planillas de conteo diligenciadas (a ciegas: sin cantidades teóricas) | Equipo de conteo del cliente | Reiterar 1 vez; sin planillas, inventario `incompleto` y reporte al Orquestador |

## Procedimiento
1. Fijar fecha de corte y congelar movimientos durante el conteo (o documentar los inevitables para ajustar el teórico).
2. Realizar corte de documentos: identificar mercancía facturada no despachada, recibida no facturada y en tránsito — ajustar el saldo teórico comparable.
3. Generar planillas a ciegas (código, descripción, ubicación — sin cantidades) y coordinar doble conteo para ítems clase A o con valor ≥ 50 UVT.
4. Cruzar físico vs teórico por ítem: confirmados, faltantes, sobrantes.
5. Segundo conteo obligatorio de toda diferencia ≥ 1 UVT o ≥ 0,5 % de la cantidad teórica del ítem antes de declararla.
6. **Faltantes confirmados:** acta firmada por responsable de bodega; clasificar causa (merma normal → `documentar-merma-deterioro`; hurto/pérdida → investigación + posible responsabilidad; error de registro → corregir el movimiento origen). Efecto fiscal: solo es deducible la disminución por faltantes de mercancías de fácil destrucción o pérdida hasta el **3 % de (inventario inicial + compras)** — Art. 64 ET; el exceso no es deducible → marcar para EspecialistaRenta.
7. **Sobrantes confirmados:** investigar origen (entrada no registrada, devolución sin documento, error de unidad); registrar el ingreso al costo documentado o de mercado, nunca dejarlo "flotando".
8. Asiento de ajuste vía AuxContable + actualización del kardex; informe final con % de exactitud, valor de diferencias y efecto fiscal.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Informe de toma física | Exactitud medida en ítems y en valor; toda diferencia con causa clasificada y acta |
| Ajustes al kardex y asiento | El kardex queda igual al físico contado; ajuste soportado en actas |
| Marca fiscal Art. 64 ET | Faltantes deducibles vs no deducibles cuantificados y entregados a EspecialistaRenta |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Diferencias masivas generalizadas (no concentradas en ítems) | Corte de documentos mal hecho (facturado-no-despachado contado como faltante) | Rehacer el cruce ajustando por documentos en tránsito | Repetir conteo de una muestra del 10 %; si persiste, escalar a EspecialistaCostos como kardex no confiable |
| Bodega pide "ajustar el sistema al físico" sin actas | Cultura de cuadre sin investigación | Negarse; exigir acta por diferencia con causa | Documentar la negativa y escalar al Orquestador; el kardex NO se toca sin soporte |
| Unidades de medida inconsistentes (kardex en cajas, conteo en unidades) | Maestro de ítems sin factor de conversión | Convertir con factor verificado del maestro | Recontar el ítem en la unidad del kardex |
| Inventario contable muy superior al físico (patrón AGROPECUARIA) | Costo de ventas no descargado / juego de inventarios sin hacer | Cuantificar el total, validar con segundo conteo, preparar acta de ajuste | Escalamiento inmediato (ver umbrales): el ajuste y su efecto en renta exigen Contador Titular |

## Escalamiento
- Diferencia neta del conteo ≥ 0,5 % del valor total del inventario o ítem individual ≥ 50 UVT → EspecialistaCostosInventarios.
- Diferencia neta ≥ 500 UVT, o cualquier patrón tipo **Cliente - AGROPECUARIA D** (contable muy por encima del físico con efecto en renta de años anteriores) → Contador Titular, mismo día; posible advertencia Arts. 648 ET / 434A CP la decide el humano.
- Indicio de hurto interno → Contador Titular decide la comunicación al cliente; nunca señalar personas directamente.

## Reglas críticas
🚫 NUNCA "cuadrar el papel de trabajo": la corrección va a la contabilidad con acta (regla de oro C.8 — [[Aux 18 - Juego de Inventarios]]).
🚫 NUNCA entregar planillas con cantidades teóricas visibles (conteo a ciegas).
✅ SIEMPRE hacer corte de documentos antes de cruzar físico vs kardex.
✅ SIEMPRE cuantificar el efecto Art. 64 ET (tope 3 %) de los faltantes para EspecialistaRenta.

## Métricas
- Exactitud del inventario (valor físico / valor teórico): ≥ 98 % en el conteo anual.
- Diferencias con acta y causa clasificada: 100 %.
- Conteo general anual ejecutado antes del cierre fiscal: 100 % de los clientes con inventarios.

## Tests
### Test 1 — (normal) Conteo anual: teórico $850M; físico $848M; faltante concentrado en perecederos ($2M, con inventario inicial + compras de $600M)
**Output:** exactitud 99,8 %; segundo conteo confirma; faltante $2M < 3 % × $600M = $18M → deducible completo (Art. 64 ET, mercancía de fácil destrucción); diferencia neta 0,24 % < 0,5 % y menor a 50 UVT → se investiga y documenta sin escalar a Master; acta firmada, ajuste al kardex, asiento, marca fiscal a EspecialistaRenta.
### Test 2 — (excepción) Conteo arroja inventario contable $1.900M vs físico $1.100M; el cliente pide "dejarlo así y ajustar el papel de trabajo"
**Output:** solicitud RECHAZADA (regla C.8); segundo conteo muestral confirma la magnitud; diferencia ≥ 500 UVT → escalamiento inmediato al Contador Titular con cuantificación del efecto en costo de ventas, renta y exógena de periodos anteriores; acta de hallazgo preparada; referencia explícita al precedente **Cliente - AGROPECUARIA D** ($1.923M) y a los Arts. 648 ET / 434A CP.

═══════════════════════════════════════════════════════════════════════

---
name: documentar-merma-deterioro
description: Activa cuando hay merma natural (evaporación, descomposición, rotura), obsolescencia o daño de inventarios. Registra la baja, exige acta de destrucción o disposición y arma el soporte de deducibilidad fiscal (Art. 64 ET) y el eventual reintegro de IVA descontable (Art. 486 ET).
agente: RITORE-AuxiliarInventarios-Senior
categoria: operativo
---

# Skill: documentar-merma-deterioro

## Para qué existe
La merma mal documentada se pierde dos veces: como inventario y como deducción fiscal. Sin acta de destrucción, la DIAN rechaza la deducción y el faltante queda como diferencia patrimonial inexplicada.

## Cuándo se activa
- Reporte de merma, vencimiento, daño u obsolescencia desde bodega o desde el conteo físico.
- Cron mensual en clientes con perecederos (sector agro/alimentos).
- Ítems sin rotación > 360 días detectados en el kardex (candidatos a obsolescencia).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Reporte de la merma/daño con cantidades, lotes y causa | Bodega del cliente | Solicitar; sin reporte formal no hay registro (espera 24 h hábiles, reiterar 1 vez, luego Orquestador) |
| Acta de destrucción/disposición firmada (con evidencia fotográfica si valor ≥ 50 UVT) | Cliente; testigo de la firma si es material | La baja contable puede registrarse con el reporte, pero la marca `deducible` NO se asigna sin acta |
| Costo en kardex de los ítems afectados | `gestionar-movimiento-kardex` | Caché con marca `[DATO EN CACHÉ — verificar]` |

## Procedimiento
1. Clasificar el evento: merma normal del proceso (se absorbe en el costo), merma anormal/casuística (gasto), obsolescencia o daño (baja + posible deterioro previo vía `evaluar-VNR-NIC-2`).
2. Verificar el reporte contra kardex (lote, fecha de vencimiento, ubicación).
3. Exigir acta de destrucción o disposición: fecha, ítems, cantidades, costo, método de destrucción/donación, firmas; fotos si ≥ 50 UVT.
4. Registrar la salida del kardex al costo y el asiento (gasto por merma/baja de inventario) vía AuxContable.
5. Armar el expediente fiscal: la disminución es deducible dentro del marco del Art. 64 ET (faltantes de fácil destrucción o pérdida hasta 3 % de inventario inicial + compras; obsolescencia/destrucción con acta soportada). Cuantificar deducible vs no deducible y entregar a EspecialistaRenta.
6. Evaluar reintegro de IVA: pérdidas o mermas que excedan lo normal pueden exigir ajuste del IVA descontable (Art. 486 ET) — consultar a EspecialistaIVA si la merma del periodo supera el 3 % de las compras.
7. Si la obsolescencia es recurrente en una familia de ítems, reportar el patrón a EspecialistaCostos (señal de compras sobredimensionadas).

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Expediente de merma (reporte + acta + fotos si aplica) | Completo y archivado; sin acta no hay marca `deducible` |
| Asiento de baja + kardex actualizado | Costo descargado = costo en kardex del lote afectado |
| Cuantificación fiscal | Deducible vs no deducible separado, con referencia al tope 3 % Art. 64 ET |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Merma reportada sin acta de destrucción | Bodega desechó sin protocolo | Registrar la baja contable y marcar `NO deducible` hasta obtener acta | Mantener la marca no deducible; informar al cliente el costo fiscal de no documentar |
| Merma mensual recurrente justo bajo el umbral de reporte | Posible hurto hormiga disfrazado de merma | Analizar tendencia 6 meses y comparar contra mermas normales del sector | Escalar a EspecialistaCostos y sugerir conteo cíclico sorpresa |
| Acta de destrucción por valor que no coincide con el kardex | Costo del acta a precio de venta o estimado | Recalcular al costo del kardex y corregir el acta | Registrar al costo de kardex y dejar nota de la discrepancia en el expediente |

## Escalamiento
- Merma/obsolescencia del periodo ≥ 50 UVT → EspecialistaCostosInventarios.
- Acumulado anual ≥ 500 UVT o merma que exceda el tope deducible del 3 % → Contador Titular (decide tratamiento del exceso no deducible).
- Patrón de merma incompatible con el sector (posible encubrimiento de hurto o ventas omitidas) → Contador Titular + nota a SAGRLAFT.

## Reglas críticas
🚫 NUNCA marcar como deducible una baja sin acta de destrucción/disposición.
🚫 NUNCA absorber merma anormal en el costo del producto (va a gasto, separada).
✅ SIEMPRE evaluar el reintegro de IVA descontable cuando la merma exceda lo normal (Art. 486 ET).

## Métricas
- Bajas por merma con expediente completo (reporte + acta): 100 %.
- Mermas registradas dentro del mes del evento: ≥ 95 % (medición mensual).

## Tests
### Test 1 — (normal) Cliente de alimentos reporta vencimiento de 200 unidades (costo kardex $3.2M) con acta de destrucción firmada y fotos
**Output:** baja del kardex al costo, asiento de gasto por merma, expediente completo; deducible (dentro del 3 % anual acumulado); IVA sin reintegro por estar dentro de lo normal del sector; acumulado anual actualizado para vigilar el tope.
### Test 2 — (excepción) Bodega informa que "botó" mercancía obsoleta por $40M hace dos meses, sin acta ni fotos
**Output:** baja contable registrada para no mantener inventario inexistente, pero marcada `NO DEDUCIBLE` por falta de soporte; carta al cliente explicando el efecto fiscal y el protocolo de actas; monto ≥ 50 UVT → escalamiento a EspecialistaCostos; se programa verificación de la familia de ítems en el próximo conteo cíclico.

═══════════════════════════════════════════════════════════════════════

---
name: evaluar-VNR-NIC-2
description: Activa al cierre de cada periodo para comparar costo vs Valor Neto Realizable por ítem (NIC 2 / Sección 13). Si VNR < costo, registra deterioro de inventarios; controla reversiones y marca la diferencia temporaria fiscal (el deterioro contable no es deducible hasta la enajenación).
agente: RITORE-AuxiliarInventarios-Senior
categoria: operativo
---

# Skill: evaluar-VNR-NIC-2

## Para qué existe
NIC 2 obliga a medir inventarios al MENOR entre costo y VNR. Sin esta evaluación, los inventarios de lenta rotación, dañados o con precios de venta caídos quedan sobrevaluados en EEFF — la otra cara del problema de **Cliente - AGROPECUARIA D**.

## Cuándo se activa
- Cierre mensual (screening) y cierre anual (evaluación completa obligatoria).
- Señales: ítems sin rotación > 180 días, precios de lista por debajo del costo, daños reportados, colecciones/temporadas vencidas.
- Solicitud de EspecialistaNIIF o del Revisor Fiscal.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Kardex valorizado por ítem con fecha de última venta | Módulo de inventarios | Caché con marca `[DATO EN CACHÉ — verificar]` si no responde en 4 h |
| Lista de precios de venta vigente y descuentos/promociones programadas | Cliente / área comercial | Reiterar 1 vez en 24 h hábiles; sin precios, evaluar solo los ítems con señal de daño y reportar evaluación `parcial` |
| Costos estimados de terminación y de venta (comisiones, fletes de salida, empaque) | EspecialistaCostos | Usar % histórico del cliente documentado como supuesto |

## Procedimiento
1. Calcular VNR por ítem = precio estimado de venta − costos de terminación − costos necesarios para la venta. La comparación es ítem por ítem (o por familias de ítems relacionados), nunca por el total del inventario.
2. Identificar ítems con VNR < costo: lenta rotación, dañados, obsoletos, con promociones por debajo del costo.
3. Registrar deterioro = costo − VNR por ítem, contra gasto del periodo (asiento vía AuxContable; el kardex conserva el costo y el deterioro se controla en cuenta correctora).
4. Materias primas: solo se deterioran si el producto terminado en que se incorporarán se venderá por debajo del costo (el costo de reposición es la referencia práctica).
5. Reversión: si en periodos siguientes el VNR se recupera, revertir el deterioro con tope en el deterioro previamente reconocido.
6. Marca fiscal: el deterioro contable de inventarios NO es deducible hasta la enajenación o destrucción soportada (Arts. 59 y 64 ET) → diferencia temporaria; entregar cuantificación a EspecialistaRenta y EspecialistaNIIF (impuesto diferido).
7. Reportar a EspecialistaCostos los ítems deteriorados recurrentes (insumo para política de compras y descuentos).

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Papel de trabajo VNR | Ítem por ítem; supuestos de precio y costos de venta documentados y reproducibles |
| Asiento de deterioro/reversión | Reversión nunca supera el deterioro acumulado previo del ítem |
| Marca de diferencia temporaria | Cuantificada y entregada al papel de impuesto diferido |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| VNR calculado con precios de lista que nadie paga (descuentos reales no considerados) | Lista comercial desactualizada | Usar precios de las últimas ventas reales del ítem (90 días) | Escalar el supuesto a EspecialistaCostos con ambos cálculos |
| Deterioro calculado sobre el total del inventario (global) | Método incorrecto | Rehacer ítem por ítem | No asentar el global; evaluación queda `pendiente` y se reporta al cierre |
| Cliente presiona para no reconocer deterioro en año de malos resultados | Gestión de resultados | Presentar el papel de trabajo con la norma (NIC 2.28-33) | Escalar a EspecialistaNIIF y, si el monto ≥ 500 UVT, al Contador Titular; el deterioro no se omite |

## Escalamiento
- Deterioro del periodo ≥ 50 UVT → EspecialistaCostosInventarios + EspecialistaNIIF.
- Deterioro ≥ 500 UVT o disputa con el cliente sobre reconocerlo → Contador Titular.
- Deterioro que sugiere inventario invendible masivo (> 10 % del inventario total) → Contador Titular (posible asunto de negocio en marcha para el dictamen).

## Reglas críticas
🚫 NUNCA evaluar VNR por el total del inventario: es ítem por ítem (o familias relacionadas).
🚫 NUNCA revertir deterioro por encima del previamente reconocido para ese ítem.
✅ SIEMPRE marcar el deterioro como diferencia temporaria (no deducible hasta enajenación, Arts. 59/64 ET).

## Métricas
- Evaluación VNR completa al cierre anual: 100 % de clientes con inventarios.
- Ítems sin rotación > 180 días evaluados: 100 % en cada cierre trimestral.

## Tests
### Test 1 — (normal) Retail de ropa: colección de temporada pasada, costo $30M, precio de liquidación estimado $24M, comisiones y empaque $2M
**Output:** VNR $22M < costo $30M → deterioro $8M a gasto, cuenta correctora; papel ítem por ítem; diferencia temporaria $8M al impuesto diferido; reporte a EspecialistaCostos sobre la familia afectada.
### Test 2 — (excepción) El año siguiente la colección se vende bien y el área comercial pide revertir $10M "porque el mercado mejoró"
**Output:** reversión LIMITADA a los $8M de deterioro previamente reconocido (tope NIC 2); los $2M adicionales se rechazan con referencia al papel del año anterior; asiento de reversión $8M; actualización de la diferencia temporaria; criterio documentado.

═══════════════════════════════════════════════════════════════════════

---
name: gestionar-inventario-en-consignacion
description: Activa cuando el cliente entrega o recibe mercancía en consignación. Separa titularidad de custodia — lo entregado sigue siendo inventario propio hasta que el consignatario venda; lo recibido NO entra al inventario propio — y coordina facturación, conteos en ubicaciones de terceros y conciliación de informes de venta.
agente: RITORE-AuxiliarInventarios-Senior
categoria: operativo
---

# Skill: gestionar-inventario-en-consignacion

## Para qué existe
La consignación rompe la regla "lo que está en mi bodega es mío": confundir titularidad con custodia infla o esconde inventarios, anticipa o difiere ingresos y descuadra el IVA. Es de los errores de clasificación más comunes en retail y distribución.

## Cuándo se activa
- Contrato o acuerdo de consignación (como consignante o consignatario) reportado por el cliente o detectado en remisiones sin factura.
- Informe periódico de ventas del consignatario.
- Conteo físico que encuentra mercancía de terceros en bodega (o mercancía propia fuera).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Contrato de consignación (partes, comisión, periodicidad de informes, responsabilidad por pérdidas) | Cliente | Operar provisionalmente con las remisiones marcando `[CONTRATO PENDIENTE]`; reiterar 1 vez en 24 h hábiles y reportar al Orquestador si no llega |
| Remisiones de entrega/recepción en consignación | Bodega / consignatario | Sin remisión no se mueve el control de consignación |
| Informe de ventas del consignatario del periodo | Consignatario vía cliente | Reiterar 1 vez; si no llega en 24 h hábiles, estimar $0 ventas (no se reconoce ingreso sin informe) y escalar el atraso |

## Procedimiento
1. Identificar el rol del cliente: consignante (dueño que entrega) o consignatario (quien recibe para vender).
2. **Como consignante:** la mercancía entregada PERMANECE en el inventario propio, reclasificada a una sub-bodega "inventario en consignación en poder de terceros" en el kardex; la remisión NO es factura ni venta; el ingreso y el costo de ventas se reconocen solo cuando el consignatario reporta la venta al tercero final; facturar al consignatario según el informe.
3. **Como consignatario:** la mercancía recibida NO entra al inventario propio — control en cuentas de orden / módulo de bienes de terceros; al vender, se reconoce el ingreso por la venta y el pasivo con el consignante (o solo la comisión, según estructura del contrato); conciliar liquidaciones.
4. Conciliar mensualmente: existencias reportadas por el consignatario + ventas informadas = entregas acumuladas (en cantidades y costo). Toda diferencia se trata como faltante en consignación (responsabilidad según contrato).
5. Incluir SIEMPRE las ubicaciones de consignación en los conteos físicos de `realizar-inventario-fisico-y-tratar-diferencias` (conteo en sitio del tercero o confirmación escrita de existencias).
6. Coordinar con EspecialistaIVA el momento de causación del IVA (la entrega en consignación no es venta; el hecho generador ocurre con la venta efectiva) y con FacturacionElectronica la secuencia remisión → informe → factura.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Kardex con sub-bodegas de consignación | Inventario propio total = bodegas propias + en poder de terceros; bienes de terceros NUNCA suman al propio |
| Conciliación mensual por consignatario | Entregas = existencias reportadas + ventas informadas; diferencia $0 o tratada como faltante |
| Reconocimiento de ingreso correcto | Cero ingresos reconocidos con remisión; solo con informe/venta efectiva |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Consignatario no envía informe de ventas | Informalidad del canal | Reiterar; bloquear nuevas entregas a ese consignatario hasta recibir informe | Confirmación de existencias en sitio; diferencias como faltante según responsabilidad del contrato |
| Remisión de consignación facturada como venta | FacturacionElectronica procesó la remisión como factura | Anular el ingreso y reclasificar; nota crédito si ya se emitió FE | Escalar a FacturacionElectronica y EspecialistaIVA para corregir el periodo de IVA |
| Mercancía de tercero contada como propia en el conteo | Bodega no separa físicamente la consignación recibida | Marcar y excluir del inventario propio; exigir separación física o etiquetado | Ajustar el informe del conteo y reportar la debilidad de control al cliente |

## Escalamiento
- Diferencia en conciliación con un consignatario ≥ 1 UVT individual o ≥ 0,5 % de lo entregado → investigar antes de nuevas entregas.
- Diferencia ≥ 50 UVT → EspecialistaCostosInventarios; ≥ 500 UVT → Contador Titular.
- Consignatario sin informes > 60 días con mercancía ≥ 50 UVT en su poder → Contador Titular (riesgo de pérdida y de subdeclaración de ingresos).

## Reglas críticas
🚫 NUNCA reconocer ingreso con la remisión de consignación: solo con la venta efectiva informada.
🚫 NUNCA sumar al inventario propio mercancía recibida en consignación.
✅ SIEMPRE incluir las existencias en poder de terceros en los conteos físicos (en sitio o por confirmación escrita).

## Métricas
- Conciliaciones mensuales de consignación al día: 100 % de los consignatarios activos.
- Ingresos reconocidos con soporte de venta efectiva (no remisión): 100 %.

## Tests
### Test 1 — (normal) Cliente consignante entrega 500 unidades (costo $20M) a un almacén; el informe mensual reporta 120 vendidas
**Output:** entrega reclasificada a sub-bodega "en poder de terceros" sin tocar resultados; con el informe: ingreso por 120 unidades + costo de ventas $4,8M + factura al consignatario; existencias en terceros 380 unidades conciliadas (500 = 380 + 120); IVA causado solo sobre lo vendido.
### Test 2 — (excepción) En el conteo físico del consignatario aparecen 340 unidades en vez de las 380 esperadas, y el contrato hace responsable al consignatario
**Output:** diferencia de 40 unidades (costo $1,6M) confirmada con segundo conteo; tratada como faltante en consignación: cuenta por cobrar al consignatario según contrato (no como merma propia); si supera 50 UVT acumulado se escala a EspecialistaCostos; bloqueo de nuevas entregas hasta firmar acta de la diferencia.

═══════════════════════════════════════════════════════════════════════

---
name: escalar-criterio-costos-master
description: Activa cuando un tratamiento de costo o de inventarios excede la competencia operativa de este agente — cambios de método, costeo por procesos/órdenes complejo, subproductos, capitalización dudosa, patrones anómalos. Empaqueta la consulta con contexto completo para EspecialistaCostosInventarios-Master y gestiona la respuesta dentro del SLA.
agente: RITORE-AuxiliarInventarios-Senior
categoria: operativo
---

# Skill: escalar-criterio-costos-master

## Para qué existe
Un Senior ejecuta procesos; no decide criterios nuevos (§1 del estándar). Esta skill garantiza que las consultas al Master lleguen completas (una sola ida y vuelta, no un ping-pong) y que el trabajo no se quede bloqueado esperando.

## Cuándo se activa
- Cualquier skill de este perfil encuentra un caso fuera de procedimiento: tratamiento de subproductos/coproductos, costeo conjunto, cambio de método de valorización solicitado, capitalización dudosa de costos indirectos, sectores con norma especial (agro: activos biológicos NIC 41 → en frontera con inventarios).
- Diferencia o ajuste ≥ 50 UVT (umbral §3) en cualquier skill del perfil.
- Mismo tipo de duda aparece por 2.ª vez en 30 días (señal de vacío de procedimiento).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Caso documentado: cliente, ítems, montos, documentos soporte | La skill que origina la consulta | No se escala "en abstracto": completar el expediente primero |
| Lo intentado y por qué no alcanza (procedimiento aplicado + punto de bloqueo) | Este agente | Obligatorio: una consulta sin intento previo se devuelve sola |
| Propuesta de tratamiento (mi mejor hipótesis con norma de referencia) | Este agente | Obligatorio: el Master decide entre opciones, no redacta desde cero |

## Procedimiento
1. Verificar que el caso realmente excede competencia (¿está cubierto por una variante de `gestionar-movimiento-kardex` o por otra skill? ¿el umbral §3 obliga a escalar?).
2. Empaquetar la consulta: (a) contexto del cliente y montos, (b) pregunta concreta y única, (c) lo que intenté y dónde se bloquea, (d) mi propuesta con referencia normativa (NIC 2 / Art. 62-65 ET / política del cliente), (e) impacto de no decidir (¿bloquea cierre? ¿plazo legal?).
3. Emitir al bus hacia `10-EspecialistaCostosInventarios-Master` con prioridad según impacto: bloquea cierre o plazo legal → alta (SLA 4 h); resto → normal (SLA 24 h).
4. Mientras llega respuesta: continuar el trabajo no dependiente; el movimiento bloqueado queda con marca `[CRITERIO EN CONSULTA]` y NO se asienta provisional salvo instrucción del Master.
5. Si el Master no responde al 80 % del SLA → alerta al Orquestador; al 100 % → aplicar §3: usar el último criterio verificado equivalente con marca `[DATO EN CACHÉ — verificar]` solo si existe precedente directo, y escalar en paralelo; si no hay precedente, el caso queda bloqueado y sube al Orquestador.
6. Recibida la decisión: aplicarla, registrarla en la ficha del cliente como precedente y, si el caso se repitió ≥ 2 veces, proponer al Master que se incorpore como variante/regla en la skill de origen.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Paquete de consulta | Contiene los 5 elementos del paso 2; pregunta única y cerrada |
| Decisión aplicada y documentada | Precedente registrado en la ficha del cliente con fecha y autor |
| Propuesta de mejora de skill (si recurrente) | Emitida al Master cuando el mismo criterio se consultó ≥ 2 veces en 30 días |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Master devuelve la consulta por contexto insuficiente | Paquete incompleto (faltó documento o monto) | Completar y reenviar el MISMO hilo (no abrir consulta nueva) | Revisar el checklist del paso 2 con el Orquestador para corregir el patrón |
| Respuesta del Master contradice una política escrita del cliente | Política desactualizada o caso excepcional | Señalar la contradicción al Master en el mismo hilo antes de aplicar | Aplicar lo que decida el Master tras conocer la contradicción y dejar ambas referencias documentadas |
| Consulta urgente sin respuesta y vence plazo legal | Master saturado | Alerta 80 % SLA ya emitida; al 100 % escalar al Orquestador con prioridad crítica | Orquestador decide (redistribución o decisión del Contador Titular); NUNCA decidir el criterio yo mismo |

## Escalamiento
- SLA de la consulta: alta 4 h / normal 24 h; al 80 % → Orquestador; al 100 % → fallback §3 + escalamiento.
- Caso con efecto ≥ 500 UVT → el paquete va simultáneamente al Master y al Contador Titular (informativo).
- Conflicto entre decisión del Master y plazo legal inminente → Orquestador con prioridad crítica.

## Reglas críticas
🚫 NUNCA decidir un criterio nuevo por mi cuenta: propongo, el Master dispone (§1 del estándar).
🚫 NUNCA asentar provisionalmente un movimiento bajo `[CRITERIO EN CONSULTA]` sin instrucción del Master.
✅ SIEMPRE registrar la decisión como precedente reutilizable en la ficha del cliente.

## Métricas
- Consultas resueltas en una sola ida y vuelta (sin devolución por contexto): ≥ 90 % (medición mensual).
- Precedentes documentados tras cada decisión: 100 %.
- Consultas recurrentes convertidas en propuesta de mejora de skill: 100 % de las que se repiten ≥ 2 veces en 30 días.

## Tests
### Test 1 — (normal) Cliente avícola pregunta cómo costear el subproducto (gallinaza) que empezó a vender; no hay precedente
**Output:** paquete completo al Master: contexto, montos, intento (no hay variante aplicable en `gestionar-movimiento-kardex`), propuesta (valor residual neto deducido del costo del producto principal, NIC 2.14) e impacto (no bloquea cierre → prioridad normal); decisión recibida en SLA, aplicada y registrada como precedente del cliente.
### Test 2 — (excepción) Consulta con prioridad alta (bloquea cierre del día 5) sin respuesta del Master al 100 % del SLA de 4 h
**Output:** alerta al Orquestador emitida desde el 80 % (3,2 h); al 100 %, se identifica precedente directo del mismo cliente del trimestre anterior → se aplica con marca `[DATO EN CACHÉ — verificar]`, escalamiento en paralelo se mantiene; al responder el Master, se valida el tratamiento y se retira la marca; todo el hilo queda en el bus.

═══════════════════════════════════════════════════════════════════════

## Relacionado
- *MOC - Agentes RITORE*
- *Proyecto - Ecosistema RITORE*
- [[00 - Estandar de Agentes RITORE]]
- [[Skills Compartidas RITORE]]
- [[10-EspecialistaCostosInventarios-Master]]
- *11-EspecialistaIVA-Master*
- **Cliente - AGROPECUARIA D**
- **Cliente - COMERCIO DE BICICLETAS A**
- [[Aux 18 - Juego de Inventarios]]

## Historial de versiones
| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-05-19 | Versión inicial consolidada (9 skills) | RITORE |
| 2.0 | 2026-06-11 | Reescritura según Estandar de Agentes v1.0: deduplicación de skills (9 → 6; movimientos de kardex consolidados en `gestionar-movimiento-kardex` con variantes; conteo físico + faltantes/sobrantes unificados), inputs/outputs, umbrales numéricos, manejo de errores | RITORE |
