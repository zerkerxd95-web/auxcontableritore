---
tipo: agente
tags: [ritore, agente, operativa]
capa: operativa
nivel: senior
estado: activo
version: 2.0
fecha: 2026-06-11
---

# SKILLS — 08-AuxiliarActivosFijos-Senior

**Documento consolidado** · 8 skills · Ecosistema RITORE · v2.0
**Modelo:** claude-opus-4-7

> Reescritura completa según [[00 - Estandar de Agentes RITORE]] (§2 secciones obligatorias, §3 umbrales, §4 anti-clonación). Las 4 skills del ciclo ordinario de PPE (adquisición, depreciación contable, depreciación fiscal, conciliación contable-fiscal) se consolidaron en una skill base con variantes paramétricas porque compartían > 70 % del procedimiento. Las reglas universales (soporte documental, no inventar datos, registro en bus) se heredan de [[Skills Compartidas RITORE]] y no se repiten aquí.

---

## Índice de skills en este documento

- `gestionar-ciclo-PPE` *(base paramétrica: adquisición · depreciación contable · depreciación fiscal · conciliación contable-fiscal)*
- `evaluar-deterioro-NIC-36`
- `gestionar-baja-PPE`
- `realizar-inventario-fisico-PPE`
- `reclasificar-PPE-vs-Inventario-vs-Propiedad-Inversion`
- `aplicar-NIC-40-propiedad-de-inversion`
- `registrar-intangible-NIC-38-Seccion-18`
- `valorizar-revaluacion-NIC-16`

═══════════════════════════════════════════════════════════════════════

---
name: gestionar-ciclo-PPE
description: Skill base del ciclo ordinario de propiedad, planta y equipo. Cubre 4 variantes paramétricas — registrar adquisición, calcular depreciación contable mensual (NIC 16 / Sec. 17), calcular depreciación fiscal anual (Art. 137 ET) y conciliar contable vs fiscal para impuesto diferido y F-2516. Activa según la variante (evento de compra, cron mensual, cron anual, cierre fiscal).
agente: RITORE-AuxiliarActivosFijos-Senior
categoria: operativo
---

# Skill: gestionar-ciclo-PPE

## Para qué existe
El ciclo ordinario de PPE (alta → depreciación contable → depreciación fiscal → conciliación) comparte la misma columna vertebral: ficha del activo, vida útil dual, cálculo y asiento. Si el ciclo se rompe en cualquier punto, los EEFF muestran activos mal medidos, el gasto de depreciación se distorsiona y el F-2516 sale con diferencias contable-fiscales sin clasificar.

## Cuándo se activa (por variante)

| Variante | Trigger |
|---|---|
| **A — Adquisición** | Factura/contrato de compra, leasing financiero, donación o acta de capitalización de construcción propia llega vía AuxContable o CarteraCxP |
| **B — Depreciación contable mensual** | Cron del cierre mensual (D+3 del cronograma del Orquestador) |
| **C — Depreciación fiscal anual** | Cron del cierre fiscal (enero, dentro del plan de cierre anual) |
| **D — Conciliación contable-fiscal** | Tras completar B (12 meses) y C; solicitud de EspecialistaRenta o EspecialistaNIIF |

## Inputs

| Insumo | De quién | Formato | Si falta |
|---|---|---|---|
| Perfil del cliente (marco NIIF, política de PPE, cuantía mínima de capitalización) | `cargar-perfil-cliente` | Ficha Notion | Solicitar a NotionArquitecto; espera máx. 24 h hábiles, luego escalar a Orquestador |
| Factura/contrato + costos atribuibles (transporte, instalación, aranceles) — variante A | AuxContable / cliente | XML FE o PDF | Suspender el alta; reiterar solicitud 1 vez en 24 h hábiles; sin soporte NO se capitaliza |
| Maestro de activos (costo, vida útil dual, residual, método, fecha inicio de uso) — variantes B, C, D | Módulo activos del ERP | Export tabla | Si el módulo no responde en 4 h, usar último maestro verificado con marca `[DATO EN CACHÉ — verificar]` y escalar en paralelo |
| Tasas máximas fiscales Art. 137 ET vigentes | MonitoreoNormativo | Tabla parametrizada | Usar última tabla vigente conocida y pedir confirmación a EspecialistaRenta |

## Procedimiento

**Tronco común (toda variante):**
1. `cargar-perfil-cliente`: marco (NIIF Plenas / PYMES), política de PPE, cuantía mínima de capitalización.
2. Validar que el activo existe en el maestro con ficha completa (variantes B-D) o crear la ficha (variante A).
3. Ejecutar los pasos de la variante (tabla siguiente).
4. Generar asiento propuesto y enviarlo a AuxContable; registrar en el módulo de activos.
5. Notificar: EspecialistaNIIF (criterios aplicados), EspecialistaRenta (efecto fiscal), AuxContable (asiento).

**Pasos específicos por variante:**

