---
tipo: leccion
tags: [ritore, escuela, auxiliar, iva, impuestos]
modulo: 4
estado: vigente
fecha: 2026-06-08
---

# Aux 15 - IVA y Prorrateo

## Objetivo

Que el auxiliar registre correctamente el **IVA generado** y el **IVA descontable**, conozca los requisitos legales del descontable (Arts. 485–488, 496 ET), distinga las tarifas (19 %, 5 %, exento, excluido), aplique el **prorrateo del Art. 490 ET** cuando coexisten operaciones gravadas y excluidas, y sepa cuándo el IVA es **mayor valor del costo o gasto**. Lo que se cause en la 2408 durante el bimestre ES el F-300: no hay liquidación buena con causación mala.

## Marco conceptual y normativo

**Las dos caras de la cuenta 2408 (impuesto sobre las ventas por pagar):**
- **Crédito — IVA generado:** el que el cliente factura en sus ventas gravadas.
- **Débito — IVA descontable:** el que pagó en compras de bienes y servicios imputables a sus operaciones gravadas.
- Saldo crédito al cierre del periodo = IVA a pagar; saldo débito = saldo a favor.

**Tarifas y categorías:**

| Categoría | Tarifa | ¿Da derecho a descontable en los insumos? |
|---|---|---|
| Gravado tarifa general | 19 % | Sí |
| Gravado tarifa reducida | 5 % | Sí (descontable limitado a la tarifa de la operación — Art. 485/498 ET) |
| **Exento** (Art. 477, 481 ET) | 0 % | **Sí** — el productor/exportador descuenta el 100 % y puede pedir devolución |
| **Excluido** (Art. 424 ET) | no causa IVA | **No** — el IVA pagado es mayor valor del costo/gasto |

> 🚫 **Regla de la firma (D.2 del CLAUDE.md):** la tarifa de IVA del **21 % NO existe en Colombia**. Si aparece en un token DIAN, una factura o un software: es un **error** — se señala y se corrige, nunca se registra.

**Requisitos del IVA descontable (Arts. 485–488 y 771-2 ET):**
1. Que el IVA esté **discriminado en factura electrónica válida** (o documento soporte equivalente).
2. Que la compra sea **costo o gasto aceptable en renta** e **imputable a operaciones gravadas o exentas** (Art. 488).
3. Que se solicite **a tiempo** (Art. 496): en el periodo de causación o en los **3 periodos bimestrales siguientes**.
4. Limitación de tarifa (Art. 485): no se descuenta más IVA del que la operación de venta permite recuperar.

**Prorrateo — Art. 490 ET:** cuando los insumos comunes (arriendo, servicios públicos, honorarios) sirven **a la vez** a operaciones gravadas/exentas y excluidas, el IVA común se descuenta **en proporción** a los ingresos gravados + exentos sobre los ingresos totales. Solo aplica si coexisten ambas; ver *Art 490 ET - Prorrateo IVA*.

**Exportadores — Art. 481 ET:** las exportaciones son **exentas**; el exportador descuenta el **100 %** de su IVA sin prorrateo. Es el caso de **Cliente - EXPORTADORA DE SERVICIOS B** (criterio D.8: además, en EXPORTADORA DE SERVICIOS B el IVA de factura DIAN **< $50.000 va como mayor valor de la compra** — criterio **exclusivo** de ese cliente, nunca generalizar).

**Reglas operativas FYT (Parte D del CLAUDE.md):** desglosar siempre Base = Total − IVA (nunca 19 % plano); notas crédito se restan en el F-300 (cifras netas) pero en exógena 1005/1006 van en columna propia; casillas 50–57 del F-300 llevan la **base sin IVA**.

**Cuentas:** manejar la **2408 con auxiliares por tarifa y naturaleza** — p. ej. 240801 generado 19 %, 240802 generado 5 %, 240810 descontable 19 %, 240811 descontable 5 % — porque el F-300 y los formatos 1005/1006 de exógena piden las cifras separadas por tarifa.

## Paso a paso (con asientos)

**Caso tipo **Cliente - COMERCIO DE BICICLETAS A**** (retail de bicicletas: ventas gravadas 19 %, accesorios al 5 %... y bicicletas excluidas — tarifas mixtas, sector con trampas).

**1. Venta gravada 19 %:** accesorios por $1.000.000 + IVA $190.000:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 130505 | Clientes nacionales | 1.190.000 | |
| 413524 | Comercio — ingresos por ventas | | 1.000.000 |
| 240801 | IVA generado 19 % | | 190.000 |

**2. Compra imputable a gravadas:** repuestos $2.000.000 + IVA 19 % $380.000 (cumple Arts. 485–488):

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 1435 | Mercancías no fabricadas por la empresa | 2.000.000 | |
| 240810 | IVA descontable 19 % | 380.000 | |
| 220501 | Proveedores nacionales | | 2.380.000 |

