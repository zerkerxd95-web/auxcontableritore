---
tipo: leccion
tags: [ritore, escuela, auxiliar, token-dian]
modulo: 6
estado: vigente
fecha: 2026-06-08
---

# Aux 20 - Interpretación del Token DIAN ⭐

> **Esta es la lección más importante de toda la Escuela.** Según el dueño de la firma, de la correcta interpretación del Token DIAN se deriva la correcta elaboración de los estados financieros y de toda la contabilidad. Si dominas esta lección, todo lo demás —causación, IVA, retenciones, exógena, cierres— se vuelve consecuencia natural. Si la fallas, todo lo que construyas encima estará torcido.

## Objetivo

Que el auxiliar sea capaz de descargar, depurar, leer e interpretar la base de documentos electrónicos del Token DIAN de cualquier cliente, clasificar cada documento con su tratamiento contable correcto, desglosar base e IVA con las tarifas reales, y convertir esa base en contabilidad verificable contra el balance.

## Marco conceptual y normativo

### Qué es el Token DIAN

El **Token DIAN** es el mecanismo de acceso al portal de facturación electrónica de la DIAN con el que se descarga, mes a mes, la **base de datos de TODOS los documentos electrónicos de la empresa**:

- Facturas de venta **emitidas** por el cliente.
- Facturas de compra **recibidas** de sus proveedores.
- **Notas crédito y débito** (emitidas y recibidas).
- **Documentos soporte** (DSEL) emitidos a proveedores no obligados a facturar.
- **Nómina electrónica** y sus notas de ajuste.
- Documentos equivalentes (POS, tiquetes).

### Por qué es la FUENTE DE VERDAD

En Colombia la facturación electrónica es la fuente fiscal de verdad: **lo que la DIAN ve, así es como ve a la empresa** ([[04-AuxiliarFacturacionElectronica-Senior]]). De ahí se derivan tres consecuencias prácticas:

1. **La contabilidad se ajusta al token, no al revés** (regla D.1 del [[Protocolo IVA Formulario 300]]). Si el libro auxiliar dice una cosa y el token dice otra, la hipótesis de trabajo es que la contabilidad está incompleta o errada.
2. Lo que no está facturado electrónicamente **no es deducible** (Art. 771-2 ET): una factura rechazada por la DIAN no es soporte de costo ni de IVA descontable.
3. La DIAN cruza automáticamente el token contra el F-300 (IVA), el F-350 (retenciones), el F-110 (renta) y la exógena. Cada inconsistencia es un requerimiento potencial.

### Normas que debes conocer

| Norma | Qué regula |
|-------|-----------|
| Art. 615, 616-1, 617 ET | Obligación de facturar, factura electrónica y sus requisitos |
| Art. 618 ET | Obligación de exigir factura |
| Art. 771-2 ET | Procedencia de costos, deducciones e IVA descontable (factura validada) |
| Art. 496 ET | Oportunidad del IVA descontable (ver "Casos especiales") |
| Decreto 358/2020, Res. DIAN 000042/2020 y 000165/2023 | Sistema de facturación electrónica con validación previa |

## Paso a paso

### 1. Descarga y recepción

- La base llega como **archivo Excel**, a veces comprimida en un **.zip** (descomprimir primero).
- Suele venir separada en archivos o pestañas **ENVIADOS / EMITIDOS** (documentos donde el cliente es emisor) y **RECIBIDOS** (donde es receptor); otras veces en un solo archivo con la columna `Grupo`.
- Antes de procesar, aplica la regla C.1 de *Lecciones Aprendidas Exogena*: si el archivo da `BadZipFile` o viene truncado (típico en carpetas OneDrive/Drive abiertas en Excel), NO reintentar en bucle — pedir cerrarlo o "Guardar como" con nombre nuevo.

### 2. Anatomía de la base — columnas clave

