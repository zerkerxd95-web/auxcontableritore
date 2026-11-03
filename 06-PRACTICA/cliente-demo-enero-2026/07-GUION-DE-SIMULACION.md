# 07 — Guion de simulación: tu primer cierre en una semana

**Cliente:** COMERCIALIZADORA EJEMPLO SAS · **NIT:** 900.123.456-8 *(ficticio)* · **Período:** ENERO 2026

**Qué es:** el guion día a día para practicar el bucle mensual de cierre con los archivos de esta carpeta, antes de trabajar con un cliente real. Sigue los 5 días en orden; cada día indica **qué archivo arrastrar a Claude, qué pedirle (prompt textual) y qué deberías encontrar**.

**Reglas de la práctica:**
1. Trabaja en un proyecto de Claude que ya tenga cargados `_FICHA-CLIENTE.md`, `VALORES-VIGENTES.md` y las skills del paquete.
2. **NO abras `08-CLAVE-DE-RESPUESTAS.md` hasta terminar el día 5.** Es tu examen.
3. Hay errores sembrados en los datos (como en cualquier contabilidad real que recibes de un cliente). Tu trabajo es encontrarlos, no asumir que todo está bien.
4. Anota cada hallazgo en una lista propia: cuenta, tercero, valor, qué harías. La comparas al final contra la clave.

---

## Día 1 — Recepción de insumos y validación estructural

**Arrastra:** `_FICHA-CLIENTE.md` + `01-BALANCE-DE-PRUEBA-ENE2026.md`

**Prompt sugerido:**
> "Vamos a cerrar enero 2026 de COMERCIALIZADORA EJEMPLO SAS (ficha adjunta). Este es el balance de prueba exportado del software. Antes de liquidar nada: (1) verifica que cuadre (∑débitos = ∑créditos y ecuación contable en saldos iniciales y finales), (2) revisa cuenta por cuenta si hay saldos contrarios a su naturaleza, (3) dime qué cuentas ameritan revisión con el auxiliar y por qué, teniendo en cuenta los criterios de la ficha."

**Qué debes encontrar hoy:**
- El balance cuadra aritméticamente (si no cuadrara, se devuelve al cliente — nunca se trabaja sobre un balance descuadrado).
- **Dos saldos negativos** (contrarios a naturaleza) que exigen explicación. Uno es un pasivo de impuestos; el otro es una cuenta por pagar que se volvió "por cobrar".
- Una pérdida operativa del mes que tendrás que explicar en el informe gerencial (¿es real o hay ingresos sin causar? — lo sabrás el día 3).
- Lista de cuentas a auditar mañana con el auxiliar (retenciones, IVA, cuentas de socios según la ficha).

---

## Día 2 — Depuración del auxiliar y terceros

**Arrastra:** `02-LIBRO-AUXILIAR-ENE2026.md` + `03-BALANCE-POR-TERCERO-ENE2026.md`

**Prompt sugerido:**
> "Aquí están el libro auxiliar y el balance por tercero de enero. Audítalos contra el balance de prueba y contra los criterios de la ficha del cliente: (1) ¿los totales del auxiliar coinciden con los débitos/créditos del balance de prueba?, (2) busca terceros mal identificados: genéricos tipo 'VARIOS', cédulas registradas como NIT, movimientos sin tercero, (3) verifica el criterio del IVA de compras menores a $200.000, (4) verifica que ningún movimiento de socios esté por fuera de las cuentas 28xx, (5) revisa las tarifas de retención en la fuente aplicadas en cada compra y servicio contra las tarifas legales."

**Qué debes encontrar hoy (mínimo 5 hallazgos):**
- Un tercero genérico prohibido en gastos (la ficha ya lo advertía como pendiente vivo).
- Una cédula de ciudadanía registrada con dígito de verificación como si fuera NIT (revienta la exógena).
- Un movimiento de retención en compras **sin tercero** (imposible de certificar y de reportar en exógena).
- Un IVA llevado a descontable que, según el criterio de la ficha, iba al gasto.
- Un pago al socio mayoritario contabilizado en una cuenta que no es la que ordena la ficha (y que además dejó esa cuenta con saldo contrario). **Este hallazgo se escala al gerente antes del cierre — así lo exige la ficha.**
- Una tarifa de retención en compras que no corresponde (verifica proveedor por proveedor: ¿declarante = 2,5%?).

---

## Día 3 — Cruce con facturación electrónica (token DIAN)

**Arrastra:** `05-TOKEN-DIAN-ENE2026.md`

