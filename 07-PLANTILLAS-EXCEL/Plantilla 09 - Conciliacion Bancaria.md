---
tipo: plantilla
tags: [ritore, plantilla, conciliacion-bancaria, tesoreria]
archivo: Suite Excel Pro/09_Conciliacion_Bancaria.xlsx
estado: vigente
fecha: 2026-06-08
---
# Plantilla 09 - Conciliacion Bancaria

## Para qué sirve y a qué cliente (el servicio que habilita)
Concilia el **extracto bancario contra los libros de contabilidad** e identifica las partidas conciliatorias del periodo (consignaciones en tránsito, cheques pendientes, notas débito/crédito no registradas). Funciona como base de datos de movimientos, motor de cruce y dashboard de control con semáforo de cuadre. Habilita el servicio mensual de **conciliación bancaria**: dejar la cuenta de bancos cuadrada y soportada, detectar GMF/comisiones no contabilizadas y rendimientos sin registrar. Cliente típico: cualquier empresa con cuenta bancaria activa. Moneda COP. Maneja varios meses filtrando por la columna `mes`.

## Estructura del libro (hoja → capa → contenido)
| Hoja | Capa | Contenido |
|------|------|-----------|
| Instrucciones | Servicio | Qué es, cómo usar, partidas conciliatorias típicas, lógica del cuadre. |
| Guia Power BI | Servicio | Conexión de `BD_Extracto` y `BD_Libros`; DAX. |
| Parametros | Parámetros | Empresa, cuenta, mes a conciliar, saldo inicial de libros. |
| BD_Extracto | Datos (hechos) | Movimientos del banco, una fila por movimiento. |
| BD_Libros | Datos (hechos) | Movimientos de contabilidad, una fila por movimiento. |
| Calc_Conciliacion | Cálculo | Cruce extracto↔libros por referencia; marca conciliado S/N. |
| Calc_Cuadre | Cálculo | Saldo extracto ± partidas = saldo libros ajustado; diferencia debe dar 0. |

> Nota: este libro **no tiene hoja Dashboard separada**; el dashboard de control (KPIs y semáforo) vive en el bloque RESULTADO de `Calc_Cuadre`.

## Modelo de datos (Power BI)
**Tabla de hechos 1: `BD_Extracto`** (rango `A4:G12`, movimientos del banco):

| Columna | Significado | Tipo |
|---------|-------------|------|
| mes | Periodo AAAA-MM | Texto |
| fecha | Fecha del movimiento | Fecha |
| descripcion | Descripción del banco | Texto |
| referencia | Referencia/documento (DEP, CHQ, PSE, GMF…) — **clave de cruce** | Texto |
| debito | Salida (banco debita) | Número (COP) |
| credito | Entrada (banco acredita) | Número (COP) |
| saldo | Saldo corrido (fórmula: saldo anterior + crédito − débito) | Número (COP) |

**Tabla de hechos 2: `BD_Libros`** (rango `A4:F11`, movimientos contables):

| Columna | Significado | Tipo |
|---------|-------------|------|
| mes | Periodo AAAA-MM | Texto |
| fecha | Fecha del comprobante | Fecha |
| comprobante | Número/referencia del comprobante — **clave de cruce** | Texto |
| tercero | Tercero del movimiento | Texto |
| debito | Entrada en libros (banco débito) | Número (COP) |
| credito | Salida en libros (banco crédito) | Número (COP) |

**Esquema estrella:** dos tablas de hechos (`BD_Extracto`, `BD_Libros`) ligadas a una dimensión Calendario (`CALENDARAUTO()`) por fecha; opcional dimensión Mes/Cuenta. **Conexión:** Obtener datos → Excel → marcar ambas tablas BD. **DAX:** `Creditos Extracto = SUM(BD_Extracto[credito])`, `Debitos Extracto = SUM(BD_Extracto[debito])`, `Movimiento Libros = SUM(BD_Libros[debito]) - SUM(BD_Libros[credito])`, `# Partidas pendientes = COUNTROWS(FILTER(Calc_Conciliacion,[conciliado]="N"))`.

## Metodología y fórmulas clave

