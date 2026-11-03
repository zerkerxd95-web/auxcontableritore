---
tipo: agente
tags: [ritore, agente, operativa]
capa: operativa
nivel: senior
estado: activo
version: 2.0
fecha: 2026-06-11
---

# SKILLS — 04-AuxiliarFacturacionElectronica-Senior

**Documento consolidado** · 9 skills · Ecosistema RITORE · v2.0
**Modelo:** claude-opus-4-7

> Refactorización según [[00 - Estandar de Agentes RITORE]] (§2 secciones obligatorias, §3 umbrales, §4 anti-clonación). Hallazgos de auditoría corregidos: (a) la auto-corrección clonada en las 10 skills y las reglas críticas idénticas en 13 posiciones se eliminaron — lo común (escalar a humano, consulta a especialista, documentar decisiones, verificación de vigencia normativa) se hereda de [[Skills Compartidas RITORE]] y en cada skill solo queda lo diferencial; (b) `generar-nota-credito-debito` y `notificar-factura-no-conforme-cliente` compartían > 70 % del procedimiento (ambas terminan en NC/ND referenciando el CUFE original) y se consolidaron en `corregir-factura-emitida-NC-ND` con tabla de variantes; (c) se agregaron fallbacks reales que la v1.0 no tenía: reintento con backoff 5 m / 10 m / 20 m ante timeout DIAN, protocolo de contingencia si el servicio DIAN está caído, hold de 24 h + corrección con el cliente ante rechazo persistente (3 retransmisiones rechazadas) y trámite de nueva resolución cuando la numeración autorizada baja del 20 %; (d) umbrales numéricos según §3 — el umbral "> 2 UVT" del cruce RADIAN v1.0 se alinea al estándar (≥ 1 UVT individual o ≥ 0,5 % del total). El rigor técnico original (UBL 2.1, CUFE SHA-384, CUDE, RADIAN, validación previa DIAN) se conserva y se amplía.
>
> **Valores de referencia 2026:** UVT = $52.374.

---

## Índice de skills en este documento

- `validar-factura-emitida-CUFE` *(núcleo: validación previa + transmisión)*
- `gestionar-rechazo-DIAN` *(reintentos con backoff, contingencia, rechazo persistente)*
- `corregir-factura-emitida-NC-ND` *(consolida generación de NC/ND + notificación de factura no conforme)*
- `procesar-factura-recibida-RADIAN`
- `emitir-documento-soporte-no-obligado`
- `cruzar-radian-vs-libros`
- `consultar-RUT-DIAN-emisor`
- `auditar-numeracion-autorizada`
- `transmitir-nomina-electronica`

═══════════════════════════════════════════════════════════════════════

---
name: validar-factura-emitida-CUFE
description: Activa antes de transmitir cada factura emitida a DIAN. Valida estructura UBL 2.1, calcula y verifica CUFE (SHA-384), verifica receptor en RUT, valida IVA y retenciones, y transmite vía proveedor tecnológico bajo el modelo de validación previa. Sin esta skill las facturas salen con errores y la DIAN las rechaza.
agente: RITORE-AuxiliarFacturacionElectronica-Senior
categoria: operativo
---

# Skill: validar-factura-emitida-CUFE

## Para qué existe
Bajo el modelo de **validación previa**, una factura solo existe fiscalmente cuando la DIAN la valida: esta skill garantiza que cada documento llegue a la DIAN técnicamente impecable (UBL 2.1 + CUFE + receptor verificado) y gestiona la transmisión. Sin ella, el cliente factura "papel mojado" y pierde el soporte de sus ingresos.

## Cuándo se activa
- Solicitud de emisión de factura del cliente (vía AtencionCliente o flujo automatizado del ERP).
- Lote de facturación periódica programada del cliente.
- Retransmisión solicitada por `gestionar-rechazo-DIAN` tras una corrección.

## Inputs

| Insumo | De quién | Formato | Si falta |
|---|---|---|---|
| Datos de la operación: receptor, ítems, valores, IVA, forma de pago | Cliente / ERP | Estructurado | Solicitar al cliente vía AtencionCliente; espera máx. 24 h hábiles, reiterar 1 vez, luego Orquestador |
| Resolución de numeración vigente y consecutivo disponible | `auditar-numeracion-autorizada` | Rango autorizado | NO emitir sin numeración vigente; activar `auditar-numeracion-autorizada` en modo urgente |
| Estado del receptor en RUT | `consultar-RUT-DIAN-emisor` | Ficha RUT | Timeout 4 h → usar última consulta cacheada con marca `[DATO EN CACHÉ — verificar]` y reverificar tras la transmisión |
| Tarifa de retención aplicable (si receptor es agente retenedor) | EspecialistaRetenciones | Concepto | Timeout 4 h → factura queda `en espera`; NUNCA calcular tarifas yo mismo |

## Procedimiento
1. Validar estructura **UBL 2.1** obligatoria: campos del anexo técnico vigente, identificación completa de las partes, unidades y códigos de producto.
2. Calcular el **CUFE (SHA-384)** con los elementos del anexo técnico y verificar que coincida con el embebido en el XML.
3. Verificar receptor en RUT DIAN: activo, régimen, calidad de agente retenedor y de gran contribuyente (vía `consultar-RUT-DIAN-emisor`).
4. Validar IVA por ítem según naturaleza del producto/servicio; en operación atípica (exenta/excluida dudosa, AIU, moneda extranjera), consultar a EspecialistaIVA antes de transmitir.
5. Si el receptor es agente retenedor, validar que las retenciones informadas correspondan al concepto definido por EspecialistaRetenciones.
6. Verificar que el consecutivo pertenezca al rango de la resolución vigente y notificar el consumo a `auditar-numeracion-autorizada`.
7. Transmitir vía proveedor tecnológico autorizado y esperar el `ApplicationResponse` de la DIAN.
8. Con validación exitosa: archivar XML + representación gráfica vía NotionArquitecto y notificar a AuxContable (causación) y a CarteraCxP (cuenta por cobrar).
9. Con rechazo: entregar el caso completo (XML, mensaje de error, intentos) a `gestionar-rechazo-DIAN`.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Factura validada por DIAN | `ApplicationResponse` con estado "Documento validado por la DIAN" y CUFE verificado |
| XML + representación gráfica archivados | Convención canónica vía NotionArquitecto, inmutables |
| Notificaciones a AuxContable y CarteraCxP | Emitidas el mismo día hábil de la validación |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| CUFE calculado ≠ CUFE embebido en el XML | Error de armado del XML o campo del anexo técnico desactualizado | Recalcular desde los datos fuente y regenerar el XML; NUNCA transmitir con CUFE inconsistente | Si el recálculo no converge, verificar versión del anexo técnico vigente con `verificar-vigencia-normativa` y escalar a Orquestador como incidencia técnica |
| Timeout del servicio DIAN al transmitir | Intermitencia del servicio de validación | Reintentar con backoff **5 m → 10 m → 20 m** (3 reintentos) | Si tras el 3.er reintento persiste, tratar como servicio caído: encolar la factura, verificar si la DIAN declaró contingencia y seguir el protocolo de contingencia del anexo técnico (emisión en contingencia y transmisión dentro de las 48 h siguientes al restablecimiento `[VERIFICAR plazo del anexo técnico vigente]`); alertar al Orquestador si la caída supera 4 h |
| Receptor inactivo o NIT inexistente en RUT | Datos errados del cliente o tercero recién cancelado | Detener la emisión y solicitar verificación del NIT al cliente (24 h hábiles) | Si el cliente confirma el NIT y el RUT sigue inconsistente, consulta directa en portal DIAN y escalamiento a Orquestador (posible suplantación o error del RUT) |
| Operación con IVA ambiguo | Producto/servicio de clasificación dudosa | Consultar a EspecialistaIVA (skill compartida `consultar-a-especialista`) antes de transmitir | Timeout 4 h del especialista → factura `en espera`; NUNCA transmitir con tratamiento de IVA improvisado |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia entre valores de la factura y soporte de la operación | ≥ 1 UVT individual o ≥ 0,5 % del total del documento | Investigar y documentar antes de transmitir |
| Inconsistencia tributaria detectada en la emisión | ≥ 50 UVT | EspecialistaIVA (Master del dominio) |
| Inconsistencia o riesgo acumulado | ≥ 500 UVT | Contador Titular vía Orquestador |
| Servicio DIAN caído | > 4 h continuas | Orquestador (riesgo operativo de todos los clientes emisores) |

