---
tipo: agente
tags: [ritore, agente, operativa]
capa: operativa
nivel: senior
estado: activo
version: 2.0
fecha: 2026-06-11
---

# SKILLS — 06-AuxiliarTesoreria-Senior

**Documento consolidado** · 9 skills · Ecosistema RITORE · v2.0
**Modelo:** claude-opus-4-7

> Reescritura completa según [[00 - Estandar de Agentes RITORE]] (§2 secciones obligatorias, §3 umbrales, §4 anti-clonación). Las 2 skills de pagos con plazo legal (impuestos y nómina+PILA) se consolidaron en `programar-pagos-criticos-legales` con variantes paramétricas porque compartían > 70 % del procedimiento. Cada skill tiene ahora métricas propias con meta numérica (antes las 10 compartían las mismas 2) y el escalamiento vago "escalar al dueño con opciones cuantificadas" se reemplazó por la tabla de déficit con umbrales en SMMLV. Las reglas universales se heredan de [[Skills Compartidas RITORE]].

---

## Tabla de escalamiento de déficit de tesorería (fuente única del perfil)

Aplica a toda skill de este perfil que detecte déficit proyectado de caja. **SMMLV 2026 = $1.750.905.**

| Déficit proyectado (ventana 30 días) | Acción | Destino y plazo |
|---|---|---|
| **< 5 SMMLV** (< $8.754.525) | Informar con propuesta de manejo interno (reordenar pagos no críticos) | Dueño — informativo, en el reporte semanal |
| **5–20 SMMLV** ($8.754.525 – $35.018.100) | Presentar ≥ 2 opciones de financiación cuantificadas (costo, plazo, requisitos) con recomendación | Dueño — decisión requerida en ≤ 48 h |
| **> 20 SMMLV** (> $35.018.100) **o imposibilidad de pagar nómina, PILA o impuestos en plazo** | Escalamiento crítico con plan de contingencia (priorización legal de pagos, fuentes de liquidez, cronología) | Contador Titular + dueño — mismo día, SLA crítico 1 h para el primer aviso |

Complementa (no reemplaza) los umbrales generales del §3 del estándar.

---

## Índice de skills en este documento

- `proyectar-flujo-caja-90-dias`
- `programar-pagos-semanales`
- `programar-pagos-criticos-legales` *(base paramétrica: impuestos DIAN/territoriales · nómina + PILA)*
- `evitar-sobregiro-bancario`
- `aprovechar-descuento-pronto-pago`
- `invertir-excedentes-temporales`
- `gestionar-relacion-bancaria`
- `documentar-decision-financiacion`
- `renovar-matricula-mercantil`

═══════════════════════════════════════════════════════════════════════

---
name: proyectar-flujo-caja-90-dias
description: Activa cada lunes (antes de programar-pagos-semanales) para construir el flujo de caja a 90 días por semana — cobros esperados, egresos programados, saldo proyectado — e identificar déficits o excedentes con anticipación.
agente: RITORE-AuxiliarTesoreria-Senior
categoria: operativo
---

# Skill: proyectar-flujo-caja-90-dias

## Para qué existe
Toda decisión de tesorería (programar, postergar, financiar, invertir) depende de saber cuánta caja habrá y cuándo. Sin proyección, los déficits se descubren cuando ya son sobregiro y los excedentes duermen sin rentar.

## Cuándo se activa
- Cron semanal: lunes, antes de `programar-pagos-semanales`.
- Recalculo inmediato si ocurre un evento material: cobro ≥ 20 SMMLV no previsto, pago extraordinario, pérdida de un cliente relevante.
- Solicitud de Financiero, el dueño o el Orquestador.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Saldos bancarios del día | Conciliador / portales bancarios | Usar último saldo conciliado con marca `[DATO EN CACHÉ — verificar]` si no hay respuesta en 4 h, y escalar en paralelo |
| Aging CxC (cobros esperados con probabilidad por edad) y aging CxP (vencimientos) | [[05-AuxiliarCarteraCxP-Senior]] | Reiterar 1 vez; sin aging fresco, proyectar con el último disponible marcando la fecha del dato |
| Calendario de obligaciones legales (impuestos, nómina, PILA, cesantías) | Especialistas tributarios + AuxiliarNomina | Sin calendario confirmado, usar calendario del año anterior con marca `[CALENDARIO POR CONFIRMAR]` y pedir confirmación |
| Ventas/cobros proyectados del cliente | Cliente / Financiero | Proyectar solo con CxC real (escenario conservador) y declararlo en el supuesto |

## Procedimiento
1. Construir la línea base: saldo bancario inicial conciliado.
2. Proyectar cobros por semana: CxC por fecha esperada de pago (ajustada por comportamiento histórico del tercero, no por fecha de vencimiento teórica) + ventas de contado proyectadas.
3. Proyectar egresos por semana: CxP por vencimiento, impuestos por calendario, nómina + PILA, servicios recurrentes, financieros (cuotas de crédito).
4. Calcular saldo proyectado por semana para 13 semanas; marcar cada semana como superávit / equilibrio / déficit.
5. Clasificar los déficits según la **tabla de escalamiento de déficit** del perfil y disparar `evitar-sobregiro-bancario` para cada semana en déficit.
6. Marcar excedentes sostenidos (> 20 SMMLV por > 30 días) para `invertir-excedentes-temporales`.
7. Medir la desviación de la proyección de la semana anterior vs el real; si la desviación supera 15 %, documentar la causa y ajustar los supuestos del modelo.
8. Publicar a Financiero, al dueño (resumen) y al bus; entregar la semana 1 como insumo de `programar-pagos-semanales`.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Flujo proyectado 13 semanas | Cobros y egresos por semana con supuestos explícitos; saldo inicial = saldo bancario conciliado |
| Alertas de déficit clasificadas | Cada déficit tiene su nivel de la tabla del perfil y su skill/destino disparado |
| Medición de desviación semanal | Desviación semana anterior calculada y, si > 15 %, causa documentada y ajuste aplicado |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Desviación > 15 % dos semanas seguidas | Supuestos de cobro optimistas (clientes pagan más tarde que lo proyectado) | Recalibrar fecha esperada de pago con el comportamiento real por tercero | Pasar a escenario conservador (solo cobros confirmados) y declararlo al dueño |
| Obligación legal aparece fuera del calendario (requerimiento, sanción, cuota no registrada) | Calendario incompleto | Incorporarla de inmediato y recalcular las 13 semanas | Si genera déficit crítico, aplicar la tabla del perfil el mismo día |
| Saldos bancarios no disponibles el lunes | Portal caído o token vencido | Usar último saldo conciliado con marca y avisar al Conciliador | Si persiste > 24 h, escalar al Orquestador: la programación de pagos no puede correr a ciegas |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Déficit proyectado en cualquier semana | Tabla de escalamiento de déficit del perfil | Dueño / Contador Titular según nivel |
| Desviación proyección vs real | > 15 % una semana | Documentar y ajustar modelo |
| Desviación proyección vs real | > 30 % o > 15 % por 3 semanas seguidas | Financiero + Orquestador (revisión del modelo) |
| Insumo faltante (aging, calendario, saldos) | > 24 h hábiles tras reiterar 1 vez | Orquestador |

## Reglas críticas
🚫 NUNCA proyectar cobros por fecha de vencimiento teórica cuando existe comportamiento histórico del tercero que la contradice.
🚫 NUNCA publicar una proyección sin supuestos explícitos (qué cobros, qué probabilidad, qué calendario).
✅ SIEMPRE medir la desviación de la semana anterior antes de emitir la nueva proyección.

## Métricas
- Proyección publicada cada lunes antes de la programación de pagos: 100 % de las semanas.
- Desviación absoluta del saldo proyectado de la semana 1 vs real: ≤ 10 % (medición semanal).
- Déficits materializados que NO fueron anticipados con ≥ 5 días hábiles: 0 (medición mensual).
- Eventos materiales incorporados a la proyección en ≤ 24 h: 100 %.

