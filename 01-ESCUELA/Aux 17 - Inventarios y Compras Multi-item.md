---
tipo: leccion
tags: [ritore, escuela, auxiliar, inventarios]
modulo: 5
estado: vigente
fecha: 2026-06-08
---

# Aux 17 - Inventarios y Compras Multi-ítem

## Objetivo

Que el auxiliar cause una **factura de compra con múltiples productos**, distribuyendo fletes y descuentos al **costo unitario** de cada referencia; lleve el **kárdex por promedio ponderado** (método estándar FYT); y registre la venta en **sistema permanente** con sus **DOS asientos** (ingreso + costo). Un kárdex limpio — referencias y unidades de medida consistentes — es la base de todo el *Proyecto - Manejo de Inventarios*.

## Marco conceptual y normativo

- **Costo de adquisición (NIC 2 / Sección 13 NIIF PYMES):** precio de compra + aranceles + **fletes y transporte** + otros costos para dejar el inventario en condición y ubicación actuales, **menos** descuentos comerciales y rebajas. El IVA descontable NO es costo (va a la 2408); el IVA no descontable SÍ ([[Aux 15 - IVA y Prorrateo]]).
- **Método de valuación:** **promedio ponderado** móvil — tras cada entrada se recalcula: costo promedio = saldo en pesos / saldo en unidades. Es el método de la plantilla 09 Kárdex de FYT; PEPS es alternativa para perecederos; **UEPS no está permitido** (NIC 2).
- **Sistema permanente:** el inventario (1435 y demás 14xx) se actualiza con cada movimiento y **cada venta dispara dos asientos**: el del ingreso (4135) y el del costo (6135 contra 1435) al costo promedio del kárdex. Es la buena práctica FYT para todo cliente con inventario relevante (vs. el periódico — ver [[Aux 18 - Juego de Inventarios]]).
- **Cuentas:** 1435 mercancías no fabricadas por la empresa (comercio); 1405 materias primas, 1410 productos en proceso, 1430 productos terminados (manufactura — ver [[Aux 19 - Estado del Costo]]).
- **Higiene de datos (la base del proyecto):** una sola referencia por producto (no "CASCO GW", "casco g.w." y "CASCO-GW" a la vez), unidad de medida única por referencia, y descripción limpia. Sin esto, el kárdex multiplica referencias fantasma y el cuadre físico se vuelve imposible.

## Paso a paso (con asientos)

**Caso tipo **Cliente - COMERCIO DE BICICLETAS A**.** Factura del proveedor (15-jun-2026), con flete a cargo nuestro facturado por un transportador aparte:

| Ítem | Cant. | Vr. unitario | Subtotal |
|---|---|---|---|
| Cascos ref. CAS-001 | 10 | 60.000 | 600.000 |
| Llantas ref. LLA-026 | 5 | 40.000 | 200.000 |
| Guayas ref. GUA-007 | 20 | 10.000 | 200.000 |
| **Subtotal mercancía** | | | **1.000.000** |
| Descuento comercial pie de factura 5 % | | | (50.000) |
| IVA 19 % sobre 950.000 | | | 180.500 |
| **Total factura** | | | **1.130.500** |
| Flete (factura del transportador, excluido de IVA) | | | 100.000 |

**1. Distribuir descuento y flete al costo unitario** (en proporción al valor de cada ítem — también puede ser por peso/volumen si es más representativo):

| Ítem | Subtotal | − Descuento (5 %) | + Flete (10 % del valor) | Costo total | Costo unitario |
|---|---|---|---|---|---|
| Cascos | 600.000 | (30.000) | 60.000 | 630.000 | **63.000** |
| Llantas | 200.000 | (10.000) | 20.000 | 210.000 | **42.000** |
| Guayas | 200.000 | (10.000) | 20.000 | 210.000 | **10.500** |
| **Total** | 1.000.000 | (50.000) | 100.000 | **1.050.000** | |

**2. Asiento de la compra** (retención por compras: base $950.000 < 27 UVT $1.414.098 → no aplica; flete $100.000 < 4 UVT → tampoco; ver [[Aux 14 - Calculo de Retenciones]]):

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 143501 | Mercancías — cascos | 630.000 | |
| 143502 | Mercancías — llantas | 210.000 | |
| 143503 | Mercancías — guayas | 210.000 | |
| 240810 | IVA descontable 19 % | 180.500 | |
| 220501 | Proveedores nacionales | | 1.130.500 |
| 233550 | Costos y gastos por pagar — transportador | | 100.000 |
| **Sumas** | | **1.230.500** | **1.230.500** |

