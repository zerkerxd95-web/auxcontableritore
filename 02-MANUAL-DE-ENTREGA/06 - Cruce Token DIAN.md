---
tipo: manual
tags: [ritore, auxiliar, token, facturacion-electronica]
estado: vigente
version: 1.0
fecha: 2026-11-03
---

# 06 · Cruce del token DIAN

> **El token es la fuente de verdad.** Es lo que la DIAN ya sabe del cliente. Si una factura está en el token y no en la contabilidad, la DIAN la va a cruzar contra la declaración y la exógena del año. Por eso el cruce se hace **antes** de liquidar cualquier impuesto, todos los meses. La lección completa está en Aux 20 y Aux 21.

## 1. Qué se descarga

Del portal de facturación electrónica de la DIAN, para el mes: documentos **emitidos** (facturas de venta, notas crédito y débito, documento soporte, nómina electrónica) y **recibidos** (facturas de compra y sus notas). Se guarda en `01-INSUMOS/TOKEN_<AAAA-MM>.xlsx` tal como sale.

## 2. Cómo se cruza (documento por documento, en los dos sentidos)

1. **Token → libros.** Cada documento del token se busca en el auxiliar por **prefijo + folio** y por NIT. Si no está: factura sin causar (hallazgo con asiento).
2. **Libros → token.** Cada factura causada en libros se busca en el token. Si no está: o es un documento soporte o una factura no electrónica (se verifica que exista y sea válida), o es un gasto sin soporte válido (hallazgo: no deducible, sin IVA descontable).
3. **Valor.** Por documento, base, IVA y total. Hasta $200 de diferencia se acepta como redondeo; más de $200 se explica.
4. **Serie sin huecos.** Las facturas emitidas deben tener numeración continua; un hueco es una factura anulada que debe tener su nota o una factura que no se transmitió.
5. **Estado.** Documentos rechazados o anulados no se causan, pero se explican.

`herramientas/cruce_token.py` hace los pasos 1 a 4 y deja el resultado en `02-PROCESADO/01_CRUCE_TOKEN_<AAAA-MM>.xlsx`.

**Que el total cuadre no prueba nada.** Dos errores que se compensan dan el mismo total. El cruce se acepta solo cuando no queda ningún documento sin pareja.

## 3. Qué se lleva al resto del cierre

| Resultado del cruce | Va a |
|---|---|
| Facturas de venta sin causar | Asiento de causación; corrige ingresos, IVA generado y autorretención |
| Facturas de compra sin causar | Asiento de causación; revisar retención (si la base del día supera la cuantía, se retiene) e IVA descontable |
| Gastos en libros sin factura electrónica | Pendiente: pedir documento soporte o proponer como no deducible |
| Retenciones | El borrador del F-350 incluye **toda** factura del token que cumpla la base, esté o no causada; la no causada es además hallazgo contable |
| Notas crédito | Afectan el período de la nota, no el de la factura |

## 4. Falsas alarmas que no son error

- Honorarios de personas naturales que no facturan: no aparecen en el token porque van con **documento soporte**; se verifica que el documento soporte exista.
- Servicios públicos y bancos: a veces no aparecen en el token del mes por fechas de emisión; se verifican contra la factura física.
- Compras con fecha de emisión del último día del mes anterior causadas este mes: error de período, no de causación.

## Relacionado

- [[Aux 20 - Interpretacion del Token DIAN]] · [[Aux 21 - Cruce Token vs Contabilidad]] · [[regla-cruce-token-obligatorio]] · [[Plantilla 10 - Interpretacion Token DIAN]]
