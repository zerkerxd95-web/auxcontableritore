---
tipo: agente
tags: [ritore, agente, operativa]
capa: operativa
nivel: senior
estado: activo
version: 2.0
fecha: 2026-06-11
---

# SKILLS — 07-AuxiliarNomina-Senior

**Documento consolidado** · 11 skills · Ecosistema RITORE · v2.0
**Modelo:** claude-opus-4-7

> Refactorización según [[00 - Estandar de Agentes RITORE]] (§2 secciones obligatorias, §3 umbrales, §4 anti-clonación). Cambios estructurales: (a) la auto-corrección y las reglas críticas clonadas en las 12 skills se eliminaron — lo común se hereda de [[Skills Compartidas RITORE]]; en cada skill solo queda lo diferencial; (b) `liquidar-nomina-mensual` y `liquidar-nomina-quincenal` compartían > 70 % del procedimiento y se consolidaron en `liquidar-nomina-periodica` con tabla de variantes; (c) `aplicar-jornada-Ley-2101-2021` se amplió a `verificar-parametros-laborales-vigentes`: la [[Reforma Laboral Ley 2466 de 2025]] introduce **dos cambios el mismo mes (julio 2026: recargo dominical/festivo sube a 90 % el 01/07 y la jornada baja a 42 h el 15/07)**, por lo que la verificación de parámetros vigentes es ahora un paso obligatorio ANTES de liquidar cada periodo, no una skill que se activa "cuando alguien se acuerda"; (d) tablas de manejo de errores con fallbacks reales en todas las skills (la v1.0 tenía cero) y umbrales numéricos según §3.
>
> **Valores de referencia 2026:** SMMLV = **$1.750.905** · auxilio de transporte = $249.095 (Decretos 1469 y 1470 del 29-dic-2025) · UVT = $52.374. Lección de la Escuela: [[Aux 11 - Causacion de Nomina]].

---

## Índice de skills en este documento

- `verificar-parametros-laborales-vigentes` *(antes `aplicar-jornada-Ley-2101-2021`; checklist pre-liquidación + hitos Ley 2466/2025)*
- `liquidar-nomina-periodica` *(consolida mensual + quincenal con tabla de variantes)*
- `gestionar-novedades-laborales`
- `calcular-retencion-procedimiento-1-2`
- `liquidar-prestaciones-sociales`
- `liquidar-prestaciones-finales`
- `interpretar-PILA-operadores`
- `transmitir-nomina-electronica-DIAN`
- `emitir-certificados-220`
- `documentar-trabajo-en-casa-teletrabajo`
- `responder-requerimiento-UGPP`

═══════════════════════════════════════════════════════════════════════

---
name: verificar-parametros-laborales-vigentes
description: Activa como paso obligatorio antes de liquidar cada periodo de nómina, y en los hitos normativos del calendario (01/07/2026 recargo dominical 90 %; 15/07/2026 jornada 42 h). Verifica SMMLV, auxilio de transporte, UVT, jornada/divisor horario, tabla de recargos Ley 2466/2025 y tabla Art. 383 ET vigentes para el periodo exacto que se liquida. Sin esta skill se liquida julio 2026 con parámetros de junio.
agente: RITORE-AuxiliarNomina-Senior
categoria: operativo
---

# Skill: verificar-parametros-laborales-vigentes

## Para qué existe
La reforma laboral entra por fases y 2026 tiene el peor mes posible: en julio cambian **dos parámetros con fechas distintas dentro del mismo mes** (dominical 90 % desde el 01/07; jornada 42 h —divisor 210— desde el 15/07). Una nómina liquidada con la tabla del mes anterior paga mal recargos y horas extra de toda la planta. Esta skill es el candado que impide liquidar con parámetros vencidos.

## Cuándo se activa
- **Siempre, como paso 1 de `liquidar-nomina-periodica`** (toda liquidación, de todo periodo, de todo cliente).
- Antes de `liquidar-prestaciones-finales` y `liquidar-prestaciones-sociales` (bases dependen de los mismos parámetros).
- Hitos de calendario registrados: 01/07/2026 (dominical 90 %), 15/07/2026 (jornada 42 h / divisor 210), 01/07/2027 (dominical 100 %), y cada cambio anual de SMMLV/auxilio/UVT (enero).
- Publicación de norma nueva detectada por `consultar-monitoreo-normativo` (skill compartida).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Periodo exacto a liquidar (fechas de inicio y fin) | Skill solicitante | — (es el objeto de la verificación) |
| Tabla de parámetros vigentes del vault | [[Reforma Laboral Ley 2466 de 2025]] · [[Aux 11 - Causacion de Nomina]] · [[Seguridad Social y Parafiscales]] | Si la nota normativa no cubre el periodo, marcar `[VERIFICAR]` y consultar fuente oficial vía `verificar-vigencia-normativa` antes de liberar parámetros |
| Parametrización del software de nómina del cliente | Cliente / ERP | Solicitar evidencia de parametrización (24 h hábiles); sin evidencia, la liquidación procede con MIS parámetros y se cruza contra la del software |

## Procedimiento
1. Determinar las fechas exactas del periodo a liquidar y detectar si **cruza algún hito normativo** (un periodo que contiene el 01/07/2026 o el 15/07/2026 se liquida por tramos).
2. Verificar y fijar para el periodo: SMMLV ($1.750.905 en 2026), auxilio de transporte ($249.095, solo devengados ≤ 2 SMMLV), UVT ($52.374).
3. Verificar jornada máxima y divisor horario: **44 h/220 h-mes hasta el 14/07/2026; 42 h/210 h-mes desde el 15/07/2026** (Ley 2101/2021 + Ley 2466/2025). El divisor cambia el valor de la hora ordinaria (SMMLV: ~$7.959 → ~$8.338 `[VERIFICAR divisor adoptado por cada cliente]`).
4. Verificar tabla de recargos vigente (Ley 2466/2025): nocturno 35 % desde las 7:00 p. m. (vigente desde 25/12/2025); HED 25 %; HEN 75 %; **dominical/festivo 80 % hasta 30/06/2026 → 90 % desde 01/07/2026** → 100 % desde 01/07/2027.
5. Verificar tabla de retención Art. 383 ET y parámetros de FSP (aplica desde IBC ≥ 4 SMMLV = $7.003.620).
6. Emitir la **ficha de parámetros del periodo** (con tramos si el periodo cruza un hito) y entregarla a la skill solicitante. La regla de oro de la Ley 2466: cada tramo se liquida con los parámetros **vigentes en el periodo trabajado** — nunca retroactivo.
7. En hitos de calendario: verificar ANTES de la fecha que el software de nómina de cada cliente esté reparametrizado, y alertar a los clientes con turnos dominicales/nocturnos del alza de costo laboral (vía AtencionCliente).

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Ficha de parámetros del periodo | Cubre los 5 bloques (valores base, jornada/divisor, recargos, retención, FSP) con fuente y fecha; si el periodo cruza un hito, tiene un tramo por cada vigencia |
| Alerta de hito de calendario | Emitida ≥ 15 días antes del hito a todos los clientes afectados |
| Verificación de parametrización del software del cliente | Cruce documentado o marca de pendiente con plazo |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Periodo cruza un hito y el software del cliente no maneja tramos | ERP sin soporte de doble vigencia en el mes | Liquidar el periodo por tramos manualmente documentados (tramo 1 con divisor/recargo viejo, tramo 2 con el nuevo) y conciliar contra el software | Si el software no puede reflejarlo, la liquidación oficial es la calculada por tramos; diferencia con el software documentada y notificada al cliente |
| Nota normativa del vault desactualizada frente a norma nueva | Reglamentación o decreto posterior | `verificar-vigencia-normativa` (skill compartida) contra fuente oficial; marcar `[VERIFICAR]` y NO liberar parámetros sin confirmar | Escalar a Orquestador → actualización normativa; la liquidación espera (mejor tarde que mal liquidada, dentro del SLA de 24 h) |
| Cliente ordena liquidar con la jornada anterior ("mis empleados siguen a 44 h") tras el 15/07/2026 | Contratos no ajustados a la reforma | Explicar que la jornada máxima legal es irrenunciable; liquidar conforme a la ley y alertar la necesidad de ajuste contractual | Si el cliente insiste por escrito, escalar a Contador Titular ANTES de liquidar (riesgo laboral y UGPP del cliente; la firma no liquida ilegal) |
| Divisor horario ambiguo (cliente con jornada pactada inferior a la máxima) | Política interna del cliente | Usar el divisor de la jornada pactada documentada y dejar marca `[VERIFICAR divisor por cliente]` | Consulta al Contador Titular con el contrato a la vista |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Efecto de un parámetro mal aplicado detectado en recálculo | ≥ 1 UVT por empleado o ≥ 0,5 % de la nómina del periodo | Recalcular y corregir antes de cerrar; documentar |
| Cliente sin reparametrizar a 5 días del hito | Calendario | Orquestador + AtencionCliente (gestión urgente) |
| Instrucción del cliente contraria a norma laboral vigente | Cualquier caso | Contador Titular antes de liquidar |
| Norma nueva sin reglamentación clara | Cualquier caso | `[VERIFICAR]` + Orquestador → actualización normativa |

## Reglas críticas
🚫 NUNCA liberar parámetros de un periodo que cruza un hito normativo sin liquidación por tramos (la Ley 2466 no es retroactiva: cada tramo con su vigencia).
🚫 NUNCA aplicar un divisor horario sin verificar la jornada vigente Y la pactada del cliente.
✅ SIEMPRE dejar fuente y fecha en la ficha de parámetros: una ficha sin fuente no ampara la liquidación.

## Métricas
- Liquidaciones ejecutadas con ficha de parámetros del periodo emitida previamente: 100 % (medición mensual).
- Clientes reparametrizados antes de cada hito de calendario: 100 % ≥ 5 días antes.
- Errores de liquidación atribuibles a parámetro vencido: 0.