## Tests
### Test 1 — (normal) Lunes: saldo conciliado $48M; CxC por cobrar del mes $120M (85 % con historial puntual), CxP $75M, nómina+PILA $32M, IVA bimestral $18M en la semana 3
**Output:** flujo de 13 semanas con saldo por semana; semana 3 queda en déficit proyectado de $6,2M (< 5 SMMLV) → nivel informativo de la tabla: propuesta de reordenar 2 pagos de proveedores no críticos de la semana 3 a la 4, informada al dueño en el reporte semanal; desviación de la semana previa 7 % (dentro de meta, sin ajuste).
### Test 2 — (excepción) El cliente principal (40 % de los cobros proyectados) avisa el miércoles que pagará 45 días tarde
**Output:** recalculo inmediato sin esperar al lunes; las semanas 2-6 entran en déficit de $38M (> 20 SMMLV) → escalamiento crítico el mismo día a Contador Titular + dueño con plan de contingencia: priorización legal de pagos (nómina y PILA primero, impuestos en plazo, proveedores renegociados), 2 fuentes de liquidez cuantificadas (descuento de cartera vs línea de crédito) y cronología; disparo de `evitar-sobregiro-bancario` y `documentar-decision-financiacion` si se toma deuda.

═══════════════════════════════════════════════════════════════════════

---
name: programar-pagos-semanales
description: Activa lunes 8 AM para programar los pagos de la semana — vencimientos CxP, impuestos, nómina, servicios — priorizando por criticidad legal, validando disponibilidad y obteniendo autorización antes de ejecutar.
agente: RITORE-AuxiliarTesoreria-Senior
categoria: operativo
---

# Skill: programar-pagos-semanales

## Para qué existe
Pagar sin orden de prioridad legal expone al cliente a sanciones (impuestos, PILA) por cubrir primero lo no crítico. Esta skill convierte las obligaciones de la semana en un calendario priorizado, autorizado y ejecutable sin sobregiro.

## Cuándo se activa
- Cron: lunes 8 a.m., con el flujo de caja de la semana ya publicado.
- Reprogramación intra-semana: cobro relevante recibido, pago rechazado por el banco o instrucción del dueño.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Flujo de caja semana 1 | `proyectar-flujo-caja-90-dias` | No programar a ciegas: pedir la proyección (espera 4 h) y, si no llega, programar SOLO obligaciones legales con saldo confirmado y escalar |
| Aging CxP con vencimientos a 14 días | [[05-AuxiliarCarteraCxP-Senior]] | Reiterar 1 vez; sin aging, usar vencimientos del ERP con marca `[DATO EN CACHÉ — verificar]` |
| Obligaciones legales de la semana (montos y fechas exactas) | Especialistas / AuxiliarNomina vía `programar-pagos-criticos-legales` | Confirmar contra calendario tributario; nunca asumir "no hay vencimientos" sin verificación |
| Autorización de la programación | Contador Titular / dueño según política del cliente | SIN autorización NO se ejecuta ningún pago; reiterar a las 4 h; al 80 % del SLA alertar al Orquestador |

## Procedimiento
1. Consolidar obligaciones de los próximos 14 días (las de la semana se programan; las de la siguiente se anticipan en el calendario).
2. Priorizar: (1) impuestos con vencimiento legal, (2) nómina + PILA, (3) servicios críticos para operar (energía, arriendo, telecomunicaciones), (4) pagos con descuento pronto pago vigente, (5) proveedores por antigüedad de vencimiento.
3. Validar disponibilidad: total programado ≤ saldo disponible + cobros confirmados de la semana. Si no alcanza, recortar desde la prioridad 5 hacia arriba — las prioridades 1 y 2 no se recortan: si están en riesgo, aplicar la **tabla de escalamiento de déficit** (nivel crítico).
4. Preparar el calendario semanal: pago, tercero, monto, fecha, cuenta origen, prioridad.
5. Obtener autorización (Contador Titular o dueño según la política del cliente) ANTES de cargar pagos al portal.
6. Cargar y ejecutar los pagos autorizados; capturar comprobante de cada uno.
7. Cierre de semana: comparar programado vs ejecutado; documentar diferencias y entregarlas como insumo de la desviación del flujo.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Calendario semanal autorizado | 100 % de pagos con prioridad asignada; autorización registrada ANTES de la ejecución |
| Comprobantes de pago | 1 comprobante por pago ejecutado, archivado y notificado a CarteraCxP (aplicación) y AuxContable (asiento) |
| Cierre programado vs ejecutado | Diferencias explicadas; ningún pago ejecutado fuera del calendario sin autorización registrada |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Pago rechazado por el banco (cuenta destino errada, fondos, límites) | Datos del tercero desactualizados o tope transaccional | Corregir datos contra RUT/certificación bancaria y reintentar el mismo día | Si es pago legal (prioridad 1-2) y no pasa, escalamiento crítico mismo día (tabla del perfil); si es proveedor, reprogramar y avisar a CarteraCxP |
| Autorizador no disponible y hay vencimientos legales hoy | Vacaciones, viaje, contingencia | Activar autorizador suplente definido en la política del cliente | Sin suplente definido: escalar a Contador Titular + dueño (SLA crítico 1 h); documentar; NUNCA pagar sin autorización |
| Doble pago de la misma factura | Factura presente en dos fuentes (ERP y correo) | Cruzar contra CxP antes de cargar; anular el duplicado en el portal | Si ya salió, gestionar recuperación con el banco/tercero y notificar a CarteraCxP y al Conciliador el mismo día |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Disponibilidad insuficiente para prioridades 1-2 (impuestos, nómina, PILA) | Cualquier monto | Nivel crítico de la tabla del perfil: Contador Titular + dueño, mismo día |
| Déficit para prioridades 3-5 | Según monto, tabla de escalamiento de déficit | Dueño (informativo o decisión según nivel) |
| Autorización pendiente | 4 h (SLA alto); al 80 % alertar al Orquestador | Orquestador → humano |
| Pago ejecutado fuera del calendario sin autorización | 1 ocurrencia | Reversar si es posible y reportar al Contador Titular el mismo día |

## Reglas críticas
🚫 NUNCA ejecutar un pago sin autorización registrada del Contador Titular o del dueño según la política.
🚫 NUNCA recortar impuestos, nómina o PILA para pagar proveedores.
🚫 NUNCA cargar pagos a cuentas de terceros no validadas contra RUT/certificación bancaria.
✅ SIEMPRE cerrar la semana comparando programado vs ejecutado.

## Métricas
- Pagos de prioridad 1-2 ejecutados en su fecha legal: 100 % (medición semanal).
- Calendario emitido y enviado a autorización el lunes antes de las 10 a.m.: ≥ 95 %.
- Pagos ejecutados fuera de calendario sin autorización: 0.
- Dobles pagos: 0 (medición mensual).

## Tests
### Test 1 — (normal) Semana con disponibilidad $90M y obligaciones: retefuente $8M (vence miércoles), nómina quincena $26M (viernes), arriendo $6M, proveedor con descuento 2 % si paga antes del jueves ($20M), otros proveedores $35M
**Output:** calendario priorizado (retefuente → nómina → arriendo → proveedor con descuento → resto), total $95M > $90M → se posterga $5M del último proveedor a la semana siguiente con justificación; autorización del Contador Titular registrada lunes 9:40 a.m.; ejecución con comprobantes; cierre viernes sin diferencias.
### Test 2 — (excepción) El miércoles el banco rechaza el pago de retefuente por token vencido del portal y el plazo DIAN vence ese mismo día
**Output:** tratamiento de incidente crítico: reintento inmediato por canal alterno (PSE DIAN directo / sucursal), aviso al Contador Titular y al dueño dentro de la primera hora; si el pago no logra salir el mismo día, cuantificación de sanción e intereses moratorios y plan de pago al día hábil siguiente documentado; registro del incidente y corrección de causa raíz (renovación de token con responsable y fecha) — el error no se repite el siguiente vencimiento.