| Variante | Pasos propios |
|---|---|
| **A — Adquisición** | (a) Determinar costo: precio + costos directamente atribuibles hasta condiciones de uso; en construcción propia, evaluar capitalización de intereses NIC 23 si es activo apto. (b) Componentizar si las partes tienen vidas útiles materialmente distintas. (c) Asignar vida útil contable (política) y fiscal (Art. 137 ET), valor residual y método. (d) Si costo < 50 UVT, marcar como depreciable fiscalmente en el mismo año (DUR 1625/2016). (e) Validar IVA descontable de bien productivo con EspecialistaIVA si el caso es ambiguo. (f) Asignar centro de costos y código de etiqueta física. |
| **B — Depreciación contable** | (a) Calcular cuota mensual por activo/componente: (costo − residual − deterioro acumulado) / vida útil restante, según método de la política (línea recta, saldos decrecientes, unidades de producción). (b) Verificar tope: depreciación acumulada + cuota ≤ valor depreciable. (c) Consolidar resumen por cuenta PUC y centro de costos. |
| **C — Depreciación fiscal** | (a) Aplicar tasa máxima anual del Art. 137 ET por clase de activo (referencia: construcciones 2,22 % ≈ 45 años; maquinaria y flota terrestre 10 %; equipo de cómputo y comunicación 20 % ≈ 5 años). (b) Si la tasa contable excede la fiscal, limitar la deducción al tope fiscal y registrar el exceso como diferencia. (c) Aplicar regla de activos menores (< 50 UVT) del paso A-d. |
| **D — Conciliación contable-fiscal** | (a) Por activo: depreciación contable acumulada vs fiscal acumulada → base contable vs base fiscal. (b) Clasificar cada diferencia: temporaria (vida útil dual, tope Art. 137) o permanente. (c) Calcular impuesto diferido por activo y consolidado; entregar papel de trabajo a EspecialistaNIIF y mapeo a renglones del F-2516 a EspecialistaRenta. |

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Ficha de activo completa (variante A) | 100 % de campos: costo, vida útil dual, residual, método, centro de costos, código de etiqueta |
| Asiento propuesto a AuxContable | Cuadrado (débitos = créditos); cuentas PUC válidas; referencia al documento soporte |
| Resumen de depreciación del periodo (B/C) | Total del resumen = suma del detalle por activo, diferencia $0; ningún activo con depreciación > valor depreciable |
| Papel de trabajo conciliación (D) | 100 % de diferencias clasificadas temporaria/permanente; cuadre contra balance de prueba a la misma fecha de corte |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Cuota calculada deja valor en libros negativo | Vida útil o residual mal parametrizados; deterioro previo no descontado | Recalcular con datos del maestro; corregir parámetro y documentar | Excluir el activo del lote, asentar el resto y escalar el caso a EspecialistaNIIF |
| Factura sin discriminar costos atribuibles (variante A) | Proveedor factura global (equipo + instalación + capacitación) | Pedir desglose al emisor; capitalizar solo lo directamente atribuible | Capitalizar el valor del bien y llevar a gasto lo no soportado como atribuible, dejando nota para NIIF |
| Vida útil del maestro ≠ política del cliente | Alta antigua sin homologar política | Alertar a EspecialistaNIIF antes de asentar; no cambiar vida útil por cuenta propia | Asentar con la vida útil vigente marcada `[EN REVISIÓN NIIF]` y registrar seguimiento |
| Depreciación fiscal aplicada supera tasa máxima Art. 137 ET | Parametrización copió la vida útil contable al campo fiscal | Recalcular con tope fiscal; cuantificar exceso de ejercicios anteriores | Escalar a EspecialistaRenta con cuantificación para evaluar corrección de declaraciones |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia conciliación física/contable o de cálculo | ≥ 1 UVT individual o ≥ 0,5 % del total del rubro | Investigar y documentar antes de asentar |
| Diferencia o ajuste | ≥ 50 UVT | EspecialistaNIIF (criterio contable) / EspecialistaRenta (criterio fiscal) |
| Diferencia o ajuste | ≥ 500 UVT | Contador Titular vía Orquestador |
| Exceso de deducción fiscal en años ya declarados | Cualquier monto | EspecialistaRenta (posible corrección de declaración) |
| Insumo faltante (factura, maestro, tabla fiscal) | > 24 h hábiles tras reiterar 1 vez | Orquestador |

## Reglas críticas
🚫 NUNCA capitalizar costos no directamente atribuibles (capacitación, publicidad de lanzamiento, gastos administrativos).
🚫 NUNCA confundir mantenimiento (gasto) con mejora que extiende vida útil o capacidad (capitaliza).
🚫 NUNCA deducir fiscalmente por encima de la tasa máxima del Art. 137 ET.
✅ SIEMPRE mantener vida útil contable y fiscal como campos separados del maestro y conciliar su efecto en la variante D.

## Métricas
- Depreciación mensual asentada a más tardar D+3 del cierre: 100 % de los meses.
- Activos con depreciación acumulada > valor depreciable: 0 (medición mensual).
- Diferencias contable-fiscales clasificadas (temporaria/permanente) en la conciliación anual: 100 %.
- Altas con ficha completa al primer intento: ≥ 95 % (medición trimestral).

## Tests
### Test 1 — (normal, variante A+B) Compra de equipo de cómputo por $9.000.000 + IVA
**Output:** capitalización por el costo sin IVA (IVA descontable como bien productivo), vida útil contable 4 años / fiscal 5 años (20 %), cuota mensual contable $187.500, diferencia temporaria marcada para la variante D, ficha con código de etiqueta y centro de costos.
### Test 2 — (excepción, variante D) Vehículo depreciado fiscalmente a 4 años cuando el tope Art. 137 ET es 10 % anual
**Output:** detección del exceso de deducción, recálculo al tope fiscal, cuantificación del exceso de los 2 años ya declarados y escalamiento a EspecialistaRenta con papel de trabajo; el asiento contable NO se modifica (el error es fiscal, no contable).

═══════════════════════════════════════════════════════════════════════

---
name: evaluar-deterioro-NIC-36
description: Activa cuando hay indicios de deterioro de un activo (daño, obsolescencia, caída material de valor o de demanda) o en el test anual obligatorio para intangibles de vida indefinida (NIC 36 / Sec. 27 PYMES). Compara valor recuperable vs valor en libros y registra la pérdida si procede.
agente: RITORE-AuxiliarActivosFijos-Senior
categoria: operativo
---

# Skill: evaluar-deterioro-NIC-36

## Para qué existe
Un activo deteriorado no detectado mantiene los EEFF sobrevaluados y la depreciación futura mal calculada. Esta skill convierte indicios en una medición disciplinada de valor recuperable.

## Cuándo se activa
- Indicio reportado: daño físico, obsolescencia tecnológica, activo ocioso, caída del precio de mercado del activo o de los ingresos que genera.
- Test anual obligatorio (intangibles de vida indefinida o plusvalía, solo Plenas).
- Solicitud de EspecialistaNIIF o del Revisor Fiscal durante cierre.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Descripción del indicio + evidencia (fotos, reporte técnico, datos de mercado) | Cliente / agente que reporta | Solicitar; sin evidencia el test no se ejecuta y se documenta el indicio como pendiente (espera 24 h hábiles, luego Orquestador) |
| Valor en libros del activo o UGE | Maestro de activos | Caché con marca `[DATO EN CACHÉ — verificar]` si módulo no responde en 4 h |
| Datos para valor recuperable: precio de venta estimado, costos de disposición, flujos proyectados y tasa de descuento | Cliente + EspecialistaFinanciero | Si no hay flujos confiables, usar solo valor razonable − costos de venta y dejarlo documentado |

