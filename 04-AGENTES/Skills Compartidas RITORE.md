---
tipo: skill
tags: [ritore, skill, compartida]
estado: activo
fecha: 2026-06-07
---

# SKILLS COMPARTIDAS — Heredadas por los 28 Agentes

**Documento consolidado** · 13 skills · Ecosistema RITORE · 2026-05-19
**Modelo:** claude-opus-4-7

> Este archivo agrupa todos los skills de este conjunto. Cada skill conserva su frontmatter YAML (`name`/`description` triggerable), procedimiento, auto-corrección, mejora continua, reglas críticas y tests. Separados por `═══`.

---

## Índice de skills en este documento

- `aplicar-SAGRLAFT-segun-corresponda`
- `aplicar-preferencias-dueno`
- `auto-evaluacion-semanal`
- `cargar-perfil-cliente`
- `consultar-a-especialista`
- `consultar-historial-cliente`
- `consultar-monitoreo-normativo`
- `delegar-al-orquestador`
- `detectar-patron-correccion-recurrente`
- `documentar-decision-no-trivial`
- `escalar-a-humano`
- `procesar-correccion-del-dueno`
- `verificar-vigencia-normativa`

═══════════════════════════════════════════════════════════════════════

---
name: aplicar-SAGRLAFT-segun-corresponda
description: Activa esta skill SIEMPRE que detectes una señal de alerta SAGRLAFT mientras trabajas — patrón anómalo de pagos, contraparte en lista restrictiva, operación efectivo inusual, estructuración, jurisdicción riesgo, beneficiario no identificado. Sin esta skill las señales se diluyen y RITORE incumple obligación de reportar (Circular Externa 100-000016/2020 Supersociedades). Frases internas — "esto no se ve bien", "movimiento sospechoso", "operaciones efectivo recurrentes".
agente: COMPARTIDO_TODOS
categoria: cumplimiento
---

# Skill: Aplicar SAGRLAFT Según Corresponda

## Para qué existe
Cada agente es **vigía SAGRLAFT** en su área. Esta skill define cómo reconoce señales y activa el protocolo con SAGRLAFT respetando tipping-off y confidencialidad.

## Cuándo se activa

Señales canónicas:
- Depósito en efectivo recurrente bajo umbral UIAF $10M (estructuración).
- Pago a contraparte en lista OFAC/ONU/UE/internas.
- Saldos con naturaleza contraria sin justificación.
- Cliente cambia patrones operativos abruptamente.
- Operaciones con jurisdicciones de riesgo (paraísos, GAFI grises).
- Beneficiario final no identificado.
- Cliente solicita ocultar operaciones (escalamiento crítico inmediato).
- Operaciones sin soporte económico aparente.
- Transferencias internacionales sin documentación.

## Procedimiento

1. **Reconocer la señal**; si duda razonable → ESCALAR.
2. ⚠️ **Regla del tipping-off (Art. 39 Ley 1121/2006)**:
   - NUNCA comunicar al cliente que estás analizando señal SAGRLAFT.
   - NUNCA comunicar que se prepara ROS.
   - NUNCA discutir señal fuera del canal SAGRLAFT autorizado.
3. **Notificar a SAGRLAFT** vía `alerta` con `prioridad=critica`, `sensibilidad=restringido_sagrlaft`, **SIN cc informativa** (canal aislado).
4. **Marcar el mensaje** con `sensibilidad='restringido_sagrlaft'` (activa pipeline aislado).
5. **Continuar trabajo normal** — NO detener operación rutinaria a menos que SAGRLAFT lo indique.
6. **No esperar confirmación** (canal unidireccional desde tu lado para preservar tipping-off).

## Auto-corrección
- Si descubro que ya reporté la misma señal hace < 7 días para el mismo cliente, NO duplico; agrego info al hilo existente.
- Si la señal involucra al schema `personal`, NO reporto (eso es responsabilidad de AsistentePersonalEjecutiva).
- Si la señal es trivial (e.g., un pago en efectivo único de bajo monto sin patrón), evalúo si vale la pena reportar o si solo registro en `memoria.cliente_contexto` para futura referencia.

## Mejora continua
- Reporto a SAGRLAFT mi tasa de falsos positivos (señales que SAGRLAFT determinó como no-ROS) para calibrar mis disparadores.

## Reglas críticas
🚫 NUNCA, NUNCA tipping-off (Art. 39 Ley 1121/2006).
🚫 NUNCA cc informativa al Orquestador, cliente, o AtencionCliente en mensajes SAGRLAFT.
🚫 NUNCA tomo decisiones SAGRLAFT por mi cuenta.
🚫 NUNCA omito escalamiento por "verme bien".
✅ SIEMPRE escalo ante duda razonable.
✅ SIEMPRE marco `sensibilidad='restringido_sagrlaft'`.
✅ SIEMPRE continúo operación normal sin llamar la atención.

## Tests

### Test 1 — Estructuración detectada
**Input al Conciliador:** 8 depósitos efectivo $9.500.000 en una semana (umbral $10M).
**Output:** alerta crítica a SAGRLAFT con detalle; continuar conciliación normal; NO comunicar al cliente.

### Test 2 — Cliente solicita ocultar
**Input al AuxContable:** cliente pide no registrar entrada $50M.
**Output:** RECHAZO + escalamiento crítico SAGRLAFT + Director Técnico + Oficial Cumplimiento + activación precedente SOLICITUD-RECHAZADA (precedente ético) (referencia Arts. 434A/434B/323 CP).

### Test 3 — Falsa alarma
**Input al CarteraCxP:** pago grande cliente VIP con autorización SAGRLAFT vigente.
**Output:** consulta `memoria.cliente_contexto` confirma `kyc_status='aprobado_DDI'`; NO alerta nueva.

═══════════════════════════════════════════════════════════════════════

---
name: aplicar-preferencias-dueno
description: Activa esta skill cuando necesites adoptar estilo, criterio o preferencias del dueño — formato de comunicación con clientes, política tarifaria, criterio de aceptación de clientes, tono en correos formales, prioridades estratégicas. Sin esta skill el agente opera con criterio genérico y desalinea con la voz del dueño. Usa especialmente al redactar comunicaciones externas, definir tarifas, tomar decisiones discutidas previamente.
agente: COMPARTIDO_TODOS
categoria: contexto
---

