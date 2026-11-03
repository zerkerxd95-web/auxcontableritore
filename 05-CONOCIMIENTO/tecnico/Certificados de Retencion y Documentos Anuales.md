---
tipo: conocimiento
tags: [ritore, conocimiento, protocolo, renta]
periodicidad: anual
estado: vigente
fecha: 2026-06-08
---

# Certificados de Retención y Documentos Anuales

Nota de referencia de los **certificados que la firma EMITE** (cuando un cliente actúa como agente retenedor) y los que **RECIBE** como insumo para liquidar renta. Estos certificados son el eslabón entre la retención mensual (F-350), la exógena (1001/1003) y la renta anual (F-110 / F-210): lo que se certifica debe coincidir con lo que se declara y con lo que se reporta. Una retención mal certificada se convierte en un cruce DIAN. Se apoya en [[ET - Retencion en la Fuente Articulos Clave]] y *Formato 1001 - Pagos y Retenciones*.

## 1. Certificados que la firma EMITE (cliente como agente retenedor)

Cuando un cliente practica retenciones, está obligado a expedir el certificado a quien le retuvo. El certificado es el soporte con el que ese tercero descuenta la retención en SU declaración.

| Certificado | Norma | Quién lo emite | Plazo / período | Dónde se usa |
|-------------|-------|----------------|-----------------|--------------|
| **Certificado de retención en la fuente a título de renta** | Art. 381 ET (Art. 379 para laborales) | El agente retenedor (cliente de la firma) al beneficiario del pago | Anual; a solicitud cuando es por concepto distinto a laborales. Contenido mínimo del Art. 381 | El proveedor lo usa como descuento de retenciones en su F-110/F-210. Espejo del F-1001 que el cliente reporta. |
| **Certificado de retención de IVA (ReteIVA)** | Art. 615 par. 2 / Art. 381 ET; Decreto 1625/2016 | Agente retenedor de IVA (cliente) al proveedor | Bimestral o a solicitud | El proveedor lo descuenta como ReteIVA en su F-300. Cuenta 2367. |
| **Certificado de ingresos y retenciones laborales (F-220)** | Art. 378-379 ET | El empleador (cliente) a cada trabajador | Anual — a más tardar el **31 de marzo** del año siguiente | El trabajador lo usa en su F-210 (cédula de trabajo). Ver *Protocolo Certificado Ingresos y Retenciones F-220*. |
| **Certificado de retención de ICA (reteICA)** | Acuerdos municipales (Medellín y demás) | Agente retenedor de ICA (cliente) | Según calendario municipal | El proveedor lo descuenta en su declaración de ICA. Cuenta 2368. Ver *Proyecto - ICA y Retenciones Municipales*. |

**Contenido mínimo del certificado de renta (Art. 381 ET):** año gravable y ciudad; apellidos/nombre o razón social y NIT del retenedor; dirección del retenedor; apellidos/nombre o razón social y NIT del beneficiario; monto total y concepto del pago sujeto a retención; concepto y cuantía de la retención practicada; firma del pagador o agente retenedor.

**Reglas de la casa al emitir:**
- El certificado debe **cuadrar con la cuenta 2365 (renta), 2367 (IVA), 2368 (ICA)** del cliente por tercero, excluyendo cierres a nombre de la DIAN — la misma base del F-350 mensual y del F-1001 anual.
- Lo certificado al tercero = lo reportado en el **F-1001** (columna de retención practicada) = lo declarado en el **F-350** del mes. Si los tres no coinciden, hay un error que corregir antes de cerrar.
- **Nunca certificar una retención que no se practicó ni se declaró** (regla D.10 — no maquillar). El certificado prueba un hecho real.

## 2. Certificados que la firma RECIBE (cliente como sujeto retenido)

Son los certificados que **otros** agentes retenedores expiden a nuestros clientes. Son insumo directo de la renta y de la exógena.