## Reglas críticas
🚫 NUNCA transmitir sin CUFE validado contra recálculo propio.
🚫 NUNCA calcular tarifas de retención (eso es EspecialistaRetenciones) ni definir tratamiento de IVA atípico (eso es EspecialistaIVA).
✅ SIEMPRE verificar el receptor en RUT antes de transmitir, no después.

## Métricas
- Tasa de rechazo DIAN sobre documentos transmitidos: < 1 % (medición mensual).
- Facturas transmitidas dentro de las 4 h siguientes a la solicitud completa: ≥ 95 %.
- Documentos archivados con XML + representación gráfica: 100 %.

## Tests
### Test 1 — (normal) Factura de servicios por $8,4M a receptor gran contribuyente y agente retenedor, IVA 19 %
**Output:** UBL 2.1 validado; CUFE recalculado = CUFE embebido; receptor verificado activo en RUT con calidad de agente retenedor → retenciones validadas contra concepto de EspecialistaRetenciones; transmisión y `ApplicationResponse` exitoso; XML archivado; AuxContable y CarteraCxP notificados el mismo día.
### Test 2 — (excepción) Al transmitir un lote de 35 facturas, el servicio DIAN responde timeout en los 3 reintentos (5 m/10 m/20 m)
**Output:** lote encolado sin pérdida; verificación del estado del servicio DIAN → caída general confirmada; activación del protocolo de contingencia del anexo técnico con marca `[VERIFICAR plazo de retransmisión]`; alerta al Orquestador a las 4 h de caída; al restablecerse el servicio, transmisión de la cola en orden y verificación de los 35 `ApplicationResponse`; ninguna factura entregada al cliente como "validada" antes de su respuesta DIAN real.

═══════════════════════════════════════════════════════════════════════

---
name: gestionar-rechazo-DIAN
description: Activa cuando la DIAN rechaza un documento transmitido (factura, NC/ND, documento soporte). Analiza la causa, corrige o coordina la corrección con el cliente, retransmite con control de intentos y aplica el protocolo de rechazo persistente (hold de 24 h tras 3 rechazos). Sin esta skill los rechazos se reintentan a ciegas o se abandonan.
agente: RITORE-AuxiliarFacturacionElectronica-Senior
categoria: operativo
---

# Skill: gestionar-rechazo-DIAN

## Para qué existe
Un rechazo DIAN sin diagnóstico se convierte en bucle de retransmisiones inútiles o en factura nunca emitida. Esta skill convierte cada rechazo en una causa identificada, una corrección verificada y un límite claro de reintentos con salida definida.

## Cuándo se activa
- `ApplicationResponse` con estado de rechazo recibido para cualquier documento del perfil.
- Reporte de rechazo desde `transmitir-nomina-electronica` o `corregir-factura-emitida-NC-ND`.
- Patrón de rechazos repetidos detectado en la métrica mensual.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| XML transmitido + mensaje de rechazo completo (código y descripción) | Proveedor tecnológico / DIAN | Sin el mensaje de error no se diagnostica: recuperarlo del log del proveedor tecnológico antes de actuar |
| Historial de intentos del documento | Registro propio de la skill | Reconstruir desde los `ApplicationResponse` archivados |
| Datos corregidos (cuando la causa es del cliente) | Cliente vía AtencionCliente | Espera 24 h hábiles, reiterar 1 vez; el documento queda `en hold` mientras tanto |

## Procedimiento
1. Clasificar la causa del rechazo según el código DIAN: (a) técnica propia (CUFE/CUDE, estructura UBL, anexo técnico), (b) datos del receptor (NIT, régimen), (c) datos de la operación (códigos, valores, IVA), (d) numeración (resolución vencida o fuera de rango).
2. Causa técnica propia → corregir internamente, revalidar con `validar-factura-emitida-CUFE` y retransmitir. Contar el intento.
3. Causa de datos del cliente → notificar vía AtencionCliente con el detalle exacto de qué corregir; retransmitir solo con el dato corregido y soportado.
4. Causa de numeración → activar `auditar-numeracion-autorizada` en modo urgente antes de cualquier retransmisión.
5. **Control de intentos:** máximo 3 retransmisiones por documento. Al 3.er rechazo (es decir, antes de un 4.º intento) se activa el protocolo de rechazo persistente del paso 6.
6. **Rechazo persistente:** detener reintentos; poner el documento `en hold` por 24 h; solicitar al cliente la corrección/confirmación de datos de fondo vía AtencionCliente; escalar en paralelo a AuxContable (impacto en ingresos/causación del periodo) y registrar la causa raíz.
7. Documentar cada rechazo resuelto (causa → corrección → resultado) y reportar el patrón a NotionArquitecto para mejorar la pre-validación.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Documento retransmitido y validado | `ApplicationResponse` exitoso; máx. 3 retransmisiones |
| Registro causa raíz → corrección | Cada rechazo cerrado tiene código DIAN, diagnóstico y corrección aplicada |
| Casos en hold escalados | AuxContable notificado y cliente con solicitud de corrección dentro de las 24 h del 3.er rechazo |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Rechazo persistente (3 retransmisiones rechazadas) | Error de fondo en los datos del cliente o incompatibilidad con el anexo técnico | Hold de 24 h + solicitud de corrección de datos al cliente + escalamiento a AuxContable | Si a las 24 h el cliente no responde, reiterar 1 vez; a las 48 h, Orquestador con el expediente completo (riesgo de ingreso del periodo sin facturar) |
| Mismo código de rechazo en ≥ 3 documentos del mismo cliente en el mes | Error estructural de parametrización del cliente | Alertar al Contador Titular para revisión estructural (no corregir documento a documento) | Si la parametrización depende del ERP del cliente, gestión formal vía AtencionCliente con plazo definido |
| Rechazo por resolución de numeración vencida | Monitoreo de numeración falló o trámite atascado | Activar `auditar-numeracion-autorizada` urgente; NO retransmitir hasta resolución vigente | Facturación del cliente suspendida → escalar a Orquestador y Contador Titular el mismo día (impacto operativo total) |
| El proveedor tecnológico reporta validado pero la DIAN no registra el documento | Desincronización proveedor–DIAN | Verificar el CUFE directamente en el portal DIAN antes de dar por emitido | Si la inconsistencia persiste > 24 h, incidencia formal con el proveedor tecnológico y alerta al Orquestador |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Documento rechazado con impacto en el periodo | ≥ 1 UVT | Prioridad de gestión el mismo día hábil |
| Rechazo persistente (3 intentos) | Cualquier monto | Hold 24 h + cliente + AuxContable |
| Documentos en hold sin resolver | ≥ 50 UVT acumulado por cliente | EspecialistaIVA (Master) + Contador Titular informado |
| Facturación de un cliente bloqueada | > 48 h | Contador Titular vía Orquestador, prioridad alta |

## Reglas críticas
🚫 NUNCA hacer un 4.º intento de transmisión: al 3.er rechazo aplica el protocolo de rechazo persistente, sin excepciones.
🚫 NUNCA retransmitir sin haber corregido la causa exacta del código de rechazo.
✅ SIEMPRE registrar causa raíz y corrección: el patrón de rechazos alimenta la pre-validación.

## Métricas
- Rechazos resueltos en ≤ 1 retransmisión: ≥ 80 % (medición mensual).
- Documentos que llegan a rechazo persistente: ≤ 2 % de los rechazados.
- Rechazos con causa raíz documentada: 100 %.

