---
name: cruce-token
description: Cruce del token DIAN (documentos electrónicos emitidos y recibidos) contra la contabilidad documento por documento, en los dos sentidos, con tolerancia de $200 y control de huecos en la serie. Úsala con "cruza el token", "revisa la facturación electrónica", "qué facturas faltan por causar".
---

# Cruce del token DIAN

1. Descarga del token del mes completo (emitidos y recibidos) → `01-INSUMOS/TOKEN_<AAAA-MM>.xlsx`.
2. Tabla de libros: una fila por documento causado (documento con prefijo y folio, fecha, NIT, total). Sirve el
   reporte de comprobantes del software o un resumen del auxiliar por documento.
3. Ejecuta:
   ```bash
   python herramientas/cruce_token.py --token "01-INSUMOS/TOKEN_<AAAA-MM>.xlsx" --libro "DOCS_<AAAA-MM>.xlsx" --nit-empresa <NIT sin DV> --salida "02-PROCESADO/01_CRUCE_TOKEN_<AAAA-MM>.xlsx"
   ```
4. Resuelve cada hoja del resultado: *EN TOKEN NO EN LIBROS* (causar), *EN LIBROS NO EN TOKEN* (soporte válido o
   decisión del contador), *DIFERENCIAS DE VALOR* (más de $200: revisar el XML y corregir en el software),
   *SERIE SIN HUECOS* (pedir la factura o la anulación).
5. Re-exporta y vuelve a correr hasta que lo pendiente esté explicado; anota cada corrida.
6. Lleva al resto del cierre: facturas con retención (todas deben estar en el F-350), IVA generado y descontable del
   token y cifras para `ENTREGA.md §2`.

Detalle: `02-MANUAL-DE-ENTREGA/06 - Cruce Token DIAN.md`, `01-ESCUELA/Aux 20` y `Aux 21`.
