---
tipo: plantilla
tags: [ritore, plantilla, token-dian, iva, exogena, facturacion-electronica]
archivo: Suite Excel Pro/10_Interpretacion_Token_DIAN.xlsx
estado: vigente
fecha: 2026-06-08
---
# Plantilla 10 - Interpretacion Token DIAN

> Plantilla **estrella** de la suite. *"De la correcta interpretación del Token DIAN se deriva toda la contabilidad, el IVA, las retenciones y la exógena."*

## Para qué sirve y a qué cliente (el servicio que habilita)
Convierte la **base de datos del Token DIAN** (todos los documentos electrónicos de la empresa: facturas de venta/compra, notas crédito, documentos soporte, nómina electrónica) en **información contable y tributaria lista para usar**: desglose base/IVA por documento, insumo del **Formato 300 de IVA** y **cruce contra la contabilidad**. Es base de datos + dashboard de venta + Power BI ready. Habilita los servicios de **liquidación de IVA (F-300)**, soporte de la **contabilización** y materia prima de la **exógena** (1001 ingresos/pagos, 1007, 2276). Frecuencia: mensual al recibir el token; consolidado bimestral/cuatrimestral para el F-300; anual para exógena. Moneda COP, UVT 2026 $52.374.

## Estructura del libro (hoja → capa → contenido)
| Hoja | Capa | Contenido |
|------|------|-----------|
| Instrucciones | Servicio | Qué es, capas, cómo se usa, **Reglas de oro de la firma**, normativa. |
| Guia Power BI | Servicio | Conexión de `BD_Token` como tabla de hechos; dimensiones y DAX con las reglas de oro. |
| Parametros | Parámetros | NIT empresa, periodo, periodicidad IVA, UVT, tarifas IVA, umbrales de semáforo. |
| BD_Token | Datos (hechos) | Tabla plana que replica las columnas del token. **Única hoja que se diligencia.** |
| Calc_Desglose | Cálculo | Aplica reglas de oro: Base=Total−IVA, clasifica venta/compra/DSEL/nómina, tarifa implícita, alerta 21%, cuenta PUC sugerida. |
| Calc_Resumen_IVA | Cálculo | Insumo del F-300: ventas/compras gravadas y exentas, liquidación IVA. |
| Calc_Cruce | Cálculo | Token vs contabilidad por concepto con semáforo de consistencia. |
| Dashboard | Presentación | Tarjetas KPI, gráficos por tipo de documento, semáforo de consistencia. |

## Modelo de datos (Power BI)
**Tabla de hechos: `BD_Token`** (rango `A4:P204`, una fila por documento electrónico). Replica las columnas reales del token DIAN:

| Columna | Significado | Tipo |
|---------|-------------|------|
| CUFE_CUDE | Código único del documento (CUFE factura / CUDE nota o soporte) — llave | Texto |
| Tipo_Documento | Factura de venta / Factura de compra / Nota credito / Documento soporte / Nomina | Texto (dimensión) |
| Grupo | **Emitido** (lo expide la empresa) / **Recibido** (lo recibe) | Texto (dimensión) |
| Folio_Prefijo | Prefijo y número (FV-1001, FC-5500, NC-201…) | Texto |
| NIT_Emisor | NIT de quien emite (sin DV) | Texto |
| NIT_Receptor | NIT de quien recibe | Texto |
| Razon_Social | Nombre del tercero | Texto |
| Fecha_Emision | Fecha de emisión | Fecha |
| Fecha_Recepcion | Fecha de recepción | Fecha |
| Total | **Valor total = base + IVA** (incluye el IVA) | Número (COP) |
| IVA | IVA real reportado en el documento | Número (COP) |
| INC | Impuesto Nacional al Consumo | Número (COP) |
| ReteFuente | Retención en la fuente | Número (COP) |
| ReteIVA | Retención de IVA | Número (COP) |
| ReteICA | Retención de ICA | Número (COP) |
| Tarifa_Reportada | Tarifa textual del documento (19%, 5%, Excluido, N/A) | Texto |