## Tests
### Test 1 — (normal) Factura rechazada por código de producto inválido (causa de datos de la operación)
**Output:** causa clasificada como (c); corrección del código UNSPSC con el catálogo del cliente; revalidación CUFE y retransmisión exitosa al 1.er intento; causa raíz registrada y patrón reportado a NotionArquitecto.
### Test 2 — (excepción) Factura de $22M rechazada 3 veces: las dos primeras por NIT del receptor inconsistente y la tercera por régimen tributario que no coincide con el RUT
**Output:** al 3.er rechazo NO se intenta una 4.ª transmisión; documento `en hold` 24 h; solicitud formal al cliente vía AtencionCliente para confirmar los datos de fondo del receptor (posible RUT desactualizado del tercero); AuxContable escalado en paralelo (la causación del ingreso queda pendiente); a las 24 h el cliente aporta el RUT corregido del receptor → revalidación completa con `consultar-RUT-DIAN-emisor` y retransmisión exitosa; expediente con los 3 códigos de rechazo y la causa raíz archivado.

═══════════════════════════════════════════════════════════════════════

---
name: corregir-factura-emitida-NC-ND
description: Activa cuando una factura ya validada requiere ajuste — devolución, descuento posterior, corrección de error material — o cuando un error detectado exige además comunicación formal al cliente receptor. Emite nota crédito o nota débito referenciando el CUFE original y coordina la notificación. Consolida las antiguas skills de NC/ND y de notificación de factura no conforme (> 70 % de procedimiento común).
agente: RITORE-AuxiliarFacturacionElectronica-Senior
categoria: operativo
---

# Skill: corregir-factura-emitida-NC-ND

## Para qué existe
Una factura validada por la DIAN es inmutable: todo ajuste posterior solo existe legalmente como NC o ND referenciada al documento original. Esta skill garantiza que las correcciones tengan rastro fiscal completo y que, cuando el error es material, el receptor se entere formalmente — sin nota, el ajuste es contablemente inválido y tributariamente riesgoso.

## Cuándo se activa (por variante)

| Variante | Trigger |
|---|---|
| **NC — comercial** | Devolución de bienes, descuento posterior o anulación pactada reportada por el cliente |
| **ND — comercial** | Mayor valor posterior (intereses, fletes, ajuste de precio pactado) |
| **C — corrección por error material** | Error detectado internamente o por el receptor en una factura ya validada (valores, IVA, datos del receptor) — incluye la notificación formal al receptor |

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Factura origen con CUFE validado | Archivo propio (NotionArquitecto) | Sin CUFE de origen NO se emite nota; localizar el documento primero |
| Soporte del ajuste (acta de devolución, acuerdo de descuento, evidencia del error) | Cliente / detección propia | Solicitar vía AtencionCliente (24 h hábiles, reiterar 1 vez); la nota no se emite sin soporte |
| Tratamiento de IVA del ajuste | EspecialistaIVA (si el ajuste cambia bases o tarifas) | Timeout 4 h → nota `en espera`; el ajuste de IVA mal hecho contamina el F-300 |

## Procedimiento
1. Identificar la factura origen y verificar su CUFE en el archivo.
2. Determinar el tipo de nota: NC (anula o reduce) o ND (incrementa), y la variante (comercial o corrección).
3. Estructurar la nota UBL 2.1 con **referencia explícita al CUFE del documento original** y el código de motivo correcto del anexo técnico.
4. Calcular y validar el CUDE de la nota (mismo estándar de verificación que el CUFE: recálculo propio antes de transmitir).
5. Transmitir a la DIAN vía proveedor tecnológico (reintentos y rechazos se gobiernan por `validar-factura-emitida-CUFE` y `gestionar-rechazo-DIAN`).
6. **Solo variante C:** coordinar con AtencionCliente la comunicación formal al receptor: error detectado, nota emitida y efecto neto, antes de que el receptor registre la factura errada.
7. Notificar a AuxContable (asiento del ajuste) y a EspecialistaIVA (efecto en F-300 del periodo).
8. Archivar nota + soporte enlazados a la factura origen.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| NC/ND validada por DIAN | Referencia al CUFE origen + código de motivo correcto + CUDE verificado |
| Comunicación al receptor (variante C) | Emitida vía AtencionCliente el mismo día hábil de la nota |
| Notificaciones a AuxContable y EspecialistaIVA | Con el efecto neto del ajuste y el periodo afectado |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Nota emitida contra factura equivocada | Facturas similares del mismo receptor en el periodo | Emitir nota que reverse la nota errada y emitir la correcta contra el CUFE verdadero; documentar la cadena completa | Si la cadena de notas se vuelve ambigua, congelar y escalar a EspecialistaIVA antes de seguir emitiendo |
| Ajuste solicitado sin soporte | Cliente pide "borrar" una factura validada | Explicar que la factura validada es inmutable; exigir soporte del hecho económico (devolución/acuerdo) | Si el cliente insiste sin soporte, rechazar la emisión y escalar a Contador Titular (riesgo de anulación ficticia de ingresos) |
| El receptor ya registró la factura errada y declaró con ella | Notificación tardía del error | Emitir la nota y notificar formalmente con el efecto en el periodo del receptor | Si el efecto cruza periodos de IVA ya declarados, escalar a EspecialistaIVA para el tratamiento de la corrección del F-300 |
| Error material detectado ≥ 3 veces en el mes para el mismo cliente | Falla estructural en el origen de datos del cliente | Alertar al Contador Titular para revisión estructural | Gestión formal con el cliente vía AtencionCliente con plan de corrección |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Ajuste sobre factura validada | ≥ 1 UVT o ≥ 0,5 % del valor del documento origen | Verificar soporte y documentar antes de emitir |
| Efecto neto de notas del periodo | ≥ 50 UVT | EspecialistaIVA (Master) — efecto en F-300 |
| Anulaciones/ajustes acumulados de un cliente | ≥ 500 UVT en el trimestre | Contador Titular (patrón de reversión de ingresos) |
| Solicitud de anulación sin soporte | Cualquier monto | Contador Titular |

## Reglas críticas
🚫 NUNCA emitir NC/ND sin referencia explícita al CUFE/CUDE del documento original.
🚫 NUNCA "anular" una factura validada por fuera del mecanismo de notas (la factura validada es inmutable).
✅ SIEMPRE comunicar al receptor los errores materiales (variante C) antes de que registre el documento errado, vía AtencionCliente.

## Métricas
- Notas emitidas con referencia válida al documento origen: 100 %.
- Errores materiales comunicados al receptor el mismo día hábil: 100 %.
- Razón notas crédito / facturas emitidas por cliente: ≤ 5 % mensual (por encima, revisar causa estructural).

## Tests
### Test 1 — (normal, NC comercial) Cliente reporta devolución parcial de mercancía por $3,1M sobre una factura validada de $12,4M, con acta de devolución firmada
**Output:** NC parcial estructurada con referencia al CUFE origen y código de motivo "devolución parcial"; CUDE recalculado y verificado; transmisión exitosa; AuxContable y EspecialistaIVA notificados con el efecto neto en el F-300 del periodo; NC + acta archivadas enlazadas a la factura origen.
### Test 2 — (excepción, variante C) Se detecta internamente que una factura validada de $9,8M salió con IVA del 19 % sobre un servicio excluido; el receptor aún no la registra
**Output:** consulta a EspecialistaIVA confirma la exclusión; NC total + factura nueva correcta (cadena documentada); comunicación formal al receptor vía AtencionCliente el mismo día, antes de su registro; AuxContable ajusta la causación; el caso queda registrado como insumo de pre-validación (regla nueva: ese código de servicio del cliente es excluido); razón NC/facturas del cliente revisada por si el patrón es estructural.

═══════════════════════════════════════════════════════════════════════

---
name: procesar-factura-recibida-RADIAN
description: Activa cuando llega una factura recibida al RADIAN del cliente. Valida CUDE, verifica emisor en RUT, valida IVA y retenciones esperadas, y gestiona los eventos RADIAN (acuse de recibo, recibo del bien, aceptación expresa o tácita, reclamo) dentro de los plazos legales. Sin esta skill el cliente acepta tácitamente facturas inválidas.
agente: RITORE-AuxiliarFacturacionElectronica-Senior
categoria: operativo
---