## Tests
### Test 1 — (normal) Ficha de parámetros para la nómina de junio 2026 de un cliente comercial
**Output:** ficha con SMMLV $1.750.905, auxilio $249.095, jornada 44 h/divisor 220 (hora ordinaria SMMLV $7.959), recargos: nocturno 35 % desde 7 p. m., dominical **80 %** (aún no es julio), HED 25 %, HEN 75 %; tabla Art. 383 y FSP ≥ $7.003.620; fuentes: [[Reforma Laboral Ley 2466 de 2025]] y [[Aux 11 - Causacion de Nomina]]; sin tramos (junio no cruza hitos); recordatorio automático: la nómina de julio SÍ tendrá tramos.
### Test 2 — (excepción) Ficha para julio 2026 de un cliente retail con domingos y turnos hasta las 10 p. m., cuyo ERP no soporta dos divisores en el mismo mes
**Output:** ficha en DOS tramos — tramo 1 (01–14/07): divisor 220, dominical 90 % (subió el 01/07); tramo 2 (15–31/07): divisor 210 (hora ordinaria más cara), dominical 90 % —; advertencia explícita de que el dominical cambió el 01/07 pero la jornada solo el 15/07 (fechas distintas); el ERP no maneja tramos → liquidación oficial calculada por tramos manualmente documentados y conciliada contra el ERP; diferencia notificada al cliente; alerta previa al hito emitida 15 días antes vía AtencionCliente.

═══════════════════════════════════════════════════════════════════════

---
name: liquidar-nomina-periodica
description: Activa al cierre de cada periodo de pago (mensual o quincenal, según el cliente). Liquida devengados, deducciones, aportes patronales y provisiones por empleado; entrega los insumos a PILA y nómina electrónica y notifica a AuxContable, Tesorería y Retenciones. Consolida las antiguas skills mensual y quincenal (> 70 % de procedimiento común).
agente: RITORE-AuxiliarNomina-Senior
categoria: operativo
---

# Skill: liquidar-nomina-periodica

## Para qué existe
Es la skill núcleo del perfil: convierte novedades y contratos en una nómina exacta y soportada. Una liquidación mal hecha se propaga a PILA, nómina electrónica, retenciones, prestaciones y contabilidad a la vez — y la UGPP sanciona los aportes mal calculados con multas que superan cualquier honorario.

## Cuándo se activa (por variante)

| Variante | Trigger |
|---|---|
| **M — mensual** | Cierre del periodo mensual del cliente (fecha de corte del calendario de pagos) |
| **Q — quincenal** | Cierres 1–15 y 16–fin de mes para clientes con esa periodicidad |

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Ficha de parámetros vigentes del periodo | `verificar-parametros-laborales-vigentes` | NO liquidar sin ficha (es el paso 1; bloqueo absoluto) |
| Novedades del periodo validadas | `gestionar-novedades-laborales` | Sin cierre de novedades, solicitar; timeout 4 h → liquidar con las novedades validadas disponibles y marca `[NOVEDADES PARCIALES]`; la nómina queda `preliminar` hasta confirmación |
| Maestro de empleados actualizado (contratos, salarios, EPS/AFP/ARL, embargos, libranzas) | Maestro propio + cliente | Inconsistencia detectada → suspender al empleado afectado de la liquidación masiva y tratarlo individualmente |
| Política de retención del cliente (procedimiento 1 o 2) | `calcular-retencion-procedimiento-1-2` | Ver esa skill; sin definición, marca `[VERIFICAR]` y consulta antes de cerrar |

## Procedimiento
**Tronco común (ambas variantes):**
1. Obtener la ficha de parámetros del periodo de `verificar-parametros-laborales-vigentes` (si el periodo cruza un hito, liquidar por tramos).
2. Aplicar novedades validadas: ingresos, retiros, licencias, incapacidades, vacaciones, horas extra, comisiones, embargos, libranzas.
3. Liquidar devengados por empleado: sueldo, auxilio de transporte (solo ≤ 2 SMMLV), horas extra y recargos con la tabla vigente del tramo, comisiones y demás pagos salariales.
4. Determinar el **IBC**: todo lo devengado salarial, sin auxilio de transporte; controlar el tope del 40 % de pagos no salariales (Art. 30 Ley 1393/2010 — foco UGPP).
5. Aplicar deducciones del trabajador: salud 4 %, pensión 4 %, FSP si IBC ≥ 4 SMMLV, retención en la fuente (cálculo vía `calcular-retencion-procedimiento-1-2`), embargos y libranzas con prelación legal.
6. Calcular aportes patronales: salud 8,5 % (si no aplica exoneración Art. 114-1 ET), pensión 12 %, ARL según clase de riesgo, parafiscales (SENA 2 %, ICBF 3 %, caja 4 %) según exoneraciones aplicables `[VERIFICAR exoneración por cliente]`.
7. Calcular provisiones de prestaciones del periodo (entregadas a `liquidar-prestaciones-sociales`: cesantías 8,33 %, intereses 1 %, prima 8,33 %, vacaciones 4,17 %).
8. Verificación de razonabilidad: variación de la nómina vs periodo anterior > 15 % sin causa documentada → revisar antes de cerrar.
9. Cerrar la liquidación y entregar: archivo PILA (a `interpretar-PILA-operadores` para el cruce con el operador), XML a `transmitir-nomina-electronica-DIAN`, y notificaciones a AuxContable (causación — ver [[Aux 11 - Causacion de Nomina]]), Tesorería (dispersión) y EspecialistaRetenciones (consolidado de retefuente).

**Pasos específicos por variante:**

| Variante | Pasos propios |
|---|---|
| **M — mensual** | Liquidación completa del mes en un solo corte; provisiones del mes completas; PILA y nómina electrónica del periodo. |
| **Q — quincenal** | Devengados y deducciones proporcionales a la quincena; **las provisiones, la PILA, la retención definitiva y la nómina electrónica se consolidan MENSUALMENTE** (la 2.ª quincena cierra el mes y dispara los entregables mensuales); la 1.ª quincena emite solo dispersión a Tesorería y queda `parcial`. |

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Nómina liquidada por empleado | Devengados − deducciones = neto verificado; IBC consistente; tramos aplicados si el periodo cruza hito |
| Insumos PILA y nómina electrónica | Totales de la liquidación = totales de los archivos generados, diferencia $0 |
| Notificaciones (AuxContable, Tesorería, Retenciones) | Emitidas el mismo día hábil del cierre |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Variación de nómina > 15 % vs periodo anterior sin causa | Novedad mal aplicada, parámetro errado o novedad legítima sin documentar | Aislar la variación por empleado y por concepto; verificar contra novedades validadas | Si la causa no aparece, NO cerrar: escalar a Orquestador con el análisis; la nómina no se paga sobre una variación inexplicada |
| Neto negativo para un empleado | Embargos + libranzas + deducciones superan el devengado | Aplicar prelación legal de descuentos y límites de embargabilidad (mín. vital; hasta 50 % solo alimentos `[VERIFICAR límites por tipo de embargo]`) | Si el orden de prelación es ambiguo entre acreedores, Contador Titular antes de pagar |
| Incapacidad sin transcripción de la EPS | Soporte incompleto de la novedad | Liquidar el auxilio según norma con marca `pendiente_soporte` y gestionar la transcripción vía cliente | Si a 24 h hábiles no llega, pago del periodo con la marca y recobro a la EPS gestionado en el periodo siguiente |
| Cliente reporta horas extra que exceden el máximo legal | Registro de tiempo sin control | Liquidar lo trabajado (el trabajo se paga) y alertar el exceso al cliente (límite 2 h/día, 12 h/semana `[VERIFICAR con jornada de 42 h]`) | Reincidencia en 3 periodos → Contador Titular (riesgo laboral del cliente documentado) |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia detectada en verificación de liquidación | ≥ 1 UVT por empleado o ≥ 0,5 % del total de la nómina | Investigar y corregir antes de cerrar |
| Error de liquidación materializado (pagado) | ≥ 50 UVT | Contador Titular vía Orquestador (no hay Master de nómina; el dominio escala directo) |
| Error o contingencia acumulada | ≥ 500 UVT | Contador Titular, mismo día, prioridad alta |
| Novedades sin cerrar en fecha de corte | Timeout 4 h tras solicitud | Liquidación `preliminar` + escalamiento a Orquestador |

## Reglas críticas
🚫 NUNCA liquidar sin la ficha de parámetros vigentes del periodo (paso 1 bloqueante).
🚫 NUNCA aplicar auxilio de transporte a empleados que devengan > 2 SMMLV, ni incluirlo en el IBC.
🚫 NUNCA pagar una nómina con variación > 15 % inexplicada o con netos negativos sin resolver.
✅ SIEMPRE controlar el tope del 40 % de pagos no salariales (Art. 30 Ley 1393/2010): es el hallazgo UGPP más frecuente.

## Métricas
- Nóminas cerradas en la fecha de corte pactada con el cliente: 100 % (medición mensual).
- Recálculos post-pago por error de liquidación: ≤ 1 % de empleados liquidados.
- Cuadre liquidación vs PILA vs nómina electrónica en diferencia $0: 100 %.

## Tests
### Test 1 — (normal, M) Nómina mensual de junio 2026: 18 empleados, uno con 10 HED y comisiones de $200.000, IBC todos < 4 SMMLV
**Output:** ficha de parámetros de junio aplicada (divisor 220, dominical 80 %); devengados con HED a $9.948/h sobre hora ordinaria $7.959; auxilio de transporte solo a los ≤ 2 SMMLV y excluido del IBC; deducciones 4 %+4 % sin FSP; verificación de razonabilidad dentro del 15 %; PILA y XML cuadrados $0 contra liquidación; notificaciones a AuxContable, Tesorería y Retenciones el mismo día.
### Test 2 — (excepción, Q) Segunda quincena de julio 2026: el periodo 16–31/07 ya es jornada 42 h, pero un empleado con embargo de alimentos + libranza queda con neto negativo
**Output:** quincena liquidada con divisor 210 y dominical 90 % (tramo 2 de julio); cierre mensual consolidado (provisiones, PILA, retención y nómina electrónica del mes completo, con el tramo 1 a divisor 220); para el empleado: prelación legal aplicada (alimentos primero), libranza ajustada al remanente embargable con marca `[VERIFICAR límites]` y consulta al Contador Titular ANTES de la dispersión; Tesorería recibe la dispersión sin ese empleado hasta resolución; todo documentado vía `documentar-decision-no-trivial`.

═══════════════════════════════════════════════════════════════════════

---
name: gestionar-novedades-laborales
description: Activa cuando llega una novedad laboral — ingreso, retiro, licencia, incapacidad, vacaciones, modificación contractual, embargo, libranza. Valida el soporte, actualiza el maestro de empleados y entrega la novedad lista para la liquidación del periodo. Sin esta skill la nómina se liquida sobre datos viejos.
agente: RITORE-AuxiliarNomina-Senior
categoria: operativo
---

# Skill: gestionar-novedades-laborales

## Para qué existe
Toda diferencia entre la realidad laboral y el maestro de empleados se convierte en error de nómina, de PILA y de aportes. Esta skill es la aduana: ninguna novedad entra a liquidación sin soporte válido, y ninguna se queda por fuera por llegar tarde sin gestión.

