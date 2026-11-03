---
tipo: conocimiento
tags: [ritore, conocimiento, protocolo, retencion]
formulario: F-350
periodicidad: mensual
estado: vigente
fecha: 2026-06-08
---

# Protocolo Retención en la Fuente — F-350

Protocolo específico para liquidar, declarar y pagar la **retención en la fuente mensual (Formulario 350)** de los clientes agentes de retención del portafolio. Es la obligación de mayor frecuencia y la de mayor riesgo silencioso de la firma: una declaración presentada **sin pago total es ineficaz de pleno derecho** (Art. 580-1 ET). Sigue el esqueleto de [[Protocolo Elaboracion de Impuestos]]; aquí solo lo específico de retención. Tarifas, bases y cronología judicial del D. 0572: ver *Proyecto - Retencion en la Fuente* (no se reinvestiga, se reutiliza). Objetivo de calidad: margen de error < 2 % ([[Margen de Error 2 por ciento]]).

## Marco normativo y versión vigente

| Norma | Contenido |
|-------|-----------|
| **Arts. 365–419 ET** | Régimen general de retención: facultades, agentes, conceptos, tarifas y bases mínimas. |
| **Art. 383 ET** | Tabla progresiva de rentas de trabajo (aplica también a honorarios/servicios de PN que no vinculen 2+ trabajadores). |
| **Arts. 392, 395, 401 ET** | Honorarios/comisiones/servicios, rendimientos financieros, otros ingresos (compras). |
| **Arts. 437-1 y 437-2 ET** | Retención de IVA (ReteIVA, 15 % del IVA; servicios de no residentes/digitales). |
| **Art. 580-1 ET** | **Ineficacia** de las declaraciones de retención presentadas sin pago total. Regla más peligrosa del formulario. |
| **D. 2201/2016** (arts. 1.2.6.6–1.2.6.8 DUR), mod. D. 261/2023, D. 242/2024, **D. 0572/2025** | Autorretención especial de renta. |
| **D. 0572 del 28/05/2025** | Subió autorretención especial y bajó bases mínimas. **Saga judicial — ver alerta abajo.** |
| **Arts. 514–518 ET** | Impuesto de timbre nacional (cuando aplique). |
| **D. 2229/2023** | Calendario tributario permanente en días hábiles (rige 2026). |

**Formulario vigente:** **F-350 prescrito por la Resolución 000031 del 29/02/2024**, en uso desde el 01/08/2024 — el mismo para todas las declaraciones de 2026. La versión vigente **separa las retenciones practicadas a personas jurídicas (PJ) y a personas naturales (PN)** en dos bloques de casillas distintos, agregó casillas de hidrocarburos/minería y conceptos PES y de pagos al exterior con/sin convenio (CDI). El **D. 0572/2025 NO cambió el formulario** — solo tarifas y bases. Confirmar siempre con *21-MonitoreoNormativo-Senior* antes de parametrizar.

> ⚠️ **ALERTA D. 0572 — saga judicial (clave operativa 2026).** En **junio de 2026 se aplican las tarifas y bases del DUR ANTERIORES al D. 0572** (suspensión provisional del 07/05/2026, Comunicado DIAN 070 del 08/05/2026). El **02/06/2026 el Consejo de Estado revocó la suspensión**: los arts. 2–8 del D. 0572 **recobran vigencia desde el primer día calendario del mes siguiente a la ejecutoria del auto — previsiblemente el 01/07/2026** `[VERIFICAR ejecutoria antes de reparametrizar]`. El **art. 1 (CDAT equiparado a CDT) nunca se suspendió**. La tarifa aplicable es siempre la vigente en la **fecha del pago o abono en cuenta**: las retenciones de junio van con esquema antiguo; desde julio se reparametriza al D. 0572. Conservar trazabilidad por cliente (si la sentencia de fondo anula el decreto, los efectos serían retroactivos). Cronología completa en *Proyecto - Retencion en la Fuente*.

## Insumos (no se liquida sin esto)

