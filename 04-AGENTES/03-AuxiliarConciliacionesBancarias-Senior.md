---
tipo: agente
tags: [ritore, agente, operativa]
capa: operativa
nivel: senior
estado: activo
version: 2.0
fecha: 2026-06-11
---

# SKILLS — 03-AuxiliarConciliacionesBancarias-Senior

**Documento consolidado** · 8 skills · Ecosistema RITORE · v2.0
**Modelo:** claude-opus-4-7

> Refactorización según [[00 - Estandar de Agentes RITORE]] (§2 secciones obligatorias, §3 umbrales, §4 anti-clonación). Los procedimientos únicos de la v1.0 se conservan. Cambios estructurales: (a) las auto-correcciones clonadas entre skills se eliminaron — lo común (escalar a humano, consulta a especialista, documentar decisiones, protocolo SAGRLAFT con tipping-off) se hereda de [[Skills Compartidas RITORE]] y aquí solo queda lo diferencial; (b) los dos parseadores de extracto (OFX/MT940 y PDF) se consolidaron en `interpretar-extracto-bancario` con tabla de variantes (> 70 % de procedimiento común); (c) `detectar-anomalias-bancarias` y `escalar-anomalia-a-SAGRLAFT` se unificaron — la detección y la canalización son fases del mismo flujo y el protocolo de escalamiento ya vive en la skill compartida `aplicar-SAGRLAFT-segun-corresponda`; (d) umbrales numéricos para partidas conciliatorias: §3 para montos (1 / 50 / 500 UVT) y los umbrales de antigüedad propios del perfil (30/60/90 días), que se conservan por ser mejores que el genérico — están justificados por el ciclo mensual de conciliación.

---

## Índice de skills en este documento

- `interpretar-extracto-bancario` *(base paramétrica: Excel/CSV · OFX/MT940 · PDF-OCR)*
- `conciliar-extracto-vs-libros`
- `clasificar-movimiento-bancario`
- `aplicar-GMF-correctamente`
- `cuadrar-cuentas-multidivisas`
- `documentar-partida-conciliatoria`
- `detectar-y-canalizar-anomalias-bancarias` *(consolida detección + escalamiento a SAGRLAFT)*
- `generar-papeles-trabajo-conciliacion`

═══════════════════════════════════════════════════════════════════════

---
name: interpretar-extracto-bancario
description: Skill base de ingestión de extractos. Recibe el extracto en cualquier formato — Excel/CSV, OFX/MT940 (estructurados) o PDF imagen/escaneado (OCR) — y lo normaliza al formato interno de conciliación con validación de consistencia. Activa al llegar cualquier extracto a Drive o al solicitarlo el cierre mensual.
agente: RITORE-AuxiliarConciliacionesBancarias-Senior
categoria: operativo
---

# Skill: interpretar-extracto-bancario

## Para qué existe
La conciliación es tan buena como los datos que entran. Esta skill garantiza que todo extracto — venga limpio (OFX) o sucio (PDF escaneado) — llegue a `conciliar-extracto-vs-libros` como tabla normalizada y validada; sin ella, clientes con formatos difíciles quedan sin conciliar.

## Cuándo se activa (por variante)

| Variante | Trigger |
|---|---|
| **X — Excel/CSV** | Extracto en hoja de cálculo cargado a Drive |
| **O — OFX/MT940** | Archivo con extensión/cabecera OFX (XML/SGML) o MT940 (SWIFT bloque 4) |
| **P — PDF/OCR** | PDF sin texto extraíble (imagen o escaneado) |

## Inputs

| Insumo | De quién | Formato | Si falta |
|---|---|---|---|
| Archivo de extracto del periodo | Cliente vía Drive / banco | Según variante | Si al día 2 hábil del mes no ha llegado, solicitar vía AtencionCliente; reiterar 1 vez en 24 h hábiles, luego Orquestador |
| Saldo inicial esperado (saldo final del extracto anterior) | Archivo del periodo anterior (NotionArquitecto) | Tabla normalizada | Sin extracto anterior (cliente nuevo), tomar el saldo inicial del propio extracto con marca `[SALDO INICIAL SIN VERIFICAR]` |
| Identificación de cuenta y banco | Perfil del cliente (`cargar-perfil-cliente`) | Ficha | Cuenta no registrada en el perfil → alertar a Onboarding antes de procesar (posible cuenta no reportada) |

## Procedimiento

**Tronco común (toda variante):**
1. Detectar formato por extensión y cabecera; elegir variante.
2. Ejecutar el parseo de la variante (tabla siguiente).
3. Normalizar al formato interno: fecha ISO 8601, monto con signo (débito/crédito), descripción, referencia, contraparte si está disponible; encoding UTF-8.
4. Validar consistencia global: saldo inicial + Σ créditos − Σ débitos = saldo final del extracto; y saldo inicial = saldo final del periodo anterior.
5. Entregar la tabla validada a `conciliar-extracto-vs-libros` y archivar el original vía NotionArquitecto.

**Pasos específicos por variante:**

