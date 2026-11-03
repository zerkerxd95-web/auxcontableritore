---
tipo: conocimiento
tags: [ritore, conocimiento, protocolo, impuestos]
estado: vigente
fecha: 2026-06-08
---

# Protocolo Elaboración de Impuestos (Protocolo Maestro)

Protocolo transversal de la firma para elaborar y presentar **CUALQUIER impuesto** (IVA, retención en la fuente, RST, renta PJ, renta PN, ICA). Generaliza el método que ya funciona en IVA ([[Protocolo IVA Formulario 300]], Parte D del CLAUDE.md raíz) y las lecciones de exógena (Parte C). Los protocolos específicos ([[Protocolo IVA Formulario 300]], *Protocolo Renta Persona Juridica F-110*) detallan cada impuesto; este define el **esqueleto común de 10 pasos** que ninguno se salta.

> **Regla de oro:** el papel de trabajo manda. Cada cifra del formulario debe ser rastreable hasta su origen (token DIAN o cuenta contable). Si no se puede rastrear, no se declara.

## Los 10 pasos

### Paso 1 — Confirmar obligación y calendario del cliente
- Verificar en el **RUT**: responsabilidades vigentes (IVA 48, retención 07, autorretenedor especial 15, RST 47, etc.) y periodicidad (IVA bimestral/cuatrimestral — regla D.6: **confirmar SIEMPRE por cliente, no asumir**).
- Vencimiento exacto según el **último dígito (o dos últimos) del NIT** y el calendario oficial DIAN (Decreto 2229/2023 — calendario permanente en días hábiles). Ojo con días cívicos sobrevinientes que desplazan ventanas (pasó con el 17/04/2026).
- Verificar vigencia normativa del periodo: tarifas y bases pueden cambiar dentro del año (caso *Decreto 0572 de 2025*: suspendido 08/05/2026, revocada la suspensión el 02/06/2026 — la tarifa aplicable es la vigente en la **fecha del pago o abono en cuenta**).

### Paso 2 — Recopilar insumos
- **Token DIAN del periodo = fuente de verdad** (a veces dentro de un `.zip`). Ver [[Aux 20 - Interpretacion del Token DIAN]].
- **Balance de prueba** + **libro auxiliar** del periodo (por tercero cuando el impuesto lo exige).
- **Declaraciones anteriores** del mismo impuesto (arrastre de saldos a favor, comparativo) y declaraciones conexas para cruces.
- Verificar **identidad de los insumos**: NIT y razón social DENTRO del archivo deben corresponder al cliente — un archivo mal rotulado es un error real y grave.

### Paso 3 — Verificar integridad de archivos y cuadre del auxiliar
- Regla C.1: los `.xlsx` en carpetas sincronizadas se corrompen mientras están abiertos en Excel. Si sale `BadZipFile`: **NO reintentar en bucle** — pedir cerrar el archivo o "Guardar como" con nombre nuevo. Ver [[Manejo de Archivos Excel Corruptos]].
- Verificar que el libro auxiliar **cuadre débitos = créditos** antes de procesarlo.
- Año contable sin cerrar (patrón recurrente, regla D.5): trabajar con los **MOVIMIENTOS del periodo**, nunca con saldos acumulados; **excluir filas "SALDO INICIAL"**. Declararlo como hallazgo, no frenar la liquidación.

### Paso 4 — Liquidar con papel de trabajo estándar
- Siempre **desglosar base e impuesto**: `Base = Total − Impuesto`. **NUNCA tarifas planas** (no aplicar 19 % plano en IVA; usar el impuesto real por factura — hay 5 %, exentos, excluidos, tarifas mixtas). La tarifa de IVA del 21 % no existe en Colombia: si aparece, es error.
- Hoja de trabajo con detalle por tercero/factura y totales de control que amarren con el formulario casilla por casilla.
- Aplicar criterios particulares del cliente **sin generalizarlos** (regla D.8): un criterio de un cliente NUNCA se generaliza sin confirmar.

### Paso 5 — Cruzar contra fuentes
- **Token DIAN ↔ contabilidad** (ventas, compras, ingresos).
- **Retenciones declaradas ↔ auxiliar 2365** (crédito − débito por tercero, excluyendo cierres a nombre de la DIAN; reteIVA 2367, reteICA 2368).
- **Ingresos ↔ facturación electrónica** del periodo.
- Los cruces de hoy son los mismos que hará la DIAN con la exógena: ver *Conciliacion Exogena vs Declaraciones*.