| Certificado recibido | Quién lo emite | Dónde se usa en la firma |
|----------------------|----------------|--------------------------|
| **Retención en la fuente a título de renta** que le practicaron | Los clientes/pagadores de nuestro cliente | Descuento de retenciones (anticipo) en el **F-110 / F-210** del cliente ↔ se reporta en el ***Formato 1003 - Retenciones que le practicaron*** de exógena. |
| **ReteIVA** que le practicaron | Agentes de retención de IVA | Descuento en el **F-300** del cliente; cuenta 135517. |
| **ReteICA** que le practicaron | Agentes municipales | Descuento en la declaración de ICA municipal. |
| **Certificados financieros** (rendimientos, intereses, GMF, saldos) | Bancos y entidades financieras | Insumo de renta (rentas de capital, patrimonio, GMF deducible 50 %). |

**Regla crítica (cruce anual):** el total de retenciones de los certificados recibidos = lo que se lleva como **anticipo de retenciones** en la renta = lo que se reporta en el **F-1003**. Validar contra el renglón R-106 del F-110 (anticipo de retenciones) — puede ser $0. Ver *Conciliacion Exogena vs Declaraciones* y [[Aux 14 - Calculo de Retenciones]].

## 3. Relación con la exógena y la renta (el circuito completo)

```
Pago a un tercero  →  retención practicada (cta 2365/2367/2368, F-350 mensual)
        ↓                                   ↓
Certificado al tercero (Art. 381)    F-1001 exógena (retención practicada)
        ↓                                   ↓
El tercero la descuenta en SU renta    cruce DIAN ↔ F-1003 del tercero
```

- **F-1001** (lo que el cliente pagó y retuvo a otros) ↔ certificados que el cliente **emite** ↔ F-350 mensual.
- **F-1003** (lo que a nuestro cliente le retuvieron) ↔ certificados que el cliente **recibe** ↔ anticipo de retenciones en su renta.
- Conceptos de retención del F-1003 (regla C.4): 1301 laborales · 1302 ventas/compras · 1303 servicios · 1304 honorarios · 1305 comisiones · 1306 intereses · 1307 arrendamientos · 1308 otros · 1309 IVA. Ver *Formato 1003 - Retenciones que le practicaron*.
- Las retenciones se reportan **siempre con el NIT real** del agente retenedor — nunca en cuantías menores.

## 4. Plazos clave

- **F-220 (ingresos y retenciones laborales):** a más tardar el **31 de marzo** del año siguiente al gravable.
- **Certificado de renta (Art. 381):** anual; el bimestral/a solicitud para conceptos no laborales debe expedirse dentro de los plazos que pida el beneficiario.
- Coordinar la emisión **antes** de la campaña de renta PN (agosto-octubre): los trabajadores y proveedores necesitan sus certificados para declarar.

## Fuentes (consultadas 2026-06-08)

- Estatuto.co — Art. 381 (certificado de retención por conceptos distintos a laborales): https://estatuto.co/381
- Estatuto.co — Arts. 378-379 (certificado de ingresos y retenciones laborales): https://estatuto.co/378 · https://estatuto.co/379
- DIAN — Formularios e instructivos (F-220): https://www.dian.gov.co/atencionciudadano/formulariosinstructivos/Paginas/default.aspx
- Práctica interna: reglas C.3 y C.4 de exógena (cuentas 2365/2367/2368, conceptos 1301-1309) y D.10 (no maquillar) — CLAUDE.md del proyecto.

## Relacionado

- *MOC - Conocimiento Tecnico* · [[Protocolo Elaboracion de Impuestos]] · [[Formularios DIAN - Catalogo]]
- *Protocolo Certificado Ingresos y Retenciones F-220* · *Protocolo Renta Persona Natural F-210* · *Protocolo Renta Persona Juridica F-110*
- *Formato 1001 - Pagos y Retenciones* · *Formato 1003 - Retenciones que le practicaron* · *Conciliacion Exogena vs Declaraciones*
- [[ET - Retencion en la Fuente Articulos Clave]] · *ET - Renta Articulos Clave*
- *Proyecto - Retencion en la Fuente* · [[Aux 14 - Calculo de Retenciones]] · *Proyecto - ICA y Retenciones Municipales*
- *12-EspecialistaRetenciones-Senior* · *14-EspecialistaExogena-Master*