| Variante | Pasos propios |
|---|---|
| **X — Excel/CSV** | Detectar fila de encabezados y formato de fecha/decimales del banco (catálogo por banco); descartar filas de subtotales y publicidad; verificar que no haya celdas combinadas que partan movimientos. |
| **O — OFX/MT940** | Parsear según especificación (OFX: XML/SGML; MT940: bloque 4, tags :61:/:86:); validar checksum/estructura — archivo con checksum inválido NO se procesa; extraer código de transacción del estándar. |
| **P — PDF/OCR** | Aplicar OCR (Tesseract o servicio cloud); reconstruir estructura tabular (fecha, descripción, débito, crédito, saldo); medir confianza del OCR por página; releer con configuración alternativa las páginas con error estimado > 5 %. |

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Tabla normalizada del extracto | Validación del paso 4 cumplida: variación de saldo = Σ movimientos, diferencia $0 |
| Extracto original archivado | Convención canónica vía NotionArquitecto |
| Metadata de calidad | Variante usada, % de confianza (OCR), incidencias de parseo |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Suma de movimientos ≠ variación de saldo | Fila perdida (OCR/parseo) o subtotal contado como movimiento | Localizar la página/sección con la diferencia exacta y reprocesarla | Variante P: solicitar al cliente extracto digital (Excel/OFX) vía AtencionCliente; NUNCA pasar a conciliación datos que no cuadran |
| Checksum OFX/estructura MT940 inválida | Archivo truncado en descarga o exportación parcial | NO procesar; solicitar archivo válido al cliente/banco | Mientras llega, usar variante X o P si existe versión alternativa del mismo extracto |
| OCR con error estimado > 5 % tras releer | Escaneo de baja calidad | Solicitar extracto en formato digital al cliente (plazo 24 h hábiles) | Si el cliente solo tiene papel, transcripción asistida con doble verificación de totales y marca `[ORIGEN OCR BAJA CALIDAD]` en los papeles de trabajo |
| Saldo inicial ≠ saldo final del extracto anterior | Falta un extracto intermedio o hubo extracto rectificado por el banco | Solicitar el extracto faltante; verificar con el banco vía cliente si hubo rectificación | Conciliación del periodo queda `bloqueada`; escalar al Orquestador si no se resuelve en 48 h hábiles |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia de cuadre interno del extracto | ≥ 1 UVT | No pasa a conciliación; investigar el parseo |
| Cuenta bancaria no registrada en el perfil del cliente | Cualquier caso | Onboarding + Orquestador (posible cuenta omitida en contabilidad) |
| Extracto imposible de obtener en formato procesable | > 5 días hábiles de gestión | Orquestador (riesgo de cierre sin conciliar) |

## Reglas críticas
🚫 NUNCA entregar a conciliación una tabla cuyo cuadre interno (saldo inicial + movimientos = saldo final) no dé $0.
🚫 NUNCA aceptar archivo estructurado con checksum inválido.
✅ SIEMPRE normalizar fechas a ISO 8601 y encoding a UTF-8 antes de entregar.

## Métricas
- Extractos normalizados dentro de las 24 h siguientes a su llegada: ≥ 95 % (medición mensual).
- Tablas entregadas a conciliación con cuadre interno $0: 100 %.
- Extractos PDF migrados a formato digital por gestión con el cliente: tendencia creciente trimestral.

## Tests
### Test 1 — (normal, O) Extracto OFX de Bancolombia con 240 movimientos y checksum válido
**Output:** parseo según especificación OFX, normalización ISO 8601/UTF-8, cuadre interno $0, continuidad de saldo con el periodo anterior verificada; tabla entregada a `conciliar-extracto-vs-libros` y original archivado.
### Test 2 — (excepción, P) PDF escaneado torcido: el OCR estima 8 % de error y, tras releer, la suma de movimientos difiere del saldo en $740.000
**Output:** datos NO entregados a conciliación; solicitud de extracto digital al cliente vía AtencionCliente con plazo de 24 h hábiles; al recibir el CSV del portal bancario, reproceso por variante X con cuadre $0; incidencia registrada en metadata y propuesta al cliente de envío mensual en formato digital.

═══════════════════════════════════════════════════════════════════════

---
name: conciliar-extracto-vs-libros
description: Activa cada vez que haya un extracto normalizado disponible o al iniciar el cierre mensual. Concilia movimiento por movimiento extracto vs libros, identifica partidas conciliatorias, dispara la detección de anomalías y produce el insumo de los papeles de trabajo. Sin esta skill los saldos de efectivo son inconfiables.
agente: RITORE-AuxiliarConciliacionesBancarias-Senior
categoria: operativo
---

# Skill: conciliar-extracto-vs-libros

## Para qué existe
Es la skill núcleo del perfil: confronta la realidad bancaria con los libros. Sin ella, el saldo de efectivo de los EEFF es una declaración de fe y los errores (y fraudes) viven indefinidamente.

## Cuándo se activa
- Tabla normalizada entregada por `interpretar-extracto-bancario`.
- Inicio del cierre mensual (verificación de que toda cuenta del cliente quede conciliada).
- Solicitud del Revisor Fiscal o del Contador Titular.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Extracto normalizado y validado | `interpretar-extracto-bancario` | No se concilia sobre datos sin validar; esperar la tabla |
| Auxiliar de bancos (libros) del periodo | AuxContable / ERP | Timeout 4 h → último auxiliar verificado con marca `[DATO EN CACHÉ — verificar]` SOLO para preconciliación; la conciliación definitiva espera el dato real |
| Perfil del cliente (cuentas, exenciones GMF, patrones recurrentes) | `cargar-perfil-cliente` | Solicitar; sin perfil la conciliación procede pero las validaciones de GMF quedan `pendientes` |

## Procedimiento
1. `cargar-perfil-cliente`.
2. Matching automático por línea: monto exacto + fecha ± 3 días + similitud de descripción. Si match → conciliado.
3. Segundo pase para matchings compuestos: un pago en libros contra varios movimientos del extracto (o viceversa), suma exacta.
4. Tipificar partidas no matcheadas: cheque pendiente de cobro, depósito en tránsito, comisión no contabilizada, GMF no contabilizado, movimiento en libros sin extracto, movimiento en extracto sin libros, posible anomalía.
5. Disparar skills satélite: `aplicar-GMF-correctamente` (movimientos sujetos), `clasificar-movimiento-bancario` (movimientos del extracto sin contraparte en libros), `documentar-partida-conciliatoria` (cada partida tipificada), `detectar-y-canalizar-anomalias-bancarias` (patrones del paso 4).
6. Calcular: saldo extracto + depósitos en tránsito − cheques pendientes ± errores = saldo en libros ajustado; la identidad debe dar diferencia $0.
7. Notificar: AuxContable (movimientos identificados sin asentar), CarteraCxP (pagos/recaudos con NIT identificado), Tesorería (saldo disponible real).
8. Entregar el resultado a `generar-papeles-trabajo-conciliacion`.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Conciliación del periodo por cuenta | Identidad del paso 6 con diferencia $0; toda partida no matcheada tipificada y documentada |
| Partidas conciliatorias registradas | 100 % con naturaleza, monto, fecha y fecha esperada de cierre |
| Notificaciones a AuxContable/CarteraCxP/Tesorería | Emitidas el mismo día hábil |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Saldo conciliado ≠ saldo según libros ajustado (diferencia residual) | Partida no tipificada, matching falso positivo o error de libros | Buscar por diferencia exacta (monto único o combinación); revisar matchings de ±3 días | Si tras búsqueda exhaustiva la diferencia persiste ≥ 1 UVT, la conciliación NO se cierra: escalar según tabla de escalamiento con el trabajo documentado |
| Matching falso positivo (mismo monto, operación distinta) | Montos repetidos en el periodo | Deshacer el match, exigir coincidencia de referencia/tercero para montos repetidos | Marcar ambos movimientos para verificación manual contra soporte |
| Auxiliar de libros desactualizado (asientos del periodo sin registrar) | AuxContable atrasado | Notificar a AuxContable el lote pendiente y pre-conciliar con lo disponible | La conciliación queda `parcial`; si el atraso supera 48 h hábiles en cierre, Orquestador |
| Partidas conciliatorias > 30 días sin resolver | Cheques no cobrados, consignaciones sin identificar | Tratamiento por `documentar-partida-conciliatoria` (umbral de antigüedad propio del perfil) | — |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia residual de conciliación | ≥ 1 UVT individual o ≥ 0,5 % del saldo de la cuenta | Investigar y documentar antes de cerrar la conciliación |
| Diferencia residual no resuelta | ≥ 50 UVT | Contador Titular vía Orquestador (no hay Master de conciliaciones; el dominio escala directo) |
| Diferencia residual no resuelta | ≥ 500 UVT | Contador Titular, mismo día, prioridad alta |
| Señal de anomalía / SAGRLAFT | Cualquier monto | `detectar-y-canalizar-anomalias-bancarias` (canal restringido) |

