---
tipo: skill
tags: [ritore, skill, iva]
estado: vigente
version: 2.1
fecha: 2026-06-11
---

# Skill — `presentar-iva-bimestral-F300` (v2.1)

**Agente:** *11-EspecialistaIVA-Master* · **Versión:** 2.1 (2026-06-11) · Fuente: `_SKILLS_MEJORADAS/presentar-iva-bimestral-f300/SKILL.md`

> La v2.0 está reescrita con base en campañas reales 2026 (**EXPORTADORA DE SERVICIOS B**, **PERSONA NATURAL J / TALLER DE DISEÑO J**, **COMERCIO DE BICICLETAS A**). Reemplaza la v1 que asumía consultas SQL a tablas inexistentes: **el flujo real es archivos Excel, no SQL.** El conocimiento técnico de respaldo está en [[Protocolo IVA Formulario 300]].

## Cuándo se activa

- Cierre del bimestre o cuatrimestre del cliente, antes del vencimiento DIAN.
- "Liquida el IVA de [cliente] [periodo]".
- Reporte de gestión a fecha de corte (corte parcial, no declaración definitiva).

Es el flujo tributario de mayor frecuencia y mayor exposición sancionatoria (Art. 641/644 ET + intereses moratorios).

## Procedimiento

**Paso 0 — Confirmar parámetros del cliente (NUNCA asumir):** periodicidad bimestral o cuatrimestral (no es uniforme — verificar SIEMPRE); régimen y calidad (ordinario, exportador, autorretenedor); periodo exacto y vencimiento por NIT; si se arrastra el saldo a favor anterior (instrucción del cliente); criterios particulares del cliente.

**Paso 0bis — Cargar criterios particulares desde la nota del cliente** (**Cliente - EXPORTADORA DE SERVICIOS B**, **Cliente - COMERCIO DE BICICLETAS A**, **Cliente - PERSONA NATURAL J (TALLER DE DISEÑO J)**, etc., sección "Criterios particulares"). **PROHIBIDO liquidar con criterios de memoria o de esta skill:** la fuente de verdad es la nota del cliente, que registra valor, origen, fecha y aprobación de cada criterio (gobernanza del §3 del *00 - Estandar de Skills RITORE*).

**Paso 1 — Cargar y clasificar el Token DIAN** (Excel, a veces en .zip): `Grupo` `Emitido` = ventas (IVA generado) · `Recibido` = compras (IVA descontable). Notas crédito se RESTAN; notas débito se suman; DSEL emitido a no obligado = compra soporte, NO venta.

**Paso 2 — Desglosar base e IVA:** `Base = Total − IVA`. Usar el IVA REAL por factura (5 %, exentos, excluidos, tarifas mixtas). Verificar tarifa efectiva = IVA/Base; **la tarifa del 21 % no existe en Colombia** — si aparece, es error: señalar.

**Paso 3 — Cargar contabilidad (BP + libro auxiliar):** alerta de año sin cerrar (cuentas 41xx/2408xx/511570 con saldos arrastrados) → trabajar con MOVIMIENTOS del periodo, excluir "SALDO INICIAL", declarar hallazgo sin frenar la liquidación. Excel corrupto → [[Manejo de Archivos Excel Corruptos]].

**Paso 4 — Cruce Token vs contabilidad:** IVA generado, IVA descontable e ingresos. **Diferencia material = ≥ 1 UVT individual o ≥ 0,5 % del total del período** (mismo estándar de exógena *B7*; ref. §4 del *00 - Estandar de Skills RITORE*): toda diferencia material se investiga y documenta antes de liquidar. **El Token DIAN es la fuente de verdad.**

**Paso 5 — Liquidar el F-300:** ingresos (casillas 27-43) y compras (50-57) llevan la **BASE sin IVA**; casillas de impuesto (59-81) llevan el IVA. Generado − descontable − ReteIVA − saldo a favor anterior = resultado. Tratamientos especiales: exportador *Art 481 ET - Exportadores*; prorrateo *Art 490 ET - Prorrateo IVA* solo con gravadas Y excluidas; bienes excluidos/exentos según producto.