### Paso 6 — Cuadrar y documentar diferencias
- Umbral de materialidad: **diferencia individual ≥ 1 UVT o acumulada ≥ 0,5 % del total** → se investiga y se resuelve antes de avanzar.
- Si la diferencia viene de un error contable (año sin cerrar, reclasificaciones mal hechas), **se corrige la contabilidad, nunca se maquilla el formulario** (regla C.8/D.10). Documentar causa raíz.
- Si revela un error en una declaración ya presentada → escalar al Contador Titular antes de continuar.

### Paso 7 — Diligenciar el formulario oficial (MUISCA / borrador)
- Usar la **versión vigente** del formulario y su instructivo (ver [[Formularios DIAN - Catalogo]] — nunca usar formulario/UVT/tarifa de otro año).
- Diligenciar el borrador en MUISCA o en plantilla espejo; verificar casillas críticas (p. ej. F-300: casillas 50-57 llevan la **BASE sin IVA**, regla D.4).
- Cotejar el borrador casilla por casilla contra el papel de trabajo.

### Paso 8 — Revisión y FIRMA del Contador Titular
- Entregar papel de trabajo + borrador + hallazgos. **NUNCA presentar sin la firma/aprobación del Contador Titular.** El trabajo apoya, no sustituye la firma.

### Paso 9 — Presentar con margen y pagar
- Presentar con **mínimo 2 días hábiles de margen** antes del vencimiento — nunca el último día (caídas del portal DIAN son frecuentes).
- Pagar con el **F-490** (recibo oficial de pago). En retención en la fuente el pago total es existencial: declaración sin pago total = **ineficaz de pleno derecho (Art. 580-1 ET)**, con las excepciones verificadas en *Proyecto - Retencion en la Fuente*.
- En RST el F-2593 es un recibo que se paga (no declaración); la mora pone en riesgo la permanencia (Art. 914 ET).

### Paso 10 — Archivar y actualizar el AVANCE
- Archivar **acuse + formulario presentado + recibo de pago + papel de trabajo** en la carpeta canónica del cliente.
- Actualizar el archivo `AVANCE_<obligación>_<cliente>.md` (regla C.9): fuentes usadas, valores de control, criterios aplicados, pendientes. Al reiniciar sesión, leerlo antes de continuar.
- Si hubo lección nueva → registrarla en el protocolo del impuesto y/o *Lecciones Aprendidas Exogena* (o su equivalente).

## Matriz impuesto → insumos → papel de trabajo → formulario → casillas críticas → errores típicos

| Impuesto | Insumos clave | Papel de trabajo | Formulario | Casillas críticas | Errores típicos (ya cometidos/vistos) |
|---|---|---|---|---|---|
| **IVA** | Token DIAN, BP, auxiliar (41xx, 2408, 2367), declaración anterior | Excel 11 hojas modelo "INVERSIONES N" | F-300 | 50-57 = **BASE sin IVA** (regla D.4); reteIVA; saldo a favor anterior solo si se arrastra | Total con IVA en casillas de base; 19 % plano; notas crédito no restadas; DSEL emitido tomado como venta; saldos acumulados de año sin cerrar |
| **Retención (RTFT)** | Token DIAN, auxiliar 2365/2367/2368, BP | Liquidación por tercero: crédito − débito 2365 | F-350 | Total retenciones ↔ movimiento 2365 del mes; autorretención especial (resp. 15); separación PJ/PN | Presentar sin pago total (ineficacia 580-1); incluir cierres a nombre de la DIAN; tarifa de fecha equivocada (cronología D. 0572) |
| **RST anticipo** | Token DIAN del bimestre, auxiliar, BP | Ingresos del bimestre por municipio | F-2593 | Ingresos brutos del bimestre **por token**; componente ICA consolidado por municipio; grupo/tarifa Art. 908 | Tomar ingresos contables en vez del token; municipio mal asignado; no pagar (riesgo exclusión Art. 914) |
| **RST anual** | Tokens del año, auxiliares, F-2593 pagados | Consolidación anual + anticipos descontados | F-260 | Ingresos anuales por grupo; anticipos pagados; ICA por municipio; descuento 0,5 % pagos electrónicos | No descontar anticipos; grupo de tarifa errado; omitir IVA anual del responsable |
| **Renta PJ** | EEFF cerrados, balance por tercero, declaraciones del año (IVA/RTFT/exógena), renta anterior | Conciliación 2516 → F-110; anexos TTD, diferido | F-110 + Formato 2516 | Ingresos ↔ F-1007/exógena; costos/deducciones ↔ F-1001; patrimonio; TTD ≥ 15 %; anticipo Art. 807 | Deducir sin soporte (771-2) o sin bancarización (771-5); omitir TTD; no armonizar con exógena; ver *Protocolo Renta Persona Juridica F-110* |
| **Renta PN** | Certificados (ingresos, retenciones, 2276), información exógena reportada por terceros, extractos | Depuración cedular | F-210 (+2517 si lleva contabilidad) | Rentas por cédula; límite 40 %/1.340 UVT de beneficios; retenciones ↔ certificados | Omitir ingresos que terceros sí reportaron en exógena; duplicar beneficios; residencia mal evaluada |
| **ICA / reteICA** | Token DIAN/facturación por municipio, auxiliar 2368, estatuto municipal | Ingresos por municipio y actividad | Formulario municipal (Medellín: declaración anual + reteICA) | Tarifa por actividad CIIU **según municipio**; territorialidad del ingreso | Aplicar tarifa de otro municipio; no descontar deducciones territoriales; ver *Proyecto - ICA y Retenciones Municipales* |