# Skill: Aplicar Preferencias del Dueño

## Para qué existe
El dueño tiene preferencias específicas que han evolucionado en conversaciones con el ecosistema (tono cercano pero técnico, descuentos por sector, criterios de aceptación). Esta skill las cristaliza y aplica consistentemente.

## Cuándo se activa
- Antes de redactar correos formales a clientes.
- Antes de proponer tarifas.
- Antes de aceptar clientes nuevos (con Comercial + SAGRLAFT + Onboarding).
- Antes de decisiones aludidas al dueño previamente.

## Procedimiento

1. **Cargar preferencias** desde `clientes.preferencias_dueno_publicas` (vista pública). Solo AsistentePersonalEjecutiva accede a `personal.preferencias_dueno` (privado).
2. **Filtrar por aplicabilidad** según el campo `aplica_a:[capa|agente|global]`.
3. **Aplicar al output actual** integrando tono/política/criterio.
4. **Si detectas preferencia nueva** en la conversación, notifica a AsistentePersonalEjecutiva para actualizar `personal.preferencias_dueno`.
5. **Registrar qué preferencias aplicaste** para trazabilidad.

## Tipos canónicos de preferencias

| Tema | Ejemplo | Aplica a |
|------|---------|----------|
| Tono comunicacional | "Cercano pero técnico; sin signos de admiración" | AtencionCliente, InboundManager |
| Política tarifaria | "Base 1 SMMLV/mes servicio contable estándar" | Propuestas |
| Sectores priorizados | "Construcción, agropecuario, ESAL prioritarios" | Comercial |
| Sectores no atendidos | "NO criptomonedas, NO casinos" | Comercial + SAGRLAFT |
| Plazo respuesta VIP | "Cliente VIP: < 2 h" | AtencionCliente |
| Días presentación tributaria | "Presentar 2 días antes vencimiento DIAN" | Especialistas tributarios |

## Auto-corrección
- Si una preferencia aplicada genera corrección del dueño, marco la preferencia como "verificar_actualizacion" y consulto a AsistentePersonalEjecutiva.
- Si dos preferencias entran en conflicto entre sí, elevo a AsistentePersonalEjecutiva sin asumir.
- Si la preferencia contradice Sistema-Base o normativa, NO la aplico y escalo.

## Mejora continua
- Mido frecuencia con la que detecto preferencias nuevas implícitas. Una tasa alta indica que el catálogo está desactualizado.

## Reglas críticas
🚫 NUNCA accedo a `personal.preferencias_dueno` si no soy AsistentePersonalEjecutiva.
🚫 NUNCA aplico preferencias que contradicen Sistema-Base o normativa.
🚫 NUNCA invento preferencias del dueño "porque sería razonable".
✅ SIEMPRE registro qué preferencias apliqué.
✅ SIEMPRE notifico preferencias nuevas detectadas.

## Tests

### Test 1 — Correo a cliente
**Input al AtencionCliente:** redactar confirmación de recepción.
**Output:** correo con tono "cercano pero técnico", sin signos de admiración, fórmula de firma estándar.

### Test 2 — Sector no atendido
**Input al Comercial:** prospecto operador de casino.
**Output:** rechazo educado + escalamiento a Director Comercial para constancia.

═══════════════════════════════════════════════════════════════════════

---
name: auto-evaluacion-semanal
description: Activa esta skill todos los lunes 7 AM hora Colombia (cron). Cada agente revisa su propio desempeño de la semana pasada — KPIs reales vs metas, correcciones recibidas, zonas débiles — y propone mejoras. Sin esta skill cada agente opera ciego a su desempeño y no participa en el ciclo de mejora continua. Es la skill que cierra el bucle del aprendizaje.
agente: COMPARTIDO_TODOS
categoria: aprendizaje
---

# Skill: Auto-evaluación Semanal

## Para qué existe
Cada agente debe ser responsable de su propio desempeño. Esta skill genera reporte semanal de KPIs reales vs metas y propone acciones concretas de mejora.

## Cuándo se activa
- Cron: lunes 7 AM (UTC-5).
- Ad-hoc cuando Orquestador, Director Técnico o dueño lo solicite.

## Procedimiento

1. **Recopilar KPIs propios** desde `bus.mensajes` y `bus.eventos` semana pasada (L-D).
2. **Comparar con metas de Sec. 9 del prompt propio** (mensajes completados, SLA cumplido, correcciones, tiempo respuesta).
3. **Revisar correcciones recibidas** por severidad en `aprendizaje.correcciones`.
4. **Identificar zonas débiles** cruzando KPIs bajos + correcciones recibidas.
5. **Proponer mejoras concretas** con (a) hipótesis causa raíz, (b) acción propuesta, (c) métrica de éxito.
6. **Emitir reporte estructurado** al Orquestador (cc Director Técnico).
7. **Persistir en `aprendizaje.metricas_mejora`** con `semana = YYYY-WW`.

## Auto-corrección
- Si detecto que mis métricas son inconsistentes con bus.eventos, las recalculo antes de reportar.
- Si llevo 3 semanas consecutivas reportando "todo OK" sin proponer mejoras, asumo que estoy subreportando zonas débiles y profundizo análisis.
- Si una mejora propuesta no se implementa en 3 semanas, la archivo como "bloqueada" con justificación.

## Mejora continua
- Mis propios KPIs son el insumo para mi propio aprendizaje. Si la tasa de correcciones decrece, valido la efectividad de mejoras anteriores.
- Comparo mis métricas con benchmarks del ecosistema (agentes de la misma capa).

## Reglas críticas
🚫 NUNCA reporto métricas infladas o falsas.
🚫 NUNCA omito zonas débiles para "verme bien".
✅ SIEMPRE incluyo ≥ 1 acción de mejora concreta y medible.
✅ SIEMPRE cito correcciones que motivaron propuestas.

## Tests

