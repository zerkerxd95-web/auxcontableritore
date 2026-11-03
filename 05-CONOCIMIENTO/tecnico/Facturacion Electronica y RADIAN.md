---
tipo: conocimiento
tags: [ritore, conocimiento, facturacion-electronica, dian, radian]
estado: vigente
fecha: 2026-06-08
---

# Facturación Electrónica y RADIAN

> El **Sistema de Facturación Electrónica (SFE)** de la DIAN es el conjunto de documentos electrónicos con validación previa que sustentan ingresos, costos, deducciones e IVA. La factura electrónica de venta validada es la **fuente de verdad** de los ingresos y, vía el [[Aux 20 - Interpretacion del Token DIAN|token DIAN]], el insumo principal de IVA ([[Protocolo IVA Formulario 300]]) y exógena. Gestionado en la firma por [[04-AuxiliarFacturacionElectronica-Senior]].

## Marco normativo vigente

- **Resolución DIAN 000165 de 2023** (01/11/2023) — norma marco actual del SFE: desarrolla la factura electrónica de venta, los documentos equivalentes, el documento soporte, los proveedores tecnológicos; adopta el **anexo técnico de factura electrónica v1.9** y el anexo técnico del documento equivalente electrónico. Deroga y compila la dispersión anterior (Res. 042/2020 y siguientes).
- **Resolución DIAN 000202 de 2025** (31/03/2025) — modifica parcialmente la 000165: **simplifica los datos del adquirente** (la factura solo exige nombre/razón social, tipo y número de identificación, y correo si está disponible), habilita el **servicio de consulta de adquirentes** de la DIAN, y ajusta plazos del documento equivalente de servicios públicos. `[VERIFICAR si hay modificatorias posteriores con *21-MonitoreoNormativo-Senior*]`.
- **Resolución DIAN 00085 de 2022** — reglamenta el **RADIAN** y la habilitación de proveedores/usuarios para registrar eventos; **Anexo Técnico RADIAN v1.1**. `[VERIFICAR vigencia/versión actual]`.
- **Art. 616-1 ET** — obligación de facturar y sistema de facturación. **Arts. 615, 617, 618 ET** — requisitos de la factura.
- Base legal del título valor electrónico: **Ley 1231 de 2008** (factura como título valor) + **Ley 1819 de 2016** + reglamentación DIAN del registro RADIAN.

## Documentos del sistema

| Documento | Qué sustenta | Notas |
|---|---|---|
| **Factura electrónica de venta** | Ingreso del vendedor / costo-deducción-IVA del comprador | Requiere **validación previa** de la DIAN para ser válida |
| **Documento soporte electrónico (en adquisiciones a no obligados a facturar)** | Costo/deducción/IVA descontable cuando el proveedor NO está obligado a facturar | Ver [[Aux 10 - Documento Soporte a No Obligados]] |
| **Documento soporte de pago de nómina electrónica (DSNE)** | Deducción de costos y gastos de nómina en renta | Transmisión mensual, dentro de los **primeros 10 días calendario** del mes siguiente al pago |
| **Documentos equivalentes electrónicos** | Tiquete POS, tiquete de transporte, etc. (sustituyen factura en casos tasados) | Calendario de implementación gradual |
| **Notas crédito y débito electrónicas** | Ajustes a la factura (devoluciones, descuentos, correcciones) | Las **notas crédito NO se restan** en exógena 1005/1006: van en columna propia (ver *Lecciones Aprendidas Exogena* C.5) |

## El RADIAN — factura electrónica como título valor

El **RADIAN** (Registro de la factura electrónica de venta como título valor) es la plataforma de la DIAN que da trazabilidad a la vida de la factura cuando va a **circular / negociarse** (factoring). El registro en RADIAN **solo es obligatorio si se quiere negociar** la factura como título valor; para el uso tributario normal de la factura no se requiere.

### Eventos del proceso de recepción (Art. 616-1 ET, par. 6 y reglamentación)
1. **Acuse de recibo de la factura electrónica** — evidencia de que el adquirente recibió la factura.
2. **Recibo del bien o prestación del servicio** — evidencia de la entrega efectiva.
3. **Aceptación o rechazo (reclamo) de la factura:**
   - **Aceptación expresa** — el adquirente manifiesta su conformidad.
   - **Aceptación tácita** — opera cuando, transcurridos **3 días hábiles** desde el recibo del bien/servicio, el adquirente **no reclama**. A partir de ese momento la factura presta mérito ejecutivo y puede circular.

> **Regla crítica costo/IVA:** para que una factura a crédito dé derecho a costo/deducción e IVA descontable, deben generarse el **acuse de recibo de la factura** y el **recibo del bien o servicio**. Su ausencia compromete la deducibilidad.

## Proveedor tecnológico

El **proveedor tecnológico** es la empresa habilitada por la DIAN que provee al cliente el software para generar, transmitir, validar, recibir y registrar (en RADIAN) los documentos electrónicos. La firma debe conocer **quién es el proveedor de cada cliente** y verificar que las facturas estén efectivamente validadas (cruce con el [[Aux 20 - Interpretacion del Token DIAN|token DIAN]]).

## Calendario de obligados y contingencia

- **Obligados:** todos los responsables de facturar (Art. 616-1 ET) según RUT; nómina electrónica obliga a empleadores declarantes de renta, contribuyentes del SIMPLE y quienes hagan pagos que constituyan ingreso para el receptor.
- **Calendario:** la implementación de documentos equivalentes electrónicos y de nuevos obligados es **gradual y por resolución**; cada fecha se confirma con *21-MonitoreoNormativo-Senior*. `[VERIFICAR calendario vigente 2026 — documentos equivalentes y nómina]`.
- **Contingencia:** ante caída del sistema del facturador, del proveedor tecnológico o de la DIAN, se factura por **talonario / factura de contingencia** y se transmite a la DIAN **dentro de las 48 horas** siguientes al restablecimiento. Documentar la contingencia.

## Relación con el token DIAN, IVA y exógena

- El **token DIAN** es la descarga de los documentos electrónicos validados; es la fuente que ya documentamos para liquidar IVA y cuadrar exógena. Ver [[Aux 20 - Interpretacion del Token DIAN]].
- **IVA (F-300):** el token (emitidos = ventas / recibidos = compras) alimenta el IVA generado y descontable; desglosar siempre base e IVA, no aplicar 19% plano ([[Protocolo IVA Formulario 300]]).
- **Exógena:** la facturación electrónica alimenta los formatos 1001 (pagos), 1007 (ingresos), 1005/1006 (IVA). Un DSEL emitido a un no obligado es **compra soporte, no venta**.

## Relacionado

- *MOC - Conocimiento Tecnico*
- [[Aux 20 - Interpretacion del Token DIAN]]
- [[04-AuxiliarFacturacionElectronica-Senior]]
- [[Aux 10 - Documento Soporte a No Obligados]]
- [[Protocolo IVA Formulario 300]] · *Catalogo de Formatos Exogena*
- *21-MonitoreoNormativo-Senior*