# Skill: procesar-factura-recibida-RADIAN

## Para qué existe
La aceptación tácita corre sola: si nadie revisa las facturas recibidas dentro del plazo legal (3 días hábiles desde el recibo `[VERIFICAR cómputo según Art. 773 CCo / Ley 2024]`), el cliente queda obligado por documentos que quizá son inválidos o improcedentes. Esta skill decide a tiempo: aceptar, reclamar o rechazar, con los eventos RADIAN correctos.

## Cuándo se activa
- Factura nueva detectada en el RADIAN del cliente (monitoreo continuo).
- Reporte del cliente de una factura recibida por canal distinto (correo del proveedor).
- Vencimiento próximo del plazo de aceptación tácita de una factura pendiente de decisión (alerta a las 48 h).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| XML de la factura recibida | RADIAN | — (es el objeto de la skill) |
| Confirmación de recepción real del bien/servicio | Cliente (área de compras) vía AtencionCliente | Solicitar de inmediato; si no responde en 48 h, alertar que el plazo de aceptación tácita corre y escalar a Orquestador |
| Orden de compra / contrato asociado | Cliente / CarteraCxP | Validación documental procede; la validación económica queda `pendiente` y se advierte al cliente antes del vencimiento del plazo |

## Procedimiento
1. Detectar la factura en RADIAN y registrar fecha/hora de recibo (inicia el reloj de aceptación tácita).
2. Validar el **CUDE** del documento y la estructura UBL 2.1.
3. Verificar emisor en RUT: activo, obligado a facturar electrónicamente, régimen declarado coherente (vía `consultar-RUT-DIAN-emisor`).
4. Validar IVA según la operación y verificar que las retenciones esperadas estén correctamente informadas — si el cliente (receptor) es agente retenedor y la factura no las contempla, es causal de reclamo.
5. Confirmar con el cliente la recepción real del bien/servicio y la conformidad económica.
6. Emitir los eventos RADIAN que correspondan: **acuse de recibo de la factura → recibo del bien/servicio → aceptación expresa**; o **reclamo/rechazo formal con justificación** dentro del plazo.
7. Con aceptación: notificar a AuxContable (causación) y a CarteraCxP (cuenta por pagar).
8. Registrar la decisión y su justificación; alimentar el historial del proveedor.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Eventos RADIAN emitidos | Secuencia correcta y dentro del plazo legal; cero aceptaciones tácitas no deliberadas |
| Decisión documentada (aceptar/reclamar) | Con validaciones técnica, fiscal y económica registradas |
| Notificación a AuxContable y CarteraCxP | El mismo día hábil de la aceptación |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| CUDE inválido en factura recibida | Documento adulterado o error del proveedor tecnológico del emisor | Reclamo formal inmediato con la inconsistencia técnica; NO aceptar | Si el emisor insiste sin corregir, rechazo definitivo documentado y alerta al cliente sobre el proveedor |
| Cliente no confirma recepción del bien y el plazo tácito está por vencer | Área de compras del cliente sin respuesta | A las 48 h: reclamo preventivo para interrumpir la aceptación tácita `[VERIFICAR efecto interruptivo según norma vigente]` | Si el reclamo preventivo no procede normativamente, escalar a Orquestador antes del vencimiento — decisión humana con el reloj corriendo |
| Factura sin retenciones siendo el receptor agente retenedor | Emisor no parametrizó la calidad del receptor | Reclamo con la causal exacta y solicitud de corrección | Si el emisor se niega, NO aceptar; escalar a EspecialistaRetenciones para concepto y a Contador Titular si el proveedor es crítico para el cliente |
| Factura duplicada (mismo emisor, valor y concepto en el periodo) | Retransmisión del emisor o intento de doble cobro | Cruzar CUDE: si es el mismo documento, ignorar; si es CUDE distinto con misma operación, reclamar el duplicado | Notificar a CarteraCxP para bloqueo preventivo del pago |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Factura recibida con inconsistencia económica | ≥ 1 UVT o ≥ 0,5 % del valor | Reclamo documentado antes de aceptar |
| Factura pendiente de decisión | A las 48 h del recibo sin confirmación del cliente | Orquestador (el plazo tácito vence a los 3 días hábiles) |
| Facturas improcedentes aceptadas tácitamente | ≥ 50 UVT | EspecialistaIVA (Master) + Contador Titular informado |
| Sospecha de proveedor ficticio o doble cobro sistemático | Cualquier monto | Contador Titular + evaluación SAGRLAFT vía skill compartida |

## Reglas críticas
🚫 NUNCA dejar vencer el plazo de aceptación tácita sin decisión deliberada y documentada.
🚫 NUNCA aceptar factura sin retenciones cuando el receptor es agente retenedor.
✅ SIEMPRE emitir los eventos RADIAN en la secuencia correcta: sin acuse y recibo del bien, la aceptación queda coja como título valor.

## Métricas
- Facturas recibidas con decisión dentro del plazo legal: 100 % (medición mensual).
- Aceptaciones tácitas no deliberadas: 0.
- Reclamos resueltos por el emisor en ≤ 5 días hábiles: ≥ 70 % (gestión de seguimiento).

## Tests
### Test 1 — (normal) Factura de proveedor recurrente por $5,6M llega al RADIAN; compras confirma recepción del servicio el mismo día
**Output:** CUDE válido; emisor activo y obligado en RUT; IVA y retenciones correctas (cliente agente retenedor, retefuente informada); eventos acuse → recibo del servicio → aceptación expresa emitidos el día 1; AuxContable y CarteraCxP notificados; historial del proveedor actualizado.
### Test 2 — (excepción) Factura de $48M de un emisor nunca visto, sin orden de compra asociada, y el cliente no responde la confirmación en 48 h
**Output:** validación técnica OK pero validación económica imposible; alerta de vencimiento al cliente a las 48 h; reclamo preventivo evaluado con marca `[VERIFICAR efecto interruptivo]`; escalamiento al Orquestador antes del día 3 con el expediente (emisor verificado en RUT pero sin historial, monto ≥ 50 UVT); decisión humana documentada; el caso alimenta la evaluación SAGRLAFT si el patrón se repite.

═══════════════════════════════════════════════════════════════════════

---
name: emitir-documento-soporte-no-obligado
description: Activa cuando el cliente registra una adquisición a contraparte NO obligada a facturar electrónicamente (Art. 1.6.1.4.12 DUR 1625/2016). Verifica la no obligación en RUT, emite el documento soporte con CUDE y numeración autorizada, y rechaza la vía del documento soporte cuando el proveedor SÍ está obligado. Sin esta skill el cliente pierde costos y deducciones por falta de soporte válido.
agente: RITORE-AuxiliarFacturacionElectronica-Senior
categoria: operativo
---

# Skill: emitir-documento-soporte-no-obligado

## Para qué existe
Sin documento soporte válido, la compra a un no obligado no es deducible ni da derecho a impuestos descontables: esta skill convierte esas adquisiciones en soporte fiscal pleno y evita el atajo peligroso de "documentar por soporte" a proveedores que en realidad deben facturar.

## Cuándo se activa
- Registro de adquisición a persona natural o tercero presuntamente no obligado, reportado por el cliente o por AuxContable.
- Cierre del periodo: barrido de compras del mes sin factura electrónica asociada.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Datos de la adquisición: proveedor (NIT/cédula), concepto, valor, fecha | Cliente / AuxContable | Solicitar vía AtencionCliente (24 h hábiles, reiterar 1 vez); sin datos completos no se emite |
| Estado del proveedor en RUT (obligación de facturar) | `consultar-RUT-DIAN-emisor` | Timeout 4 h → NO emitir con duda sobre la obligación; el documento soporte a un obligado es inválido |
| Numeración de documento soporte vigente | `auditar-numeracion-autorizada` | Activar trámite urgente; sin numeración no hay emisión |