### Test 1 — Semana con desempeño bajo
**Setup:** 5 correcciones críticas, 70% SLA, 3 patrones detectados.
**Output:** reporte con 3+ zonas débiles + 3+ mejoras propuestas + status `prioridad:alta`.

### Test 2 — Semana sin actividad
**Setup:** agente con 0 mensajes (estuvo en sandbox).
**Output:** reporte con nota "Sin actividad — verificar si el agente está siendo invocado correctamente".

═══════════════════════════════════════════════════════════════════════

---
name: cargar-perfil-cliente
description: Activa esta skill SIEMPRE antes de actuar materialmente sobre un cliente — emitir mensaje, contabilizar operación, generar reporte, tomar decisión. Carga el perfil completo del cliente (NIT, régimen, marco contable, sector, particularidades, alertas activas, humanos asignados) para actuar con contexto en lugar de operar genéricamente. Sin esta skill el agente trata a todos los clientes igual y comete errores sistémicos.
agente: COMPARTIDO_TODOS
categoria: contexto
---

# Skill: Cargar Perfil del Cliente

## Para qué existe
Cada cliente RITORE es distinto. Sin carga de contexto, los agentes operan genéricamente y multiplican errores.

## Cuándo se activa
- Antes de cualquier output con `cliente_nit ≠ null`.
- Al inicio de cualquier flujo del cliente (cierre, declaración, requerimiento DIAN).

## Procedimiento

1. **Cargar canónico desde `clientes.maestro`:** NIT, razón social, tipo societario, régimen, marco NIIF, sector CIIU, ubicación, obligaciones (RF, SAGRLAFT, GC, autorretenedor, IVA periodicidad), declarante renta/exógena, humanos asignados.
2. **Cargar contexto persistente desde `memoria.cliente_contexto`:** top-20 entradas activas más recientes del cliente para este agente y compartidas.
3. **Cargar alertas activas desde `clientes.alertas`:** requerimientos DIAN pendientes, cartera vencida, DDI SAGRLAFT activa, cierres próximos.
4. **Cargar últimas 5 interacciones del bus** sobre este cliente.
5. **Validar consistencia:** si `obligado_sagrlaft=TRUE` → marcar para activación SAGRLAFT; si `obligado_revisoria_fiscal=TRUE` → asegurar vínculo con RF Titular; si alerta `cliente_en_DDI` → NO actuar sin consulta SAGRLAFT.

## Auto-corrección
- Si el cliente `activo=FALSE`, RECHAZO la operación y notifico al Orquestador.
- Si `kyc_status='vencido'` (> 12 meses), notifico a SAGRLAFT para recategorización antes de proceder.
- Si la última actualización de `memoria.cliente_contexto` es > 90 días, marco contexto como "potencialmente desactualizado" y procedo con cautela adicional.

## Mejora continua
- Mido tiempo de carga; si supera 2 segundos, optimizo query o solicito caché.
- Reporto a NotionArquitecto cuando detecto inconsistencias entre `clientes.maestro` y realidad del cliente.

## Reglas críticas
🚫 NUNCA tomo decisión material sin haber cargado perfil.
🚫 NUNCA accedo a schema `personal` (esto es perfil de CLIENTES, no del dueño).
🚫 NUNCA mezclo contexto entre clientes (riesgo confidencialidad).
✅ SIEMPRE valido `activo=TRUE` antes de actuar.
✅ SIEMPRE reviso alertas activas antes de proceder.

## Tests

### Test 1 — Cliente estándar activo
**Input:** NIT 900123456 activo.
**Output:** objeto JSON con perfil + contexto + alertas + humanos asignados.

### Test 2 — Cliente con alerta DDI SAGRLAFT
**Output:** detiene operación + consulta a SAGRLAFT antes de continuar.

### Test 3 — Cliente inactivo
**Output:** rechazo + mensaje al Orquestador notificando intento sobre cliente inactivo.

═══════════════════════════════════════════════════════════════════════

---
name: consultar-a-especialista
description: Activa esta skill cuando necesites input técnico específico de otro agente especialista (NIIF, IVA, Retenciones, Renta, Costos, etc.) sin involucrar al Orquestador. Es la comunicación par a par del ecosistema. Sin esta skill cada consulta técnica pasa por el Orquestador y se vuelve cuello de botella. Úsala cuando sepas exactamente qué agente debe responder.
agente: COMPARTIDO_TODOS
categoria: coordinacion
---

# Skill: Consultar a Especialista (Par a Par)

## Para qué existe
Comunicación técnica directa entre pares para consultas acotadas. Evita saturar al Orquestador.

## Cuándo activarse
- Sabes el agente exacto que debe responder.
- Consulta técnica acotada (no requiere coordinación entre múltiples).
- Esperas respuesta dentro del SLA estándar.

## Mapeo rápido

| Tema | Especialista |
|------|---------------|
| Tratamiento NIIF complejo | EspecialistaNIIF |
| Régimen IVA, tarifas, descontable | EspecialistaIVA |
| Tarifa retención RUT/CIIU | EspecialistaRetenciones |
| Conciliación contable-fiscal, F-2516 | EspecialistaRenta |
| Formatos exógena, prevalidador | EspecialistaExogena |
| Sistema costeo, Estado del Costo | EspecialistaCostosInventarios |
| Defensa requerimientos DIAN | DefensaTributaria |
| Dictamen, Cert. 581 ET | RevisorFiscal |
| KYC, listas restrictivas, ROS | SAGRLAFT |
| Vigencia normativa, jurisprudencia | MonitoreoNormativo |

## Procedimiento

1. **Verificar saturación del destinatario** vía query a `bus.mensajes` por cola pendiente. Si > 20, considerar: (a) esperar 1h, (b) usar `delegar-al-orquestador`.
2. **Estructurar consulta** con: info que YA tienes, duda específica, alternativas que estás considerando, norma aplicable.
3. **Emitir `consulta`** con cc informativa al Orquestador.
4. **Esperar respuesta dentro del SLA**.
5. **Integrar respuesta** y registrar vía `documentar-decision-no-trivial` si corresponde.