1. **Token DIAN del periodo** (a veces dentro de un `.zip`) — **fuente de verdad** de las facturas recibidas/emitidas sujetas a retención. Interpretación: [[Aux 20 - Interpretacion del Token DIAN]].
2. **Libro auxiliar por tercero de las cuentas de retención por pagar:**
   - **2365** — Retención en la fuente a título de renta practicada.
   - **2367** — ReteIVA practicada.
   - **2368** — ReteICA practicada (municipal — alimenta la declaración territorial, no el F-350).
3. **Balance de prueba por tercero** del mes — cuadrado (débitos = créditos) antes de procesar (regla C.1).
4. **Nómina del mes** (rentas de trabajo, Art. 383) y soporte del cálculo de retención de salarios.
5. **RUT del cliente:** verificar **responsabilidad 15** (autorretenedor especial de renta) y las responsabilidades de ReteIVA/ReteICA antes de parametrizar.
6. **Certificados de retención emitidos** del periodo, para cuadre y para la exógena anual.
7. **Papel de trabajo** [[Aux 14 - Calculo de Retenciones]] con la matriz de tarifas y bases del mes.

## Paso a paso

1. **Determinar retenciones practicadas por concepto.** Por cada tercero y concepto, la retención practicada en el mes = **crédito − débito de la cuenta 2365 por tercero**, **excluyendo los cierres a nombre de la DIAN** (el traslado mensual del saldo de 2365 a la DIAN no es una retención nueva). Misma lógica para 2367 (ReteIVA). Excluir filas "SALDO INICIAL" (regla C.2/D.5). La autorretención especial **no** sale de 2365 por tercero: se calcula aparte (paso 4).
2. **Clasificar PJ vs PN.** El F-350 v2024 exige discriminar: cada concepto se reporta por separado según el beneficiario sea persona jurídica (bloque casillas 29-58) o persona natural (bloque 77-112). Mantener esa separación desde el auxiliar.
3. **Asignar la tarifa correcta por la fecha del pago o abono en cuenta** (no por la fecha de factura) — crítico durante la transición D. 0572 (junio = esquema antiguo; julio en adelante = D. 0572 si quedó ejecutoriado). Tabla de tarifas/bases en *Proyecto - Retencion en la Fuente*.
4. **Autorretención especial del periodo** (solo si el cliente tiene responsabilidad 15 en el RUT). Base = ingresos del mes por la actividad; tarifa por CIIU. **Hasta 30/06/2026 (previsible):** tarifas D. 261/2023 y D. 242/2024 — 0,55 % / 1,1 % / 1,6 % según sector. **Desde ~01/07/2026 (reactivación D. 0572):** tarifas por CIIU hasta 4,5 %. Se declara y paga en el mismo F-350.
5. **ReteIVA** (Art. 437-1, 15 % del IVA): cuadrar contra el movimiento de la cuenta **2367** por tercero. Separar lo practicado a responsables de IVA (casilla 131) de lo practicado a servicios de no residentes/digitales (casilla 132).
6. **Retención de timbre** (casilla 135) solo si hubo actuaciones o documentos gravados con timbre en el mes (Arts. 514-518 ET) — caso excepcional; verificar antes de diligenciar.
7. **No declarar en ceros sin obligación:** no es obligatorio presentar F-350 de un mes sin operaciones sujetas a retención (Art. 606 par. 6 ET). Documentar la decisión.

## Mapa de renglones/conceptos del F-350 (Res. 000031/2024)

Casillas verificadas en el instructivo oficial DIAN (Formulario_350_2026.pdf). El formulario discrimina **bases** y **valores retenidos**, y separa **PJ** de **PN**.

**Retenciones a título de renta — Personas Jurídicas (valor retenido):**

| Casilla | Concepto |
|---------|----------|
| 42 | Honorarios |
| 43 | Comisiones |
| 44 | Servicios |
| 45 | Rendimientos financieros e intereses |
| 46 | Arrendamientos (muebles e inmuebles) |
| 48 | Dividendos y participaciones |
| 49 | Compras |
| 54 | Otros pagos sujetos a retención |
| 57 / 58 | Pagos al exterior sin convenio / con convenio (PJ) |
| 70–76 | Autorretenciones (honorarios, comisiones, servicios, rendimientos, otros) — bloque PJ |

