---
tipo: skill
tags: [ritore, skill, auditoria, cierre, ajustes, conciliacion, hoja-unica]
estado: activo
version: 1.0
fecha: 2026-10-19
---

# 🧾 Skill — Auditoría de Cierre y Ajuste Contable

> Norma vinculante para TODA auditoría de cierre (mensual, trimestral, semestral o anual) que se haga en la firma. Nace de una lección cara: en COMERCIO DE BICICLETAS A, el cierre de enero a junio de 2026 se entregó como diagnóstico y hubo que volver a intervenir una y otra vez (V2, V3, V4, V5) porque el entregable nunca garantizó que, digitado completo, dejara la contabilidad cuadrada. **Esta skill existe para que eso no vuelva a pasar.**

Comportamientos comunes heredados de [[Skills Compartidas RITORE]] (cargar perfil de cliente, verificar vigencia normativa, escalar a humano, documentar decisión no trivial); no se re-copian aquí.

## Para qué existe

Un diagnóstico no es una auditoría de cierre. El auxiliar no puede digitar un hallazgo: digita asientos. Esta skill obliga a que todo trabajo de auditoría termine en **un plan de asientos ejecutable, en una sola hoja, mes a mes, con prueba aritmética de que al digitarlo la contabilidad queda ajustada y conciliada**.

La regla de oro, y es la que se incumplió:

> **GARANTÍA DE CIERRE — Al terminar de digitar todos los asientos del plan, y sin ninguna decisión adicional del auxiliar, la contabilidad debe quedar: cartera conciliada, bancos conciliados contra extracto, impuestos cerrados contra las declaraciones y el balance cuadrado. Mes a mes, no solo a la fecha de corte. Si el entregable no lo garantiza y no lo demuestra con números, el trabajo NO está terminado.**

## Cuándo se activa

- Siempre que se pida una auditoría, una revisión de cierre, un programa de ajustes, una conciliación de período o unos EEFF que exijan ajustes previos.
- Siempre que se vaya a emitir un juego de estados financieros: la skill corre ANTES, no después.
- Cuando un cierre ya entregado requiera una segunda versión. **Una segunda versión es una señal de que esta skill no se aplicó.** Registrar en [[Registro de Errores Recurrentes]].

## Inputs

| Insumo | Origen | Obligatorio | Si falta |
|---|---|---|---|
| Libro auxiliar del período completo, con tercero y centro de costo | Software contable | Sí | No se arranca |
| Balance de prueba del mismo corte | Software contable | Sí | No se arranca |
| Saldos de apertura del período | Software contable | Sí | No se arranca |
| Extractos bancarios de TODAS las cuentas, TODOS los meses | Bancos | Sí | El frente de bancos queda abierto y se dice |
| Token DIAN del período (emitidas, recibidas, nómina electrónica, DSEL) | Portal DIAN | Sí | El frente de ingresos queda abierto y se dice |
| Declaraciones presentadas del período + acuses + comprobantes de pago | Carpeta del cliente | Sí | El frente de impuestos queda abierto y se dice |
| Criterios particulares del cliente | Ficha `Cliente - X.md` | Sí | Nunca se hardcodean aquí (§3 del estándar) |
| Soportes de terceros (pasarelas, franquicias, liquidaciones) | Cliente / portales | Según hallazgos | Se pide por escrito y queda como pendiente |

**El auxiliar y el balance de prueba deben coincidir antes de empezar.** Si no coinciden, se devuelve al cliente: no se audita sobre datos que no cuadran entre sí.

## Procedimiento

### Fase 0 — Encuadre
1. Fijar el período y los cortes intermedios. **Los cortes son todos los meses del período, no solo el último.**
2. Normalizar auxiliar, balance, apertura, extractos y token a CSV en el scratchpad. Verificar que auxiliar y balance coincidan cuenta por cuenta.
3. Fijar materialidad con los umbrales estándar del ecosistema: material ≥ 1 UVT o ≥ 0,5 % del total; crítico ≥ 50 UVT; mayor ≥ 500 UVT.

### Fase 1 — Las ocho áreas obligatorias, en paralelo y COMPLETAS
Se despliegan auditores simultáneos y se reparten las ocho áreas entre ellos (típicamente 4 agentes × 2 áreas). **Las ocho son obligatorias aunque el encargo mencione una sola: lo que nadie audita es exactamente donde aparece el ajuste olvidado.** Esta lista es la cobertura que ya se validó en terreno; no se recorta.

