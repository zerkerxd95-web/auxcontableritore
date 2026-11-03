---
tipo: leccion
tags: [ritore, escuela, auxiliar, notas-credito, iva]
modulo: 2
estado: vigente
fecha: 2026-06-08
---
# Aux 09 - Notas Credito y Debito

## Objetivo
El auxiliar sabrá contabilizar notas crédito y débito emitidas y recibidas, entender su efecto en el IVA, y aplicar la doble regla de la firma: en la **liquidación del F-300 las notas se netean** (regla D.3), pero en los **formatos 1005/1006 de exógena van en columna propia, NO se restan**.

## Marco conceptual y normativo
- **Nota crédito (emitida):** documento electrónico que DISMINUYE una factura de venta — devoluciones, anulaciones, rebajas o descuentos posteriores (Art. 484 ET permite restar del IVA generado el impuesto de operaciones anuladas, rescindidas o resueltas).
- **Nota débito (emitida):** AUMENTA el valor de una factura ya emitida (intereses, fletes, mayor valor facturado por error en menos).
- Recibidas funcionan en espejo: una nota crédito de nuestro proveedor disminuye nuestra compra y nuestro IVA descontable (Art. 486 ET).
- **Son documentos electrónicos DIAN:** llevan CUDE, numeración electrónica propia y SIEMPRE referencian la factura afectada. Aparecen en el token DIAN y deben cruzar con ella ([[Aux 20 - Interpretacion del Token DIAN]]).

## Paso a paso

1. Identifica el tipo (NC/ND), si es emitida o recibida y la **factura que afecta**.
2. Verifica que la nota esté validada DIAN y tenga la referencia a la factura original.
3. Contabiliza en espejo de la factura afectada, con el mismo tercero.
4. Marca el efecto en IVA del periodo.
5. Registra el efecto en cartera/CxP (el saldo de la factura cambia).

### Asientos modelo

**1. Nota crédito EMITIDA — devolución en venta.** Habíamos facturado $1.000.000 + IVA 19%; el cliente devuelve la mitad:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 417501 | Devoluciones en ventas (DB) | 500.000 | |
| 240801 | IVA generado (reversión) | 95.000 | |
| 130505 | Clientes nacionales | | 595.000 |

*Se usa 4175 (cuenta débito de la clase 4) en lugar de debitar 4135: así el bruto y las devoluciones quedan trazables por separado — exactamente lo que piden los formatos de exógena.*

**2. Nota crédito RECIBIDA — devolución en compra.** Devolvemos al proveedor mercancía por $800.000 + IVA:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 220505 | Proveedores nacionales | 952.000 | |
| 143505 | Mercancías no fabricadas por la empresa | | 800.000 |
| 240802 | IVA descontable (reversión) | | 152.000 |

**3. Nota débito EMITIDA — intereses de mora al cliente** $100.000 (no gravados en este ejemplo):

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 130505 | Clientes nacionales | 100.000 | |
| 421005 | Ingresos financieros — intereses | | 100.000 |

### El efecto en IVA: dos reglas que conviven
| Contexto | Tratamiento de las notas crédito |
|---|---|
| **Liquidación F-300** (regla D.3) | Se **RESTAN**: ventas e IVA se declaran en cifras netas de notas |
| **Exógena F-1005/1006** (regla C.5, *Formato 1005 y 1006 - IVA*) | **NO se restan**: van en columna propia — 1005: "IVA devolución en ventas"; 1006: "IVA recuperado en devoluciones en compras". Ambos formatos cruzan compras y ventas |

Memorízalo así: **la declaración quiere el neto; la exógena quiere el detalle**.

## Errores comunes
- **Restar las notas crédito en los formatos 1005/1006:** error clásico que el prevalidador no detecta pero el cruce DIAN sí — la regla de la firma es columna propia (lección de campañas reales, ver *Lecciones Aprendidas Exogena*).
- **No netearlas en el F-300:** infla ventas e IVA del periodo y descuadra el cruce token vs contabilidad (regla D.3: "las notas crédito se RESTAN del total y del IVA — cifras netas").
- **Emitir nota crédito sin referencia a la factura original:** la DIAN la valida pero el cruce interno queda cojo; toda nota referencia su factura.
- **Usar nota crédito para "borrar" cartera incobrable o descuentos por pronto pago:** lo primero es deterioro/castigo de cartera; lo segundo es gasto 530535 ([[Aux 07 - Recibos de Caja]]). La nota crédito reversa la VENTA, no maquilla saldos.
- **Contabilizar la devolución debitando directamente la 4135:** se pierde la trazabilidad bruto/devoluciones que piden renta y exógena — usar 4175.
- **Olvidar el efecto en retenciones:** si el cliente nos retuvo sobre la factura original y la operación se anula, el ajuste de la retención debe gestionarse (certificados/reintegro), no ignorarse.

## Checklist de calidad
1. ¿La nota está validada DIAN (CUDE) y aparece en el token?
2. ¿Referencia correctamente la factura afectada y al mismo tercero?
3. ¿Asiento en espejo correcto (4175/2408 emitidas; 2205/2408 recibidas)?
4. ¿El saldo de cartera/CxP de la factura quedó ajustado?
5. ¿En la liquidación de IVA del periodo las notas quedaron NETEADAS?
6. ¿En los papeles de exógena las notas quedaron en COLUMNA PROPIA (sin restar)?
7. ¿Devoluciones del periodo razonables vs ventas (una explosión de NC es bandera roja)?

## Relacionado
- Anterior: [[Aux 08 - Comprobantes de Egreso]] · Siguiente: [[Aux 10 - Documento Soporte a No Obligados]]
- [[MOC - Escuela Auxiliar Contable]] · [[02-AuxiliarContable-Senior]]
- *Formato 1005 y 1006 - IVA* · [[Protocolo IVA Formulario 300]] · [[Aux 15 - IVA y Prorrateo]] · [[Aux 20 - Interpretacion del Token DIAN]]
