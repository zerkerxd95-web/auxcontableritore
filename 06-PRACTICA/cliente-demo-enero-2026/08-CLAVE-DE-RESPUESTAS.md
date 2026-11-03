# 08 — Clave de respuestas

> # ⚠️ No abras este archivo hasta terminar el guion
> Si estás aquí antes de completar el día 5 de `07-GUION-DE-SIMULACION.md`, cierra esto y vuelve a la práctica. La clave solo sirve si primero intentaste encontrar todo por tu cuenta.

**Cliente:** COMERCIALIZADORA EJEMPLO SAS · **NIT:** 900.123.456-8 *(ficticio)* · **Período:** ENERO 2026

**Qué es:** verificación final de la práctica — los 8 errores sembrados, las 4 partidas conciliatorias, el F-350 esperado y el criterio de aprobación.

---

## A. Los 8 errores sembrados

| # | Error | Ubicación exacta | Corrección esperada |
|---|---|---|---|
| a | Tercero genérico **"VARIOS" (NIT 222222222)** en gastos | Auxiliar, cuenta 519590, CE-015 del 28-ene, $470.000. Además no tiene factura electrónica en el token | Exigir identificación real del tercero y soporte; los genéricos revientan la exógena (formato 1001) y no son deducibles sin soporte idóneo |
| b | **Cédula registrada con DV como si fuera NIT**: "71.456.789-2" JULIÁN ESTEBAN MORA CADAVID | Auxiliar 511025/236515/236801, CE-016 del 28-ene; balance por tercero 236515 | Es una C.C. (tipo documento 13): se reporta **sin** dígito de verificación; corregir el tipo de documento en el maestro de terceros |
| c | **Pasivo 2408 con saldo contrario a su naturaleza** | Balance de prueba, cuenta **240805 IVA por pagar — declaraciones: saldo final DÉBITO $1.240.000** (saldo inicial $3.610.000 CR vs pago de $4.850.000 el 14-ene, CE-003) | El saldo inicial venía mal del contador anterior: auditar la declaración de IVA nov-dic realmente presentada y ajustar contra la cuenta que corresponda. OJO: la 240801 descontable en débito NO es el error — esa naturaleza es normal a mitad de bimestre |
| d | **Retención de compras al 3,5% donde correspondía 2,5%** (proveedor declarante) | Auxiliar 236540, FC-2204 del 16-ene, INSUMOS LA CASCADA SAS: retuvo $224.000; lo correcto era $160.000 (2,5% de $6.400.000). Exceso: **$64.000** | Reintegrar/ajustar con el proveedor antes de presentar el F-350; verificar la calidad de declarante en el RUT |
| e | **IVA de compra < $200.000 llevado a descontable** (viola criterio de la ficha del 2026-01-15) | Auxiliar 240801, CE-009 del 20-ene, PAPELERÍA EL PUNTO: compra $180.000 con IVA $34.200 en la 240801 | Reclasificar $34.200 de 240801 a 519530 (mayor valor del gasto) |
| f | **Movimiento en 236540 sin tercero** | Auxiliar 236540, FC-2205 del 21-ene, $205.000 (la compra es de QUÍMICOS DEL NORTE pero la retención quedó sin tercero); visible también en el balance por tercero como "(SIN TERCERO)" | Asignar el tercero (900.000.000-1); sin tercero no hay certificado de retención ni exógena posible |
| g | **Pago al socio mayoritario en 233595 en vez de 28xx** | Auxiliar 233595, CE-013 del 26-ene, $5.000.000 a JORGE IVÁN EJEMPLO PÉREZ; deja la 233595 con saldo DÉBITO $5.000.000 (contrario) mientras la 289505 sigue en $15.000.000 | Reclasificar a 289505 (queda en $10.000.000 CR). La ficha obliga a revisarlo con el gerente antes del cierre + recordar la formalización del préstamo (pendiente vivo) |
| h | **Factura de venta del token NO causada en el auxiliar** | Token DIAN: **FEV-1088 del 21-ene, HOTELES ANTIOQUIA SA, $2.300.000 + IVA $437.000 = $2.737.000** — no existe en la 4135 ni en la 130505 | Causar: D 130505 $2.737.000 / C 413550 $2.300.000 / C 240802 $437.000. Afecta ingresos, IVA (bimestre ene-feb) y autorretención 0,55% |