## Reglas críticas
🚫 NUNCA cerrar conciliación con partidas no documentadas o con diferencia residual ≥ 1 UVT sin investigar.
🚫 NUNCA contabilizar yo mismo (eso es AuxContable) ni conciliar con terceros externos (eso es CarteraCxP).
✅ SIEMPRE disparar GMF, clasificación, documentación de partidas y detección de anomalías como parte del flujo, no como pasos opcionales.

## Métricas
- Cuentas conciliadas antes del día 5 hábil: 100 % (medición mensual).
- Tasa de matching automático: ≥ 90 % de movimientos, con tendencia creciente por cliente.
- Conciliaciones cerradas con diferencia residual $0: 100 %.

## Tests
### Test 1 — (normal) Cuenta Bancolombia con 180 movimientos: matching automático 94 %, 6 cheques pendientes, 2 consignaciones en tránsito, GMF del mes sin contabilizar
**Output:** identidad de conciliación con diferencia $0; 8 partidas conciliatorias tipificadas y documentadas; GMF disparado a `aplicar-GMF-correctamente`; notificaciones a AuxContable (GMF y comisiones por asentar), Tesorería (saldo disponible) y entrega a papeles de trabajo.
### Test 2 — (excepción) Tras conciliar queda una diferencia residual de $18M (≈ 0,9 % del saldo y > 50 UVT) que no corresponde a ninguna partida tipificada
**Output:** conciliación NO cerrada; búsqueda por diferencia exacta detecta un traslado entre cuentas del cliente registrado en libros una sola vez (salida sin la entrada); AuxContable notificado para el asiento faltante; si no se hubiera identificado, escalamiento al Contador Titular el mismo día (≥ 50 UVT) con todo el trabajo de búsqueda documentado en los papeles.

═══════════════════════════════════════════════════════════════════════

---
name: clasificar-movimiento-bancario
description: Activa por cada movimiento bancario que necesite identificación de contraparte y naturaleza — pago a proveedor, cobro de cliente, pago de impuestos, transferencia interna, comisión, GMF. Sin esta skill los movimientos quedan sin asignar y la conciliación se rompe.
agente: RITORE-AuxiliarConciliacionesBancarias-Senior
categoria: operativo
---

# Skill: clasificar-movimiento-bancario

## Para qué existe
Un movimiento sin contraparte identificada no puede contabilizarse ni aplicarse a cartera: esta skill convierte descripciones bancarias crípticas en operaciones con nombre, NIT y destino.

## Cuándo se activa
- Movimiento del extracto sin match en libros, derivado de `conciliar-extracto-vs-libros`.
- Solicitud puntual de Tesorería o CarteraCxP sobre un movimiento específico.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Movimiento: fecha, monto, descripción, referencia | `conciliar-extracto-vs-libros` | — (es el objeto de la skill) |
| Facturas pendientes y programación de pagos | CarteraCxP / Tesorería | Timeout 4 h → clasificar solo con catálogos locales y marcar lo no identificado |
| Catálogo de recurrentes del cliente (servicios, comisiones, impuestos con calendario DIAN) | Memoria del agente + `cargar-perfil-cliente` | Construir catálogo desde los 6 meses previos del extracto |

## Procedimiento
1. Analizar descripción + monto + fecha del movimiento.
2. Buscar matching contra: facturas pendientes (CarteraCxP), programación de pagos (Tesorería), calendarios DIAN (pagos de impuestos), recurrentes (servicios públicos, comisiones, cuotas).
3. Extraer NIT de la descripción si está presente y cruzar contra maestro de terceros.
4. Asignar naturaleza y contraparte con nivel de confianza (alta/media/baja).
5. Notificar al agente correspondiente: CarteraCxP (aplicación), Tesorería (programados), AuxContable (asiento).
6. Registrar la lógica de clasificación aplicada (alimenta el matching futuro).

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Movimiento clasificado (naturaleza + contraparte + confianza) | Confianza alta para notificar a contabilización directa; media/baja exige verificación |
| Notificación al agente destino | Emitida el mismo día hábil |
| Regla de clasificación registrada | Reutilizable en periodos siguientes |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Contraparte no identificable | Descripción genérica del banco ("transferencia recibida") | Marcar `pendiente_identificacion` y consultar al cliente vía AtencionCliente (plazo de respuesta 24 h hábiles, reiterar 1 vez) | Mantener como partida conciliatoria documentada; si ≥ 50 UVT y > 30 días sin identificar, escalar al Contador Titular (consignación no identificada es además ingreso potencial no reconocido) |
| Dos candidatos plausibles para el mismo movimiento | Facturas del mismo tercero por montos iguales | Pedir a CarteraCxP el criterio de aplicación (factura más antigua / instrucción del cliente) | Aplicar a la más antigua con marca `[APLICACIÓN POR DEFECTO]` y nota al cliente |
| Contraparte aparece en lista restrictiva | Señal SAGRLAFT | Activar `detectar-y-canalizar-anomalias-bancarias` SIN marcar nada visible en los canales normales | El protocolo restringido lo gobierna la skill compartida `aplicar-SAGRLAFT-segun-corresponda` |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Movimiento sin identificar | ≥ 1 UVT y > 24 h hábiles | Consulta al cliente vía AtencionCliente |
| Movimiento sin identificar | ≥ 50 UVT o > 30 días | Contador Titular |
| Acumulado de movimientos sin identificar en una cuenta | ≥ 5 % del total de movimientos del mes | Orquestador (señal de desconexión entre cliente y contabilidad) |