## Procedimiento
1. Confirmar que el indicio es real y específico del activo o de su UGE (no ruido de mercado general).
2. Determinar la unidad de evaluación: activo individual o UGE si el activo no genera flujos independientes.
3. Calcular valor recuperable = MAYOR entre (valor razonable − costos de disposición) y (valor en uso = flujos descontados).
4. Comparar contra valor en libros. Si recuperable ≥ libros → documentar test sin ajuste. Si recuperable < libros → pérdida por deterioro por la diferencia.
5. Proponer asiento (gasto por deterioro contra deterioro acumulado) y recalcular la depreciación futura sobre la nueva base.
6. Marcar el deterioro como NO deducible fiscalmente hasta la enajenación → diferencia temporaria para impuesto diferido (notificar a EspecialistaNIIF y EspecialistaRenta).
7. En periodos siguientes, evaluar reversión si los indicios desaparecen (tope: valor en libros que existiría sin deterioro previo).

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Memoria del test (indicio, método, supuestos, resultado) | Reproducible: un tercero llega al mismo valor con los supuestos documentados |
| Asiento de deterioro o constancia de test sin ajuste | Cuadrado; nueva base de depreciación recalculada |
| Marca de diferencia temporaria | Visible en el papel de impuesto diferido de `gestionar-ciclo-PPE` variante D |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Flujos proyectados inconsistentes con presupuesto del cliente | Cliente entrega proyecciones optimistas ad-hoc para el test | Contrastar con presupuesto aprobado y resultados históricos; pedir justificación | Usar solo valor razonable − costos de venta y escalar el criterio a EspecialistaNIIF |
| Tasa de descuento sin soporte | No hay WACC documentado | Solicitar a EspecialistaFinanciero una tasa de referencia sectorial | Sensibilizar con rango de tasas y escalar la elección a EspecialistaNIIF |
| Reversión propuesta supera el costo histórico depreciado | Error de tope en el cálculo | Limitar al valor en libros que existiría sin el deterioro | No asentar; escalar a EspecialistaNIIF con el cálculo |

## Escalamiento
- Pérdida por deterioro ≥ 50 UVT → validación de EspecialistaNIIF antes de asentar.
- Pérdida ≥ 500 UVT o deterioro de una UGE completa → Contador Titular vía Orquestador.
- Indicio durante cierre anual con dictamen en curso → notificar también al RevisorFiscal el mismo día.

## Reglas críticas
🚫 NUNCA registrar deterioro sin memoria de cálculo reproducible.
🚫 NUNCA revertir deterioro por encima del valor en libros que existiría sin la pérdida previa.
✅ SIEMPRE recalcular la depreciación futura sobre la base deteriorada.

## Métricas
- Tests con memoria de cálculo completa: 100 %.
- Indicios reportados evaluados en ≤ 5 días hábiles: ≥ 90 % (medición trimestral).

## Tests
### Test 1 — (normal) Maquinaria dañada por inundación; valor en libros $80M, valor razonable − costos de venta $45M, valor en uso $52M
**Output:** valor recuperable $52M (el mayor), pérdida por deterioro $28M, asiento propuesto, depreciación futura sobre $52M, diferencia temporaria marcada (no deducible fiscal).
### Test 2 — (excepción) Cliente entrega flujos que duplican los ingresos históricos del activo sin justificación
**Output:** test NO se cierra con esos flujos; se contrasta con presupuesto, se calcula con valor razonable − costos de venta como única referencia confiable y se escala el criterio a EspecialistaNIIF documentando la inconsistencia.

═══════════════════════════════════════════════════════════════════════

---
name: gestionar-baja-PPE
description: Activa cuando se vende, retira, destruye o dona un activo fijo. Da de baja costo y depreciación acumulada, calcula utilidad o pérdida, gestiona el efecto IVA y la renta por recuperación de deducciones, y exige acta de baja.
agente: RITORE-AuxiliarActivosFijos-Senior
categoria: operativo
---

# Skill: gestionar-baja-PPE

## Para qué existe
Una baja mal registrada deja activos fantasma en libros (sobrevaluación) o borra activos sin soporte (riesgo de fiscalización y de responsabilidad por custodia). El resultado de la venta tiene además efectos fiscales propios que el ciclo ordinario no cubre.

## Cuándo se activa
- Factura de venta de activo fijo emitida por el cliente.
- Acta de retiro, destrucción, siniestro o donación.
- Faltante confirmado por `realizar-inventario-fisico-PPE`.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Documento de la baja (factura de venta, acta de destrucción/donación, denuncia si hurto) | Cliente / AuxContable | NO se da de baja sin documento; reiterar 1 vez en 24 h hábiles, luego Orquestador |
| Ficha del activo: costo, depreciación acumulada, deterioro acumulado, superávit por revaluación si existe | Maestro de activos | Caché con marca `[DATO EN CACHÉ — verificar]`; la baja no se asienta hasta confirmar saldos |
| Valor de la transacción (si venta o permuta) | Factura | Solicitar; sin precio no hay cálculo de resultado |

## Procedimiento
1. Verificar documento soporte y que el activo exista en el maestro con saldos al día (correr depreciación del mes de la baja hasta la fecha de la operación).
2. Calcular valor en libros = costo − depreciación acumulada − deterioro acumulado.
3. Calcular resultado = precio de venta (o $0 si retiro/destrucción) − valor en libros − costos de disposición.
4. Efecto IVA: la venta de activos fijos en general NO genera IVA (no es del giro ordinario); validar excepciones (automotores vendidos por intermediarios, activos formados para la venta) con EspecialistaIVA si hay duda.
5. Efecto renta: si hay utilidad y el activo se poseyó ≥ 2 años → ganancia ocasional; si < 2 años → renta líquida; la utilidad hasta el monto de la depreciación deducida es renta por recuperación de deducciones (Art. 195 ET). Marcar para EspecialistaRenta.
6. Si el activo tenía superávit por revaluación (ORI), trasladarlo a utilidades retenidas (nunca a resultados).
7. Asiento de baja vía AuxContable; retirar etiqueta y registro del inventario físico de PPE; archivar acta.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Asiento de baja | Costo y depreciación acumulada quedan en $0 para el activo; resultado calculado y clasificado |
| Marca fiscal (ganancia ocasional / renta / recuperación de deducciones) | Entregada a EspecialistaRenta con fecha de adquisición y depreciación deducida histórica |
| Acta de baja archivada | Firmada por responsable del cliente; referenciada en la ficha del activo |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Activo a dar de baja no aparece en el maestro | Nunca se capitalizó o se dio de baja antes sin trazabilidad | Buscar en histórico y en altas pendientes; reconstruir ficha | Escalar a EspecialistaNIIF: posible error de ejercicios anteriores (corrección NIC 8) |
| Venta por valor muy inferior al de mercado a una parte vinculada | Operación entre vinculados sin soporte de precio | Solicitar avalúo o justificación del precio | Asentar solo con instrucción escrita del cliente y alerta al Contador Titular (riesgo fiscal Art. 90 ET) |
| Baja por hurto sin denuncia | Cliente quiere "limpiar" el activo sin soporte | Exigir denuncia o acta interna firmada | No asentar; documentar la negativa y escalar al Orquestador |

