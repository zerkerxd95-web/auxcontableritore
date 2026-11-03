---
tipo: leccion
tags: [ritore, escuela, auxiliar, nomina, nomina-electronica]
modulo: 3
estado: vigente
fecha: 2026-06-08
---

# Aux 13 - Nómina Electrónica y Documento Soporte de Pago

## Objetivo

Que el auxiliar entienda qué es el **documento soporte de pago de nómina electrónica** (Resolución DIAN 000013 de 2021), cuándo y cómo se transmite, por qué de él depende la **deducibilidad del gasto laboral en renta**, y cómo se cruza contra la contabilidad, la PILA y el *Formato 2276 - Rentas de Trabajo*. La nómina electrónica no es "un trámite más": es la fotografía mensual que la DIAN y la UGPP usan para fiscalizar al cliente.

## Marco conceptual y normativo

- **Norma base:** Resolución DIAN **000013 del 11-feb-2021** y modificatorias — crea el documento soporte de pago de nómina electrónica y las notas de ajuste.
- **Obligados:** quienes realicen pagos de nómina y quieran soportar **costos y deducciones en renta** o impuestos descontables. Sin documento soporte transmitido y validado, el costo laboral **no es deducible** (concordancia con el Art. 771-2 ET: el documento soporte es requisito de procedencia).
- **Plazo de transmisión:** dentro de los **10 primeros días del mes siguiente** al pago (calendario 2026: nómina de enero → 10-feb; febrero → 10-mar; marzo → 10-abr; abril → 11-may por festivo, y así sucesivamente — ver *Proyecto - Nomina y Seguridad Social*).
- **Documentos del sistema:**
	- **Nómina individual (NIE):** XML por trabajador y por mes, con devengados, deducciones y neto. La DIAN lo valida y devuelve el CUNE (código único).
	- **Nómina individual de ajuste:** XML que **reemplaza o elimina** un documento ya transmitido (errores de valores, de identificación, retroactivos). Nunca se "corrige" transmitiendo otro documento normal duplicado.
- **Quién la transmite en FYT:** el software habilitado del cliente o el proveedor tecnológico; el auxiliar valida los valores ANTES de transmitir y archiva los acuses en la carpeta canónica del cliente.

**El triángulo de consistencia que fiscalizan DIAN y UGPP:**

```
Nómina electrónica (XML)  ↔  Contabilidad (51xx/52xx/72xx, 2505, 2370)  ↔  PILA (IBC)
                 ↘                          ↓                          ↙
                       Formato 2276 de exógena + certificados laborales
```

- La **UGPP** verifica que el **IBC de PILA** cuadre con los devengos salariales de la nómina electrónica y la contabilidad, y que los pagos no salariales no superen el **40 %** de la remuneración total (Art. 30 Ley 1393/2010).
- La **DIAN** cruza el gasto laboral declarado en renta contra los XML transmitidos, y la exógena F-2276 contra ambos.
- Regla C.3 de *Proyecto - Exogena 2026*: los pagos laborales (y los pagos del Art. 383 a PN sin retención) se reportan en el **2276** y se **excluyen del F-1001**.

## Paso a paso (con asientos)

**1. Causar la nómina** como en [[Aux 11 - Causacion de Nomina]] y las provisiones de [[Aux 12 - Provisiones y Prestaciones Sociales]]. La nómina electrónica **no genera asiento propio**: es el documento soporte del asiento ya causado. El XML de Marta debe decir exactamente lo que dice la contabilidad:

| Concepto del XML (NIE) | Cuenta contable | Valor |
|---|---|---|
| Devengado: sueldo | 510506 | 1.750.905 |
| Devengado: auxilio de transporte | 510527 | 249.095 |
| Devengado: horas extra | 510515 | 99.483 |
| Devengado: comisiones | 510518 | 200.000 |
| Deducción: salud 4 % | 237005 | 82.016 |
| Deducción: pensión 4 % | 237045 | 82.016 |
| Neto pagado (ComprobanteTotal) | 250505 | 2.135.451 |