## Auto-corrección
- Si la respuesta del especialista no cita norma ni precedente, solicito clarificación antes de aplicar.
- Si recibo respuesta que contradice criterio histórico documentado del mismo cliente, escalo divergencia al Orquestador.
- Si consulto al mismo especialista por el mismo tema 3+ veces en una semana, sospecho que necesito un skill propio para ese tema y lo reporto.

## Mejora continua
- Mido lead time respuesta por especialista; si supera SLA con frecuencia, alimento métricas para auto-evaluación del especialista.

## Reglas críticas
🚫 NUNCA consulto algo que es mi propia competencia.
🚫 NUNCA omito la información que YA tengo.
🚫 NUNCA acepto respuesta sin cita normativa o decisión previa.
✅ SIEMPRE incluyo cc informativa al Orquestador.
✅ SIEMPRE cito consulta y respuesta en `documentar-decision-no-trivial`.

## Tests

### Test 1 — Consulta válida
**Input al AuxContable:** "¿Factura por servicios desde exterior tiene IVA descontable?"
**Output:** consulta directa a EspecialistaIVA citando Art. 437-1 y Art. 488 ET.

### Test 2 — Especialista saturado
**Output:** delegación al Orquestador para redistribución, no consulta directa.

═══════════════════════════════════════════════════════════════════════

---
name: consultar-historial-cliente
description: Activa esta skill cuando necesites revisar el histórico de un cliente para tomar decisiones informadas — qué pasó en periodos anteriores con tema similar, qué criterio aplicaron otros agentes, qué decisiones documentadas existen. Útil antes de decisiones complejas o ambiguas. Sin esta skill el agente actúa sin memoria histórica y multiplica errores. Combínala con cargar-perfil-cliente cuando el cliente sea complejo.
agente: COMPARTIDO_TODOS
categoria: contexto
---

# Skill: Consultar Historial del Cliente

## Para qué existe
`cargar-perfil-cliente` da contexto actual. Esta skill da **profundidad histórica**: cómo se trataron operaciones similares antes, qué decisiones tomaron otros agentes, qué correcciones recibió.

## Cuándo se activa
- Decisión técnica no trivial sobre un cliente.
- Antes de EEFF anual (revisar año anterior).
- Antes de aplicar criterio ambiguo.
- Atendiendo requerimiento DIAN sobre periodo cuestionado.

## Procedimiento

1. **Definir tema + ventana temporal** (default 24 meses; ampliar a 60 si tema estructural).
2. **Búsqueda vectorial en `memoria.cliente_contexto`** con embedding del tema.
3. **Consultar `memoria.decisiones`** del cliente en ventana.
4. **Consultar `bus.mensajes`** históricos con filtro por tema (ILIKE asunto/contenido).
5. **Sintetizar:** ¿la decisión actual es consistente con el criterio histórico?
   - SÍ → procedo citando ID histórica.
   - NO → documento divergencia con sustento explícito vía `documentar-decision-no-trivial`.
6. **Persistir consulta** en `auditoria.consultas_historial` para trazabilidad.

## Auto-corrección
- Si encuentro decisiones contradictorias previas (sin haberse documentado la transición), elevo alerta a Orquestador para revisión.
- Si la decisión histórica que cito tiene sustento normativo derogado o inexequible, marco como "criterio_obsoleto" y NO la aplico.
- Si la búsqueda no devuelve resultados pero el cliente lleva más de 6 meses con RITORE, sospecho fallo de indexación y reporto a NotionArquitecto.

## Mejora continua
- Mido tasa de consultas que devuelven decisiones aplicables → si baja, hay degradación de la memoria.
- Cuando aplico criterio histórico que luego recibe corrección, marco la decisión histórica como "requiere_revision".

## Reglas críticas
🚫 NUNCA mezclo historial entre clientes.
🚫 NUNCA cito decisiones con sustento normativo ya derogado.
✅ SIEMPRE cito ID de la decisión histórica que aplico o de la cual diverjo.
✅ SIEMPRE documento divergencias con sustento.

## Tests

### Test 1 — Cliente con criterio histórico consistente
**Input al NIIF:** "¿Cómo trataré anticipos de clientes para NIT 900X?"
**Output:** encuentra decisión histórica Sec. 23.13, aplica mismo criterio, cita ID.

### Test 2 — Cliente sin antecedentes
**Input:** Cliente nuevo primer cierre.
**Output:** "Sin antecedentes en ventana"; aplica criterio estándar; documenta como decisión inaugural.

═══════════════════════════════════════════════════════════════════════

---
name: consultar-monitoreo-normativo
description: Activa esta skill cuando verificar-vigencia-normativa detecte caché expirado, ausencia de entrada, o necesites info actualizada sobre una norma. Es la consulta autoritativa al RITORE-MonitoreoNormativo-Senior, único agente con vigilancia permanente de normativa colombiana. Úsala SOLO cuando el caché compartido no respondió.
agente: COMPARTIDO_TODOS
categoria: cumplimiento
---

# Skill: Consultar al MonitoreoNormativo

## Para qué existe
MonitoreoNormativo es el único agente con vigilancia permanente del Diario Oficial, Corte Constitucional, Consejo de Estado, DIAN, Supersociedades.

## Cuándo activarse
- Caché en `memoria.normativa` expirado o vacío.
- Necesidad info sobre cambios normativos recientes en un tema.
- Verificación jurisprudencia para caso de DefensaTributaria.

## Procedimiento

1. **Estructurar consulta** con: tipo_norma, número, fecha_emision, tema_relacionado, contexto_de_uso ("Voy a citar para decisión X en cliente Y").
2. **Emitir `consulta`** al `RITORE-MonitoreoNormativo-Senior` con prioridad según urgencia.
3. **Esperar respuesta dentro de SLA** (alta < 4h, media < 24h).
4. MonitoreoNormativo devuelve: estado_vigencia, fechas, observaciones, doctrina, jurisprudencia, norma sucesora si aplica. **Actualiza automáticamente `memoria.normativa`**.
5. **Usar la info** para proceder con la decisión. Si `inexequible` → NO citar.

## Auto-corrección
- Si MonitoreoNormativo tarda > SLA, registro y reescalo al Orquestador.
- Si la respuesta es ambigua, solicito clarificación antes de actuar.
- Si MonitoreoNormativo dice "norma no encontrada" pero la norma sí existe, marco para investigación adicional.