═══════════════════════════════════════════════════════════════════════

---
name: programar-pagos-criticos-legales
description: Skill base de pagos con plazo legal y sanción automática por mora. Variante A — impuestos (DIAN y territoriales) tras recibir declaración firmada; variante B — nómina y PILA coordinada con AuxiliarNomina. Consolida programar-pago-impuestos y programar-pago-nomina-PILA (v1.0).
agente: RITORE-AuxiliarTesoreria-Senior
categoria: operativo
---

# Skill: programar-pagos-criticos-legales

## Para qué existe
Impuestos, nómina y PILA son los únicos pagos cuyo atraso genera sanciones automáticas (intereses moratorios DIAN, sanción UGPP) o riesgo laboral inmediato. Por eso tienen skill propia con verificación de plazo legal independiente del calendario semanal: si todo lo demás falla, esto se paga.

## Cuándo se activa (por variante)

| Variante | Trigger |
|---|---|
| **A — Impuestos** | Especialista tributario entrega declaración firmada con valor a pagar (IVA, retefuente, renta, ICA, etc.) |
| **B — Nómina + PILA** | AuxiliarNomina entrega nómina liquidada y aprobada del periodo |

## Inputs

| Insumo | De quién | Formato | Si falta |
|---|---|---|---|
| Declaración firmada con valor y plazo (variante A) | Especialista tributario | PDF + recibo 490 si aplica | NO pagar sobre borradores; reclamar la declaración firmada (espera 4 h por SLA del vencimiento; al 80 % alertar Orquestador) |
| Nómina liquidada y aprobada + archivo de dispersión + planilla PILA (variante B) | AuxiliarNomina | Archivo banco + planilla operador | Reiterar de inmediato; si el vencimiento PILA es ≤ 2 días hábiles, escalar al Orquestador sin esperar 24 h |
| Plazo legal exacto (calendario DIAN por NIT / calendario PILA por dígitos del NIT) | Especialista / AuxiliarNomina / calendario tributario | Fecha | NUNCA asumir el plazo: verificar contra el calendario oficial vigente; `[VERIFICAR]` ante cualquier duda |
| Disponibilidad en la cuenta pagadora | `proyectar-flujo-caja-90-dias` + saldo del día | Saldo | Si no alcanza: nivel crítico de la tabla de escalamiento de déficit, mismo día |
| Autorización de pago | Contador Titular / dueño según política | Registro | Sin autorización no se paga; SLA 4 h con alerta al 80 % |

## Procedimiento

**Tronco común:**
1. Verificar el plazo legal contra el calendario oficial (no contra memoria ni contra el año pasado).
2. Validar disponibilidad en la cuenta pagadora a la fecha del pago; si falta, activar tabla de déficit (nivel crítico) de inmediato.
3. Programar el pago con ≥ 2 días hábiles de margen sobre el vencimiento (colchón para rechazos técnicos).
4. Obtener autorización registrada.
5. Ejecutar, capturar comprobante y verificar que el débito aparezca en el extracto del día.
6. Notificar con comprobante al emisor de la obligación y al Contador Titular; archivar.

**Pasos específicos por variante:**

| Variante | Pasos propios |
|---|---|
| **A — Impuestos** | (a) Validar que el valor a pagar del portal coincide con la declaración firmada. (b) Pagar por PSE DIAN o recibo 490 según el caso; impuestos territoriales por el portal del municipio. (c) Si el cliente decide no pagar total (pago parcial), exigir instrucción escrita y notificar al Especialista (los intereses corren sobre el saldo). |
| **B — Nómina + PILA** | (a) Validar plazo PILA según los dos últimos dígitos del NIT en el calendario del operador vigente. (b) Dispersar salarios (archivo banco/ACH) ANTES de pagar PILA si la caja obliga a secuenciar — el salario es prioridad 1 laboral. (c) Pagar la planilla en el operador (Enlace Operativo/ARUS/SOI/Mi Planilla según cliente). (d) Confirmar a AuxiliarNomina con ambos comprobantes (dispersión + PILA). |

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Pago ejecutado dentro del plazo legal | Fecha de débito ≤ fecha de vencimiento; comprobante archivado |
| Notificación con comprobante | Al Especialista (A) o a AuxiliarNomina (B) + Contador Titular, el mismo día del pago |
| Registro del margen | Pago programado con ≥ 2 días hábiles de anticipación al vencimiento (o la excepción documentada) |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Valor del portal DIAN ≠ declaración firmada | Corrección posterior o error de prediligenciado | Detener el pago y confirmar con el Especialista qué valor rige | No pagar hasta resolver; si el vencimiento es hoy, escalar a Contador Titular dentro de la hora |
| PILA rechazada por el operador (inconsistencias de novedades/IBC) | Error en la planilla | Devolver a AuxiliarNomina con el detalle del rechazo para corrección inmediata | Si el plazo vence, pagar la planilla corregida apenas esté y cuantificar la mora; aviso a Contador Titular el mismo día |
| Dispersión de salarios parcialmente rechazada (cuentas inactivas) | Datos bancarios de empleados desactualizados | Reprocesar los rechazados por canal alterno el mismo día | Pago por ventanilla/cheque al empleado afectado en ≤ 24 h y corrección del maestro con AuxiliarNomina |
| Caja insuficiente para nómina o impuestos | Déficit no anticipado | Activar nivel crítico de la tabla de déficit: Contador Titular + dueño con plan de contingencia | Documentar la decisión humana resultante; nunca decidir yo qué obligación legal se incumple |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Riesgo de no pagar impuestos, nómina o PILA en plazo | Cualquier monto | Nivel crítico de la tabla del perfil: Contador Titular + dueño, primer aviso ≤ 1 h |
| Insumo faltante (declaración, nómina, planilla) con vencimiento ≤ 2 días hábiles | — | Orquestador de inmediato (sin esperar 24 h) |
| Pago parcial de impuestos solicitado por el cliente | Cualquier monto | Instrucción escrita + Especialista + Contador Titular |
| Mora materializada (pago extemporáneo) | 1 ocurrencia | Contador Titular con cuantificación de sanción/intereses, mismo día |

## Reglas críticas
🚫 NUNCA pagar impuestos sobre borradores o valores no confirmados con la declaración firmada.
🚫 NUNCA asumir el plazo legal de memoria: siempre contra calendario oficial vigente.
🚫 NUNCA decidir por cuenta propia qué obligación legal se deja de pagar cuando la caja no alcanza (eso se escala con plan, nivel crítico).
✅ SIEMPRE programar con ≥ 2 días hábiles de margen sobre el vencimiento.

## Métricas
- Pagos de impuestos dentro del plazo legal: 100 % (cero extemporáneos, medición mensual).
- PILA pagada en el plazo del calendario por dígitos del NIT: 100 %.
- Pagos programados con margen ≥ 2 días hábiles: ≥ 95 % (excepciones documentadas).
- Intereses moratorios o sanciones causados por gestión de tesorería: $0 acumulado anual.

## Tests
### Test 1 — (normal, variante A) EspecialistaIVA entrega el lunes la declaración bimestral firmada por $14.300.000; el calendario DIAN da vencimiento el viernes según el NIT
**Output:** plazo verificado contra el calendario oficial 2026 (no asumido); disponibilidad confirmada con el flujo de la semana; pago programado para el miércoles (2 días de margen); autorización registrada; PSE DIAN ejecutado, comprobante cruzado contra el extracto y enviado al Especialista y al Contador Titular el mismo día.
### Test 2 — (excepción, variante B) AuxiliarNomina entrega la quincena el día del vencimiento PILA y al cargar la planilla el operador la rechaza por una novedad de ingreso mal reportada
**Output:** devolución inmediata a AuxiliarNomina con el detalle exacto del rechazo; mientras corrige, dispersión de salarios ejecutada (no se retiene el salario por el problema de PILA); planilla corregida y pagada el mismo día si el operador la acepta; si queda extemporánea, cuantificación de la mora e informe al Contador Titular el mismo día con causa raíz (entrega tardía) y compromiso de calendario con AuxiliarNomina para el siguiente periodo.

