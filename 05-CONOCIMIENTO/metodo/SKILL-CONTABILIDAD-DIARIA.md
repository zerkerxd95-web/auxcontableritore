---
name: ejecutar-ciclo-contable-diario
description: Usar SIEMPRE para el ciclo contable operativo de cualquier empresa colombiana; recepción y verificación de soportes, causación de facturas de venta y compra, documento soporte a no obligados, recibos de caja, comprobantes de egreso, notas crédito/débito, registro en libros, verificación del balance de prueba y cierre contable del mes. Activar cuando se mencione causar, contabilizar, registrar, asiento, comprobante, libro auxiliar, balance de prueba, partida doble, PUC, o "poner al día la contabilidad". Es el motor del sistema; sin contabilidad limpia no hay impuestos ni estados financieros confiables.
---

> ## FASE 0 — Protocolo del método (obligatorio antes de cualquier otra fase)
>
> 1. **Candado de valores:** carga `06-NORMATIVA/VALORES-VIGENTES.md`. La UVT, el SMMLV, el auxilio, las bases y los valores en pesos salen SOLO de esa tabla; los topes expresados en UVT dentro de esta skill se convierten con la UVT del candado. Si un valor necesario no está en el candado o la tabla está vencida (año gravable posterior a su vigencia), DETENTE y pide al titular verificarlo contra la fuente oficial. Nunca uses valores de memoria.
> 2. **Estándar de entregables:** todo lo que produzcas cumple `03-METODO/ESTANDAR-DE-ENTREGABLES.md` (entregables E1–E8 y su control de calidad). Nada genérico: cliente con nombre y NIT, período, fuente de cada cifra, conclusión con criterio y salvedades explícitas.
> 3. **Carpetas del método:** insumos a `01-INSUMOS/` (jamás se editan), papeles de trabajo a `02-TRABAJO/`, entregables y acuses a `03-SALIDA/`, registro de diferencias y decisiones a `04-TRAZAS/`. (Si esta skill define una estructura interna propia de campaña, esa estructura vive DENTRO de 02-TRABAJO y 03-SALIDA.)
> 4. **Umbral de materialidad:** toda diferencia >= 1 UVT o >= 0,5 % se investiga y documenta antes de avanzar. Antes de entregar, mide el error sobre muestra (el 2 % de los registros de mayor valor + 1 % aleatorio): si el error supera el 2 %, la entrega se BLOQUEA y se corrige en la fuente.
> 5. **Insumo faltante:** pide todo lo que falte de una sola vez, con lista completa. Si a las 24 horas hábiles no llega, reitera con alerta de vencimiento al titular. Nunca avances sobre supuestos sin marcarlos como tales.
> 6. **Tú preparas y validas; el titular revisa y firma.** Nada se da por presentado sin su aprobación expresa.


# Ejecutar el Ciclo Contable Diario (RITORE OS)

Ejecuta el ciclo contable completo del período: del soporte al asiento, del asiento al libro, del libro al balance de prueba verificado. Es la skill del trabajo de auxiliar hecho con rigor de senior — y la base de la que se alimentan TODAS las demás skills del sistema.

---

## 1. POR QUÉ NO PUEDE FALLAR

- **Todo lo demás se construye sobre esto:** un asiento mal causado hoy es un cruce de IVA descuadrado este bimestre, una exógena con diferencias el próximo año y una renta indefendible después.
- La contabilidad es prueba (Arts. 772–774 ET): llevada en debida forma es la defensa del contribuyente; descuidada, es la evidencia en su contra.
- El costo del desorden es exponencial: causar bien toma minutos; reconstruir un mes mal causado toma días.

**Lema:** *cada registro con soporte, cada soporte al PUC correcto, cada tercero identificado, y el balance cuadrado ANTES de que nadie liquide nada sobre él.*

---

## 2. CUÁNDO SE ACTIVA

Procesamiento periódico de documentos de un cliente (semanal/quincenal/mensual); puesta al día de una contabilidad atrasada; verificación de la contabilidad de un cliente nuevo; y como **prerrequisito** del bucle de impuestos recurrentes.

---

## 3. MARCO DE REFERENCIA

| Tema | Fuente |
|------|-------|
| Plan Único de Cuentas comerciantes | Decreto 2650/1993 (estructura clase-grupo-cuenta-subcuenta) |
| Libros y comprobantes | Código de Comercio arts. 48–60 |
| Soportes válidos (FE, documento soporte, equivalentes) | Art. 771-2 ET + resoluciones DIAN de facturación |
| Reconocimiento contable | NIIF PYMES (devengo, Secciones 2, 23) |
| La contabilidad como prueba | Arts. 772–774 ET |

**El PUC en una línea por clase:** 1 Activo · 2 Pasivo · 3 Patrimonio · 4 Ingresos · 5 Gastos · 6 Costos de ventas · 7 Costos de producción · 8/9 cuentas de orden. Naturaleza débito: 1, 5, 6, 7. Naturaleza crédito: 2, 3, 4. *(Lecciones Aux 01–02 de la Escuela para formar al auxiliar en esto.)*

---

## 4. PROCEDIMIENTO MAESTRO

### FASE 1 — Recepción y verificación de soportes
1. Clasificar lo recibido: facturas de venta, facturas de compra (FE recibidas), documentos soporte a no obligados, extractos, planillas de nómina, recibos y egresos.
2. **Verificar cada soporte ANTES de causar:** ¿es del cliente (NIT correcto)? ¿del período? ¿factura electrónica válida (existe en el token) o documento soporte bien emitido? ¿tercero identificado con NIT y DV?
3. Lo que no tiene soporte válido NO se causa como deducible — se registra la operación si es real, pero marcada, y se informa al cliente (Art. 771-2: sin soporte no hay costo fiscal).
4. **El token DIAN es el checklist de completitud:** toda factura del token debe terminar causada; toda factura causada debe existir en el token. La lista de faltantes de cada período se trabaja, no se ignora.