### Cruce (Calc_Conciliacion)
Cada movimiento del extracto se busca en libros y viceversa **por la referencia/comprobante**:
- Bloque extracto (tabla `Marca_Extracto`): `en_libros = COUNTIF(BD_Libros[comprobante], referencia)`; `conciliado = "S"` si > 0, si no "N".
- Bloque libros (tabla `Marca_Libros`): `en_extracto = COUNTIF(BD_Extracto[referencia], comprobante)`; `conciliado = "S"/"N"`.
Las partidas con "N" son las **partidas conciliatorias** del periodo.

### Cuadre (Calc_Cuadre) — la lógica de oro
**Lado banco:**
`(+) Saldo final del extracto` `(+) Consignaciones en tránsito` (débitos de libros no en banco, `SUMIFS` de libros con conciliado="N") `(−) Cheques girados pendientes` (créditos de libros no en banco) `(=) SALDO BANCARIO AJUSTADO`.

**Lado libros:**
`(+) Saldo inicial libros` `(+) Débitos del periodo` `(−) Créditos del periodo` `(=) Saldo de libros sin ajustar`; luego `(−) Notas débito bancarias no registradas` (GMF, comisiones — débitos del extracto con conciliado="N") `(+) Notas crédito bancarias no registradas` (rendimientos) `(=) SALDO EN LIBROS AJUSTADO`.

**Resultado:** `DIFERENCIA = saldo bancario ajustado − saldo libros ajustado` → **debe ser 0**.

### Partidas conciliatorias típicas (de Instrucciones)
- **Consignaciones en tránsito:** registradas en libros, el banco aún no acredita → suman al saldo del banco.
- **Cheques girados pendientes de cobro:** en libros, no debitados por el banco → restan del saldo del banco.
- **Notas débito bancarias no registradas:** GMF (4x1000), comisiones, cuota de manejo → el banco ya cobró, faltan en libros.
- **Notas crédito bancarias no registradas:** rendimientos, abonos → el banco ya acreditó, faltan en libros.

## Cómo usarla (paso a paso)
1. Pegue el extracto del banco en **BD_Extracto** (fecha, descripción, referencia, débito, crédito; el saldo se calcula).
2. Pegue los movimientos de libros en **BD_Libros** (fecha, comprobante, tercero, débito, crédito). La **referencia del extracto** y el **comprobante de libros** deben coincidir para que el cruce funcione.
3. En **Parametros** indique empresa, cuenta bancaria, mes a conciliar y saldo inicial de libros del mes anterior.
4. **Calc_Conciliacion** marca cada partida como conciliada (S) o pendiente (N).
5. **Calc_Cuadre** muestra el cuadre y la diferencia (debe dar 0).

## Interpretación del dashboard
- **Estado del cuadre (Calc_Cuadre):** `Estado = IF(ABS(diferencia)<1, "CONCILIADO", "DESCUADRE")`. Verde si diferencia = 0; rojo si no.
- Las partidas marcadas "N" en `Calc_Conciliacion` son la lista de pendientes a contabilizar o a esperar del banco. Una conciliación correcta deja la diferencia en cero y todas las partidas "N" explicadas como partidas conciliatorias legítimas.

## Errores comunes / controles
- **Referencias que no coinciden** entre extracto y libros: el cruce es exacto por texto; un "CHQ-4501" vs "4501" no concilia. Homologar la referencia al pegar.
- **No registrar GMF, comisiones ni rendimientos:** aparecen como partidas "N" del extracto; deben contabilizarse para que la diferencia cierre en cero el mes siguiente.
- **Saldo inicial mal puesto:** el cuadre parte del saldo inicial de libros de `Parametros`; si está mal, todo descuadra.
- **Mezclar meses:** filtrar por columna `mes` o duplicar el libro por periodo; el cuadre asume un solo mes.
- Si la diferencia no da 0 y no hay partida conciliatoria que lo explique, hay un error contable o una partida no cargada → investigar, no forzar.

## Relacionado
*MOC - Plantillas Pro* · *Estandar de Plantillas FYT* · [[Aux 22 - Conciliacion Bancaria]] · [[03-AuxiliarConciliacionesBancarias-Senior]]