**Prompt sugerido:**
> "Este es el reporte de facturación electrónica DIAN de enero (emitidos y recibidos). Crúzalo contra el auxiliar: (1) ¿todas las facturas de venta emitidas están causadas en la 4135? Lista factura por factura, (2) ¿todas las compras recibidas están causadas?, (3) ¿hay gastos en el auxiliar sin factura electrónica que los respalde?, (4) cuantifica el efecto de cualquier diferencia sobre ingresos, IVA generado y la autorretención del 0,55%."

**Qué debes encontrar hoy:**
- **Una factura de venta emitida que NO está causada** en el auxiliar. Efecto triple: ingresos subestimados, IVA generado subestimado (ojo: el IVA es bimestral, se declara con febrero, pero debe quedar causado ya) y autorretención del 0,55% subestimada.
- El gasto del tercero genérico del día 2 no tiene factura electrónica que lo respalde (doble bandera).
- Los honorarios de persona natural no aparecen en el token — eso es **normal** (documento soporte); distinguir diferencias reales de falsas alarmas también es parte del método.

---

## Día 4 — Conciliación bancaria y nómina

**Arrastra:** `04-EXTRACTO-BANCARIO-ENE2026.md` (y ten a la mano el auxiliar del día 2)

**Prompt sugerido (parte A):**
> "Concilia la cuenta 111005 contra este extracto de Bancolombia: parte del saldo en libros y del saldo del extracto, identifica cada partida conciliatoria (libro vs banco), clasifícala (falta causar en libros / pendiente de corresponder en banco) y dame el saldo conciliado. Propón los asientos de ajuste que haya que registrar."

**Qué debes encontrar (parte A): exactamente 4 partidas conciliatorias.** Dos son cargos del banco no causados en libros (se ajustan con asiento), una es un cheque girado y entregado que el beneficiario no ha cobrado (no se ajusta, se controla), y una es una consignación que el banco abonó pero no sabes de quién es (se investiga con cartera antes de tocarla). El saldo conciliado debe darte **idéntico por las dos vías**; si no, hay algo sin identificar.

**Arrastra después:** `06-PRENOMINA-ENE2026.md`

**Prompt sugerido (parte B):**
> "Revisa esta prenómina de enero contra los valores vigentes 2026 del candado: SMMLV, auxilio de transporte y su tope de 2 SMMLV, salud y pensión 4%, FSP desde 4 SMMLV. Verifica que los totales crucen contra las cuentas 5105, 237005 y 250505 del balance, y contra la dispersión de nómina del extracto."

**Qué debes encontrar (parte B):** la prenómina está bien liquidada y cruza contra contabilidad y contra el banco — comprobarlo también es trabajo. Verifica en especial quién recibe auxilio de transporte y quién cotiza FSP.

---

## Día 5 — Liquidación, vigilancias y entrega

**Sin archivo nuevo.** Trabaja con todo lo acumulado.

**Prompt sugerido:**
> "Con todos los hallazgos de la semana: (1) liquida el F-350 de enero 2026 por concepto (honorarios, servicios, arrendamientos, compras, autorretención 0,55%) en dos columnas: 'según libros' y 'corregido tras hallazgos', explicando cada diferencia, (2) dame el checklist de obligaciones del mes según la ficha, incluida la vigilancia reforzada de ReteICA (¿este bimestre se presenta algo? ¿qué queda programado?), (3) redacta la lista de ajustes contables propuestos para aprobación del contador titular (control de cuatro ojos), (4) borrador del correo al gerente con los temas que la ficha obliga a revisar con él."

**Qué debes producir hoy:**
- F-350 de enero liquidado por concepto, con la diferencia entre lo registrado y lo correcto, y su explicación (dos de los errores de la semana lo afectan).
- Recordatorio ReteICA: el bimestre ene-feb se declara en marzo, **se presenta aunque dé $0** (antecedente de sanción en la ficha). Lo retenido en enero queda acumulado en la 2368.
- Paquete de ajustes propuestos (venta sin causar, reclasificación del socio, IVA al gasto, tarifa de retención, GMF y cuota de manejo, saldo de la 240805) — **ninguno se registra sin el visto bueno del titular: cuatro ojos siempre.**
- Correo al gerente: préstamo del socio (formalización pendiente según ficha) y el abono que apareció esta semana; la consignación bancaria sin identificar; la pérdida del mes.

---

## Cierre de la práctica

1. Abre `08-CLAVE-DE-RESPUESTAS.md` y compara tu lista de hallazgos.
2. **Criterio de aprobación: encontraste ≥6 de los 8 errores sembrados = listo para tu primer cliente real.** Si encontraste menos, repite los días 2 y 3 — ahí vive lo que se te escapó.
3. Copia `_FICHA-CLIENTE.md` como plantilla, llénala con tu cliente real más simple y corre el mismo bucle. Esa es la promesa: **primer cierre real en una semana.**
