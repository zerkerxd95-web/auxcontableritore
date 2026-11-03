---
tipo: plantilla
tags: [ritore, plantilla, control, cumplimiento, tributario]
archivo: Suite Excel Pro/29_Control_Maestro_de_Obligaciones.xlsx
estado: vigente
fecha: 2026-06-08
---
# Plantilla 29 - Control Maestro de Obligaciones

## Para qué sirve y a qué cliente
Es el **calendario de cumplimiento vivo de toda la firma**: un tablero único donde FYT controla TODAS las obligaciones tributarias y societarias de sus **56 clientes** a lo largo del año (IVA F-300, Retención F-350, Anticipo Simple F-2593, RST anual F-260, Renta PJ F-110, Renta PN F-210, Exógena, ICA, EEFF, PILA, Nómina electrónica). No es para un cliente: es la herramienta interna de control de gestión que **previene la sanción por extemporaneidad (Art. 641 ET)** — 5 % del impuesto por mes o fracción de retraso, mínimo 10 UVT — y la **ineficacia de la retención sin pago total (Art. 580-1 ET)**. Es la defensa #1 contra el incumplimiento de plazos. Base de datos + dashboard + Power BI ready. Semáforo dinámico con HOY().

## Estructura del libro (hoja → capa → contenido)
| Hoja | Capa | Contenido |
|------|------|-----------|
| Instrucciones | Servicio | Qué es, convención de celdas, cómo se carga y la **rutina semanal** (lunes revisar/asignar, viernes verificar) que hace que el control proteja. |
| Guia Power BI | Servicio | Conexión de las tres tablas `BD_`; modelo estrella; medidas DAX (Pendientes, Vencidas, % Cumplimiento). |
| Parametros | Parámetros | Año de control, fecha de hoy (dinámica), días de alerta ámbar (7) y rojo (3), UVT, sanción mínima Art. 641, margen mínimo de presentación. Nombres definidos `Anio`, `Hoy`, `DiasAmbar`, `DiasRojo`. |
| BD_Clientes | Datos (dimensión) | Los 56 clientes reales: id, cliente, NIT, dos últimos dígitos (fórmula), tipo, régimen, responsable tributario, periodicidad IVA, agente de retención, obligado exógena, responsable interno. |
| BD_Calendario | Datos (dimensión) | 41 vencimientos base 2026 por obligación, periodicidad, periodo, fecha límite, rango de dígitos NIT y norma fuente (Decreto 2229/2023 + calendario DIAN 2026). |
| BD_Estado | Datos (hechos) | El corazón: una fila por (cliente × obligación × periodo) con estado, fecha de presentación, responsable y observación. Filas EJEMPLO en crema. |
| Calc_Vencimientos | Cálculo | Días restantes = fecha límite − HOY(); semáforo CRÍTICO/ALERTA/OK con formato condicional. |
| Calc_Semaforo_Cliente | Cálculo | Por cliente: obligaciones registradas, pendientes, vencidas, próxima fecha límite y estado general. |
| Calc_Cumplimiento | Cálculo | % de obligaciones presentadas a tiempo (indicador madre), avance del periodo, vencidas sin presentar, extemporáneas. |
| Dashboard | Presentación | KPIs (esta semana, vencidas, pendientes, % cumplimiento), semáforo global, 4 gráficos (vencimientos por mes, estado, por responsable, top pendientes) y la tabla filtrable "esta semana". |

## Modelo de datos (Power BI)
**Hechos: `BD_Estado`** (un registro por cliente × obligación × periodo):

| Columna | Significado | Tipo |
|---------|-------------|------|
| id | Consecutivo | Número |
| cliente | Nombre del cliente (clave hacia BD_Clientes) | Texto |
| obligacion | Obligación (clave hacia BD_Calendario) | Texto |
| periodo | Periodo gravable / cuota | Texto |
| fecha_limite | Vencimiento aplicable a ese cliente | Fecha |
| estado | Pendiente / En proceso / Presentado / Pagado / No aplica | Texto |
| fecha_presentacion | Fecha real de presentación | Fecha |
| responsable | Responsable interno que ejecuta | Texto |
| observacion | Nota de control | Texto |

