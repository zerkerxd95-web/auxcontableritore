---
tipo: manual
tags: [ritore, auxiliar, nomina, pila, seguridad-social]
estado: vigente
version: 1.0
fecha: 2026-11-03
---

# 08 · Nómina y seguridad social

> La nómina tiene cuatro versiones que deben dar lo mismo: **la causada**, **la electrónica transmitida a la DIAN**, **la PILA** y **lo que salió del banco**. El auxiliar entrega las cuatro cruzadas por empleado.

## 1. Cada período de pago

1. Recibe novedades (ingresos, retiros, incapacidades, licencias, vacaciones, horas extra, recargos, bonificaciones).
2. Liquida devengados y deducciones con los valores del año (`VALORES-VIGENTES.md`): SMMLV, auxilio de transporte hasta 2 SMMLV, salud 4 % y pensión 4 % a cargo del empleado, Fondo de Solidaridad Pensional desde 4 SMMLV.
3. Causa la nómina (Aux 11) y las provisiones del mes (Aux 12): cesantías, intereses sobre cesantías, prima y vacaciones.
4. Verifica que la nómina electrónica del mes quede transmitida (Aux 13). Si se atrasó, se transmite por bloques atrasados, nunca se omite.
5. Cruza la PILA contra la causación de aportes (2370) y la dispersión del banco contra los salarios por pagar (2505).

## 2. Horas extra y recargos `[VERIFICAR VIGENCIA cada julio]`

Con la reducción de jornada (Ley 2101 de 2021) y la Ley 2466 de 2025:

- **Divisor de la hora**: jornada semanal × 30 / 6. Con jornada de 42 horas el divisor es **210**; liquidar con 240 paga de menos.
- **Jornada nocturna** desde las 7:00 p. m.
- **Recargo dominical y festivo**: 90 % desde el 1 de julio de 2026 y 100 % desde julio de 2027.

| Clase de hora | Factor sobre la hora ordinaria |
|---|---|
| Recargo nocturno (hora ordinaria) | 0,35 |
| Recargo dominical/festivo diurno | 0,90 |
| Recargo dominical/festivo nocturno | 1,25 |
| Hora extra diurna | 1,25 |
| Hora extra nocturna | 1,75 |
| Hora extra dominical/festiva diurna | 2,15 |
| Hora extra dominical/festiva nocturna | 2,65 |

**Recargo no es hora extra.** El recargo es una hora de la jornada ordinaria que cae de noche o en domingo: el sueldo ya pagó la hora, se liquida solo el porcentaje adicional. La hora extra es tiempo por encima de la jornada y se paga completa con su factor.

Las horas extra y los recargos son **salario** (art. 127 CST) y forman parte del IBC. Los pagos no salariales no pueden superar el 40 % de la remuneración total (art. 30 de la Ley 1393 de 2010); si se superan, se informa al contador.

## 3. Entrega (`05_NOMINA_<AAAA-MM>.xlsx`)

Una hoja por fuente (causada, electrónica, PILA, banco) y una hoja de cruce por empleado con las diferencias. Toda diferencia se explica en `TABLA-DE-DIFERENCIAS.md`.

## 4. Lo anual

- Cesantías: se consignan al fondo antes del 14 de febrero; intereses sobre cesantías se pagan al empleado en enero.
- Prima: junio y diciembre.
- Certificados de ingresos y retenciones (F-220) a empleados: febrero–marzo.
- Liquidaciones de contrato: con el contador; el auxiliar prepara la liquidación y la revisa contra el contrato y la historia de pagos.

## Relacionado

- [[Aux 11 - Causacion de Nomina]] · [[Aux 12 - Provisiones y Prestaciones Sociales]] · [[Aux 13 - Nomina Electronica y Documento Soporte de Pago]]
- [[Reforma Laboral Ley 2466 de 2025]] · [[Seguridad Social y Parafiscales]] · [[Prestaciones Sociales y Liquidacion]] · [[Plantilla 08 - Nomina y Prestaciones Sociales]]