> En notas crédito el Total y el IVA van en **negativo** (se restan). En documento soporte de nómina/no obligado el IVA suele ser 0.

**Esquema estrella:** `BD_Token` es la única tabla de hechos. Dimensiones a crear en Power BI: Calendario (`CALENDAR`) ligada a `Fecha_Emision`; `Tipo_Documento`; `Grupo`; `Tercero` (NIT + Razon_Social) por relaciones 1:N. **Conexión:** Obtener datos → Excel → marcar la tabla `BD_Token` (las hojas `Calc_*` y `Dashboard` no se importan, se recrean como medidas). **DAX (replicando reglas de oro):**
- `Ventas = CALCULATE(SUM(Base), Grupo="Emitido")`
- `Compras = CALCULATE(SUM(Base), Grupo="Recibido")`
- `IVA Generado = CALCULATE(SUM(IVA), Grupo="Emitido")`
- `IVA Descontable = CALCULATE(SUM(IVA), Grupo="Recibido")`
- `IVA a Pagar = [IVA Generado] - [IVA Descontable]`
- En DAX: Base = Total − IVA; las NC se restan (signo negativo ya viene en los datos); el DSEL en "Emitido" cuenta como compra (usar la columna `Clasificacion` de `Calc_Desglose` como criterio). Relación `Calendario[Fecha] 1:N BD_Token[Fecha_Emision]`. Actualizar tras pegar nuevos documentos.

## Metodología y fórmulas clave

### REGLAS DE ORO DE LA FIRMA (memorizar)
1. **Base = Total − IVA.** La columna Total incluye base + IVA: siempre desglosar.
2. **NUNCA aplicar 19% plano.** Usar el IVA real por factura (5%, exento, excluido, tarifas mixtas).
3. **La tarifa 21% NO existe en Colombia.** Si IVA/Base ≈ 21% → ERROR, señalar y escalar.
4. **Emitido = ventas (IVA generado) · Recibido = compras (IVA descontable).**
5. **Un DSEL (documento soporte) emitido a un no obligado es COMPRA soporte, NO venta.**
6. **Las notas crédito se RESTAN** del total y del IVA (cifras netas).

### Calc_Desglose (aplica las reglas, una fila por documento)
- `Base = Total − IVA`.
- **Clasificacion** (lógica de fórmula): si el Tipo_Documento contiene "soporte" → **Compra (DSEL)**; si contiene "Nomina" → **Nomina**; si Grupo="Emitido" → **Venta**; si Grupo="Recibido" → **Compra**; en otro caso "Revisar". *(Así un DSEL emitido cae como compra, no como venta — regla 5.)*
- **Tarifa_Implicita** = IVA / Base.
- **Alerta_Tarifa:** si tarifa implícita ≈ 21% → "ERROR 21% - escalar"; si ≈ 19% o ≈ 5% o 0% → "OK"; resto → "Revisar tarifa".
- **Cuenta_PUC_Sugerida** según clasificación: Venta → `4135 / 240801 / 130505`; Compra → `143515 / 5x6x / 240802 / 220505`; Compra (DSEL) → `5x6x / 220505-2335`; Nomina → `5105-5205 / 2505`.

### Calc_Resumen_IVA (insumo Formato 300, cifras netas con NC restadas)
- **Ventas gravadas** (Clasificacion="Venta" y tarifa > 0): base e IVA generado.
- **Ventas exentas/excluidas** (Clasificacion="Venta" y tarifa 0).
- **TOTAL VENTAS** (ingresos del periodo, Emitido neto de NC).
- **Compras gravadas** (Clasificacion="Compra" + "Compra (DSEL)" con tarifa > 0): base (sin IVA, para casillas 50-57 del F-300) e IVA descontable.
- **Compras excluidas/DSEL** (tarifa 0).
- **TOTAL COMPRAS** (Recibido + DSEL).
- **Liquidación IVA:** IVA generado (= IVA de ventas) − IVA descontable (= IVA de compras) = **IVA a pagar** (negativo = saldo a favor).

