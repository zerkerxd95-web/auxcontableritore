---
name: liquidar-nomina-y-seguridad-social
description: Usar SIEMPRE para la nómina de cualquier empleador colombiano; liquidación mensual (devengados, deducciones, horas extra y recargos), provisiones de prestaciones sociales, PILA, nómina electrónica DIAN, liquidaciones definitivas de contrato y los pagos anuales (prima, cesantías, intereses). Activar cuando se mencione nómina, salario, PILA, planilla, prestaciones, cesantías, prima, vacaciones, liquidación de contrato, nómina electrónica, horas extra, o seguridad social. Liquida con las reglas laborales vigentes y protege la deducibilidad del gasto laboral (Art. 108 ET).
---

> ## FASE 0 — Protocolo del método (obligatorio antes de cualquier otra fase)
>
> 1. **Candado de valores:** carga `06-NORMATIVA/VALORES-VIGENTES.md`. La UVT, el SMMLV, el auxilio, las bases y los valores en pesos salen SOLO de esa tabla; los topes expresados en UVT dentro de esta skill se convierten con la UVT del candado. Si un valor necesario no está en el candado o la tabla está vencida (año gravable posterior a su vigencia), DETENTE y pide al titular verificarlo contra la fuente oficial. Nunca uses valores de memoria.
> 2. **Estándar de entregables:** todo lo que produzcas cumple `03-METODO/ESTANDAR-DE-ENTREGABLES.md` (entregables E1–E8 y su control de calidad). Nada genérico: cliente con nombre y NIT, período, fuente de cada cifra, conclusión con criterio y salvedades explícitas.
> 3. **Carpetas del método:** insumos a `01-INSUMOS/` (jamás se editan), papeles de trabajo a `02-TRABAJO/`, entregables y acuses a `03-SALIDA/`, registro de diferencias y decisiones a `04-TRAZAS/`. (Si esta skill define una estructura interna propia de campaña, esa estructura vive DENTRO de 02-TRABAJO y 03-SALIDA.)
> 4. **Umbral de materialidad:** toda diferencia >= 1 UVT o >= 0,5 % se investiga y documenta antes de avanzar. Antes de entregar, mide el error sobre muestra (el 2 % de los registros de mayor valor + 1 % aleatorio): si el error supera el 2 %, la entrega se BLOQUEA y se corrige en la fuente.
> 5. **Insumo faltante:** pide todo lo que falte de una sola vez, con lista completa. Si a las 24 horas hábiles no llega, reitera con alerta de vencimiento al titular. Nunca avances sobre supuestos sin marcarlos como tales.
> 6. **Tú preparas y validas; el titular revisa y firma.** Nada se da por presentado sin su aprobación expresa.


# Liquidar Nómina y Seguridad Social (RITORE OS)

Liquida el ciclo laboral completo: nómina mensual, aportes, provisiones, nómina electrónica, pagos anuales y liquidaciones de contrato — con la contabilización correcta y la vista fiscal siempre presente.

---

## 1. POR QUÉ NO PUEDE FALLAR

- **La UGPP fiscaliza con cruces automáticos** (PILA vs nómina vs renta): aportes mal liquidados son un pasivo oculto con sanciones propias.
- **Sin aportes pagados no hay deducción de salarios** (Art. 108 ET): una nómina con PILA en mora contamina la renta del año.
- Los errores laborales prescriben lento y se cobran caro: una liquidación de contrato mal hecha aparece en una demanda tres años después.
- **Sin nómina electrónica transmitida, el costo laboral no es soportable ante la DIAN** para quienes están obligados.

**Lema:** *lo que se paga al trabajador, lo que se aporta al sistema y lo que se deduce en renta son TRES vistas del mismo hecho — y tienen que cuadrar entre sí.*

---

## 2. CUÁNDO SE ACTIVA

Liquidación mensual/quincenal de nómina; PILA del período; transmisión de nómina electrónica; ingreso o retiro de un trabajador (liquidación definitiva); pagos anuales (prima jun/dic, cesantías feb, intereses ene); consolidación anual para renta, exógena (F-2276) y certificados.

---

## 3. MARCO NORMATIVO (verificar valores de CADA año)