## Reglas críticas
🚫 NUNCA inventar contraparte ni forzar una aplicación sin evidencia.
✅ SIEMPRE registrar la lógica de clasificación para que el matching aprenda.
✅ SIEMPRE tratar las consignaciones no identificadas también como tema de ingresos (no solo de conciliación).

## Métricas
- Movimientos clasificados con confianza alta: ≥ 85 % (medición mensual, tendencia creciente).
- Movimientos `pendiente_identificacion` al cierre: ≤ 2 % del volumen del mes.
- Reglas de clasificación reutilizadas con éxito: ≥ 70 % de los recurrentes.

## Tests
### Test 1 — (normal) Débito de $4,2M cuya descripción contiene NIT de un proveedor con factura pendiente por el mismo monto
**Output:** clasificado como pago a proveedor, confianza alta; notificación a CarteraCxP para aplicación y a AuxContable para asiento; regla registrada (NIT + monto exacto).
### Test 2 — (excepción) Consignación de $30M con descripción "transferencia recibida" sin NIT ni referencia, sin CxC abierta por ese monto
**Output:** marca `pendiente_identificacion`; consulta al cliente vía AtencionCliente con plazo 24 h hábiles y una reiteración; partida conciliatoria documentada; al no identificarse en 30 días y superar 50 UVT → Contador Titular con la advertencia de ingreso potencial no reconocido; si la contraparte resultara estar en lista restrictiva, activación inmediata del canal de anomalías.

═══════════════════════════════════════════════════════════════════════

---
name: aplicar-GMF-correctamente
description: Activa al detectar movimientos sujetos al Gravamen a los Movimientos Financieros (Arts. 870-881 ET). Aplica la tarifa 4×1.000, valida exenciones (Art. 879 ET) y marca la deducibilidad parcial en renta (50 %, Art. 115 ET). Sin esta skill se contabiliza mal el GMF y se afecta la deducibilidad.
agente: RITORE-AuxiliarConciliacionesBancarias-Senior
categoria: operativo
---

# Skill: aplicar-GMF-correctamente

## Para qué existe
El GMF mal tratado produce dos errores silenciosos: pagarlo donde había exención (costo innecesario) y deducirlo al 100 % en renta cuando solo procede el 50 % (Art. 115 ET) — riesgo directo en la declaración.

## Cuándo se activa
- Movimientos sujetos detectados durante `conciliar-extracto-vs-libros` (retiros, transferencias salientes, pagos).
- Verificación mensual: GMF cobrado por el banco vs GMF teórico calculado.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Movimientos del periodo con su naturaleza | `conciliar-extracto-vs-libros` | — (flujo interno) |
| Marcación de cuenta exenta y exenciones aplicables del cliente (Art. 879 ET) | `cargar-perfil-cliente` | Sin perfil de exenciones, calcular GMF teórico pleno y marcar la validación `pendiente`; no reclamar al banco sin confirmar |
| GMF efectivamente cobrado por el banco | Extracto normalizado | — (viene en el extracto) |

## Procedimiento
1. Identificar movimientos sujetos: retiros, transferencias salientes, pagos a terceros.
2. Validar exenciones (Art. 879 ET): cuenta marcada exenta (una por titular), traslados entre cuentas del mismo titular en el mismo banco, pagos de seguridad social, operaciones específicas exentas.
3. Calcular GMF teórico = base sujeta × 4/1.000.
4. Comparar GMF teórico vs GMF cobrado por el banco en el periodo.
5. Notificar a AuxContable el asiento del GMF con la marca de deducibilidad parcial: solo el 50 % es deducible en renta (Art. 115 ET) → la marca alimenta a EspecialistaRenta.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Cuadre GMF teórico vs cobrado | Diferencia $0 o explicada movimiento a movimiento |
| Notificación de asiento a AuxContable | Incluye marca `deducible_50%` (Art. 115 ET) |
| Reclamos al banco identificados | Cada cobro improcedente con movimiento, monto y exención aplicable |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| GMF cobrado ≠ GMF teórico del mes | Exención no aplicada por el banco, o base mal calculada por mí | Cuadrar movimiento a movimiento hasta aislar la diferencia | Diferencia ≥ 1 UVT sin explicar → no cerrar el cuadre; documentar e investigar con el extracto del mes siguiente (cobros retroactivos del banco) |
| Cuenta marcada exenta presenta cobros de GMF | Banco no registró la marcación o el cliente excedió el tope exento mensual | Verificar el tope de la exención; si el cobro es improcedente, preparar reclamo al banco vía cliente (AtencionCliente) | Si el banco no responde en 30 días, escalar al Contador Titular con el acumulado del reclamo |
| GMF aplicado a traslado entre cuentas del mismo titular | Exención del Art. 879 ET no reconocida | Confirmar misma titularidad y mismo banco; preparar reclamo | Registrar el GMF cobrado mientras se resuelve (la contabilidad refleja la realidad), con marca de reclamo en curso |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia GMF teórico vs cobrado | ≥ 1 UVT | Investigar y documentar antes de cerrar el cuadre |
| GMF cobrado improcedentemente (acumulado en reclamo) | ≥ 50 UVT | Contador Titular |
| Patrón de error del banco recurrente (3+ meses) | Cualquier monto | Orquestador + AtencionCliente (gestión formal con el banco) |