**Criterio de aprobación: encontraste ≥6 de 8 errores = listo para cliente real.** Menos de 6: repite los días 2 y 3 del guion.

---

## B. Las 4 partidas conciliatorias (banco)

Saldo libro 111005 al 31-ene: **$11.331.514** · Saldo extracto al 31-ene: **$21.767.020** · Diferencia: $10.435.506, explicada exactamente así:

| # | Partida | Valor | Tratamiento |
|---|---|---:|---|
| 1 | GMF 4x1000 del mes (extracto 31-ene) no causado en libros | $334.994 | Causar: D 530595 (D 519595/511595 según política) / C 111005 |
| 2 | Cuota de manejo (extracto 31-ene) no causada en libros | $34.500 | Causar: D 530595 / C 111005 |
| 3 | Cheque N.º 4571 girado a PLÁSTICOS ANTIOQUIA (CE-019, 30-ene, pago FEC-2202) **no cobrado** | $8.621.000 | No se ajusta; se controla en la conciliación hasta que lo cobren |
| 4 | Consignación sin identificar (extracto 23-ene, corresponsal bancario ref. 78412) | $2.184.000 | Investigar con cartera/gerente antes de aplicarla; mientras tanto es partida conciliatoria (o se lleva a pasivo 2815 si se causa) |

**Saldo conciliado: $13.146.020**
- Vía libros: $11.331.514 − GMF $334.994 − cuota $34.500 + consignación $2.184.000 = **$13.146.020** ✓
- Vía extracto: $21.767.020 − cheque no cobrado $8.621.000 = **$13.146.020** ✓

---

## C. F-350 de enero 2026 esperado (retenciones por concepto)

| Concepto | Según libros | Correcto (tras hallazgos) | Diferencia | Explicación |
|---|---:|---:|---:|---|
| Honorarios 10% (Mora Cadavid) | $120.000 | $120.000 | $0 | — |
| Servicios (4% MG $34.000 + 1% transporte $16.500) | $50.500 | $50.500 | $0 | — |
| Arrendamientos 3,5% (Inmobiliaria Horizonte) | $147.000 | $147.000 | $0 | — |
| Compras 2,5% | $1.319.000 | $1.255.000 | −$64.000 | Error (d): La Cascada al 3,5% |
| Autorretención especial renta 0,55% | $375.100 | $387.750 | +$12.650 | Error (h): base $68.200.000 → $70.500.000 con FEV-1088 |
| **TOTAL F-350 ENERO** | **$2.011.600** | **$1.960.250** | **−$51.350** | |

Notas: el IVA es **bimestral** (ene-feb se declara en marzo, ya con el ajuste de FEV-1088). ReteICA retenida en enero ($28.750 en la 2368) se acumula para la declaración bimestral de Medellín — **se presenta aunque dé $0** (vigilancia reforzada de la ficha por sanción previa). El error (e) no afecta el F-350 (solo IVA/gasto).

---

## D. Otros valores de control

| Concepto | Valor |
|---|---:|
| Ventas causadas en libros (4135) | $68.200.000 |
| Ventas reales del mes (token, con FEV-1088) | $70.500.000 |
| IVA generado corregido del mes (para el bimestre) | $13.395.000 |
| IVA descontable en libros | $10.592.500 (correcto: $10.558.300 tras error e) |
| Resultado de enero según libros | −$12.244.002 (pérdida; con FEV-1088 causada: −$9.944.002) |
| Prenómina | Devengado $23.446.380 · deducciones $1.827.144 · neto $21.619.236 — **sin errores sembrados: debía cruzar limpia** |

---

## E. Cierre

Si llegaste aquí con ≥6 errores encontrados, las 4 partidas conciliatorias identificadas y el F-350 liquidado en dos columnas: **la práctica está aprobada**. Copia la ficha como plantilla, móntala con tu cliente real más simple y corre el mismo bucle. Recuerda las dos reglas que no se negocian: control de cuatro ojos antes de registrar ajustes y prevalidación DIAN antes de presentar.