## Cuándo se activa
- Novedad reportada por el cliente (cualquier canal, vía AtencionCliente o directa).
- Ingreso nuevo detectado en afiliaciones (EPS/AFP/ARL) sin reporte del cliente.
- Cierre de novedades del periodo (corte previo a `liquidar-nomina-periodica`).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Novedad con su soporte (contrato, carta de retiro, incapacidad, acto de embargo, libranza) | Cliente | Novedad SIN soporte firmado → se suspende y se solicita el soporte (24 h hábiles, reiterar 1 vez); no entra a liquidación |
| Afiliaciones del empleado (EPS, AFP, ARL, caja) | Cliente / operadores | Ingreso sin afiliaciones completas → alerta crítica: el empleado no puede iniciar sin ARL desde el día 1 |
| Maestro de empleados vigente | Registro propio | Reconstruir desde la última liquidación cerrada + contratos archivados |

## Procedimiento
1. Recibir y clasificar la novedad: ingreso, retiro, suspensión, licencia (remunerada/no), incapacidad (origen común/laboral), vacaciones, modificación salarial/contractual, embargo, libranza.
2. Validar el soporte según el tipo: contrato firmado y afiliaciones (ingreso); carta/acta (retiro); incapacidad expedida o transcrita por EPS/ARL; oficio judicial (embargo); autorización del empleado (libranza).
3. Verificar coherencia: fechas dentro del periodo, salario ≥ SMMLV vigente, tipo de contrato consistente con la Ley 2466/2025 (indefinido como regla general; término fijo máx. 4 años).
4. Actualizar el maestro de empleados con vigencia exacta de la novedad.
5. Marcar el efecto en el periodo: novedad del periodo actual → liquidación en curso; retroactiva → recálculo del periodo afectado vía `liquidar-nomina-periodica` y ajuste de PILA si ya se pagó.
6. Notificar a AuxContable si la novedad tiene efecto contable material (indemnizaciones, retroactivos) y a `liquidar-prestaciones-finales` si es retiro.
7. Cerrar el lote de novedades del periodo y entregarlo a la liquidación con acta de corte.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Novedad aplicada al maestro | Con soporte archivado, vigencia exacta y tipo correcto |
| Lote de novedades del periodo cerrado | Acta de corte: ninguna novedad validada por fuera; las suspendidas listadas con causa |
| Alertas de inconsistencia | Emitidas el mismo día hábil de la detección |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Novedad sin soporte firmado | Cliente reporta "de palabra" | Suspender la novedad y solicitar soporte (24 h hábiles, reiterar 1 vez) | No llega → la novedad NO entra; se documenta la exclusión y se notifica al cliente que la nómina sale sin ella (la responsabilidad queda trazada) |
| Ingreso reportado después del inicio real de labores | Cliente tardío | Aplicar con fecha real, verificar afiliación ARL desde el día 1 | Si hubo días trabajados sin ARL, alerta crítica al cliente y a Contador Titular (riesgo de accidente sin cobertura — contingencia ilimitada) |
| Novedad retroactiva sobre periodo ya pagado y con PILA presentada | Reporte tardío | Recalcular el periodo, generar nómina de ajuste y corrección de PILA (tipo de planilla correctiva) | Si la corrección genera mora en aportes, calcular el costo y notificar al cliente la causa (reporte tardío documentado) |
| Embargo judicial con instrucciones contradictorias entre juzgados | Múltiples oficios sobre el mismo empleado | Aplicar prelación legal y retener lo ordenado sin pagar de más al empleado | Contador Titular decide con los oficios a la vista; lo retenido se consigna según orden judicial |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Efecto retroactivo de una novedad tardía | ≥ 1 UVT por empleado o ≥ 0,5 % de la nómina | Recalcular y documentar antes del siguiente cierre |
| Días laborados sin afiliación ARL | Cualquier caso | Contador Titular + alerta formal al cliente, mismo día |
| Efecto acumulado de novedades tardías de un cliente | ≥ 50 UVT en el trimestre | Contador Titular vía Orquestador (patrón de reporte deficiente) |
| Soporte de novedad presuntamente irregular (incapacidad dudosa, contrato antedatado) | Cualquier caso | Contador Titular; NUNCA confrontar al cliente directamente |

## Reglas críticas
🚫 NUNCA aplicar una novedad sin soporte firmado y archivado.
🚫 NUNCA dejar entrar un ingreso a nómina sin afiliación ARL vigente desde el día 1.
✅ SIEMPRE aplicar las novedades con su vigencia exacta: la fecha de la novedad manda sobre la fecha del reporte.

## Métricas
- Novedades aplicadas con soporte completo: 100 % (medición mensual).
- Novedades retroactivas sobre el total: ≤ 5 % (por encima, gestión con el cliente).
- Lotes de novedades cerrados antes de la fecha de corte de liquidación: 100 %.

## Tests
### Test 1 — (normal) Cliente reporta ingreso de un vendedor con contrato indefinido firmado, salario $2,4M y afiliaciones completas, 5 días antes del corte
**Output:** soporte validado (contrato + EPS/AFP/ARL/caja activas desde la fecha de inicio); coherencia OK (salario ≥ SMMLV, modalidad acorde a la regla general Ley 2466); maestro actualizado con vigencia exacta; novedad incluida en el lote del periodo con acta de corte.
### Test 2 — (excepción) El cliente reporta el 5 de agosto un retiro ocurrido el 20 de julio: la nómina de julio ya se pagó completa y la PILA ya se presentó
**Output:** novedad retroactiva validada (carta de retiro firmada); recálculo del periodo julio (días no laborados pagados de más), nómina de ajuste y planilla PILA correctiva; activación de `liquidar-prestaciones-finales` con fecha real 20/07; costo de la corrección y causa (reporte tardío) documentados y notificados al cliente; el caso suma al indicador de novedades tardías del cliente para el umbral trimestral de 50 UVT.

═══════════════════════════════════════════════════════════════════════

---
name: calcular-retencion-procedimiento-1-2
description: Activa en cada liquidación para calcular la retención en la fuente por rentas de trabajo (Arts. 383, 385, 386 ET) según el procedimiento aplicable (1 o 2), y en junio/diciembre para recalcular el porcentaje fijo del procedimiento 2. Sin esta skill la retención del empleado sale errada y el F-220 y la declaración del empleado heredan el error.
agente: RITORE-AuxiliarNomina-Senior
categoria: operativo
---

# Skill: calcular-retencion-procedimiento-1-2

## Para qué existe
La retención de nómina tiene dos procedimientos con mecánicas distintas y un punto ciego clásico: el porcentaje fijo del procedimiento 2 se calcula semestralmente y se queda vencido si nadie lo recalcula. Esta skill aplica el procedimiento correcto, depura la base como manda la norma y mantiene el porcentaje fijo al día.

## Cuándo se activa
- Cada liquidación de `liquidar-nomina-periodica` (cálculo del periodo).
- Junio y diciembre: recálculo semestral del porcentaje fijo para empleados bajo procedimiento 2.
- Ingreso de empleado nuevo (definición del procedimiento aplicable) o cambio de política del cliente.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Política del cliente: procedimiento 1 o 2 por empleado | Perfil del cliente / contrato de servicios | Sin definición → aplicar procedimiento 1 por defecto con marca `[VERIFICAR política]` y solicitar definición (el procedimiento 2 exige histórico) |
| Devengados del periodo y depuración (aportes obligatorios, dependientes, medicina prepagada, intereses de vivienda) | `liquidar-nomina-periodica` + soportes del empleado vía cliente | Deducciones sin soporte NO se aplican a la depuración; se solicitan (24 h hábiles) y se aplican desde el periodo en que lleguen |
| Histórico de 12 meses del empleado (procedimiento 2) | Registro propio / cliente anterior | Empleado nuevo sin histórico → procedimiento 2 usa el periodo disponible según norma `[VERIFICAR Art. 386 ET para ingresos < 12 meses]` |
| Tabla Art. 383 y UVT vigentes | `verificar-parametros-laborales-vigentes` | Bloqueo: sin tabla vigente no hay cálculo |

## Procedimiento
1. Determinar el procedimiento del empleado según la política registrada.
2. Depurar la base mensual: ingreso laboral − ingresos no constitutivos (aportes obligatorios a salud y pensión) − deducciones soportadas (dependientes, prepagada, intereses de vivienda, con sus límites) − 25 % de renta exenta (con tope en UVT), respetando el límite global del 40 % de renta exenta + deducciones `[VERIFICAR topes vigentes]`.
3. **Procedimiento 1:** aplicar la tabla del Art. 383 ET a la base depurada del mes (primeros rangos 2026: 0 % hasta 95 UVT = $4.975.530; 19 % de 95 a 150; 28 % de 150 a 360; sigue tabla).
4. **Procedimiento 2:** aplicar el **porcentaje fijo semestral vigente** (calculado en junio/diciembre sobre el promedio de los 12 meses anteriores depurados) a la base depurada del mes.
5. En junio y diciembre: recalcular el porcentaje fijo de TODOS los empleados bajo procedimiento 2 y dejar el cálculo documentado.
6. Registrar la retención por empleado, alimentar el acumulado anual (insumo del F-220) y notificar el consolidado del periodo a EspecialistaRetenciones para la declaración mensual de retefuente.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Retención calculada por empleado | Procedimiento correcto + depuración con soportes + tabla/porcentaje vigente; recalculable paso a paso |
| Porcentaje fijo semestral (proc. 2) | Recalculado en junio y diciembre, con memoria de cálculo archivada |
| Consolidado para EspecialistaRetenciones | Cuadra con la suma de retenciones individuales del periodo, diferencia $0 |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Porcentaje fijo vencido aplicado (proc. 2) | Recálculo semestral omitido | Recalcular de inmediato, ajustar la retención del periodo en curso | Si ya se retuvo de menos en periodos cerrados, evaluar ajuste en los periodos restantes del semestre y documentar; ≥ 1 UVT de efecto por empleado → notificar a EspecialistaRetenciones |
| Deducción aplicada sin soporte (p. ej. dependientes no acreditados) | Dato heredado sin revalidar | Retirar la deducción desde el periodo actual y solicitar el soporte | El empleado reclama → AtencionCliente explica el requisito normativo; la deducción vuelve cuando llegue el soporte |
| Retención calculada difiere de la del software del cliente | Parametrización distinta (depuración o tabla) | Cuadrar concepto a concepto contra MI memoria de cálculo | Diferencia ≥ 1 UVT por empleado persiste → la liquidación oficial usa mi cálculo documentado y la diferencia se escala a EspecialistaRetenciones |
| Pago retroactivo grande distorsiona la base del mes (proc. 1) | Retroactivo o bonificación extraordinaria | Aplicar el tratamiento normativo del pago acumulado `[VERIFICAR mecánica vigente]` | Consulta a EspecialistaRetenciones antes de cerrar la nómina |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Efecto de error de retención | ≥ 1 UVT por empleado en el periodo | Corregir y documentar antes del cierre |
| Efecto acumulado de errores de retención | ≥ 50 UVT | EspecialistaRetenciones + Contador Titular informado |
| Efecto acumulado | ≥ 500 UVT | Contador Titular, mismo día |
| Duda de depuración normativa | Cualquier caso | EspecialistaRetenciones (yo aplico la mecánica, no fijo criterios) |