## Reglas críticas
🚫 NUNCA validar GMF sobre operaciones exentas sin verificar la exención específica del Art. 879 ET.
🚫 NUNCA marcar el GMF como 100 % deducible: solo el 50 % (Art. 115 ET).
✅ SIEMPRE cuadrar el GMF del mes contra lo efectivamente cobrado por el banco.

## Métricas
- Meses con cuadre GMF teórico vs cobrado en diferencia $0 o explicada: 100 %.
- Cobros improcedentes detectados y reclamados: 100 % de los identificados.
- Asientos de GMF con marca de deducibilidad parcial: 100 %.

## Tests
### Test 1 — (normal) Mes con 40 movimientos sujetos; el banco cobró $812.000 de GMF y el teórico da $812.000
**Output:** cuadre $0; asiento notificado a AuxContable con marca `deducible_50%`; EspecialistaRenta recibe la marca para la depuración de renta.
### Test 2 — (excepción) La cuenta de nómina del cliente, marcada exenta, muestra cobros de GMF por $640.000 en el mes
**Output:** verificación del tope de exención (no excedido) → cobro improcedente; reclamo preparado al banco vía AtencionCliente con el detalle por movimiento; GMF cobrado se asienta mientras tanto (realidad bancaria) con marca de reclamo en curso; seguimiento a 30 días; si el acumulado del reclamo supera 50 UVT, Contador Titular.

═══════════════════════════════════════════════════════════════════════

---
name: cuadrar-cuentas-multidivisas
description: Activa cuando el cliente tenga cuentas en USD/EUR u otra moneda extranjera. Convierte a COP con la TRM de la fecha de cada movimiento, valoriza el saldo al cierre y registra la diferencia en cambio (NIC 21 / Sección 30). Sin esta skill las cuentas extranjeras se desconectan de los EEFF.
agente: RITORE-AuxiliarConciliacionesBancarias-Senior
categoria: operativo
---

# Skill: cuadrar-cuentas-multidivisas

## Para qué existe
Las cuentas en moneda extranjera generan dos cifras que nadie más calcula: la conversión transaccional a TRM de cada operación y la diferencia en cambio del cierre (NIC 21 / Sección 30). Sin esta skill, el saldo en COP de esas cuentas es ficción.

## Cuándo se activa
- Conciliación de cualquier cuenta en moneda distinta de COP (detectada por el perfil del cliente o por la divisa del extracto).
- Cierre mensual: valorización del saldo final a TRM de cierre.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Extracto normalizado de la cuenta en divisa | `interpretar-extracto-bancario` | Flujo normal de ingestión |
| TRM oficial por fecha | Banco de la República (serie oficial) | Si la TRM de una fecha específica no está disponible (feriado/fin de semana), usar la TRM vigente certificada para ese día (la del último día hábil) y documentar la fuente |
| Marco NIIF del cliente (plenas: NIC 21 / Pymes: Sección 30) | `cargar-perfil-cliente` | Solicitar; el tratamiento es equivalente para conversión transaccional, pero se documenta el marco |

## Procedimiento
1. Detectar cuentas en moneda extranjera del cliente.
2. Convertir cada movimiento a COP con la TRM vigente de la fecha de la operación.
3. Conciliar la cuenta en su moneda origen (la conciliación es en divisa; la conversión es un cálculo derivado).
4. Al cierre: valorizar el saldo final a TRM de cierre del mes.
5. Calcular diferencia en cambio = saldo valorizado a TRM cierre − saldo en libros COP; clasificar como ingreso o gasto financiero (NIC 21 / Sección 30).
6. Notificar a AuxContable (asiento de diferencia en cambio) y a EspecialistaNIIF si la diferencia del periodo es ≥ 50 UVT.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Conciliación en divisa origen | Diferencia $0 en la moneda de la cuenta |
| Conversión a COP documentada | TRM por fecha con fuente (serie oficial BanRep) |
| Asiento de diferencia en cambio | Cuadra con el recálculo: saldo divisa × TRM cierre = saldo COP tras el ajuste |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| TRM no disponible para una fecha | Feriado o fin de semana | Usar la TRM certificada vigente para ese día (último día hábil) y documentar | NUNCA usar TRM aproximada o promedio cuando existe TRM certificada |
| Saldo en COP no cuadra tras el ajuste de cierre | Movimiento convertido con TRM de fecha errada | Recalcular la conversión movimiento por movimiento contra la serie oficial | Diferencia ≥ 1 UVT persiste → no cerrar la valorización; escalar a EspecialistaNIIF con el papel de recálculo |
| El banco reporta el extracto con conversión propia a COP | Cuenta dual o reporte del banco en ambas monedas | Conciliar SIEMPRE sobre la divisa origen; la conversión propia del banco no reemplaza la TRM oficial | Documentar la diferencia entre conversión del banco y TRM oficial si genera confusión en libros |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Descuadre de conversión | ≥ 1 UVT | Investigar y documentar antes de cerrar |
| Diferencia en cambio del periodo | ≥ 50 UVT | EspecialistaNIIF (validación del tratamiento) |
| Diferencia en cambio o ajuste acumulado | ≥ 500 UVT | Contador Titular vía Orquestador |

## Reglas críticas
🚫 NUNCA usar TRM aproximada para fechas con TRM certificada disponible.
🚫 NUNCA omitir la valorización y la diferencia en cambio en el cierre.
✅ SIEMPRE conciliar en la divisa origen y derivar el COP, no al revés.

## Métricas
- Cierres con valorización a TRM de cierre registrada: 100 % de las cuentas en divisa.
- Descuadres de conversión al cierre: $0 (toda diferencia explicada).
- Diferencias en cambio ≥ 50 UVT validadas con NIIF: 100 %.

## Tests
### Test 1 — (normal) Cuenta USD con 12 movimientos en el mes; saldo final USD 45.000
**Output:** conciliación en USD con diferencia $0; cada movimiento convertido con TRM de su fecha (serie BanRep documentada); valorización del saldo a TRM de cierre; diferencia en cambio calculada y notificada a AuxContable como ingreso/gasto financiero según signo.
### Test 2 — (excepción) Tres movimientos caen en Semana Santa (sin TRM propia del día) y la diferencia en cambio del mes da 65 UVT
**Output:** conversión con la TRM certificada vigente para esos días (la del último día hábil), fuente documentada en el papel de trabajo; diferencia en cambio ≥ 50 UVT → validación con EspecialistaNIIF antes del asiento; asiento emitido a AuxContable tras el visto bueno y papel de recálculo archivado.

