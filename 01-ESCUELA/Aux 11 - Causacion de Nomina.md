---
tipo: leccion
tags: [ritore, escuela, auxiliar, nomina]
modulo: 3
estado: vigente
fecha: 2026-06-08
---

# Aux 11 - Causación de Nómina

## Objetivo

Que el auxiliar sepa **causar una nómina mensual completa**: liquidar devengados (sueldo, auxilio de transporte, horas extra y recargos, comisiones), calcular las deducciones del trabajador (salud 4 %, pensión 4 %, FSP, retención Art. 383 ET) y registrar el asiento contable con códigos PUC, dejando el neto a pagar en la 2505 y los aportes retenidos en la 2370. La nómina bien causada es la base de la PILA, de la nómina electrónica ([[Aux 13 - Nomina Electronica y Documento Soporte de Pago]]) y del *Formato 2276 - Rentas de Trabajo*.

## Marco conceptual y normativo

**Valores 2026:** SMMLV **$1.750.905** y auxilio de transporte **$249.095** (Decretos 1469 y 1470 del 29-dic-2025). UVT 2026 = **$52.374**. Detalle normativo en *Proyecto - Nomina y Seguridad Social*.

**Jornada y valor de la hora (¡cambia en julio!):** por la Ley 2101/2021, la jornada máxima en junio de 2026 es de **44 horas semanales** → el divisor mensual es **220 horas**. Desde el **15-jul-2026** baja a **42 horas** → divisor **210**: la hora ordinaria se encarece sin que cambie el salario.

- Valor hora ordinaria SMMLV (jun-2026) = 1.750.905 / 220 = **$7.959**.

**Recargos vigentes (Ley 2466/2025 — reforma laboral):**

| Concepto | Recargo | Factor | Valor hora SMMLV jun-2026 |
|---|---|---|---|
| Hora extra diurna (HED) | 25 % | 1,25 | $9.948 |
| Hora extra nocturna (HEN) | 75 % | 1,75 | $13.928 |
| Recargo nocturno (jornada ordinaria 7:00 p. m. – 6:00 a. m.) | 35 % | 0,35 | $2.786 |
| Trabajo dominical/festivo | **80 % hasta 30-jun-2026 → 90 % desde 01-jul-2026** (100 % desde jul-2027) | 0,80 / 0,90 | $6.367 / $7.163 |

> ⚠️ Dos cambios el mismo mes (jul-2026): el recargo dominical sube a 90 % y la jornada baja a 42 h. Parametrizar el software de nómina ANTES de liquidar julio.

**Deducciones del trabajador (sobre el IBC):**
- Salud **4 %** y pensión **4 %**.
- **Fondo de Solidaridad Pensional (FSP):** solo si el IBC ≥ 4 SMMLV ($7.003.620): 1 % (y del 1,2 % al 2 % adicional progresivo para IBC de 16 a +20 SMMLV).
- **Retención en la fuente Art. 383 ET:** tabla progresiva sobre la base mensual depurada (ingreso − aportes obligatorios − deducciones − 25 % renta exenta, con límites). Primeros rangos 2026: 0 % hasta 95 UVT ($4.975.530); 19 % de 95 a 150 UVT; 28 % de 150 a 360 UVT; sigue tabla. Ver *Proyecto - Retencion en la Fuente* y [[Aux 14 - Calculo de Retenciones]].

**IBC (Ingreso Base de Cotización):** todo lo devengado con carácter **salarial** (sueldo, horas extra, recargos, comisiones). El **auxilio de transporte NO hace parte del IBC** (sí de la base de prestaciones — ver [[Aux 12 - Provisiones y Prestaciones Sociales]]). Los pagos no salariales pactados no pueden superar el 40 % de la remuneración total (Art. 30 Ley 1393/2010 — foco de la UGPP).

**Cuentas PUC:** gasto según el área: **5105** (personal de administración), **5205** (personal de ventas), **72xx** (mano de obra de producción — ver [[Aux 19 - Estado del Costo]]). Pasivos: **2505** salarios por pagar (neto), **2370** retenciones y aportes de nómina, **2365** retención en la fuente Art. 383.

## Paso a paso (con asientos)

**Caso:** Marta, auxiliar administrativa de una SAS, junio 2026. Sueldo SMMLV, 10 horas extra diurnas y $200.000 de comisiones.

**1. Liquidar devengados:**

| Concepto | Cálculo | Valor |
|---|---|---|
| Sueldo | SMMLV | $1.750.905 |
| Auxilio de transporte | devenga ≤ 2 SMMLV → tiene derecho | $249.095 |
| Horas extra diurnas | 10 × $7.959 × 1,25 = 10 × $9.948 | $99.483 |
| Comisiones | pactadas | $200.000 |
| **Total devengado** | | **$2.299.483** |

**2. Determinar el IBC:** devengado salarial = 1.750.905 + 99.483 + 200.000 = **$2.050.388** (sin auxilio de transporte).