| # | Área | Alcance | Objetivo de cierre |
|---|---|---|---|
| 1 | **Bancos y efectivo** | 11xx, una conciliación por cuenta y por mes, caja general y cajas menores | Libros = extracto al cierre de CADA mes; ninguna caja con saldo crédito |
| 2 | **Cartera y recaudos** | 13xx, pasarelas de crédito, franquicias de tarjetas, anticipos de clientes, cuentas por cobrar a socios | Cada saldo con respaldo documental y con tercero identificado |
| 3 | **Proveedores y cuentas por pagar** | 22xx, 23xx (salvo retenciones), pagos a proveedores | Saldos conciliados contra soportes; sin naturaleza contraria |
| 4 | **Impuestos** | 24xx, anticipos del 13xx, retención, autorretención, IVA, ICA, pagos a la DIAN | Saldo en libros = valor de la declaración, mes a mes |
| 5 | **Facturación y token DIAN** | Cruce documento por documento, ventas sin facturar, facturas sin causar, notas crédito | Cero diferencias entre token y contabilidad, o diferencias explicadas una a una |
| 6 | **Costos y gastos** | 5x, 6x, 7x, costo de ventas, gastos sin soporte, gastos personales de socios | Margen coherente; todo gasto con soporte y con tercero |
| 7 | **Nómina y pasivos laborales** | 25xx, seguridad social, provisiones, nómina electrónica | Causada, pagada y provisionada al día mes a mes |
| 8 | **Apertura, cierre anterior y patrimonio** | Saldos de apertura, arrastre del año anterior, 3x, cuentas plug | Apertura amarrada al cierre anterior; cero plugs vivos |

Y en todas: **buscar cuentas plug** (saldos de naturaleza contraria, partidas redondas grandes, comprobantes manuales de ajuste sin soporte, movimientos de fin de mes que cuadran algo). Es el hallazgo más repetido de la firma y el que más caro sale.

Reglas de método que aplican a todas las áreas:
- **Bancos: cuadre agregado POR SENTIDO mes a mes**, nunca emparejar movimientos individuales por valor exacto como prueba. El emparejamiento sirve para identificar partidas, no para concluir.
- **Token: cruce documento por documento, NUNCA por el agregado**, tolerancia ±200. Incluir TODAS las cuentas de ingreso.
- **Cartera: agotar los cruces uno-a-varios** antes de declarar una partida sin identificar (*Regla - Conciliacion con cruces 1-a-N*).
- **Retenciones: un asiento de cierre por cada F-350**, cancelando mes por mes; nunca un asiento acumulado del período.
- **NIIF 2.52: prohibido compensar** activo contra pasivo. Los saldos crédito en cartera se reclasifican al pasivo; los saldos a favor se llevan al activo.

### Fase 2 — Consolidación en la HOJA ÚNICA DE ASIENTOS
4. Todos los asientos de los cuatro frentes se consolidan en **una sola hoja**, ordenada por mes y numerada de forma continua. No se reparten los asientos entre hojas temáticas: el auxiliar trabaja sobre una sola.
5. Formato obligatorio de la hoja, una línea por renglón contable:

   `N° | MES | COMPROBANTE | FECHA | CUENTA | NOMBRE DE LA CUENTA | TERCERO | DÉBITO | CRÉDITO | QUÉ REGISTRA | SOPORTE`

6. **Cada comprobante cuadra por separado** y muestra su subtotal. **La hoja completa cuadra**: suma de débitos = suma de créditos.
7. Los asientos van **fechados dentro del mes al que corresponden**, para que cada mes cierre por sí solo.
8. Si un asiento depende de otro, se indica el orden y por qué. Si un grupo de asientos debe digitarse junto (típico en conciliación bancaria, donde el banco pasa por saldos transitorios), se marca como **bloque indivisible**.

### Fase 3 — LA PRUEBA DE CIERRE (es lo que hace válido el entregable)
9. Por cada mes y cada área, se demuestra con números:

   `saldo en libros hoy + débitos del plan − créditos del plan = saldo objetivo`

   donde el saldo objetivo es: el extracto bancario, el valor de la declaración, el soporte del tercero o el saldo depurado con respaldo. **La diferencia resultante debe ser CERO.** Si no da cero, el plan está incompleto y no se entrega.
10. Si algo NO puede quedar en cero por falta de información, se dice explícitamente: cuánto, por qué, qué documento falta, a quién se le pide y qué pasa si no llega. **Un hueco declarado es aceptable; un hueco silencioso no.**
11. Cuando falte el contrapartida de una salida real de banco, se usa una **cuenta puente nombrada y con fecha de cierre** (nunca un plug anónimo), y el asiento de cierre de esa cuenta queda en el plan marcado como PENDIENTE.

