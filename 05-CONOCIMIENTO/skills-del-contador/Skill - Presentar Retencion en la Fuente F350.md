---
tipo: skill
tags: [ritore, skill, retencion]
estado: vigente
version: 1.0
fecha: 2026-06-11
---

# Skill - Presentar Retencion en la Fuente F350

**Agente:** *12-EspecialistaRetenciones-Senior* · Conocimiento de respaldo: [[Protocolo Retencion en la Fuente F-350]] y *Proyecto - Retencion en la Fuente* (tarifas, cronología D. 0572 y calendario: NO se reinvestigan, se reutilizan). Estructura conforme a *00 - Estandar de Skills RITORE* §1; comportamientos comunes heredados de [[Skills Compartidas RITORE]] (§2 del estándar — no se repiten aquí).

## Objetivo

Liquidar, cuadrar, presentar **con pago total** y archivar la declaración mensual de retención en la fuente (**Formulario 350**) de cada cliente agente de retención, lista para firma del Contador Titular, con margen de error < 2 % ([[Margen de Error 2 por ciento]]) y sin exposición a la ineficacia del Art. 580-1 ET.

## Trigger

- Cierre de cada mes calendario, con antelación suficiente a la ventana de vencimientos del NIT (regla D. 2229/2023: 7.º–16.º día hábil del mes siguiente).
- Orden directa: "liquida la retención de [cliente] [mes]".
- Invocada por el orquestador del ciclo tributario mensual o por *Tablero de Alertas y Pendientes*.
- Quién la invoca: *12-EspecialistaRetenciones-Senior*; el cierre del periodo lo aprueba siempre un humano (Contador Titular).

## Inputs

| Insumo | Origen | Si falta |
|--------|--------|----------|
| **Token DIAN del periodo** (a veces en `.zip`) — fuente de verdad | Descarga MUISCA / carpeta del cliente · [[Aux 20 - Interpretacion del Token DIAN]] | NO liquidar; solicitar al responsable y registrar el bloqueo |
| Libro auxiliar por tercero cuentas **2365** (retefuente), **2367** (ReteIVA) | Contabilidad del cliente (Excel) | NO liquidar; pedir reproceso contable |
| Balance de prueba por tercero del mes, **cuadrado** (débitos = créditos) | Contabilidad | Detener: auxiliar descuadrado = insumo inválido |
| Nómina del mes + soporte del cálculo Art. 383 ET | Frente de nómina del cliente | Liquidar el resto y dejar el bloque de rentas de trabajo abierto; escalar si no llega en 24 h |
| **RUT del cliente** (responsabilidad 15 — autorretenedor especial; responsabilidades ReteIVA) | Carpeta del cliente / RUT actualizado | NO parametrizar autorretención sin verificarlo |
| Calendario DIAN 2026 — fecha exacta por último dígito del NIT | `Calendario_Tributario_2026.pdf` · *Proyecto - Retencion en la Fuente* | NO asumir fecha: confirmar contra el PDF oficial |
| Criterios particulares del cliente | Nota `04 - Clientes/Cliente - X.md`, sección "Criterios particulares" (§3 del estándar) | Continuar solo con criterios generales y dejarlo registrado |
| Matriz de tarifas y bases del mes | [[Aux 14 - Calculo de Retenciones]] + [[Matriz Reparametrizacion Decreto 0572]] | Construirla desde *Proyecto - Retencion en la Fuente* antes de liquidar |

Verificar **identidad del insumo** (NIT y razón social DENTRO de cada archivo) antes de procesar — un archivo mal rotulado es un error real y grave. Excel corrupto → [[Manejo de Archivos Excel Corruptos]].

## Pasos

1. **Confirmar calendario y parámetros por NIT (NUNCA asumir).** Fecha exacta de vencimiento según último dígito del NIT en el calendario oficial (los días cívicos desplazan ventanas — pasó el 17/04/2026). Meta interna: presentar con **mínimo 2 días hábiles de margen**. *Validación:* fecha registrada en el papel de trabajo con fuente.
2. **Verificar el régimen de tarifas vigente — D. 0572/2025 (paso explícito, no opcional).** La tarifa aplicable es la vigente en la **fecha del pago o abono en cuenta** (no la fecha de factura):
   - **Periodos hasta junio 2026:** tarifas y bases del DUR **anteriores** al D. 0572 (suspensión provisional 07/05/2026, Comunicado DIAN 070).
   - **Desde ~julio 2026:** el Consejo de Estado revocó la suspensión el 02/06/2026; los arts. 2–8 recobran vigencia el primer día calendario del mes siguiente a la ejecutoria — previsiblemente **01/07/2026** `[VERIFICAR ejecutoria antes de reparametrizar]`. El art. 1 (CDAT = CDT) nunca se suspendió.
   - Parametrizar SIEMPRE desde [[Matriz Reparametrizacion Decreto 0572]] y confirmar con *21-MonitoreoNormativo-Senior*. Conservar trazabilidad por cliente (si el fallo de fondo anula el decreto, los efectos serían retroactivos).
   *Validación:* esquema aplicado (pre/post decreto) anotado en el papel de trabajo con la fecha de pago de cada concepto.
