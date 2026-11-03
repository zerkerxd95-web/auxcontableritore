---
tipo: leccion
tags: [ritore, escuela, auxiliar, partida-doble]
modulo: 1
estado: vigente
fecha: 2026-06-08
---
# Aux 02 - Partida Doble y Asientos Contables

## Objetivo
El auxiliar entenderá la ecuación contable, dominará la mecánica débito/crédito y será capaz de construir y leer asientos completos para las operaciones más frecuentes de la firma, cumpliendo la regla de oro: **todo asiento cuadra y todo movimiento tiene tercero y soporte**.

## Marco conceptual y normativo
- **Ecuación contable:** `Activo = Pasivo + Patrimonio`. Toda transacción la mantiene en equilibrio; por eso cada registro afecta al menos dos cuentas (partida doble, Art. 50 C.Co.: contabilidad por el sistema de partida doble en libros registrados).
- **Débito y crédito NO significan "bueno" o "malo":** son los dos lados del registro. Débito aumenta clases 1-5-6-7 y disminuye 2-3-4; crédito al revés (ver [[Aux 01 - Plan de Cuentas PUC]]).
- **Comprobante de contabilidad** (Art. 53 C.Co., Decreto 2649/1993 Art. 124): documento que resume las operaciones, numerado consecutivamente, fechado, con cuentas afectadas y soportes adjuntos. Es lo que el software genera con cada asiento (comprobante de venta, egreso, recibo de caja, nota de contabilidad).
- **NIIF PYMES Sección 2:** se reconoce un activo/pasivo/ingreso/gasto cuando se cumple la definición y es medible con fiabilidad — la causación (devengo) manda, no el flujo de caja.

## Paso a paso

### Mecánica de todo asiento
1. Identifica la operación y su **soporte** (factura, extracto, planilla).
2. Pregunta: ¿qué recibo / qué entrego? ¿qué cuentas se afectan y de qué clase son?
3. Aplica naturaleza: lo que entra/aumenta en activo o gasto → débito; lo que se debe o se gana → crédito.
4. Asigna **tercero** a cada renglón (sin excepción) y centro de costos si el cliente los usa.
5. Verifica: **suma débitos = suma créditos**. Si no cuadra, NO se asienta.

### Asientos modelo (valores 2026)

**1. Venta de servicios a crédito** — $10.000.000 + IVA 19%; el cliente (agente retenedor) nos retiene 4% por servicios:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 130505 | Clientes nacionales | 11.500.000 | |
| 135515 | Anticipo retención en la fuente | 400.000 | |
| 413550 | Ingresos por servicios | | 10.000.000 |
| 240801 | IVA generado | | 1.900.000 |

**2. Compra de mercancía a crédito** — $5.000.000 + IVA 19%; retenemos compras 2,5%:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 143505 | Mercancías no fabricadas por la empresa | 5.000.000 | |
| 240802 | IVA descontable | 950.000 | |
| 236540 | Retención en la fuente — compras | | 125.000 |
| 220505 | Proveedores nacionales | | 5.825.000 |

**3. Pago al proveedor por banco** (incluye GMF 4×1000 que cobra el banco):

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 220505 | Proveedores nacionales | 5.825.000 | |
| 530525 | Gravamen a los movimientos financieros | 23.300 | |
| 111005 | Bancos — Bancolombia | | 5.848.300 |

**4. Cobro de la factura de venta** (recaudo total):

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 111005 | Bancos — Bancolombia | 11.500.000 | |
| 130505 | Clientes nacionales | | 11.500.000 |

**5. Nómina simplificada** — 1 empleado con SMMLV 2026 ($1.750.905) + auxilio de transporte ($249.095); deducciones del empleado salud 4% y pensión 4% sobre salario:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 510506 | Sueldos | 1.750.905 | |
| 510527 | Auxilio de transporte | 249.095 | |
| 2370xx | Retenciones y aportes de nómina (salud+pensión empleado) | | 140.072 |
| 250505 | Salarios por pagar | | 1.859.928 |

*(Aportes patronales, provisiones de prestaciones y exoneración Art. 114-1 ET se desarrollan en [[Aux 11 - Causacion de Nomina]].)*

**6. Depreciación mensual** — computador de $4.800.000, vida útil 5 años (política NIIF), línea recta → $80.000/mes:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 516010 | Depreciación equipo de cómputo | 80.000 | |
| 159220 | Depreciación acumulada — equipo de cómputo | | 80.000 |

**7. Ajuste por reclasificación** (corrección detectada: un arrendamiento se asentó como servicio). NUNCA se modifica el asiento original — se reversa y se registra bien (skill `corregir-asientos-detectados-erroneos`):

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 512010 | Arrendamientos — construcciones y edificaciones | 1.500.000 | |
| 513505 | Servicios — aseo y vigilancia | | 1.500.000 |

**8. Anticipo recibido de cliente** (sin factura aún — patrón **Cliente - SALÓN DE BELLEZA I**):

| Cuenta | Nombre | Débito | Crédito |
|---|---|---:|---:|
| 111005 | Bancos | 800.000 | |
| 280505 | Anticipos y avances recibidos de clientes | | 800.000 |

## Errores comunes
- **Asientos sin tercero:** el movimiento queda huérfano y en exógena termina en un genérico que daña el reporte ([[Aux 03 - Terceros y RUT]], caso **Cliente - EMPRESA H**).
- **Asentar sin soporte** "mientras llega la factura": regla de oro del agente — NUNCA contabilizar sin soporte documental verificable.
- **Confundir causación con pago:** la factura se causa en su fecha (devengo); el pago es otro asiento. Saltarse la causación rompe el cruce token DIAN vs contabilidad.
- **Cuadrar a la fuerza:** si débitos ≠ créditos, la diferencia NUNCA se manda a una cuenta puente "para que cierre". Se busca la causa (regla C.8: jamás maquillar).
- **Modificar asientos de periodos cerrados o declarados:** se reversa en periodo de ajuste y se coordina con EspecialistaRenta si el periodo ya se declaró.

## Checklist de calidad
1. ¿Suma de débitos = suma de créditos?
2. ¿Cada renglón tiene tercero identificado con NIT?
3. ¿El asiento referencia su documento soporte (número de factura, extracto, planilla)?
4. ¿La fecha del asiento es la de causación, dentro del periodo correcto?
5. ¿Las cuentas usadas respetan su naturaleza y jerarquía PUC?
6. ¿Centro de costos asignado si el cliente los maneja?
7. ¿El IVA y las retenciones quedaron en sus cuentas (2408/2365/1355), no embebidos en el gasto o ingreso?
8. ¿Quedó documentado el criterio si la operación no era estándar?

## Relacionado
- Anterior: [[Aux 01 - Plan de Cuentas PUC]] · Siguiente: [[Aux 03 - Terceros y RUT]]
- [[MOC - Escuela Auxiliar Contable]] · [[02-AuxiliarContable-Senior]]
- [[Aux 05 - Causacion de Facturas de Venta]] · [[Aux 06 - Causacion de Facturas de Compra y Gastos]] · [[Aux 11 - Causacion de Nomina]]