## Escalamiento
- Resultado de la baja (utilidad o pérdida) ≥ 50 UVT → revisión de EspecialistaRenta antes de cerrar el mes.
- Baja individual o lote ≥ 500 UVT de valor en libros → aprobación del Contador Titular.
- Indicio de baja para ocultar activos o simular pérdidas → Contador Titular + nota a SAGRLAFT, mismo día.

## Reglas críticas
🚫 NUNCA dar de baja sin documento soporte (factura, acta o denuncia).
🚫 NUNCA llevar el superávit por revaluación del activo dado de baja a resultados.
✅ SIEMPRE correr la depreciación hasta la fecha exacta de la baja antes de calcular el resultado.

## Métricas
- Bajas con acta/documento archivado: 100 %.
- Bajas asentadas dentro del mes de la operación: ≥ 95 % (medición mensual).

## Tests
### Test 1 — (normal) Venta de vehículo: costo $60M, depreciación acumulada $36M, precio de venta $30M, poseído 4 años
**Output:** valor en libros $24M, utilidad $6M; como la utilidad ($6M) es menor que la depreciación deducida ($36M), se marca íntegramente como renta por recuperación de deducciones (Art. 195 ET) para EspecialistaRenta; sin IVA por no ser del giro ordinario; asiento de baja y acta archivada.
### Test 2 — (excepción) Cliente pide dar de baja maquinaria "perdida" sin denuncia ni acta
**Output:** baja NO asentada; solicitud formal de acta o denuncia con plazo 24 h hábiles; al vencer, escalamiento al Orquestador con el caso documentado y el activo marcado `[FALTANTE SIN SOPORTE]` en el maestro.

═══════════════════════════════════════════════════════════════════════

---
name: realizar-inventario-fisico-PPE
description: Activa anualmente (o por solicitud del Revisor Fiscal) para la toma física de propiedad, planta y equipo. Concilia existencia física vs maestro de activos, trata faltantes (baja con investigación) y sobrantes (alta a investigar) y verifica etiquetado.
agente: RITORE-AuxiliarActivosFijos-Senior
categoria: operativo
---

# Skill: realizar-inventario-fisico-PPE

## Para qué existe
El maestro de activos solo es confiable si se confronta periódicamente con la realidad física. Sin toma física, los faltantes se acumulan en libros (activos fantasma) y los sobrantes operan sin control ni seguro.

## Cuándo se activa
- Cron anual (programado en el plan de cierre, idealmente octubre-noviembre para alcanzar a ajustar antes del cierre).
- Solicitud del Revisor Fiscal, del cliente o del Orquestador.
- Alta rotación de sedes/responsables del cliente (indicio de pérdida de control).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Maestro de activos por sede/responsable con códigos de etiqueta | Módulo de activos | Sin maestro NO hay conteo útil: escalar a Orquestador antes de programar |
| Cronograma y responsables de conteo del cliente | Cliente | Proponer cronograma; si el cliente no confirma en 24 h hábiles, reiterar 1 vez y escalar |
| Planillas de conteo diligenciadas | Equipo de conteo del cliente | Reiterar 1 vez; sin planillas el inventario queda `incompleto` y se reporta así |

## Procedimiento
1. Preparar planillas de conteo por sede/responsable desde el maestro (código, descripción, ubicación esperada) — sin valores en libros, para no sesgar el conteo.
2. Coordinar la toma física con el cliente; exigir doble verificación en activos de valor ≥ 50 UVT.
3. Recibir planillas y cruzar contra el maestro: existencias confirmadas, faltantes, sobrantes, activos sin etiqueta y activos en mal estado.
4. Faltantes: solicitar investigación al responsable de custodia (plazo 5 días hábiles); confirmado el faltante, disparar `gestionar-baja-PPE` con el acta de investigación.
5. Sobrantes: investigar origen (compra no capitalizada, traslado no registrado, comodato de tercero); si es activo propio no registrado, alta vía `gestionar-ciclo-PPE` variante A con avalúo o costo documentado.
6. Activos en mal estado u ociosos: reportar como indicio a `evaluar-deterioro-NIC-36`.
7. Emitir informe de toma física: % conciliado, listado de diferencias con valor en libros, ajustes propuestos y re-etiquetados realizados.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Informe de toma física | Cubre el 100 % de los activos del maestro; cada diferencia tiene valor en libros y acción propuesta |
| Actas de faltantes/sobrantes | Firmadas por el responsable de custodia |
| Disparos a skills conexas (baja, alta, deterioro) | Cada diferencia confirmada tiene su skill destino registrada en el bus |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Activos sin etiqueta física (no identificables en conteo) | Altas antiguas sin etiquetar | Identificar por factura/serie y re-etiquetar durante la toma | Listarlos como `no identificados` en el informe y programar re-etiquetado con plazo |
| Cliente reporta 100 % conciliado en tiempo récord | Conteo "de escritorio" (copiaron el maestro) | Solicitar evidencia muestral (fotos con etiqueta visible) de ≥ 10 % de los ítems | Marcar la toma como `no confiable`, repetir conteo muestral propio y alertar al Orquestador |
| Faltante atribuido a traslado entre sedes sin documento | Traslados informales | Verificar existencia física en la sede destino | Si no aparece en destino, tratar como faltante real y abrir investigación |

## Escalamiento
- Faltantes acumulados ≥ 0,5 % del valor en libros total de PPE o un faltante individual ≥ 50 UVT → EspecialistaNIIF + alerta al Orquestador.
- Faltantes acumulados ≥ 500 UVT → Contador Titular (posible hecho relevante para dictamen).
- Indicio de apropiación indebida por empleado del cliente → Contador Titular, quien decide comunicación al cliente; nunca comunicar directamente la sospecha.