**Retenciones a título de renta — Personas Naturales (valor retenido):**

| Casilla | Concepto |
|---------|----------|
| 93 | Rentas de trabajo (Art. 383) |
| 94 | Rentas de pensiones |
| 95 | Honorarios |
| 96 | Comisiones |
| 97 | Servicios |
| 98 | Rendimientos financieros e intereses |
| 99 | Arrendamientos (muebles e inmuebles) |
| 101 | Dividendos y participaciones |
| 102 | Compras |
| 108 | Otros pagos sujetos a retención |
| 111 / 112 | Pagos al exterior sin convenio / con convenio (PN) |
| 122–128 | Autorretenciones — bloque PN |

> Las casillas 29-41 (PJ) y 77-92 (PN) son las **bases** (pagos o abonos) de cada concepto; las anteriores son el **valor retenido**. Las rentas de trabajo (casilla 77 base / 93 retenido) y de pensiones (78/94) van siempre en el bloque PN.

**Totales y otros impuestos:**

| Casilla | Concepto |
|---------|----------|
| 129 | (−) Reintegros / retenciones practicadas en exceso o indebidas a título de renta |
| **130** | **Total retenciones renta y complementario** (suma de todos los conceptos renta − casilla 129) |
| 131 | ReteIVA a responsables del IVA (Art. 437-2) |
| 132 | ReteIVA practicada por servicios a no residentes / digitales |
| 133 | (−) ReteIVA en exceso/indebida |
| **134** | **Total retenciones IVA** (131 + 132 − 133) |
| 135 | Retenciones impuesto de timbre nacional |
| **136** | **Total retenciones** (130 + 134 + 135) |
| 137 | Sanciones (mín. 10 UVT en extemporaneidad/corrección) |
| **138** | **Total retenciones más sanciones** (136 + 137) — valor a pagar con el F-490 |

> Pagos al exterior (casillas 50/51 base y 75/76 PJ; equivalentes PN): se diligencian por anexo, seleccionando CON/SIN CONVENIO (casilla 90), concepto (91), país (92), base (93) y tarifa (94) del anexo de exterior.

## Regla crítica — Art. 580-1 ET (ineficacia)

La declaración de retención presentada **sin pago total** NO produce efecto legal alguno, **de pleno derecho** y sin acto administrativo. Es la regla más peligrosa del formulario: una declaración "presentada" pero sin pago equivale a NO haber declarado, con la sanción de extemporaneidad corriendo. **Excepciones verificadas:**

1. **Pago dentro de los 2 meses** siguientes al vencimiento del plazo para declarar (más intereses de mora) → la declaración produce efectos.
2. **Lo dejado de pagar no supera 10 UVT** ($523.740 en 2026, UVT 2026) y se paga dentro del año siguiente al vencimiento.
3. El agente tiene **saldo a favor ≥ 2 veces** la retención a cargo, susceptible de compensación (solicitar la compensación dentro de los 6 meses siguientes).

**Regla de la casa:** se presenta **con pago total y con mínimo 2 días hábiles de margen** antes del vencimiento. Nunca el último día. Nunca sin pago salvo que aplique y se documente una de las tres excepciones.

## Cuadres y cruces

**Cuadre del periodo (antes de presentar):**

- **F-350 ↔ auxiliar 2365 / 2367 ↔ token DIAN.** El total de cada concepto declarado debe cuadrar con el movimiento contable del mes (crédito − débito por tercero). Umbral material: diferencia individual ≥ 1 UVT o acumulada ≥ 0,5 % del total.
- ReteIVA declarado ↔ movimiento de la cuenta **2367**.
- Autorretención especial declarada ↔ base de ingresos del mes × tarifa CIIU del esquema vigente.

**Cruces anuales (la retención alimenta la exógena y la renta):**