**3. Liquidar deducciones:**

| Deducción | Cálculo | Valor |
|---|---|---|
| Salud trabajador 4 % | 2.050.388 × 4 % | $82.016 |
| Pensión trabajador 4 % | 2.050.388 × 4 % | $82.016 |
| FSP | IBC = 1,17 SMMLV < 4 SMMLV | $0 |
| Retención Art. 383 | base depurada ≈ $1.415.000 < 95 UVT ($4.975.530) | $0 |
| **Total deducciones** | | **$164.032** |

**4. Neto a pagar:** 2.299.483 − 164.032 = **$2.135.451**.

**5. Asiento de causación (28-jun-2026):**

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 510506 | Sueldos | 1.750.905 | |
| 510515 | Horas extras y recargos | 99.483 | |
| 510518 | Comisiones | 200.000 | |
| 510527 | Auxilio de transporte | 249.095 | |
| 237005 | Aportes a EPS (4 % trabajador) | | 82.016 |
| 237045 | Aportes a fondos de pensiones (4 % trabajador) | | 82.016 |
| 250505 | Salarios por pagar | | 2.135.451 |
| **Sumas** | | **2.299.483** | **2.299.483** |

> Si hubiera retención Art. 383, el crédito adicional va a la **236505** (retención salarios). Si Marta fuera vendedora, los débitos serían 5205xx; si fuera operaria de planta, 72xx.

**6. Asiento del pago (30-jun-2026):**

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 250505 | Salarios por pagar | 2.135.451 | |
| 111005 | Bancos — cuenta corriente | | 2.135.451 |

**7. Salario integral — la diferencia clave:**
- Mínimo legal: 13 SMMLV (10 de salario + factor prestacional del 30 %) = **$22.761.765** en 2026.
- **No** genera provisión de cesantías, intereses, ni prima (van incluidas en el factor); **sí** genera vacaciones.
- El **IBC es el 70 %** del salario integral: 22.761.765 × 70 % = $15.933.236 → 9,1 SMMLV → aplica **FSP del 1 %** ($159.332) además del 4 % + 4 %.
- No tiene auxilio de transporte y casi siempre tiene retención Art. 383.

## Errores comunes (casos reales FYT)

1. **Incluir el auxilio de transporte en el IBC** → aportes inflados y hallazgo en el cruce PILA ↔ contabilidad. El error inverso (excluir comisiones del IBC) es exactamente lo que fiscaliza la **UGPP**.
2. **No reparametrizar recargos en los hitos de la reforma:** liquidar julio-2026 con dominical al 80 % (ya es 90 %) o con divisor 220 (ya es 210). En clientes con domingos intensivos como **Cliente - RESTAURANTE L** la diferencia es material.
3. **Causar nómina y pagos laborales en el F-1001 de exógena:** los pagos laborales van al *Formato 2276 - Rentas de Trabajo* y se **excluyen** del 1001 (regla C.3 de *Proyecto - Exogena 2026*).
4. **Confundir 2370 con 2365:** la 2370 recibe los aportes de seguridad social retenidos al trabajador; la 2365 solo la retención en la fuente de renta (Art. 383).
5. **Mezclar gasto de administración y de producción:** en manufactura (**Cliente - METALMECÁNICA T**) la nómina de planta va a la clase 7, no a la 5105 — si no, el estado de costos queda cojo ([[Aux 19 - Estado del Costo]]).
6. **Pagar la nómina sin causarla** (débito directo al gasto contra bancos): se pierde el control del pasivo y el cruce con PILA y nómina electrónica.

## Checklist de calidad

- [ ] Devengado total = sueldo + auxilio + extras + comisiones, soportado en el control de tiempos.
- [ ] IBC = devengado salarial (sin auxilio de transporte); verificado contra PILA.
- [ ] Deducciones: 4 % + 4 % sobre el mismo IBC; FSP solo si IBC ≥ 4 SMMLV.
- [ ] Retención Art. 383 calculada con la depuración y la tabla UVT 2026.
- [ ] Asiento cuadrado: débitos (51xx/52xx/72xx) = créditos (2370 + 2365 + 2505).
- [ ] Recargos con los porcentajes vigentes a la fecha de la liquidación (¡ojo a julio-2026!).
- [ ] Pagos no salariales ≤ 40 % de la remuneración total (Ley 1393/2010).
- [ ] La nómina causada coincide con la que se transmitirá en nómina electrónica.

## Relacionado

- Anterior: [[Aux 10 - Documento Soporte a No Obligados]] · Siguiente: [[Aux 12 - Provisiones y Prestaciones Sociales]]
- [[MOC - Escuela Auxiliar Contable]]
- [[07-AuxiliarNomina-Senior]] · [[02-AuxiliarContable-Senior]]
- *Proyecto - Nomina y Seguridad Social* · *Proyecto - Retencion en la Fuente*