**Dimensiones:** `BD_Clientes` (clave `cliente`) y `BD_Calendario` (clave `obligacion`). **Esquema estrella:** BD_Estado al centro; una dimensión Calendario de fechas (CALENDARAUTO) sobre `fecha_limite` y `fecha_presentacion`. **DAX clave:** `Vencidas = CALCULATE(COUNTROWS(BD_Estado), BD_Estado[fecha_limite] < TODAY(), NOT(BD_Estado[estado] IN {"Presentado","Pagado","No aplica"}))`; `% Cumplimiento = DIVIDE(CALCULATE(COUNTROWS(BD_Estado), BD_Estado[fecha_presentacion] <= BD_Estado[fecha_limite], BD_Estado[estado] IN {"Presentado","Pagado"}), [Presentadas])`.

## Metodología y fórmulas clave
### Semáforo dinámico (HOY)
- `Dias restantes = fecha_limite − HOY()` (Calc_Vencimientos, celda B4 = `=TODAY()`).
- Estado del semáforo: `Presentado`/`Pagado` → **OK**; `No aplica` → **N/A**; si días ≤ `DiasRojo` (3) o ya venció → **CRÍTICO**; si días ≤ `DiasAmbar` (7) → **ALERTA**; en otro caso → **OK**. Formato condicional pinta verde/ámbar/rojo.
- Cambia solo cada día al abrir el archivo: no hay que tocar nada.

### Cumplimiento de la firma
- **Presentadas a tiempo** = filas con `fecha_presentacion <= fecha_limite` (SUMPRODUCT). **% Cumplimiento = a tiempo / presentadas.** Meta: 100 %.
- **Vencidas sin presentar** = `fecha_limite < HOY()` y estado distinto de Presentado/Pagado/No aplica — son las que disparan la sanción.

### Calendario base 2026 (BD_Calendario)
- Cargado del *INICIO* y los proyectos de obligaciones, con las ventanas del **Decreto 2229/2023** y el **calendario DIAN 2026** por último dígito (o dos últimos para exógena/renta PN). La fecha base es el **inicio de la ventana**; ajustar por NIT con la columna `rango_digitos_NIT`. Las casillas con `[VERIFICAR]` deben confirmarse contra el `Calendario_Tributario_2026.pdf` de la DIAN.

## Cómo usarla (paso a paso)
1. En **Parametros** fije el **año de control** y los días de alerta ámbar/rojo (defecto 7/3).
2. En **BD_Clientes** complete los NIT en blanco y ajuste régimen, periodicidad IVA, agente de retención, obligado exógena y responsable interno de cada cliente.
3. En **BD_Calendario** confirme cada fecha base contra el calendario DIAN del año y la ventana por dígito de NIT.
4. En **BD_Estado** registre una fila por cada (cliente × obligación × periodo) que aplique. Reemplace las filas EJEMPLO (crema) por las reales.
5. **Rutina semanal:** lunes revise `Calc_Vencimientos` y el `Dashboard`, asigne y pase a "En proceso"; al presentar ponga "Presentado/Pagado" y la fecha real; viernes verifique que nada de la semana siga pendiente.

## Interpretación del dashboard
- **Tarjetas KPI:** Esta semana (lo que vence en ≤ 7 días sin presentar), Vencidas, Pendientes, % Cumplimiento a tiempo.
- **Semáforo global:** rojo si hay vencidas, ámbar si algo vence esta semana, verde si está al día.
- **Gráficos:** vencimientos por mes (carga de trabajo), estado de obligaciones (torta), obligaciones por responsable interno (balance de cargas), clientes con más pendientes (top 5).
- **Tabla "esta semana":** filtrable; úsela cada lunes para repartir el trabajo.

## Errores comunes / controles
- **No registrar el periodo:** sin la fila en BD_Estado el control no "ve" la obligación; un cliente obligado no puede quedar sin sus filas del año.
- **Olvidar la fecha de presentación:** sin ella, el % de cumplimiento a tiempo no se calcula y la obligación sigue contando como pendiente.
- **Usar "Presentado" sin pago en retención:** Art. 580-1 ET — la declaración sin pago total es ineficaz; para F-350 use "Pagado" solo cuando esté pagada.
- **Fecha base sin ajustar por NIT:** la columna `fecha_limite` de BD_Estado debe ser la del cliente según su dígito, no la base genérica de BD_Calendario.
- **No revisar cada semana:** la herramienta solo protege con la rutina semanal; un tablero sin disciplina no previene la sanción.

## Relacionado
*MOC - Plantillas Pro* · *Estandar de Plantillas FYT* · *Proyecto - Control de Obligaciones* · *Tablero de Alertas y Pendientes* · *01-Orquestador-Master* · *27-InboundManager-GoogleWorkspace-Senior*