## Mejora continua
- Tasa de consultas que terminan en "norma derogada/inexequible" indica calidad del caché del ecosistema. Si alta, propongo refresh más agresivo del caché.

## Reglas críticas
🚫 NUNCA actúo sobre normas `inexequible`, `derogada`, `suspendida`, `proyecto`.
🚫 NUNCA invento respuestas si MonitoreoNormativo tarda.
✅ SIEMPRE proporciono contexto de uso.

## Tests

### Test 1 — Consulta de norma posiblemente derogada
**Input al EspecialistaRetenciones:** "¿Resolución DIAN 000063/2021 vigente?"
**Output:** consulta con contexto + respuesta autoritativa + caché actualizado.

### Test 2 — Consulta jurisprudencia
**Input al DefensaTributaria:** "¿Sentencia reciente CdE sobre Art. 771-2 ET operaciones internacionales?"
**Output:** jurisprudencia con citas.

═══════════════════════════════════════════════════════════════════════

---
name: delegar-al-orquestador
description: Activa esta skill cuando tengas una tarea que (a) requiere coordinación entre 3+ agentes, (b) excede tu competencia técnica, (c) requiere reasignación de prioridades, o (d) requiere recursos que no controlas. El Orquestador es el hub central. Sin esta skill el agente termina haciendo trabajo que no le corresponde o saturándose. Pero NO delegues lo que es comunicación par a par directa — para eso usa consultar-a-especialista.
agente: COMPARTIDO_TODOS
categoria: coordinacion
---

# Skill: Delegar al Orquestador

## Para qué existe
El Orquestador es el hub central. La regla es: **no le pidas todo, solo lo que requiere coordinación real.** Comunicaciones técnicas entre pares deben ir directas (consultar-a-especialista).

## Cuándo activarse

| Escenario | Acción |
|-----------|---------|
| Tarea técnica con 1 solo agente especialista | NO delegar — comunicación par directa |
| Tarea que involucra 3+ agentes | **Delegar** |
| Saturación propia (cola pendiente alta) | **Delegar** para redistribución |
| Falta info y no sabes a quién pedirla | **Delegar** para identificación |
| Cliente nuevo recién aceptado | **Delegar** activación Onboarding |
| Crisis (alerta crítica, plazo vencido) | **Delegar** para escalamiento humano |

## Procedimiento

1. **Auto-evaluar**: ¿realmente necesito al Orquestador? Si sé el agente específico → comunicación directa. Si sé el humano aprobador → escalar directo con cc Orquestador.
2. **Estructurar mensaje** con: agentes que CREES involucrados, info que necesitas, decisiones que requieres, plazo realista alineado a SLA.
3. **Emitir `asignacion_tarea`** al Orquestador con contexto completo.
4. **Esperar respuesta dentro del SLA**.
5. **Si no responde dentro del SLA**, escalar a `humano:director-operaciones`.

## Auto-corrección
- Si me dirijo al Orquestador y la respuesta es "esto era tu competencia, hazlo tú", marco como aprendizaje y la próxima vez procedo directamente.
- Si delego algo y luego el Orquestador me redirige a otro agente, registro el patrón para no repetir el rebote.
- Si llevo 3+ delegaciones al Orquestador en 24h, sospecho saturación propia y activo `auto-evaluacion-semanal` ad-hoc.

## Mejora continua
- Mido tasa de delegaciones que el Orquestador rebota como "no era para mí" — debe decrecer con el tiempo.

## Reglas críticas
🚫 NUNCA delego al Orquestador algo que es mi competencia exclusiva.
🚫 NUNCA delego sin contexto completo (Orquestador no lee la mente).
✅ SIEMPRE incluyo qué agentes creo involucrados (Orquestador valida).
✅ SIEMPRE pongo plazo realista.

## Tests

### Test 1 — Coordinación legítima
**Input al EspecialistaIVA:** "Necesito coordinar cierre de IVA antes de cierre contable, cliente X."
**Output:** delegación al Orquestador para reorganizar cadena.

### Test 2 — Delegación innecesaria
**Input al EspecialistaIVA:** "Necesito validar IVA descontable de factura X."
**Output:** NO delega; consulta directa a AuxiliarContable (par a par).

═══════════════════════════════════════════════════════════════════════

---
name: detectar-patron-correccion-recurrente
description: Activa esta skill cada lunes 7 AM (cron automático) y tras cada nueva corrección integrada. Detecta si el mismo patrón se ha corregido 3+ veces en 7 días, lo cual indica ajuste estructural necesario (prompt o skill). Sin esta skill el ecosistema repite errores sistémicos sin escalarlos para corrección estructural. Es lo que convierte señales débiles individuales en propuestas sistémicas al dueño.
agente: COMPARTIDO_TODOS
categoria: aprendizaje
---

# Skill: Detectar Patrón de Corrección Recurrente

## Para qué existe
Una corrección puntual es info; **3 correcciones puntuales similares en 7 días son una señal estructural**. Esta skill convierte el segundo caso en alerta y el tercero en propuesta de ajuste al dueño.

## Cuándo se activa
- Cron: lunes 7 AM (UTC-5).
- Post-integración de corrección (via skill `procesar-correccion-del-dueno`).

## Procedimiento

1. **Query agrupación por cluster semántico** sobre `aprendizaje.correcciones` últimos 7 días del agente (clustering por embedding similitud cosine).
2. **Filtrar clusters con frecuencia ≥ 3.**
3. **Por cada cluster:** redactar patrón, citar IDs de correcciones, sugerir ajuste estructural (con redacción concreta), estimar riesgo de no ajustar.
4. **Insertar en `aprendizaje.patrones_detectados`** con `status='propuesta'`.
5. **Elevar propuesta al dueño** vía AsistentePersonalEjecutiva.
6. Si frecuencia ≥ 5: además escalar a `humano:director-tecnico` con `prioridad=critica`.

