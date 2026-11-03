---
tipo: plantilla
tags: [ritore, plantilla, contable]
archivo: Suite Excel Pro/24_PUC_Interactivo.xlsx
estado: vigente
fecha: 2026-06-08
---
# Plantilla 24 - PUC Interactivo

## Para qué sirve y a qué cliente
**Plan Único de Cuentas navegable** (Decreto 2650/1993) con catálogo de cuentas, saldos de prueba y, sobre todo, la **matriz de mapeo cuenta → formato → concepto de exógena**. Sirve como referencia maestra de codificación contable y como puente entre la contabilidad y la información exógena DIAN: por cada cuenta del PUC indica a qué formato (1001, 1003, 1005/1006, 1007, 1008/1009, 1010, 2276…) y concepto va. Útil para cualquier cliente y como herramienta interna del auxiliar contable y del especialista en exógena.

## Estructura del libro
| Hoja | Capa | Contenido |
|------|------|-----------|
| Instrucciones | servicio | Qué es y cómo se usa |
| Guia Power BI | servicio | Conexión de BD_PUC y BD_Saldos |
| BD_PUC | datos (dimensión) | Catálogo completo del PUC con clase, grupo, tipo y formato exógena |
| BD_Saldos | datos (hechos) | Saldos por cuenta y periodo |
| Calc_Estructura | cálculo | Conteo y saldo de cuentas por clase |
| Calc_MapeoExogena | cálculo / referencia | Matriz cuenta PUC → formato DIAN → concepto |
| Dashboard | dashboard | Navegador por clase y distribución del PUC |

## Modelo de datos (Power BI)
**BD_PUC** es una tabla con formato de tabla de Excel (`BD_PUC[...]`), encabezados en fila 4:
| Columna | Significado |
|---------|-------------|
| codigo | Código de la cuenta (1, 11, 1105, 110505…) |
| nombre | Nombre de la cuenta |
| clase | Dígito de clase (1 a 7) |
| grupo / cuenta | Niveles intermedios del PUC |
| naturaleza | `Debito` / `Credito` |
| tipo | `Balance` o `Resultado` |
| formato_exogena | Formato/concepto DIAN al que va la cuenta (p. ej. `F-1001 concepto 5004`, `F-1003`, `F-1005 / F-1006 (IVA desc./gen.)`, `F-1007`, `F-1008`, `F-1010`, `F-2276`…) |

**BD_Saldos** (hechos) — `codigo`, `periodo` (YYYY-MM), `saldo`, `origen`. Se relaciona con BD_PUC por `codigo`.

**Conexión en Power BI:** importar BD_PUC (dimensión) y BD_Saldos (hechos); relación `codigo→codigo`. El campo `formato_exogena` permite agrupar saldos por formato DIAN.

## Metodología y fórmulas clave
- **Estructura por clase (Calc_Estructura):** número de cuentas `=COUNTIFS(BD_PUC[clase];clase;BD_PUC[cuenta];"<>")` y saldo de la clase `=SUMPRODUCT((LEFT(BD_Saldos[codigo];1)=TEXT(clase;"0"))*BD_Saldos[saldo])`.
- **Matriz de mapeo (Calc_MapeoExogena):** tabla de referencia Formato → qué contiene → cuentas PUC típicas → concepto/regla → fuente. Ejemplos cargados: 5110/5210 → F-1001 honorarios 5002; 5135/5235/5145 → F-1001 servicios 5004; 5120/5220 → arrendamientos 5005; clase 53 → columna NO deducible del F-1001; 135515/135517/135518 → F-1003 (1301–1309); 2408 débito/crédito → F-1005/F-1006; 41xx/42xx → F-1007; 1305/1325/1330/1380 → F-1008 (saldo por tercero); 2205/2335/2105 → F-1009; 3105/3115/3205 → F-1010; 5105/5205/2510/2515 → F-2276; 2805/2815 → F-1647.
- **Regla de cuantías menores:** pagos acumulados por beneficiario < 3 UVT del año a reportar → id `222222222`, razón `CUANTÍAS MENORES`, tipo doc `43`. La clase 53 marca no deducibilidad (columna O del F-1001).

## Cómo usarla
1. Cargar (o usar) el **catálogo PUC** en BD_PUC, completando `tipo` (Balance/Resultado) y `formato_exogena` por cuenta.
2. Cargar **saldos** del periodo en BD_Saldos.
3. Usar **Calc_MapeoExogena** como guía para asignar cada cuenta a su formato y concepto al armar la exógena.
4. Consultar la distribución por clase en **Dashboard** (navegador).

## Interpretación del dashboard
KPIs: **Total cuentas (≥4 dígitos)**, **Cuentas de balance**, **Cuentas de resultado** y **Cuentas mapeadas a exógena**. Navegador: se elige una clase (1 a 7) y muestra sus cuentas con código, nombre, grupo, naturaleza, `formato_exogena` y saldo de BD_Saldos. La proporción de cuentas mapeadas a exógena es un indicador de preparación para el reporte anual.

## Errores comunes / controles
- **Cuenta sin `formato_exogena`** cuando sí debe reportarse: queda fuera del cruce; revisar contra Calc_MapeoExogena.
- Asignar un concepto "a ojo" en lugar de seguir la matriz (especialmente el cajón de sastre 5016): documentar toda excepción.
- **Confundir el dígito de clase** (tipo Balance vs Resultado) altera la estructura del balance.
- La matriz es **referencia**, no presenta exógena: la generación efectiva se hace en la Plantilla 18 (Exógena Maestra) con los datos por tercero.

## Relacionado
- *MOC - Plantillas Pro*
- *Estandar de Plantillas FYT*
- [[Aux 01 - Plan de Cuentas PUC]]
- *Subskill B4 - Mapear Cuenta Formato Concepto*
