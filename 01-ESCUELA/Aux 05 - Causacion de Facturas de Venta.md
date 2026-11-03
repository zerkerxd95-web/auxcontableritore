---
tipo: leccion
tags: [ritore, escuela, auxiliar, ventas, iva]
modulo: 2
estado: vigente
fecha: 2026-06-08
---
# Aux 05 - Causacion de Facturas de Venta

## Objetivo
El auxiliar sabrá causar correctamente cualquier factura de venta: separar base, IVA (19% / 5% / exento / excluido) o INC 8%, registrar la retención que nos practican (135515), distinguir contado vs crédito y manejar los ingresos recibidos por anticipado (2805).

## Marco conceptual y normativo
- **Causación del ingreso:** NIIF PYMES Sección 23 — el ingreso se reconoce cuando se transfiere el bien/servicio, no cuando entra la plata. Fiscalmente, Art. 28 ET (devengo para obligados a llevar contabilidad).
- **IVA generado:** Arts. 420 y ss. ET. Tarifas vigentes: **general 19%, reducida 5%** (Arts. 468-1 y 468-3 ET: ciertos alimentos, planes de medicina prepagada, etc.), **exentos 0%** (Arts. 477 y 481 ET) y **excluidos** (Art. 424 ET).
- **Exento vs excluido — diferencia clave:**
  - **Exento** = gravado a tarifa 0%. El vendedor ES responsable de IVA, declara, y tiene derecho a IVA descontable (los exportadores como **Cliente - EMPRESA CON SOCIO EXTRANJERO C** facturan exento por Art. 481 ET y recuperan su descontable).
  - **Excluido** = no causa IVA. No hay derecho a descontable: el IVA pagado en insumos es mayor valor del costo. Frecuente en el sector bicicletas (**Cliente - COMERCIO DE BICICLETAS A**).
- **INC 8%:** impuesto nacional al consumo en servicio de restaurantes/bares (Arts. 512-1 y 512-9 ET). No es IVA: no genera descontable para quien lo paga. Es el caso de **Cliente - CENTRO CULTURAL M** (RST con INC 8%).
- **Retención que nos practican:** si el comprador es agente retenedor, descuenta retefuente (y a veces reteIVA/reteICA) del pago — para nosotros es un **anticipo de impuestos** (1355), jamás un gasto ni un menor ingreso.

## Paso a paso

1. Verifica que la factura esté **emitida y validada DIAN** (CUFE) — viene del token, grupo `Emitido`.
2. Identifica el tratamiento del producto/servicio: gravado 19%/5%, exento, excluido o INC.
3. Desglosa SIEMPRE base e impuesto: `Base = Total − IVA` con el IVA real por factura — nunca 19% plano (regla D.2; hay tarifas mixtas).
4. Determina si el comprador nos practicó retención (aparece en la factura o en el certificado).
5. Causa el asiento con tercero = NIT del comprador; contado → 1105/1110, crédito → 1305.
6. Notifica/alimenta: IVA generado → liquidación F-300 ([[Aux 15 - IVA y Prorrateo]]); ingreso → F-1007 de exógena.

### Asientos modelo (valores 2026)

**1. Venta a crédito gravada 19% con retención de compras 2,5%** — mercancía $8.000.000:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 130505 | Clientes nacionales | 9.320.000 | |
| 135515 | Anticipo retención en la fuente (2,5%) | 200.000 | |
| 413524 | Comercio al por mayor y al por menor | | 8.000.000 |
| 240801 | IVA generado 19% | | 1.520.000 |

**2. Venta de contado de bien a tarifa 5%** — $2.000.000 base:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 111005 | Bancos | 2.100.000 | |
| 4135xx | Ingresos por ventas | | 2.000.000 |
| 240801 | IVA generado 5% | | 100.000 |

**3. Venta exenta (exportación de servicios, Art. 481 ET — patrón **Cliente - EMPRESA CON SOCIO EXTRANJERO C**)** — USD facturados equivalentes a $15.000.000:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 130510 | Clientes del exterior | 15.000.000 | |
| 4155xx | Ingresos por servicios — exportación (exento) | | 15.000.000 |