| Cruce | Contra |
|-------|--------|
| Suma de los 12 F-350 del año (retención practicada por tercero) | **F-1001** de exógena, columna R (retención practicada) — ver *Formato 1001 - Pagos y Retenciones* |
| Retenciones que le practicaron al cliente | **F-1003** de exógena ↔ *Formato 1003 - Retenciones que le practicaron* |
| Bases de pagos del F-350 | F-1001 (pagos a terceros) ↔ costos y deducciones del **F-110** |
| Retención declarada por tercero | **Certificados de retención emitidos** (Art. 381 ET) — deben coincidir |

Método de conciliación en *Conciliacion Exogena vs Declaraciones*. Ningún cierre con cruce material abierto; si la diferencia revela un error contable, se corrige la contabilidad, no el formato (regla de oro C.8/D.10) y se escala al Contador Titular.

## Diligenciamiento, firma y pago

1. **Diligenciar en MUISCA** (módulo WebDilIngresoFormReteFuente350 — [[Formularios DIAN - Catalogo]]) o cargar desde el SIE.
2. **Firma del Contador Titular** (y revisor fiscal cuando aplique por patrimonio/ingresos) — nunca presentar sin firma.
3. **Pago total con la presentación** vía **Formulario 490**, verificando concepto y periodo exactos (un F-490 con concepto errado no extingue la obligación). El pago total es **existencial** (Art. 580-1).
4. **Archivar** acuse de presentación + F-350 firmado + F-490 + papeles de trabajo en la carpeta canónica del cliente.
5. **Certificados anuales** de retención a terceros (Art. 381 ET) dentro del plazo reglamentario del año siguiente.

## Calendario 2026

Regla general (D. 2229/2023): el F-350 del mes anterior vence entre el **7.º y el 16.º día hábil del mes siguiente**, según el **último dígito del NIT**. Ventanas verificadas (los días cívicos/festivos desplazan vencimientos — confirmar siempre la fecha exacta del cliente en `Calendario_Tributario_2026.pdf`):

| Periodo (mes retenido) | Ventana de vencimientos |
|------------------------|--------------------------|
| Diciembre 2025 | 13 – 26 enero 2026 |
| Enero | 10 – 23 febrero 2026 |
| Febrero | marzo 2026 (7.º–16.º día hábil) `[VERIFICAR día exacto]` |
| Marzo | 13 – 24 abril 2026 (desplazada por el día cívico del 17/04/2026) |
| Abril | 12 – 26 mayo 2026 |
| **Mayo** | **10 – 24 junio 2026** (próximo hito del portafolio) |
| Junio | 9 – 23 julio 2026 |
| Julio | agosto 2026 (7.º–16.º día hábil) `[VERIFICAR]` |
| Agosto | 9 – 22 septiembre 2026 |
| Septiembre | octubre 2026 (7.º–16.º día hábil) `[VERIFICAR]` |
| Octubre | 11 – 25 noviembre 2026 |
| Noviembre | diciembre 2026 (7.º–16.º día hábil) `[VERIFICAR]` |
| Diciembre | 13 – 26 enero 2027 |

> **Hito de transición:** la retención de **junio (vence 9-23 julio 2026)** es la primera que probablemente se liquida con el esquema reactivado del D. 0572. Verificar la ejecutoria antes de reparametrizar y dejarlo en el *Tablero de Alertas y Pendientes*.

## Errores típicos

- **Presentar sin pago total** creyendo que "ya quedó declarado" → ineficacia Art. 580-1 (el error más caro). Verificar el F-490 pagado ANTES de dar por cerrado el periodo.
- **Tomar el saldo de 2365 en vez del movimiento del mes** (crédito − débito por tercero), o **no excluir los cierres a nombre de la DIAN** → infla o desinfla el total.
- **No separar PJ de PN** en el formulario v2024 → rechazo o cruce errado.
- **Aplicar la tarifa por fecha de factura** en vez de fecha de pago o abono en cuenta — crítico en la transición D. 0572.
- **Olvidar la autorretención especial** del cliente con responsabilidad 15, o aplicarle tarifa del esquema equivocado (antiguo vs D. 0572).
- **Incluir ReteICA (2368) en el F-350** — ReteICA es municipal, no va en el F-350.
- **No incluir filas con "SALDO INICIAL"** o, peor, incluirlas en el movimiento del mes.
- **Liquidar sobre un auxiliar descuadrado** (débitos ≠ créditos) o sobre un archivo de otro cliente (verificar NIT/razón social dentro del archivo).

