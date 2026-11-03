---
tipo: conocimiento
tags: [ritore, iva]
estado: vigente
fecha: 2026-06-07
---

# Protocolo IVA — Formulario 300 (Parte D)

Reglas destiladas de campañas reales de IVA 2026 (**EXPORTADORA DE SERVICIOS B**, **PERSONA NATURAL J / TALLER DE DISEÑO J**, **COMERCIO DE BICICLETAS A**). Verificadas en ejecución, no teoría. Aplican a toda liquidación o reporte de IVA. Skill operativa: [[Skill - Presentar IVA Bimestral F300]].

## D.1 — Insumos

La liquidación se hace con archivos Excel: el **Token DIAN** (a veces dentro de un `.zip`) y la contabilidad (**balance de prueba** + **libro auxiliar** del periodo). **El Token DIAN es la fuente de verdad**; la contabilidad debe ajustarse a él, no al revés. Si un Excel no abre, aplicar [[Manejo de Archivos Excel Corruptos]].

## D.2 — Desglose base/IVA (regla crítica)

- La columna `Total` del Token incluye base + IVA. Siempre desglosar: **`Base = Total − IVA`**.
- **NUNCA aplicar 19 % plano:** usar el IVA real reportado por factura (hay 5 %, exentos, excluidos y tarifas mixtas — frecuentes en el sector bicicletas).
- **La tarifa de IVA del 21 % no existe en Colombia:** si aparece, es error — señalar, no descontar a ciegas.

## D.3 — Clasificación

- Columna `Grupo`: **`Emitido` = ventas** (IVA generado) · **`Recibido` = compras** (IVA descontable).
- Un **DSEL emitido a un no obligado es compra soporte, NO venta**, aunque aparezca en "Emitido".
- Las **notas crédito se RESTAN** del total y del IVA (cifras netas); las notas débito se suman.

## D.4 — Casillas del F-300

- Las casillas de **compras (50-57) llevan la BASE sin IVA**, nunca el total con IVA. Error frecuente ya cometido y corregido.
- Las casillas de impuesto llevan el valor del IVA. IVA generado − IVA descontable = saldo; restar ReteIVA y saldo a favor anterior (si se arrastra).

## D.5 — Año contable sin cerrar (patrón recurrente)

Si no se cerró el año anterior contra utilidades acumuladas (36/37), las cuentas 41xx, 2408xx, 511570/731570 arrastran saldos antiguos. **Trabajar con los MOVIMIENTOS del periodo** (débitos/créditos), nunca con el saldo final acumulado. Excluir filas "SALDO INICIAL". Declararlo como hallazgo; no frenar la liquidación por ello.

## D.6 — Periodicidad: confirmar SIEMPRE por cliente

No es uniforme: **bimestral** (ene-feb, mar-abr, …) o **cuatrimestral** (ene-abr, may-ago, sep-dic). El arrastre del saldo a favor anterior depende de instrucción del cliente — no asumir.

## D.7 — Tratamientos especiales

- **Exportador (*Art 481 ET - Exportadores*):** ventas exentas, IVA generado $0, descontable 100 % imputable sin prorrateo.
- **Prorrateo *Art 490 ET - Prorrateo IVA*:** solo si hay operaciones gravadas Y excluidas.
- **Bienes excluidos/exentos:** verificar el tratamiento del producto facturado.

## D.8 — Criterios por cliente (NO generalizar)

| Cliente | NIT/CC | Periodicidad | Criterio particular |
|---------|--------|--------------|---------------------|
| **Cliente - EXPORTADORA DE SERVICIOS B** | 900000000 | Bimestral | Exportador (Art. 481). IVA de factura DIAN **< $50.000 → mayor valor de la compra** (no se descuenta), por factura completa. **Exclusivo de EXPORTADORA DE SERVICIOS B.** |
| **Cliente - COMERCIO DE BICICLETAS A** | 900000000 | **Cuatrimestral** | Sector bicicletas: bienes exentos/excluidos en ventas; compras con tarifas mixtas. |
| **Cliente - PERSONA NATURAL J (TALLER DE DISEÑO J)** | 71338055 | Bimestral | Persona natural. NO aplica regla < $50.000. Arrastre de saldo a favor según instrucción. |

Ante un criterio nuevo: preguntar si aplica solo a ese cliente o es general, y registrarlo. **Un criterio de un cliente NUNCA se generaliza sin confirmar.**

## D.9 — Entregables

- **Excel** `FORMATO 300 IVA [PERIODO] [CLIENTE] - Claude.xlsx` con 11 hojas (modelo "INVERSIONES N"): Resumen, Formato 300, IVA Generado, IVA Descontable, Cuadres, Cruce DIAN vs Contab, Detalle por NIT, Compras DIAN, Ventas DIAN, Nómina, Comparativo. Las hojas de detalle separan "Base (sin IVA)" y "Total (con IVA)".
- **Word** `INFORME EJECUTIVO IVA [PERIODO] [CLIENTE] - Claude.docx`: semáforo, liquidación, cruce, hallazgos con severidad, sustento normativo, plan de acción.
- **Reporte de gestión a fecha de corte:** documento simple dirigido al destinatario, declarando EXPRESAMENTE que es un corte parcial y no la declaración definitiva.

## D.10 — Ética

Nunca forzar ni "maquillar" cifras para que cuadren. Si una diferencia viene de un error contable (año sin cerrar, reclasificaciones), se corrige la contabilidad, no el formato. Documentar la causa raíz y escalar al Contador Titular. **No presentar sin su firma.**

## Relacionado

- [[Skill - Presentar IVA Bimestral F300]] · *11-EspecialistaIVA-Master*
- *Art 481 ET - Exportadores* · *Art 490 ET - Prorrateo IVA*
- [[Manejo de Archivos Excel Corruptos]] · *Formato 1005 y 1006 - IVA*
- **Cliente - EXPORTADORA DE SERVICIOS B** · **Cliente - COMERCIO DE BICICLETAS A** · **Cliente - PERSONA NATURAL J (TALLER DE DISEÑO J)** · **Cliente - INVERSIONES N**
- *Proyecto - IVA 2026* · *MOC - Conocimiento Tecnico*