═══════════════════════════════════════════════════════════════════════

---
name: evitar-sobregiro-bancario
description: Activa cuando la proyección o el monitoreo diario detecta saldo bancario negativo o déficit en la ventana de 30 días. Construye opciones cuantificadas (postergar, anticipar cobros, financiar) y escala según la tabla de déficit del perfil.
agente: RITORE-AuxiliarTesoreria-Senior
categoria: operativo
---

# Skill: evitar-sobregiro-bancario

## Para qué existe
El sobregiro es la financiación más cara y la señal pública más dañina ante el banco. Esta skill convierte un déficit detectado en un menú de opciones cuantificadas con destino y plazo de decisión claros, en lugar de una alerta genérica.

## Cuándo se activa
- `proyectar-flujo-caja-90-dias` marca cualquier semana en déficit.
- Monitoreo diario: el saldo disponible del día cae por debajo de los pagos comprometidos de los próximos 5 días hábiles.
- Pago inesperado material (≥ 5 SMMLV) sin caja que lo respalde.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Déficit cuantificado por semana (monto y fechas) | `proyectar-flujo-caja-90-dias` | Recalcular el tramo afectado antes de proponer opciones; sin cifra no hay opciones serias |
| Pagos postergables (prioridades 3-5) con costo de postergar (mora pactada, pérdida de descuento, relación) | `programar-pagos-semanales` + aging CxP | Asumir que solo prioridad 5 es postergable y declararlo |
| Cartera descontable / cobros anticipables | Aging CxC de [[05-AuxiliarCarteraCxP-Senior]] | Excluir la opción de descuento de cartera y dejarlo explícito |
| Condiciones de líneas de crédito disponibles (cupo, tasa, plazo de desembolso) | `gestionar-relacion-bancaria` / bancos | Solicitar cotización exprés; mientras llega, presentar la opción con datos de la última negociación marcados `[DATO EN CACHÉ — verificar]` |

## Procedimiento
1. Confirmar el déficit: monto máximo, semana en que ocurre y duración (¿es puntual o estructural?).
2. Construir el menú de opciones, cada una cuantificada (monto que libera, costo, plazo de implementación, riesgo):
   a. Postergar pagos no críticos (prioridades 3-5) con costo explícito.
   b. Anticipar cobros: gestión de cobro intensiva vía AtencionCliente sobre cartera corriente grande.
   c. Descuento de cartera / factoring (costo financiero efectivo).
   d. Uso de línea de crédito o cupo de sobregiro PACTADO (no sobregiro de hecho).
3. Clasificar el déficit en la **tabla de escalamiento de déficit** del perfil y enviar al destino que corresponda (informativo / decisión requerida ≤ 48 h / crítico mismo día).
4. Ejecutar la opción decidida por el humano; si implica deuda nueva, disparar `documentar-decision-financiacion`.
5. Verificar después del evento: ¿se evitó el sobregiro? Documentar el desenlace y la efectividad de la opción elegida.
6. Si el déficit es estructural (se repite ≥ 3 proyecciones seguidas), reportar a Financiero como problema de fondo, no de tesorería.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Menú de opciones cuantificadas | ≥ 2 opciones, cada una con monto, costo, plazo y riesgo; recomendación argumentada |
| Escalamiento según tabla del perfil | Nivel correcto según monto; registro de a quién, cuándo y respuesta |
| Registro del desenlace | Sobregiro evitado sí/no, opción ejecutada, costo real vs estimado |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| El dueño no decide dentro del plazo (48 h, nivel medio) | Agenda, indecisión | Reiterar al 80 % del plazo con consecuencia cuantificada de no decidir | Al vencer, escalar a Contador Titular (el silencio no autoriza: yo no elijo por el dueño) |
| La opción elegida no se materializa a tiempo (desembolso demorado) | Tiempos del banco | Activar la segunda opción del menú de inmediato | Escalamiento crítico si el sobregiro queda a < 2 días hábiles |
| Déficit calculado sobre proyección desactualizada | Cobro grande recibido después del corte | Recalcular antes de escalar (no quemar un escalamiento crítico falso) | Si ya se escaló y el déficit desaparece, retractar formalmente el mismo día |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Déficit proyectado | **< 5 SMMLV** | Dueño — informativo (reporte semanal) con propuesta interna |
| Déficit proyectado | **5–20 SMMLV** | Dueño — menú de financiación, decisión requerida ≤ 48 h |
| Déficit proyectado o sobregiro inminente | **> 20 SMMLV** o compromete nómina/PILA/impuestos | Contador Titular + dueño — crítico, primer aviso ≤ 1 h, plan de contingencia |
| Déficit estructural | ≥ 3 proyecciones consecutivas en déficit | Financiero + dueño (problema de fondo del negocio) |

## Reglas críticas
🚫 NUNCA permitir sobregiro de hecho como "solución": solo cupos pactados con el banco.
🚫 NUNCA postergar pagos de prioridad 1-2 (impuestos, nómina, PILA) como opción de manejo de déficit sin escalamiento crítico previo.
✅ SIEMPRE presentar mínimo 2 opciones cuantificadas con recomendación — nunca el problema sin el menú.

## Métricas
- Sobregiros de hecho materializados: 0 (medición mensual).
- Déficits escalados en el nivel correcto de la tabla y dentro del plazo del nivel: 100 %.
- Opciones presentadas por evento de déficit: ≥ 2 con costos cuantificados, 100 % de los eventos.
- Tiempo entre detección del déficit crítico y primer aviso: ≤ 1 h, 100 % de los casos.

## Tests
### Test 1 — (normal) La proyección del lunes muestra déficit de $12M en la semana 2 por concentración de vencimientos CxP
**Output:** déficit en rango 5–20 SMMLV → menú al dueño con decisión requerida ≤ 48 h: (a) postergar $8M de proveedores prioridad 5 (costo: pérdida de descuento $160.000), (b) descuento de cartera de $15M al 1,8 % mes (costo ~$270.000), recomendación (a) por menor costo; decisión del dueño registrada el martes; reprogramación ejecutada; desenlace: sobregiro evitado, costo real igual al estimado.
### Test 2 — (excepción) Jueves: un cliente grande reversa un pago de $40M ya contado en la proyección y el lunes vence la nómina de $28M
**Output:** déficit > 20 SMMLV + compromete nómina → escalamiento crítico dentro de la primera hora a Contador Titular + dueño con plan de contingencia: salarios primero, PILA en plazo, propuesta de desembolso exprés de línea pactada ($30M, desembolso 24-48 h) y gestión simultánea del recobro al cliente; seguimiento horario hasta asegurar la nómina; desenlace y costo documentados; disparo de `documentar-decision-financiacion` por el uso de la línea.

═══════════════════════════════════════════════════════════════════════

---
name: aprovechar-descuento-pronto-pago
description: Activa cuando un proveedor ofrece descuento por pronto pago y el flujo lo permite. Evalúa la tasa efectiva del descuento contra el costo de oportunidad de la caja y programa el pago anticipado si conviene.
agente: RITORE-AuxiliarTesoreria-Senior
categoria: operativo
---

# Skill: aprovechar-descuento-pronto-pago

## Para qué existe
Un descuento por pronto pago suele equivaler a una tasa efectiva anual altísima (2 % por pagar 20 días antes ≈ 36 % EA): dejarlo pasar teniendo caja es regalar rentabilidad. Pero tomarlo sin verificar el flujo puede crear el déficit que luego cuesta más financiar.