## Reglas críticas
🚫 NUNCA entregar planillas de conteo con valores en libros visibles (sesga el conteo).
🚫 NUNCA ajustar el maestro "para que cuadre" sin acta de investigación de la diferencia.
✅ SIEMPRE verificar etiquetado físico y re-etiquetar durante la misma toma.

## Métricas
- Cobertura de la toma física: 100 % de los activos del maestro, 1 vez al año.
- Tasa de conciliación física-libros: ≥ 98 % en valor (medición anual).
- Diferencias resueltas (baja/alta/explicación) antes del cierre anual: 100 %.

## Tests
### Test 1 — (normal) Toma anual: 240 activos, 235 confirmados, 3 faltantes menores ($400.000 c/u), 2 sobrantes (comodato de un proveedor)
**Output:** informe con 97,9 % de conciliación en ítems; faltantes < 1 UVT cada uno pero suma documentada e investigada por acumulación; sobrantes identificados como bienes de terceros → NO se capitalizan, se registran en control de bienes de terceros; cero disparos de deterioro.
### Test 2 — (excepción) Cliente devuelve planillas el mismo día reportando 100 % sin novedades
**Output:** solicitud de evidencia muestral fotográfica del 10 %; el cliente no la entrega; toma marcada `no confiable`, conteo muestral propio sobre 20 activos detecta 2 faltantes; alerta al Orquestador y reprogramación de toma completa supervisada.

═══════════════════════════════════════════════════════════════════════

---
name: reclasificar-PPE-vs-Inventario-vs-Propiedad-Inversion
description: Activa cuando un activo cambia de uso — PPE de uso propio pasa a venderse en el giro ordinario (inventario), a arrendarse/valorizarse (propiedad de inversión NIC 40) o viceversa. Determina la fecha del cambio de uso, la medición en la transferencia y los efectos en depreciación y revelaciones.
agente: RITORE-AuxiliarActivosFijos-Senior
categoria: operativo
---

# Skill: reclasificar-PPE-vs-Inventario-vs-Propiedad-Inversion

## Para qué existe
La clasificación determina la norma de medición (NIC 16 vs NIC 2 vs NIC 40) y por tanto el valor del activo, su depreciación y su presentación. Una reclasificación omitida o mal fechada distorsiona EEFF y la conciliación fiscal.

## Cuándo se activa
- Evidencia de cambio de uso: inmueble propio se arrienda a terceros, flota propia se pone a la venta como mercancía, inventario inmobiliario se destina a renta.
- Detección en cierre: ingresos por arrendamiento de un bien clasificado como PPE.
- Solicitud de EspecialistaNIIF.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Evidencia del cambio de uso (contrato de arrendamiento, decisión de venta documentada, inicio de desarrollo para venta) | Cliente | Sin evidencia NO se reclasifica; documentar el indicio y esperar 24 h hábiles, luego Orquestador |
| Ficha del activo con saldos al día | Maestro de activos | Caché con marca `[DATO EN CACHÉ — verificar]` |
| Valor razonable a la fecha del cambio (si destino u origen es PI a valor razonable) | Avalúo / cliente | Solicitar avalúo; mientras llega, reclasificar al valor en libros con marca `[PENDIENTE AVALÚO]` solo si el marco lo permite (modelo costo) |

## Procedimiento
1. Confirmar el cambio de uso con evidencia (no la intención: el hecho — inicio de arrendamiento, inicio de desarrollo para venta, inicio de uso propio).
2. Fijar la fecha de reclasificación = fecha del cambio de uso, no la fecha en que se detectó.
3. Determinar la matriz de medición en la transferencia:
   - PPE → Inventario: trasladar al valor en libros; deja de depreciarse desde la fecha.
   - PPE → PI modelo costo (o PYMES sin VR fiable): continúa al costo, cambia presentación.
   - PPE → PI modelo valor razonable (Plenas): medir a VR a la fecha; diferencia contra libros se trata como revaluación NIC 16 hasta esa fecha (ORI si positiva).
   - PI a VR → PPE o Inventario: el VR a la fecha del cambio es el costo atribuido en adelante.
   - Inventario → PI a VR: diferencia VR vs libros va a resultados.
4. Correr depreciación hasta la fecha de reclasificación y suspenderla o reiniciarla según el destino.
5. Asiento de reclasificación vía AuxContable; actualizar maestro y, si el destino es inventario, notificar a AuxiliarInventarios para el alta en kardex.
6. Marcar efectos fiscales: la reclasificación contable NO cambia el costo fiscal ni la depreciación fiscal del Art. 137 ET → documentar diferencias para impuesto diferido.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Asiento de reclasificación | Fechado en el cambio de uso; medición conforme a la matriz del paso 3 |
| Ficha actualizada (o traslado a kardex) | El activo existe en UN solo módulo destino; sin duplicados |
| Nota de efectos fiscales | Diferencias contable-fiscales de la transferencia documentadas para la variante D del ciclo PPE |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Cambio de uso detectado meses después (ingresos de arrendamiento sobre un PPE) | Cliente no informó | Reclasificar con fecha real del cambio y recalcular depreciación del periodo intermedio | Si afecta ejercicios cerrados, escalar a EspecialistaNIIF para evaluar corrección NIC 8 |
| Activo queda duplicado en maestro PPE y kardex | Traslado a inventario sin baja en módulo origen | Eliminar del módulo origen con referencia cruzada al destino | Congelar ambos registros con marca `[DUPLICADO EN REVISIÓN]` y resolver antes del cierre |
| Uso mixto del inmueble (parte propia, parte arrendada) | Realidad operativa del cliente | Separar por porciones si son vendibles/arrendables por separado; si no, clasificar por uso predominante y documentar | Escalar el criterio a EspecialistaNIIF con la medición de ambas alternativas |

## Escalamiento
- Efecto de la reclasificación en resultados u ORI ≥ 50 UVT → EspecialistaNIIF antes de asentar.
- Efecto ≥ 500 UVT o corrección de ejercicios anteriores → Contador Titular.
- Reclasificaciones repetidas del mismo activo (≥ 2 en 12 meses) → EspecialistaNIIF (posible gestión de resultados).

## Reglas críticas
🚫 NUNCA reclasificar por intención: solo por cambio de uso evidenciado.
🚫 NUNCA mantener el mismo activo activo en dos módulos (PPE y kardex) tras la transferencia.
✅ SIEMPRE fechar la reclasificación en el cambio de uso real, aunque la detección sea posterior.