| Columna | Qué es | Cómo leerla |
|---------|--------|-------------|
| **CUFE / CUDE** | Código único del documento (CUFE = facturas; CUDE = NC/ND, DSEL, nómina) | Identificador irrepetible: úsalo para detectar duplicados |
| **Tipo de documento** | Factura de venta, NC, ND, documento soporte, nómina, etc. | Define el tratamiento contable (ver tabla siguiente) |
| **Folio / Prefijo** | Numeración del documento | Verificar consecutivos y rangos autorizados |
| **NIT emisor** | Quién expide el documento | En `Recibido`, es el proveedor; en `Emitido`, debe ser el NIT del cliente |
| **NIT receptor** | A quién va dirigido | En `Recibido` DEBE ser el NIT del cliente — si no, el documento NO es de la empresa |
| **Fecha de emisión** | Fecha del documento | Define el periodo del ingreso/costo |
| **Fecha de recepción/validación** | Cuándo lo validó la DIAN o lo recibió el cliente | Relevante para documentos que llegan tarde |
| **Grupo** | `Emitido` o `Recibido` | **`Emitido` = ventas · `Recibido` = compras** (con la excepción del DSEL, ver reglas de oro) |
| **Total** | Valor total del documento | **INCLUYE base + IVA**: nunca lo uses como base |
| **IVA** | IVA real del documento | Es el IVA reportado factura a factura — la única fuente válida de IVA |
| **INC** | Impuesto nacional al consumo | Va aparte del IVA; en compras es mayor valor del gasto |
| **Retenciones** (ReteFuente/ReteIVA/ReteICA) | Retenciones informadas en el documento | Referencia para cuadrar 2365/1355; la cifra definitiva es la contable |

### 3. REGLAS DE ORO de la firma (memorizar — Protocolo D)

1. **`Base = Total − IVA`.** La columna `Total` incluye base + IVA. Siempre desglosar antes de contabilizar o liquidar.
2. **NUNCA aplicar 19 % plano.** Usar el IVA real reportado por factura: existen tarifas del 5 %, bienes exentos, excluidos y facturas con **tarifas mixtas** (frecuentes en el sector bicicletas — **Cliente - COMERCIO DE BICICLETAS A**).
3. **La tarifa del 21 % NO existe en Colombia.** Si `IVA/Base` da 21 % (u otra tarifa inexistente), es un error del documento: señalar, no descontar a ciegas.
4. **`Emitido` = ventas (IVA generado) · `Recibido` = compras (IVA descontable).**
5. **Un DSEL emitido a un no obligado es COMPRA soporte, NO venta**, aunque aparezca en `Emitido`. Excepción clave de la regla 4.
6. **Las notas crédito se RESTAN** del total y del IVA para obtener cifras netas en liquidaciones de IVA (en exógena 1005/1006 van en columna propia — regla C.5).

**Ejemplo numérico del desglose:**

| Factura | Total (token) | IVA (token) | Base = Total − IVA | Tarifa implícita |
|---------|--------------:|------------:|-------------------:|------------------|
| FV-1001 | 1.190.000 | 190.000 | 1.000.000 | 19 % ✔ |
| FV-1002 | 2.100.000 | 100.000 | 2.000.000 | 5 % ✔ (NO era 19 %) |
| FV-1003 | 1.560.000 | 60.000 | 1.500.000 | 4 % → tarifa MIXTA (parte exenta + parte 19 %): revisar el XML, no asumir |
| FV-1004 | 1.210.000 | 210.000 | 1.000.000 | 21 % ✘ → ERROR, escalar |

### 4. Clasificación documento por documento