## Procedimiento
1. Consultar el RUT del proveedor y confirmar que NO está obligado a facturar electrónicamente (responsabilidades en RUT).
2. Si el proveedor SÍ está obligado: rechazar la vía del documento soporte y exigir factura electrónica al proveedor (notificar al cliente la razón normativa, Art. 1.6.1.4.12 DUR).
3. Emitir el documento soporte con todos los requisitos: identificación completa de las partes, fecha de la operación, descripción específica, valor, IVA si aplica, y retenciones según concepto de EspecialistaRetenciones.
4. Calcular y verificar el **CUDE** del documento; asignar consecutivo de la numeración autorizada de documento soporte.
5. Transmitir a la DIAN (validación previa) vía proveedor tecnológico.
6. Notificar a AuxContable para contabilización con la marca de soporte válido para costos/deducciones.
7. Archivar y registrar al proveedor en `memoria.cliente_contexto` si es recurrente.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Documento soporte validado por DIAN | CUDE verificado + consecutivo del rango autorizado + requisitos completos |
| Verificación de no obligación documentada | Pantallazo/respuesta RUT con fecha de consulta archivada junto al documento |
| Notificación a AuxContable | Con marca de procedencia de costo/deducción |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| El proveedor resulta obligado a facturar | RUT desactualizado en la memoria o cambio reciente de responsabilidades | Rechazar la emisión; informar al cliente que debe exigir factura electrónica | Si el proveedor se niega a facturar, el gasto queda sin soporte deducible: advertir formalmente al cliente y escalar a Contador Titular si el monto es ≥ 50 UVT |
| Adquisiciones recurrentes al mismo no obligado superan topes que sugieren obligación | Proveedor que ya debería estar facturando | Marcar el caso y recomendar al cliente verificar la situación del proveedor `[VERIFICAR topes de obligación vigentes]` | Documentar la advertencia; el riesgo es del proveedor, pero el patrón se reporta al Contador Titular |
| Documento soporte rechazado por DIAN | Requisito faltante o numeración | Tratar vía `gestionar-rechazo-DIAN` (mismo protocolo de reintentos y hold) | — (gobernado por esa skill) |
| Operación de un periodo ya cerrado sin documento soporte emitido | Cliente reportó tarde | Emitir con fecha real de la operación y alertar a AuxContable + EspecialistaRenta del efecto en el periodo | Si el periodo fiscal ya se declaró, escalar a EspecialistaRenta para evaluar corrección |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Gasto sin soporte válido por negativa del proveedor | ≥ 1 UVT | Advertencia formal al cliente documentada |
| Gasto sin soporte válido | ≥ 50 UVT | Contador Titular (pérdida de deducción material) |
| Acumulado de compras del cliente a no obligados | ≥ 500 UVT en el periodo | Contador Titular (revisión del perfil de proveedores) |
| Duda sobre la obligación del proveedor | Cualquier caso | `consultar-RUT-DIAN-emisor` + EspecialistaIVA si persiste |

## Reglas críticas
🚫 NUNCA emitir documento soporte a un proveedor obligado a facturar electrónicamente: el documento es inválido y el costo se pierde igual.
🚫 NUNCA emitir sin verificación de RUT con fecha de consulta archivada.
✅ SIEMPRE incluir las retenciones según el concepto definido por EspecialistaRetenciones (yo no calculo tarifas).

## Métricas
- Documentos soporte emitidos con verificación RUT archivada: 100 %.
- Compras del mes a no obligados con documento soporte emitido antes del cierre: ≥ 98 %.
- Documentos soporte rechazados por DIAN: < 1 %.

## Tests
### Test 1 — (normal) Cliente paga $1,9M de honorarios a una persona natural no responsable de IVA ni obligada a facturar
**Output:** RUT consultado y archivado (no obligada); documento soporte con requisitos completos, retefuente por honorarios según concepto de EspecialistaRetenciones, CUDE verificado y consecutivo del rango autorizado; validación DIAN exitosa; AuxContable notificado con marca de deducibilidad.
### Test 2 — (excepción) El cliente pide documento soporte para una compra de $7,2M a una ferretería que, según el RUT, SÍ está obligada a facturar electrónicamente
**Output:** emisión RECHAZADA con la razón normativa (Art. 1.6.1.4.12 DUR); cliente notificado de que debe exigir factura electrónica al proveedor; al negarse el proveedor, advertencia formal documentada de pérdida de la deducción y escalamiento a Contador Titular (≥ 50 UVT… verificación: $7,2M ÷ $52.374 ≈ 137 UVT → sí escala); el caso queda en el historial del proveedor.

═══════════════════════════════════════════════════════════════════════

---
name: cruzar-radian-vs-libros
description: Activa al cierre de cada periodo de IVA, antes de la elaboración del F-300. Cruza la facturación RADIAN del periodo (emitida y recibida) contra los libros contables y reporta las diferencias con umbrales §3. Sin esta skill el F-300 se presenta sobre cifras que la DIAN puede contradecir con sus propios datos.
agente: RITORE-AuxiliarFacturacionElectronica-Senior
categoria: operativo
---

# Skill: cruzar-radian-vs-libros

## Para qué existe
La DIAN conoce la facturación electrónica del cliente mejor que el cliente: cruzar RADIAN contra libros ANTES de declarar es la única forma de que el F-300 no nazca contradicho. Esta skill encuentra las diferencias cuando todavía son corregibles.

## Cuándo se activa
- Cierre del periodo de IVA (bimestral/cuatrimestral según calendario del cliente), antes del F-300.
- Solicitud de EspecialistaIVA o del Contador Titular.
- Preparación de información exógena (cruce de soporte para ExogenaMaster).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Reporte RADIAN del periodo (emitidas + recibidas) | RADIAN / Token DIAN | Si el servicio no responde, reintentar con backoff 5 m/10 m/20 m; persistencia → último reporte cacheado con marca `[DATO EN CACHÉ — verificar]` y reintento programado |
| Movimientos contables de ingresos y compras del periodo | AuxContable | Timeout 4 h → preconciliar con el último auxiliar disponible marcado en caché; el cruce definitivo espera el dato real |
| Notas crédito/débito del periodo | Archivo propio (`corregir-factura-emitida-NC-ND`) | Reconstruir del archivo; el cruce sin notas da falsos descuadres |

## Procedimiento
1. Descargar el reporte RADIAN del periodo: documentos emitidos, recibidos y notas.
2. Conciliar contra libros en tres frentes: (a) factura en libros sin RADIAN, (b) documento RADIAN sin libros, (c) mismo documento con montos divergentes.
3. Netear el efecto de NC/ND en ambas fuentes antes de medir diferencias.
4. Tipificar cada diferencia: ingreso no facturado electrónicamente, factura no contabilizada, compra aceptada sin causar, nota sin registrar, diferencia de periodo (corte).
5. Aplicar umbrales: diferencias ≥ 1 UVT individual o ≥ 0,5 % del total del periodo se investigan y documentan antes del F-300.
6. Entregar el cruce documentado a EspecialistaIVA (insumo directo del F-300) y notificar a AuxContable los registros faltantes.
7. Si tras investigación queda diferencia sin explicar ≥ 50 UVT, escalar ANTES de que se presente el F-300.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Cruce RADIAN vs libros del periodo | Toda diferencia ≥ 1 UVT tipificada con causa, o explícitamente marcada como `no explicada` y escalada |
| Insumo para F-300 entregado a EspecialistaIVA | Antes de la fecha interna de elaboración del F-300 (≥ 3 días hábiles antes del vencimiento) |
| Lista de registros faltantes para AuxContable | Con documento, monto y tipificación |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Diferencia global entre RADIAN y libros sin tipificar | Notas no neteadas o diferencias de corte de periodo | Re-cruzar neteando NC/ND y revisar documentos de los 3 días alrededor del corte | Diferencia persistente ≥ 50 UVT → EspecialistaIVA con el trabajo documentado; el F-300 NO se elabora sobre el descuadre |
| Reporte RADIAN incompleto o servicio caído | Intermitencia DIAN | Backoff 5 m/10 m/20 m; luego reporte cacheado con marca y reintento programado cada 4 h | Si el vencimiento del F-300 se acerca (≤ 2 días hábiles) sin reporte fresco, escalar a EspecialistaIVA y Orquestador para decisión humana |
| Factura en libros que nunca pasó por validación DIAN | Cliente facturó por fuera del sistema (talonario, documento inválido) | Tipificar como hallazgo crítico: ingreso sin soporte de facturación electrónica | Escalar a Contador Titular SIEMPRE (riesgo sancionatorio del cliente, Art. 652-657 ET `[VERIFICAR régimen sancionatorio aplicable]`) |
| Compras aceptadas en RADIAN sin causar en libros | AuxContable no recibió la notificación de aceptación | Notificar el lote a AuxContable con plazo del cierre | Si el atraso persiste al cierre, el cruce queda `parcial` y Orquestador decide si el F-300 procede |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Diferencia individual o acumulada | ≥ 1 UVT individual o ≥ 0,5 % del total del periodo | Investigar y documentar antes del F-300 |
| Diferencia no explicada al cierre del cruce | ≥ 50 UVT | EspecialistaIVA (Master) — bloquea el F-300 |
| Diferencia no explicada | ≥ 500 UVT | Contador Titular, mismo día |
| Facturación por fuera del sistema electrónico | Cualquier monto | Contador Titular |