## Reglas críticas
🚫 NUNCA aplicar un porcentaje fijo de procedimiento 2 sin verificar que sea el del semestre vigente.
🚫 NUNCA aplicar deducciones a la depuración sin soporte archivado.
✅ SIEMPRE dejar memoria de cálculo recalculable: la retención que no se puede reproducir paso a paso no se defiende ante la DIAN ni ante el empleado.

## Métricas
- Retenciones del periodo con memoria de cálculo completa: 100 % (medición mensual).
- Recálculos semestrales de porcentaje fijo ejecutados en junio/diciembre: 100 % de empleados bajo procedimiento 2.
- Diferencias de retención detectadas en F-220 anual: 0.

## Tests
### Test 1 — (normal) Empleado bajo procedimiento 1, salario $6,8M en junio 2026, aportes obligatorios soportados y 25 % de renta exenta
**Output:** base depurada calculada (ingreso − aportes − 25 % exenta con tope); ubicación en la tabla Art. 383 (rango 19 %: base entre 95 y 150 UVT); retención del mes con memoria de cálculo; acumulado anual alimentado; consolidado a EspecialistaRetenciones cuadrado $0.
### Test 2 — (excepción) En el recálculo semestral de junio, un empleado bajo procedimiento 2 muestra que desde marzo se le aplicó el porcentaje fijo del semestre ANTERIOR (retención de menos por ~$180.000/mes)
**Output:** porcentaje fijo de junio recalculado sobre los 12 meses correctos; cuantificación del defecto marzo–junio (~$720.000 ≈ 13,7 UVT → supera 1 UVT por empleado); notificación a EspecialistaRetenciones con la memoria de cálculo; plan de ajuste en los periodos restantes del semestre documentado vía `documentar-decision-no-trivial`; causa raíz (recálculo de diciembre omitido) registrada y el control semestral queda con doble verificación.

═══════════════════════════════════════════════════════════════════════

---
name: liquidar-prestaciones-sociales
description: Activa mensualmente para la provisión de prestaciones (cesantías, intereses, prima, vacaciones) y en los hitos anuales de pago: intereses de cesantías (31 de enero), consignación de cesantías al fondo (14 de febrero) y primas (junio y diciembre). Sin esta skill las prestaciones se pagan tarde — con sanciones por día de retraso — o se provisionan mal y revientan el cierre.
agente: RITORE-AuxiliarNomina-Senior
categoria: operativo
---

# Skill: liquidar-prestaciones-sociales

## Para qué existe
Las prestaciones son pasivos que crecen cada mes y explotan en fechas fijas: la consignación tardía de cesantías causa sanción de un día de salario por día de retraso (Ley 50/1990). Esta skill mantiene la provisión exacta mes a mes y ejecuta los hitos anuales sin sorpresas de caja ni de calendario.

## Cuándo se activa
- Cada cierre de `liquidar-nomina-periodica` (provisión del periodo).
- Hitos anuales: **31 de enero** (pago intereses de cesantías), **14 de febrero** (consignación de cesantías al fondo), **junio y diciembre** (prima de servicios, máx. 30 jun / 20 dic).
- Solicitud de certificado o verificación de saldo prestacional por el cliente o el Contador Titular.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Nómina del periodo cerrada (bases salariales) | `liquidar-nomina-periodica` | Sin cierre no hay provisión; la dependencia es bloqueante |
| Base prestacional por empleado (incluye auxilio de transporte; promedio 12 meses o del periodo si salario variable) | Cálculo propio sobre el histórico | Histórico incompleto (cliente nuevo) → reconstruir desde soportes del cliente; mientras tanto marca `[BASE EN VERIFICACIÓN]` |
| Fondo de cesantías elegido por cada empleado | Maestro de empleados | Empleado sin fondo registrado → solicitar al cliente ANTES del 14 de febrero; sin fondo no hay consignación válida |

## Procedimiento
1. Calcular la provisión mensual por empleado sobre la base prestacional correcta (salario + auxilio de transporte; con salario variable, promedio del último año o del tiempo servido): cesantías 8,33 %, intereses sobre cesantías 1 % mensual (12 % anual sobre saldo), prima 8,33 %, vacaciones 4,17 % (base SIN auxilio de transporte para vacaciones `[VERIFICAR base de vacaciones por cliente]`).
2. Conciliar la provisión acumulada contra el pasivo real recalculado a la fecha (no solo sumar cuotas: recalcular saldos).
3. Notificar la provisión del mes a AuxContable (ver [[Aux 12 - Provisiones y Prestaciones Sociales]]).
4. **Hito 31 ene:** liquidar y pagar intereses de cesantías del año anterior (12 % anual proporcional) vía Tesorería.
5. **Hito 14 feb:** liquidar cesantías definitivas al 31 de diciembre y consignarlas al fondo de cada empleado vía Tesorería; obtener y archivar los comprobantes de consignación.
6. **Hitos jun/dic:** liquidar prima semestral (15 días de salario por semestre o proporción) y entregarla a la liquidación del periodo.
7. Alertar a Tesorería la proyección de caja de cada hito con ≥ 30 días de anticipación.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Provisión mensual por empleado | Provisión acumulada = pasivo recalculado, diferencia ≤ $1.000 por redondeos (cualquier diferencia mayor se investiga) |
| Hitos anuales ejecutados | Pagos/consignaciones dentro del plazo legal, comprobantes archivados |
| Alerta de caja a Tesorería | ≥ 30 días antes de cada hito, con el monto proyectado |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Provisión acumulada ≠ pasivo recalculado | Base prestacional desactualizada (aumentos, comisiones no promediadas) | Recalcular empleado a empleado y ajustar la provisión con nota a AuxContable | Diferencia ≥ 1 UVT por empleado persistente → revisar el histórico salarial completo del empleado antes de cerrar el mes |
| Empleado sin fondo de cesantías al acercarse el 14 feb | Afiliación nunca reportada | Solicitar al cliente la afiliación/elección con plazo improrrogable (alerta a 30, 15 y 5 días) | Sin fondo al 14 feb la consignación es imposible → escalar a Contador Titular ANTES del vencimiento; la sanción por no consignar es del cliente, pero la alerta documentada es de la firma |
| Cliente sin caja para la consignación de febrero | Hito no provisionado en tesorería del cliente | Alerta temprana (la proyección de 30 días existe para esto); coordinar con Tesorería alternativas de priorización | Si el cliente decide no consignar a tiempo, documentar la advertencia formal (sanción: 1 día de salario por día de mora) y escalar a Contador Titular |
| Salario variable sin histórico suficiente para promediar | Empleado reciente | Promediar por el tiempo servido (norma) y documentar la base | Marca `[BASE EN VERIFICACIÓN]` hasta completar el histórico |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia de provisión | ≥ 1 UVT por empleado o ≥ 0,5 % del pasivo prestacional | Investigar y ajustar antes del cierre mensual |
| Riesgo de incumplimiento de hito anual | A 15 días del hito sin condiciones resueltas | Contador Titular + Orquestador |
| Pasivo prestacional con error acumulado | ≥ 50 UVT | Contador Titular vía Orquestador |
| Cliente decide incumplir un hito legal | Cualquier caso | Contador Titular, mismo día, con advertencia formal documentada |

## Reglas críticas
🚫 NUNCA calcular prestaciones sin auxilio de transporte en la base (excepto vacaciones): es el error de base más común y la UGPP lo detecta.
🚫 NUNCA dejar pasar el 14 de febrero sin consignación o sin escalamiento documentado: la sanción corre por día.
✅ SIEMPRE conciliar provisión contra pasivo recalculado, no contra la suma de cuotas.

## Métricas
- Hitos anuales cumplidos en plazo (31 ene, 14 feb, 30 jun, 20 dic): 100 %.
- Diferencias provisión vs pasivo recalculado al cierre: ≤ 0,5 % del pasivo total.
- Alertas de caja emitidas ≥ 30 días antes de cada hito: 100 %.

## Tests
### Test 1 — (normal) Provisión de junio 2026 para una planta de 22 empleados, 3 con salario variable por comisiones, y liquidación de la prima del primer semestre
**Output:** provisión mensual por empleado con bases correctas (variables promediadas a 12 meses, auxilio incluido salvo vacaciones); conciliación provisión vs pasivo recalculado en diferencia $0; prima semestral liquidada (15 días o proporción) y entregada a la nómina de junio antes del 30/06; AuxContable notificado según [[Aux 12 - Provisiones y Prestaciones Sociales]].
### Test 2 — (excepción) El 30 de enero se detecta que un empleado que ingresó en marzo del año anterior nunca eligió fondo de cesantías, y el 14 de febrero está a 15 días
**Output:** intereses de cesantías del 31 ene se pagan normalmente (no dependen del fondo); alerta inmediata al cliente con plazo improrrogable para la elección/afiliación al fondo (recordatorios a 15 y 5 días); al persistir la omisión a 5 días del vencimiento, escalamiento a Contador Titular con la advertencia formal documentada (sanción de 1 día de salario por día de mora corre contra el cliente); la gestión completa queda archivada como evidencia de diligencia de la firma.

═══════════════════════════════════════════════════════════════════════

---
name: liquidar-prestaciones-finales
description: Activa cuando termina un contrato laboral, por cualquier causa. Calcula la liquidación definitiva — cesantías e intereses pendientes, prima y vacaciones proporcionales, indemnización si aplica (Art. 64 CST) — genera el acta y coordina el pago. Sin esta skill el cliente paga mal la salida y queda expuesto a la indemnización moratoria (Art. 65 CST).
agente: RITORE-AuxiliarNomina-Senior
categoria: operativo
---

# Skill: liquidar-prestaciones-finales

