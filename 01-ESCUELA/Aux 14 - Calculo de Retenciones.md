---
tipo: leccion
tags: [ritore, escuela, auxiliar, retencion, impuestos]
modulo: 4
estado: vigente
fecha: 2026-06-08
---

# Aux 14 - Cálculo de Retenciones

## Objetivo

La lección más densa del programa. Que el auxiliar sepa, **al causar cada factura**, decidir: (1) si practica **retención en la fuente a título de renta** y a qué tarifa, (2) si practica **ReteIVA**, (3) si practica **ReteICA** (Medellín), (4) cómo opera la **autorretención especial** del Decreto 2201/2016, y (5) cómo registrar todo en las cuentas 2365/2367/2368 de modo que el auxiliar contable cuadre con el **F-350** mes a mes. La retención se decide en la causación: lo que se cause mal, se declara mal.

## Marco conceptual y normativo

Base normativa, cronología del **Decreto 0572 de 2025** y tabla completa verificada en *Proyecto - Retencion en la Fuente* (Arts. 365–419, 383, 392, 401, 437-1, 437-2 ET; DUR 1625/2016; D. 2201/2016).

### 1. Retención a título de renta — tabla operativa 2026 (UVT 2026 = $52.374)

Régimen vigente en **junio de 2026** (anterior al D. 0572 — ver alerta abajo):

| Concepto | Tarifa | Base mínima (UVT) | Base mínima ($) |
|---|---|---|---|
| Honorarios y comisiones — PJ y PN declarante | 11 % | 0 | $1 |
| Honorarios y comisiones — PN no declarante | 10 % | 0 | $1 |
| Servicios generales — declarante | 4 % | 4 | $209.496 |
| Servicios generales — no declarante | 6 % | 4 | $209.496 |
| Compras generales — declarante | 2,5 % | 27 | $1.414.098 |
| Compras generales — no declarante | 3,5 % | 27 | $1.414.098 |
| Productos agropecuarios sin procesamiento | 1,5 % | 92 | $4.818.408 |
| Servicios de hoteles, restaurantes y hospedaje | 3,5 % | 4 | $209.496 |
| Arrendamiento de bienes muebles | 4 % | 0 | $1 |
| Arrendamiento de bienes inmuebles | 3,5 % | 27 | $1.414.098 |
| Transporte de carga | 1 % | 4 | $209.496 |
| Rendimientos financieros | 7 % | 0 | $1 |
| Rentas de trabajo y Art. 383 | tabla progresiva (0 % hasta 95 UVT de base depurada) | — | — |

> ⚠️ **ALERTA D. 0572/2025:** el Consejo de Estado revocó la suspensión el 02-jun-2026; las tarifas y bases del D. 0572 **vuelven previsiblemente el 01-jul-2026**: compras 27 → **10 UVT** ($523.740), hoteles/restaurantes 4 → **2 UVT**, agropecuarios 92 → **70 UVT**, y autorretención por CIIU hasta **4,5 %**. La tarifa aplicable es la de la **fecha del pago o abono en cuenta**. `[VERIFICAR ejecutoria antes de reparametrizar]` — detalle en *Proyecto - Retencion en la Fuente*.

### 2. ReteIVA (Art. 437-1 y 437-2 ET)

- Tarifa: **15 % del IVA** facturado (100 % en servicios prestados desde el exterior).
- Se practica, en lo cotidiano, cuando un **gran contribuyente o entidad estatal** compra a un responsable de IVA del régimen ordinario; y cuando cualquier responsable contrata servicios gravados con **no residentes**.
- **No** se practica ReteIVA a grandes contribuyentes ni a entidades estatales.
- Cuenta: **2367** (impuesto a las ventas retenido).

### 3. ReteICA — Medellín

