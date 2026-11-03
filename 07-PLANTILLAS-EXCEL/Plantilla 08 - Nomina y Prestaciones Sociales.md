---
tipo: plantilla
tags: [ritore, plantilla, nomina, prestaciones-sociales, seguridad-social]
archivo: Suite Excel Pro/08_Nomina_y_Prestaciones_Sociales.xlsx
estado: vigente
fecha: 2026-06-08
---
# Plantilla 08 - Nomina y Prestaciones Sociales

## Para qué sirve y a qué cliente (el servicio que habilita)
Suite de **liquidación de nómina, aportes patronales y prestaciones sociales** para Colombia, con valores 2026 precargados. Liquida el devengado y neto a pagar mensual por empleado, los aportes a cargo del empleador (con exoneración Art. 114-1), la provisión mensual de prestaciones sociales y la liquidación definitiva al retiro (incluida indemnización Art. 64 CST). Habilita el servicio de **nómina y seguridad social**: el cliente PYME conoce su costo laboral total, su carga prestacional y la causación contable de nómina. Es base de datos + herramienta de presentación + fuente lista para Power BI. Moneda COP, vigencia 2026.

## Estructura del libro (hoja → capa → contenido)
| Hoja | Capa | Contenido |
|------|------|-----------|
| Instrucciones | Servicio | Qué es, arquitectura por capas, cómo usar. |
| Guia Power BI | Servicio | Conexión modelo estrella `BD_Empleados` (dim) + `BD_Novedades` (hechos); DAX. |
| Parametros | Parámetros | Valores 2026, % aportes/prestaciones, tabla ARL por clase de riesgo, escala FSP. |
| BD_Empleados | Datos (dim) | Maestro de empleados (cédula = llave). |
| BD_Novedades | Datos (hechos) | Novedades por empleado y periodo (días, extras, comisiones, incapacidades). |
| Calc_Liquidacion | Cálculo | Liquidación mensual: devengado, IBC, deducciones, neto a pagar. |
| Calc_AportesPatronales | Cálculo | Salud, pensión, ARL, parafiscales con exoneración 114-1; costo total empleador. |
| Calc_Prestaciones | Cálculo | Provisión mensual de cesantías, intereses, prima y vacaciones. |
| Calc_Liquidacion_Definitiva | Cálculo | Liquidación al retiro: prestaciones causadas + indemnización si aplica. |
| Dashboard | Presentación | KPIs de costo laboral + semáforo IBC vs tope 25 SMMLV. |

## Modelo de datos (Power BI)
**Dimensión: `BD_Empleados`** (rango `A4:I10`, cédula = llave):

| Columna | Significado | Tipo |
|---------|-------------|------|
| cedula | Identificación (llave de relación) | Entero |
| nombre | Nombre del empleado | Texto |
| cargo | Cargo | Texto |
| centro_costo | Centro de costo (Administración, Ventas, Producción…) | Texto |
| salario_base | Salario mensual base | Número (COP) |
| fecha_ingreso | Fecha de ingreso | Fecha |
| tipo_contrato | Indefinido / Fijo / Obra | Texto |
| clase_riesgo | Clase de riesgo ARL I–V | Texto |
| aux_transporte | Si/No (aplica a quienes devengan ≤ 2 SMMLV) | Texto |

**Tabla de hechos: `BD_Novedades`** (rango `A4:I10`, una fila por empleado y periodo):

| Columna | Significado | Tipo |
|---------|-------------|------|
| periodo | AAAA-MM | Texto |
| cedula | Identificación (FK → BD_Empleados) | Entero |
| dias | Días laborados (mes comercial 30) | Entero |
| horas_extra | Cantidad de horas extra | Número |
| valor_hora_extra | Valor unitario de la hora extra (0 = se estima) | Número (COP) |
| comisiones | Comisiones del periodo | Número (COP) |
| incapacidades | Días de incapacidad | Número |
| otros_devengados | Otros devengos | Número (COP) |
| otras_deducciones | Otras deducciones | Número (COP) |

**Esquema estrella:** relación `BD_Novedades[cedula]` → `BD_Empleados[cedula]` (muchos a uno). Dimensión Calendario (`CALENDARAUTO()`) por `periodo`. **Conexión:** Obtener datos → Excel → marcar SOLO `BD_Empleados` y `BD_Novedades` (nunca importar `Calc_*` ni `Dashboard`). **DAX:** `Headcount = DISTINCTCOUNT(BD_Empleados[cedula])`, `Total Comisiones = SUM(BD_Novedades[comisiones])`, `Salario Base Total = SUM(BD_Empleados[salario_base])`, `Costo Empleador = [Devengado]+[Aportes Patronales]+[Provisiones]`, `Carga Prestacional % = DIVIDE([Costo Empleador]-[Devengado],[Devengado])`.

## Metodología y fórmulas clave

