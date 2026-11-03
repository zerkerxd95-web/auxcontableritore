---
tipo: leccion
tags: [ritore, escuela, auxiliar, gmf, bancos]
modulo: 4
estado: vigente
fecha: 2026-06-08
---

# Aux 16 - GMF y Cuentas Bancarias

## Objetivo

Que el auxiliar entienda cómo opera el **Gravamen a los Movimientos Financieros (GMF, "4×1000")**, aplique la **exención de la cuenta marcada** (350 UVT/mes), lo contabilice correctamente (530595), controle el **50 % deducible** en renta y lo **concilie contra el extracto** cada mes. El GMF es pequeño por transacción pero, mal manejado, suma millones al año y descuadra todas las conciliaciones bancarias.

## Marco conceptual y normativo

**Qué es (Arts. 870–881 ET):** impuesto del **4 por mil (0,4 %)** sobre las disposiciones de recursos de cuentas corrientes, de ahorro y de depósito: retiros, transferencias, pagos con cheque, débitos automáticos. Lo **retiene el banco** automáticamente al debitar la cuenta: el cliente no lo declara, solo lo asume — por eso aparece en el extracto, no en una factura.

**Exención principal (Art. 879 num. 1 ET):** los retiros de **una cuenta de ahorros marcada como exenta** por el titular, hasta **350 UVT mensuales** = 350 × $52.374 = **$18.330.900 en 2026**. Lo que exceda el tope en el mes sí paga 4×1000. Solo se puede tener **una** cuenta marcada por titular ante el sistema financiero (la Ley 2277/2022 abrió la puerta a distribuir el beneficio entre varios productos hasta el mismo tope global — `[VERIFICAR reglamentación y operatividad con el banco antes de aplicarlo a un cliente]`).

**Deducibilidad (Art. 115 ET):** en renta es deducible el **50 %** del GMF efectivamente pagado en el año, **certificado por el banco**, sin necesidad de relación de causalidad con la actividad. El otro 50 % es gasto contable **no deducible** → diferencia permanente que se controla en la hoja fiscal de la declaración.

**Cálculo rápido:** GMF = débitos sujetos × 0,004. Ejemplo: transferencia de $10.000.000 → GMF $40.000.

**Cuenta PUC (práctica FYT):** **530595** (gastos financieros — otros / GMF) al débito, contra la cuenta bancaria. Recomendado un auxiliar exclusivo para GMF (no mezclarlo con comisiones bancarias 530520), porque en renta el tratamiento es distinto y el certificado del banco se cruza contra esa subcuenta.

## Paso a paso (con asientos)

**1. Registro mensual desde el extracto.** El GMF se toma del **extracto bancario** (el banco lo debita transacción por transacción o en resumen). Cliente con débitos no exentos de $25.000.000 en el mes → GMF = $100.000:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 530595 | Gastos financieros — GMF (4×1000) | 100.000 | |
| 111005 | Bancos — cuenta corriente | | 100.000 |

**2. Cuenta de ahorros marcada (exenta).** Retiros del mes por $15.000.000 en la cuenta marcada → bajo el tope de $18.330.900 → GMF $0. Si en el mes retira $20.000.000 → el exceso de $1.669.100 paga: GMF = $6.676.

**3. Manejo de varias cuentas — caso **Cliente - COMERCIO DE BICICLETAS A**** (2 cuentas Bancolombia): solo **una** puede estar marcada como exenta. Estrategia operativa: concentrar la dispersión de pagos (nómina, proveedores) en la cuenta marcada hasta el tope mensual, y vigilar que la otra asuma el menor flujo posible. En la contabilidad, cada cuenta bancaria tiene su auxiliar (111005-01, 111005-02) y su GMF se registra por separado para poder conciliar extracto por extracto.

**4. Conciliación mensual del GMF** (práctica de [[03-AuxiliarConciliacionesBancarias-Senior]] y de [[Aux 22 - Conciliacion Bancaria]]):

| Verificación | Fuente A | Fuente B |
|---|---|---|
| GMF del mes por cuenta | Extracto (códigos "GMF"/"4x1000") | Auxiliar 530595 por banco |
| GMF acumulado del año | Suma extractos | Saldo 530595 |
| GMF para renta | **Certificado anual del banco** | 530595 × 50 % deducible |

Si el libro no registra el GMF que el extracto sí muestra, la conciliación bancaria arroja partidas conciliatorias "notas débito sin contabilizar" — el ajuste se registra con el asiento del paso 1, **en el mes del extracto**.

**5. Control fiscal al cierre:** del saldo anual de 530595 (ej. $1.200.000), solo $600.000 es deducible; los otros $600.000 se controlan como gasto no deducible en la conciliación fiscal. El soporte de la deducción es el **certificado del banco**, no el auxiliar.

## Errores comunes (casos reales FYT)

1. **No contabilizar el GMF mensualmente** y dejarlo como partida conciliatoria eterna — descuadra la [[Aux 22 - Conciliacion Bancaria]] y el saldo del banco en libros queda inflado. Es la nota débito sin registrar más frecuente del portafolio.
2. **Mezclar GMF con comisiones bancarias** en una sola subcuenta: en renta la comisión es 100 % deducible y el GMF solo 50 % — sin separación toca rehacer el análisis al cierre.
3. **Marcar como exenta la cuenta equivocada** (la de menor movimiento) o creer que ambas cuentas de **Cliente - COMERCIO DE BICICLETAS A** están exentas — solo una cuenta goza del beneficio.
4. **Deducir el 100 % del GMF en renta** — solo procede el 50 % certificado (Art. 115 ET). El revisor y la DIAN lo detectan de inmediato porque cruzan con el certificado bancario.
5. **Calcular el GMF "teórico" en vez de tomar el real del extracto:** hay operaciones exentas (traslados entre cuentas del mismo titular en el mismo banco, recaudos de impuestos) y el banco ya las depuró — la fuente de verdad es el extracto.
6. **Olvidar el GMF en los flujos de caja proyectados:** todo plan de pagos grande (p. ej. compra de inventario de **Cliente - AGROPECUARIA D**) debe presupuestar el 0,4 % adicional.

## Checklist de calidad

- [ ] GMF de TODOS los extractos del mes contabilizado (530595, auxiliar por banco).
- [ ] Cuenta marcada identificada por cliente; tope mensual de 350 UVT ($18.330.900 en 2026) vigilado.
- [ ] GMF separado de comisiones y otros gastos bancarios.
- [ ] Conciliación: GMF extracto = GMF libro, cuenta por cuenta, mes a mes.
- [ ] Cierre: 530595 anual vs certificado del banco; 50 % marcado como no deducible.
- [ ] Clientes con varias cuentas: estrategia de uso de la cuenta exenta documentada.

## Relacionado

- Anterior: [[Aux 15 - IVA y Prorrateo]] · Siguiente: [[Aux 17 - Inventarios y Compras Multi-item]]
- [[MOC - Escuela Auxiliar Contable]]
- [[02-AuxiliarContable-Senior]] · [[03-AuxiliarConciliacionesBancarias-Senior]]
- [[Aux 22 - Conciliacion Bancaria]] · **Cliente - COMERCIO DE BICICLETAS A**