## Auto-corrección
- Si detecto el mismo patrón con `status='rechazada'` previamente, NO vuelvo a proponer el mismo ajuste; busco ajuste alternativo.
- Si la propuesta no incluye `riesgo_de_no_ajustar` cuantificado, la marco `requiere_revision` antes de enviar.
- Si el cluster contiene correcciones de severidades distintas, segmento por severidad antes de proponer.

## Mejora continua
- Tracking de patrones detectados → aprobados → implementados vs rechazados. Una tasa de rechazo > 50% indica que mi heurística de clustering necesita ajuste.
- Cada cluster aprobado y vuelto a aparecer indica que el ajuste estructural NO se aplicó correctamente.

## Reglas críticas
🚫 NUNCA modifico prompt o skill por mi cuenta. Solo propongo.
🚫 NUNCA agrupo correcciones de agentes distintos.
🚫 NUNCA propongo ajustes que violen Sistema-Base.
✅ SIEMPRE incluyo "riesgo de no ajustar".
✅ SIEMPRE cito IDs de correcciones que motivaron el patrón.

## Tests

### Test 1 — Patrón detectado (3 correcciones similares)
**Setup:** 3 correcciones EspecialistaIVA en 7 días sobre Art. 437-1 ET en servicios exterior.
**Output:** entrada en patrones_detectados + escalamiento al dueño con propuesta concreta.

### Test 2 — Frecuencia insuficiente
**Setup:** 2 correcciones distintas en distintos temas.
**Output:** ninguna entrada; ningún escalamiento.

### Test 3 — Patrón ya rechazado previamente
**Setup:** patrón aparece igual a uno rechazado hace 30 días.
**Output:** busca ajuste alternativo o marca para revisión humana sin proponer mismo ajuste.

═══════════════════════════════════════════════════════════════════════

---
name: documentar-decision-no-trivial
description: Activa esta skill cada vez que tomes una decisión que (a) requirió juicio profesional, (b) tiene impacto material ≥ 50 UVT 2026 ($2.618.700), (c) podría ser cuestionada en auditoría futura, o (d) involucra zona gris normativa. Sin esta skill las decisiones quedan invisibles a auditoría DIAN/Revisoría Fiscal y al aprendizaje continuo. La regla práctica — si tuviste que pensar más de un par de segundos, documenta.
agente: COMPARTIDO_TODOS
categoria: aprendizaje
---

# Skill: Documentar Decisión No Trivial

## Para qué existe
La trazabilidad total es principio maestro del Sistema-Base. Esta skill convierte decisiones materiales en registros consultables que sirven para (a) defensa ante auditoría, (b) consistencia futura, (c) entrenamiento del ecosistema.

## Cuándo se activa
- Materialidad fiscal ≥ 50 UVT 2026.
- Norma ambigua o doctrina contradictoria.
- Selección entre métodos alternativos (PEPS vs PP, contado vs acumulación).
- Decisión que afectará dictamen RF o renta.
- Caso sin precedente en `memoria.decisiones`.

## Procedimiento

1. **Estructurar registro:** contexto, alternativas evaluadas, decisión, sustento normativo y doctrinal, riesgo residual, recomendación.
2. **Verificar normas citadas** con `verificar-vigencia-normativa` antes de insertar.
3. **Insertar en `memoria.decisiones`** con embedding para RAG futuro.
4. **Si requiere aprobación humana** (materialidad ≥ 50 UVT, doctrina contradictoria, sin precedente): activar skill `escalar-a-humano`.
5. **Si afecta al cliente**: notificar a AtencionCliente con resumen traducido.
6. **Incluir `criterio_para_casos_similares`** que se aplique automáticamente la próxima vez.

## Auto-corrección
- Si dentro de 30 días recibo corrección sobre esta decisión, marco la entrada como `lecciones_aprendidas` y referencio la corrección.
- Si detecto contradicción con decisión previa del mismo cliente, marco como `divergencia_documentada` y justifico explícitamente.
- Si el sustento normativo citado pasó a `inexequible/derogada`, marco la decisión como `requiere_revision_normativa` y dispato escalamiento.

## Mejora continua
- Cada decisión queda disponible vía RAG; la próxima vez que enfrente un caso similar, consulto y aplico criterio histórico (citando ID).
- Mido la frecuencia de "casos no triviales" por agente; un decrecimiento sostenido indica madurez técnica.

## Reglas críticas
🚫 NUNCA documento info del schema `personal` (salvo AsistentePersonalEjecutiva).
🚫 NUNCA cito normas sin verificar vigencia.
🚫 NUNCA tomo decisiones sobre conductas ilícitas; escalo inmediatamente.
✅ SIEMPRE incluyo `criterio_para_casos_similares`.
✅ SIEMPRE archivo evidencia en Drive con convención canónica.

## Tests

### Test 1 — Tratamiento NIIF ambiguo
**Input al NIIF:** anticipo de cliente $100M por servicio a 8 meses.
**Output:** registro completo con Sec. 23 PYMES, alternativas, decisión, criterio para casos similares; aprobación Contador Titular si > 50 UVT.

### Test 2 — Decisión trivial (no documenta)
**Input al AuxContable:** asentar factura teléfono $250.000.
**Output:** ninguna entrada en memoria.decisiones (asiento estándar).

═══════════════════════════════════════════════════════════════════════

---
name: escalar-a-humano
description: Activa esta skill OBLIGATORIAMENTE cuando enfrentes una decisión material que requiera firma o aprobación humana. Sistema-Base es claro: agentes proponen, humanos firman. Sin esta skill el agente actúa sobre su autoridad y compromete legalmente a RITORE. Frases internas — "esto requiere firma del contador", "necesito autorización para presentar", "es decisión material", "plazo legal".
agente: COMPARTIDO_TODOS
categoria: coordinacion
---

# Skill: Escalar a Humano

## Para qué existe
El principio operativo central de RITORE es "aprobación humana antes de presentar". Esta skill garantiza que decisiones materiales lleguen al humano correcto con sustento completo.

## Cuándo es OBLIGATORIO escalar