**3. Kárdex promedio ponderado — ref. CAS-001** (saldo inicial: 8 u a $60.000):

| Fecha | Detalle | Entrada (u × $) | Salida (u × $) | Saldo u | Saldo $ | Costo promedio |
|---|---|---|---|---|---|---|
| 01-jun | Saldo inicial | | | 8 | 480.000 | 60.000 |
| 15-jun | Compra FV-1234 | 10 × 63.000 = 630.000 | | 18 | 1.110.000 | **61.667** |
| 20-jun | Venta FV-501 | | 12 × 61.667 = 740.000 | 6 | 370.000 | 61.667 |
| 28-jun | Compra FV-1301 | 10 × 65.000 = 650.000 | | 16 | 1.020.000 | **63.750** |

> El promedio **solo cambia con las entradas**; las salidas van al promedio vigente. Tras cada movimiento: saldo $ / saldo u = promedio.

**4. La venta dispara DOS asientos.** El 20-jun se venden 12 cascos a $110.000 + IVA c/u:

*Asiento 1 — el ingreso:*

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 130505 | Clientes nacionales | 1.570.800 | |
| 413524 | Comercio — ingresos por ventas | | 1.320.000 |
| 240801 | IVA generado 19 % | | 250.800 |

*Asiento 2 — el costo (al promedio del kárdex):*

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 613524 | Costo de ventas — comercio | 740.000 | |
| 143501 | Mercancías — cascos | | 740.000 |

Margen bruto de la operación: 1.320.000 − 740.000 = $580.000 (43,9 %) — visible **en tiempo real** gracias al permanente.

**5. Cuadre mensual:** saldo del kárdex (todas las referencias) = saldo contable 14xx; suma de salidas del mes = movimiento 6135. Conteos cíclicos ABC y rutina completa en *Proyecto - Manejo de Inventarios*.

## Errores comunes (casos reales FYT)

1. **Mandar el flete al gasto (5235) en vez del costo del inventario** — subvalúa el inventario y adelanta el gasto. NIC 2 lo exige en el costo de adquisición.
2. **Registrar la compra con un solo renglón "mercancía"** sin distribuir a referencias: el kárdex queda sin costo unitario y el margen por producto del *Proyecto - Informes de Costos y Costeo* no se puede calcular.
3. **Referencias y unidades sucias** — el problema de fondo del inventario **no confiable** de **Cliente - COMERCIO DE BICICLETAS A** (alerta del acta de inicio): la misma llanta con 3 códigos en Siigo = tres kárdex fantasma.
4. **Olvidar el segundo asiento de la venta** (el del costo): la 4135 crece, la 6135 no, el margen bruto del mes sale irreal y el inventario contable se infla — primo hermano del caso **Cliente - AGROPECUARIA D**.
5. **Recalcular el promedio con las salidas** o usar el último costo de compra en vez del promedio — descuadra kárdex vs contabilidad.
6. **Tomar el descuento comercial como ingreso** (4210) en vez de menor costo: el descuento pie de factura NO es ingreso financiero.

## Checklist de calidad

- [ ] Costo unitario = (subtotal − descuentos + fletes y otros costos atribuibles) / unidades, por ítem.
- [ ] IVA descontable a la 2408; IVA no descontable al costo.
- [ ] Kárdex actualizado el mismo día del movimiento; promedio recalculado solo en entradas.
- [ ] Cada venta con sus DOS asientos (ingreso + costo al promedio).
- [ ] Cuadre mensual kárdex = 14xx contable = informe del software.
- [ ] Referencias únicas y unidad de medida única por referencia.
- [ ] Retenciones de la compra evaluadas (bases mínimas UVT) según [[Aux 14 - Calculo de Retenciones]].

## Relacionado

- Anterior: [[Aux 16 - GMF y Cuentas Bancarias]] · Siguiente: [[Aux 18 - Juego de Inventarios]]
- [[MOC - Escuela Auxiliar Contable]]
- [[02-AuxiliarContable-Senior]] · [[09-AuxiliarInventarios-Senior]] · [[10-EspecialistaCostosInventarios-Master]]
- *Proyecto - Manejo de Inventarios* · **Cliente - COMERCIO DE BICICLETAS A**