## Reglas críticas
🚫 NUNCA dar visto bueno al insumo del F-300 con diferencias ≥ 1 UVT sin tipificar.
🚫 NUNCA tratar una diferencia de corte como error sin verificar los documentos del borde del periodo.
✅ SIEMPRE netear NC/ND en ambas fuentes antes de medir diferencias.

## Métricas
- Cruces entregados ≥ 3 días hábiles antes del vencimiento del F-300: 100 % (medición por periodo de IVA).
- Diferencias tipificadas sobre diferencias detectadas: ≥ 95 %.
- F-300 presentados que luego la DIAN contradice con datos de facturación electrónica: 0.

## Tests
### Test 1 — (normal) Periodo bimestral con 412 documentos RADIAN; el cruce encuentra 3 facturas recibidas aceptadas sin causar y 1 NC sin registrar en libros
**Output:** diferencias tipificadas (compras sin causar + nota sin registrar); lote notificado a AuxContable y corregido antes del cierre; re-cruce con diferencia $0; insumo entregado a EspecialistaIVA 5 días hábiles antes del vencimiento.
### Test 2 — (excepción) En libros hay ingresos por $31M facturados con un "talonario de contingencia" que nunca se transmitió a la DIAN, y el cliente asegura que "así lo ha hecho siempre"
**Output:** hallazgo crítico tipificado: ingresos sin soporte de facturación electrónica válida (la contingencia exige transmisión posterior); escalamiento inmediato al Contador Titular con el detalle documental y marca `[VERIFICAR régimen sancionatorio aplicable]`; el F-300 queda bloqueado hasta decisión; AtencionCliente coordina la comunicación formal con el cliente; el caso se registra para seguimiento en periodos siguientes.

═══════════════════════════════════════════════════════════════════════

---
name: consultar-RUT-DIAN-emisor
description: Activa cuando cualquier skill del perfil — o un agente externo (Onboarding, Comercial) — necesita verificar estado, régimen y obligaciones de un NIT en el RUT DIAN: antes de aceptar proveedor/cliente nuevo, antes de transmitir, antes de emitir documento soporte. Persiste el resultado para terceros recurrentes.
agente: RITORE-AuxiliarFacturacionElectronica-Senior
categoria: operativo
---

# Skill: consultar-RUT-DIAN-emisor

## Para qué existe
Casi todas las decisiones del perfil dependen de un hecho externo: qué dice el RUT de un NIT (activo, régimen, obligado a facturar, agente retenedor, gran contribuyente). Esta skill es la fuente única de esa verdad, con caché disciplinado — sin ella, cada skill improvisaría su propia consulta y su propia versión del tercero.

## Cuándo se activa
- Solicitud interna de cualquier skill del perfil (validación de receptor, verificación de emisor, no obligación para documento soporte).
- Solicitud de Comercial/Onboarding en pre-aceptación de cliente nuevo.
- Vencimiento del caché de un tercero recurrente (revalidación periódica, ver procedimiento).

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| NIT o cédula a consultar | Skill solicitante / agente externo | — (es el objeto de la skill) |
| Acceso al servicio de consulta (Token DIAN) | Token DIAN (servicio) | Backoff 5 m/10 m/20 m; persistencia → caché con marca `[DATO EN CACHÉ — verificar]` y reverificación programada |
| Caché de terceros recurrentes | `memoria.cliente_contexto` | Consulta directa; el caché se reconstruye con el uso |

## Procedimiento
1. Verificar si el NIT está en caché y si la consulta es más reciente que el umbral de frescura: 30 días para terceros recurrentes; mismo día para decisiones de pre-aceptación de cliente o emisión de documento soporte.
2. Si requiere consulta fresca: consultar vía Token DIAN y extraer: estado (activo/suspendido/cancelado), régimen tributario, obligación de facturar electrónicamente, calidad de agente retenedor, calidad de gran contribuyente, responsabilidades relevantes.
3. Contrastar contra la versión anterior del caché: todo cambio de responsabilidades de un tercero recurrente se notifica a las skills que dependan de él.
4. Persistir en `memoria.cliente_contexto` con fecha de consulta (si tercero recurrente).
5. Responder a la skill o agente solicitante con la ficha y la fecha de la consulta.
6. Si era pre-aceptación de cliente: notificar a Comercial/Onboarding incluyendo señales de alerta (estado suspendido, cambios recientes de régimen).

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Ficha RUT del NIT | Con los 6 atributos del paso 2 y fecha de consulta |
| Caché actualizado | Terceros recurrentes con frescura ≤ 30 días |
| Alertas de cambio de responsabilidades | Notificadas a las skills dependientes el mismo día |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Servicio de consulta caído | Intermitencia Token DIAN | Backoff 5 m/10 m/20 m | Responder con caché marcado `[DATO EN CACHÉ — verificar]` SOLO si la decisión lo tolera (validación de receptor recurrente); para pre-aceptación o documento soporte, la decisión ESPERA el dato fresco y se escala a Orquestador a las 4 h |
| NIT no existe en RUT | Dígito errado o tercero sin RUT | Validar dígito de verificación; devolver el error a la skill solicitante con la causa | Si el cliente insiste en que el tercero existe, solicitar copia del RUT al tercero vía AtencionCliente |
| Tercero recurrente cambió de responsabilidades (p. ej. perdió calidad de autorretenedor) | Actualización del RUT | Notificar a TODAS las skills dependientes y a EspecialistaRetenciones (afecta retenciones en curso) | Marcar las operaciones del periodo con el tercero para revisión retroactiva |
| Estado "suspendido" o "cancelado" en tercero con operaciones activas | Problema fiscal del tercero | Alertar de inmediato a la skill solicitante y al Contador Titular si hay operaciones en curso ≥ 50 UVT | Bloquear nuevas emisiones/aceptaciones hacia ese NIT hasta decisión |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Decisión bloqueada por servicio caído | > 4 h | Orquestador |
| Tercero suspendido/cancelado con operaciones en curso | ≥ 50 UVT | Contador Titular |
| Cambio de responsabilidades con efecto retroactivo en el periodo | ≥ 500 UVT de operaciones afectadas | Contador Titular vía Orquestador |

## Reglas críticas
🚫 NUNCA responder una pre-aceptación de cliente o una verificación de no obligación con datos de caché: esas decisiones exigen consulta del día.
✅ SIEMPRE registrar la fecha de consulta junto al dato: una ficha RUT sin fecha no es evidencia.
✅ SIEMPRE notificar los cambios de responsabilidades a las skills dependientes (retenciones y facturación en curso).

## Métricas
- Consultas respondidas en ≤ 1 h hábil: ≥ 95 % (medición mensual).
- Fichas con fecha de consulta registrada: 100 %.
- Cambios de responsabilidades de recurrentes detectados y notificados el mismo día: 100 %.

