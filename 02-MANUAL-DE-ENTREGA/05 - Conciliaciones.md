---
tipo: manual
tags: [ritore, auxiliar, conciliacion, bancos, cartera]
estado: vigente
version: 1.0
fecha: 2026-11-03
---

# 05 · Conciliaciones

> **Lo que el contador espera ver.** Por cada cuenta: saldo según libros → partidas conciliatorias una a una → saldo según extracto → **diferencia CERO**. Un "faltante" o "sobrante" sin agotar los cruces no es un hallazgo: es una conciliación sin terminar.

## 1. Bancos y pasarelas — el método en tres capas

**Capa 0 · Cuadre agregado por sentido, mes a mes.** Suma los abonos del extracto contra los débitos de la cuenta en libros, y los cargos del extracto contra los créditos, **mes por mes**. Si cada sentido cuadra, el mes está prácticamente cerrado; si no, ya sabes en qué sentido y en qué mes está la diferencia. El emparejamiento individual sirve para **identificar**, no para concluir.

**Capa 1 · Cruce uno a uno.** Mismo valor y fecha dentro de ± 6 días.

**Capa 2 · Bloques por categoría.** Nómina quincenal individual contra un egreso; GMF diario contra la nota mensual; varias consignaciones contra un recibo de caja.

**Capa 3 · Uno a varios y varios a uno.** Sobre lo que sobra, busca combinaciones: un egreso del libro que se pagó con varias transferencias, un retiro en efectivo que paga varios egresos, reembolsos encadenados entre meses. `herramientas/conciliar_1aN.py` hace las capas 1 y 3 automáticamente.

Solo lo que sobrevive a las tres capas es diferencia real, y la prueba es aritmética: **la suma de las diferencias reales debe ser igual a la diferencia de saldos, al centavo**. Si no da, faltan cruces.

### Clasificación de las partidas que quedan

| Partida | Ejemplo | Tratamiento |
|---|---|---|
| Cargo del banco no registrado en libros | GMF, comisión, cuota de manejo, intereses | Se causa en el período (asiento rutinario) |
| Abono del banco no registrado en libros | Consignación de cliente, rendimientos | **Se investiga primero** con cartera; si no se identifica, va a una cuenta de paso con nombre y fecha |
| Registro en libros no reflejado en el banco | Cheque girado no cobrado, consignación en tránsito | No se ajusta; se controla y se envejece mes a mes |
| Error de valor o de cuenta | Egreso digitado por otro valor, pago registrado en caja y salió por banco | **Reclasificación** propuesta al contador |

### Formato de entrega (una hoja por cuenta en `02_CONCILIACIONES_<AAAA-MM>.xlsx`)

```
Saldo según libros al <fecha>                         $ xxx
(+) Abonos del banco no registrados en libros          $ xxx   (detalle)
(−) Cargos del banco no registrados en libros          $ xxx   (detalle)
(+) Cheques girados no cobrados                         $ xxx   (detalle con fecha de giro)
(−) Consignaciones en tránsito                          $ xxx   (detalle)
(±) Errores por reclasificar                            $ xxx   (con asiento propuesto)
= Saldo según extracto al <fecha>                      $ xxx
Diferencia                                              $ 0,00
```

Y dos hojas de soporte: **cruces confirmados** (sin ajuste) separada de **diferencias reales** (con asiento propuesto).

## 2. Pasarelas de pago

Por cada pasarela: ventas brutas del período → comisión → IVA de la comisión → retenciones que practica (renta, IVA, ICA) → abono neto al banco. La cuenta por cobrar a la pasarela debe recibir **créditos** cada vez que la pasarela abona; si en todo el trimestre no tiene créditos, el abono se está registrando en otra cuenta o no se está registrando. Las tarifas de cada pasarela se toman de su contrato o de su liquidación y se anotan en la ficha del cliente.

## 3. Cartera (clientes)

- Saldo por tercero, nunca solo el total.
- Cada recibo de caja cruza contra la o las facturas que paga (uno a varios).
- Saldos crédito en clientes = anticipos o pagos dobles: se identifican y se proponen a anticipos o a devolución.
- Edad de cartera (0–30, 31–60, 61–90, > 90) en el informe si el cliente la tiene pactada.

## 4. Proveedores y cuentas por pagar

- Cada egreso cruza contra las facturas que cancela.
- Saldos débito en proveedores = anticipos o pagos dobles: se reclasifican a anticipos (propuesto) o se piden de vuelta.
- Las retenciones practicadas al pagar deben estar en la factura causada, no en el egreso.

## 5. Impuestos

| Cuenta | Contra qué se concilia | Cuándo |
|---|---|---|
| 2365 Retención por pagar | Borrador F-350 por concepto | Todos los meses; un asiento de cierre por cada F-350 |
| 236575 / 135595 Autorretención | Ingresos del token y contables × tarifa | Todos los meses |
| 2367 ReteIVA | Casillas de ReteIVA del F-350 | Todos los meses |
| 2368 ReteICA | Declaración municipal | Según periodicidad del municipio |
| 2408 IVA | Borrador F-300 (generado y descontable por movimientos del período) | Al cerrar bimestre o cuatrimestre |
| 1355 Retenciones que le practicaron | Token y certificados de los clientes | Todos los meses |

Después de presentar, el saldo de 2365 del mes debe quedar en cero contra el pago. Un saldo que se arrastra de un mes a otro es una declaración que no cuadra o un pago que no se registró.

## 6. Nómina y seguridad social

Nómina causada (5105) ↔ nómina electrónica transmitida ↔ planilla PILA (2370 aportes) ↔ dispersión del banco (2505 salarios por pagar). Las cuatro deben dar lo mismo por empleado.

## 7. Cuentas de socios, vinculados y cuentas puente

Las cuentas de socios (por cobrar 1330/1380, por pagar 2355/2380, préstamos 28xx según el plan del cliente) se revisan contra la ficha. Una **cuenta puente** solo se acepta con nombre propio, valor, origen y fecha de cierre, y su asiento de cierre queda en la hoja de asientos propuestos marcado PENDIENTE.

## Relacionado

- [[Aux 22 - Conciliacion Bancaria]] · [[Aux 16 - GMF y Cuentas Bancarias]] · [[regla-conciliacion-cruces-1-a-n]] · [[regla-cierre-retencion-mensual]]
- [[06 - Cruce Token DIAN]] · [[Plantilla 09 - Conciliacion Bancaria]]