### Fase 4 — Pendientes y plan de acción
12. Todo lo que no se pueda resolver en el período se lleva a una lista de **PENDIENTES DEL MES SIGUIENTE**, con: número, asunto, valor, qué hay que hacer, ante quién, plazo y riesgo de no hacerlo.
13. **Las declaraciones no presentadas o mal presentadas quedan en esa lista**, con el procedimiento que aplique (corrección art. 588/589 ET, sanción mínima art. 639, extemporaneidad) y su costo estimado.
14. Plan de acción ordenado por materialidad, separando lo que desbloquea (los prerequisitos) de lo que depende.

### Fase 5 — Aprendizaje
15. Todo hallazgo repetible se registra como lección en [[Bitacora de Aprendizajes]]. A la 3ª ocurrencia se cambia esta skill o la skill de origen, no se vuelve a corregir a mano.

## Outputs y criterios de aceptación

Son **dos libros**, siempre, con esta estructura probada:

**Libro A — AUDITORÍA `<período> - <CLIENTE>.xlsx`** (el diagnóstico, una hoja por área)

`01 VEREDICTO · 02 QUÉ CAMBIÓ · 03 CUENTAS PLUG · 04 CAUSA RAÍZ · 05 PLAN DE ACCIÓN · 06 DOCUMENTOS QUE FALTAN · 07 BANCOS · 08 CARTERA Y RECAUDOS · 09 PROVEEDORES · 10 IMPUESTOS · 11 FACTURACIÓN Y TOKEN · 12 COSTOS Y GASTOS · 13 NÓMINA · 14 APERTURA Y CIERRE ANTERIOR · 15 RESULTADO · 16 PRUEBAS`

**Libro B — PROGRAMA DE AJUSTES `<período> - <CLIENTE>.xlsx`** (lo que se digita)

`01 INSTRUCCIONES · 02 ASIENTOS (hoja única) · 03 DECISIONES DEL CONTADOR · 04 SECUENCIA · 05 PENDIENTES · 06 CONTROLES DE SALIDA · 07 CÓMO QUEDA AL FINAL`

| Output | Criterio de aceptación |
|---|---|
| **`02 ASIENTOS` — hoja única** | UNA sola hoja con TODOS los asientos de todas las áreas; cada comprobante cuadra; la hoja cuadra; asientos fechados en su mes; columna de soporte diligenciada en todas las líneas |
| **`06 CONTROLES DE SALIDA` — prueba de cierre** | Por mes y por área: diferencia CERO, con la aritmética a la vista. Los huecos, si los hay, cuantificados y nombrados |
| **`07 CÓMO QUEDA AL FINAL`** | El balance resultante después de digitar todo: activo = pasivo + patrimonio, bancos = extracto, impuestos = declaración |
| **`04 SECUENCIA`** | El orden de digitación, marcando los bloques indivisibles |
| **`05 PENDIENTES`** | Numerada, con valor, qué hacer, ante quién, plazo y riesgo |
| **`03 DECISIONES DEL CONTADOR`** | Lo que requiere criterio humano, separado de lo que es mecánico |
| **Papeles de trabajo por área** | Cada cifra del plan es trazable a un papel de trabajo y de ahí al insumo |

**Aceptación global: el entregable se acepta solo si un auxiliar que no participó en la auditoría puede digitar la hoja `02 ASIENTOS` completa sin hacer una sola pregunta, y al terminar la contabilidad queda conciliada.** Si tiene que preguntar algo, falta ese dato en la hoja.

## Manejo de errores y fallback

| Error | Acción | Fallback |
|---|---|---|
| Auxiliar y balance de prueba no coinciden | No se audita. Se devuelve al cliente | Documentar el descuadre y escalar |
| Falta un extracto de un mes | Ese mes NO se declara conciliado. Se dice cuál falta | Conciliar los meses que sí se tienen y dejar el otro abierto |
| Salida de banco real sin contrapartida identificada | Cuenta puente nombrada + asiento de cierre pendiente | Nunca un plug anónimo ni dejar el banco descuadrado en silencio |
| El plan propone un ajuste que contradice una versión anterior | Decirlo expresamente y explicar qué cambió | Nunca corregir en silencio una conclusión previa |
| Un ajuste tocaría una declaración ya presentada | Cuantificar la corrección y su sanción; NO digitar sin aprobación del titular | Pendiente del mes siguiente con el procedimiento |
| El titular instruye una ruta contable distinta a la técnicamente ideal | Se ejecuta lo que instruye, se deja por escrito el supuesto y la consecuencia, y se entrega igual la ruta correcta | Nunca ejecutar en silencio ni negarse en silencio |

