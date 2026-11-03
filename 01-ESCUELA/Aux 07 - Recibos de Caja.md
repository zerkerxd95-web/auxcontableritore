---
tipo: leccion
tags: [ritore, escuela, auxiliar, recaudo, cartera]
modulo: 2
estado: vigente
fecha: 2026-06-08
---
# Aux 07 - Recibos de Caja

## Objetivo
El auxiliar sabrá elaborar y contabilizar recibos de caja: aplicar recaudos a facturas específicas, manejar abonos parciales, descuentos por pronto pago y cruces con anticipos (2805), e identificar al pagador real desde el extracto bancario.

## Marco conceptual y normativo
- **Recibo de caja:** comprobante de contabilidad **interno** (Decreto 2649/1993 Art. 124) que documenta la entrada de dinero — efectivo, consignación o transferencia — y su aplicación contable. Numeración consecutiva propia.
- No reemplaza la factura: la factura causa el ingreso; el recibo de caja registra el **recaudo** (descarga la CxC 1305 o crea el anticipo 2805).
- **Descuento por pronto pago (condicionado):** financieramente es un gasto para quien lo concede — cuenta **530535** (descuentos comerciales condicionados). No toca el IVA ya generado ni reversa el ingreso facturado.

## Paso a paso

1. Identifica la entrada de dinero (consignación en el extracto, efectivo, pasarela/POS).
2. **Identifica al pagador real:** el nombre del extracto no siempre es el cliente de la factura (paga la esposa, otra empresa del grupo, Sistecrédito). Si no se identifica, se solicita soporte ANTES de aplicar — un recaudo no identificado nunca se aplica "al más parecido".
3. Ubica la(s) factura(s) pendiente(s) del tercero en el auxiliar de cartera (1305).
4. Aplica el recaudo: total, parcial (abono) o como anticipo si no hay factura (2805).
5. Genera el recibo de caja con consecutivo, fecha, tercero, forma de pago y facturas aplicadas.
6. Notifica/actualiza el aging de cartera.

### Asientos modelo

**1. Recaudo total de una factura** — el cliente consigna $9.320.000 de la factura del ejemplo de [[Aux 05 - Causacion de Facturas de Venta]]:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 111005 | Bancos — Bancolombia | 9.320.000 | |
| 130505 | Clientes nacionales | | 9.320.000 |

**2. Abono parcial** — el cliente abona $4.000.000 a una factura de $9.320.000:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 111005 | Bancos | 4.000.000 | |
| 130505 | Clientes nacionales (abono FV-1234) | | 4.000.000 |

*El saldo de la factura ($5.320.000) sigue vivo en el auxiliar por tercero y por factura — la aplicación SIEMPRE es a factura específica, no "al saldo global".*

**3. Descuento por pronto pago concedido** — factura de $10.000.000, pago dentro de 10 días con 2% de descuento; el cliente consigna $9.800.000:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 111005 | Bancos | 9.800.000 | |
| 530535 | Descuentos comerciales condicionados | 200.000 | |
| 130505 | Clientes nacionales | | 10.000.000 |

**4. Recaudo sin factura → anticipo** (patrón **Cliente - SALÓN DE BELLEZA I**: ingresos del día no facturados van a anticipos de clientes):

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 111005 | Bancos | 350.000 | |
| 280505 | Anticipos y avances recibidos de clientes | | 350.000 |

**5. Cruce posterior anticipo ↔ factura** — se factura el servicio ya cobrado:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 280505 | Anticipos y avances recibidos de clientes | 350.000 | |
| 130505 | Clientes nacionales (aplica FV-1300) | | 350.000 |

**6. Recaudo vía financiador (patrón Sistecrédito en SALÓN DE BELLEZA I):** el financiador paga la cartera del cliente final — el dinero llega de Sistecrédito pero descarga la cuenta del deudor según el reporte del financiador (en SALÓN DE BELLEZA I se descarga de 13050501).

## Errores comunes
- **Aplicar el recaudo al tercero del extracto y no al deudor real:** en grupos empresariales (SALÓN DE BELLEZA I ↔ INVERSIONES N) los pagos cruzados entre empresas son constantes; aplicar mal genera saldos contrarios y carteras ficticias.
- **Dejar recaudos "en el aire" (sin aplicar):** crean partidas conciliatorias eternas; regla del agente: movimientos bancarios sin identificar = 0 al cierre del mes.
- **Registrar el descuento por pronto pago como menor ingreso o nota crédito:** es gasto financiero 530535; emitir nota crédito por un descuento condicionado altera indebidamente IVA e ingresos.
- **No cruzar contra 2805 antes de crear cartera:** si el cliente ya había anticipado, facturarle y además cobrarle duplica el ingreso percibido y deja el 2805 inflado (depuración típica del cierre de diciembre en SALÓN DE BELLEZA I).
- **Romper el consecutivo de recibos de caja** o expedirlos sin fecha/tercero: debilita el control interno y la auditoría del disponible.
- **Confundir recaudo con ingreso:** un recibo de caja jamás acredita el 4135 directamente si existe factura — el ingreso ya se causó con la factura.

## Checklist de calidad
1. ¿Pagador identificado y coincide con el deudor de la factura (o quedó documentado el pago por cuenta de tercero)?
2. ¿Aplicación a factura específica (no al saldo global)?
3. ¿Consecutivo del recibo de caja íntegro y fechado?
4. ¿Descuentos por pronto pago en 530535?
5. ¿Recaudos sin factura llevados a 2805 y con plan de cruce?
6. ¿El auxiliar de cartera quedó sin saldos contrarios (créditos en 1305)?
7. ¿Total recaudado del mes concilia contra el extracto bancario?

## Relacionado
- Anterior: [[Aux 06 - Causacion de Facturas de Compra y Gastos]] · Siguiente: [[Aux 08 - Comprobantes de Egreso]]
- [[MOC - Escuela Auxiliar Contable]] · [[02-AuxiliarContable-Senior]]
- [[Aux 22 - Conciliacion Bancaria]] · [[Aux 05 - Causacion de Facturas de Venta]]
- **Cliente - SALÓN DE BELLEZA I** (anticipos 2805, Sistecrédito, pagos cruzados de grupo)
