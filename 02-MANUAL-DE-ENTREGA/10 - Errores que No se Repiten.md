---
tipo: leccion
tags: [ritore, auxiliar, errores, calidad]
estado: vigente
version: 1.0
fecha: 2026-11-03
---

# 10 · Errores que no se repiten

Errores reales que costaron reprocesos en la firma. Cada uno trae la regla que lo evita. Antes de entregar, repasa esta lista: si te reconoces en alguno, corrígelo antes de que lo encuentre el contador.

| # | Error | Qué costó | Regla que lo evita |
|---|---|---|---|
| 1 | Entregar un **diagnóstico** en vez de una auditoría de cierre ("encontré estas diferencias") | Cinco versiones sucesivas del mismo cierre | El auxiliar digita asientos, no hallazgos. Toda diferencia sale con asiento propuesto y prueba de cierre en cero, mes a mes |
| 2 | Cuadrar el token **por el total** de las facturas emitidas | Facturas sin causar escondidas detrás de dos errores que se compensaban | Cruce documento por documento, en los dos sentidos, y serie sin huecos |
| 3 | Liquidar retención **solo con la contabilidad** | Dos informes de retención rechazados | El F-350 incluye toda factura del token que cumpla la base |
| 4 | Medir la cuantía mínima de retención **por mes** por proveedor | Retenciones de menos | Por operación diaria por proveedor, o por factura si la ficha lo dice |
| 5 | Reportar "faltantes" en bancos sin agotar los cruces uno a varios | Hallazgos falsos que el contador tuvo que deshacer | Tres capas de cruce; las diferencias reales deben sumar la diferencia de saldos al centavo |
| 6 | Sumar el libro auxiliar W **con las filas TOTAL** | Débitos 5 veces mayores que los reales; nada amarraba | Descartar las filas que empiezan por `TOTAL` y comprobar D = C contra el balance de prueba |
| 7 | Tratar el **saldo inicial** como movimiento | Descuadres en todos los cruces | Trabajar por movimientos del período |
| 8 | Cuadrar IVA contra el saldo acumulado de 2408 con el **año anterior sin cerrar** | IVA del período inflado | Movimientos del período, siempre |
| 9 | **Cédula con dígito de verificación** o NIT sin DV | La exógena revienta en el prevalidador | Cédula sin DV; NIT con DV calculado |
| 10 | Terceros **VARIOS** "por afán de cerrar" | La exógena del año siguiente lo cobra con intereses | Tercero real o pendiente documentado |
| 11 | **Pasarelas** sin conciliar "porque no son bancos" | Ventas cobradas que nunca se abonaron a la cuenta por cobrar | Cada pasarela se concilia como una cuenta bancaria |
| 12 | Crear **cuentas contables nuevas** | Comparativos rotos y exógena mal mapeada | Plan de cuentas existente; si no encuentras la cuenta, pregunta |
| 13 | Archivos `v2`, `FINAL`, `(LIMPIA)` | Nadie sabía cuál era la versión buena | Nombre canónico; la versión anterior va a `04-TRAZAS/` |
| 14 | Corregir **a mano** una salida (el Excel del informe) en vez del origen | La siguiente corrida borró la corrección | Se corrige en el software, se re-exporta y se rehace |
| 15 | Mezclar **dos clientes o dos contribuyentes** en una misma respuesta | Cifras de una persona en el expediente de otra | La carpeta que te asignan fija el expediente; si no está claro cuál es, pregunta antes de calcular |
| 16 | Formato de moneda `#,##0` en ajustes pequeños | Asientos de centavos que se veían en cero | Formato `#,##0.##`; nunca redondear un ajuste a cero |
| 17 | Editar un Excel abierto en una carpeta sincronizada | Archivo dañado (`BadZipFile`) | Cerrar, "Guardar como" una copia local, trabajar sobre ella |
| 18 | Dejar los **pendientes en la cabeza** | El mes siguiente nadie sabía qué quedó abierto | `NOTAS-Y-PENDIENTES.md` con valor, responsable y fecha |

## Regla del 3

Lo que corriges dos veces se documenta como lección (`05-CONOCIMIENTO/mejora-continua/Plantilla - Leccion Aprendida.md`). A la tercera vez se cambia el procedimiento, no se vuelve a corregir a mano.

## Relacionado

- [[Registro de Errores Recurrentes]] · [[Aux 25 - Cierre Anual y Errores Comunes]] · [[regla-auditoria-garantia-de-cierre]] · [[Manejo de Archivos Excel Corruptos]]
