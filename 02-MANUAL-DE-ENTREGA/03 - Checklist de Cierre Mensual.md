---
tipo: checklist
tags: [ritore, auxiliar, cierre, checklist]
estado: vigente
version: 1.0
fecha: 2026-11-03
---

# 03 · Checklist de cierre mensual

Se copia a `04-TRAZAS/` de cada período y se marca a medida que se avanza. Cada casilla exige **evidencia** (el archivo o la hoja donde se ve). Una casilla marcada sin evidencia es una casilla sin marcar.

## A. Insumos (`01-INSUMOS/`)
- [ ] Token DIAN del mes descargado completo: emitidos, recibidos, notas crédito y débito, documento soporte, nómina electrónica.
- [ ] Extracto de **todas** las cuentas bancarias **y** pasarelas de pago (datáfonos, plataformas de crédito, billeteras).
- [ ] Balance de prueba y libro auxiliar del mes exportados del software (formato S o W), **por movimientos del período**.
- [ ] Balance por tercero.
- [ ] Novedades de nómina, planilla PILA y soportes que no son electrónicos.
- [ ] Ningún archivo de `01-INSUMOS/` editado a mano.

## B. Causación y digitación
- [ ] Cada factura del token está causada (cruce por folio en los dos sentidos; serie de facturación sin huecos).
- [ ] Cada asiento tiene soporte, fecha del documento y tercero real con NIT y DV correctos.
- [ ] Ningún tercero genérico (`VARIOS`, `CLIENTES`, `CONSUMIDOR` donde no aplica, NIT propio de la empresa).
- [ ] Cédulas registradas **sin** dígito de verificación; NIT de personas jurídicas **con** DV.
- [ ] Ninguna cuenta contable nueva creada: se usó el plan de cuentas existente.
- [ ] Retenciones practicadas con la tarifa correcta (base, cuantía mínima, art. 383 para personas naturales de servicios).
- [ ] IVA descontable solo con factura electrónica válida a nombre del cliente y según los criterios de la ficha.
- [ ] Notas crédito referencian la factura que afectan.

## C. Conciliaciones (`02-PROCESADO/`)
- [ ] Bancos: cuadre agregado por sentido mes a mes, luego cruces 1-1 y 1-a-N; formato contable con **diferencia cero** por cuenta.
- [ ] Pasarelas: ventas brutas, comisión, IVA de la comisión, retenciones y abono neto conciliados.
- [ ] GMF, comisiones y cuota de manejo del extracto causados.
- [ ] Cartera por tercero: recaudos cruzados contra facturas; anticipos identificados; sin saldos contrarios sin explicar.
- [ ] Proveedores por tercero: pagos cruzados contra facturas; anticipos identificados.
- [ ] Cuentas de socios y vinculados (13xx, 23xx, 28xx) revisadas contra la ficha del cliente.
- [ ] Ninguna cuenta puente o "por identificar" sin nombre, valor y fecha de cierre.

## D. Impuestos (`04_CUADRE_IMPUESTOS`)
- [ ] 2365 del mes = borrador F-350 por concepto (honorarios, servicios, arrendamientos, compras, otros).
- [ ] Autorretención calculada sobre el mayor entre ingresos del token e ingresos contables, con la diferencia explicada.
- [ ] 2367 ReteIVA y 2368 ReteICA calculadas; ReteICA en cero **también se presenta** si el municipio lo exige.
- [ ] 2408: IVA generado y descontable del período = borrador F-300 (si cierra bimestre o cuatrimestre).
- [ ] 1355 retenciones que le practicaron al cliente cruzadas contra el token y los certificados.
- [ ] Un asiento de cierre por cada F-350 (ver regla de cierre de retención mes por mes).

## E. Nómina (`05_NOMINA`)
- [ ] Nómina causada = nómina electrónica transmitida = PILA = dispersión del banco.
- [ ] Provisiones de prestaciones del mes (cesantías, intereses, prima, vacaciones) al día.
- [ ] Auxilio de transporte solo hasta 2 SMMLV; FSP desde 4 SMMLV; recargos y horas extra con los factores vigentes.

## F. Cierre
- [ ] Depreciaciones y amortizaciones del mes corridas.
- [ ] Balance de prueba: débitos = créditos; ecuación patrimonial; sin saldos de naturaleza contraria nuevos sin explicar.
- [ ] `TABLA-DE-DIFERENCIAS.md`: toda diferencia ≥ 1 UVT o ≥ 0,5 % con causa, acción y estado.
- [ ] `ASIENTOS_PROPUESTOS`: cada comprobante cuadra, la hoja cuadra, cuentas existentes, tercero en cada línea.
- [ ] `NOTAS-Y-PENDIENTES.md`: cada pendiente con valor, responsable y fecha.
- [ ] `ENTREGA.md` completo con el semáforo de las ocho áreas.
- [ ] `revisar_entrega.py` sin rojos.

## Relacionado

- [[01 - Estandar de Entrega al Contador]] · [[02 - Calendario de Cierre Mensual]] · [[Aux 24 - Cierre Contable Mensual]]