═══════════════════════════════════════════════════════════════════════

---
name: documentar-partida-conciliatoria
description: Activa por cada partida conciliatoria detectada (cheque pendiente, depósito en tránsito, comisión o GMF sin contabilizar, movimiento sin identificar). Documenta, controla la antigüedad con umbrales 30/60/90 días y gestiona su resolución. Sin esta skill las partidas envejecen y el cliente no sabe qué pasa con su efectivo.
agente: RITORE-AuxiliarConciliacionesBancarias-Senior
categoria: operativo
---

# Skill: documentar-partida-conciliatoria

## Para qué existe
Una partida conciliatoria sin dueño ni fecha de cierre esperada se vuelve permanente — y una partida permanente suele esconder un error o algo peor. Esta skill les pone naturaleza, responsable, reloj y salida.

## Cuándo se activa
- Cada partida tipificada por `conciliar-extracto-vs-libros`.
- Cron semanal de revisión de antigüedad del inventario de partidas abiertas.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Partida tipificada: naturaleza, monto, fecha de origen | `conciliar-extracto-vs-libros` | — (flujo interno) |
| Soporte de la partida (copia de cheque, consignación, nota del banco) | Cliente / banco vía AtencionCliente | Documentar la partida con lo disponible y solicitar el soporte (espera 24 h hábiles, reiterar 1 vez) |
| Inventario de partidas abiertas de periodos anteriores | Registro propio de la skill | Reconstruir desde los papeles de trabajo archivados |

## Procedimiento
1. Registrar la partida: fecha de origen, monto, naturaleza (cheque pendiente / depósito en tránsito / comisión / GMF / sin identificar), contraparte si se conoce, fecha esperada de cierre y responsable de resolución.
2. Asignar el reloj de antigüedad (umbrales propios del perfil, justificados por el ciclo mensual de conciliación — declarados conforme al §3 del estándar):
   - **> 30 días** → marca `envejecida`; gestión activa con el responsable.
   - **> 60 días** → alerta al Contador Titular con el detalle y lo gestionado.
   - **> 90 días** → propuesta formal de ajuste contable al Contador Titular (p. ej. cheque no cobrado → reverso del pago y reconocimiento del pasivo).
3. Notificar a CarteraCxP si la partida involucra un tercero externo (aplicación pendiente).
4. Cron semanal: recalcular antigüedades, ejecutar las acciones del paso 2 y actualizar el inventario.
5. Al resolverse: cerrar la partida con referencia al documento o asiento que la resolvió.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Partida documentada | Tiene naturaleza, monto, origen, responsable y fecha esperada de cierre |
| Inventario de partidas con antigüedad | Sin partidas > 30 días sin gestión documentada |
| Propuestas de ajuste (> 90 días) | Con tratamiento contable propuesto y soporte de la gestión realizada |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Partida > 60 días sin respuesta del responsable | Cliente o banco no contesta | Alerta al Contador Titular (umbral del perfil) con el historial de gestión | El Contador Titular decide presión comercial o ajuste anticipado |
| Cheque pendiente supera la vigencia legal de cobro | Beneficiario nunca lo cobró | Proponer al Contador Titular el reverso del pago y la reclasificación del pasivo | Mantener la partida con la propuesta documentada hasta decisión humana |
| La misma partida reaparece como nueva en otro periodo | Inventario de partidas no consultado al conciliar | Unificar bajo el registro original (la antigüedad cuenta desde el origen real) | Auditar el inventario completo de la cuenta y corregir duplicados |
| Partida `sin identificar` ≥ 50 UVT | Movimiento opaco | Tratarla además por `clasificar-movimiento-bancario` y evaluar señal de anomalía | Escalamiento según tabla |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Partida abierta | ≥ 1 UVT y > 30 días | Gestión activa documentada (marca `envejecida`) |
| Partida abierta | > 60 días, o ≥ 50 UVT a cualquier edad | Contador Titular |
| Partida abierta | > 90 días | Propuesta de ajuste contable al Contador Titular |
| Partida sin identificar | ≥ 500 UVT | Contador Titular, mismo día |

## Reglas críticas
🚫 NUNCA dejar partidas sin documentar ni sin responsable asignado.
🚫 NUNCA cerrar una partida sin referencia al documento o asiento que la resolvió.
✅ SIEMPRE contar la antigüedad desde el origen real, no desde el último periodo conciliado.

## Métricas
- Partidas documentadas con responsable y fecha esperada: 100 %.
- Partidas > 60 días sobre el total abierto: ≤ 5 % (medición mensual).
- Partidas > 90 días sin propuesta de ajuste: 0.

## Tests
### Test 1 — (normal) Cheque girado hace 15 días que aún no aparece cobrado en el extracto
**Output:** partida registrada (naturaleza: cheque pendiente, responsable: beneficiario vía cliente, fecha esperada: vigencia del cheque); sin marcas de antigüedad; aparecerá en el inventario del cron semanal hasta su cobro.
### Test 2 — (excepción) Depósito en tránsito de $11M cumple 70 días sin reflejarse en el extracto pese a dos solicitudes de soporte al cliente
**Output:** > 60 días → alerta al Contador Titular con historial de gestión (2 reiteraciones documentadas); hipótesis registrada (consignación reversada por el banco o registro contable sin operación real); a los 90 días, propuesta formal de ajuste (reverso del registro en libros) y verificación con `detectar-y-canalizar-anomalias-bancarias` por si el patrón sugiere registro ficticio.

═══════════════════════════════════════════════════════════════════════

---
name: detectar-y-canalizar-anomalias-bancarias
description: Activa con cada extracto procesado. Busca patrones anómalos — estructuración, contrapartes en listas restrictivas, transferencias internacionales sin soporte, cargos duplicados, saldos contranatura — distingue error operativo (se gestiona con el cliente) de señal SAGRLAFT (canal restringido, jamás al cliente) y canaliza cada una. Consolida las antiguas skills de detección y de escalamiento a SAGRLAFT: eran fases del mismo flujo.
agente: RITORE-AuxiliarConciliacionesBancarias-Senior
categoria: cumplimiento
---