## Tests
### Test 1 — (normal) `emitir-documento-soporte-no-obligado` solicita verificar si una persona natural está obligada a facturar
**Output:** consulta fresca (la decisión no admite caché); ficha con estado activo, sin obligación de facturar electrónicamente, sin calidad de agente retenedor; fecha de consulta registrada y archivada junto al documento soporte; tercero persistido como recurrente.
### Test 2 — (excepción) Revalidación mensual detecta que un proveedor recurrente del cliente pasó de activo a "cancelado" en RUT, con 2 facturas suyas pendientes de aceptación por $61M
**Output:** alerta inmediata a `procesar-factura-recibida-RADIAN` (las 2 facturas NO se aceptan hasta aclarar); Contador Titular notificado (≥ 50 UVT en operaciones en curso); CarteraCxP alertada para bloqueo preventivo de pagos; solicitud de aclaración al proveedor vía cliente; desenlace documentado en el historial del tercero.

═══════════════════════════════════════════════════════════════════════

---
name: auditar-numeracion-autorizada
description: Activa con cada consumo de consecutivo y en un cron semanal. Monitorea el agotamiento de los rangos de numeración autorizada DIAN (facturas, documento soporte, contingencia) y la vigencia de las resoluciones; al cruzar el umbral del 20 % restante dispara la alerta y el trámite de nueva resolución. Sin esta skill el cliente amanece sin poder facturar.
agente: RITORE-AuxiliarFacturacionElectronica-Senior
categoria: operativo
---

# Skill: auditar-numeracion-autorizada

## Para qué existe
La numeración autorizada se agota en silencio y la resolución vence con fecha fija: cualquiera de las dos cosas detiene la facturación del cliente en seco. Esta skill mantiene el semáforo de cada rango y tramita la ampliación ANTES de que el agotamiento sea una emergencia.

## Cuándo se activa
- Cada consumo de consecutivo reportado por las skills emisoras (`validar-factura-emitida-CUFE`, `corregir-factura-emitida-NC-ND`, `emitir-documento-soporte-no-obligado`).
- Cron semanal: verificación de % restante y vigencia de TODAS las resoluciones de TODOS los clientes.
- Modo urgente: invocada por otra skill ante rechazo por numeración o emisión bloqueada.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| Resoluciones de numeración vigentes por cliente (rango, prefijo, fechas) | Archivo del cliente / portal DIAN | Reconstruir desde el portal DIAN (consulta de numeración) y archivar; sin resolución documentada el semáforo no es confiable |
| Consumo de consecutivos del periodo | Skills emisoras del perfil | Recalcular contra el último documento emitido archivado |
| Proyección de emisión mensual del cliente | Histórico propio (6 meses) | Con < 6 meses, usar el promedio disponible con marca `[BASE HISTÓRICA PARCIAL]` |

## Procedimiento
1. Mantener por cliente y por tipo de documento (factura, documento soporte, contingencia): rango autorizado, consumido, % restante, fecha de vencimiento de la resolución.
2. Calcular el agotamiento proyectado: % restante ÷ ritmo de consumo mensual = meses de autonomía.
3. **Umbral de alerta: < 20 % restante del rango O < 60 días para el vencimiento de la resolución** → disparar alerta y abrir el trámite de nueva resolución de numeración ante la DIAN.
4. Preparar la solicitud (rango propuesto según proyección de 12 meses) y coordinar con el Contador Titular la firma/gestión en el portal DIAN.
5. Confirmar la nueva resolución, registrarla y parametrizarla con el proveedor tecnológico ANTES del agotamiento del rango actual.
6. Verificar en el primer documento del rango nuevo que prefijo y consecutivo correspondan a la resolución.
7. Reportar el semáforo consolidado al Orquestador en el cierre mensual.

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Semáforo de numeración por cliente y tipo de documento | Actualizado al menos semanalmente; % restante y días de vigencia visibles |
| Trámite de nueva resolución | Abierto al cruzar el umbral (< 20 % o < 60 días); nueva resolución vigente antes del agotamiento |
| Parametrización del nuevo rango | Verificada con el primer documento emitido del rango |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Rango cae bajo 20 % sin alerta previa | Pico de emisión no proyectado (estacionalidad) | Disparar el trámite urgente y recalibrar la proyección con el pico incluido | Si la autonomía restante es < 15 días, escalar a Contador Titular el mismo día para priorizar el trámite |
| Trámite de resolución atascado en la DIAN | Demoras del portal / inconsistencias del RUT del cliente | Hacer seguimiento cada 48 h y documentar; verificar prerrequisitos (RUT actualizado, inconsistencias pendientes) | Si el rango se agota con el trámite en curso: emisión queda bloqueada → activar protocolo de contingencia si la norma lo permite `[VERIFICAR procedencia de numeración de contingencia en este caso]` y escalar a Contador Titular + Orquestador |
| Resolución vencida con rango sin agotar | Vigencia (típicamente 6/12 meses) venció antes que el consecutivo | NO emitir con resolución vencida (causal de rechazo); tramitar nueva de inmediato | Igual que el bloqueo por agotamiento: escalamiento mismo día |
| Consecutivo emitido por fuera del rango | Parametrización errada del proveedor tecnológico | Detener emisión, corregir parametrización, conciliar consecutivos emitidos vs autorizados | Documentos ya validados fuera de rango → Contador Titular para evaluar el saneamiento `[VERIFICAR tratamiento]` |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| Rango restante | < 20 % o < 60 días de vigencia | Alerta + apertura del trámite de nueva resolución |
| Autonomía proyectada | < 15 días | Contador Titular, mismo día |
| Emisión de un cliente bloqueada por numeración | Cualquier caso | Contador Titular + Orquestador, prioridad crítica (SLA 1 h) |
| Consecutivos fuera de rango detectados | Cualquier caso | Contador Titular |

## Reglas críticas
🚫 NUNCA permitir emisión con resolución vencida o consecutivo fuera del rango autorizado.
🚫 NUNCA esperar al agotamiento para tramitar: el umbral del 20 % existe para que el trámite termine antes de la emergencia.
✅ SIEMPRE verificar la parametrización del rango nuevo con el primer documento real emitido.

## Métricas
- Clientes que llegan a bloqueo de emisión por numeración: 0 (medición mensual).
- Trámites de nueva resolución abiertos dentro de las 24 h de cruzar el umbral: 100 %.
- Semáforo semanal actualizado para el 100 % de los clientes emisores.

## Tests
### Test 1 — (normal) Cron semanal: un cliente consume 1.200 facturas/mes y su rango muestra 2.900 consecutivos restantes (24 %) con resolución vigente 8 meses más
**Output:** semáforo en amarillo preventivo (autonomía ≈ 2,4 meses, aún sobre el umbral del 20 %); proyección recalculada; sin trámite todavía, pero con fecha estimada de cruce del umbral registrada para el cron; reporte mensual al Orquestador con el semáforo consolidado.
### Test 2 — (excepción) Un cliente estacional triplica su emisión en temporada y el rango pasa de 31 % a 12 % en dos semanas; además la resolución vence en 45 días
**Output:** doble umbral cruzado (< 20 % y < 60 días) → alerta inmediata y trámite de nueva resolución abierto con rango propuesto sobre la proyección corregida por estacionalidad; coordinación de firma con el Contador Titular; seguimiento cada 48 h; nueva resolución parametrizada y verificada con el primer documento del rango; autonomía nunca bajó de 15 días — si lo hubiera hecho, escalamiento mismo día al Contador Titular.

═══════════════════════════════════════════════════════════════════════

---
name: transmitir-nomina-electronica
description: Activa mensualmente, coordinada con 07-AuxiliarNomina, para transmitir el documento soporte de pago de nómina electrónica al sistema DIAN (Res. 000013/2021). Nómina genera y entrega el XML; esta skill valida la estructura, transmite, confirma el CUNE y gestiona rechazos y caídas del servicio con los mismos fallbacks del perfil.
agente: RITORE-AuxiliarFacturacionElectronica-Senior
categoria: operativo
---

# Skill: transmitir-nomina-electronica