## Para qué existe
La salida de un empleado es el momento de mayor riesgo laboral del cliente: cada día de retraso en el pago de la liquidación puede causar indemnización moratoria de un día de salario (Art. 65 CST). Esta skill produce una liquidación exacta, completa y pagable de inmediato, con la indemnización por despido bien calculada cuando aplica.

## Cuándo se activa
- Novedad de retiro validada por `gestionar-novedades-laborales` (renuncia, despido con/sin justa causa, mutuo acuerdo, vencimiento de término fijo, periodo de prueba).
- Solicitud de pre-liquidación (cliente evaluando el costo de una salida antes de decidirla).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Novedad de retiro con causa y fecha exacta | `gestionar-novedades-laborales` | Sin causa documentada NO se liquida indemnización (cambia el cálculo por completo); solicitar al cliente con urgencia (el reloj del Art. 65 corre desde la terminación) |
| Histórico salarial y prestacional del empleado | `liquidar-prestaciones-sociales` + maestro | Reconstruir desde las liquidaciones cerradas; con vacíos, marca `[BASE EN VERIFICACIÓN]` y prioridad máxima |
| Saldos pendientes: vacaciones no disfrutadas, préstamos, deducciones autorizadas | Maestro + cliente | Liquidar con lo registrado; descuentos no soportados NO se aplican (riesgo de pago incompleto ilegal) |
| Ficha de parámetros vigentes a la fecha de retiro | `verificar-parametros-laborales-vigentes` | Bloqueante: la liquidación usa los parámetros del día de terminación |

## Procedimiento
1. Verificar causa y fecha de terminación; determinar si procede indemnización (despido sin justa causa → Art. 64 CST según tipo de contrato y antigüedad; término fijo → salarios faltantes del plazo pactado).
2. Calcular cesantías del año en curso + intereses proporcionales (base prestacional con auxilio de transporte; salario variable promediado).
3. Calcular prima proporcional del semestre en curso y vacaciones causadas no disfrutadas (base sin auxilio `[VERIFICAR base]`; las vacaciones en dinero se liquidan a salario actual).
4. Calcular la indemnización si procede (Art. 64 CST): contrato indefinido por tramos de antigüedad y nivel salarial; término fijo por el tiempo faltante; documentar la memoria de cálculo.
5. Aplicar retención en la fuente sobre los conceptos gravados de la liquidación (vía `calcular-retencion-procedimiento-1-2`; la indemnización tiene tratamiento propio `[VERIFICAR retención del 20 % para ingresos ≥ 204 UVT/mes — Art. 401-3 ET]`).
6. Descontar únicamente deducciones soportadas y legalmente procedentes al retiro.
7. Generar el acta de liquidación final con detalle concepto a concepto y entregarla al cliente para firma del empleado.
8. Notificar a Tesorería (pago inmediato — el Art. 65 corre por día) y a AuxContable (cancelación de provisiones y causación del gasto final); reportar el retiro a PILA y nómina electrónica del periodo.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Liquidación final por concepto | Cada concepto con base, fórmula y valor recalculable; total neto verificado |
| Acta de liquidación | Completa, con causa de terminación y memoria de la indemnización si aplica |
| Notificaciones a Tesorería y AuxContable | El mismo día hábil del cálculo (el pago no puede esperar al ciclo normal) |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Causa de despido en disputa (cliente alega justa causa sin soporte sólido) | Proceso disciplinario incompleto | Liquidar TODOS los conceptos no controvertidos de inmediato y presentar al cliente ambos escenarios (con/sin indemnización) | Decisión jurídica no es de la firma: escalar a Contador Titular, recomendar concepto legal externo y documentar; lo no controvertido SE PAGA (limita la moratoria) |
| Cliente ordena descontar un faltante/daño sin autorización escrita del empleado | Descuento ilegal al retiro | Rechazar el descuento no soportado y explicar el riesgo (pago incompleto = moratoria + reclamo) | Si el cliente insiste por escrito, Contador Titular antes de pagar; la instrucción queda documentada |
| Histórico salarial con vacíos (comisiones sin registrar) | Información incompleta de periodos viejos | Reconstruir con soportes del cliente con plazo de 24 h hábiles (prioridad por el Art. 65) | Liquidar con la mejor base disponible documentada y ajustar después si aparecen soportes; la liquidación NO se congela indefinidamente |
| Retiro reportado semanas después de la fecha real | Cliente tardío | Liquidar con fecha real y cuantificar la moratoria ya corrida | Notificación formal al cliente del costo del retraso (causa: reporte tardío) y escalamiento si ≥ 50 UVT |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia en verificación de la liquidación | ≥ 1 UVT o ≥ 0,5 % del total | Recalcular antes de emitir el acta |
| Liquidación final total | ≥ 50 UVT | Doble verificación + visto bueno del Contador Titular antes del pago |
| Liquidación o contingencia | ≥ 500 UVT | Contador Titular, mismo día (indemnizaciones grandes, directivos) |
| Disputa jurídica sobre la causa | Cualquier caso | Contador Titular (la firma no emite conceptos jurídicos laborales) |

## Reglas críticas
🚫 NUNCA retener el pago de los conceptos no controvertidos: cada día de retraso es moratoria potencial del cliente (Art. 65 CST).
🚫 NUNCA aplicar descuentos al retiro sin autorización escrita o soporte legal.
✅ SIEMPRE presentar la memoria de cálculo de la indemnización: es el concepto que más se demanda.

## Métricas
- Liquidaciones finales emitidas en ≤ 2 días hábiles desde la novedad de retiro: 100 % (medición mensual).
- Liquidaciones recalculadas por error tras emitidas: 0.
- Actas con memoria de cálculo completa de indemnización (cuando aplica): 100 %.

## Tests
### Test 1 — (normal) Renuncia voluntaria de una empleada con contrato indefinido, 3 años y 4 meses, salario fijo $3,2M, 6 días de vacaciones pendientes
**Output:** liquidación sin indemnización (renuncia): cesantías + intereses del año en curso, prima proporcional del semestre, 6 días de vacaciones a salario actual; retención sobre conceptos gravados vía `calcular-retencion-procedimiento-1-2`; acta concepto a concepto emitida en ≤ 2 días hábiles; Tesorería instruida para pago inmediato; provisiones canceladas en AuxContable; retiro reportado a PILA y nómina electrónica.
### Test 2 — (excepción) Despido que el cliente alega con justa causa pero sin proceso disciplinario documentado; empleado con 7 años, salario $5,1M, y el cliente además pide descontarle $900.000 de un equipo dañado sin autorización escrita
**Output:** conceptos no controvertidos liquidados y pagados de inmediato (cesantías, intereses, prima, vacaciones) para limitar la moratoria; doble escenario presentado (con indemnización Art. 64 por 7 años ≈ valor que supera 50 UVT → visto bueno del Contador Titular requerido); descuento del equipo RECHAZADO por falta de autorización escrita, con explicación del riesgo; recomendación documentada de concepto legal externo sobre la justa causa; toda la secuencia archivada vía `documentar-decision-no-trivial`.

═══════════════════════════════════════════════════════════════════════

---
name: interpretar-PILA-operadores
description: Activa al recibir la planilla PILA del operador del cliente (Enlace Operativo, ARUS, SOI, Mi Planilla). Parsea el formato del operador, cruza contra la liquidación interna aporte por aporte e investiga toda diferencia antes de aceptar la planilla como definitiva. Sin esta skill los aportes pagados pueden diferir de los liquidados sin que nadie lo note — hasta que la UGPP lo nota.
agente: RITORE-AuxiliarNomina-Senior
categoria: operativo
---

# Skill: interpretar-PILA-operadores

## Para qué existe
Entre la liquidación interna y lo que el operador PILA realmente presenta hay un trecho donde viven los errores silenciosos: IBC truncados, novedades no reflejadas, tarifas de ARL erradas. Esta skill cierra ese trecho cruzando ambas fuentes aporte por aporte — es la defensa preventiva contra la UGPP.

## Cuándo se activa
- Planilla PILA del periodo disponible en el operador del cliente (descarga o recepción).
- Antes del vencimiento de pago PILA del cliente (según los últimos dígitos del NIT `[VERIFICAR calendario Decreto 1990/2016]`): verificación de que la planilla exista y cuadre.
- Planilla correctiva generada por una novedad retroactiva.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Planilla PILA del periodo (archivo del operador) | Operador PILA vía cliente | Si a 3 días hábiles del vencimiento no está disponible, alerta al cliente y a Orquestador (la mora en aportes es automática) |
| Liquidación interna del periodo (IBC y aportes por empleado) | `liquidar-nomina-periodica` | Dependencia bloqueante: sin liquidación cerrada no hay contra qué cruzar |
| Catálogo de formatos por operador | Registro propio | Operador nuevo → mapear el formato con la primera planilla y documentarlo para reutilización |

## Procedimiento
1. Detectar el operador y aplicar el parser del formato correspondiente (Enlace Operativo / ARUS / SOI / Mi Planilla); normalizar a estructura interna.
2. Cruzar por empleado: IBC, días cotizados, novedades (ingreso/retiro/incapacidad/licencia), y cada aporte (salud, pensión, ARL con su clase de riesgo, caja, SENA, ICBF según exoneración).
3. Verificar totales: suma de aportes de la planilla = total a pagar del operador, y = total de la liquidación interna.
4. Toda diferencia se investiga ANTES de aceptar la planilla: identificar si el error es del operador (parametrización) o de la liquidación interna (entonces corregir internamente primero).
5. Validar que las novedades del periodo (de `gestionar-novedades-laborales`) estén reflejadas en la planilla.
6. Aceptada la planilla: notificar a Tesorería el monto y fecha límite de pago, y a AuxContable el asiento de aportes.
7. Archivar planilla + cruce como papel de trabajo (insumo de `responder-requerimiento-UGPP`).

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Cruce PILA vs liquidación interna | Diferencia $0 por empleado y en totales, o toda diferencia ≥ 1 UVT investigada y resuelta antes del pago |
| Notificación a Tesorería | Monto exacto y fecha límite según NIT, con ≥ 2 días hábiles de margen |
| Papel de trabajo archivado | Planilla + cruce + resolución de diferencias, recuperable para UGPP |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| IBC del operador ≠ IBC liquidado | Truncamiento, tope de 25 SMMLV mal aplicado, o novedad no cargada en el operador | Identificar el origen empleado a empleado; corregir en el operador antes del pago | Si el operador no permite corregir antes del vencimiento, pagar lo correcto vía planilla ajustada o documentar la corrección para planilla correctiva inmediata — NUNCA dejar pasar la diferencia sin rastro |
| Clase de riesgo ARL distinta entre operador y maestro | Reclasificación no actualizada en alguna de las dos fuentes | Verificar contra el acto de clasificación de la ARL; corregir la fuente errada | Diferencia de aportes retroactiva ≥ 1 UVT → cuantificar y gestionar la corrección con planillas correctivas |
| Planilla no disponible a 3 días del vencimiento | Cliente no la generó / operador caído | Alerta inmediata al cliente con la fecha límite y el costo de la mora (intereses automáticos) | Si el operador está caído, gestionar planilla por canal alterno del operador; persistencia → Orquestador (la mora corre contra el cliente, la alerta documentada protege a la firma) |
| Novedad de retiro no reflejada (se cotiza por un empleado ya retirado) | Novedad no cargada al operador | Corregir antes del pago (aporte de más es recuperable pero engorroso) | Si ya se pagó, gestionar la devolución/compensación ante los subsistemas y documentar |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia PILA vs liquidación | ≥ 1 UVT individual o ≥ 0,5 % del total de aportes | Investigar y resolver antes del pago |
| Diferencia no resuelta al vencimiento | ≥ 50 UVT | Contador Titular vía Orquestador, mismo día |
| Mora en aportes materializada | Cualquier monto | Contador Titular informado + cuantificación de intereses |
| Patrón de errores del operador | 3+ periodos consecutivos | Orquestador + recomendación al cliente de cambio de operador |