# Skill: detectar-y-canalizar-anomalias-bancarias

## Para qué existe
El Conciliador es el agente que más de cerca ve el dinero moverse: es el vigía natural de fraude, error bancario y lavado. Esta skill define QUÉ patrones buscar en extractos y A QUÉ canal va cada hallazgo. El protocolo SAGRLAFT en sí (tipping-off, canal aislado, marca `restringido_sagrlaft`) NO se duplica aquí: se hereda de `aplicar-SAGRLAFT-segun-corresponda` en [[Skills Compartidas RITORE]].

## Cuándo se activa
- Automáticamente con cada extracto conciliado (`conciliar-extracto-vs-libros`, paso de anomalías).
- Contraparte en lista restrictiva detectada por `clasificar-movimiento-bancario`.
- Patrón sospechoso reportado por cualquier otra skill del perfil.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Movimientos del periodo + histórico de 6 meses | Extractos normalizados archivados | Con < 6 meses de histórico (cliente nuevo), análisis con lo disponible y marca `[BASE HISTÓRICA PARCIAL]` |
| Listas restrictivas vigentes | SAGRLAFT (servicio de listas) | Timeout 4 h → usar última lista cacheada con marca `[DATO EN CACHÉ — verificar]` y reverificar al restablecerse |
| Estado KYC/DDI del cliente | `memoria.cliente_contexto` | Tratar como cliente sin DDI reforzada (umbral de sensibilidad normal) |

## Procedimiento
1. Analizar el patrón de movimientos del mes contra los 6 meses previos.
2. Buscar patrones de **señal SAGRLAFT**: estructuración (depósitos en efectivo recurrentes bajo el umbral UIAF de $10M), contrapartes en listas restrictivas, transferencias internacionales sin documentación, operaciones sin soporte económico aparente.
3. Buscar patrones de **error operativo**: cargos duplicados, comisiones inusuales o no pactadas, saldos negativos no operacionales, débitos no reconocidos.
4. Clasificar cada hallazgo en una de las dos categorías — esta distinción es la regla de oro de la skill: el error operativo SE comunica al cliente; la señal SAGRLAFT JAMÁS.
5. **Señal SAGRLAFT** → activar `aplicar-SAGRLAFT-segun-corresponda` (skill compartida: canal aislado, sin cc, sin tipping-off) y continuar la conciliación con total normalidad.
6. **Error operativo** → notificar a AtencionCliente (gestión/reclamo con el banco) y a AuxContable (efecto contable si existe).
7. Registrar el hallazgo y su desenlace para calibrar umbrales propios (falsos positivos).

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Hallazgos clasificados (SAGRLAFT / operativo) | Cada hallazgo con evidencia: montos, fechas, contraparte, patrón |
| Activación del canal correspondiente | SAGRLAFT vía skill compartida (sin rastro en canales normales); operativo vía AtencionCliente |
| Registro de calibración | Desenlace de cada hallazgo (confirmado / falso positivo) documentado |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Duda entre error operativo y señal SAGRLAFT | Patrón ambiguo (p. ej. depósitos en efectivo crecientes pero con soporte parcial) | Ante duda razonable, canalizar como SAGRLAFT (la skill compartida lo exige); NUNCA preguntar al cliente para "aclarar" | — (la duda ya tiene tratamiento definido) |
| Misma anomalía operativa reportada 2+ veces sin acción correctiva | Cliente o banco no gestiona | Escalar al Orquestador con el historial | Contador Titular decide si la inacción amerita gestión directa |
| Falsos positivos recurrentes de un mismo patrón | Umbral propio demasiado sensible | Recalibrar el umbral local y documentar el cambio | Si la calibración exige criterio de cumplimiento, consultar a SAGRLAFT (sin caso concreto abierto, consulta metodológica) |
| Histórico insuficiente para línea base | Cliente nuevo | Comparar contra patrones del sector del cliente como referencia provisional | Marca `[BASE HISTÓRICA PARCIAL]` en el análisis hasta completar 6 meses |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Señal SAGRLAFT (cualquiera) | Sin umbral mínimo — la duda razonable basta | Canal restringido vía `aplicar-SAGRLAFT-segun-corresponda` |
| Error operativo con efecto económico | ≥ 1 UVT | AtencionCliente (reclamo) + AuxContable |
| Error operativo no corregido por el banco | ≥ 50 UVT acumulado | Contador Titular |
| Anomalía repetida sin acción | 2.ª ocurrencia | Orquestador |

## Reglas críticas
🚫 NUNCA comunicar al cliente una señal SAGRLAFT ni sus indicios (la regla completa de tipping-off vive en la skill compartida y se hereda).
✅ SIEMPRE distinguir explícitamente error operativo (se gestiona con el cliente) de señal SAGRLAFT (canal aislado) — es la decisión diferencial de ESTA skill.
✅ SIEMPRE continuar la conciliación con normalidad tras canalizar una señal.

## Métricas
- Extractos procesados con análisis de anomalías ejecutado: 100 %.
- Tiempo entre detección de señal y activación del canal: ≤ 4 h.
- Tasa de falsos positivos SAGRLAFT (cerrados sin acción por SAGRLAFT): ≤ 30 % con tendencia decreciente (medición trimestral, insumo de calibración).

## Tests
### Test 1 — (normal, operativo) El extracto muestra dos cobros idénticos de la misma comisión de manejo ($89.000) el mismo día
**Output:** clasificado como error operativo (cargo duplicado); notificación a AtencionCliente para reclamo al banco y a AuxContable (asentar lo cobrado y el reverso cuando el banco abone); registro del hallazgo; sin activación SAGRLAFT.
### Test 2 — (excepción, señal) Cliente comercial que históricamente recauda por transferencia empieza a recibir 6 consignaciones en efectivo de $9,8M en 10 días, en dos ciudades donde no tiene operación
**Output:** patrón de estructuración + cambio abrupto de comportamiento → activación de `aplicar-SAGRLAFT-segun-corresponda` (canal restringido, prioridad crítica, sin cc); la conciliación del mes continúa y se entrega con total normalidad; cero menciones al cliente ni en papeles de trabajo visibles; desenlace registrado en el log de calibración restringido.

