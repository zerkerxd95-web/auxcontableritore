---
tipo: manual
tags: [ritore, auxiliar, digitacion, causacion]
estado: vigente
version: 1.0
fecha: 2026-11-03
---

# 04 · Digitación y causación

> **Principio.** Lo que se digita bien una vez no se vuelve a tocar. Cada error de digitación se paga tres veces: en el cierre del mes, en la exógena del año y en la renta. Las lecciones Aux 01 a Aux 19 explican el **porqué**; este manual fija el **cómo se hace en la firma**.

## 1. Las diez reglas de digitación

1. **Sin soporte no hay asiento.** Factura electrónica, documento soporte, recibo, extracto, contrato o acta. El soporte se archiva digital en `01-INSUMOS/SOPORTES/` con el número del comprobante en el nombre.
2. **Tercero real en cada línea.** NIT con dígito de verificación para personas jurídicas; cédula **sin** DV para personas naturales. Nunca `VARIOS`, nunca el NIT de la propia empresa como tercero de un gasto. El DV se calcula, no se copia (Aux 03; `herramientas/` lo valida).
3. **Plan de cuentas existente.** Ninguna cuenta nueva: son contabilidades en marcha y una cuenta nueva rompe comparativos, exógena y renta. Si no encuentras la cuenta, pregunta al contador.
4. **Fecha del documento, período correcto.** La factura del 31 se causa en el mes del 31 aunque llegue el 3.
5. **Concepto que se entiende solo.** `FV SETP-1234 · venta mercancía · CUFE …` y no `factura`. Prefijo y folio siempre, porque el cruce con el token se hace por folio.
6. **Retención bien calculada en el momento.** Base, tarifa y cuantía mínima según la tabla vigente y el RUT del tercero. Persona natural de servicios: primero el art. 383 (tabla de rentas de trabajo) y después el 6 % o 4 % (ver regla de la casa). La cuantía mínima se mide como diga la ficha del cliente: por operación diaria por proveedor (regla general de la firma) o por factura (si el contador lo fijó para ese cliente).
7. **IVA descontable con requisitos.** Factura electrónica válida a nombre del cliente, bien o servicio relacionado con la actividad, y los criterios particulares de la ficha (por ejemplo, IVA de compras menores como mayor valor del gasto).
8. **Sin compensaciones.** Un anticipo a un proveedor no se resta de lo que se le debe en la misma cuenta; un saldo a favor de IVA no se netea contra un pasivo (NIIF, prohibido compensar).
9. **Notas crédito y débito referenciadas.** Toda nota dice qué factura afecta; las devoluciones de venta afectan ingreso e IVA del período de la nota.
10. **Lo que no está claro se pregunta, no se supone.** Se anota en `NOTAS-Y-PENDIENTES.md` y se causa en una cuenta de paso **con nombre y fecha de cierre**, nunca en una cuenta genérica.

## 2. Comprobantes y qué causa cada uno

| Comprobante | Cuándo | Lección |
|---|---|---|
| Factura de venta (FV) | Cada factura electrónica emitida | Aux 05 |
| Factura de compra / causación de gasto (FC) | Cada factura recibida o documento soporte | Aux 06, Aux 10 |
| Recibo de caja (RC) | Cada recaudo: cruza contra la factura que paga | Aux 07 |
| Comprobante de egreso (CE) | Cada pago: cruza contra la factura que cancela | Aux 08 |
| Nota crédito / débito (NC/ND) | Devoluciones, descuentos, ajustes de precio | Aux 09 |
| Nómina (NM) | Cada período de pago, con provisiones | Aux 11–13 |
| Nota contable (NC) | Depreciaciones, provisiones, GMF, ajustes **aprobados** | Aux 12, Aux 16 |

## 3. Particularidades que más fallan

- **Pasarelas de pago y datáfonos** (plataformas de crédito, billeteras, adquirentes): la venta se causa por el bruto; la comisión, su IVA y las retenciones que practica la pasarela se causan aparte; lo que se abona al banco es el neto. La cuenta por cobrar a la pasarela **se abona** cuando llega el dinero: si nunca se abona, la conciliación está mal.
- **Caja**: cada salida con soporte; arqueo al cierre; la caja no puede quedar con saldo crédito.
- **Anticipos de clientes**: plata recibida sin factura va a la cuenta de anticipos (2805), no a ingresos, hasta que se facture.
- **Gastos del socio**: si hay gastos personales pagados por la empresa, se proponen como cuenta por cobrar al socio o no deducible; **se informan** al contador, no se esconden en un gasto.
- **Documento soporte a no obligados**: lo emite el cliente al comprarle a alguien que no factura; sin él, el gasto no es deducible.

## 4. Exportes del software (formato S y formato W)

El balance de prueba y el libro auxiliar se exportan en el formato del software del cliente. Al leerlos:

- Descarta las filas de **saldo inicial** como movimiento.
- En el libro auxiliar tipo W, descarta **toda fila cuya columna A empiece por `TOTAL`** antes de sumar: repiten los totales de la cuenta e incluyen el saldo inicial dentro de los débitos.
- Comprueba que débitos = créditos y que el total coincide con el balance de prueba **antes** de usar el archivo para cualquier cruce.
- Si el año anterior no se cerró en el software, trabaja con **movimientos del período**, nunca con saldos acumulados de cuentas de resultado.

## Relacionado

- [[Aux 01 - Plan de Cuentas PUC]] · [[Aux 03 - Terceros y RUT]] · [[Aux 14 - Calculo de Retenciones]] · [[Aux 15 - IVA y Prorrateo]]
- [[regla-no-crear-cuentas-nuevas]] · [[regla-retencion-pn-art-383]] · [[formato-siigo-exportes]] · [[05 - Conciliaciones]]
