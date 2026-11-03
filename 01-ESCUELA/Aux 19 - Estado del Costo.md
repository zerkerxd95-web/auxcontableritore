---
tipo: leccion
tags: [ritore, escuela, auxiliar, costos]
modulo: 5
estado: vigente
fecha: 2026-06-08
---

# Aux 19 - Estado del Costo

## Objetivo

Que el auxiliar arme el **estado de costos de producción y ventas** de una empresa manufacturera: materia prima consumida + mano de obra directa + CIF = costo de producción, ajustado por inventarios de producto en proceso y de producto terminado hasta llegar al **costo de ventas**. Y que entienda el papel de la **clase 7** del PUC como puente entre la nómina/las compras y los inventarios. Es la lección que conecta el módulo de inventarios con el *Proyecto - Informes de Costos y Costeo*.

## Marco conceptual y normativo

**La estructura (memorizarla):**

```
   Inventario inicial de MATERIA PRIMA (1405)
 + Compras de materia prima
 − Inventario final de materia prima
 = MATERIA PRIMA CONSUMIDA                      (clase 71)
 + MANO DE OBRA DIRECTA                          (clase 72)
 + COSTOS INDIRECTOS DE FABRICACIÓN (CIF)        (clase 73)
 = COSTO DE PRODUCCIÓN DEL PERIODO
 + Inventario inicial de PRODUCTO EN PROCESO (1410)
 − Inventario final de producto en proceso
 = COSTO DEL PRODUCTO TERMINADO
 + Inventario inicial de PRODUCTO TERMINADO (1430)
 − Inventario final de producto terminado
 = COSTO DE VENTAS (6120)
```

**Cuentas involucradas:**

| Cuenta | Contenido |
|---|---|
| 1405 | Materias primas |
| 1410 | Productos en proceso |
| 1430 | Productos terminados |
| 71 | Materia prima (consumo) |
| 72 | Mano de obra directa (nómina de planta — ver [[Aux 11 - Causacion de Nomina]]) |
| 73 | Costos indirectos: MOI, arriendo de planta, energía, depreciación de maquinaria, dotación |
| 6120 | Costo de ventas — industrias manufactureras (la 6135 es para comercio) |

- Las cuentas de la **clase 7** acumulan el costo durante el periodo y se **trasladan** a la 1410 (no van al estado de resultados directamente).
- **NIC 2 / Sección 13:** los CIF se asignan sobre **capacidad normal**; los desperdicios anormales, el almacenamiento innecesario y los gastos de administración y ventas **NO** son costo del producto — van al gasto (51xx/52xx).
- La nómina de producción va a la clase 7 con TODOS sus componentes (prestaciones de [[Aux 12 - Provisiones y Prestaciones Sociales]] incluidas): el costo real de la hora-hombre es ≈ 1,35 × el devengado.

## Paso a paso (con asientos)

**Caso tipo **Cliente - METALMECÁNICA T**** — manufactura metálica pequeña, año 2026 (cifras en $):

**1. Consumo de materia prima:** II 1405 = 20.000.000; compras del año = 80.000.000; IF (físico valorizado) = 15.000.000 → **MP consumida = 85.000.000**.

*Asiento del consumo (acumulado del periodo):*

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 7105 | Costos — materia prima | 85.000.000 | |
| 1405 | Materias primas | | 85.000.000 |

**2. Mano de obra directa del año = 30.000.000** (nómina de operarios con prestaciones y seguridad social patronal):

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 7205 | Costos — mano de obra directa | 30.000.000 | |
| 2505/2370/2610 | Nómina por pagar, aportes y provisiones | | 30.000.000 |

**3. CIF del año = 25.000.000** (arriendo de planta 12M, energía 6M, depreciación maquinaria 4M, MOI y dotación 3M):

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 7305 | Costos indirectos de fabricación | 25.000.000 | |
| 233525 / 1592 / 2505 | Por pagar, depreciación acumulada, nómina MOI | | 25.000.000 |

**4. Traslado a producto en proceso** (cierre de la clase 7): 85 + 30 + 25 = **costo de producción 140.000.000**:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 1410 | Productos en proceso | 140.000.000 | |
| 7105 | Materia prima | | 85.000.000 |
| 7205 | Mano de obra directa | | 30.000.000 |
| 7305 | CIF | | 25.000.000 |

**5. Producto terminado:** II PP = 10.000.000; IF PP = 12.000.000 → costo del PT del año = 10 + 140 − 12 = **138.000.000**:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 1430 | Productos terminados | 138.000.000 | |
| 1410 | Productos en proceso | | 138.000.000 |