## Métricas
- Reclasificaciones asentadas dentro del mes del cambio de uso: ≥ 90 % (medición trimestral).
- Activos duplicados entre módulos tras reclasificación: 0.

## Tests
### Test 1 — (normal) Constructora termina un edificio para uso administrativo y decide arrendarlo completo; política PI a valor razonable
**Output:** reclasificación PPE → PI en la fecha del primer contrato de arrendamiento; medición a VR con avalúo; diferencia positiva VR vs libros tratada como revaluación (ORI); depreciación suspendida en adelante (modelo VR no deprecia); nota fiscal: la depreciación fiscal Art. 137 continúa → diferencia temporaria.
### Test 2 — (excepción) En el cierre aparecen ingresos de arrendamiento desde marzo sobre una bodega clasificada como PPE; estamos en noviembre
**Output:** reclasificación fechada en marzo (no en noviembre), recálculo de los 8 meses intermedios, evaluación de materialidad del efecto; como el efecto supera 50 UVT, escalamiento a EspecialistaNIIF antes de asentar y nota al cliente pidiendo informar cambios de uso oportunamente.

═══════════════════════════════════════════════════════════════════════

---
name: aplicar-NIC-40-propiedad-de-inversion
description: Activa cuando un inmueble se destina a obtener rentas, plusvalía o ambas (no a uso propio ni a venta en el giro ordinario). Aplica NIC 40 (Plenas, modelo costo o valor razonable) o Sección 16 PYMES (valor razonable si es medible con fiabilidad sin costo desproporcionado).
agente: RITORE-AuxiliarActivosFijos-Senior
categoria: operativo
---

# Skill: aplicar-NIC-40-propiedad-de-inversion

## Para qué existe
Las propiedades de inversión tienen medición y presentación propias: bajo valor razonable no se deprecian y sus cambios de valor van a resultados. Tratarlas como PPE distorsiona resultados, EEFF y la conciliación fiscal.

## Cuándo se activa
- Adquisición de un inmueble destinado a renta o plusvalía.
- `reclasificar-PPE-vs-Inventario-vs-Propiedad-Inversion` transfiere un activo hacia PI.
- Cierre anual: actualización del valor razonable de la cartera de PI existente.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Destino del inmueble documentado (contratos de arrendamiento, decisión de inversión) | Cliente | Clasificar provisionalmente como PPE con marca `[CLASIFICACIÓN PENDIENTE]` y reiterar solicitud 1 vez en 24 h hábiles |
| Política del cliente (modelo costo o VR) y marco (Plenas/PYMES) | `cargar-perfil-cliente` | Solicitar a NotionArquitecto; sin política definida, escalar a EspecialistaNIIF para fijarla (nunca elegirla yo) |
| Avalúo técnico vigente (modelo VR) — antigüedad máx. 12 meses | Cliente / avaluador | Reiterar 1 vez; si no llega, mantener último VR con marca `[AVALÚO VENCIDO]` y escalar a EspecialistaNIIF |

## Procedimiento
1. Validar elegibilidad: el inmueble genera rentas o plusvalía y NO es de uso propio ni inventario inmobiliario. Uso mixto: separar porciones o clasificar por uso predominante (documentar criterio).
2. Reconocimiento inicial al costo (precio + costos de transacción directamente atribuibles).
3. Medición posterior según política:
   - **Modelo costo:** depreciar como PPE (componentes, vida útil) y revelar el valor razonable en notas.
   - **Modelo valor razonable (Plenas) / Sección 16 (PYMES con VR fiable):** actualizar VR cada cierre anual con avalúo; cambios de VR a resultados; sin depreciación.
4. Efecto fiscal: fiscalmente el inmueble sigue las reglas de costo y depreciación del ET (Art. 69 y 137); los ajustes de VR contables NO tienen efecto fiscal → diferencia temporaria, documentar para impuesto diferido.
5. Registrar en el módulo de activos con clase `propiedad_inversion`; asiento vía AuxContable.
6. Notificar a EspecialistaNIIF (medición y revelaciones de VR: jerarquía, avaluador, supuestos) y a EspecialistaRenta (depreciación fiscal que continúa).

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Ficha PI con modelo de medición y avalúo referenciado | Avalúo con antigüedad ≤ 12 meses si modelo VR |
| Asiento de reconocimiento o de ajuste de VR | Ajuste de VR a resultados (nunca a ORI bajo NIC 40) |
| Nota de impuesto diferido | Diferencia base contable VR vs base fiscal costo cuantificada por inmueble |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Avalúo con variación > 20 % anual sin cambio de mercado que lo explique | Avalúo de baja calidad o presión del cliente | Pedir sustento al avaluador (comparables, método) | No asentar el ajuste; escalar a EspecialistaNIIF con ambos valores |
| PYMES alega "costo desproporcionado" para no medir a VR un inmueble con mercado activo | Preferencia por evitar volatilidad | Verificar si existen referencias de mercado razonables | Escalar el criterio a EspecialistaNIIF; documentar la decisión en la política |
| Ajuste de VR llevado a ORI | Confusión con revaluación NIC 16 | Corregir: bajo NIC 40 los cambios de VR van a resultados | Si ya se publicaron EEFF, escalar a EspecialistaNIIF para reexpresión |

## Escalamiento
- Ajuste anual de VR ≥ 50 UVT → revisión de EspecialistaNIIF antes de asentar.
- Ajuste ≥ 500 UVT o cambio de modelo de medición (costo↔VR) → Contador Titular (cambio de política contable).
- Sospecha de avalúo inflado para apalancar crédito → Contador Titular + nota a SAGRLAFT.

## Reglas críticas
🚫 NUNCA depreciar una PI medida a valor razonable.
🚫 NUNCA llevar ajustes de VR de PI a ORI (eso es revaluación NIC 16, no NIC 40).
✅ SIEMPRE documentar la diferencia temporaria VR contable vs costo fiscal por inmueble.

## Métricas
- PI bajo modelo VR con avalúo ≤ 12 meses al cierre: 100 %.
- Diferencias temporarias de PI documentadas en el papel de impuesto diferido: 100 % (medición anual).