## Escalamiento

- Diferencia crítica ≥ 50 UVT → Master del dominio. Diferencia mayor ≥ 500 UVT → Contador Titular.
- Indicios de irregularidad (gastos personales del socio pagados por la empresa, plugs sin soporte, ingresos omitidos, cartera sin respaldo documental) → Contador Titular de inmediato y registro en la ficha del cliente. **Nunca normalizar en silencio.**
- Corrección de declaraciones, castigo de cartera contra resultados y firma: SIEMPRE humano.

## Reglas críticas

1. **Un diagnóstico sin plan de asientos ejecutable no es un entregable.** Se devuelve.
2. **Una sola hoja de asientos.** Los papeles de trabajo pueden ser muchos; la hoja que digita el auxiliar es una.
3. **Mes a mes, siempre.** Conciliar solo a la fecha de corte oculta errores que se compensan entre meses (caso real: un mes con salidas de más tapó 8,6 millones del descuadre del mes anterior).
4. **Los cuatro frentes son obligatorios**, aunque el encargo mencione solo uno. El ajuste que se escapa está siempre en el frente que nadie miró.
5. **La prueba de cierre va en el entregable**, no en la cabeza del auditor.
6. **Cuenta puente siempre con nombre y fecha de cierre.** Una cuenta puente que nadie cierra se convierte en el próximo saldo sin explicar.
7. **Lo no presentado se nombra.** Declaraciones pendientes, correcciones y sanciones van en la lista del mes siguiente con su valor.
8. **Nunca se inventa una cifra.** Si no se puede probar con los insumos, se dice que no se puede probar.
9. **Si una versión anterior se equivocó, se dice.** El entregable nuevo corrige expresamente lo que corrige.
10. Criterios de cliente solo desde su ficha; jamás hardcodeados aquí (§3 del estándar).

## Métricas

- **Versiones por cierre (la métrica que importa): meta 1.** Dos o más versiones del mismo cierre = fallo de esta skill, se investiga.
- Diferencia residual después de digitar el plan (meta: cero en todas las áreas y todos los meses).
- Preguntas del auxiliar al digitar (meta: cero).
- Pendientes que se cierran dentro del mes siguiente (meta ≥ 80 %).
- Hallazgos detectados ANTES de emitir EEFF vs. después (meta: 100 % antes).

## Tests

**Test 1 (caso normal):** Cliente con un trimestre cerrado, dos cuentas bancarias, IVA cuatrimestral y retención mensual. Resultado esperado: hoja única con los asientos de los tres meses, cada comprobante cuadrado, prueba de cierre en cero para bancos (ambas cuentas, los tres meses), cartera, impuestos y balance; lista de pendientes del mes siguiente; cero preguntas del auxiliar al digitar.

**Test 2 (caso borde):** Al conciliar aparece una salida real de banco de 400 UVT cuyo destinatario no se puede identificar con los insumos disponibles. Resultado esperado: NO se declara el banco conciliado en silencio ni se deja el descuadre; se registra la salida contra una cuenta puente nombrada ("traslados por identificar"), el banco SÍ queda conciliado contra el extracto, el asiento de cierre de la cuenta puente queda en el plan marcado como PENDIENTE con el documento que hace falta y a quién se le pide, y el hallazgo se escala al Contador Titular por superar las 50 UVT.

## Historial de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-10-19 | Creación. Nace de la lección del cierre enero-junio 2026 de un cliente de retail, donde el entregable de auditoría se limitó al diagnóstico y obligó a cuatro versiones sucesivas de ajustes. Establece la garantía de cierre, la hoja única de asientos, los cuatro frentes obligatorios, el corte mes a mes y la prueba de cierre con diferencia cero. |

## Relacionado

- *00 - Estandar de Skills RITORE*
- [[Skill - Bucle de Cierre Mensual de Cliente]]
- [[Skill - Presentar Retencion en la Fuente F350]]
- [[Skill - Presentar IVA Bimestral F300]]
- *Skill - Presentar ICA Municipal*
- *19-RevisorFiscal-Senior*
- [[02-AuxiliarContable-Senior]]
- [[03-AuxiliarConciliacionesBancarias-Senior]]
- [[05-AuxiliarCarteraCxP-Senior]]
- *11-EspecialistaIVA-Master*
- *12-EspecialistaRetenciones-Senior*
- *16-EstadosFinancieros-Senior*
- [[Registro de Errores Recurrentes]]
- [[Bitacora de Aprendizajes]]