**6. Costo de ventas:** II PT = 18.000.000; IF PT = 20.000.000 → costo de ventas = 18 + 138 − 20 = **136.000.000**:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 6120 | Costo de ventas — industrias manufactureras | 136.000.000 | |
| 1430 | Productos terminados | | 136.000.000 |

**7. El estado de costos de producción y ventas (el entregable):**

| Estado de costos 2026 — Metálicas (ejemplo) | $ |
|---|---|
| Inventario inicial de materia prima | 20.000.000 |
| (+) Compras de materia prima | 80.000.000 |
| (−) Inventario final de materia prima | (15.000.000) |
| **= Materia prima consumida** | **85.000.000** |
| (+) Mano de obra directa | 30.000.000 |
| (+) Costos indirectos de fabricación | 25.000.000 |
| **= Costo de producción del periodo** | **140.000.000** |
| (+) Inventario inicial de producto en proceso | 10.000.000 |
| (−) Inventario final de producto en proceso | (12.000.000) |
| **= Costo del producto terminado** | **138.000.000** |
| (+) Inventario inicial de producto terminado | 18.000.000 |
| (−) Inventario final de producto terminado | (20.000.000) |
| **= COSTO DE VENTAS** | **136.000.000** |

**Verificación:** el costo de ventas del estado = saldo 6120 = crédito acumulado de la 1430 por ventas. Y los tres inventarios finales (1405 + 1410 + 1430 = 47.000.000) deben coincidir con la toma física del cierre ([[Aux 18 - Juego de Inventarios]] y plan del *Proyecto - Manejo de Inventarios*).

**Variante de servicios de alimentos — **Cliente - RESTAURANTE L**:** en un asadero el "estado del costo" se arma **por receta**: la MP es el pollo y los insumos costeados **por gramo**, la MOD es el personal de cocina y los CIF son gas, empaques y arriendo proporcional. La lógica es idéntica; cambia la unidad de costeo (plato/combo en lugar de unidad fabricada) y el control de **mermas** se vuelve crítico (cruce con el 3 % del Art. 64 ET).

## Errores comunes (casos reales FYT)

1. **Nómina de planta en la 5105:** el costo del producto queda subvaluado y el gasto de administración inflado — el margen bruto sale irreal. Todo lo de producción (con prestaciones) va a la clase 7 (**Cliente - METALMECÁNICA T**).
2. **Cargar gastos de administración o ventas a los CIF** para "mejorar" la utilidad operacional — NIC 2 lo prohíbe expresamente; distorsiona el estado de costos y el inventario.
3. **Saltarse la clase 7 y debitar la 6120 directamente:** se pierde la trazabilidad MP/MOD/CIF, no se puede armar el estado de costos ni costear por producto u orden (*Proyecto - Informes de Costos y Costeo*).
4. **No valorizar los inventarios de producto en proceso al cierre:** asumir IF PP = 0 traslada costo de más al PT y al costo de ventas del año.
5. **CIF asignados sobre producción real en periodos de baja actividad** (en vez de capacidad normal): infla el costo unitario; la capacidad ociosa es gasto del periodo.
6. **Mermas sin control por gramo/unidad** en alimentos (**Cliente - RESTAURANTE L**): el costo "se come" la diferencia y nadie ve la fuga — mismo patrón del faltante camuflado de [[Aux 18 - Juego de Inventarios]].

## Checklist de calidad

- [ ] Las tres fórmulas cuadradas: MP consumida, costo de producción, costo de ventas.
- [ ] Clase 7 cerrada contra 1410; saldo de la clase 7 en cero al cierre.
- [ ] Nómina de producción (con prestaciones y aportes) en la 72, no en la 5105.
- [ ] CIF sin gastos de administración/ventas; asignación a capacidad normal.
- [ ] Inventarios finales 1405/1410/1430 soportados en toma física valorizada.
- [ ] Costo de ventas en la 6120 (manufactura); la 6135 es de comercio.
- [ ] Estado de costos entregado con el juego de estados financieros y conciliado con renta.

## Relacionado

- Anterior: [[Aux 18 - Juego de Inventarios]] · Siguiente: [[Aux 20 - Interpretacion del Token DIAN]]
- [[MOC - Escuela Auxiliar Contable]]
- [[02-AuxiliarContable-Senior]] · [[10-EspecialistaCostosInventarios-Master]] · [[09-AuxiliarInventarios-Senior]]
- *Proyecto - Informes de Costos y Costeo* · **Cliente - METALMECÁNICA T** · **Cliente - RESTAURANTE L**