**2. Conciliar antes de transmitir (primeros días del mes siguiente):** total devengado del XML = suma débitos 51xx/52xx/72xx de conceptos de nómina del mes; total deducciones = créditos 2370/2365; neto = movimiento de la 2505. Diferencias = error en el software de nómina o en la contabilización: se corrige ANTES de transmitir.

**3. Transmitir dentro de los 10 primeros días** del mes siguiente al pago. Descargar el acuse/CUNE de cada trabajador y archivarlo.

**4. Si hay error después de transmitir:** generar **nota de ajuste** (reemplazo). Ejemplo: se transmitió a Marta sin las comisiones de $200.000. Se ajusta el XML por reemplazo y, si la contabilidad también estaba errada, se corrige con asiento:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 510518 | Comisiones | 200.000 | |
| 237005 | Aportes a EPS (4 %) | | 8.000 |
| 237045 | Fondos de pensiones (4 %) | | 8.000 |
| 250505 | Salarios por pagar | | 184.000 |

(Y se ajusta la PILA del periodo con la planilla correctiva — el IBC subió.)

**5. Cierre anual:** conciliación de cuatro vías — nómina contable ↔ XML de los 12 meses ↔ PILA ↔ **F-2276** ↔ certificados de ingresos y retenciones. Las cesantías del 2276 salen del saldo inicial 2510/2515 por tercero (regla C.7, ver [[Aux 12 - Provisiones y Prestaciones Sociales]]).

## Errores comunes (casos reales FYT)

1. **Transmitir tarde de forma sistemática:** la DIAN puede rechazar la deducción del costo laboral en renta — regla crítica de *Proyecto - Nomina y Seguridad Social*. Para un cliente con nómina de $20M/mes, perder la deducción es regalarse un mayor impuesto de ~$70M/año (tarifa 35 %).
2. **XML ≠ contabilidad:** transmitir lo que dice el software de nómina sin verificar que la causación contable diga lo mismo. En el cruce anual del 2276 las diferencias afloran y tocan rehacer meses enteros.
3. **Corregir transmitiendo un duplicado** en lugar de la **nota de ajuste**: la DIAN queda con dos documentos vigentes del mismo mes y el gasto aparece doble en los cruces.
4. **IBC de PILA distinto del devengado salarial del XML:** disparador clásico de requerimiento UGPP. Vigilar también el tope del 40 % de pagos no salariales (Ley 1393/2010).
5. **No archivar los acuses/CUNE:** ante requerimiento, el cliente no puede demostrar la transmisión oportuna. SIEMPRE a la carpeta canónica (*Proyecto - Nomina y Seguridad Social*, regla crítica).
6. **Olvidar trabajadores retirados en el mes:** la liquidación final (con vacaciones compensadas e indemnizaciones) también se transmite.

## Checklist de calidad

- [ ] XML del mes = causación contable (devengados, deducciones, neto), trabajador por trabajador.
- [ ] Transmisión dentro de los 10 primeros días del mes siguiente; acuses/CUNE archivados.
- [ ] IBC PILA = devengado salarial del XML = base de aportes en contabilidad.
- [ ] Errores corregidos con nota de ajuste (reemplazo/eliminación), nunca con duplicados.
- [ ] Retiros y liquidaciones finales incluidos.
- [ ] Pagos no salariales ≤ 40 % de la remuneración total.
- [ ] Cierre anual: nómina contable ↔ XML ↔ PILA ↔ F-2276 conciliados antes de la exógena.

## Relacionado

- Anterior: [[Aux 12 - Provisiones y Prestaciones Sociales]] · Siguiente: [[Aux 14 - Calculo de Retenciones]]
- [[MOC - Escuela Auxiliar Contable]]
- [[07-AuxiliarNomina-Senior]] · [[02-AuxiliarContable-Senior]]
- *Formato 2276 - Rentas de Trabajo* · *Proyecto - Nomina y Seguridad Social* · *Proyecto - Exogena 2026*