## Cuándo se activa
- CarteraCxP o la causación identifican condición de descuento en una factura (ej. "2/10 neto 30").
- Oferta puntual del proveedor comunicada por el cliente.
- Revisión semanal del aging CxP: facturas con ventana de descuento aún abierta.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Condición exacta del descuento (%, ventana, base) | Factura / CarteraCxP / proveedor | Sin condición escrita NO se paga anticipado "de palabra": pedir confirmación escrita (24 h hábiles) |
| Flujo de caja de las semanas afectadas | `proyectar-flujo-caja-90-dias` | No anticipar pagos sin proyección vigente: el descuento nunca justifica un déficit en prioridades 1-2 |
| Costo de oportunidad de la caja (tasa de inversión temporal o costo de la línea si habría que financiar) | `invertir-excedentes-temporales` / `gestionar-relacion-bancaria` | Usar tasa de referencia conservadora documentada con marca `[TASA DE REFERENCIA]` |

## Procedimiento
1. Calcular la tasa efectiva anual del descuento: EA ≈ (d / (1−d)) × (365 / días anticipados), con d = % de descuento.
2. Comparar contra el costo de oportunidad: si la caja sobra → comparar con la tasa de inversión temporal; si habría que dejar de hacer otro pago o financiarse → comparar con ese costo.
3. Verificar en el flujo que el pago anticipado NO genera déficit en la ventana de 30 días (si lo genera, la evaluación pasa por la tabla de déficit del perfil — normalmente se descarta).
4. Si conviene: incluir el pago en `programar-pagos-semanales` con prioridad 4 y la condición de descuento adjunta; obtener autorización ordinaria.
5. Coordinar con CarteraCxP la aplicación del pago CON el descuento reconocido (variante D de `aplicar-pago-a-tercero`) — el pago y el registro del descuento van juntos.
6. Registrar el ahorro capturado del mes (suma de descuentos tomados) y las oportunidades descartadas con su razón.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Evaluación por oportunidad | Tasa EA del descuento calculada y comparada contra costo de oportunidad explícito |
| Pago anticipado programado (si conviene) | Dentro de la ventana de descuento, sin generar déficit, con autorización |
| Registro de ahorro mensual | Ahorro capturado + oportunidades descartadas con razón documentada |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Proveedor no respeta el descuento pese al pago en ventana | Condición mal comunicada o disputa de fecha valor | Reclamar con el comprobante de fecha valor del banco | Notificar a CarteraCxP para que la diferencia quede como saldo a favor en disputa; informar al cliente |
| Descuento tomado genera déficit imprevisto (cobro esperado falló) | Proyección desviada | Disparar `evitar-sobregiro-bancario` de inmediato | Aplicar tabla de déficit; documentar la lección: ese proveedor/monto exige cobros confirmados, no proyectados |
| Ventana de descuento ya vencida al detectar la condición | Causación tardía de la factura | Verificar fecha real de recepción; negociar extensión con el proveedor | Registrar la oportunidad perdida con causa (causación tardía) para corregir el proceso aguas arriba |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Pago anticipado individual | ≥ 20 SMMLV | Dueño — decisión expresa (no basta autorización ordinaria) |
| Tomar el descuento exige financiarse | Cualquier monto | Evaluar como decisión de financiación: dueño + `documentar-decision-financiacion` |
| Oportunidades perdidas por causación tardía | ≥ 3 en un trimestre | Orquestador (defecto de proceso aguas arriba) |

## Reglas críticas
🚫 NUNCA tomar un descuento que comprometa pagos de prioridad 1-2 en la ventana de 30 días.
🚫 NUNCA pagar anticipado sobre condiciones de descuento verbales.
✅ SIEMPRE decidir con tasa efectiva anual comparada, no con el % nominal del descuento.

## Métricas
- Aprovechamiento de descuentos viables (los que pasan el filtro de flujo): ≥ 70 % (medición mensual).
- Ahorro capturado por descuentos: reportado en pesos cada mes, meta ≥ el costo financiero mensual del cliente como referencia de gestión.
- Descuentos tomados que generaron déficit posterior: 0.
- Oportunidades perdidas por causación tardía: ≤ 1 por trimestre.

## Tests
### Test 1 — (normal) Factura de $20.000.000 con condición 2/10 neto 30; hay caja excedente que rinde 0,75 % mes en fondo de liquidez
**Output:** EA del descuento ≈ (0,02/0,98) × (365/20) ≈ 37 % EA vs ~9,4 % EA del fondo → conviene; flujo verificado sin déficit en 30 días; pago de $19.600.000 programado dentro de la ventana con autorización; CarteraCxP aplica con descuento reconocido ($400.000 de ahorro registrado en el acumulado del mes).
### Test 2 — (excepción) Proveedor ofrece 4 % por pago inmediato de $60M, pero tomarlo obligaría a usar la línea de crédito al 1,9 % mes durante 25 días
**Output:** EA del descuento ≈ (0,04/0,96) × (365/25) ≈ 61 % EA vs costo de la línea ~25 % EA → financieramente conviene, PERO supera 20 SMMLV y exige financiarse → no se ejecuta con autorización ordinaria: se presenta al dueño como decisión expresa con ambos números y el efecto en el flujo, y se dispara `documentar-decision-financiacion`; sin decisión del dueño en la ventana, la oportunidad se deja pasar y queda registrada con su razón.

═══════════════════════════════════════════════════════════════════════

---
name: invertir-excedentes-temporales
description: Activa cuando el saldo disponible supera 20 SMMLV por encima de las necesidades de la ventana de 30 días durante más de 30 días sostenidos. Propone opciones de inversión temporal de bajo riesgo (CDT, fondos de liquidez) para decisión del dueño.
agente: RITORE-AuxiliarTesoreria-Senior
categoria: operativo
---

# Skill: invertir-excedentes-temporales

## Para qué existe
La caja ociosa pierde contra la inflación y contra el GMF de moverla mal. Esta skill detecta excedentes estructurales y los convierte en propuestas de inversión comparables — la decisión siempre es del dueño.

## Cuándo se activa
- `proyectar-flujo-caja-90-dias` muestra excedente > 20 SMMLV (> $35.018.100) sobre las necesidades de 30 días, sostenido > 30 días.
- Ingreso extraordinario (venta de activo, capitalización) sin destino inmediato.
- Vencimiento de una inversión existente (decidir renovación).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Excedente cuantificado y su horizonte (cuándo se necesitará la plata) | `proyectar-flujo-caja-90-dias` | Sin horizonte NO se propone inversión: el plazo del instrumento debe caber en el horizonte de caja |
| Apetito de riesgo y restricciones del cliente | `cargar-perfil-cliente` / dueño | Asumir perfil más conservador (fondos de liquidez a la vista) y declararlo |
| Tasas vigentes de ≥ 2 instrumentos (CDT por plazo, fondo de liquidez) | Bancos vía `gestionar-relacion-bancaria` | Solicitar cotizaciones; con datos viejos, marcar `[TASA POR CONFIRMAR]` y no ejecutar hasta confirmar |
| Efecto GMF y comisiones del movimiento | Banco / AuxContable | Incluir estimado conservador del 4×1000 en la comparación; sin él la rentabilidad neta está inflada |