## Tests
### Test 1 — (normal) Cliente Grupo 1 compra oficina por $500M + gastos notariales $8M para arrendar; política VR
**Output:** reconocimiento inicial $508M; al cierre, avalúo $530M → ajuste +$22M a resultados; sin depreciación contable; depreciación fiscal 2,22 % anual continúa → diferencia temporaria documentada; revelaciones de VR notificadas a EspecialistaNIIF.
### Test 2 — (excepción) Avalúo llega con incremento del 35 % en un año, sin hechos de mercado que lo expliquen
**Output:** ajuste NO asentado; solicitud de sustento al avaluador (comparables y método); ante respuesta insuficiente, escalamiento a EspecialistaNIIF con el avalúo anterior y el nuevo; el cierre usa el último VR confiable con marca `[VR EN DISPUTA]`.

═══════════════════════════════════════════════════════════════════════

---
name: registrar-intangible-NIC-38-Seccion-18
description: Activa al adquirir o desarrollar intangibles — software, licencias, marcas, patentes, derechos. Aplica NIC 38 (Plenas) o Sección 18 (PYMES), distingue investigación (gasto) de desarrollo (capitalizable solo en Plenas con los 6 criterios) y gestiona amortización contable y fiscal (Arts. 142-143 ET).
agente: RITORE-AuxiliarActivosFijos-Senior
categoria: operativo
---

# Skill: registrar-intangible-NIC-38-Seccion-18

## Para qué existe
Los intangibles tienen reglas de reconocimiento más estrictas que la PPE: sin identificabilidad, control y beneficios futuros demostrables, lo pagado es gasto. Capitalizar mal infla activos; expensar mal castiga resultados y pierde amortización fiscal.

## Cuándo se activa
- Factura de adquisición de software, licencias, marcas, patentes o derechos.
- Proyecto interno de desarrollo (software propio, fórmulas, plataformas).
- Combinación de negocios con intangibles identificables (en coordinación con EspecialistaNIIF).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Contrato/factura con alcance de los derechos adquiridos (licencia perpetua vs suscripción) | Cliente / AuxContable | Suspender reconocimiento; reiterar 1 vez en 24 h hábiles; una suscripción SaaS sin control del software es gasto, no activo |
| Para desarrollo interno: bitácora del proyecto con fases y costos separados investigación/desarrollo | Cliente | Sin separación de fases, TODO el costo es gasto (regla NIC 38); informar al cliente |
| Marco del cliente | `cargar-perfil-cliente` | Solicitar; PYMES Sección 18: investigación Y desarrollo van a gasto siempre |

## Procedimiento
1. Test de reconocimiento: ¿es identificable (separable o surge de derechos)? ¿el cliente lo controla? ¿generará beneficios económicos? Si falla alguno → gasto.
2. Clasificar el origen: adquisición separada (capitaliza al costo), desarrollo interno (paso 3), generado internamente tipo marcas/clientela (NUNCA capitaliza).
3. Desarrollo interno — solo Plenas: fase de investigación a gasto; fase de desarrollo capitaliza únicamente si cumplen los 6 criterios de NIC 38.57 (viabilidad técnica, intención, capacidad de uso/venta, beneficios probables, recursos disponibles, medición fiable de costos). PYMES (Sección 18): todo I+D a gasto.
4. Determinar vida útil: definida → amortizar (línea recta salvo patrón distinto demostrable); indefinida (solo Plenas) → no amortizar + test de deterioro anual vía `evaluar-deterioro-NIC-36`.
5. Amortización fiscal: Art. 143 ET (en general, alícuotas que no excedan 20 % anual del costo fiscal; software y demás intangibles adquiridos según Art. 142). Marcar diferencias contable-fiscal para impuesto diferido.
6. Registrar en módulo de activos clase `intangible`; asiento vía AuxContable; notificar EspecialistaNIIF y EspecialistaRenta.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Memoria del test de reconocimiento | Las 3 condiciones (identificabilidad, control, beneficios) evaluadas explícitamente |
| Ficha del intangible con vida útil y plan de amortización dual | Vida útil contable y tope fiscal 20 % anual como campos separados |
| Asiento + marca de diferencia temporaria | Si amortización contable ≠ fiscal, diferencia cuantificada |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Suscripción SaaS capitalizada como software | Confusión licencia perpetua vs derecho de uso temporal sin control | Reclasificar a gasto (o activo por derecho de uso si aplica arrendamiento) | Escalar a EspecialistaNIIF con el contrato |
| Costos de desarrollo sin bitácora que separe fases | Cliente no llevó control del proyecto | Informar que sin separación todo es gasto; ofrecer estructura de bitácora para futuro | Expensar todo y documentar la causa; no reconstruir fases retroactivamente "de memoria" |
| Marca propia registrada que el cliente quiere activar por avalúo | Marcas generadas internamente no se capitalizan (NIC 38.63) | Explicar la prohibición; el costo de registro legal sí puede capitalizarse (menor) | Negativa documentada; escalar a EspecialistaNIIF si el cliente insiste |

## Escalamiento
- Capitalización de desarrollo interno ≥ 50 UVT → validación de EspecialistaNIIF de los 6 criterios antes de asentar.
- Intangible individual ≥ 500 UVT o vida útil indefinida propuesta → Contador Titular.
- Diferencia amortización contable vs fiscal ≥ 1 UVT o ≥ 0,5 % del rubro → documentar para impuesto diferido antes de cerrar.

## Reglas críticas
🚫 NUNCA capitalizar marcas, clientela o plusvalía generadas internamente.
🚫 NUNCA capitalizar desarrollo en clientes PYMES (Sección 18 manda todo I+D a gasto).
✅ SIEMPRE separar la amortización contable del tope fiscal del 20 % anual (Art. 143 ET).

## Métricas
- Intangibles con memoria de test de reconocimiento: 100 %.
- Amortización mensual corrida sin excepciones en cierres: 100 % (medición mensual).

## Tests
### Test 1 — (normal) Compra de licencia perpetua de ERP por $40M, cliente Plenas, vida útil contable 8 años
**Output:** capitalización $40M; amortización contable 12,5 % anual vs tope fiscal 20 % → el fiscal puede ir más rápido: diferencia temporaria documentada; ficha con plan dual; IVA descontable validado.
### Test 2 — (excepción) Cliente PYMES desarrolló internamente una app ($25M en salarios de desarrolladores) y pide activarla
**Output:** reconocimiento NEGADO por Sección 18 (PYMES expensa todo I+D); $25M permanecen en gasto; explicación al cliente documentada con la referencia normativa; nota a EspecialistaRenta sobre el tratamiento fiscal de los gastos; sin asiento de activación.