### Parámetros 2026 verificados
- **SMMLV 2026:** $1.750.905 (Decreto 1469/2025). **Auxilio de transporte 2026:** $249.095 (Decreto 1470/2025, hasta 2 SMMLV). **UVT 2026:** $52.374.
- Tope IBC: 25 SMMLV. Umbral exoneración 114-1: < 10 SMMLV. Mes base: 30 días.

### Liquidación mensual (Calc_Liquidacion)
- **Salario proporcional** = salario_base / 30 × días.
- **Horas extra:** `horas × valor_hora`; si no se digita valor_hora, se estima a `(salario/240) × 1,25`.
- **Auxilio de transporte:** se paga si el empleado lo tiene marcado y su salario ≤ 2 SMMLV, prorrateado por días.
- **Total devengado** = salario proporcional + extras + comisiones + otros + auxilio.
- **IBC** = `MAX(SMMLV, MIN(devengado SIN auxilio, 25 SMMLV))` — el auxilio de transporte **no** hace parte del IBC.
- **Deducciones trabajador:** Salud 4% del IBC, Pensión 4% del IBC, **FSP** (Fondo de Solidaridad Pensional) por escala si IBC ≥ 4 SMMLV (1% desde 4, escalando a 2% desde 20), + otras deducciones.
- **Neto a pagar** = devengado − total deducciones.

### Aportes patronales (Calc_AportesPatronales) — exoneración Art. 114-1
- **Exonera** = "Si" si salario base < 10 SMMLV. Si exonera: **Salud 8,5%, SENA 2% e ICBF 3% quedan en $0**.
- Siempre se pagan: **Pensión 12%**, **ARL** (por clase de riesgo: I 0,522% · II 1,044% · III 2,436% · IV 4,35% · V 6,96%), **Caja de Compensación 4%**.
- **Costo total empleador** = devengado + total aportes + provisión de prestaciones.

### Provisión de prestaciones (Calc_Prestaciones) — provisión mensual
- **Cesantías** 8,33% sobre (salario + auxilio de transporte).
- **Intereses a cesantías** 1% mensual sobre las cesantías del mes.
- **Prima de servicios** 8,33% sobre (salario + auxilio).
- **Vacaciones** 4,17% sobre el salario **SIN** auxilio ni horas extra.

### Liquidación definitiva (Calc_Liquidacion_Definitiva)
Ingrese fecha de retiro y causal (azul). Calcula días con `DAYS360`. Cesantías = base × días/360; intereses = cesantías × días × 0,12/360; prima = base × MIN(días,180)/360; vacaciones = salario × días/720. **Indemnización Art. 64 CST**: si la causal contiene "sin justa", aprox. 30 días el primer año + 20 días por año adicional (contrato indefinido < 10 SMMLV). **Siempre verificar la indemnización con el Contador Titular** según contrato y antigüedad.

## Cómo usarla (paso a paso)
1. Revise **Parametros**: valores 2026 ya cargados; celdas amarillas = supuestos ajustables.
2. Reemplace las filas EJEMPLO (crema) de **BD_Empleados** con la nómina real (cédula es la llave).
3. Capture las novedades del mes en **BD_Novedades** (una fila por empleado y periodo, formato AAAA-MM).
4. Indique el periodo a liquidar en `Calc_Liquidacion!B3`.
5. Las hojas `Calc_*` y el Dashboard se recalculan solos. Para liquidación al retiro, llene fecha y causal en `Calc_Liquidacion_Definitiva`.

## Interpretación del dashboard
- **Tarjetas KPI:** Nómina total (devengado), Costo total empleador, Headcount, Costo promedio/empleado, y **% Carga prestacional** = (costo empleador − devengado) / devengado.
- **Semáforo IBC vs tope 25 SMMLV** por empleado: % del tope = IBC / (25 × SMMLV). Umbrales: **OK** < 90%, **ALERTA** ≥ 90%, **CRÍTICO** ≥ 100% (IBC topado). Sirve para detectar salarios altos cuyo IBC ya choca con el tope legal.

## Errores comunes / controles
- **Incluir el auxilio de transporte en el IBC:** no hace parte; las fórmulas lo excluyen, pero verificar al cargar datos manuales.
- **Olvidar la exoneración 114-1:** salud/SENA/ICBF van en $0 para devengados < 10 SMMLV; cargarlos infla el costo.
- **Horas extra sin valor unitario:** se estiman a (salario/240)×1,25; si el recargo real difiere (nocturna, festiva), digitar el valor_hora.
- **FSP:** solo aplica desde 4 SMMLV de IBC; revisar la escala en Parametros.
- **Indemnización:** la fórmula es una aproximación del Art. 64 CST; escalar al Contador Titular para contratos a término fijo o casos especiales.
- Verificar que el periodo de `Calc_Liquidacion!B3` coincida con el periodo cargado en `BD_Novedades`.

## Relacionado
*MOC - Plantillas Pro* · *Estandar de Plantillas FYT* · *Proyecto - Nomina y Seguridad Social* · [[Seguridad Social y Parafiscales]] · [[07-AuxiliarNomina-Senior]] · [[Aux 11 - Causacion de Nomina]]