## Semáforo de entregables

Todo encargo cierra con (modelo D.9):
- 🟢 **Excel** `FORMATO [N°] [IMPUESTO] [PERIODO] [CLIENTE] - Claude.xlsx` — modelo 11 hojas (Resumen, Formulario, detalle del impuesto generado/descontable o equivalente, Cuadres, Cruce DIAN vs Contab, Detalle por NIT, Compras DIAN, Ventas DIAN, Nómina, Comparativo). Hojas de detalle separan "Base (sin impuesto)" y "Total (con impuesto)". Cero errores de fórmula.
- 🟡 **Word** `INFORME EJECUTIVO [IMPUESTO] [PERIODO] [CLIENTE] - Claude.docx` — semáforo, liquidación, cruce, hallazgos con severidad, sustento normativo, plan de acción.
- 🔴 **Reporte a fecha de corte** (cuando aplica): declarar EXPRESAMENTE que es corte parcial, no la declaración definitiva.

## Ética (regla D.10 — innegociable)

Nunca forzar ni "maquillar" cifras para que cuadren. Si una diferencia viene de un error contable, se corrige la contabilidad, no el formulario. Documentar la causa raíz y escalar al Contador Titular. No presentar sin su firma. No facilitar evasión, simulación ni abuso (Art. 869 ET); ante operación inusual, activar el canal SAGRLAFT sin tipping-off.

## Fuentes (consultadas 2026-06-08)

- DIAN — Formularios e instructivos: https://www.dian.gov.co/atencionciudadano/formulariosinstructivos/Paginas/default.aspx
- DIAN — Calendario Tributario 2026: https://www.dian.gov.co/Calendarios/Calendario_Tributario_2026.pdf
- Práctica interna verificada: CLAUDE.md raíz (Partes C y D), [[Protocolo IVA Formulario 300]], *Proyecto - Retencion en la Fuente*, *Proyecto - Regimen Simple RST*, CLAUDE.md de RENTAS PERSONA JURIDICA 2025

## Relacionado

- *MOC - Conocimiento Tecnico* · *Protocolo de Razonamiento 10 Pasos*
- [[Protocolo IVA Formulario 300]] · *Protocolo Renta Persona Juridica F-110* · [[Formularios DIAN - Catalogo]]
- *Conciliacion Exogena vs Declaraciones* · [[Manejo de Archivos Excel Corruptos]] · [[Margen de Error 2 por ciento]]
- [[Aux 20 - Interpretacion del Token DIAN]] · [[UVT y Topes]]
- Proyectos: *Proyecto - IVA 2026* · *Proyecto - Retencion en la Fuente* · *Proyecto - Regimen Simple RST* · *Proyecto - Rentas Persona Juridica 2025* · *Proyecto - Rentas Persona Natural* · *Proyecto - ICA y Retenciones Municipales* · *Proyecto - Exogena 2026*
- Agentes: *11-EspecialistaIVA-Master* · *12-EspecialistaRetenciones-Senior* · *13-EspecialistaRenta-Senior* · *14-EspecialistaExogena-Master*
