---
tipo: leccion
tags: [ritore, escuela, auxiliar, soportes, papeles-de-trabajo]
modulo: 1
estado: vigente
fecha: 2026-06-08
---
# Aux 04 - Soportes Contables y Papeles de Trabajo

## Objetivo
El auxiliar sabrá distinguir un soporte válido de uno que no lo es, exigir los requisitos del Art. 617 ET en facturas, organizar los papeles de trabajo con la estructura canónica de la firma y proteger los archivos de trabajo (avances, backups, Excel) contra pérdida y corrupción.

## Marco conceptual y normativo
- **Art. 53 C.Co. y Decreto 2649/1993 Arts. 123-124:** todo asiento debe estar respaldado por comprobantes y soportes de origen interno o externo, fechados y autorizados.
- **Art. 771-2 ET:** para que costos, deducciones e IVA descontable procedan fiscalmente, se requiere factura o documento equivalente que cumpla los requisitos de los Arts. **617** y 618 ET.
- **Art. 617 ET — requisitos de la factura de venta** (los que el auxiliar verifica siempre):
  1. Denominación expresa "factura de venta".
  2. Apellidos y nombre o razón social y NIT del vendedor.
  3. Apellidos y nombre o razón social y NIT del adquirente, con discriminación del IVA pagado.
  4. Numeración consecutiva autorizada por la DIAN.
  5. Fecha de expedición.
  6. Descripción específica o genérica de los bienes/servicios.
  7. Valor total de la operación.
  8. Calidad de retenedor del IVA (cuando aplique).
- **Factura electrónica** (Res. DIAN 000165 de 2023 y modificatorias): añade CUFE, código QR y firma digital; solo es soporte válido si está **validada por la DIAN** (regla del agente: nunca aceptar factura sin validación CUFE/CUDE).
- **Documentos equivalentes y documento soporte:** tiquete POS electrónico (con límite de 5 UVT por operación para ser soporte de costos), extractos, nóminas electrónicas, y el documento soporte a no obligados ([[Aux 10 - Documento Soporte a No Obligados]]).

## Paso a paso

### 1. Validar un soporte antes de contabilizar
1. ¿Es el tipo de documento correcto para la operación? (venta → factura; compra a no obligado → documento soporte; pago → comprobante de egreso + soporte bancario).
2. ¿Cumple Art. 617 ET? Revisa especialmente NIT del adquirente (¡que sea el del cliente, no el del socio!) e IVA discriminado.
3. ¿Está validado por DIAN (CUFE/CUDE) si es electrónico? Cruza contra el token DIAN ([[Aux 20 - Interpretacion del Token DIAN]]).
4. ¿La fecha cae en el periodo que estoy contabilizando?
5. Solo entonces: contabiliza y referencia el número del soporte en el asiento.

### 2. Organizar papeles de trabajo (estructura canónica FYT)
```
📁 [NIT]_[RazonSocial]/
   📁 [Año]/
      📁 [Mes]/
         📁 01_Facturacion/ (Emitidas / Recibidas)
         📁 02_Bancos/ (Extractos / Conciliaciones)
         📁 03_Nomina/
         📁 04_Impuestos/
         📁 05_Soportes_Diversos/
         📁 06_Cierre_Mensual/ (Balance_Prueba, Estado_Resultados, Reporte_Validaciones)
```
- **Regla C.9 (continuidad):** por cada cliente en campaña (exógena, renta) se mantiene un archivo `AVANCE_EXOGENA_<cliente>.md` con fuentes usadas, formatos terminados (archivo + valor de control), criterios aplicados y pendientes. Al retomar una sesión, se lee ANTES de continuar.
- Todo entregable de la firma lleva la convención de nombres del cliente (ej. `FORMATO 300 IVA [PERIODO] [CLIENTE] - Claude.xlsx`).

### 3. Proteger los archivos de trabajo
- **Backups `.xlk`:** algunos clientes (convención de **Cliente - EMPRESA DE TECNOLOGÍA K**) mantienen copias de seguridad `.xlk` de sus balances y libros — **no se borran**: son la red de seguridad del papel de trabajo.
- **Regla de oro de [[Manejo de Archivos Excel Corruptos]] (lección C.1, aprendida a golpes):** los `.xlsx` en carpetas sincronizadas (OneDrive/Drive) se corrompen o truncan mientras están abiertos en Excel. Si al leer un archivo aparece `BadZipFile` o similar:
  1. **NO reintentar en bucle.**
  2. Pedir que cierren el archivo o hagan "Guardar como" con nombre nuevo.
  3. Verificar integridad (firma EOCD del zip) antes de procesar.
  4. Verificar que el auxiliar cuadre **débitos = créditos** antes de usarlo como insumo.

### Asiento de ejemplo — el soporte define el asiento
Factura electrónica de honorarios contables $3.000.000 + IVA, validada DIAN, del proveedor PJ régimen ordinario; retención honorarios 11%:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 511025 | Honorarios — asesoría financiera y contable | 3.000.000 | |
| 240802 | IVA descontable | 570.000 | |
| 236515 | Retención en la fuente — honorarios | | 330.000 |
| 233525 | Costos y gastos por pagar — honorarios | | 3.240.000 |

Si la misma operación llega como "cuenta de cobro" de un obligado a facturar → **se devuelve**: sin factura electrónica válida no hay costo deducible ni IVA descontable (Art. 771-2 ET).

## Errores comunes
- **Contabilizar con pantallazos, cotizaciones o pedidos** en vez de la factura validada: el cruce con el token DIAN no cuadra y el gasto se cae en renta.
- **Aceptar facturas a nombre del socio** o de otra empresa del grupo: el NIT del adquirente debe ser el del cliente (caso típico en grupos como **Cliente - SALÓN DE BELLEZA I** / INVERSIONES N, donde los pagos se cruzan entre empresas).
- **Trabajar sobre el Excel "vivo" sincronizado** y perder horas por corrupción: ver [[Manejo de Archivos Excel Corruptos]] — copiar localmente, verificar integridad, luego procesar.
- **No dejar rastro del avance:** sin `AVANCE_*.md` la siguiente sesión repite trabajo o, peor, contradice criterios ya aplicados (regla C.9).
- **Procesar un auxiliar descuadrado:** si el libro auxiliar no cumple débitos = créditos, es señal de exportación incompleta del software — se vuelve a exportar, no se "ajusta".

## Checklist de calidad
1. ¿Cada asiento del periodo referencia un soporte verificable?
2. ¿Las facturas recibidas cumplen Art. 617 ET y están validadas (CUFE) en el token?
3. ¿Los soportes están archivados en la carpeta canónica del cliente/año/mes?
4. ¿El `AVANCE_*.md` del cliente está actualizado con fuentes, criterios y pendientes?
5. ¿Los Excel de insumo pasaron verificación de integridad y cuadre débitos = créditos?
6. ¿Los `.xlk` y versiones de respaldo siguen intactos?
7. ¿Los soportes rechazados (inválidos) quedaron documentados y devueltos al cliente?

## Relacionado
- Anterior: [[Aux 03 - Terceros y RUT]] · Siguiente: [[Aux 05 - Causacion de Facturas de Venta]]
- [[MOC - Escuela Auxiliar Contable]] · [[02-AuxiliarContable-Senior]]
- [[Manejo de Archivos Excel Corruptos]] · [[Aux 20 - Interpretacion del Token DIAN]] · *Lecciones Aprendidas Exogena*
- **Cliente - EMPRESA DE TECNOLOGÍA K** (convención .xlk) · **Cliente - EMPRESA H** (revisión de libros de terceros)