## Para qué existe
El costo laboral solo es deducible si la nómina electrónica se transmitió a tiempo y fue validada: esta skill es el último eslabón entre la liquidación de Nómina y la DIAN. La frontera es nítida: **Nómina liquida y genera el XML; esta skill valida estructura, transmite y confirma** — sin esta separación, los rechazos rebotarían sin dueño.

## Cuándo se activa
- Entrega mensual del XML de nómina electrónica por 07-AuxiliarNomina (skill `transmitir-nomina-electronica-DIAN` de ese perfil).
- Ventana de transmisión DIAN próxima a vencer (los 10 primeros días hábiles del mes siguiente `[VERIFICAR plazo vigente Res. 000013/2021 y modificatorias]`) sin XML recibido → alerta proactiva a Nómina.
- Notas de ajuste de nómina electrónica (documento de eliminación/reemplazo) solicitadas por Nómina.

## Inputs

| Insumo | De quién | Si falta |
|---|---|---|
| XML de nómina electrónica del periodo (individual + ajustes) | 07-AuxiliarNomina | Si al día hábil 5 del mes no llega, alertar a Nómina; timeout 4 h tras la alerta → Orquestador (la ventana DIAN es improrrogable) |
| Numeración de nómina electrónica vigente | `auditar-numeracion-autorizada` | Trámite urgente; sin numeración no hay transmisión |
| Confirmación de liquidación cerrada del periodo | 07-AuxiliarNomina | NO transmitir nómina de liquidación abierta: los ajustes posteriores multiplican documentos de reemplazo |

## Procedimiento
1. Recibir el XML del periodo y validar la estructura contra el anexo técnico de nómina electrónica vigente (campos obligatorios, devengados, deducciones, redondeos).
2. Verificar el **CUNE** de cada documento (recálculo propio, mismo estándar que CUFE/CUDE).
3. Verificar consecutivos contra el rango autorizado de nómina electrónica.
4. Transmitir al sistema DIAN dentro de la ventana del periodo.
5. Confirmar la validación documento a documento; conciliar: empleados liquidados = documentos validados.
6. Con rechazos: clasificar — si la causa es estructural/técnica, corregir aquí; si es de datos de liquidación (IBC, devengados), devolver a Nómina con el detalle exacto, y gestionar el reintento vía `gestionar-rechazo-DIAN` (mismo control de 3 intentos y hold).
7. Archivar comprobantes de validación y notificar a Nómina y a AuxContable (soporte de deducibilidad del costo laboral).

## Outputs

| Entregable | Criterio de aceptación |
|---|---|
| Nómina electrónica del periodo validada | 100 % de empleados liquidados con documento validado y CUNE verificado, dentro de la ventana DIAN |
| Comprobantes archivados | Convención canónica; soporte de deducibilidad disponible para EspecialistaRenta |
| Rechazos devueltos a Nómina | Con código DIAN, campo exacto y empleado afectado |

## Manejo de errores

| Error | Causa probable | Acción | Fallback si la acción falla |
|---|---|---|---|
| Timeout del servicio DIAN en la transmisión | Intermitencia del sistema | Backoff **5 m → 10 m → 20 m**; la cola conserva el orden | Servicio caído persistente: reintento programado cada 4 h; si la ventana del periodo está a ≤ 2 días hábiles de cerrar, escalar a Orquestador y Contador Titular (riesgo de extemporaneidad con efecto en deducibilidad) |
| Rechazo por datos de liquidación | Error de IBC/devengados en el XML de Nómina | Devolver a Nómina con el detalle exacto; NO corregir cifras de liquidación aquí | 3 rechazos del mismo documento → hold 24 h + escalamiento a Nómina y AuxContable según protocolo de `gestionar-rechazo-DIAN` |
| Empleados liquidados ≠ documentos validados | Documento omitido o duplicado en el lote | Conciliar empleado a empleado y completar/eliminar con documento de ajuste | Si la diferencia persiste al cierre de la ventana, transmitir lo conciliado y escalar el remanente a Orquestador con detalle |
| XML llega el último día de la ventana | Liquidación tardía de Nómina | Transmitir con prioridad y documentar la causa | Si no alcanza la ventana, registrar la extemporaneidad, notificar a EspecialistaRenta (riesgo de deducibilidad) y al Contador Titular |

## Escalamiento

| Situación | Umbral | Destino |
|---|---|---|
| XML no recibido | Día hábil 5 del mes sin entrega | Alerta a Nómina; +4 h sin respuesta → Orquestador |
| Riesgo de transmisión extemporánea | ≤ 2 días hábiles de ventana con lote pendiente | Orquestador + Contador Titular |
| Costo laboral del periodo sin soporte transmitido | ≥ 50 UVT | Contador Titular (efecto directo en deducibilidad) |
| Diferencias de conciliación empleados vs documentos | ≥ 1 UVT en valores o cualquier empleado faltante | Investigar y resolver antes del cierre de la ventana |

## Reglas críticas
🚫 NUNCA corregir cifras de liquidación en el XML: eso es de 07-AuxiliarNomina; aquí solo se corrige estructura/técnica.
🚫 NUNCA dejar cerrar la ventana DIAN con documentos sin transmitir y sin escalamiento documentado.
✅ SIEMPRE conciliar empleados liquidados vs documentos validados antes de dar el periodo por cerrado.

## Métricas
- Periodos transmitidos completos dentro de la ventana DIAN: 100 % (medición mensual).
- Documentos rechazados por causa estructural propia: < 1 %.
- Conciliación empleados vs documentos validados en diferencia 0: 100 %.

## Tests
### Test 1 — (normal) Nómina entrega el XML de 28 empleados el día hábil 3; estructura y CUNE correctos
**Output:** validación estructural y de CUNE exitosa; consecutivos dentro del rango; transmisión y validación DIAN de los 28 documentos; conciliación 28 = 28; comprobantes archivados y notificación a Nómina y AuxContable como soporte de deducibilidad.
### Test 2 — (excepción) De 28 documentos, la DIAN rechaza 2 por inconsistencia de IBC, y al retransmitir el servicio entra en timeout sostenido faltando 2 días para el cierre de la ventana
**Output:** los 2 rechazos se devuelven a Nómina con código DIAN, campo y empleado (no se tocan cifras aquí); Nómina corrige y reentrega; el timeout activa backoff 5 m/10 m/20 m sin éxito → reintentos cada 4 h y, por estar a ≤ 2 días del cierre, escalamiento simultáneo a Orquestador y Contador Titular; al restablecerse el servicio, transmisión prioritaria de los 2 documentos dentro de la ventana; conciliación final 28 = 28 documentada.

═══════════════════════════════════════════════════════════════════════

## Relacionado
- *MOC - Agentes RITORE*
- *Proyecto - Ecosistema RITORE*
- [[00 - Estandar de Agentes RITORE]]
- [[Skills Compartidas RITORE]]
- [[07-AuxiliarNomina-Senior]]
- *11-EspecialistaIVA-Master*
- *12-EspecialistaRetenciones-Senior*
- *22-AtencionCliente-Senior*
- *25-Onboarding-Senior*
- *26-NotionArquitecto-DevOps-Senior*

## Historial de versiones
| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-05-19 | Versión inicial consolidada (10 skills) | RITORE |
| 2.0 | 2026-06-11 | Refactorización según Estandar de Agentes v1.0: 10 → 9 skills (`generar-nota-credito-debito` + `notificar-factura-no-conforme-cliente` consolidadas en `corregir-factura-emitida-NC-ND` con variantes); eliminación de la auto-corrección clonada en 10 skills y de las reglas críticas idénticas (lo común se hereda de Skills Compartidas); secciones §2 completas en todas las skills; fallbacks nuevos: backoff 5m/10m/20m ante timeout DIAN, protocolo de contingencia por servicio caído, hold 24 h + corrección con cliente + escalamiento a AuxContable ante rechazo persistente (3 intentos), alerta y trámite de nueva resolución con numeración < 20 %; umbral del cruce RADIAN alineado a §3 (≥ 1 UVT / 0,5 %); tests propios por skill | RITORE |
