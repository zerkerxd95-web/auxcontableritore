---
tipo: plantilla
tags: [ritore, plantilla, contable]
archivo: Suite Excel Pro/23_Facturacion_Compra_y_Venta.xlsx
estado: vigente
fecha: 2026-06-08
---
# Plantilla 23 - Facturación Compra y Venta

## Para qué sirve y a qué cliente
Registra **facturas de venta y de compra** con maestros de clientes, proveedores y productos, y por fórmula calcula base/IVA/total, **retención practicada**, ventas y compras por tercero y por producto, **cartera (CxC) y cuentas por pagar (CxP) por antigüedad** y los **asientos contables** de cada factura (con chequeo de cuadre). Habilita el servicio de **facturación, causación de ventas/compras y control de cartera** para comercializadoras y prestadores de servicios.

## Estructura del libro
| Hoja | Capa | Contenido |
|------|------|-----------|
| Instrucciones | servicio | Qué es y cómo se usa |
| Guia Power BI | servicio | Conexión de las BD de hechos y dimensiones |
| BD_Clientes | datos (dimensión) | Maestro de clientes (NIT, ciudad, agente retenedor) |
| BD_Proveedores | datos (dimensión) | Maestro de proveedores (tipo de persona, régimen) |
| BD_Productos | datos (dimensión) | Maestro de productos (precio, costo, IVA, margen) |
| Parametros | parámetros | Datos del periodo, fecha de corte de cartera y umbrales de antigüedad |
| BD_FacturasVenta | datos (hechos) | Una fila por factura de venta |
| BD_FacturasCompra | datos (hechos) | Una fila por factura de compra |
| Calc_Ventas | cálculo | Ventas por cliente y por producto |
| Calc_Compras | cálculo | Compras por proveedor (base, IVA, retención, total) |
| Calc_CarteraCxP | cálculo | Cartera CxC y CxP pendientes por antigüedad |
| Calc_Asientos | cálculo | Asiento contable por factura con cuadre |
| Dashboard | dashboard | Ventas, compras, margen, IVA neto y cartera vencida |

## Modelo de datos (Power BI)
Modelo en **estrella** con dos tablas de hechos (ventas y compras) y tres dimensiones.

**BD_Clientes** (dim) — `id`, `nit`, `nombre`, `ciudad`, `agente_retenedor` (Sí/No, determina si practica retención).
**BD_Proveedores** (dim) — `id`, `nit`, `nombre`, `tipo_persona`, `regimen`.
**BD_Productos** (dim) — `codigo`, `descripcion`, `precio`, `costo`, `iva_pct`, `margen_unit` (`=precio-costo`).

**BD_FacturasVenta** (hechos) — encabezados fila 1:
| Columna | Significado |
|---------|-------------|
| fecha, factura | Fecha y consecutivo |
| cliente_id | → BD_Clientes |
| producto | → BD_Productos |
| cantidad, valor_unitario | Insumos |
| base | `=cantidad*valor_unitario` |
| iva | `=base*VLOOKUP(producto;BD_Productos;5)` (toma iva_pct) |
| total | `=base+iva` |
| estado | `pendiente` / `pagada` (alimenta la cartera) |
| reten_practicada | `=IF(VLOOKUP(cliente;BD_Clientes;5)="Si"; base*0,04; 0)` |
| mes | `=TEXT(fecha;"YYYY-MM")` |

**BD_FacturasCompra** (hechos) — `fecha`, `factura`, `proveedor_id`→BD_Proveedores, `concepto`, `base`, `iva`, `reten_practicada`, `total` (`=base+iva-reten`), `deducible` (S/N), `estado`, `cuenta_debito` (cuenta PUC), `mes`.

**Conexión en Power BI:** relaciones `cliente_id→BD_Clientes.id`, `proveedor_id→BD_Proveedores.id`, `producto→BD_Productos.codigo`; segmentar por `mes`.

## Metodología y fórmulas clave
- **Ventas (Calc_Ventas):** por cliente `=SUMIF(BD_FacturasVenta!cliente; id; base/iva/total)`; por producto, unidades `=SUMIF(...;cantidad)` y valor `=SUMIF(...;base)`.
- **Compras (Calc_Compras):** por proveedor, base/IVA/retención/total con `=SUMIF`.
- **Cartera y CxP (Calc_CarteraCxP):** solo facturas con `estado="pendiente"`; días de mora `=Parametros!fecha_corte - fecha_factura`; tramo `=IF(dias<=corriente;"Corriente";IF(dias<=alerta;"Por vencer";"Vencida"))`.
- **Asientos (Calc_Asientos):** por factura de venta — Dr Clientes (`total-retención`, 130505), Dr Retención que nos practican (135515), Cr Ingreso (413524), Cr IVA generado (240801); cuadre `=IF(ROUND(Db-Cr;0)=0;"CUADRA";"REVISAR")`. Las compras siguen el esquema simétrico (Dr gasto/inventario + Dr IVA descontable / Cr proveedores − retención practicada).

## Cómo usarla
1. Cargar los maestros **BD_Clientes**, **BD_Proveedores** y **BD_Productos** (marcar `agente_retenedor` en clientes y fijar `iva_pct` por producto).
2. Fijar en **Parametros** el periodo, la **fecha de corte** de cartera y los umbrales de antigüedad (corriente/alerta/vencida).
3. Registrar facturas en **BD_FacturasVenta** y **BD_FacturasCompra**; marcar `estado` (pendiente/pagada).
4. Revisar ventas, compras, cartera y asientos en las hojas Calc_; verificar que cada asiento diga "CUADRA".
5. El **Dashboard** se recalcula solo.

## Interpretación del dashboard
KPIs: **Ventas (base)**, **Compras (base)**, **Margen bruto**, **% Margen** e **IVA neto** (generado − descontable). Gráficos: ventas vs compras por mes, top de clientes y de productos, y cartera por tramo (Corriente / Por vencer / Vencida). **Semáforo de cartera vencida:** rojo cuando crece la CxC con mora > umbral (Parametros). El IVA neto anticipa el saldo del F-300.

## Errores comunes / controles
- **Cliente sin `agente_retenedor`** bien marcado: la retención practicada sale en 0 o de más.
- **`iva_pct` errado** en el producto (debe ser la tarifa real: 0%, 5%, 19% — no plano 19%); el IVA de la factura queda mal (regla operativa D.2).
- **No actualizar `estado` a "pagada":** la cartera nunca se descarga y la CxC queda inflada.
- **Fecha de corte mal puesta** en Parametros: la antigüedad de cartera se distorsiona.
- Las **notas crédito** se manejan como cifras netas (se restan), no en signo invertido suelto (regla D.3 / C.5).

## Relacionado
- *MOC - Plantillas Pro*
- *Estandar de Plantillas FYT*
- [[Aux 05 - Causacion de Facturas de Venta]]
- [[Aux 06 - Causacion de Facturas de Compra y Gastos]]
- [[05-AuxiliarCarteraCxP-Senior]]