- Se retiene a la **tarifa de la actividad del proveedor** (en ‰), si la operación se grava en Medellín y supera la base mínima municipal.
- Rangos del estatuto tributario de Medellín: **industria 2–7 ‰ · comercio 2–10 ‰ · servicios 2–10 ‰ · sector financiero 5 ‰**. La tarifa exacta depende del código CIIU — consultar el [centro documental de la Alcaldía](https://www.medellin.gov.co/es/centro-documental/tarifas-de-liquidacion-del-impuesto-de-industria-y-comercio-ica/) `[VERIFICAR tarifa y base mínima vigentes por CIIU antes de parametrizar]`.
- En Medellín opera además la **autorretención de ICA** (100 % de la tarifa de la actividad) para los contribuyentes obligados.
- Cuenta: **2368** (impuesto de industria y comercio retenido). Se declara al **municipio** (bimestral en Medellín), NO en el F-350.

### 4. Autorretención especial de renta (D. 2201/2016, arts. 1.2.6.6–1.2.6.8 DUR)

- La practican las **sociedades nacionales contribuyentes exoneradas de aportes por el Art. 114-1 ET** (responsabilidad **15 en el RUT**) sobre sus **ingresos brutos** gravados.
- Tarifas hasta el 30-jun-2026 (previsible): **0,55 %** (comercio, servicios generales), **1,1 %** (manufactura, transporte de carga), **1,6 %** (energía, servicios profesionales). Desde la reactivación del D. 0572 (~01-jul-2026): por CIIU, **hasta 4,5 %**.
- Se declara y paga en el mismo **F-350** mensual.

### 5. LA MATRIZ CLAVE — ¿a quién se retiene? (decisión por tipo de proveedor)

Antes de causar, consultar el **RUT del proveedor** (responsabilidades) y aplicar:

| Tipo de proveedor (vendedor) | ¿Retención renta? | ¿ReteIVA? | ¿ReteICA? |
|---|---|---|---|
| Gran contribuyente (resp. 13) NO autorretenedor | SÍ, tarifa del concepto | **NO** (no se le practica) | Según municipio (salvo autorretenedor ICA) |
| Autorretenedor de renta (resp. 15 / resolución DIAN) | **NO** (él se autorretiene) | NO si además es GC | Según municipio |
| PJ régimen ordinario | SÍ | Solo si el comprador es GC o entidad estatal | SÍ, tarifa de su actividad |
| **Régimen Simple — RST (resp. 47)** | **NO** (Art. 911 ET) — salvo pagos **laborales** | SÍ puede aplicar sobre el IVA que facture | **NO** (el SIMPLE integra el ICA) |
| PN no responsable de IVA (compras/servicios) | SÍ, tarifa de no declarante si no declara renta | No hay IVA → no aplica | SÍ, si es contribuyente de ICA |
| **PN honorarios/servicios SIN 2+ trabajadores** | **Tabla Art. 383** (no la tarifa fija) | Según responsabilidad | SÍ |
| No residente / exterior | Retención de pagos al exterior (Arts. 406–419, tarifas propias) | 100 % del IVA teórico en servicios gravados | No aplica |

> El comprador también importa: una **PN no comerciante y no agente de retención** no practica retención de renta. Las PJ clientes de FYT son todas agentes de retención (Art. 368 ET).

## Paso a paso (con asientos)

**Caso 1 — Servicio de aseo, proveedor PJ declarante responsable de IVA, nuestro cliente es GC, Medellín.** Factura: $2.000.000 + IVA 19 % $380.000.

- Renta servicios 4 % (base $2.000.000 ≥ 4 UVT ✓) = $80.000
- ReteIVA 15 % × 380.000 (somos GC) = $57.000
- ReteICA servicios ej. 10 ‰ `[VERIFICAR CIIU]` = $20.000

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 513505 | Servicios — aseo y vigilancia | 2.000.000 | |
| 240810 | IVA descontable | 380.000 | |
| 236525 | Retención en la fuente — servicios | | 80.000 |
| 236701 | Impuesto a las ventas retenido (ReteIVA) | | 57.000 |
| 236801 | ReteICA Medellín | | 20.000 |
| 233525 | Costos y gastos por pagar | | 2.223.000 |
| **Sumas** | | **2.380.000** | **2.380.000** |

**Caso 2 — Honorarios a PN.** $3.000.000, contadora independiente que **no vincula 2+ trabajadores** → NO se aplica el 10/11 %: se aplica la **tabla Art. 383** sobre la base depurada. Depuración rápida: 3.000.000 − aportes obligatorios (cotiza sobre el 40 %: salud+pensión ≈ 96.000... según planilla) − 25 % exenta ≈ $2.105.000 < 95 UVT ($4.975.530) → **retención $0**. Si la misma PN tuviera 2+ trabajadores vinculados → tarifa fija 10 % (no declarante) = $300.000 u 11 % si es declarante.

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 511025 | Honorarios | 3.000.000 | |
| 233525 | Costos y gastos por pagar | | 3.000.000 |

**Caso 3 — Compra de mercancía a proveedor del RST (resp. 47).** $5.000.000 + IVA. **NO** se retiene renta (Art. 911 ET) ni ICA; el IVA sigue las reglas generales. Error frecuente: retenerle "por costumbre" — luego toca devolver o el proveedor reclama.

**Caso 4 — Autorretención especial del mes.** Cliente SAS de servicios (0,55 %), ingresos gravados de junio $100.000.000 → autorretención $550.000:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 135515 | Anticipo de impuestos — autorretención | 550.000 | |
| 236575 | Autorretenciones | | 550.000 |

**Caso 5 — Pago de la declaración F-350 (mes siguiente):**

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 236525 | Retención servicios | 80.000 | |
| 236575 | Autorretenciones | 550.000 | |
| 236701 | ReteIVA | 57.000 | |
| 111005 | Bancos — cuenta corriente | | 687.000 |

El ReteICA (2368) se paga aparte, al municipio de Medellín, con su propia declaración bimestral.

**Verificación mensual obligatoria (regla C.3 / proyecto):** por cada subcuenta, **crédito − débito de la 2365 por tercero = base del F-350**, excluyendo los traslados/cierres a nombre de la DIAN. El total del F-350 debe cuadrar con el movimiento contable del mes ANTES de presentar. Recordar el **Art. 580-1 ET**: F-350 presentado sin pago total es **ineficaz de pleno derecho**.

## Errores comunes (casos reales FYT)

1. **No consultar el RUT y retener a un RST o a un autorretenedor** — genera reclamos, notas y reprocesos. La matriz de decisión se aplica factura por factura.
2. **Aplicar tarifa fija a una PN de honorarios sin verificar el Art. 383** — la PN que no subcontrata tiene derecho a la tabla progresiva (casi siempre $0 en valores bajos). Caso típico en **Cliente - PERSONA NATURAL J (TALLER DE DISEÑO J)** como proveedor persona natural.
3. **Olvidar el cambio de régimen del D. 0572 en julio-2026:** seguir usando base de compras de 27 UVT cuando ya es 10 UVT → retenciones dejadas de practicar, que el agente retenedor **responde con su propio patrimonio** (Art. 370 ET).
4. **Mezclar ReteICA en el F-350** o declarar el 2368 a la DIAN — el ReteICA es municipal.
5. **Presentar el F-350 sin pago total** — ineficacia automática (Art. 580-1 ET), la más peligrosa del régimen; ver reglas y excepciones en *Proyecto - Retencion en la Fuente*.
6. **No excluir los cierres a nombre de la DIAN al cuadrar la 2365** — infla la base del F-350 y descuadra el cruce con exógena (F-1001 columna R / *Formato 1003 - Retenciones que le practicaron*).
7. **Retener sobre el total con IVA:** la base de la retención de renta es el valor **antes de IVA**.

## Checklist de calidad

- [ ] RUT del proveedor consultado: responsabilidades 13/15/47/48/49 identificadas.
- [ ] Concepto correcto (honorarios ≠ servicios ≠ compras) y base ≥ mínima en UVT del régimen vigente a la fecha de pago.
- [ ] Base de retención sin IVA; ReteIVA = 15 % del IVA solo cuando procede.
- [ ] ReteICA con la tarifa de la actividad del proveedor (‰) y a la cuenta 2368.
- [ ] Autorretención especial calculada sobre ingresos brutos del mes y causada (135515/236575).
- [ ] Cuadre mensual: crédito − débito 2365 por tercero = F-350 (sin cierres DIAN).
- [ ] F-350 presentado CON pago total y con 2 días hábiles de margen.
- [ ] Julio-2026: tarifas y bases reparametrizadas al D. 0572 `[VERIFICAR ejecutoria]`.

## Relacionado

- Anterior: [[Aux 13 - Nomina Electronica y Documento Soporte de Pago]] · Siguiente: [[Aux 15 - IVA y Prorrateo]]
- [[MOC - Escuela Auxiliar Contable]]
- *12-EspecialistaRetenciones-Senior* · [[02-AuxiliarContable-Senior]]
- *Proyecto - Retencion en la Fuente* · *Formato 1003 - Retenciones que le practicaron*