> Recordar (criterio FYT): las casillas de compras del F-300 (50-57) llevan la **base sin IVA**, nunca el total con IVA. Las casillas de impuesto llevan el valor del IVA.

### Calc_Cruce (token vs contabilidad)
Compara, por concepto, lo que dice el token contra el movimiento contable del periodo (columna azul a diligenciar): Ventas (4135), IVA generado (240801), Compras (5x/6x/1435), IVA descontable (240802), Nómina electrónica (5105/5205). Para cada uno: `Diferencia = token − contabilidad`, `% Dif` y semáforo. **Regla de oro del cruce: la contabilidad se ajusta al token, no al revés**; si difieren, la hipótesis es que la contabilidad está incompleta o errada.

## Cómo usarla (paso a paso)
1. Descargue el token de la DIAN (Excel; descomprima si viene en `.zip`).
2. Pegue los documentos en **BD_Token** respetando las columnas (única hoja que se diligencia, celdas azules/crema a reemplazar).
3. Complete **Parametros**: NIT de la empresa (define quién es Emisor), año gravable, periodo, **periodicidad IVA (Bimestral/Cuatrimestral — confirmar por cliente)**, UVT y umbrales.
4. Lea **Calc_Desglose** (revisa clasificación y alertas de tarifa), **Calc_Resumen_IVA** (insumo F-300), **Calc_Cruce** (diligencie el movimiento contable y revise el semáforo) y el **Dashboard**.

## Interpretación del dashboard
- **Tarjetas KPI:** Total Ventas, Total Compras, IVA Generado, IVA Descontable, **IVA a Pagar** (generado − descontable; negativo = saldo a favor), # Documentos.
- **Gráfico por tipo de documento:** conteo de Facturas de venta, Facturas de compra, Notas crédito, etc.
- **Semáforo de consistencia (token vs contabilidad)**, regla por umbrales de Parametros:
  - **OK** si diferencia ≤ 0,5% → "token y contabilidad cuadran".
  - **REVISAR** (ámbar) si ≤ 2% → "diferencias a explicar".
  - **CRÍTICO** (rojo) si > 2% → "inconsistencias materiales". El estado global toma el peor semáforo de los conceptos cruzados.

## Errores comunes / controles
- **Aplicar 19% plano sobre el total:** mata el desglose; usar el IVA real por documento (hay 5%, exentos, excluidos, mixtas — frecuente en sector bicicletas).
- **Tarifa 21%:** no existe en Colombia; la columna Alerta_Tarifa la marca como ERROR → señalar y escalar, es un error del emisor.
- **Poner el total con IVA en las casillas de base del F-300:** error ya cometido y corregido en campañas reales; las casillas de compras llevan base sin IVA.
- **Tratar un DSEL emitido a no obligado como venta:** es compra soporte; la clasificación lo corrige, pero verificar al cargar manualmente.
- **No restar las notas crédito:** deben venir en negativo en Total e IVA (cifras netas).
- **Archivo .xlsx abierto/sincronizado:** si el token llega corrupto (BadZipFile), pedir "Guardar como" con nombre nuevo; no reintentar en bucle.
- **Año contable sin cerrar:** trabajar con movimientos del periodo, no con saldos acumulados; declarar como hallazgo sin frenar la liquidación.
- **Periodicidad IVA:** confirmar siempre por cliente (Bimestral vs Cuatrimestral); no asumir.

## Relacionado
*MOC - Plantillas Pro* · *Estandar de Plantillas FYT* · [[Aux 20 - Interpretacion del Token DIAN]] · [[Protocolo IVA Formulario 300]] · [[04-AuxiliarFacturacionElectronica-Senior]]
