---
tipo: leccion
tags: [ritore, escuela, auxiliar, egresos, pagos]
modulo: 2
estado: vigente
fecha: 2026-06-08
---
# Aux 08 - Comprobantes de Egreso

## Objetivo
El auxiliar sabrá elaborar y contabilizar comprobantes de egreso: pagar pasivos ya causados (proveedores, nómina, impuestos), registrar el GMF asociado y aplicar la regla de la firma: **todo egreso debe tener factura o documento soporte ANTES del pago**.

## Marco conceptual y normativo
- **Comprobante de egreso:** comprobante interno (Decreto 2649/1993 Art. 124) que documenta cada salida de dinero, con consecutivo, beneficiario, concepto, forma de pago y soportes anexos (factura + autorización de pago).
- **Secuencia correcta: causar → autorizar → pagar.** El egreso descarga un pasivo ya causado (2205/2335/23xx/25xx). Si al momento de pagar no existe causación, primero se causa (con su soporte) y luego se paga.
- **GMF (4×1000):** Art. 870 y ss. ET. Lo debita el banco en cada dispersión; se registra en **530525** (convención de la firma). Solo el 50% es deducible en renta (Art. 115 ET) — por eso vive en la clase 53.
- **Art. 771-5 ET:** límite a pagos en efectivo (100 UVT = $5.237.400 por pago en 2026, y topes globales); pagos grandes van por canal bancario.

## Paso a paso

1. Verifica el **soporte**: factura/documento soporte causado + autorización de pago (del cliente o del flujo interno). Sin soporte, NO hay pago.
2. Confirma el valor a pagar = saldo del pasivo en el auxiliar del tercero (neto de retenciones ya causadas, anticipos y notas).
3. Ejecuta/registra el pago contra el banco correcto.
4. Registra el GMF del movimiento.
5. Genera el comprobante de egreso con consecutivo y anexa soportes.
6. Marca la factura como pagada en el auxiliar (aging de CxP al día).

### Asientos modelo

**1. Pago a proveedor** — saldo en 2205 de $6.990.000 (neto de retención, ver [[Aux 06 - Causacion de Facturas de Compra y Gastos]]):

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 220505 | Proveedores nacionales | 6.990.000 | |
| 530525 | Gravamen a los movimientos financieros | 27.960 | |
| 111005 | Bancos — Bancolombia | | 7.017.960 |

**2. Pago de nómina** — salarios por pagar del mes ($1.859.928 del ejemplo de [[Aux 02 - Partida Doble y Asientos Contables]]):

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 250505 | Salarios por pagar | 1.859.928 | |
| 530525 | GMF | 7.440 | |
| 111005 | Bancos | | 1.867.368 |

**3. Pago de impuestos** — se paga la retefuente del mes ($505.000) y el saldo de IVA del bimestre ($2.300.000):

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 2365xx | Retención en la fuente por pagar | 505.000 | |
| 240805 | IVA por pagar (saldo del periodo) | 2.300.000 | |
| 530525 | GMF | 11.220 | |
| 111005 | Bancos | | 2.816.220 |

*El pago de impuestos NUNCA es gasto: descarga el pasivo 2404/2408/2365/2367/2368 ya causado. Las sanciones e intereses de mora sí son gasto — no deducible (539520 / 530520).*

**4. Pago de seguridad social (PILA):**

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 2370xx | Retenciones y aportes de nómina | 689.357 | |
| 530525 | GMF | 2.757 | |
| 111005 | Bancos | | 692.114 |

## Errores comunes
- **Pagar sin factura ("luego la mandan"):** regla de la firma — el soporte va ANTES del pago. Un egreso sin soporte es un hallazgo inmediato y, fiscalmente, un costo en riesgo (Art. 771-2 ET).
- **Pagar y mandar el débito directo al gasto** existiendo causación previa: duplica el gasto (una vez al causar, otra al pagar). El pago descarga el PASIVO.
- **Olvidar el GMF:** queda como partida conciliatoria perpetua en bancos; el GMF se registra movimiento a movimiento o con el extracto ([[Aux 22 - Conciliacion Bancaria]]).
- **Pagar al tercero equivocado del grupo:** en **Cliente - SALÓN DE BELLEZA I** / INVERSIONES N la nómina y los proveedores se pagan cruzados entre empresas — cada egreso debe quedar en la empresa cuyo pasivo descarga, y el cruce interempresas registrado como CxC/CxP entre vinculadas.
- **Egresos "sin identificar" clasificados a la carrera:** el patrón correcto (SALÓN DE BELLEZA I) es agotar la identificación (nómina, proveedores del grupo, seguridad social) y solo el residuo documentado va a 530505 como no deducible.
- **No descontar anticipos ni notas crédito** del saldo a pagar: se paga de más y nace una CxC incómoda con el proveedor.
- **Romper el consecutivo de egresos** o emitirlos sin autorización: debilita el control del disponible (es de lo primero que prueba el revisor fiscal).

## Checklist de calidad
1. ¿Cada egreso tiene factura/documento soporte causado + autorización ANTES del pago?
2. ¿El pago descarga el pasivo correcto (2205/2335/23xx/24xx/25xx) y no un gasto?
3. ¿Valor pagado = saldo del auxiliar del tercero (neto de retenciones, anticipos, notas)?
4. ¿GMF registrado en 530525 por cada dispersión?
5. ¿Pagos en efectivo dentro de los límites del Art. 771-5 ET?
6. ¿Consecutivo de comprobantes de egreso completo?
7. ¿Egresos del mes concilian contra el extracto bancario?
8. ¿Pagos interempresas del grupo registrados como CxC/CxP entre vinculadas?

## Relacionado
- Anterior: [[Aux 07 - Recibos de Caja]] · Siguiente: [[Aux 09 - Notas Credito y Debito]]
- [[MOC - Escuela Auxiliar Contable]] · [[02-AuxiliarContable-Senior]]
- [[Aux 11 - Causacion de Nomina]] · [[Aux 14 - Calculo de Retenciones]] · [[Aux 22 - Conciliacion Bancaria]]
- **Cliente - SALÓN DE BELLEZA I** (clasificación de egresos y pagos cruzados)