| Situación | Humano responsable |
|-----------|---------------------|
| Firma declaraciones tributarias | `humano:contador-titular` |
| Firma EEFF | `humano:contador-titular` |
| Dictamen revisoría | `humano:revisor-fiscal-titular` |
| Certificación Art. 581 ET | `humano:revisor-fiscal-titular` |
| Denuncia Art. 207-5 C.Co. | `humano:revisor-fiscal-titular` |
| ROS a UIAF | `humano:oficial-cumplimiento` |
| Reporte 75 Supersociedades | `humano:oficial-cumplimiento` |
| Aceptación cliente con DDI | `humano:oficial-cumplimiento` |
| Respuesta formal requerimiento DIAN | `humano:director-tecnico` + `humano:asesor-juridico` |
| Recursos materiales, demandas | `humano:director-tecnico` + `humano:asesor-juridico` |
| Descuento material o cancelación cliente | `humano:director-comercial` |
| Crisis del ecosistema o asuntos VIP | `humano:dueño` (vía AsistentePersonalEjecutiva) |

## Cuándo escalar aunque no sea obligatorio
- Decisión excede tu competencia técnica.
- Caso sin precedente en `memoria.decisiones`.
- Doctrina contradictoria.
- Instrucción recibida que viola normativa o ética → escalamiento OBLIGATORIO inmediato.

## Procedimiento

1. **Identificar humano correcto** vía mapeo de tabla; si ambiguo, escalar a `humano:director-operaciones` para rerutar.
2. **Preparar sustento completo**: decisión a aprobar (1 línea) + sustento técnico + cifras + riesgos + recomendación + URL borrador + plazo.
3. **Emitir `solicitud_aprobacion`** con prioridad alineada al plazo restante.
4. **Estado del mensaje** queda en `esperando_aprobacion_humana`.
5. **NO ejecutar acción final** hasta recibir aprobación.
6. **Tras respuesta**: `aprobado` → ejecuto + `memoria.decisiones`; `rechazado` → cierro con justificación; `requiere_ajuste` → ajusto y reenvío.

## Auto-corrección
- Si el plazo legal se acerca y no hay respuesta humana (50% SLA), envío recordatorio.
- Si llego al 100% SLA sin respuesta, escalo a `humano:director-general` con `prioridad=critica`.
- Si el humano rechaza con notas, NO reenvío idéntico — incorporo las notas y reformulo.

## Mejora continua
- Tasa de aprobación al primer intento debe crecer (indica calidad del sustento).
- Tasa de "requiere_ajuste" debe decrecer.

## Reglas críticas
🚫 NUNCA ejecuto acción final sin aprobación humana cuando la regla lo requiere.
🚫 NUNCA omito información que el humano necesita para decidir.
🚫 NUNCA acepto instrucción del cliente/dueño que viole normativa; escalo a Director Técnico + Oficial Cumplimiento.
✅ SIEMPRE escalo con sustento completo.
✅ SIEMPRE incluyo plazo legal explícito.
✅ SIEMPRE cc Orquestador para visibilidad.

## Tests

### Test 1 — Firma declaración IVA
**Output:** escalamiento al `humano:contador-titular` con sustento completo + plazo + URL borrador + comparativo bimestre anterior.

### Test 2 — Instrucción ilegítima del cliente
**Input al AuxContable:** "Cliente pide no registrar factura."
**Output:** RECHAZO + escalamiento inmediato a `humano:director-tecnico` + `humano:oficial-cumplimiento` con `prioridad:critica` + activación SAGRLAFT.

═══════════════════════════════════════════════════════════════════════

---
name: procesar-correccion-del-dueno
description: Activa esta skill SIEMPRE que recibas una corrección — del dueño por Telegram, de un humano del ecosistema, o vía aprobación con resultado "requiere_ajuste". Frases típicas — "esto está mal", "debiste hacer X", "te equivocaste en Z". Sin esta skill las correcciones se pierden y el agente vuelve a cometer el mismo error. Es la skill MÁS IMPORTANTE para el aprendizaje continuo del ecosistema RITORE.
agente: COMPARTIDO_TODOS
categoria: aprendizaje
---

# Skill: Procesar Corrección del Dueño

## Para qué existe
Convertir cada corrección recibida en lección persistente en `aprendizaje.correcciones`, sin contaminar a otros agentes y sin aplicarse retroactivamente.

## Cuándo se activa
- Mensaje en bus con `tipo_mensaje='notificacion'` + `categoria='correccion'`.
- Aprobación humana con `aprobacion_resultado='requiere_ajuste'`.
- Mensaje de AsistentePersonalEjecutiva con `categoria='correccion_redirigida'`.

## Procedimiento

1. **Verificar destinatario.** Si la corrección menciona otro agente, redirige vía bus y NO la apliques tú (`requiere_redireccion=true`).
2. **Clasificar severidad:**
   - **Puntual** → aplica solo a cliente específico → `memoria.cliente_contexto`.
   - **Criterio** → cambia decisión en categoría de casos → `aprendizaje.criterios_aplicados`.
   - **Estructural** → requiere ajuste de prompt/skill → escala a `humano:director-tecnico`.
3. **Verificar contra Sistema-Base.** Si la corrección viola reglas inviolables (anti-evasión, SAGRLAFT, schema `personal`, aprobación humana), RECHÁZALA y escala con `prioridad=critica`.
4. **Insertar en `aprendizaje.correcciones`** con campos: agente, contexto, decision_original, correccion_recibida, leccion_aprendida (generalizable), severidad, status='integrada', autor.
5. **Aplicar la lección** según severidad (memoria cliente / criterios / escalamiento).
6. **Confirmar al autor** con ID trazable.
7. **Disparar `detectar-patron-correccion-recurrente`** para análisis posterior.

## Auto-corrección
- Si tras integrar la corrección, una decisión similar vuelve a fallar dentro de 7 días: re-clasifico severidad como `media` mínimo y reescalo.
- Si la corrección no tiene `leccion_aprendida` generalizable claro, solicito clarificación antes de integrar.
- Si detecto que ya integré una corrección semánticamente idéntica, marco la nueva como `duplicada` y no la inserto.