*IVA generado $0, pero el descontable de sus compras SÍ se recupera (D.7). Una venta excluida se ve igual en el asiento — la diferencia está en el derecho al descontable y en las casillas del F-300.*

**4. Venta de restaurante con INC 8% (patrón **Cliente - CENTRO CULTURAL M**)** — consumo $500.000:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 110505 | Caja general | 540.000 | |
| 4140xx | Ingresos — restaurante/bar | | 500.000 |
| 2467xx | Impuesto nacional al consumo por pagar (8%) | | 40.000 |

*En CENTRO CULTURAL M la factura global de ventas se construye desde las consignaciones bancarias, con INC 8%. La cuenta del INC se habilita en el plan del cliente (24xx); verificar el plan antes de usar.*

**5. Ingreso recibido por anticipado (patrón real **Cliente - SALÓN DE BELLEZA I**)** — el cliente paga $600.000 por un servicio que se prestará después:

Al recibir la plata (no hay factura aún):

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 111005 | Bancos | 600.000 | |
| 280505 | Anticipos y avances recibidos de clientes | | 600.000 |

Al prestar el servicio y facturar (servicio sin IVA en este cliente):

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 280505 | Anticipos y avances recibidos de clientes | 600.000 | |
| 4135xx | Ingresos por servicios | | 600.000 |

*En SALÓN DE BELLEZA I los ingresos no facturados del POS LIZTO van a 2805 y solo se reconoce el ingreso al redimir el servicio. El 2805 se depura al cierre de diciembre.*

## Errores comunes
- **Aplicar 19% plano a todo:** regla D.2 — usar el IVA real por factura; hay 5%, exentos, excluidos y mixtas. Y la "tarifa 21%" NO existe en Colombia: si aparece, es error a señalar.
- **Registrar la retención que nos practican como gasto o como menor ingreso:** va al **135515** (activo, anticipo). De ahí sale el cruce con el F-1003 de exógena y la casilla de retenciones del F-110.
- **Reconocer como ingreso la plata recibida sin prestar el servicio:** infla ingresos y RST/IVA del periodo; va a 2805 (caso SALÓN DE BELLEZA I).
- **Confundir INC con IVA:** el INC no va al 2408 ni entra al F-300 como IVA generado; tiene su propia cuenta y su propio formulario (310/RST según el caso).
- **No causar facturas anuladas/notas asociadas:** el cruce token vs contabilidad queda descuadrado ([[Aux 09 - Notas Credito y Debito]]).
- **Olvidar el ingreso en el F-1007:** todo lo causado en 41xx debe conciliar con renta e IVA (regla C.8: 1007 ↔ ingresos F-110 ↔ F-300).

## Checklist de calidad
1. ¿Factura validada DIAN y presente en el token del periodo?
2. ¿Base e impuesto desglosados con el IVA real de la factura?
3. ¿Tratamiento correcto: 19% / 5% / exento / excluido / INC?
4. ¿Retención que nos practicaron registrada en 135515 con el tercero correcto?
5. ¿Contado vs crédito reflejado en la cuenta correcta (1105/1110 vs 1305)?
6. ¿Anticipos previos del cliente cruzados contra 2805 antes de crear nueva CxC?
7. ¿Total de ingresos del mes cuadra contra el token DIAN (grupo Emitido, neto de notas)?
8. ¿Asiento con tercero, soporte y fecha de causación correcta?

## Relacionado
- Anterior: [[Aux 04 - Soportes Contables y Papeles de Trabajo]] · Siguiente: [[Aux 06 - Causacion de Facturas de Compra y Gastos]]
- [[MOC - Escuela Auxiliar Contable]] · [[02-AuxiliarContable-Senior]]
- [[Aux 15 - IVA y Prorrateo]] · [[Aux 20 - Interpretacion del Token DIAN]] · [[Protocolo IVA Formulario 300]]
- **Cliente - CENTRO CULTURAL M** · **Cliente - SALÓN DE BELLEZA I** · **Cliente - EMPRESA CON SOCIO EXTRANJERO C**
