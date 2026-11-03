---
name: causacion
description: Causa y digita documentos (facturas de venta y compra, documento soporte, recibos, egresos, notas, nómina, provisiones) con el plan de cuentas del cliente y las retenciones e IVA correctos. Úsala con "causa esta factura", "cómo registro…", "qué asiento lleva…", "digita los soportes de…".
---

# Causación y digitación

Para cada documento:

1. **Identifica:** tipo, tercero (NIT con DV correcto, persona natural o jurídica, responsabilidades del RUT), fecha,
   base, IVA, total. Siempre el tercero real, nunca uno genérico.
2. **Cuenta:** del plan de cuentas existente del cliente (balance de prueba). Si no hay cuenta adecuada, se pregunta al
   contador; no se crea.
3. **Retención:** concepto según el bien o servicio; persona natural que presta servicios → art. 383 primero;
   cuantía mínima por día y por proveedor (o por factura si la ficha lo dice); autorretención si el cliente es
   autorretenedor. Tarifas y UVT de `05-CONOCIMIENTO/normativa/VALORES-VIGENTES.md`.
4. **IVA:** descontable solo con factura electrónica válida y los requisitos de los arts. 771-2 y 488 E.T.; prorrateo
   si el cliente tiene ingresos excluidos (lección `Aux 15`); criterio particular de la ficha si existe.
5. **Asiento:** tabla `CUENTA · NOMBRE · TERCERO · DÉBITO · CRÉDITO · QUÉ REGISTRA · SOPORTE`, que cuadre y sea neto.
6. **Digitado o propuesto:** se digitan las causaciones normales; correcciones de meses anteriores, reclasificaciones y
   lo que toque socios, patrimonio o impuestos declarados va a `ASIENTOS_PROPUESTOS`.

Referencias: `02-MANUAL-DE-ENTREGA/04 - Digitacion y Causacion.md`, lecciones `Aux 05`–`Aux 17`,
`03-REGLAS-DE-LA-CASA/regla-retencion-pn-art-383.md` y `regla-no-crear-cuentas-nuevas.md`.
