---
tipo: conocimiento
tags: [ritore, conocimiento, estatuto-tributario, iva]
estado: vigente
fecha: 2026-06-08
---

# ET - IVA · Artículos Clave

Artículos del Libro Tercero (420-513) y conexos de facturación que sustentan la liquidación del F-300 y los formatos exógenos 1005/1006. Complementa el [[Protocolo IVA Formulario 300]] (reglas operativas D.1-D.10) y [[Aux 15 - IVA y Prorrateo]]. Valores con **UVT 2026 = $52.374**. Recordatorio operativo: **la tarifa del 21 % NO existe en Colombia** — si aparece en un archivo, es error (regla D.2).

## Hecho generador, responsables y retención de IVA

| Artículo | Regla esencial | Uso en la firma |
|---|---|---|
| **420** | Hecho generador: (a) venta de bienes corporales muebles e inmuebles no excluidos —la venta de inmuebles está excluida por el Art. 424—; (b) venta o cesión de intangibles de propiedad industrial; (c) prestación de servicios en Colombia o desde el exterior; (d) importación; (e) circulación/venta/operación de juegos de suerte y azar (salvo loterías). | Punto de partida para decidir si una operación del cliente genera IVA. |
| **424** | Bienes **excluidos**: no causan IVA y NO dan derecho a descontables (el IVA pagado es mayor costo). Lista taxativa (animales vivos, vegetales frescos, medicamentos, venta de inmuebles, etc.). | Sector bicicletas (COMERCIO DE BICICLETAS A): mezclar excluidos/exentos/gravados obliga a revisar producto por producto (regla D.7). |
| **437** | Responsables del IVA: comerciantes, importadores, prestadores de servicios. Par. 3: PN **no responsables** si ingresos brutos gravados del año anterior < 3.500 UVT ($183.309.000 con UVT 2026; se mide con la UVT del año anterior), un solo establecimiento, sin franquicia, consignaciones y contratos bajo topes. | Verificar la calidad de responsable en el RUT de cada cliente antes de liquidar. |
| **437-1** | **ReteIVA**: retención del 15 % del IVA causado (el reglamento puede llevarla hasta el 50 %); 100 % en servicios prestados desde el exterior. | Cuentas 2367/135517 de los clientes; cruce con el F-1003 concepto 1309. |
| **437-2** | Agentes de ReteIVA: entidades estatales, grandes contribuyentes, designados por la DIAN, quienes contraten con no residentes (retienen 100 %), emisores de tarjetas, y prestadores de servicios electrónicos/digitales del exterior (num. 8 — origen de los conceptos 5080-5085 del F-1001). | Determinar si el cliente debe retener IVA y a quién. |

## Tarifas, excluidos y exentos

| Artículo | Regla esencial | Uso en la firma |
|---|---|---|
| **468** | Tarifa general: **19 %**. | Tarifa por defecto, pero NUNCA aplicar 19 % plano al Token DIAN: usar el IVA real por factura (regla D.2). |
| **468-1** | Bienes a la tarifa del **5 %** (lista taxativa: insumos y productos agro, maíz y arroz industrial, aceites, y **bicicletas, bicicletas y motos eléctricas, patines y patinetas de valor ≤ 50 UVT** ≈ $2.618.700). | Clave para COMERCIO DE BICICLETAS A: tarifas mixtas 19 %/5 %/excluido en el mismo cliente. |
| **468-3** | Servicios al **5 %** (medicina prepagada y pólizas de salud, almacenamiento de productos agrícolas, etc.). | Verificación de tarifa en compras de servicios. |
| **476** | Servicios **excluidos**: salud humana, educación, transporte público de pasajeros y transporte de carga, arrendamiento de vivienda, servicios públicos domiciliarios, intereses de créditos de vivienda, entre otros. | Compras sin IVA legítimas: no buscar IVA descontable donde no lo hay. |
| **477** | Bienes **exentos** (tarifa 0 % con derecho a impuestos descontables para el productor): carnes, pescado, leche, huevos, etc. | Diferencia clave excluido (sin descontable) vs exento (con descontable). |
| **481** | Exentos **con derecho a devolución bimestral**: exportaciones de bienes y servicios, servicios turísticos a no residentes, ventas a sociedades de comercialización internacional, libros. El exportador factura exento, IVA generado $0 y descontable 100 % imputable sin prorrateo (regla D.7). | Régimen de EXPORTADORA DE SERVICIOS B (exportador). Detalle en *Art 481 ET - Exportadores*. |

## Impuestos descontables

