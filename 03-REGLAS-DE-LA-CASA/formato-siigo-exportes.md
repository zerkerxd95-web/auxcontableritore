---
name: formato-siigo-exportes
description: "REGLA — los exportes contables se entregan en DOS formatos elegibles: S (Siigo Nube) y W (World Office); estructura exacta de ambos verificada contra exports reales, incluida la diferencia de signos entre ellos."
metadata: 
  node_type: memory
  type: feedback
---

El titular estandarizó (2026-08-28) que los exportes de balance de prueba y libro auxiliar de NUESTROS software (familia jmlr_: *(nota interna de la firma)*, *(nota interna de la firma)*) y de cualquier entregable futuro usen el formato de **Siigo Nube**, porque muchas de sus empresas usan Siigo.

**Why:** uniformidad con los archivos que ya circulan entre sus clientes y otros contadores; papeles de trabajo intercambiables.

**How to apply:** estructura extraída de exports reales (SALÓN DE BELLEZA I 2025):

*Balance de prueba general* (hoja Sheet1, 8 cols A:H): R1 vacía; R2 título "Balance de prueba general" (negrita 30); R3 razón social; R4 `NIT-DV`; R5 "De <Mes> <Año> a <Mes> <Año>"; R6-7 vacías (R1-6 combinadas A:H, negrita 14). R8 encabezados con relleno `FFF1F4F9`: `Nivel | Transaccional | Código cuenta contable | Nombre cuenta contable | Saldo inicial | Movimiento débito | Movimiento crédito | Saldo final`. Cuerpo jerárquico en cascada: Clase(1 díg)/Grupo(2)/Cuenta(4)/Subcuenta(6)/Auxiliar(8), `Transaccional=Sí` solo en el nivel de registro. Saldos con signo: pasivo/patrimonio/ingresos NEGATIVOS. Al final: fila vacía, `Total general` solo con débitos y créditos, fila vacía, `Procesado en: <fecha>`. Números `#,##0.00`, textos `@`. Anchos: A 15.6, B 16.4, C 14.7, D 50.

*Movimiento auxiliar por cuenta contable* (16 cols A:P): mismo encabezado (R5 con días: "De Enero 01 2025 a ..."). R8: `Código contable | Cuenta contable | Comprobante | Secuencia | Fecha elaboración | Identificación | Sucursal | Nombre del tercero | Descripción | Detalle | Centro de costo | Saldo inicial | Débito | Crédito | Saldo Movimiento | Saldo total cuenta`. Fila de grupo por cuenta (negrita): A=`Cuenta contable: <código><nombre>`, L=saldo inicial, M/N=totales, P=saldo total. Filas de detalle: fecha dd/mm/yyyy, Identificación=NIT sin DV, Sucursal=0, O=saldo corrido dentro de la cuenta, L y P vacíos. Cierre: `Total general` (M/N), `Procesado en:`.

Implementado en `js/siigo-export.js` + `js/puc-niveles.js` de ambas apps. Muestras de referencia: carpeta SALÓN DE BELLEZA I (Balance de prueba general (1).xlsx, Movimiento auxiliar por cuenta contable (27).xlsx).

---

## Segundo formato: WORLD OFFICE ("W") — 2026-09-29

El titular estandarizo que los software entreguen los mismos dos informes en DOS formatos, porque unos contadores trabajan con Siigo y otros con World Office: **BALANCE DE PRUEBA S / LIBRO AUXILIAR S** (Siigo) y **BALANCE DE PRUEBA W / LIBRO AUXILIAR W** (World Office), elegibles con un selector en Contabilidad. Muestras de referencia (ROJO): `TRABAJOS Y REQUERIMIENTOS/WO PARA SOFTWARE CONTABLE/` (BP y LA 2025 de EXPORTADORA DE SERVICIOS B).

**DIFERENCIA CLAVE DE SIGNOS:** Siigo usa debito-positivo (pasivo, patrimonio e ingresos NEGATIVOS). World Office muestra cada cuenta **en su naturaleza y en positivo**, por eso su "Total general" del balance NO da cero sino la suma de los saldos. Verificado: caja general inicial 887.062 + debitos 92.822.427 - creditos 83.171.542 = final 10.537.947. Un mismo periodo se ve distinto en cada formato y ES correcto.