**3. Compra destinada SOLO a operaciones excluidas:** el IVA NO es descontable → **mayor valor del costo**. Compra $1.000.000 + IVA $190.000 de insumos para la línea excluida:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 1435 | Mercancías (costo = base + IVA no descontable) | 1.190.000 | |
| 220501 | Proveedores nacionales | | 1.190.000 |

**4. Prorrateo Art. 490 — IVA común del cuatrimestre.** Ingresos del periodo: gravados $70.000.000, excluidos $30.000.000 → **factor = 70/100 = 70 %**. IVA de costos comunes (arriendo del local, energía, contador): $1.900.000, registrado inicialmente en 240815 "IVA transitorio común":

- Descontable: 1.900.000 × 70 % = **$1.330.000**
- Mayor valor del gasto: 1.900.000 × 30 % = **$570.000**

Asiento de ajuste al cierre del periodo:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 240810 | IVA descontable 19 % | 1.330.000 | |
| 512010 | Arrendamientos (IVA no descontable, proporcional) | 570.000 | |
| 240815 | IVA transitorio por prorratear | | 1.900.000 |

**5. Exportador (caso **Cliente - EXPORTADORA DE SERVICIOS B**):** vende al exterior $50.000.000 — exento, IVA generado $0; TODO su IVA descontable se toma al 100 % (sin prorrateo) y el saldo a favor es susceptible de devolución:

| Cuenta | Nombre | Débito | Crédito |
|---|---|---|---|
| 130510 | Clientes del exterior | 50.000.000 | |
| 4135xx | Ingresos por exportaciones (exentas) | | 50.000.000 |

**6. Cierre del periodo — liquidación:** IVA generado (créditos 24080x) − IVA descontable (débitos 24081x) = saldo del F-300. El pago: D 2408 / C 1110. Verificar la **periodicidad por cliente** (regla D.6): EXPORTADORA DE SERVICIOS B y TALLER DE DISEÑO J bimestral; **COMERCIO DE BICICLETAS A cuatrimestral** — nunca asumir.

## Errores comunes (casos reales FYT)

1. **Aplicar 19 % plano sobre el total del token DIAN** en vez del IVA real por factura — en el sector bicicletas (**Cliente - COMERCIO DE BICICLETAS A**) hay 5 %, exentos y excluidos; regla D.2. Y si aparece un "21 %": error, se señala.
2. **Poner el total con IVA en las casillas de base (50–57) del F-300** — error ya cometido y corregido en campañas reales (regla D.4). Las hojas de trabajo separan "Base (sin IVA)" y "Total (con IVA)".
3. **Tomar descontable IVA de compras imputables a excluidas** o no prorratear el IVA común cuando coexisten gravadas y excluidas (Art. 490). El inverso: prorratearle el IVA a un exportador puro del Art. 481, que tiene derecho al 100 % (**Cliente - EXPORTADORA DE SERVICIOS B**).
4. **Generalizar criterios de cliente:** la regla "< $50.000 a mayor valor de la compra" es EXCLUSIVA de EXPORTADORA DE SERVICIOS B (D.8). Aplicársela a TALLER DE DISEÑO J o a COMERCIO DE BICICLETAS A es un hallazgo.
5. **Trabajar con saldos acumulados cuando el año no se cerró** (regla D.5): usar los **movimientos** del periodo de las 41xx/2408, excluyendo "SALDO INICIAL".
6. **Perder el descontable por extemporáneo:** facturas viejas contabilizadas tarde, fuera de la ventana del Art. 496 (periodo + 3 bimestres).
7. **Una sola subcuenta 2408 para todo:** sin auxiliares por tarifa no se pueden diligenciar el F-300 ni los formatos 1005/1006 de exógena sin reprocesos.

## Checklist de calidad

- [ ] Toda venta clasificada: 19 %, 5 %, exenta o excluida (¿el producto realmente es excluido? verificar Art. 424).
- [ ] Todo descontable con factura electrónica válida, imputable a gravadas/exentas y dentro del plazo del Art. 496.
- [ ] IVA de compras para excluidas → mayor valor del costo (nunca a la 2408).
- [ ] Prorrateo Art. 490 calculado con los ingresos del periodo; papel de trabajo del factor archivado.
- [ ] 2408 con auxiliares por tarifa; base y total siempre separados.
- [ ] Notas crédito netas para el F-300; en columna propia para exógena 1005/1006.
- [ ] Periodicidad confirmada por cliente (bimestral/cuatrimestral) antes de liquidar.
- [ ] Tarifa 21 % = error; reportar de inmediato.

## Relacionado

- Anterior: [[Aux 14 - Calculo de Retenciones]] · Siguiente: [[Aux 16 - GMF y Cuentas Bancarias]]
- [[MOC - Escuela Auxiliar Contable]]
- [[02-AuxiliarContable-Senior]] · [[Aux 20 - Interpretacion del Token DIAN]] · [[Aux 21 - Cruce Token vs Contabilidad]]
- *Art 490 ET - Prorrateo IVA* · **Cliente - EXPORTADORA DE SERVICIOS B** · **Cliente - COMERCIO DE BICICLETAS A**
