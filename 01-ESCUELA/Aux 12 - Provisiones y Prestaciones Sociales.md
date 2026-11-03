---
tipo: leccion
tags: [ritore, escuela, auxiliar, nomina, prestaciones]
modulo: 3
estado: vigente
fecha: 2026-06-08
---

# Aux 12 - Provisiones y Prestaciones Sociales

## Objetivo

Que el auxiliar provisione cada mes las **prestaciones sociales** (cesantías, intereses, prima, vacaciones), cause la **seguridad social patronal** y los **parafiscales** aplicando correctamente la exoneración del Art. 114-1 ET, conozca el **calendario legal de pagos** y registre la diferencia entre provisionar y pagar. Sin provisión mensual, el gasto se concentra en junio y diciembre y los estados financieros intermedios mienten.

## Marco conceptual y normativo

**Porcentajes de provisión mensual (sobre la base de cada prestación):**

| Prestación | % mensual | Base | Norma |
|---|---|---|---|
| Cesantías | 8,33 % | salario + auxilio de transporte | Ley 50/1990, Art. 99 |
| Intereses a las cesantías | 12 % anual (1 % mensual) sobre el **saldo acumulado de cesantías** | cesantías acumuladas | Ley 52/1975 |
| Prima de servicios | 8,33 % | salario + auxilio de transporte | Art. 306 CST |
| Vacaciones | 4,17 % | salario **sin** auxilio de transporte | Art. 186 CST |

**Seguridad social y parafiscales a cargo del empleador (sobre el IBC):**

| Aporte | % patronal | Exonerable Art. 114-1 ET |
|---|---|---|
| Salud | 8,5 % | **Sí** |
| Pensión | 12 % | No |
| ARL | según clase de riesgo: I 0,522 % · II 1,044 % · III 2,436 % · IV 4,350 % · V 6,960 % | No |
| SENA | 2 % | **Sí** |
| ICBF | 3 % | **Sí** |
| Caja de compensación | 4 % | No |