| Tipo de documento (código DIAN) | Grupo típico | Tratamiento contable | Cuenta PUC sugerida |
|--------------------------------|--------------|----------------------|---------------------|
| Factura de venta (01) | Emitido | Ingreso + IVA generado | DB 130505 / CR 4135xx / CR 240801 |
| Factura de exportación (02) | Emitido | Ingreso exento, IVA $0 | DB 130505 / CR 4135xx |
| Factura recibida (01 del proveedor) | Recibido | Inventario, activo o gasto + IVA descontable | DB 1435xx-15xxxx-5xxxx-6xxxx / DB 240802 / CR 220505 |
| Nota crédito (91) emitida | Emitido | Devolución en ventas, reversa IVA generado | DB 4175xx / DB 240801 / CR 130505 |
| Nota crédito (91) recibida | Recibido | Devolución en compras, reversa IVA descontable | DB 220505 / CR 1435xx-5xxxx / CR 240802 |
| Nota débito (92) | Según emisor | Mayor ingreso (emitida) o mayor costo (recibida) | Como factura origen |
| Documento soporte DSEL (05) | Aparece en Emitido | **COMPRA** a no obligado a facturar — NO es venta | DB 5xxxx-6xxxx / CR 220505-2335 |
| Factura POS (20) | Emitido | Venta (verificar si además hay factura electrónica para no duplicar) | DB 1105/130505 / CR 4135xx / CR 240801 |
| Nómina electrónica (102) | Emitido | Gasto laboral — cruza contra la nómina causada, no se causa desde el token | 5105/5205/7205 (verificación) |
| Nota de ajuste de nómina (103) | Emitido | Ajuste al documento 102 | ídem |

### 5. De token a contabilidad — flujo completo

```
1. DESCARGAR    → Excel del token (mes completo), descomprimir si .zip.
2. DEPURAR      → quitar duplicados por CUFE; verificar NIT receptor en Recibidos;
                  separar DSEL de las ventas; identificar anulados (NC asociada).
3. CLASIFICAR   → por Grupo y tipo de documento (tabla anterior).
4. DESGLOSAR    → Base = Total − IVA, factura por factura, con la tarifa real.
5. CAUSAR       → asiento por lote (un comprobante resumen por tipo y tarifa) o
                  individual (clientes con pocos documentos o multi-ítem).
6. VERIFICAR    → ventas del token = movimiento crédito 4135 del mes;
                  IVA del token = movimiento 240801/240802; compras = 1435/5x/6x.
```

**Ejemplo de asiento por lote (ventas del mes, tarifa 19 %):**

```
DB 130505 Clientes nacionales        11.900.000
   CR 413550 Ingresos por servicios              10.000.000
   CR 240801 IVA generado 19 %                    1.900.000
```

## Casos especiales reales

- **Facturas recibidas que NO son de la empresa:** verificar SIEMPRE que el NIT receptor sea el del cliente. A los tokens llegan a veces documentos dirigidos a terceros (errores del proveedor al facturar). No se contabilizan; se notifica al proveedor para anulación.
- **Compras de socios por reembolsar:** facturas a nombre de la empresa pagadas por el socio con su tarjeta personal. Se causan normal (gasto + IVA si procede) con contrapartida CxP al socio (2355), no contra bancos. Si la factura está a nombre del socio (persona natural), NO es deducible para la empresa.
- **Facturas anuladas con nota crédito:** una FV con NC posterior por el 100 % es una anulación: el neto es cero. Contabilizar ambas o ninguna, pero nunca solo la factura. Detectarlas cruzando la NC con su CUFE de referencia.
- **Documentos de meses anteriores que llegan tarde:** distinguir **fecha de emisión** (periodo del costo/gasto) de **fecha de recepción**. Para el IVA descontable, el Art. 496 ET permite contabilizar el descontable en el periodo de causación **o en uno de los tres periodos bimestrales inmediatamente siguientes** (declarantes bimestrales) o **en el periodo cuatrimestral inmediatamente siguiente** (declarantes cuatrimestrales), y solicitarlo en la declaración del periodo en que se contabilizó (texto vigente, Art. 194 Ley 1819/2016). Pasado ese plazo, el derecho al descuento se pierde.
- **Duplicados:** un mismo CUFE dos veces en la base (re-descargas, archivos superpuestos). Deduplicar SIEMPRE por CUFE antes de sumar.
- **POS + factura electrónica del mismo hecho:** algunas ventas aparecen dos veces (tiquete POS y factura). Verificar y contar una sola vez.

## Por qué esta habilidad domina los EEFF

Si el token está bien interpretado, **toda la cadena aguas abajo cuadra sola**:

| Token bien leído | Cuadra contra | Producto final |
|------------------|---------------|----------------|
| Ventas (Emitido, netas de NC) | Crédito 4135 + 240801 | Estado de Resultados confiable y F-300 |
| Compras (Recibido + DSEL) | 1435/5x/6x + 240802 | Costo y gasto reales, IVA descontable |
| Nómina electrónica | 5105/5205/2505 | Gasto laboral completo |
| Ventas anuales del token | **Formato 1007** de exógena | Exógena "sale sola" |
| Compras anuales del token | **Formato 1001** de exógena | ídem |
| Nómina electrónica anual | **Formato 2276** | ídem |

Por eso el dueño insiste: la exógena, la renta y los EEFF no se "construyen" a fin de año — **se derivan** de un token bien interpretado mes a mes.

## Errores comunes (casos reales FYT)

| Error | Caso real | Prevención |
|-------|-----------|------------|
| Aplicar 19 % plano a todas las compras | Sector bicicletas con tarifas 5 %/exentas/mixtas (**Cliente - COMERCIO DE BICICLETAS A**) | Usar el IVA real por factura, siempre |
| Poner el Total (con IVA) como base | Error cometido y corregido en casillas 50-57 del F-300 (regla D.4) | Desglosar Base = Total − IVA antes de cualquier uso |
| Tratar un DSEL como venta | DSEL aparece en `Emitido` y se suma a ingresos | Separar DSEL en la depuración (paso 2) |
| Descontar IVA de tarifa inexistente (21 %) | Regla D.2 — documento con error | Señalar y escalar; no descontar a ciegas |
| No restar notas crédito | Ventas e IVA generados inflados | Cifras netas en liquidación (en 1005/1006 columna propia) |
| Procesar un Excel corrupto en bucle | `BadZipFile` por OneDrive (regla C.1) | Pedir cerrar / "Guardar como"; verificar firma EOCD |
| Trabajar con saldos acumulados de 41xx/2408 en año sin cerrar | Patrón recurrente (regla D.5) | Trabajar con MOVIMIENTOS del periodo; excluir "SALDO INICIAL" |

## Checklist de calidad

- [ ] Archivo íntegro (abre sin `BadZipFile`; si venía en .zip, descomprimido completo).
- [ ] Duplicados eliminados por CUFE/CUDE.
- [ ] NIT receptor verificado en todos los `Recibido` (solo documentos de la empresa).
- [ ] DSEL separados de las ventas y tratados como compras.
- [ ] Base = Total − IVA aplicado factura por factura (sin 19 % plano).
- [ ] Tarifas implícitas razonables (0 %, 5 %, 19 %); las atípicas investigadas, 21 % escalado.
- [ ] Notas crédito identificadas y aplicadas (netas en liquidación).
- [ ] Anulaciones (FV + NC 100 %) tratadas en pareja.
- [ ] Documentos extemporáneos asignados al periodo correcto (Art. 496 ET para el descontable).
- [ ] Totales del token verificados contra movimientos contables del mes (4135, 240801, 240802, compras).

## Relacionado

- Lección anterior: [[Aux 19 - Estado del Costo]] · Lección siguiente: [[Aux 21 - Cruce Token vs Contabilidad]]
- Fundamentos: [[Aux 05 - Causacion de Facturas de Venta]] · [[Aux 06 - Causacion de Facturas de Compra y Gastos]] · [[Aux 09 - Notas Credito y Debito]] · [[Aux 10 - Documento Soporte a No Obligados]] · [[Aux 13 - Nomina Electronica y Documento Soporte de Pago]] · [[Aux 15 - IVA y Prorrateo]]
- Conocimiento de la firma: [[Protocolo IVA Formulario 300]] · *Lecciones Aprendidas Exogena*
- Agentes: [[04-AuxiliarFacturacionElectronica-Senior]] · [[02-AuxiliarContable-Senior]] · *11-EspecialistaIVA-Master*
- [[MOC - Escuela Auxiliar Contable]]
