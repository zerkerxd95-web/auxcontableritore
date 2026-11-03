---
tipo: leccion
tags: [ritore, escuela, auxiliar, compras, gastos]
modulo: 2
estado: vigente
fecha: 2026-06-08
---
# Aux 06 - Causacion de Facturas de Compra y Gastos

## Objetivo
El auxiliar sabrá causar facturas de compra y gasto: clasificar el débito (inventario, gasto, costo o activo fijo), decidir si el IVA es descontable o mayor valor, aplicar la retención correcta al crédito y — crucial — distinguir gasto de la empresa vs gasto personal de socios.

## Marco conceptual y normativo
- **IVA descontable:** Arts. 485-488 ET — solo es descontable el IVA de compras que computen como costo o gasto de la actividad y se destinen a operaciones gravadas o exentas. Si la compra se destina a operaciones excluidas, o no da derecho, el IVA es **mayor valor del costo/gasto**.
- **Procedencia del costo:** Art. 771-2 ET (factura válida) y Art. 771-5 ET (límite a pagos en efectivo).
- **Retención en la fuente:** Arts. 365 y ss. ET. El comprador agente retenedor retiene al proveedor según concepto y responsabilidades del RUT (tarifas y bases en [[Aux 14 - Calculo de Retenciones]]; nunca se inventa una tarifa — se consulta).
- **Deducible vs no deducible:** los gastos sin relación de causalidad (Art. 107 ET), sanciones, GMF en su 50%, y en general lo registrado en la clase **53 (no operacionales)** se trata como no deducible — en exógena va a la columna O del F-1001 (regla C.3).

## Paso a paso

1. Valida la factura (Art. 617 ET, CUFE, NIT del adquirente = el cliente) — viene del token, grupo `Recibido`.
2. Clasifica el débito: ¿inventario (1435), gasto admin (51xx), gasto ventas (52xx), costo (6xxx/7xxx), activo fijo (15xx) o no deducible (53xx)?
3. Decide el IVA: ¿descontable (240802) o mayor valor del débito?
4. Calcula retenciones (renta 2365, reteIVA 2367, reteICA 2368) según concepto, base mínima y RUT del proveedor.
5. Acredita el neto a 2205 (proveedores de bienes) o 2335 (costos y gastos por pagar).
6. Verifica débitos = créditos y tercero en todos los renglones.

### Asientos modelo (valores 2026)

**1. Compra de mercancía para la venta** — $6.000.000 + IVA 19%, retención compras 2,5% (base 27 UVT = $1.414.098 superada):

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 143505 | Mercancías no fabricadas por la empresa | 6.000.000 | |
| 240802 | IVA descontable | 1.140.000 | |
| 236540 | Retefuente — compras 2,5% | | 150.000 |
| 220505 | Proveedores nacionales | | 6.990.000 |

**2. Servicio de vigilancia (gasto)** — $1.200.000 + IVA, retención servicios 4%:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 513510 | Servicios — vigilancia | 1.200.000 | |
| 240802 | IVA descontable | 228.000 | |
| 236525 | Retefuente — servicios 4% | | 48.000 |
| 233595 | Costos y gastos por pagar | | 1.380.000 |

**3. Compra de activo fijo** — computador $4.800.000 + IVA. Va al 15xx, NO al gasto:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 152805 | Equipo de procesamiento de datos | 4.800.000 | |
| 240802 | IVA descontable | 912.000 | |
| 236540 | Retefuente — compras 2,5% | | 120.000 |
| 233595 | Costos y gastos por pagar | | 5.592.000 |

*En exógena este pago va al F-1001 concepto 5008 (compra de activos fijos), no al 5016.*

**4. IVA como mayor valor — criterio EXCLUSIVO **Cliente - EXPORTADORA DE SERVICIOS B**:** factura DIAN con IVA **< $50.000** → el IVA no se descuenta, es mayor valor de la compra, por factura completa (regla D.8 — este criterio NO se generaliza a otros clientes). Factura de $200.000 + IVA $38.000:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 5195xx / 14xx | Gasto o inventario (base + IVA) | 238.000 | |
| 233595 | Costos y gastos por pagar | | 238.000 |