*Balance de prueba W* — DOS hojas. `Tabla` (5 cols A:E): R1 razon social, R2 `NIT <nit>-<dv>`, R3 `Balance de Prueba entre el DD/MM/YYYY y el DD/MM/YYYY`, R4 `Elaborado Bajo Normas Locales  `, todas combinadas A:E, negrita 10, CENTRADAS; R5 vacia; R6 encabezados sin negrita y sin relleno (A vacia | Saldo Inicial | Debitos | Creditos | Saldo Final). Cuerpo en cascada con `codigo nombre` en la MISMA celda A: clase(1) / grupo(2) / cuenta(4) / transaccional / una fila de DETALLE POR TERCERO con valores / `Total <cuenta>` / `Total <grupo>` / `Total <clase>`, y al final `Total general`. Los renglones sin tercero se agrupan en una fila con el nombre de la cuenta. Formato contable `_(* #,##0.00_);_(* \(#,##0.00\);_(* "-"??_);_(@_)`. Anchos A 73.6, B 18.9.
Hoja `ExportarAExcel` (9 cols, encabezado negrita): `CodCuentaNivel1 | CodCuentaNivel2 | CodCuentaNivel3 | CodCuentaNivel5 | SaldoInicialDet | TotalDebitosDet | TotalCreditosDet | SaldoFinalDet | Cuenta o Tercero P`. Nivel5 = la cuenta transaccional completa (6, 8 o 10 digitos). Formato `#,##0.00`. Anchos A 44.4, B 45.1, C 68.7, D 73.6, E 16.6, F 17.7, G 18.3, H 15.4, I 93.6.

*Libro auxiliar W* — UNA hoja `ExportarAExcel` (9 cols A:I): R1 razon social (A1:I1), R2 `Libro Auxiliar entre el DD/MM/YYYY y el DD/MM/YYYY` (A2:I2), R3 vacia, R4 encabezados negrita formato `@`: `Cuenta | Tercero | Fecha | Nota | Cheque | Doc Num | Debitos | Creditos | Saldo`. Por cuenta: fila de apertura con A=`codigo NOMBRE`, C=fecha del dia ANTERIOR a desde, D=`SALDO INICIAL`, el inicial en Debitos o Creditos segun naturaleza; filas de detalle con A vacia y saldo corrido en I; cierre `Total <codigo NOMBRE>`. Al final `Total general` (G,H,I) y `Total Movimientos Debitos y Creditos` (G,H, sin I). Fuente Calibri 10. Anchos A 89.1, B 82.4, C 10.1, D 120.0, E 8.9, F 14.6, G 14.7.

Implementado primero SOLO en CENTRO CULTURAL M (app contable v2.2.0, `js/wo-export.js` = `AG.wo`, mismas firmas que `AG.siigo`) para revisarlo en la nube antes de replicarlo a CONSTRUCTORA AA y RESTAURANTE R.

**REGLA DE MARCA (29-sep-2026, decision del titular):** en el software MAESTRO y en todo lo que se replique a clientes, la interfaz NO nombra a Siigo ni a World Office — solo **"Formato S"** y **"Formato W"**, por prudencia frente a derechos de autor. Aplicado en CONSTRUCTORA AA v7.2.1: botones `⬇ BALANCE DE PRUEBA S` / `⬇ LIBRO AUXILIAR S`, tooltips que describen la estructura sin nombrar marcas, nombre del archivo descargado (`Balance_de_prueba_general_S_...`), toasts, comentarios de cabecera de `siigo-export.js` y `puc-niveles.js`, y README. Se conservan los identificadores internos (`AG.siigo`, `cb-siigo-*`, el nombre del archivo `siigo-export.js`) porque no los ve el usuario; renombrarlos queda como opcion pendiente. La comparacion competitiva del README (linea ~33) se dejo: nombrar competidores en una comparacion de mercado es uso nominativo normal.
CENTRO CULTURAL M conserva los nombres de marca por decision expresa del titular (es cliente propio, uso interno). RESTAURANTE R todavia los tiene y es un despliegue a cliente: PENDIENTE decidir si se neutraliza tambien.

**TRAMPA AL LEER UN LIBRO AUXILIAR W (11-oct-2026):** el export intercala **filas `Total <codigo NOMBRE>`** (una por cuenta, 109 en el de EXPORTADORA DE SERVICIOS B) y esas filas repiten los totales de la cuenta E INCLUYEN el saldo inicial dentro de la columna Debitos. Si el parser no las descarta, los debitos del semestre dan **5,4 veces** lo real (9.677 millones contra 1.789) y nada amarra con el BP. Regla: descartar toda fila cuya columna A, en mayusculas y sin espacios, empiece por `TOTAL`, ANTES de cualquier otra cosa; luego confirmar que debitos = creditos y que el total coincide con el del balance de prueba. Es una trampa distinta de la de los saldos iniciales (ver *(nota interna de la firma)*): alli el error era tratar la fila de CABECERA de cuenta como movimiento, aqui es tratar la fila de CIERRE como movimiento. Las dos juntas: la cabecera trae el saldo inicial y la de cierre trae los totales, asi que el unico movimiento real es la fila que no es ninguna de las dos.