| Tema | Fuente |
|------|-------|
| Contrato, jornada, recargos, prestaciones | Código Sustantivo del Trabajo + reforma laboral vigente `[VERIFICAR régimen de jornada y recargos vigente — ha cambiado por reforma reciente]` |
| SMMLV y auxilio de transporte | Decreto de cada enero `[VERIFICAR]` |
| Seguridad social (%, topes, FSP) | Ley 100/1993 + normas PILA (tope base: 25 SMMLV; FSP desde 4 SMMLV) |
| Parafiscales y exoneración | Art. 114-1 ET (exoneración de salud, SENA e ICBF para trabajadores < 10 SMMLV en obligados a renta `[VERIFICAR condiciones]`) |
| Deducibilidad de salarios | Art. 108 ET (aportes pagados como requisito) |
| Nómina electrónica | Resolución DIAN vigente (transmisión mensual) |
| Retención laboral | Art. 383/388 ET (procedimiento 1 o 2, depuración con rentas exentas) |
| Salario integral | Art. 132 CST (≥ 10 SMMLV + factor 30 %; sin prestaciones, aportes sobre el 70 %) |

## 4. LOS NÚMEROS QUE NO SE PUEDEN ERRAR

**Aportes sobre el IBC (base = salario + variables; el auxilio de transporte NO hace base de seguridad social pero SÍ de prestaciones):**

| Concepto | Empleador | Trabajador |
|---|---|---|
| Salud | 8,5 % (exonerable Art. 114-1) | 4 % |
| Pensión | 12 % | 4 % (+FSP 1–2 % desde 4 SMMLV) |
| ARL | 0,522 %–6,96 % según riesgo | — |
| Caja de compensación | 4 % | — |
| SENA + ICBF | 2 % + 3 % (exonerables) | — |

**Provisiones mensuales (sobre base prestacional = salario + auxilio de transporte):** cesantías 8,33 % · intereses sobre cesantías 1 % · prima 8,33 % · vacaciones 4,17 % (sobre salario sin auxilio).

**Recargos** `[VERIFICAR % vigentes por la reforma laboral]`: extra diurna, extra nocturna, recargo nocturno, dominical/festivo — liquidar con la tabla vigente a la fecha de cada turno, no con la del año pasado.

**Calendario anual fijo:** intereses de cesantías → 31 de enero · consignación de cesantías al fondo → 14 de febrero · prima → 30 de junio y 20 de diciembre · dotación → 3 entregas/año para quienes ganan hasta 2 SMMLV.

## 5. PROCEDIMIENTO MAESTRO

### FASE 1 — Novedades del período
Recopilar ANTES de liquidar: ingresos/retiros, incapacidades (quién paga qué: empleador días 1–2, EPS desde el 3º al 66,67 % `[VERIFICAR]`), licencias, vacaciones disfrutadas, horas extra autorizadas, variables (comisiones, bonificaciones — ¿constitutivas de salario?), préstamos y libranzas. Sin novedades confirmadas por el cliente NO se liquida.

### FASE 2 — Liquidación
Por trabajador: devengados (salario, auxilio si aplica, extras con recargo vigente, variables) − deducciones (salud 4 %, pensión 4 %, FSP, retención Art. 383 si aplica, libranzas autorizadas) = neto. Verificar mínimos legales (nadie por debajo del SMMLV proporcional; deducciones sin autorización escrita, jamás).

### FASE 3 — PILA
IBC por trabajador (mínimo 1 SMMLV, tope 25; independientes sobre el 40 % del ingreso con piso 1 SMMLV). Planilla del período pagada dentro del plazo por dígito. **PILA paga = requisito de deducción (Art. 108) y de exoneración (114-1).**

### FASE 4 — Contabilización y provisiones
Asiento de nómina (gasto/costo por centro, por pagar, descuentos, aportes) + asiento de provisiones mensuales. Las cuentas de provisión (2510, 2515, 2520, 2525) DEBEN moverse cada mes — una prestación sin provisionar es un pasivo oculto en los EEFF.

### FASE 5 — Nómina electrónica
Transmitir el documento soporte de nómina del mes a la DIAN dentro del plazo; ajustes por notas de ajuste, no retransmisiones informales. Guardar el CUNE/acuse. **Cruce obligatorio: nómina electrónica = nómina contabilizada = PILA.**