## Reglas críticas
🚫 NUNCA aceptar una planilla con diferencias ≥ 1 UVT sin investigar — "el operador lo calculó así" no es explicación.
🚫 NUNCA dejar que el vencimiento PILA pase sin pago ni escalamiento documentado (los intereses moratorios son automáticos y la UGPP fiscaliza la mora).
✅ SIEMPRE archivar el cruce como papel de trabajo: es la primera línea de defensa ante un requerimiento UGPP.

## Métricas
- Planillas cruzadas contra liquidación antes del pago: 100 % (medición mensual).
- Planillas aceptadas con diferencia $0 o diferencias resueltas: 100 %.
- Pagos PILA dentro del plazo del calendario por NIT: 100 %.

## Tests
### Test 1 — (normal) Planilla SOI de un cliente con 15 empleados llega 5 días antes del vencimiento; el cruce da diferencia $0
**Output:** parser SOI aplicado; cruce por empleado (IBC, días, novedades, aportes por subsistema) y totales en $0; novedades del periodo verificadas como reflejadas; Tesorería notificada con monto y fecha límite con margen; planilla + cruce archivados como papel de trabajo.
### Test 2 — (excepción) En la planilla de ARUS, un empleado con incapacidad de 12 días aparece cotizando 30 días con IBC pleno, y el vencimiento es en 2 días hábiles
**Output:** diferencia detectada en el cruce (días e IBC no reflejan la novedad de incapacidad); origen identificado: la novedad no se cargó al operador; corrección en el operador el mismo día y re-cruce en $0 antes del pago; si el operador no hubiera permitido la corrección a tiempo, pago con la mejor planilla disponible + planilla correctiva inmediata documentada; Tesorería notificada dentro del plazo; el caso alimenta el registro de calidad del operador.

═══════════════════════════════════════════════════════════════════════

---
name: transmitir-nomina-electronica-DIAN
description: Activa mensualmente tras el cierre de la liquidación. Genera el XML de nómina electrónica según el anexo técnico (Res. DIAN 000013/2021), lo cuadra contra la liquidación y lo entrega a 04-AuxiliarFacturacionElectronica para transmisión al sistema DIAN; gestiona las correcciones de los rechazos por datos de liquidación. Sin esta skill el costo laboral del cliente pierde su soporte de deducibilidad.
agente: RITORE-AuxiliarNomina-Senior
categoria: operativo
---

# Skill: transmitir-nomina-electronica-DIAN

## Para qué existe
La nómina electrónica es el documento soporte de deducibilidad del costo laboral: sin transmisión validada, el gasto de nómina del cliente queda en riesgo en renta. La frontera con FacturaciónElectrónica es nítida: **esta skill genera el XML fiel a la liquidación y corrige datos de liquidación; FacturaciónElectrónica valida estructura, transmite y confirma**.

## Cuándo se activa
- Cierre mensual de `liquidar-nomina-periodica` (en clientes quincenales, al cierre de la 2.ª quincena que consolida el mes).
- Devolución de rechazo por datos de liquidación desde 04-AuxiliarFacturacionElectronica.
- Ajustes del periodo (novedad retroactiva ya recalculada) que exigen documento de reemplazo/eliminación.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Liquidación del periodo cerrada y verificada | `liquidar-nomina-periodica` | Bloqueante: NUNCA generar XML de liquidación abierta (cada ajuste posterior multiplica documentos de reemplazo) |
| Maestro de empleados con identificación completa | `gestionar-novedades-laborales` | Datos de identificación incompletos → completar antes de generar (causa típica de rechazo) |
| Anexo técnico de nómina electrónica vigente | `verificar-parametros-laborales-vigentes` / monitoreo normativo | Versión dudosa → `verificar-vigencia-normativa` antes de generar |

## Procedimiento
1. Generar el XML por empleado según el anexo técnico: devengados, deducciones, neto, con los códigos de concepto correctos.
2. Cuadre interno: Σ devengados, Σ deducciones y Σ netos del XML = totales de la liquidación cerrada, diferencia $0.
3. Entregar el lote a 04-AuxiliarFacturacionElectronica (skill `transmitir-nomina-electronica`) antes del día hábil 5 del mes, para transmisión dentro de la ventana DIAN.
4. Recibir confirmaciones: conciliar empleados liquidados = documentos validados.
5. Ante rechazo por datos de liquidación devuelto por FacturaciónElectrónica: corregir aquí el dato de origen (IBC, devengado, identificación), re-cuadrar y reentregar (el control de 3 intentos y hold lo gobierna `gestionar-rechazo-DIAN` del perfil 04).
6. Para ajustes retroactivos: generar documento de reemplazo/eliminación referenciando el documento original del empleado afectado.
7. Archivar el cuadre XML vs liquidación como papel de trabajo del periodo.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| XML del periodo entregado a FacturaciónElectrónica | Cuadre $0 contra la liquidación; antes del día hábil 5 |
| Conciliación de confirmaciones | Empleados liquidados = documentos validados, sin huérfanos |
| Documentos de ajuste (cuando aplica) | Referencian el documento original correcto |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| XML no cuadra contra la liquidación | Concepto mapeado a código errado o redondeo acumulado | Cuadrar concepto a concepto hasta aislar; corregir el mapeo | NUNCA entregar un XML descuadrado; si el origen es la liquidación, reabrirla antes de generar |
| Rechazo devuelto por datos de liquidación | IBC o devengado inconsistente en origen | Corregir el dato fuente, re-cuadrar y reentregar el documento corregido | 3 rechazos del mismo documento → hold de 24 h (protocolo del perfil 04) y revisión conjunta con AuxContable del caso |
| Liquidación reabierta después de entregado el XML | Novedad de última hora | Coordinar con FacturaciónElectrónica: si no se transmitió, reemplazar el lote; si ya se transmitió, documento de reemplazo por empleado afectado | Cadena de reemplazos > 2 sobre el mismo periodo → Orquestador (señal de proceso de cierre roto) |
| Ventana DIAN próxima a cerrar sin lote entregado | Liquidación tardía | Priorizar el cierre y entregar parcial lo verificado, completando el resto dentro de la ventana | Si la extemporaneidad es inevitable, alerta a Contador Titular y EspecialistaRenta (riesgo de deducibilidad) ANTES del cierre de la ventana |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Descuadre XML vs liquidación | ≥ 1 UVT | No se entrega; aislar y corregir |
| Riesgo de transmisión extemporánea | ≤ 2 días hábiles de ventana con lote pendiente | Orquestador + Contador Titular |
| Costo laboral sin soporte transmitido | ≥ 50 UVT | Contador Titular (deducibilidad en riesgo) |
| FacturaciónElectrónica no confirma recepción del lote | Timeout 4 h | Reiterar y escalar a Orquestador en paralelo |

## Reglas críticas
🚫 NUNCA generar XML de una liquidación abierta o descuadrada.
🚫 NUNCA corregir un rechazo "en el XML" sin corregir el dato en la liquidación de origen (el XML siempre refleja la liquidación, no al revés).
✅ SIEMPRE conciliar empleados liquidados vs documentos validados antes de dar el periodo por cerrado.

## Métricas
- Lotes entregados a FacturaciónElectrónica antes del día hábil 5: 100 % (medición mensual).
- Rechazos por datos de liquidación: < 2 % de documentos del periodo.
- Conciliación empleados vs documentos validados en diferencia 0: 100 %.

## Tests
### Test 1 — (normal) Cierre de junio: liquidación de 28 empleados verificada; generación y entrega del lote el día hábil 3
**Output:** XML por empleado con códigos de concepto correctos; cuadre Σ devengados/deducciones/netos = liquidación, diferencia $0; lote entregado a FacturaciónElectrónica; confirmaciones conciliadas 28 = 28; papel de trabajo del cuadre archivado.
### Test 2 — (excepción) Tras entregar el lote de julio, una incapacidad retroactiva obliga a recalcular 2 empleados cuyo documento ya fue validado por la DIAN
**Output:** liquidación de los 2 empleados recalculada por tramos (julio 2026: cuidado con el doble parámetro del mes); documentos de **reemplazo** generados referenciando los originales validados; re-cuadre del periodo ajustado; reentrega a FacturaciónElectrónica y conciliación final sin huérfanos; el origen (novedad tardía) se reporta a `gestionar-novedades-laborales` para el indicador del cliente; cadena de reemplazos = 1 (bajo el umbral de señal de proceso roto).

═══════════════════════════════════════════════════════════════════════

---
name: emitir-certificados-220
description: Activa anualmente entre febrero y marzo para emitir los Certificados de Ingresos y Retenciones por rentas de trabajo (F-220) del año gravable anterior, a todos los empleados activos y retirados. Sin esta skill los empleados no pueden declarar y el cliente incumple una obligación formal.
agente: RITORE-AuxiliarNomina-Senior
categoria: operativo
---

# Skill: emitir-certificados-220

## Para qué existe
El F-220 es la fotografía anual oficial de lo que cada empleado ganó y le retuvieron: si no cuadra con la nómina, con la exógena y con lo declarado en retefuente, alguien (el empleado, el cliente o la firma) tendrá un problema con la DIAN. Esta skill lo emite completo, cuadrado y a tiempo.