## Procedimiento
1. Confirmar que el excedente es estructural: descontar obligaciones estacionales de los próximos 90 días (prima, impuestos anuales, renovación mercantil) antes de declarar excedente invertible.
2. Definir monto invertible = excedente − colchón mínimo de seguridad (default: 1 mes de egresos operativos; el perfil del cliente puede fijar otro).
3. Construir ≥ 2 opciones comparables: instrumento, tasa EA, plazo, liquidez (penalidad de redención), riesgo, rentabilidad neta de GMF y comisiones.
4. Presentar al dueño con recomendación; decisión requerida — sin decisión no se mueve dinero.
5. Ejecutada la decisión: registrar la inversión, el plazo y la fecha de vencimiento en el calendario de tesorería; notificar a AuxContable (registro contable) y a Financiero.
6. Al vencimiento: reevaluar (renovar / liquidar según el flujo vigente) — nunca renovar automático.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Propuesta de inversión | ≥ 2 opciones con tasa EA neta de GMF/comisiones, plazo dentro del horizonte de caja, riesgo explícito |
| Decisión registrada del dueño | Por escrito antes de cualquier movimiento |
| Calendario de vencimientos | Toda inversión vigente con fecha de vencimiento y alerta 5 días hábiles antes |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| El flujo cambia y la plata invertida se necesita antes del vencimiento | Déficit sobreviniente | Comparar penalidad de redención anticipada vs costo de financiarse el faltante; presentar ambos al dueño | Aplicar tabla de déficit del perfil; lección: ajustar el colchón mínimo de ese cliente |
| Propuesta del banco con instrumento fuera del perfil conservador (fiducia estructurada, derivados) | Comercial del banco empuja producto | Excluirla del menú salvo instrucción expresa del dueño | Documentar el ofrecimiento y la exclusión; informar al dueño sin recomendarla |
| Inversión vence y nadie decide | Falta de seguimiento | Alerta 5 días hábiles antes; reiterar al vencimiento | Default seguro: liquidar a cuenta corriente (no renovar a ciegas) e informar el mismo día |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Propuesta de inversión | Cualquier monto | Dueño — decisión expresa requerida (yo nunca muevo dinero a inversión por cuenta propia) |
| Monto a invertir | ≥ 100 SMMLV (~$175M) | Dueño + Contador Titular (efecto patrimonial y fiscal del rendimiento) |
| Necesidad de redención anticipada | Cualquier caso | Dueño con comparación penalidad vs financiación |

## Reglas críticas
🚫 NUNCA invertir sin decisión escrita del dueño, sin importar lo obvio del excedente.
🚫 NUNCA proponer plazos que excedan el horizonte de caja del flujo a 90 días sin colchón.
🚫 NUNCA comparar tasas brutas: siempre netas de GMF y comisiones.
✅ SIEMPRE mantener el colchón mínimo de seguridad fuera de cualquier inversión.

## Métricas
- Excedentes > 20 SMMLV sostenidos > 30 días sin propuesta presentada: 0 (medición mensual).
- Propuestas con ≥ 2 opciones netas comparadas: 100 %.
- Redenciones anticipadas con penalidad: ≤ 1 por año por cliente (señal de buen calce de plazos).
- Vencimientos gestionados antes del día del vencimiento: 100 %.

## Tests
### Test 1 — (normal) Cliente acumula $80M sobre las necesidades de 30 días durante 6 semanas; en 90 días no hay obligaciones extraordinarias salvo prima de junio ($14M)
**Output:** excedente estructural = $80M − $14M (estacional) − colchón 1 mes de egresos ($25M) = $41M invertibles; menú: CDT 60 días al X % EA vs fondo de liquidez al Y % EA, ambos netos de GMF, con liquidez y riesgo comparados; recomendación según horizonte; decisión del dueño registrada antes de constituir; vencimiento en calendario con alerta a 5 días.
### Test 2 — (excepción) Con $50M en CDT a 90 días, una avería mayor exige $30M en la semana 2
**Output:** comparación presentada al dueño el mismo día: penalidad de redención anticipada del CDT vs costo de cubrir $30M con la línea de crédito hasta el vencimiento; recomendación por menor costo neto; decisión del dueño ejecutada; lección registrada: el colchón mínimo de este cliente sube (su operación tiene contingencias físicas), ajuste aplicado al parámetro del perfil.

═══════════════════════════════════════════════════════════════════════

---
name: gestionar-relacion-bancaria
description: Activa para negociar o renegociar condiciones con bancos — tasas, comisiones, cupos, productos — y para mantener el inventario de condiciones vigentes por banco que alimenta a las demás skills de tesorería.
agente: RITORE-AuxiliarTesoreria-Senior
categoria: operativo
---

# Skill: gestionar-relacion-bancaria

## Para qué existe
Las condiciones bancarias (tasas, comisiones, cupos) no mejoran solas: se negocian con datos. Además, `evitar-sobregiro-bancario`, `invertir-excedentes-temporales` y `documentar-decision-financiacion` dependen de un inventario actualizado de condiciones por banco — esta skill lo mantiene.

## Cuándo se activa
- Revisión programada: 1 vez al año por banco activo del cliente.
- Evento: comisiones que suben sin aviso, necesidad de cupo nuevo o ampliado, oferta de otro banco que sirve de palanca.
- Solicitud de `evitar-sobregiro-bancario` (cupo) o `invertir-excedentes-temporales` (tasas).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Histórico operativo con el banco (volúmenes, reciprocidad, productos, incidencias) | Registros propios + Conciliador | Reconstruir con extractos de los últimos 12 meses; sin histórico la negociación pierde palanca y se declara |
| Condiciones vigentes (tarifario aplicado al cliente) | Banco / extractos | Solicitar tarifario por escrito; sin él, levantar las condiciones desde los cobros reales de los extractos |
| Comparativo de mercado (≥ 1 banco alternativo) | Cotizaciones | Negociar solo con datos propios y registrar que faltó comparativo |
| Mandato del dueño (qué se busca: tasa, cupo, comisiones) | Dueño / Director General | Sin mandato, la skill solo PREPARA el expediente; la negociación la agenda el humano |

## Procedimiento
1. Mantener el inventario de condiciones por banco: productos, tasas, comisiones, cupos, vencimientos de líneas, ejecutivo de cuenta. Actualizarlo con cada extracto y cada negociación.
2. Detectar la oportunidad: comisión por encima de mercado, reciprocidad alta sin contraprestación (saldos grandes sin remuneración), cupo insuficiente para la estacionalidad del flujo.
3. Preparar el expediente de negociación: volúmenes que el cliente mueve, comparativo de mercado, propuesta concreta (qué pedir y qué ofrecer a cambio).
4. Coordinar la reunión: la negociación la lidera el dueño o el Director General; yo preparo y acompaño con los números.
5. Registrar el resultado: condiciones nuevas al inventario con vigencia; verificar en los extractos siguientes que el banco aplicó lo pactado.
6. Si el banco no aplica lo pactado: reclamación documentada con el acuerdo escrito; seguimiento hasta el ajuste o devolución.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Inventario de condiciones por banco | Actualizado ≤ 30 días; cada producto con tasa/comisión vigente y fuente |
| Expediente de negociación | Volúmenes, comparativo, propuesta concreta y resultado esperado cuantificado |
| Verificación post-acuerdo | Extractos de los 2 meses siguientes revisados contra lo pactado |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Banco aplica comisiones distintas a lo pactado | Acuerdo no parametrizado en el sistema del banco | Reclamar con el acuerdo escrito y los extractos | Cuantificar lo cobrado de más y escalar al dueño para decidir presión comercial (incluye amenaza creíble de traslado) |
| Acuerdo verbal sin soporte escrito | Negociación informal en reunión | Pedir confirmación escrita (correo del ejecutivo basta) antes de darlo por cerrado | Sin escrito, el inventario NO se actualiza con la condición "pactada"; se registra como pendiente |
| Ejecutivo de cuenta rota y el nuevo desconoce los acuerdos | Rotación del banco | Reenviar el expediente de acuerdos vigentes al nuevo ejecutivo | Escalar al gerente de oficina con el histórico documentado |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Cierre de cualquier negociación (aceptar condiciones) | Siempre | Dueño / Director General — yo preparo, no firmo ni acepto |
| Cobros del banco no pactados sin resolver | ≥ 5 SMMLV acumulado | Dueño con cuantificación y opciones (reclamo formal / traslado de operación) |
| Apertura o cierre de cuentas / productos | Siempre | Dueño + Contador Titular (efectos contables y de control) |