═══════════════════════════════════════════════════════════════════════

---
name: valorizar-revaluacion-NIC-16
description: Activa periódicamente para clientes Grupo 1 (NIIF Plenas) con política de revaluación de PPE. Ajusta el activo a valor razonable contra superávit por revaluación (ORI), recalcula la depreciación sobre el valor revaluado y documenta el impuesto diferido del superávit.
agente: RITORE-AuxiliarActivosFijos-Senior
categoria: operativo
---

# Skill: valorizar-revaluacion-NIC-16

## Para qué existe
Bajo el modelo de revaluación, el valor en libros debe mantenerse cercano al valor razonable. Sin revaluaciones oportunas el modelo se incumple; sin disciplina en el ORI, las valorizaciones terminan inflando resultados.

## Cuándo se activa
- Cron según la política del cliente (típicamente cada 3 años, o anual si el mercado es volátil).
- Variación de mercado que haga que el valor en libros difiera materialmente (≥ 10 %) del valor razonable.
- Solicitud de EspecialistaNIIF o del Revisor Fiscal.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Política de revaluación (clase de activos, frecuencia) | `cargar-perfil-cliente` | Sin política de revaluación vigente, esta skill NO aplica: confirmar con EspecialistaNIIF y cerrar |
| Avalúo técnico de la clase completa de activos | Avaluador independiente vía cliente | Reiterar 1 vez en 24 h hábiles; sin avalúo no hay revaluación: escalar a Orquestador si bloquea el cierre |
| Saldos del activo: costo, depreciación acumulada, superávit previo en ORI | Maestro de activos | Caché con marca `[DATO EN CACHÉ — verificar]` |

## Procedimiento
1. Verificar que la revaluación cubre la CLASE completa de activos (no activos individuales seleccionados a conveniencia).
2. Por activo: comparar valor razonable del avalúo vs valor en libros neto.
3. Aplicar la asimetría del ORI:
   - Incremento → ORI (superávit por revaluación), salvo que revierta una desvalorización previa reconocida en resultados (esa porción va a resultados).
   - Disminución → resultados, salvo que exista superávit previo de ESE activo en ORI (consume primero el ORI).
4. Ajustar la depreciación acumulada (método de reexpresión proporcional o de eliminación contra el costo bruto, según política).
5. Recalcular la depreciación futura sobre el valor revaluado y la vida útil remanente.
6. Impuesto diferido: la revaluación NO tiene efecto fiscal (el costo fiscal del Art. 69 ET no incluye revaluaciones contables) → reconocer pasivo por impuesto diferido contra ORI. Notificar a EspecialistaNIIF.
7. Documentar transferencia del superávit a utilidades retenidas por la porción realizada vía depreciación o baja (nunca por resultados).

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Papel de revaluación por activo | Asimetría ORI/resultados aplicada activo por activo (no neteo entre activos) |
| Asientos de ajuste + impuesto diferido contra ORI | El superávit en ORI queda neto de impuesto diferido |
| Nueva base de depreciación | Cuota futura recalculada sobre valor revaluado y vida remanente |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Avalúo cubre solo los activos que se valorizan (omite los que caen) | Selección a conveniencia ("cherry picking") | Exigir avalúo de la clase completa | No asentar revaluación parcial; escalar a EspecialistaNIIF y al Revisor Fiscal si hay presión del cliente |
| Desvalorización neteada contra superávit de OTRO activo | Manejo del ORI por bolsa común | Rehacer el cálculo activo por activo | Escalar a EspecialistaNIIF con el detalle por activo |
| Superávit transferido a resultados al dar de baja el activo | Confusión con reciclaje de ORI | Corregir: la transferencia es ORI → utilidades retenidas | Si ya está en EEFF publicados, escalar a EspecialistaNIIF para corrección |

## Escalamiento
- Ajuste neto de revaluación de la clase ≥ 50 UVT → EspecialistaNIIF antes de asentar.
- Ajuste ≥ 500 UVT o adopción/abandono del modelo de revaluación → Contador Titular (cambio de política).
- Avalúos con indicios de complacencia (incrementos sin sustento de mercado) → Contador Titular + Revisor Fiscal.

## Reglas críticas
🚫 NUNCA revaluar activos individuales: siempre la clase completa.
🚫 NUNCA netear incrementos y disminuciones entre activos distintos en el ORI.
✅ SIEMPRE reconocer el impuesto diferido del superávit contra ORI (la revaluación no tiene efecto fiscal, Art. 69 ET).

## Métricas
- Clases bajo modelo revaluación con avalúo dentro de la frecuencia de política: 100 %.
- Superávit en ORI conciliado activo por activo al cierre: 100 % (medición anual).

## Tests
### Test 1 — (normal) Revaluación trienal de la clase "terrenos y edificios": edificio con libros $900M, avalúo $1.080M, sin desvalorizaciones previas
**Output:** incremento $180M a ORI; pasivo por impuesto diferido sobre $180M contra ORI; depreciación futura sobre $1.080M y vida remanente; papel por activo; nota de que el costo fiscal permanece sin cambio (Art. 69 ET).
### Test 2 — (excepción) En la misma clase, una bodega cae $60M y el cliente pide netearlo contra el superávit del edificio
**Output:** neteo RECHAZADO; la bodega no tiene superávit previo propio → los $60M van a resultados; el superávit del edificio queda intacto en ORI; criterio documentado (NIC 16.40) y notificado a EspecialistaNIIF; como el efecto en resultados supera 50 UVT, validación del Master antes de asentar.

═══════════════════════════════════════════════════════════════════════

## Relacionado
- *MOC - Agentes RITORE*
- *Proyecto - Ecosistema RITORE*
- [[00 - Estandar de Agentes RITORE]]
- [[Skills Compartidas RITORE]]
- *11-EspecialistaIVA-Master*
- *13-EspecialistaRenta-Senior*
- *15-EspecialistaNIIF-Senior*

## Historial de versiones
| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-05-19 | Versión inicial consolidada (11 skills) | RITORE |
| 2.0 | 2026-06-11 | Reescritura según Estandar de Agentes v1.0: deduplicación de skills (11 → 8; ciclo ordinario consolidado en `gestionar-ciclo-PPE` con 4 variantes), inputs/outputs, umbrales numéricos, manejo de errores | RITORE |