## Cuándo se activa
- Anualmente, en febrero del año siguiente al gravable (meta de entrega: antes del 31 de marzo `[VERIFICAR plazo del calendario tributario vigente]`).
- Retiro de un empleado durante el año (derecho a certificado de su fracción, si lo solicita).
- Solicitud puntual de un empleado o del cliente (reexpedición).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Acumulados anuales por empleado: ingresos por concepto, retenciones, aportes obligatorios | Liquidaciones cerradas del año + `calcular-retencion-procedimiento-1-2` | Vacíos en el acumulado → reconstruir desde las nóminas mensuales archivadas ANTES de emitir; no se certifica sobre datos incompletos |
| Consolidado de retefuente declarado en el año | EspecialistaRetenciones | Timeout 4 h → emitir queda en espera; el F-220 DEBE cuadrar con lo declarado |
| Datos de identificación y contacto de empleados (incluye retirados) | Maestro + cliente | Retirados ilocalizables → certificado emitido y custodiado; entrega documentada como intentada |

## Procedimiento
1. Consolidar por empleado los acumulados del año gravable: salarios, primas, cesantías pagadas `[VERIFICAR tratamiento de cesantías consignadas vs pagadas]`, vacaciones, bonificaciones, aportes obligatorios a salud y pensión, y retención practicada.
2. Cruce de control triple: Σ certificados = Σ nóminas del año = consolidado declarado en retefuente (EspecialistaRetenciones). Toda diferencia se resuelve ANTES de emitir.
3. Generar el F-220 individual por empleado (activos y retirados del año) en el formato vigente del año gravable.
4. Entregar a los empleados vía cliente (o canal directo pactado) antes del plazo; registrar la entrega.
5. Reportar el consolidado emitido a EspecialistaRetenciones y dejarlo disponible como insumo del Formato 2276 de exógena (ExogenaMaster).
6. Archivar los certificados y el cruce de control como papel de trabajo del año.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| F-220 por empleado (activos + retirados del año) | Cobertura 100 %; cifras = acumulado de nómina = declarado en retefuente |
| Registro de entrega | Fecha y canal por empleado; intentos documentados para ilocalizables |
| Cruce de control archivado | Triple cuadre con diferencia $0 o diferencias resueltas documentadas |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Σ certificados ≠ retefuente declarada | Retención de un mes corregida sin actualizar el acumulado, o error en declaración | Aislar el mes y el empleado de la diferencia con EspecialistaRetenciones | Si el error está en una declaración presentada, EspecialistaRetenciones evalúa corrección; los certificados esperan la cifra definitiva |
| Empleado reclama que su certificado no cuadra con sus desprendibles | Error de acumulado o desprendible no oficial | Recalcular el acumulado del empleado contra las 12 nóminas cerradas | Si el error es real, reexpedir el certificado corregido y verificar si el error contamina el triple cruce (entonces revisar TODOS) |
| Empleado retirado ilocalizable | Datos de contacto desactualizados | Solicitar datos al cliente; certificado custodiado con intentos de entrega documentados | La obligación queda cubierta con la emisión y la diligencia documentada |
| Año con cambio de formato F-220 | Resolución DIAN nueva | `verificar-vigencia-normativa` y usar el formato del año gravable correcto | Marca `[VERIFICAR formato]` y consulta a EspecialistaRetenciones antes de emitir masivamente |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia en el triple cruce | ≥ 1 UVT | Resolver con EspecialistaRetenciones antes de emitir |
| Diferencia que implica corrección de declaraciones | ≥ 50 UVT | EspecialistaRetenciones + Contador Titular |
| Certificados sin emitir | A 15 días del plazo límite | Orquestador |
| Error masivo detectado tras la entrega | Cualquier caso | Contador Titular (reexpedición controlada y comunicación a empleados) |

## Reglas críticas
🚫 NUNCA emitir certificados sin el triple cruce (nómina = certificados = retefuente declarada) en $0 o con diferencias resueltas.
🚫 NUNCA omitir a los retirados del año: tienen el mismo derecho que los activos.
✅ SIEMPRE registrar la entrega: el certificado emitido pero no entregado no cumple la obligación.

## Métricas
- Certificados entregados antes del plazo: 100 % de empleados del año (medición anual).
- Triple cruce con diferencia $0: 100 %.
- Reexpediciones por error de la firma: 0.

## Tests
### Test 1 — (normal) Año gravable con 31 empleados (26 activos + 5 retirados); el triple cruce cuadra a la primera
**Output:** 31 F-220 generados en el formato del año gravable; triple cruce nómina = certificados = retefuente en $0; entrega registrada vía cliente antes del plazo (retirados contactados, 1 ilocalizable con diligencia documentada); consolidado reportado a EspecialistaRetenciones y disponible para el Formato 2276; archivo completo.
### Test 2 — (excepción) El triple cruce arroja $2,1M más en certificados que en la retefuente declarada, concentrados en agosto
**Output:** emisión DETENIDA; aislamiento con EspecialistaRetenciones encuentra que la corrección de retención de un empleado en agosto se aplicó en nómina pero la declaración de ese mes no se corrigió; diferencia ≈ 40 UVT → EspecialistaRetenciones evalúa la corrección de la declaración (y por estar bajo 50 UVT no exige al Contador Titular, aunque se le informa); certificados emitidos solo tras la cifra definitiva; cruce final $0 archivado con la trazabilidad de la corrección.

═══════════════════════════════════════════════════════════════════════

---
name: documentar-trabajo-en-casa-teletrabajo
description: Activa cuando el cliente tiene empleados en teletrabajo (Ley 1221/2008), trabajo en casa (Ley 2088/2021) o trabajo remoto, y en cada liquidación que incluya auxilios de la modalidad. Verifica acuerdos, aplica auxilios diferenciales y documenta el cumplimiento de la desconexión laboral (Ley 2191/2022). Sin esta skill el cliente paga auxilios mal o queda sin evidencia de cumplimiento ante un reclamo.
agente: RITORE-AuxiliarNomina-Senior
categoria: operativo
---

# Skill: documentar-trabajo-en-casa-teletrabajo

## Para qué existe
Cada modalidad remota tiene reglas distintas y se confunden con costo: el teletrabajo exige auxilio de conectividad y condiciones registradas; el trabajo en casa es temporal y conserva el auxilio de transporte como auxilio de conectividad para quienes devengan ≤ 2 SMMLV `[VERIFICAR equivalencia vigente]`; y la desconexión laboral aplica a todos. Esta skill mantiene la modalidad de cada empleado correcta, pagada y documentada.

## Cuándo se activa
- Novedad de cambio de modalidad reportada por `gestionar-novedades-laborales`.
- Cada liquidación de periodo con empleados en modalidad remota (verificación de auxilios).
- Revisión semestral de acuerdos y de cumplimiento de desconexión (cron).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Acuerdo firmado de la modalidad (anexo de teletrabajo / habilitación de trabajo en casa) | Cliente | Modalidad SIN acuerdo firmado → marca `irregular`; solicitar regularización (24 h hábiles, reiterar 1 vez) y alertar el riesgo |
| Política de desconexión laboral del cliente (Ley 2191/2022) | Cliente | Solicitar; si no existe, recomendar formalmente su adopción y documentar la recomendación |
| Maestro con modalidad vigente por empleado | `gestionar-novedades-laborales` | Reconstruir con los acuerdos archivados |

## Procedimiento
1. Clasificar la modalidad de cada empleado remoto: teletrabajo (Ley 1221/2008, permanente con anexo contractual), trabajo en casa (Ley 2088/2021, habilitación temporal), o trabajo remoto.
2. Verificar el acuerdo firmado y su vigencia (el trabajo en casa tiene término — extensible — `[VERIFICAR términos]`).
3. Aplicar el tratamiento económico por modalidad: teletrabajo → auxilio de conectividad pactado, sin auxilio de transporte; trabajo en casa → auxilio de conectividad en reemplazo del de transporte para devengados ≤ 2 SMMLV; verificar compatibilidades.
4. Entregar a `liquidar-nomina-periodica` la marca de modalidad y los auxilios aplicables por empleado.
5. Documentar el cumplimiento de desconexión laboral: política adoptada, canales de reporte, ausencia de reclamos en el periodo.
6. Revisión semestral: acuerdos vigentes, modalidades reales vs documentadas (un "teletrabajador de hecho" sin anexo es un riesgo), y reporte de irregularidades al cliente.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Registro de modalidad por empleado | Con acuerdo firmado archivado y vigencia |
| Auxilios del periodo entregados a liquidación | Coherentes con la modalidad y el nivel salarial de cada empleado |
| Expediente de cumplimiento (desconexión + acuerdos) | Actualizado al menos semestralmente; irregularidades reportadas con fecha |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Empleado remoto "de hecho" sin acuerdo firmado | Modalidad adoptada informalmente | Marca `irregular`; solicitar al cliente la formalización con plazo | Si el cliente no formaliza en 30 días, advertencia formal documentada del riesgo laboral (la firma no puede firmar por él) y reporte en la revisión semestral |
| Auxilio de transporte pagado a teletrabajador | Parametrización heredada | Corregir desde el periodo en curso; cuantificar el pagado de más | Recuperación de pagos previos: decisión del cliente documentada (descuento requiere autorización del empleado) |
| Cliente sin política de desconexión y con reclamo de un empleado | Ley 2191/2022 sin implementar | Documentar el reclamo y recomendar política + respuesta formal inmediata | Escalar a Contador Titular si el reclamo escala a queja ante el Ministerio (riesgo de inspección) |
| Acuerdo de trabajo en casa vencido sin renovar | Término cumplido | Alertar al cliente: renovar o retornar a presencialidad formalmente | Vencido + sin gestión en 30 días → tratar como irregular y reportar |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Auxilios mal aplicados detectados | ≥ 1 UVT acumulado por empleado | Corregir en el periodo y documentar |
| Empleados en modalidad irregular | > 10 % de la planta remota del cliente | Orquestador + AtencionCliente (gestión estructural) |
| Reclamo formal de desconexión o queja ministerial | Cualquier caso | Contador Titular |
| Pagado de más acumulado por auxilios errados | ≥ 50 UVT | Contador Titular |

## Reglas críticas
🚫 NUNCA aplicar auxilios de una modalidad sin acuerdo firmado que la soporte.
🚫 NUNCA pagar simultáneamente auxilio de transporte y auxilio de conectividad al mismo empleado salvo soporte normativo expreso `[VERIFICAR compatibilidad]`.
✅ SIEMPRE documentar el estado de cumplimiento aunque el cliente no lo pida: el expediente vale oro el día del reclamo.