*El mismo tratamiento "IVA al costo" aplica de forma GENERAL cuando la compra se destina a operaciones excluidas (Art. 488 ET) — ahí no es criterio de cliente sino norma.*

**5. Gasto no deducible (clase 53)** — sanción DIAN $400.000:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 539520 | Multas, sanciones y litigios | 400.000 | |
| 233595 | Costos y gastos por pagar | | 400.000 |

**6. Gasto personal de socio = préstamo, NUNCA gasto.** El socio pagó su mercado/viaje personal con la tarjeta de la empresa, $900.000. Casos reales: **Cliente - EMPRESA DE TECNOLOGÍA K** y **Cliente - EMPRESA CON SOCIO EXTRANJERO C** (los socios pagan muchas cosas a título personal; distinguir empresa/personal es parte central del trabajo):

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 132505 | Cuentas por cobrar a socios y accionistas | 900.000 | |
| 111005 | Bancos | | 900.000 |

*Cuenta PUC estándar: 1325. Verifica el plan del cliente: lo esencial es que va a una cuenta por cobrar al socio, jamás a 51xx/52xx. Si se asienta como gasto: no es deducible, infla el gasto, distorsiona renta y puede configurar pagos a vinculados sin soporte.*

## Errores comunes
- **Descontar IVA de compras destinadas a operaciones excluidas** o sin relación con la actividad (Art. 488 ET): el descontable se cae en el F-300 y en el F-1005.
- **Aplicar el criterio EXPORTADORA DE SERVICIOS B (<$50.000) a otros clientes:** regla D.8 — un criterio particular NUNCA se generaliza sin confirmar.
- **Activos fijos al gasto** para "simplificar": revienta renta, depreciación y el concepto 5007/5008 de exógena.
- **Gastos de socios como gasto de la empresa:** en **Cliente - EMPRESA CON SOCIO EXTRANJERO C** hay carpetas enteras ("NO TOKEN PERSONALES RICARDO") para separar lo personal; en **Cliente - EMPRESA DE TECNOLOGÍA K** el saneamiento de cuentas tipo 131015 (CxC socios/particulares) fue papel de cierre. La regla: a 1325 (préstamo al socio) o a reembolso, nunca a 5xxx.
- **Retener a un proveedor RST (código 47)** o no retener a uno ordinario: revisar RUT antes de causar ([[Aux 03 - Terceros y RUT]]).
- **Olvidar la base mínima:** servicios 4 UVT ($209.496 en 2026), compras 27 UVT ($1.414.098) — bajo la base no se retiene.
- **Cuenta 53 usada como cajón genérico:** en SALÓN DE BELLEZA I el residuo no identificable de egresos va a 530505 como no deducible — es un último recurso documentado, no una práctica de descarga.

## Checklist de calidad
1. ¿Factura válida (617 ET), del token, a nombre del cliente?
2. ¿Débito clasificado correctamente: 1435 / 5xxx / 6xxx / 15xx / 53xx?
3. ¿El IVA es realmente descontable? Si no, ¿quedó como mayor valor?
4. ¿Retención calculada con concepto, tarifa y base mínima correctos, según RUT del proveedor?
5. ¿Crédito al pasivo correcto (2205 bienes / 2335 servicios) por el NETO?
6. ¿Ningún gasto personal de socios coló como gasto de la empresa?
7. ¿Criterios particulares del cliente aplicados solo a ese cliente (D.8)?
8. ¿Compras del mes cuadran contra token DIAN (grupo Recibido)?

## Relacionado
- Anterior: [[Aux 05 - Causacion de Facturas de Venta]] · Siguiente: [[Aux 07 - Recibos de Caja]]
- [[MOC - Escuela Auxiliar Contable]] · [[02-AuxiliarContable-Senior]]
- [[Aux 14 - Calculo de Retenciones]] · [[Aux 15 - IVA y Prorrateo]] · [[Aux 17 - Inventarios y Compras Multi-item]]
- **Cliente - EXPORTADORA DE SERVICIOS B** · **Cliente - EMPRESA DE TECNOLOGÍA K** · **Cliente - EMPRESA CON SOCIO EXTRANJERO C** · *Formato 1001 - Pagos y Retenciones*
