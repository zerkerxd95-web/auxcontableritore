---
tipo: leccion
tags: [ritore, escuela, auxiliar, inventarios]
modulo: 5
estado: vigente
fecha: 2026-06-08
---

# Aux 18 - Juego de Inventarios

## Objetivo

Que el auxiliar domine el **sistema periódico** (juego de inventarios): la fórmula **inventario inicial + compras − inventario final = costo de ventas**, sus asientos de cierre (6205 → 6135), cuándo es admisible fiscalmente (Arts. 62–64 ET), el **límite del 3 %** para faltantes, y — sobre todo — por qué un **inventario final sobrestimado infla la utilidad** sin que nadie lo note hasta que llega la DIAN. El caso de los **$1.923M** de **Cliente - AGROPECUARIA D** es la lección viva de este capítulo.

## Marco conceptual y normativo

**La fórmula del juego de inventarios:**

```
Inventario inicial (1435 al 01-ene)
+ Compras del año (6205)
− Inventario final (conteo físico al 31-dic, valorizado)
= COSTO DE VENTAS (6135)
```

**Marco fiscal (Arts. 62–64 ET — detalle en *Proyecto - Manejo de Inventarios*):**
- **Art. 62 ET:** el costo de lo enajenado se establece por (a) **juego de inventarios** (periódico), (b) **inventarios permanentes o continuos**, o (c) otro sistema técnico autorizado por la DIAN. Desde la Ley 1819/2016 (AG 2017+) **ya no hay obligación fiscal** de llevar permanente para quienes firman con contador o revisor fiscal: es elección técnica.
- En el periódico el conteo físico de fin de año **es obligatorio**: sin inventario final no hay costo. En el permanente, el conteo anual también es buena práctica obligatoria FYT: el kárdex se ajusta al físico, no al revés.
- **Art. 64 ET:** disminuciones por faltantes de mercancías de **fácil destrucción o pérdida**: deducibles hasta el **3 % de (inventario inicial + compras)**. Por encima: solo con soporte fuerte (actas de baja, destrucción documentada) o no deducible.

**Cuentas del sistema periódico:** las compras NO van a la 1435 durante el año: van a la **6205** (compras de mercancías). La 1435 queda congelada con el inventario inicial hasta el cierre. Las devoluciones en compras van a la **6225** (crédito).

**Comparación de sistemas (decisión por cliente):**

| Criterio | Permanente ([[Aux 17 - Inventarios y Compras Multi-item]]) | Periódico (esta lección) |
|---|---|---|
| Costo de ventas | En cada venta, al promedio del kárdex | Solo al cierre, por fórmula |
| Detección de faltantes | Inmediata (kárdex vs físico) | **Imposible**: el faltante queda escondido dentro del costo |
| Carga operativa | Alta | Baja |
| Recomendado para | Retail, manufactura, agro con insumos | Negocios muy pequeños sin software |

## Paso a paso (con asientos)

**Caso:** comercializadora pequeña, año 2026. Inventario inicial $20.000.000; compras del año $80.000.000; conteo físico al 31-dic valorizado en $25.000.000.

**1. Durante el año — las compras van a la 6205:**

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 620501 | Compras de mercancías | 80.000.000 | |
| 240810 | IVA descontable 19 % | 15.200.000 | |
| 220501 | Proveedores nacionales | | 95.200.000 |

(Las ventas solo registran el asiento del ingreso — no hay asiento de costo por venta.)

**2. Cierre 31-dic — paso A: trasladar inventario inicial y compras al costo:**

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 613524 | Costo de ventas — comercio | 100.000.000 | |
| 143501 | Mercancías (inventario inicial) | | 20.000.000 |
| 620501 | Compras de mercancías | | 80.000.000 |

**3. Cierre — paso B: registrar el inventario final (físico valorizado):**

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 143501 | Mercancías (inventario final) | 25.000.000 | |
| 613524 | Costo de ventas — comercio | | 25.000.000 |

**Resultado:** la 6135 queda en 20 + 80 − 25 = **$75.000.000** (el costo del año) y la 1435 con el físico real de $25.000.000.

**4. Evaluación fiscal de faltantes:** límite Art. 64 = 3 % × (20M + 80M) = **$3.000.000**. Si el conteo evidenció bajas/faltantes de fácil destrucción por $2M → deducibles; si fueran $5M → $3M deducibles y $2M solo con acta de destrucción/baja soportada (o no deducible).

**5. Por qué el permanente es superior — mismo caso con un robo de $2.000.000:**

| | Permanente | Periódico |
|---|---|---|
| Costo de ventas "real" según kárdex | 73.000.000 | no se conoce |
| Faltante visible | **$2.000.000** (kárdex 27M vs físico 25M) → se investiga, se registra como pérdida (5310/6135 según el caso) y se evalúa el 3 % | **$0** — el robo queda camuflado dentro del costo de 75M |
| Decisión gerencial | Posible (seguridad, seguros, control) | Imposible |

## Errores comunes (casos reales FYT)

1. **Inventario final sobrestimado — el caso insignia:** **Cliente - AGROPECUARIA D** llegó con inventarios contables **$1.923M por encima del físico**. Efecto en cadena: costo de ventas subestimado → utilidad inflada → más renta → patrimonio inflado → exógena (F-1012) y estados financieros distorsionados. La corrección va a la **contabilidad** (conteo, acta de ajuste, escalamiento al Contador Titular), nunca a "cuadrar el papel de trabajo" — regla de oro C.8.
2. **Saltarse el conteo físico** y "estimar" el inventario final: en el periódico eso es inventar el costo. Sin físico no hay juego de inventarios (Art. 62 ET).
3. **Compras registradas en la 1435 durante el año en sistema periódico** (o mezclar sistemas): al cierre, el paso A descuadra y el costo sale doble o incompleto.
4. **No registrar devoluciones en compras (6225):** inflan las compras y el costo.
5. **Castigar faltantes por encima del 3 % sin soporte** — la DIAN rechaza la deducción; se necesita acta de baja/destrucción con evidencia (fotos, testigos, certificación).
6. **Valorizar el físico al precio de venta** en lugar del costo (promedio/último costo razonable): infla el inventario final y reduce el costo artificialmente. Y recordar NIC 2: si el valor neto realizable < costo, se reconoce deterioro.

## Checklist de calidad

- [ ] Sistema definido y documentado por cliente (permanente vs periódico) — no se mezclan.
- [ ] Compras del año completas en la 6205 (netas de devoluciones 6225).
- [ ] Conteo físico al cierre con acta firmada (plan de toma física del *Proyecto - Manejo de Inventarios*).
- [ ] Inventario final valorizado al costo (y prueba VNR aplicada).
- [ ] Asientos de cierre: II + compras → 6135; inventario final → 1435.
- [ ] Faltantes evaluados contra el 3 % del Art. 64 ET; excesos soportados o marcados no deducibles.
- [ ] Saldo final 14xx conciliado con renta (costo) y exógena (F-1012 patrimonio).

## Relacionado

- Anterior: [[Aux 17 - Inventarios y Compras Multi-item]] · Siguiente: [[Aux 19 - Estado del Costo]]
- [[MOC - Escuela Auxiliar Contable]]
- [[02-AuxiliarContable-Senior]] · [[09-AuxiliarInventarios-Senior]] · [[10-EspecialistaCostosInventarios-Master]]
- *Proyecto - Manejo de Inventarios* · **Cliente - AGROPECUARIA D**