| Artículo | Regla esencial | Uso en la firma |
|---|---|---|
| **485** | Descontable: el IVA facturado en compras de bienes y servicios y el pagado en importaciones, hasta el 100 % aunque la tarifa de la compra supere la de la venta. | Hoja "IVA Descontable" del entregable F-300. |
| **488** | Solo otorga descuento el IVA de compras que (a) sean computables como costo o gasto en renta y (b) se destinen a operaciones gravadas (o exentas). | Filtro de procedencia: IVA de gastos no deducibles o destinados a excluidas NO se descuenta (va al costo/gasto). |
| **490** | **Prorrateo**: cuando los descontables comunes no son imputables directamente a operaciones gravadas, exentas o excluidas, se descuentan en proporción a los ingresos de cada tipo. Solo aplica si coexisten operaciones gravadas/exentas Y excluidas. | COMERCIO DE BICICLETAS A. Detalle en *Art 490 ET - Prorrateo IVA* y [[Aux 15 - IVA y Prorrateo]]. |
| **496** | Oportunidad del descontable: se contabiliza en el período de causación **o** en los 3 períodos bimestrales siguientes (declarantes bimestrales) / el período siguiente (cuatrimestrales), y se declara en el período en que se contabilizó. | Facturas de compra que llegan tarde: aún se pueden descontar dentro de la ventana. |

## Periodicidad, declaración y facturación

| Artículo | Regla esencial | Uso en la firma |
|---|---|---|
| **600** | Periodicidad: **bimestral** para grandes contribuyentes y quienes tuvieron ingresos brutos ≥ 92.000 UVT al 31/dic del año anterior (con UVT 2025: ≈ $4.581.508.000) y para responsables de los Arts. 477/481; **cuatrimestral** para los demás. | Regla D.6: confirmar SIEMPRE por cliente (EXPORTADORA DE SERVICIOS B y TALLER DE DISEÑO J bimestral; COMERCIO DE BICICLETAS A cuatrimestral). |
| **601** | Deben declarar todos los responsables; **no es obligatorio declarar por períodos sin operaciones** gravadas ni descontables. | Períodos en cero: evaluar si procede no presentar. |
| **602** | Contenido de la declaración de IVA (F-300): ingresos por tipo de operación, descontables, sanciones, firma. | Estructura del entregable Excel de 11 hojas (regla D.9): casillas de compras 50-57 con BASE sin IVA, nunca el total (regla D.4). |
| **615** | **Todos** los que vendan bienes o presten servicios deben expedir factura o documento equivalente, sean o no responsables de IVA. | Exigir soporte a todo proveedor; base del documento soporte con no obligados. |
| **616-1** | Sistemas de facturación: factura electrónica con validación previa DIAN (regla general), documentos equivalentes (el tiquete POS solo soporta ventas ≤ **5 UVT = $261.870**; por encima, el comprador puede exigir factura electrónica si quiere costos/descontables). | El Token DIAN refleja este ecosistema: `Emitido` = ventas, `Recibido` = compras (regla D.3); tiquetes POS grandes sin FE = riesgo de rechazo del descontable. |
| **617** | Requisitos de la factura: denominación, numeración autorizada, fecha, identificación de vendedor y adquirente, descripción, valor, IVA discriminado, calidad de retenedor. | Checklist al auditar soportes (junto con Art. 771-2). |

## Cambios recientes y vigencia (corte: junio 2026)

- La estructura del IVA NO fue tocada por la Ley 2277/2022 (la reforma se concentró en renta, patrimonio y saludables); tarifas 19 %/5 % y listas de excluidos/exentos siguen siendo las de las Leyes 1819/2016, 1943/2018 y 2010/2019.
- **Decreto 1474 de 2025** (emergencia: IVA a juegos de azar en línea y otras medidas) **inexequible** — C-079 de 2026; la DIAN debe devolver lo recaudado. No aplicar ninguna medida de la emergencia.
- Ley de financiamiento 2025 (que proponía cambios de IVA): **hundida** — sin efectos.
- Umbral de no responsables (3.500 UVT) y periodicidad (92.000 UVT) sin cambios a jun-2026.

## Fuentes (consultadas 2026-06-08)

- ET en Función Pública: https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=6533
- Estatuto.co Libro III (420 y ss.): https://estatuto.co
- Normograma DIAN: https://normograma.dian.gov.co
- Siempre al Día — inexequibilidad Decreto 1474/2025 y efectos DIAN: https://siemprealdia.co/colombia/impuestos/inexequibilidad-del-decreto-1474-de-2025/
- Corte Constitucional — C-079 de 2026: https://www.corteconstitucional.gov.co/relatoria/2026/C-079-26.htm

## Relacionado

- *Art 481 ET - Exportadores* · *Art 490 ET - Prorrateo IVA*
- [[Protocolo IVA Formulario 300]] · [[Aux 15 - IVA y Prorrateo]] · *Formato 1005 y 1006 - IVA*
- *ET - Estructura del Estatuto Tributario* · *ET - Renta Articulos Clave* · [[ET - Retencion en la Fuente Articulos Clave]] · *ET - Procedimiento y Sanciones Articulos Clave*
- *MOC - Conocimiento Tecnico* · *Proyecto - Estatuto Tributario y Normatividad Fiscal*
