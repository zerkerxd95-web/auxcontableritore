---
tipo: leccion
tags: [ritore, escuela, auxiliar, documento-soporte, dsel]
modulo: 2
estado: vigente
fecha: 2026-06-08
---
# Aux 10 - Documento Soporte a No Obligados

## Objetivo
El auxiliar sabrá cuándo y cómo generar el documento soporte en adquisiciones a sujetos no obligados a facturar (DS/DSNO/DSEL), transmitirlo electrónicamente en plazo, contabilizarlo como cualquier compra y evitar el error clásico: confundirlo con una venta en el token DIAN.

## Marco conceptual y normativo
- **Qué es:** cuando compramos a alguien que NO está obligado a expedir factura (típicamente persona natural no responsable de IVA — código 49 del RUT: arrendadores, transportadores informales, prestadores ocasionales), **el COMPRADOR genera el documento** que soporta el costo/gasto y el IVA descontable si lo hubiera.
- **Base normativa:** Art. 771-2 ET (procedencia de costos) y Art. 1.6.1.4.12 del DUR 1625/2016; funcionalidad electrónica y anexo técnico en la **Resolución DIAN 000167 de 2021** (modificada en plazos/transmisión por las Res. 000488 y 000587 de 2022). Fuente: [DIAN — Documento Soporte con no obligados](https://www.dian.gov.co/impuestos/Paginas/Sistema-de-Factura-Electronica/Documento-Soporte-Adquisiciones-No-Obligados.aspx), [Res. 167/2021](https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0167_2021.htm). `[VERIFICAR con MonitoreoNormativo si hay resolución posterior vigente antes de cada campaña]`
- **Requisitos del documento** (verificados jun-2026):
  1. Denominación expresa "Documento soporte en adquisiciones efectuadas a no obligados a facturar".
  2. Fecha de la operación (= fecha de generación).
  3. Nombre/razón social y NIT del **vendedor** y del **adquirente**.
  4. Numeración consecutiva autorizada por la DIAN (rango propio, prefijo DS).
  5. Descripción del bien/servicio y valor total.
  6. CUDS y firma digital (generación electrónica).
- **Transmisión electrónica — dos modalidades** (Art. 2, Res. 167/2021): por **cada operación** (generado el mismo día de la compra) o **acumulado semanal por proveedor** (un documento generado dentro de la semana siguiente a la primera operación). Generarlo fuera de plazo **invalida su efecto fiscal** (doctrina DIAN 2025).

## Paso a paso

1. Confirma que el proveedor NO está obligado a facturar: RUT con código 49, sin responsabilidad de facturador electrónico. Si está obligado y "no factura", se le exige la factura — el DS no lo reemplaza.
2. Reúne los datos del tercero (NIT/cédula con DV validado, nombre, dirección — [[Aux 03 - Terceros y RUT]]).
3. Genera el DS electrónico en el software facturador del cliente, en plazo (mismo día u opción semanal acumulada).
4. Calcula y causa la **retención en la fuente** que aplique (al no obligado SÍ se le retiene según el concepto).
5. Contabiliza **igual que una compra** y archiva el XML/PDF con CUDS.

### Asientos modelo

**1. Arrendamiento de local a persona natural no responsable** — canon $1.500.000, retención arrendamientos 3,5%:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 512010 | Arrendamientos — construcciones y edificaciones | 1.500.000 | |
| 236530 | Retefuente — arrendamientos 3,5% | | 52.500 |
| 233545 | Costos y gastos por pagar | | 1.447.500 |

**2. Servicio de transporte de carga con no obligado** — $500.000, retención transporte de carga 1%:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 523550 | Transporte, fletes y acarreos | 500.000 | |
| 236525 | Retefuente — servicios (transporte de carga 1%) | | 5.000 |
| 233595 | Costos y gastos por pagar | | 495.000 |

*Sin IVA: el no responsable no lo cobra. Si el pago es a un prestador de servicios persona natural sin retención posible bajo Art. 383 ET, recuerda la regla C.3 de exógena: esos pagos van al F-2276, no al F-1001 — criterio que define el especialista.*

### En el token DIAN
El DS generado aparece en el token del cliente. **Regla D.3 — error común ya cometido y corregido:** un **DSEL emitido a un no obligado es COMPRA soporte, NO venta**, aunque el token lo muestre en el grupo `Emitido` (porque lo "emite" el comprador). Jamás se suma a ingresos: se clasifica como compra. En **Cliente - EMPRESA CON SOCIO EXTRANJERO C** el token mensual trae hoja `DS` separada justamente para esto.

## Errores comunes
- **Clasificar el DS emitido como venta** al interpretar el token: infla ingresos e IVA generado (regla D.3, lección real de campañas IVA 2026 — ver [[Aux 20 - Interpretacion del Token DIAN]]).
- **Aceptar "cuentas de cobro" sin generar el DS electrónico:** la cuenta de cobro sola NO es soporte fiscal válido desde la vigencia de la transmisión electrónica; sin DS transmitido en plazo, el costo se cae.
- **Generarlo por fuera del plazo** (mismo día / semana acumulada): la DIAN lo considera sin efecto fiscal (doctrina 2025) — el gasto queda en riesgo.
- **No retener** "porque es informal": al no obligado se le practican las retenciones según concepto y base — la informalidad del proveedor no exime al agente retenedor.
- **Usar el DS con proveedores que SÍ están obligados a facturar:** maquilla un incumplimiento del proveedor y deja al cliente sin soporte válido.
- **Crear el tercero sin NIT/cédula verificada:** estos proveedores suelen ser nuevos en el maestro; el DV se valida al crearlos (*Subskill B5 - Depurar Terceros y Cuantias Menores*).

## Checklist de calidad
1. ¿El proveedor realmente NO está obligado a facturar (RUT código 49, sin obligación de FE)?
2. ¿DS generado electrónicamente, con CUDS, dentro del plazo (día de la operación o acumulado semanal)?
3. ¿Datos completos del vendedor y adquirente, con DV del NIT validado?
4. ¿Retención practicada con el concepto y tarifa correctos?
5. ¿Contabilizado como compra/gasto con tercero real (nunca genérico)?
6. ¿En el cruce del token quedó clasificado como COMPRA, no como venta?
7. ¿XML/PDF archivado en la carpeta canónica del cliente?

## Relacionado
- Anterior: [[Aux 09 - Notas Credito y Debito]] · Siguiente: [[Aux 11 - Causacion de Nomina]]
- [[MOC - Escuela Auxiliar Contable]] · [[02-AuxiliarContable-Senior]]
- [[Aux 03 - Terceros y RUT]] · [[Aux 06 - Causacion de Facturas de Compra y Gastos]] · [[Aux 14 - Calculo de Retenciones]] · [[Aux 20 - Interpretacion del Token DIAN]]
- **Cliente - EMPRESA CON SOCIO EXTRANJERO C** (hoja DS del token mensual) · [[Protocolo IVA Formulario 300]]