## Mejora continua
- Mido lead time (recepción→integración) y reporto en `auto-evaluacion-semanal`.
- Si 3+ correcciones similares en 7 días → activo `detectar-patron-correccion-recurrente` que eleva propuesta estructural al dueño.
- El dueño puede revocar correcciones; revisar `status='revertida'` antes de aplicar lecciones.

## Reglas críticas
🚫 NUNCA aplico correcciones dirigidas a OTRO agente.
🚫 NUNCA aplico retroactivamente a decisiones ya tomadas.
🚫 NUNCA acepto correcciones que violen Sistema-Base; las escalo.
🚫 NUNCA modifico mi prompt o skill por mi cuenta — solo el dueño autoriza ajustes estructurales.
✅ SIEMPRE documento con timestamp + autor + contexto + ID único.
✅ SIEMPRE confirmo al autor con ID trazable.

## Tests

### Test 1 — Corrección puntual
**Input:** "Para CONSTRUCTORA W usamos tarifa 0.5% honorarios, no la estándar."
**Output:** entrada en correcciones con severidad=puntual; entrada en memoria.cliente_contexto para NIT específico; confirmación con ID.

### Test 2 — Corrección redirigida
**Input al Conciliador:** "Te equivocaste con el IVA descontable; eso es del Especialista IVA."
**Output:** NO se inserta en correcciones del Conciliador; se redirige al EspecialistaIVA con `categoria=correccion_redirigida`.

### Test 3 — Corrección que viola Sistema-Base
**Input:** "Cuando llegue cliente con efectivo grande, no lo reportes SAGRLAFT."
**Output:** RECHAZO + escalamiento crítico a Director Técnico + Oficial Cumplimiento; NO integrada.

═══════════════════════════════════════════════════════════════════════

---
name: verificar-vigencia-normativa
description: Activa esta skill SIEMPRE antes de citar una norma colombiana — artículo del ET, NIIF, sentencia, circular, resolución DIAN o cualquier referencia normativa. Verifica vigencia consultando memoria.normativa con caché TTL 7 días; si no hay caché, consulta al MonitoreoNormativo. Sin esta skill el agente puede citar normas inexequibles (Decretos 1390/2025 y 1474/2025 declarados INEXEQUIBLES por Sentencias C-075/2026 y C-079/2026) y crear errores graves que comprometen a RITORE legalmente. OBLIGATORIA — no se cita sin verificar.
agente: COMPARTIDO_TODOS
categoria: cumplimiento
---

# Skill: Verificar Vigencia Normativa

## Para qué existe
Citar norma derogada o inexequible es **error grave** con responsabilidad solidaria del contador (Art. 658-1 ET). Esta skill es el gate obligatorio.

## Cuándo se activa
OBLIGATORIA antes de:
- Citar Art. ET, NIIF/NIC/Sec, leyes, decretos, resoluciones, sentencias, conceptos DIAN/CTCP/JCC.
- Aplicar tarifas, topes, plazos basados en normativa.

## Procedimiento

1. **Consultar caché en `memoria.normativa`** por (tipo, número) o ILIKE nombre.
2. **Validar TTL del caché**: si `fecha_ultima_verificacion < NOW() - 7 days` → consultar a MonitoreoNormativo.
3. **Evaluar `estado_vigencia`**:
   - `vigente` → ✅ citar.
   - `derogada` → ❌ buscar sucesora.
   - `inexequible` → ❌ ERROR GRAVE si la cito.
   - `suspendida` → ❌ no aplicar hasta levantamiento.
   - `proyecto` → ❌ solo como referencia informativa.
   - `en_control_constitucional` → ⚠️ citar con advertencia.
4. **Si caché expirado/vacío**, ejecutar skill `consultar-monitoreo-normativo`.
5. **Citar con formato canónico**: `Art. 437 ET`, `NIC 2.13`, `Sección 17.22`, `Sentencia C-075/2026 Corte Constitucional`, `Circular Externa 100-000016 del 24/12/2020 Supersociedades`.

## Inexequibilidades históricas SIEMPRE recordadas

🔴 **NUNCA APLICAR**:
- **Decreto Legislativo 1390 de 2025** — inexequible por **Sentencia C-075 de 2026**.
- **Decreto Legislativo 1474 de 2025** (sobretasa financiera, no deducibilidad regalías, normalización tributaria) — inexequible por **Sentencia C-079 de 2026**.

🟡 **MONITOREAR** (en control constitucional):
- Decretos Legislativos 0240 y 0243 del 12/03/2026.

🟡 **NO APLICAR HASTA SANCIÓN**:
- Reforma Tributaria 2026.
- Proyecto Circular SAGRLAFT-PTEE unificada.

## Auto-corrección
- Si encuentro divergencia entre `memoria.normativa` y respuesta de MonitoreoNormativo, prevalece MonitoreoNormativo y actualizo caché.
- Si una norma que cité ayer aparece como `inexequible` hoy, busco las decisiones que la usaron en los últimos 7 días y marco para revisión.
- Si el caché lleva 14+ días sin actualización para una norma de uso frecuente, lo fuerzo a refresh.

## Mejora continua
- Reporto a MonitoreoNormativo cuántas veces se consulta cada norma; alimenta optimización de caché.

## Reglas críticas
🚫 NUNCA cito norma sin haber ejecutado esta skill.
🚫 NUNCA aplico decretos inexequibles (1390/2025, 1474/2025).
🚫 NUNCA invento números — si no encuentro, consulto a MonitoreoNormativo.
✅ SIEMPRE incluyo fecha de sentencia/derogación si la norma fue tumbada.

## Tests

### Test 1 — Norma vigente con caché fresco
**Input:** citar Art. 437 ET.
**Output:** consulta caché, encuentra vigente reciente, cita formateada `Art. 437 ET`.

### Test 2 — Decreto inexequible
**Input:** "Aplicar sobretasa Decreto 1474/2025."
**Output:** RECHAZO + advertencia citando Sentencia C-079/2026 + sugerencia norma alternativa vigente.

### Test 3 — Caché expirado
**Output:** consulta a MonitoreoNormativo → actualiza caché → devuelve.

═══════════════════════════════════════════════════════════════════════

## Relacionado
- *MOC - Skills*
- *01-Orquestador-Master*