3. **Consolidar bases desde contabilidad y facturación.** Retención practicada por tercero y concepto = **crédito − débito de la cuenta 2365 por tercero**, excluyendo los cierres a nombre de la DIAN y las filas "SALDO INICIAL". Misma lógica para 2367 (ReteIVA). **2368 (ReteICA) NO entra al F-350** — alimenta *Skill - Presentar ICA Municipal*. *Validación:* total consolidado = movimiento neto del auxiliar.
4. **Cruzar contra el Token DIAN.** Facturas recibidas/emitidas sujetas a retención vs. lo contabilizado. Diferencia material (≥ 1 UVT individual o ≥ 0,5 % acumulada) se investiga y documenta antes de avanzar. El Token es la fuente de verdad. *Validación:* tabla de conciliación sin diferencias materiales abiertas.
5. **Clasificar PJ vs PN y liquidar el F-350 por casillas** (Res. 000031/2024): bases en casillas 29-41 (PJ) y 77-92 (PN); valores retenidos en 42-58 (PJ) y 93-112 (PN); rentas de trabajo siempre en bloque PN (77/93). Pagos al exterior por anexo con/sin convenio. Mapa completo de casillas en [[Protocolo Retencion en la Fuente F-350]]. *Validación:* casilla 130 = suma de conceptos renta − reintegros (129).
6. **Autorretención especial** (solo con responsabilidad 15 en el RUT): base = ingresos del mes por actividad × tarifa del esquema vigente (paso 2): 0,55 %/1,1 %/1,6 % hasta ~30/06/2026; tarifas por CIIU hasta 4,5 % desde la reactivación del D. 0572. Se declara en el mismo F-350 (bloques 70-76 PJ / 122-128 PN). *Validación:* base × tarifa = valor declarado.
7. **Cuadre de ReteIVA** (Arts. 437-1 y 437-2 ET, 15 % del IVA): casilla 131 (practicada a responsables de IVA) separada de la 132 (servicios de no residentes/digitales); total 134 = 131 + 132 − 133. Cuadrar contra el movimiento de la 2367 por tercero y contra el ReteIVA del frente de IVA ([[Skill - Presentar IVA Bimestral F300]]). *Validación:* 134 = movimiento neto 2367.
8. **Timbre (casilla 135)** solo si hubo documentos gravados en el mes (Arts. 514–518 ET) — caso excepcional; verificar antes de diligenciar. Total: 136 = 130 + 134 + 135; con sanciones, 138. Si el mes no tuvo operaciones sujetas a retención, **no es obligatorio declarar en ceros** (Art. 606 par. 6 ET) — documentar la decisión. *Validación:* aritmética de totales sin error.
9. **Revisión de cuatro ojos.** Segundo revisor (otro agente o el Master) repasa: esquema de tarifas aplicado, separación PJ/PN, exclusión de cierres DIAN, cuadres de los pasos 4 y 7, y el [[Checklist de Revision antes de Firmar]]. *Validación:* checklist firmado por el revisor.
10. **Firma, presentación y PAGO TOTAL.** Borrador + papeles al Contador Titular; tras aprobación, diligenciar en MUISCA y presentar con 2+ días hábiles de margen. Pagar **el 100 % con el F-490** verificando concepto y periodo exactos. **Regla existencial — Art. 580-1 ET: la declaración presentada sin pago total es INEFICAZ de pleno derecho** (equivale a no declarar). Excepciones tasadas (pago en 2 meses; faltante ≤ 10 UVT pagado en el año; saldo a favor ≥ 2× compensable): solo aplican documentadas y aprobadas por el Contador Titular. *Validación:* F-490 pagado verificado ANTES de dar por cerrado el periodo.
11. **Archivar papeles de trabajo:** acuse + F-350 firmado + F-490 + papel [[Aux 14 - Calculo de Retenciones]] + tabla de conciliación, en la carpeta canónica del cliente ([[Gestion de Papeles de Trabajo y Archivo]]). Registrar el cierre en el *Tablero de Alertas y Pendientes*. *Validación:* carpeta completa con los 5 documentos.
12. **Ciclo anual:** los 12 F-350 alimentan la exógena (F-1001 columna R y F-1003 — *Conciliacion Exogena vs Declaraciones*) y los **certificados anuales de retención a proveedores (Art. 381 ET)**, que deben coincidir con lo declarado y emitirse dentro del plazo reglamentario del año siguiente ([[Certificados de Retencion y Documentos Anuales]]). *Validación:* suma F-350 del año = certificados emitidos = F-1001 columna R.

## Outputs y criterios de aceptación

| Output | Criterio de aceptación |
|--------|------------------------|
| F-350 presentado en MUISCA | Firmado por el Contador Titular; presentado con ≥ 2 días hábiles de margen; **F-490 pagado por el 100 %** (sin pago = NO aceptado) |
| Papel de trabajo de liquidación (Excel) | Casillas cuadradas: 2365/2367 ↔ Token ↔ F-350 sin diferencia material (≥ 1 UVT o ≥ 0,5 %); cero errores de fórmula |
| Tabla de conciliación de diferencias | Toda diferencia investigada con causa, ajuste, fecha y responsable (ninguna "explicada de palabra") |
| Carpeta archivada | Acuse + F-350 + F-490 + papeles + conciliación |
| Registro en Tablero | Periodo marcado cerrado solo con pago verificado |

