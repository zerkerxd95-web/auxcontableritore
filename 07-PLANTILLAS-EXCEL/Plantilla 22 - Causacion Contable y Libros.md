---
tipo: plantilla
tags: [ritore, plantilla, contable]
archivo: Suite Excel Pro/22_Causacion_Contable_y_Libros.xlsx
estado: vigente
fecha: 2026-06-08
---
# Plantilla 22 - Causación Contable y Libros

## Para qué sirve y a qué cliente
Motor de **partida doble** que recibe los comprobantes contables (causaciones de venta, compra, nómina, recibos de caja, egresos, notas) y, por fórmula, genera los tres libros oficiales: **Libro Diario**, **Libro Mayor** y **Balance de Prueba**, con un tablero de **cuadre por comprobante** (débitos = créditos). Habilita el servicio de **teneduría / causación contable** para cualquier cliente que requiera contabilidad bajo PUC (Decreto 2650/1993) y deja la información lista para alimentar exógena, IVA, retención y estados financieros.

## Estructura del libro
| Hoja | Capa | Contenido |
|------|------|-----------|
| Instrucciones | servicio | Qué es y cómo se usa |
| Guia Power BI | servicio | Conexión de BD_Comprobantes y BD_PUC |
| BD_PUC | datos (dimensión) | Catálogo de cuentas del cliente con clase, grupo y naturaleza |
| Parametros | parámetros | Razón social, NIT, periodo, moneda, UVT del año, umbrales de descuadre |
| BD_Comprobantes | datos (hechos) | Una fila por línea de comprobante (débito/crédito por cuenta y tercero) |
| Calc_Cuadre | cálculo | Cuadre débito vs crédito por número de comprobante |
| Calc_LibroDiario | cálculo | Libro diario en orden de registro |
| Calc_LibroMayor | cálculo | Movimiento y saldo por cuenta |
| Calc_BalancePrueba | cálculo | Balance de prueba (saldo inicial, débitos, créditos, saldo final) |
| Dashboard | dashboard | Cuadre global, volumen de movimientos y composición por tipo de comprobante |

## Modelo de datos (Power BI)
Modelo en **estrella**: la tabla de hechos `BD_Comprobantes` se relaciona con la dimensión `BD_PUC` por el campo `cuenta` ↔ `codigo`.

**BD_PUC** (dimensión cuenta) — encabezados en fila 1:
| Columna | Significado |
|---------|-------------|
| codigo | Código PUC (p. ej. 110505) |
| nombre | Nombre de la cuenta |
| clase | Clase con dígito y nombre (`1 Activo`, `5 Gasto`, …) |
| grupo | Grupo (`11 Disponible`, …) |
| naturaleza | `Debito` o `Credito` (define el signo del saldo) |

**BD_Comprobantes** (tabla de hechos, una fila por línea de asiento) — encabezados en fila 1:
| Columna | Significado |
|---------|-------------|
| fecha | Fecha del comprobante |
| comprobante | Consecutivo (CV-001, CC-001, RC-001…) — clave del cuadre |
| tipo | Tipo de comprobante (Factura venta, Factura compra, Nómina, Recibo de caja, Comprobante egreso, Nota contable) |
| cuenta | Código PUC → relación con BD_PUC |
| nombre_cuenta | `=IFERROR(VLOOKUP(cuenta;BD_PUC!A:B;2;FALSE);"")` |
| tercero | Nombre del tercero |
| nit_tercero | NIT/identificación |
| debito / credito | Valores del movimiento |
| descripcion | Glosa |
| mes | `=TEXT(fecha;"YYYY-MM")` (para segmentar) |
| clase | `=LEFT(cuenta;1)` (dígito de clase, para Power BI) |

**Conexión en Power BI:** importar BD_Comprobantes (hechos) y BD_PUC (dimensión); relación `cuenta → codigo` (muchos a uno). Medidas DAX de débitos, créditos y saldo por clase replican el balance.

## Metodología y fórmulas clave
- **Cuadre por comprobante (Calc_Cuadre):** débito `=SUMIF(BD_Comprobantes!B:B;comprobante;H:H)`, crédito `=SUMIF(...;I:I)`, diferencia `=B-C` y semáforo `=IF(ROUND(dif;0)=0;"CUADRA";"DESCUADRE")`. Todo comprobante debe cuadrar antes de leer cualquier libro.
- **Libro Diario (Calc_LibroDiario):** espejo en orden de registro de BD_Comprobantes (fecha, comprobante, cuenta, tercero, débito, crédito), con `=IF(...="";"";…)` para no arrastrar filas vacías.
- **Libro Mayor (Calc_LibroMayor):** por cuenta, débitos `=SUMIF(BD_Comprobantes!D:D;cuenta;H:H)`, créditos `=SUMIF(...;I:I)` y saldo según naturaleza: `=IF(naturaleza="Debito"; SI+Db-Cr ; SI-Db+Cr)`.
- **Balance de Prueba (Calc_BalancePrueba):** trae código, nombre, clase `=LEFT(...;1)`, saldo inicial débito/crédito y los movimientos y saldo del Libro Mayor. El total de débitos debe igualar el total de créditos.

## Cómo usarla
1. Cargar el **catálogo de cuentas** del cliente en BD_PUC (código, nombre, clase, grupo, naturaleza).
2. Diligenciar **Parametros**: razón social, NIT, periodo, moneda, UVT del año y umbrales de descuadre tolerado/alerta.
3. Registrar cada línea de asiento en **BD_Comprobantes** (un débito y su contrapartida en crédito comparten el mismo número de comprobante).
4. Verificar en **Calc_Cuadre** que cada comprobante diga "CUADRA".
5. Los libros (Diario, Mayor, Balance de Prueba) y el **Dashboard** se recalculan solos.

## Interpretación del dashboard
KPIs: **Total Débitos**, **Total Créditos**, **# Comprobantes** y **Descuadre $**. Gráficos: movimiento por tipo de comprobante, débito vs crédito por clase (1 a 7) y conteo de cuentas con movimiento. **Semáforo de cuadre global:** verde si débitos = créditos (descuadre ≤ tolerado en Parametros), ámbar si el descuadre ≤ umbral de alerta, rojo si lo supera. La igualdad débito = crédito por clase es el control maestro.

## Errores comunes / controles
- **Comprobante descuadrado:** falta una contrapartida o un valor está mal; Calc_Cuadre lo marca como "DESCUADRE" — corregir antes de seguir.
- **Cuenta sin naturaleza correcta** en BD_PUC: el saldo del Libro Mayor sale con signo invertido.
- **Cuenta no existente** en BD_PUC: nombre_cuenta queda en blanco; agregar la cuenta antes de causar.
- Incluir filas "SALDO INICIAL" dentro de los movimientos infla los débitos/créditos del periodo; sepáralas (regla operativa C.2).
- El total de débitos del Balance de Prueba debe igualar el total de créditos; si no, hay un descuadre acumulado.

## Relacionado
- *MOC - Plantillas Pro*
- *Estandar de Plantillas FYT*
- [[Aux 02 - Partida Doble y Asientos Contables]]
- [[Aux 23 - Balance de Prueba y Libro Auxiliar]]
- [[02-AuxiliarContable-Senior]]