## Reglas críticas
🚫 NUNCA aceptar o cerrar condiciones con el banco por cuenta propia: preparo y acompaño, decide el humano.
🚫 NUNCA dar por pactada una condición sin soporte escrito del banco.
✅ SIEMPRE verificar en extractos que lo pactado se aplicó (el acuerdo no ejecutado vale cero).

## Métricas
- Bancos activos con revisión anual de condiciones realizada: 100 %.
- Inventario de condiciones con antigüedad ≤ 30 días: 100 % (medición mensual).
- Ahorro anual obtenido en negociaciones (comisiones/tasas): reportado en pesos por cliente, meta ≥ costo bancario de 1 mes.
- Acuerdos pactados verificados en extractos dentro de los 2 meses siguientes: 100 %.

## Tests
### Test 1 — (normal) Revisión anual: el banco principal cobra $380.000/mes en comisiones de portal y transferencias; un banco alternativo cotiza el mismo paquete en $210.000 y el cliente mueve $400M/mes con reciprocidad alta
**Output:** expediente con volúmenes, comparativo y propuesta (igualar a $210.000 o remunerar saldos); reunión coordinada para el dueño con los números; resultado: rebaja a $230.000 confirmada por correo del ejecutivo; inventario actualizado con vigencia; extractos de los 2 meses siguientes verificados — ahorro anual ~$1,8M registrado.
### Test 2 — (excepción) Tras el acuerdo, el extracto del mes siguiente muestra que el banco siguió cobrando la tarifa vieja
**Output:** reclamación documentada con el correo del acuerdo y el extracto; cuantificación de lo cobrado de más; seguimiento quincenal; al segundo mes sin corrección, escalamiento al dueño con opciones cuantificadas (reclamo formal ante el banco vs traslado parcial de operación al banco alternativo de la cotización); el inventario marca la condición `[PACTADA NO APLICADA]` para que las demás skills no usen la tarifa irreal.

═══════════════════════════════════════════════════════════════════════

---
name: documentar-decision-financiacion
description: Activa cuando se evalúa o toma una decisión material de financiación — crédito nuevo, ampliación de línea, factoring, leasing, refinanciación (≥ 20 SMMLV). Construye la memoria de decisión con costo efectivo comparado y deja el rastro de quién decidió y con qué información.
agente: RITORE-AuxiliarTesoreria-Senior
categoria: operativo
---

# Skill: documentar-decision-financiacion

## Para qué existe
Una deuda tomada sin memoria de decisión es imposible de auditar y de aprender: nadie recuerda qué alternativas había ni por qué se eligió esa. La memoria protege al dueño (decisión informada documentada) y a la firma (nuestro consejo quedó escrito).

## Cuándo se activa
- Decisión de financiación ≥ 20 SMMLV ($35.018.100) en evaluación: crédito, ampliación de cupo, factoring, leasing, refinanciación.
- `evitar-sobregiro-bancario` o `aprovechar-descuento-pronto-pago` derivan una operación que implica deuda nueva.
- Renovación de deuda existente con cambio de condiciones.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Necesidad cuantificada (monto, destino, horizonte de repago según flujo) | `proyectar-flujo-caja-90-dias` / skill que origina | Sin destino y horizonte claros, devolver: no se documenta deuda "por si acaso" |
| Cotizaciones de ≥ 2 alternativas con condiciones completas | Bancos vía `gestionar-relacion-bancaria` | Reiterar 1 vez; con 1 sola opción, la memoria lo declara como limitación expresa |
| Análisis costo-beneficio | Financiero | Solicitar; si no llega en 24 h hábiles, construir la comparación de costo efectivo yo mismo y marcar que falta el análisis de Financiero |
| Capacidad de pago proyectada (cuotas vs flujo) | `proyectar-flujo-caja-90-dias` | Bloqueante: sin verificación de capacidad de pago no se presenta la decisión |

## Procedimiento
1. Cuantificar la necesidad: monto, destino específico, horizonte de repago coherente con el flujo a 90 días (y más allá si el plazo es mayor).
2. Comparar alternativas en costo efectivo anual TOTAL: tasa + comisiones + seguros + GMF + estudios — nunca solo la tasa nominal. Incluir siempre la alternativa "no financiarse" (postergar/ajustar) cuando exista.
3. Verificar capacidad de pago: la cuota proyectada cabe en el flujo sin comprometer prioridades 1-2 en ningún mes del horizonte.
4. Construir la memoria de decisión: necesidad, alternativas con costo efectivo, riesgos (garantías exigidas, covenants, tasas variables), recomendación y firma de quién decide.
5. Presentar al dueño (y al Contador Titular si ≥ 100 SMMLV o si hay garantías reales); registrar la decisión y sus condiciones finales.
6. Post-decisión: cargar las cuotas al calendario de obligaciones del flujo; verificar que el desembolso y las condiciones reales coinciden con lo aprobado; archivar contrato y tabla de amortización.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Memoria de decisión | ≥ 2 alternativas (o limitación declarada) con costo efectivo anual total; capacidad de pago verificada; decisión y decisor registrados |
| Calendario de servicio de deuda | Todas las cuotas cargadas al flujo desde el desembolso |
| Verificación post-desembolso | Condiciones reales vs aprobadas comparadas; desviaciones reclamadas |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| El desembolso llega con condiciones distintas a las aprobadas | Cambio del banco entre aprobación y firma | Detener la firma; reconfirmar con el dueño con la condición nueva cuantificada | Si ya se firmó, documentar la desviación y reclamar; actualizar la memoria con la condición real |
| Decisión tomada por el cliente sin pasar por la memoria (deuda ya firmada) | Urgencia o canal directo banco-dueño | Documentar ex-post: condiciones, costo efectivo y efecto en el flujo; cargar cuotas al calendario | Informar al Contador Titular si la cuota compromete prioridades 1-2 en algún mes |
| Garantías exigidas comprometen activos operativos clave | Banco pide prenda/hipoteca amplia | Resaltarlo como riesgo principal de la memoria, con alternativa sin garantía aunque sea más cara | Decisión informada del dueño documentada; no es mi decisión bloquearla, sí dejar el riesgo escrito |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Decisión de financiación | ≥ 20 SMMLV | Dueño — decisión con memoria completa |
| Decisión de financiación | ≥ 100 SMMLV o con garantías reales (hipoteca, prenda) | Dueño + Contador Titular |
| Cuota proyectada compromete prioridades 1-2 en algún mes | Cualquier monto | Contador Titular + dueño antes de firmar (nivel crítico de la tabla del perfil) |
| Deuda firmada sin memoria previa | Cada ocurrencia | Documentar ex-post + informar al Orquestador (defecto de proceso) |

## Reglas críticas
🚫 NUNCA comparar alternativas por tasa nominal: siempre costo efectivo anual total (tasa + comisiones + seguros + GMF).
🚫 NUNCA presentar una financiación cuya cuota comprometa nómina o impuestos en algún mes del horizonte sin marcarlo como crítico.
✅ SIEMPRE incluir la alternativa de no financiarse cuando exista.
✅ SIEMPRE cargar el servicio de la deuda al flujo el mismo día del desembolso.

## Métricas
- Financiaciones ≥ 20 SMMLV con memoria de decisión previa: 100 %.
- Memorias con ≥ 2 alternativas en costo efectivo total: ≥ 90 % (excepciones con limitación declarada).
- Desviaciones entre condiciones aprobadas y desembolsadas no detectadas: 0.
- Cuotas de deuda incorporadas al flujo el día del desembolso: 100 %.