## Manejo de errores y fallback

- **Auxiliar descuadrado o archivo de otro cliente:** detener, devolver a contabilidad; nunca liquidar sobre insumo inválido.
- **Token DIAN no disponible:** no se presenta con contabilidad sola; escalar la consecución del Token. Si el vencimiento está a < 3 días hábiles, escalar de inmediato al Contador Titular para decisión.
- **Diferencia material Token ↔ contabilidad que revela error contable:** se corrige la contabilidad, no el formato (regla de oro C.8/D.10).
- **Duda sobre el esquema de tarifas (transición D. 0572):** aplicar el esquema pre-decreto (posición conservadora vigente a junio 2026), documentar, y confirmar con *21-MonitoreoNormativo-Senior* antes de presentar.
- **Imposibilidad de pago total del cliente:** NO presentar sin pago por defecto; evaluar las 3 excepciones del Art. 580-1 con el Contador Titular y documentar la elegida; si ninguna aplica, alertar por escrito al cliente del efecto de ineficacia y la extemporaneidad corriendo.
- **Error propio detectado tras presentar:** notificar de inmediato y proyectar corrección (Art. 644 ET) — herencia de auto-corrección base.
- **Excel corrupto:** [[Manejo de Archivos Excel Corruptos]].

## Escalamiento

| Situación | Escala a |
|-----------|----------|
| Diferencia material no resuelta, decisión de no declarar en ceros, duda de régimen D. 0572, o impacto ≥ **50 UVT** | Master del dominio (retencion-master) + registro en `memoria.decisiones` |
| Impacto ≥ **500 UVT**, riesgo de ineficacia Art. 580-1, error en declaración ya presentada, o aplicación de una excepción del 580-1 | **Contador Titular (humano)** |
| Firma y presentación | SIEMPRE humano — el agente nunca presenta sin firma |
| Requerimiento DIAN sobre un F-350 | *18-DefensaTributaria-Master* |

## Métricas

| KPI | Meta | Frecuencia |
|-----|------|------------|
| Declaraciones presentadas con pago total y en plazo | 100 % | Mensual |
| Declaraciones ineficaces (Art. 580-1) | 0 | Mensual |
| Margen de presentación | ≥ 2 días hábiles | Mensual |
| Diferencias materiales abiertas al presentar | 0 | Mensual |
| Margen de error de liquidación | < 2 % | Mensual |
| Certificados Art. 381 emitidos en plazo y cuadrados con F-350 | 100 % | Anual |

## Tests

1. **Normal:** cliente PJ con retefuente, ReteIVA y responsabilidad 15; junio 2026 → liquidación con esquema pre-D. 0572, separación PJ/PN correcta, cuadre 2365/2367 ↔ Token sin diferencias, F-350 + F-490 pagados con 2+ días de margen.
2. **Excepción — sin pago total:** el cliente no gira los fondos al vencimiento → la skill NO presenta por defecto, evalúa las 3 excepciones del Art. 580-1, escala al Contador Titular y documenta la alerta escrita al cliente.
3. **Transición de régimen:** retención de julio 2026 con pagos de junio y de julio → cada pago con la tarifa de su fecha de pago/abono (junio pre-decreto, julio D. 0572 si quedó ejecutoriado), trazabilidad por concepto.
4. **Mes sin operaciones:** no se presenta en ceros (Art. 606 par. 6); decisión documentada en el papel de trabajo y en el Tablero.

## Historial de versiones

| Versión | Fecha | Cambio |
|---------|-------|--------|
| 1.0 | 2026-06-11 | Creación inicial sobre [[Protocolo Retencion en la Fuente F-350]] y *Proyecto - Retencion en la Fuente*, conforme al *00 - Estandar de Skills RITORE* (gap crítico identificado en auditoría del ciclo tributario). |

## Relacionado

- [[Protocolo Retencion en la Fuente F-350]] · *Proyecto - Retencion en la Fuente* · [[Matriz Reparametrizacion Decreto 0572]]
- [[Aux 14 - Calculo de Retenciones]] · [[Aux 20 - Interpretacion del Token DIAN]] · [[Certificados de Retencion y Documentos Anuales]]
- [[Skill - Presentar IVA Bimestral F300]] · *Skill - Presentar ICA Municipal* · *Skill - Preparar Renta PJ F110*
- *Conciliacion Exogena vs Declaraciones* · *Formato 1001 - Pagos y Retenciones* · *Formato 1003 - Retenciones que le practicaron*
- *12-EspecialistaRetenciones-Senior* · *21-MonitoreoNormativo-Senior* · *18-DefensaTributaria-Master*
- [[ET - Retencion en la Fuente Articulos Clave]] · [[UVT y Topes]] · *MOC - Skills*