### FASE 6 — Eventos especiales
- **Liquidación definitiva de contrato:** cesantías + intereses + prima + vacaciones proporcionales a la fecha exacta + indemnización si aplica (según tipo de contrato y causa). Paz y salvo, examen de egreso, reporte de retiro en PILA y EPS. Doble verificación SIEMPRE (es el cálculo más demandado).
- **Pagos anuales:** prima, consignación de cesantías, intereses — contra las provisiones acumuladas (la provisión bien llevada hace estos pagos indoloros).
- **Consolidación anual:** certificados de ingresos y retenciones (F-220) a cada trabajador, insumo del F-2276 de exógena (con las reglas del manual: cesantías por criterio de caja, salud/pensión del empleado por valor real).

## 6. CONTROL DE CALIDAD

1. Nómina = PILA = nómina electrónica = contabilidad (una sola verdad en 4 vistas).
2. IBC correctos (variables incluidas; auxilio fuera de seguridad social).
3. Provisiones al día y cuadradas contra el pasivo.
4. Retención laboral depurada según procedimiento elegido, documentado.
5. Novedades soportadas (incapacidades con certificado, extras autorizadas).
6. Calendario anual agendado en el Control de Obligaciones.

## 7. REGLAS CRÍTICAS

🚫 **NUNCA:** liquidar sin novedades confirmadas · deducir del salario sin autorización escrita · pagar por debajo de los mínimos · dejar PILA en mora y deducir los salarios en renta como si nada · liquidar un retiro sin doble verificación · usar tablas de recargos desactualizadas · tratar como "no salarial" lo que se paga habitual y remunerativamente (la UGPP lo reclasifica).

✅ **SIEMPRE:** cruzar nómina-PILA-electrónica-contabilidad cada mes · provisionar mensualmente · verificar la exoneración 114-1 antes de aplicarla · documentar la naturaleza de cada pago variable · agendar los pagos anuales desde enero.

## 8. TESTS

**Test 1 — Mes estándar.** 12 trabajadores, 2 con extras, 1 incapacidad. Resultado: liquidación con recargos vigentes, incapacidad repartida correctamente, PILA pagada en plazo, nómina electrónica transmitida, asientos y provisiones registrados, cruce de 4 vistas limpio.

**Test 2 — Retiro con indemnización.** Contrato indefinido terminado sin justa causa. Resultado: liquidación definitiva a fecha exacta, indemnización según tabla vigente, doble verificación documentada, retiros reportados.

**Test 3 — PILA en mora en cierre de renta.** Resultado: alerta de que los salarios del período en mora no son deducibles (Art. 108); cuantificación del efecto y plan de pago antes de presentar renta.

**Test 4 — Bonificación mensual "no salarial".** El cliente paga hace un año una bonificación fija mensual pactada como no salarial. Resultado: advertencia del riesgo UGPP (habitualidad = salario), cuantificación del contingente y recomendación escrita.

---

**FIN DE LA HABILIDAD** — Plantilla de apoyo: `08_Nomina_y_Prestaciones_Sociales.xlsx`. Formación del auxiliar: Escuela Aux 11–13.

## COMPLEMENTO V2 — Fases con validación bloqueante y entregables

| Fase | Qué se hace | Validación BLOQUEANTE antes de avanzar |
|---|---|---|
| N1. Novedades | Recibir novedades del período (ingresos, retiros, extras, incapacidades, licencias, vacaciones) | Confirmación ESCRITA del cliente; sin confirmación no se liquida |
| N2. Liquidación | Devengados, deducciones, provisiones por trabajador | Neto >= mínimos legales · suma devengados - deducciones = suma netos · auxilio solo <= 2 SMMLV (candado) |
| N3. PILA | Liquidar y pagar la planilla | IBC por trabajador = base de nómina · planilla PAGADA (no solo liquidada) antes de continuar |
| N4. Contabilización | Causar nómina y provisiones | Gasto contable del mes = nómina + provisiones (cuadre al peso contra N2) |
| N5. Nómina electrónica | Transmitir a la DIAN | CUNE de cada documento archivado en 03-SALIDA (sin NE transmitida peligra la deducción del costo laboral en renta) |

**Entregables:** papel de liquidación por trabajador (E1) y resumen de nómina para el cliente (E8: total devengado, deducido, neto, seguridad social, provisiones — con variación vs. mes anterior explicada) en 02-TRABAJO/03-SALIDA; comprobante contable; certificado de la PILA y CUNEs en 03-SALIDA.