**Exoneración Art. 114-1 ET (Ley 1819/2016):** las **personas jurídicas contribuyentes de renta** (y las PN con 2+ trabajadores) están exoneradas de salud patronal (8,5 %), SENA (2 %) e ICBF (3 %) por los trabajadores que devenguen, individualmente, **menos de 10 SMMLV** ($17.509.050 en 2026). La caja (4 %), la pensión (12 %) y la ARL **siempre** se pagan. Fuentes consultadas 2026-06-08: [Actualícese — aporte a salud 2026](https://actualicese.com/aporte-a-salud-2026-en-el-regimen-contributivo/) y [Buk — parafiscales 2026](https://www.buk.co/blog/aportes-parafiscales-con-salario-minimo-2026-en-colombia). Verificar en el RUT que el cliente sea contribuyente de renta (los del RST tienen reglas propias).

**Calendario legal de pagos:**

| Hito | Fecha límite | Sanción por incumplir |
|---|---|---|
| Intereses a las cesantías | **31 de enero** | sanción equivalente al doble (Ley 52/1975) |
| Consignación de cesantías al fondo | **14 de febrero** | **un día de salario por cada día de retardo** (Art. 99 Ley 50/1990) |
| Prima 1.ª mitad | **30 de junio** | indemnización moratoria CST |
| Prima 2.ª mitad | **20 de diciembre** | indemnización moratoria CST |
| Dotación | 30-abr / 31-ago / 20-dic (≤ 2 SMMLV y 3+ meses) | Art. 230 CST |

**Cuentas PUC:** provisión mensual al pasivo estimado **2610** (261005 cesantías, 261010 intereses, 261015 vacaciones, 261020 prima). Al cierre del año, lo causado y consolidado se reclasifica a pasivo real: **2510** cesantías consolidadas, **2515** intereses sobre cesantías, **2525** vacaciones consolidadas. **Dato clave de exógena (regla C.7):** el saldo inicial de 2510/2515 por tercero es la cifra de cesantías que alimenta el *Formato 2276 - Rentas de Trabajo*.

## Paso a paso (con asientos)

Seguimos con **Marta** ([[Aux 11 - Causacion de Nomina]]): devengado salarial $2.050.388 + auxilio $249.095 = base prestacional $2.299.483. IBC $2.050.388. Empresa: SAS contribuyente de renta, clase de riesgo ARL I.

**1. Provisión de prestaciones del mes (junio 2026, primer mes para simplificar los intereses):**

| Prestación | Cálculo | Valor |
|---|---|---|
| Cesantías | 2.299.483 × 8,33 % | $191.547 |
| Intereses cesantías | 191.547 × 1 % | $1.915 |
| Prima | 2.299.483 × 8,33 % | $191.547 |
| Vacaciones | 2.050.388 × 4,17 % | $85.501 |

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 510530 | Cesantías | 191.547 | |
| 510533 | Intereses sobre cesantías | 1.915 | |
| 510536 | Prima de servicios | 191.547 | |
| 510539 | Vacaciones | 85.501 | |
| 261005 | Para obligaciones laborales — cesantías | | 191.547 |
| 261010 | Intereses sobre cesantías | | 1.915 |
| 261020 | Prima de servicios | | 191.547 |
| 261015 | Vacaciones | | 85.501 |
| **Sumas** | | **470.510** | **470.510** |

> Los intereses se provisionan al 1 % mensual sobre el **acumulado** de cesantías: en el mes 6 del año la provisión es 1 % × (cesantías acumuladas a ese mes), no 1 % de la provisión del mes.

**2. Seguridad social patronal y parafiscales (IBC $2.050.388, trabajadora < 10 SMMLV → exoneración Art. 114-1 aplica):**

| Aporte | Cálculo | Valor |
|---|---|---|
| Salud patronal 8,5 % | exonerado Art. 114-1 | $0 |
| Pensión 12 % | 2.050.388 × 12 % | $246.047 |
| ARL clase I 0,522 % | 2.050.388 × 0,522 % | $10.703 |
| SENA 2 % / ICBF 3 % | exonerados Art. 114-1 | $0 |
| Caja 4 % | 2.050.388 × 4 % | $82.016 |

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 510570 | Aportes a fondos de pensiones y/o cesantías | 246.047 | |
| 510568 | Aportes a ARL | 10.703 | |
| 510572 | Aportes cajas de compensación familiar | 82.016 | |
| 237045 | Fondos de pensiones (12 % patronal) | | 246.047 |
| 237006 | Aportes a ARL | | 10.703 |
| 237010 | Aportes ICBF, SENA y cajas de compensación | | 82.016 |
| **Sumas** | | **338.766** | **338.766** |

> Si el trabajador devenga ≥ 10 SMMLV (o el empleador no es beneficiario del 114-1), se adicionan: 510569/237005 salud 8,5 %, 510578 SENA 2 % y 510575 ICBF 3 % contra 237010.

**Costo total del empleador del mes:** 2.299.483 (devengado) + 470.510 (prestaciones) + 338.766 (seguridad social patronal) = **$3.108.759** ≈ **1,35 veces** el devengado. Este multiplicador es el que se usa para cotizar servicios con componente laboral.

**3. Pago de la PILA (mes siguiente, según dígito del NIT):**

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 237005 | Aportes a EPS (4 % trabajador) | 82.016 | |
| 237045 | Fondos de pensiones (4 % + 12 %) | 328.063 | |
| 237006 | Aportes a ARL | 10.703 | |
| 237010 | ICBF, SENA y cajas | 82.016 | |
| 111005 | Bancos — cuenta corriente | | 502.798 |

**4. Pago de la prima de junio (provisión acumulada ene–jun = 6 × 191.547 = $1.149.282):**

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 261020 | Prima de servicios (provisión acumulada) | 1.149.282 | |
| 111005 | Bancos — cuenta corriente | | 1.149.282 |

Si la liquidación real difiere de lo provisionado, la diferencia ajusta el gasto (510536): **nunca** se deja saldo muerto en la 2610.

**5. Cierre del año — consolidación:** el 31-dic se liquida la prestación real por trabajador y se reclasifica la 2610 al pasivo real:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 261005 | Provisión cesantías | 2.298.564 | |
| 261010 | Provisión intereses | 137.914 | |
| 251005 | Cesantías consolidadas | | 2.298.564 |
| 251505 | Intereses sobre cesantías | | 137.914 |

Ese **saldo inicial de 2510/2515 por tercero** es el que se reporta como cesantías en el *Formato 2276 - Rentas de Trabajo* (regla C.7 de *Proyecto - Exogena 2026*). En febrero, la consignación al fondo se registra D 251005 / C 111005, y los intereses pagados en enero D 251505 / C 111005.

## Errores comunes (casos reales FYT)

1. **Provisionar vacaciones sobre la base con auxilio de transporte** — el auxilio entra a cesantías y prima, no a vacaciones.
2. **Aplicar la exoneración 114-1 a la caja de compensación o a la pensión** — la exoneración cubre solo salud 8,5 %, SENA e ICBF, y solo para devengos < 10 SMMLV.
3. **Olvidar la consolidación de diciembre:** la 2610 queda inflada, la 2510/2515 en cero, y el *Formato 2276 - Rentas de Trabajo* sale sin cesantías (regla C.7) — hallazgo recurrente en las campañas de exógena de *Proyecto - Exogena 2026*.
4. **Pagar PILA tarde:** intereses moratorios automáticos y marca ante la UGPP (*Proyecto - Nomina y Seguridad Social*). La UGPP cruza PILA ↔ nómina electrónica ↔ exógena.
5. **No consignar cesantías el 14-feb:** un día de salario por día de retardo — en un cliente con 10 empleados son cifras que se vuelven millonarias en semanas.
6. **Intereses calculados sobre la provisión del mes y no sobre el acumulado** — subestima el pasivo todo el año y revienta en enero.

## Checklist de calidad

- [ ] Provisiones del mes = base prestacional × (8,33 / 1 sobre acumulado / 8,33 / 4,17) %.
- [ ] Vacaciones sin auxilio de transporte; cesantías y prima con auxilio.
- [ ] Exoneración 114-1 verificada por trabajador (< 10 SMMLV) y por tipo de empleador.
- [ ] ARL con la clase de riesgo del RUT/afiliación del cliente (I a V).
- [ ] PILA pagada en la fecha del dígito del NIT; acuse archivado.
- [ ] Saldo 2610 = provisión acumulada − pagos; sin residuos tras prima/vacaciones.
- [ ] Consolidación 31-dic: 2610 → 2510/2515/2525 por tercero.
- [ ] Saldo inicial 2510/2515 por tercero conciliado para el F-2276.

## Relacionado

- Anterior: [[Aux 11 - Causacion de Nomina]] · Siguiente: [[Aux 13 - Nomina Electronica y Documento Soporte de Pago]]
- [[MOC - Escuela Auxiliar Contable]]
- [[07-AuxiliarNomina-Senior]] · [[02-AuxiliarContable-Senior]]
- *Proyecto - Nomina y Seguridad Social* · *Formato 2276 - Rentas de Trabajo*