**Paso 6 — Entregables:** Excel `FORMATO 300 IVA [PERIODO] [CLIENTE] - Claude.xlsx` (11 hojas, modelo "INVERSIONES N") + Word `INFORME EJECUTIVO IVA [PERIODO] [CLIENTE] - Claude.docx` (semáforo, hallazgos con severidad, plan de acción). Reporte a fecha de corte: declarar EXPRESAMENTE que es parcial.

**Paso 7 — Normativa de referencia** (verificar vigencia antes de citar): Arts. 420, 447, 437/437-1/437-2, 468, 468-1/468-3, 477, 481, 485/488, 490, 600, 641, 850 ET.

**Paso 8 — Escalar a firma y presentar:** borrador + hoja de trabajo + cruce al Contador Titular; tras aprobación, presentar vía MUISCA con 2+ días de margen; archivar acuse y recibo 490; registrar contablemente.

## Criterios por cliente: gobernanza (§3 del estándar)

Esta skill **NO contiene criterios particulares de clientes** (prohibido hardcodearlos — §3 del *00 - Estandar de Skills RITORE*). Aplica el **Paso 0bis**: cargar los criterios desde la nota del cliente (**Cliente - EXPORTADORA DE SERVICIOS B**, **Cliente - COMERCIO DE BICICLETAS A**, **Cliente - PERSONA NATURAL J (TALLER DE DISEÑO J)**, etc.), sección "Criterios particulares". PROHIBIDO liquidar con criterios de memoria o de esta skill: la fuente de verdad es la nota del cliente, que registra valor, origen, fecha y aprobación de cada criterio.

## Reglas críticas

🚫 NUNCA: presentar sin firma del Contador Titular · poner el total CON IVA en las casillas de base (50-57) · aplicar 19 % plano · generalizar un criterio de un cliente · usar saldos finales con año sin cerrar · presentar con diferencia material no documentada.
✅ SIEMPRE: confirmar periodicidad · desglosar Base = Total − IVA y restar notas crédito · clasificar Emitido=ventas / Recibido=compras · presentar con 2+ días de margen · documentar el saldo a favor.

## Tests

1. Cliente estándar bimestral → desglose base/IVA, cruce con contabilidad, F-300 listo para firma en plazo.
2. Sin ventas en el periodo → generado $0, saldo a favor; confirmar que no se omitió facturar (riesgo Art. 652-1).
3. Exportador → generado $0, descontable 100 % sin prorrateo; evaluar devolución.
4. Reporte a fecha de corte → declarar expresamente que NO es la declaración definitiva.
5. Año contable sin cerrar → movimientos del periodo, hallazgo declarado, liquidación no se frena.
6. Criterio particular recordado "de memoria" pero ausente de la nota del cliente → NO se aplica; se confirma con el titular y se registra primero en la nota del cliente.

## Historial de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 2.1 | 2026-06-11 | Gobernanza de criterios por cliente (Paso 0bis: cargar desde la nota del cliente, §3 del estándar; tabla hardcodeada eliminada y criterios migrados a las notas de cliente) + umbral de materialidad en el cruce Token vs contabilidad (≥ 1 UVT individual o ≥ 0,5 % del total del período, §4 del estándar). Test 6 nuevo. |
| 2.0 | 2026-05-21 | Reescritura con base en campañas reales 2026; flujo Excel (no SQL). |

## Relacionado

- [[Protocolo IVA Formulario 300]] · *Art 481 ET - Exportadores* · *Art 490 ET - Prorrateo IVA*
- [[Manejo de Archivos Excel Corruptos]] · *Formato 1005 y 1006 - IVA*
- *11-EspecialistaIVA-Master* · *14-EspecialistaExogena-Master*
- **Cliente - EXPORTADORA DE SERVICIOS B** · **Cliente - COMERCIO DE BICICLETAS A** · **Cliente - PERSONA NATURAL J (TALLER DE DISEÑO J)** · **Cliente - INVERSIONES N**
- *Proyecto - IVA 2026* · *MOC - Skills*