## Métricas
- Empleados remotos con acuerdo firmado y vigente: 100 % (medición semestral).
- Auxilios de modalidad correctamente aplicados en liquidación: 100 % (verificación mensual).
- Irregularidades reportadas al cliente con fecha y seguimiento: 100 % de las detectadas.

## Tests
### Test 1 — (normal) Cliente con 6 teletrabajadores con anexo firmado y auxilio de conectividad pactado de $80.000
**Output:** modalidades verificadas con acuerdos vigentes; auxilio de conectividad (no de transporte) entregado a `liquidar-nomina-periodica` para los 6; expediente de desconexión actualizado (política adoptada, sin reclamos); revisión semestral programada.
### Test 2 — (excepción) En la revisión semestral aparecen 4 empleados trabajando desde casa hace 5 meses sin habilitación firmada, dos de ellos recibiendo auxilio de transporte pese a no desplazarse
**Output:** los 4 marcados `irregular`; solicitud de formalización al cliente con plazo; auxilios corregidos desde el periodo en curso (conectividad en lugar de transporte para los ≤ 2 SMMLV) con cuantificación de lo pagado de manera inconsistente; al persistir la informalidad a los 30 días, advertencia formal documentada del riesgo laboral; el caso queda en el expediente semestral y, por superar el 10 % de la planta remota, se escala a Orquestador para gestión estructural con el cliente.

═══════════════════════════════════════════════════════════════════════

---
name: responder-requerimiento-UGPP
description: Activa cuando llega un requerimiento de la UGPP al cliente (información, requerimiento para declarar y/o corregir, pliego de cargos). Arma el expediente probatorio de nómina y PILA, coordina la estrategia con DefensaTributaria y cumple los plazos de respuesta. Sin esta skill el cliente responde tarde o sin soporte — y la UGPP liquida oficialmente con sanciones.
agente: RITORE-AuxiliarNomina-Senior
categoria: operativo
---

# Skill: responder-requerimiento-UGPP

## Para qué existe
Ante la UGPP, el que no prueba paga: los requerimientos tienen plazos perentorios y la diferencia entre una respuesta soportada y una genérica son sanciones que pueden superar los honorarios de años. Esta skill arma la prueba (ese es mi dominio: nómina, IBC, PILA) y la pone en manos de quien diseña la defensa (DefensaTributaria).

## Cuándo se activa
- Requerimiento UGPP notificado al cliente (cualquier etapa: persuasivo, requerimiento de información, requerimiento para declarar/corregir, pliego de cargos).
- Solicitud de DefensaTributaria de soporte probatorio de nómina para una actuación en curso.
- Hallazgo interno que anticipe fiscalización (p. ej. pagos no salariales > 40 % sostenidos — gestión preventiva).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Requerimiento completo con fecha de notificación | Cliente vía AtencionCliente | Sin el documento completo no se dimensiona el alcance: solicitarlo el MISMO DÍA; el plazo legal corre desde la notificación, no desde que el cliente lo reenvía |
| Expediente de nómina del periodo requerido: liquidaciones, PILA con cruces, contratos, novedades, IBC | Archivo propio (papeles de trabajo de las demás skills) | Vacíos en el archivo → reconstrucción prioritaria; si el periodo es anterior al servicio de la firma, solicitar al cliente los soportes históricos con inventario de lo faltante |
| Estrategia de respuesta | DefensaTributaria (Master) | Timeout 4 h de respuesta inicial → escalar a Orquestador: el plazo del requerimiento no espera |

## Procedimiento
1. Registrar la fecha de notificación y calcular el plazo de respuesta; fijar fecha interna de cierre con ≥ 3 días hábiles de margen.
2. Identificar el alcance: periodos, subsistemas (salud/pensión/ARL/parafiscales), empleados y conceptos cuestionados (típico: IBC, pagos no salariales Art. 30 Ley 1393/2010, mora).
3. Armar el expediente probatorio: liquidaciones de los periodos, planillas PILA con sus cruces (papel de trabajo de `interpretar-PILA-operadores`), contratos y otrosíes, soportes de novedades, política de pagos no salariales del cliente.
4. Preparar la matriz hecho-cuestionado → prueba → explicación técnica, cuantificando cada diferencia alegada por la UGPP contra el cálculo propio.
5. Entregar el expediente a DefensaTributaria para la redacción jurídica de la respuesta; resolver sus solicitudes de soporte adicional con prioridad crítica (SLA 1 h de acuse).
6. Apoyar la revisión técnica del borrador (cifras, anexos) y obtener la aprobación del Contador Titular ANTES de radicar.
7. Confirmar radicación dentro del plazo, archivar respuesta + anexos + constancia, y registrar lecciones (qué conceptos cuestionó la UGPP → insumo preventivo para `liquidar-nomina-periodica`).

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Expediente probatorio completo | Cubre el 100 % de los periodos/conceptos requeridos; matriz hecho → prueba sin vacíos o con vacíos explícitos e informados a DefensaTributaria |
| Respuesta radicada en plazo | Constancia de radicación archivada; aprobación del Contador Titular previa |
| Registro de lecciones | Conceptos cuestionados incorporados a los controles preventivos del perfil |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Cliente reenvía el requerimiento con días de retraso | Correo físico/electrónico desatendido | Recalcular el plazo restante real y comprimir el cronograma interno | Si el plazo restante es insuficiente para una respuesta completa, DefensaTributaria evalúa solicitud de prórroga `[VERIFICAR procedencia]`; escalar a Contador Titular el mismo día |
| Soportes de periodos anteriores a la firma no existen | Cliente sin archivo histórico | Inventariar lo faltante, reconstruir lo reconstruible (PILA histórica de operadores, certificados de fondos) | Lo irreconstruible se informa a DefensaTributaria con precisión (la estrategia jurídica decide cómo tratarlo); NUNCA presentar soportes fabricados o "aproximados" |
| La cuantificación propia confirma (parcial o totalmente) la diferencia de la UGPP | El error sí existió | Informar con exactitud a DefensaTributaria y al Contador Titular: la decisión entre corregir/allanarse o controvertir es de ellos, sobre cifras exactas | — (la regla es no ocultar: el allanamiento temprano reduce sanciones) |
| Requerimiento sobre cálculos hechos por un tercero anterior | Periodos pre-servicio | Responder con la prueba disponible distinguiendo épocas de responsabilidad | DefensaTributaria define el tratamiento; documentar la frontera temporal con precisión |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Requerimiento recibido | Cualquiera | DefensaTributaria (coordinación inmediata) + Contador Titular informado el mismo día |
| Contingencia cuantificada | ≥ 50 UVT | Contador Titular en la mesa de estrategia |
| Contingencia cuantificada | ≥ 500 UVT | Contador Titular, mismo día, prioridad crítica (decisión de fondo es humana) |
| DefensaTributaria sin respuesta | Timeout 4 h | Orquestador (el plazo legal no se negocia) |

## Reglas críticas
🚫 NUNCA radicar una respuesta sin aprobación del Contador Titular ni redacción jurídica de DefensaTributaria (yo aporto la prueba, no la defensa).
🚫 NUNCA ocultar o maquillar un error propio confirmado en la cuantificación: las decisiones se toman sobre cifras exactas.
✅ SIEMPRE trabajar contra la fecha interna (plazo − 3 días hábiles): los requerimientos no admiten "casi a tiempo".

## Métricas
- Respuestas radicadas dentro del plazo legal: 100 %.
- Expedientes probatorios completos a la primera entrega a DefensaTributaria: ≥ 90 %.
- Conceptos cuestionados convertidos en control preventivo del perfil: 100 % de los procedentes.

## Tests
### Test 1 — (normal) Requerimiento de información UGPP sobre IBC de 8 empleados en 6 periodos del año anterior, notificado ayer al cliente
**Output:** plazo registrado con fecha interna a −3 días hábiles; expediente armado el mismo día (liquidaciones, PILA con cruces $0, contratos, novedades soportadas); matriz hecho → prueba completa; entrega a DefensaTributaria; revisión técnica del borrador, aprobación del Contador Titular y radicación con constancia 4 días antes del vencimiento; lecciones registradas.
### Test 2 — (excepción) Requerimiento para corregir: la UGPP alega pagos no salariales por encima del 40 % (Art. 30 Ley 1393/2010) en un año en que la firma aún no atendía al cliente, y el cliente reenvía la notificación 6 días después de recibida
**Output:** plazo restante real recalculado (comprimido); inventario de soportes históricos: bonificaciones pactadas reconstruidas parcialmente desde extractos y otrosíes del cliente; cuantificación propia CONFIRMA exceso del tope en 2 trimestres (≈ 120 UVT → Contador Titular en la mesa); informe exacto a DefensaTributaria distinguiendo la época de responsabilidad del tercero anterior; DefensaTributaria evalúa allanamiento parcial vs controversia y la prórroga `[VERIFICAR procedencia]`; radicación dentro del plazo con constancia; el control preventivo del 40 % se refuerza para TODOS los clientes del perfil.

═══════════════════════════════════════════════════════════════════════

## Relacionado
- *MOC - Agentes RITORE*
- *Proyecto - Ecosistema RITORE*
- [[00 - Estandar de Agentes RITORE]]
- [[Skills Compartidas RITORE]]
- [[04-AuxiliarFacturacionElectronica-Senior]]
- [[06-AuxiliarTesoreria-Senior]]
- *12-EspecialistaRetenciones-Senior*
- *18-DefensaTributaria-Master*
- [[Reforma Laboral Ley 2466 de 2025]]
- [[Aux 11 - Causacion de Nomina]]
- [[Aux 12 - Provisiones y Prestaciones Sociales]]
- [[Seguridad Social y Parafiscales]]

## Historial de versiones
| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-05-19 | Versión inicial consolidada (12 skills) | RITORE |
| 2.0 | 2026-06-11 | Refactorización según Estandar de Agentes v1.0: 12 → 11 skills (`liquidar-nomina-mensual` + `liquidar-nomina-quincenal` consolidadas en `liquidar-nomina-periodica` con variantes; `aplicar-jornada-Ley-2101-2021` ampliada a `verificar-parametros-laborales-vigentes` como paso bloqueante previo a toda liquidación, con los hitos de la Reforma Laboral Ley 2466/2025: dominical 90 % desde 01/07/2026 y jornada 42 h desde 15/07/2026); eliminación de auto-corrección y reglas críticas clonadas (lo común se hereda de Skills Compartidas); secciones §2 completas, tablas Error-Causa-Acción-Fallback y umbrales §3 en todas las skills; tests propios por skill; SMMLV 2026 $1.750.905 y referencias a la lección Aux 11 de la Escuela | RITORE |