═══════════════════════════════════════════════════════════════════════

---
name: generar-papeles-trabajo-conciliacion
description: Activa al cierre mensual para producir papeles de trabajo auditables por cuenta bancaria, consumibles por el Revisor Fiscal bajo NIAS. Sin esta skill el RF no puede soportar su dictamen y la conciliación no es demostrable.
agente: RITORE-AuxiliarConciliacionesBancarias-Senior
categoria: operativo
---

# Skill: generar-papeles-trabajo-conciliacion

## Para qué existe
Una conciliación que no queda en papeles de trabajo verificables no existe para efectos de auditoría: esta skill convierte el trabajo del mes en evidencia con estructura NIAS, firmada y archivada.

## Cuándo se activa
- Cierre mensual, tras completarse `conciliar-extracto-vs-libros` para todas las cuentas del cliente.
- Solicitud del Revisor Fiscal o del Contador Titular (auditoría, dictamen, requerimiento).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Conciliación cerrada por cuenta (diferencia $0) | `conciliar-extracto-vs-libros` | NO se generan papeles de conciliaciones abiertas; gestionar el cierre primero |
| Inventario de partidas conciliatorias actualizado | `documentar-partida-conciliatoria` | Regenerar desde el registro de partidas antes de emitir |
| Copia del extracto original | `interpretar-extracto-bancario` (archivo) | Recuperar de NotionArquitecto; sin extracto adjunto el papel está incompleto |

## Procedimiento
1. Por cada cuenta bancaria del cliente, compilar: saldo según extracto (con copia del extracto), saldo según libros, listado detallado de partidas conciliatorias (naturaleza, monto, antigüedad, gestión), y saldo conciliado.
2. Verificar consistencia interna: saldo extracto ± partidas = saldo libros, diferencia $0; antigüedades del listado = inventario de partidas.
3. Firmar electrónicamente como agente con timestamp.
4. Archivar vía NotionArquitecto con convención canónica (versión oficial inmutable).
5. Notificar al RevisorFiscal si el cliente está obligado a revisoría fiscal; al Contador Titular en todos los casos.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Papeles de trabajo por cuenta | Estructura completa (4 bloques del paso 1) + extracto adjunto + firma con timestamp |
| Archivo oficial | Convención canónica; inmutable tras la firma |
| Notificación a RF / Contador Titular | Emitida dentro de las 24 h siguientes a la firma |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Inconsistencia interna en los papeles (suma de partidas no explica la diferencia de saldos) | Partida omitida o monto desactualizado | NO firmar; regenerar contra el inventario de partidas y la conciliación fuente | Si la inconsistencia viene de la conciliación, reabrirla (`conciliar-extracto-vs-libros`) antes de emitir papeles |
| Partida sin documentar > 60 días aparece al compilar | Gestión de partidas atrasada | Alertar al Contador Titular ANTES de firmar (umbral de antigüedad del perfil) | Papeles emitidos con la partida claramente revelada y la alerta referenciada; nunca ocultarla |
| Error detectado DESPUÉS de archivada la versión oficial | Hallazgo posterior del RF o de auditoría | Emitir versión corregida como nuevo documento referenciando el original (no se altera el archivado) | Documentar la corrección vía `documentar-decision-no-trivial` |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Partida sin documentar en papeles | > 60 días o ≥ 50 UVT | Contador Titular antes de firmar |
| Papeles del mes no emitidos | > día 10 hábil | Orquestador |
| Corrección de papeles ya entregados al RF | Cualquier caso | Contador Titular (informativo) + RF |

## Reglas críticas
🚫 NUNCA firmar papeles con inconsistencias internas o partidas sin documentar.
🚫 NUNCA alterar una versión oficial archivada: las correcciones son documentos nuevos referenciados.
✅ SIEMPRE adjuntar la copia del extracto: el papel sin fuente no es evidencia.

## Métricas
- Papeles emitidos antes del día 10 hábil: 100 % (medición mensual).
- Papeles devueltos por el RF o el Contador Titular por inconsistencia: 0.
- Cuentas del cliente cubiertas con papeles: 100 %.

## Tests
### Test 1 — (normal) Cliente con revisoría fiscal obligatoria y 3 cuentas bancarias, las 3 conciliadas en $0
**Output:** 3 papeles de trabajo completos (extracto adjunto, partidas detalladas con antigüedad, saldo conciliado), firmados con timestamp, archivados con convención canónica; notificación al RevisorFiscal y al Contador Titular.
### Test 2 — (excepción) Al compilar, las partidas listadas suman $14,2M pero la diferencia entre extracto y libros es $15,4M
**Output:** firma RETENIDA; regeneración contra el inventario detecta una comisión de $1,2M tipificada en la conciliación pero ausente del listado; corrección, verificación de consistencia interna en $0 y firma; si la diferencia hubiera venido de la conciliación misma, esta se habría reabierto antes de emitir.

═══════════════════════════════════════════════════════════════════════

## Relacionado
- *MOC - Agentes RITORE*
- *Proyecto - Ecosistema RITORE*
- [[00 - Estandar de Agentes RITORE]]
- [[Skills Compartidas RITORE]]
- *01-Orquestador-Master*
- [[02-AuxiliarContable-Senior]]
- [[05-AuxiliarCarteraCxP-Senior]]
- [[06-AuxiliarTesoreria-Senior]]
- *19-RevisorFiscal-Senior*
- *20-SAGRLAFT-Senior*
- *22-AtencionCliente-Senior*
- *26-NotionArquitecto-DevOps-Senior*

## Historial de versiones
| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-05-19 | Versión inicial consolidada (10 skills) | RITORE |
| 2.0 | 2026-06-11 | Refactorización según Estandar de Agentes v1.0: 10 → 8 skills (parseadores OFX/MT940 + PDF consolidados en `interpretar-extracto-bancario` con variantes; detección + escalamiento SAGRLAFT unificados, protocolo heredado de Skills Compartidas); eliminación de auto-correcciones clonadas; umbrales numéricos §3 + umbrales propios de antigüedad de partidas (30/60/90 días) justificados; Inputs/Outputs, manejo de errores, métricas y tests propios en todas las skills | RITORE |