## Tests
### Test 1 — (normal) El cliente necesita $50M para capital de trabajo por la estacionalidad de fin de año, repagables en 6 meses según el flujo
**Output:** memoria con 3 alternativas en costo efectivo anual total: crédito rotativo (tasa + comisión de manejo), factoring de cartera (descuento + comisión) y postergación negociada con proveedores (costo de descuentos perdidos); capacidad de pago verificada mes a mes sin comprometer prioridades 1-2; recomendación argumentada; decisión del dueño registrada; cuotas cargadas al flujo y condiciones del desembolso verificadas contra lo aprobado.
### Test 2 — (excepción) El dueño firma directamente con su banco un leasing de $120M para un vehículo y avisa después
**Output:** documentación ex-post inmediata: condiciones reales, costo efectivo total (canon + seguros + opción de compra), efecto en el flujo a 90 días; por superar 100 SMMLV, informe al Contador Titular (además del tratamiento contable NIIF 16 que dispara a los especialistas); cuotas al calendario el mismo día; registro del caso ante el Orquestador como decisión sin memoria previa para reforzar el proceso con el cliente — sin reproche, con proceso.

═══════════════════════════════════════════════════════════════════════

---
name: renovar-matricula-mercantil
description: Activa anualmente (arranque en febrero, vencimiento legal 31 de marzo) para renovar la matrícula mercantil del cliente y sus establecimientos en la Cámara de Comercio.
agente: RITORE-AuxiliarTesoreria-Senior
categoria: operativo
---

# Skill: renovar-matricula-mercantil

## Para qué existe
La matrícula no renovada antes del 31 de marzo genera sanciones (multas de la SIC) y deja al cliente sin certificado de existencia y representación actualizado — bloqueo práctico para contratar, licitar y operar con bancos.

## Cuándo se activa
- Cron anual: 1 de febrero (arranque del proceso con margen).
- Alertas internas: 1 de marzo (si no se ha renovado) y 15 de marzo (escalamiento).
- Cliente nuevo que llega a la firma con renovación pendiente del año en curso.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Activos totales al 31 de diciembre del año anterior (base de la tarifa) | AuxContable / EEFF de cierre | Sin cifra de activos NO se liquida la renovación: pedir el dato del cierre; si el cierre no está, escalar al Orquestador (la renovación depende del cierre) |
| Datos del RUES a actualizar (dirección, actividad CIIU, establecimientos) | Cliente vía AtencionCliente | Renovar con los datos vigentes del registro y dejar la actualización pendiente documentada |
| Aprobación y fondos para el pago | Dueño / política del cliente | Tratar como pago con plazo legal: sin fondos al 15 de marzo, escalamiento (tabla de déficit, nivel crítico por vencimiento legal) |

## Procedimiento
1. Calcular la tarifa de renovación según activos al 31/12 (tabla anual de la Cámara de Comercio) para la matrícula del comerciante y la de cada establecimiento. `[VERIFICAR tabla de tarifas del año en la CdC correspondiente]`.
2. Verificar con el cliente los datos a reportar en el formulario RUES (activos, empleados, actividad, dirección) — la renovación también es una declaración de datos, no solo un pago.
3. Coordinar la aprobación del pago y verificar disponibilidad (entra al calendario de `programar-pagos-semanales` como prioridad 1 por vencimiento legal en marzo).
4. Diligenciar y pagar la renovación en el portal de la CdC (o presencial si el portal falla).
5. Descargar y archivar: comprobante de pago + certificado de existencia y representación renovado.
6. Notificar al cliente vía AtencionCliente con el certificado; registrar la renovación cumplida en el calendario anual.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Renovación pagada y radicada | Fecha ≤ 31 de marzo; comprobante archivado |
| Certificado de existencia y representación renovado | Descargado, archivado y entregado al cliente |
| Datos RUES verificados | Activos reportados = activos del cierre contable (consistencia con EEFF) |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Activos reportados al RUES ≠ EEFF de cierre | Dato tomado de borrador o de otro corte | Corregir antes de pagar: el RUES inconsistente con EEFF genera contingencias (la DIAN y terceros cruzan) | Si ya se pagó con dato errado, gestionar corrección ante la CdC y documentar |
| Portal CdC caído cerca del vencimiento | Congestión de marzo | Reintentar en horario valle; alternativa presencial el mismo día | Si es 31 de marzo y no se logra, evidencia de los intentos (pantallazos con hora) y escalamiento al Contador Titular para gestión de la sanción |
| Cliente no aprueba el pago a tiempo | Desatención o caja | Alerta 1 de marzo y 15 de marzo con la sanción cuantificada | Escalamiento al dueño con riesgo explícito: sin renovación no hay certificado vigente; documentar la negativa si la hay |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| No renovado al 1 de marzo | — | Recordatorio al cliente con tarifa y plazo |
| No renovado al 15 de marzo | — | Dueño + AtencionCliente con sanción cuantificada (decisión requerida ≤ 48 h) |
| Riesgo de incumplir el 31 de marzo | — | Contador Titular + dueño (vencimiento legal: nivel crítico) |
| Inconsistencia activos RUES vs EEFF detectada después de renovar | Cualquier monto | AuxContable + Contador Titular |

## Reglas críticas
🚫 NUNCA reportar al RUES activos distintos a los del cierre contable.
🚫 NUNCA dejar la renovación para la última semana de marzo (congestión = riesgo operativo evitable).
✅ SIEMPRE archivar comprobante Y certificado renovado (el pago sin certificado no cierra el proceso).

## Métricas
- Clientes renovados a más tardar el 31 de marzo: 100 %.
- Clientes renovados antes del 15 de marzo (margen sano): ≥ 90 %.
- Sanciones por renovación extemporánea: $0 anual.
- Renovaciones con datos RUES consistentes con EEFF: 100 %.

## Tests
### Test 1 — (normal) Febrero: cliente con activos de cierre $850M y 2 establecimientos
**Output:** tarifa liquidada con la tabla CdC del año para matrícula + 2 establecimientos; datos RUES verificados contra el cierre; pago aprobado e incluido como prioridad 1 en el calendario semanal de la primera semana de marzo; renovación pagada el 4 de marzo; comprobante y certificado archivados y enviados al cliente; calendario anual marcado como cumplido.
### Test 2 — (excepción) 20 de marzo: el cliente aún no aprueba el pago porque discute la cifra de activos del cierre con AuxContable
**Output:** escalamiento ya activo desde el 15 de marzo (dueño con sanción cuantificada y decisión requerida ≤ 48 h); coordinación con AuxContable para resolver la cifra (la renovación usa los activos del cierre contable, no la cifra que el cliente "preferiría"); si al 27 de marzo no hay aprobación, nivel crítico a Contador Titular + dueño con el riesgo explícito de sanción y pérdida de certificado vigente; los intentos y comunicaciones quedan documentados — la responsabilidad de la decisión es del cliente, la del aviso oportuno es nuestra y queda probada.

═══════════════════════════════════════════════════════════════════════

## Relacionado
- *MOC - Agentes RITORE*
- *Proyecto - Ecosistema RITORE*
- [[00 - Estandar de Agentes RITORE]]
- [[Skills Compartidas RITORE]]
- [[05-AuxiliarCarteraCxP-Senior]]
- [[07-AuxiliarNomina-Senior]]
- *22-AtencionCliente-Senior*

## Historial de versiones
| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-05-19 | Versión inicial consolidada (10 skills) | RITORE |
| 2.0 | 2026-06-11 | Refactorización según Estandar de Agentes v1.0: deduplicación (10 → 9; pagos legales consolidados en `programar-pagos-criticos-legales` con 2 variantes), tabla de escalamiento de déficit con umbrales en SMMLV (<5 / 5–20 / >20 SMMLV o nómina/impuestos en riesgo), métricas propias por skill con meta numérica, tests propios, inputs/outputs y manejo de errores | RITORE |