## Clientes aplicables (agentes de retención del portafolio)

- **Cliente - EXPORTADORA DE SERVICIOS B**
- **Cliente - COMERCIO DE BICICLETAS A**
- **Cliente - SERVICIOS SANITARIOS E**
- **Cliente - EMPRESA CON SOCIO EXTRANJERO C**
- **Cliente - EMPRESA DE SOFTWARE O**
- **Cliente - EMPRESA Z**
- **Cliente - TALLER AUTOMOTRIZ U**

> En cada cliente revisar en el RUT la **responsabilidad 15** (autorretenedor especial) y las responsabilidades de ReteIVA/ReteICA antes de la primera liquidación del año. TALLER DE DISEÑO J (**Cliente - PERSONA NATURAL J (TALLER DE DISEÑO J)**) figura en el proyecto pero como PN; verificar su calidad de agente de retención caso a caso.

## Fuentes (consultadas 2026-06-08)

- DIAN — Formulario 350 e instructivo 2026 (Res. 000031/2024, casillas verificadas): https://www.dian.gov.co/atencionciudadano/formulariosinstructivos/Formularios/2026/Formulario_350_2026.pdf
- DIAN — Cambios del formulario 350 (separación PJ/PN, PES, exterior): https://www.dian.gov.co/Prensa/Paginas/NG-Conozca-los-cambios-en-el-formulario-350-para-la-declaracion-de-retencion-en-la-fuente.aspx
- DIAN — Comunicado de Prensa 070 del 08/05/2026 (normas aplicables durante la suspensión del D. 0572): https://www.dian.gov.co/Prensa/Paginas/NG-Comunicado-de-Prensa-070-2026.aspx
- DIAN — Calendario Tributario 2026: https://www.dian.gov.co/Calendarios/Calendario_Tributario_2026.pdf
- Siempre al Día — Revocatoria de la suspensión del D. 0572 (auto del 02/06/2026): https://siemprealdia.co/colombia/impuestos/suspension-del-decreto-572-de-2025-tarifas-de-retencion-y-autorretencion-en-la-fuente/
- Actualícese — Guía F-350 paso a paso 2026: https://actualicese.com/guia-actualicese-retencion-en-la-fuente-2026-aplicacion-practica-y-formulario-350-paso-a-paso/
- Estatuto.co — Art. 580-1 ET: https://estatuto.co/580-1

## Relacionado

- *MOC - Conocimiento Tecnico* · [[Protocolo Elaboracion de Impuestos]] · [[Formularios DIAN - Catalogo]]
- [[Protocolo IVA Formulario 300]] · *Protocolo Renta Persona Juridica F-110*
- *Proyecto - Retencion en la Fuente* · *Proyecto - Exogena 2026* · *Proyecto - ICA y Retenciones Municipales*
- [[Aux 14 - Calculo de Retenciones]] · [[Aux 20 - Interpretacion del Token DIAN]]
- *12-EspecialistaRetenciones-Senior* · *21-MonitoreoNormativo-Senior*
- *Conciliacion Exogena vs Declaraciones* · *Formato 1001 - Pagos y Retenciones* · *Formato 1003 - Retenciones que le practicaron*
- [[ET - Retencion en la Fuente Articulos Clave]] · *ET - Procedimiento y Sanciones Articulos Clave* · [[UVT y Topes]]
- [[Margen de Error 2 por ciento]] · *Tablero de Alertas y Pendientes* · [[Manejo de Archivos Excel Corruptos]]