### FASE 2 — Causación (los 7 movimientos que cubren el 95 % del trabajo)

| Documento | Esquema del asiento | Trampas frecuentes |
|---|---|---|
| **Factura de venta** | CxC/caja (D) — Ingreso (C) + IVA generado 2408 (C) − ReteFuente que me practican 1355 (D) | El ingreso SIN IVA; la retención es del pagador, no mía |
| **Factura de compra/gasto** | Gasto/costo/inventario (D) + IVA descontable 2408 (D) — CxP/banco (C) − retención practicada 2365 (C) | Base y IVA separados; verificar si el IVA es descontable o mayor valor (según régimen y destino) |
| **Documento soporte a no obligado** | Igual a compra, con el documento soporte como respaldo | Sin documento soporte emitido, el gasto no es deducible |
| **Nómina** | Gasto 5105/7205 (D) — por pagar 25xx (C) + descuentos empleado (C) + aportes por pagar 2370/2380 (C) | El gasto real es salario + carga prestacional; los descuentos NO son gasto |
| **Recibo de caja** | Banco/caja (D) — CxC (C) | Aplicar al tercero y factura correctos; los "pagos sin identificar" son deuda técnica |
| **Comprobante de egreso** | CxP (D) — Banco (C) | Cruzar contra la factura causada; no crear el gasto dos veces |
| **Notas crédito/débito** | Reversan o ajustan la operación original con su misma estructura | La NC de venta reversa ingreso E IVA; jamás se borra el asiento original |

**Reglas de causación innegociables:** partida doble siempre (todo asiento cuadra solo) · fecha del período correcto (corte estricto de mes) · tercero SIEMPRE (un movimiento sin tercero es un problema futuro en exógena) · centro de costos si el cliente los maneja · descripción que un tercero entienda en un año.

### FASE 3 — Registro y libros
Asientos al software contable; verificación de que el consecutivo de comprobantes no tiene huecos; libro auxiliar generado y **cuadrado (total débitos = total créditos — SIEMPRE)**.

### FASE 4 — Verificación del período (antes de entregar a impuestos)
1. Balance de prueba: D = C.
2. **Naturalezas:** ningún activo en crédito ni pasivo en débito sin explicación documentada.
3. Bancos contra extracto (la conciliación formal la hace el bucle mensual; aquí se verifica que lo evidente esté registrado).
4. Token vs causado: lista de faltantes en cero o documentada.
5. Cuentas puente y transitorias en cero o justificadas.
6. CxC y CxP por tercero sin saldos "sin identificar".
7. IVA y retenciones del período coherentes (2408 y 2365 con los movimientos esperados).

### FASE 5 — Entrega y encadenamiento
El balance verificado se entrega al bucle de impuestos recurrentes (SKILL-IMPUESTOS-RECURRENTES) y al cierre de EEFF. **Contabilidad no verificada = nada aguas abajo.** Pendientes del período (soportes faltantes, saldos por aclarar) quedan en lista con responsable y fecha.

---

## 5. PUESTA AL DÍA DE CONTABILIDAD ATRASADA (protocolo especial)

1. Diagnóstico: ¿desde cuándo? ¿qué hay (extractos, token, facturas físicas)? ¿el año anterior está cerrado?
2. **Si el año anterior no está cerrado: trabajar con MOVIMIENTOS del período, no saldos acumulados** (lección de campo — evita arrastrar basura).
3. Reconstruir por fuentes objetivas en este orden: token DIAN (ventas y compras) → extractos (pagos y recaudos) → nómina (planillas PILA) → lo demás.
4. Causar cronológicamente por mes, verificando cada mes antes del siguiente.
5. Documentar TODO lo reconstruido con criterio y limitación (qué no se pudo soportar).

## 6. REGLAS CRÍTICAS

🚫 **NUNCA:** causar sin soporte válido · registrar sin tercero · saltarse el corte del período · borrar asientos (se reversan con nota) · dejar el balance descuadrado "para después" · inventar contrapartidas para cuadrar (el descuadre se investiga, no se esconde) · causar en el NIT del empleado lo que es de la entidad (EPS, fondos).

✅ **SIEMPRE:** token como checklist de completitud · partida doble verificada · naturalezas revisadas antes de entregar · pendientes por escrito con responsable · lo dudoso se pregunta al cliente y su respuesta se documenta en la ficha.

## 7. TESTS

**Test 1 — Semana estándar.** Lote de 40 facturas de compra, 25 de venta, nómina y extractos. Resultado: todo causado con soporte y tercero, token cuadrado, balance D=C, lista de pendientes (2 facturas sin soporte) informada al cliente.

**Test 2 — Factura sin soporte.** El cliente pide causar un gasto grande "que ya casi llega la factura". Resultado: no se causa como deducible sin soporte; se documenta la instrucción del cliente y la advertencia del Art. 771-2.

**Test 3 — Balance con pasivo en débito.** Resultado: la Fase 4 lo detecta, rastrea la causa (anticipo mal aplicado), corrige con nota y documenta — no se entrega a impuestos hasta resolver.

**Test 4 — Contabilidad 8 meses atrasada.** Resultado: protocolo de puesta al día por fuentes objetivas, mes a mes, con informe de limitaciones y plan al cliente.

---

**FIN DE LA HABILIDAD** — Se apoya en: Escuela Aux 01–10 y 23–25 (formación del auxiliar) y plantillas `22_Causacion_Contable_y_Libros`, `23_Facturacion_Compra_y_Venta`, `24_PUC_Interactivo`, `10_Interpretacion_Token_DIAN`.
