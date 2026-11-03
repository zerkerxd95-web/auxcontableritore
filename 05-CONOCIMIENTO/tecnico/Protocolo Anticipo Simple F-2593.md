---
tipo: conocimiento
tags: [ritore, conocimiento, protocolo, rst]
formulario: F-2593
periodicidad: bimestral
estado: vigente
fecha: 2026-06-08
---

# Protocolo Anticipo Simple — F-2593 (Recibo Electrónico del SIMPLE)

Protocolo específico para liquidar y pagar el **anticipo bimestral del Régimen Simple de Tributación (Formulario 2593)** de los clientes RST del portafolio. Es un **recibo electrónico que se paga, NO una declaración**: si no se paga, no existe, y la mora pone en riesgo la permanencia en el régimen (Art. 914 ET). Sigue el esqueleto de [[Protocolo Elaboracion de Impuestos]]; aquí solo lo específico del anticipo SIMPLE. Tarifas por grupo, calendario y estado del régimen 2026: ver *Proyecto - Regimen Simple RST* (reutilizar, no reinvestigar). Objetivo de calidad: margen de error < 2 % ([[Margen de Error 2 por ciento]]).

## Marco normativo y versión vigente

| Norma | Contenido |
|-------|-----------|
| **Libro VIII ET, Arts. 903–916** | Régimen Simple: hecho generador, sujetos, **tarifas (Art. 908)**, declaración y pago (Art. 910), exclusión (Art. 914). |
| **Art. 910 ET** | Obligación de pagar **anticipos bimestrales** mediante el recibo electrónico y de presentar la declaración anual consolidada. |
| **Art. 908 par. 4 ET** | Grupos de actividad y rangos de tarifa; par. 5: si hay varias actividades se aplica la **tarifa más alta**. |
| **Ley 2155/2021 (Art. 42)** | Tope de ingresos 100.000 UVT y grupos de tarifas. |
| **Sentencia C-540/2023** | Revivió el numeral 3 del Art. 42 Ley 2155 (servicios profesionales: grupo "3 sic", tope 100.000 UVT y tarifas 5,9 %–14,5 %). |
| **D. 2229/2023** | Plazos de los anticipos bimestrales. |

**Formulario vigente:** **F-2593 prescrito por la Resolución 000081 de 2024** (AG 2024 y siguientes), **versión 6** según la guía práctica DIAN — el mismo para 2026 `[VERIFICAR si hay resolución posterior para AG 2026 con MonitoreoNormativo]`. Estado del régimen: **VIGENTE en 2026** (la ley de financiamiento 2025 se hundió el 09/12/2025 y los decretos de emergencia fueron declarados inexequibles — C-075 y C-079 de 2026); no hubo derogatoria del RST. Detalle en *Proyecto - Regimen Simple RST*.

> **Grupos del formulario (etiquetas oficiales, atención a la rareza):** el F-2593 rotula los grupos como **Grupo 1, Grupo 2, Grupo 3, "Grupo 3 (sic)" y Grupo 6**. El "Grupo 3" del formulario = expendio de comidas/bebidas y transporte (numeral 3 del Art. 908); el **"Grupo 3 (sic)"** = servicios profesionales/consultoría/científicos (numeral revivido por la C-540/23). El Grupo 6 = CIIU 4665/3830/3811 (1,62 %). El SI de Diligenciamiento aplica la tarifa automáticamente según el grupo y el rango de ingresos.

## Insumos (no se liquida sin esto)

1. **Token DIAN del bimestre** — **fuente de verdad de los ingresos brutos facturados**. Interpretación: [[Aux 20 - Interpretacion del Token DIAN]]. Si viene en `.zip`, descomprimir; si el Excel no abre, aplicar [[Manejo de Archivos Excel Corruptos]].
2. **Libro auxiliar y balance de prueba** del bimestre, para cruzar contra el token (movimientos del periodo, excluir "SALDO INICIAL" — regla D.5).
3. **Nota del cliente** con su **grupo de tarifa del Art. 908** y los **municipios/distritos** donde genera ingresos (para el componente ICA consolidado, hoja 2).
4. **RUT:** confirmar la **responsabilidad 47** (RST) y si es responsable de IVA y/o de INC de comidas y bebidas.
5. Certificados de **aportes a pensión a cargo del empleador** pagados en el bimestre (descuento, casilla 45) y, si aplica, certificación de **pagos electrónicos** (0,5 %) o del **GMF** (descuentos del anual, no del anticipo).

## Paso a paso

1. **Determinar los ingresos brutos del bimestre por el Token DIAN** (sin incluir ganancias ocasionales). NO tomar el saldo contable acumulado: usar los **ingresos facturados del bimestre**. Cruzar contra el auxiliar.
2. **Clasificar los ingresos por grupo de actividad** (Art. 908) y por **municipio/distrito** (necesario para el ICA consolidado de la hoja 2). Si el cliente desarrolla actividades de un solo grupo, todo va a ese grupo; si son varias, el SI aplica la tarifa más alta (par. 5 Art. 908).
3. **Diligenciar los ingresos por grupo** (casillas 26-35, país y exterior por cada grupo). El SI consolida en la casilla 39.
4. **Restar ingresos no constitutivos de renta** (casilla 40) → total ingresos netos (casilla 41).
5. **Aplicar la tarifa SIMPLE consolidada** (casilla 36, automática por grupo y rango): anticipo SIMPLE = casilla 41 × casilla 36 (casilla 42). Tarifas por grupo en *Proyecto - Regimen Simple RST* y en el mapa de casillas abajo.
6. **Restar el ICA consolidado del bimestre** (casilla 43, viene de la hoja 2) → valor del componente SIMPLE nacional (casilla 44).
7. **Aplicar descuentos:** aportes a pensión del empleador pagados en el bimestre (casilla 45, limitados) → anticipo neto SIMPLE (casilla 49). El **descuento del 0,5 % por pagos electrónicos y el GMF se aplican en la declaración anual (F-260), no aquí.**
8. **Liquidar el ICA territorial integrado** en la hoja 2 por municipio (ingresos gravados × tarifa por mil del acuerdo municipal) → casilla 99 → alimenta la casilla 43 del componente nacional y la casilla 76 (ICA municipios) de valores a pagar.
9. **Liquidar IVA bimestral del RST** (casillas 66-75) e **INC de comidas y bebidas 8 %** (casillas 58-65) solo si el cliente es responsable — el RST transfiere el IVA cada bimestre por este recibo, pero la **declaración de IVA es anual** (cruce en *Proyecto - IVA 2026*).
10. **Pagar con el Formulario 490** generado desde el recibo. Sin pago, el anticipo no existe.

## Mapa de casillas del F-2593 (Res. 000081/2024 v6)

Casillas verificadas en el instructivo oficial DIAN (Formulario_2593_2024.pdf).

**Datos generales y ajustes:** 1 Año · 3 Período (01 ene-feb … 06 nov-dic) · 5 NIT · 6 DV · 24 Ajuste · 25 N.º recibo 2593 anterior.

**Ingresos brutos bimestrales por grupo (país / exterior):**

| Grupo | País | Exterior |
|-------|------|----------|
| Grupo 1 (tiendas, peluquerías) | 26 | 27 |
| Grupo 2 (comercio, industria, telecom, construcción) | 28 | 29 |
| Grupo 3 (comidas/bebidas, transporte) | 30 | 31 |
| Grupo 3 (sic) (profesionales/consultoría) | 32 | 33 |
| Grupo 6 (CIIU 4665/3830/3811 = 1,62 %) | 34 | 35 |

**Liquidación anticipo componente SIMPLE nacional:**

| Casilla | Concepto |
|---------|----------|
| 36 | **Tarifa SIMPLE consolidada** (automática por grupo y rango) |
| 37 / 38 | Ganancias ocasionales país / exterior (informativas) |
| 39 | Ingresos brutos bimestrales (suma 26 a 35) |
| 40 | Ingresos no constitutivos de renta |
| 41 | Total ingresos netos bimestrales (39 − 40) |
| 42 | **Anticipo SIMPLE** (41 × 36) |
| 43 | ICA consolidado liquidado durante el bimestre (de hoja 2, casilla 99) |
| 44 | Valor del anticipo componente SIMPLE nacional (42 − 43) |
| 45 | Aportes a pensión del empleador pagados en el bimestre (descuento) |
| 46–48 | Excedentes / límite / exceso de aportes |
| 49 | **Anticipo neto impuesto unificado SIMPLE** (44 − 47) |

**Determinación del valor a pagar:**

| Casilla | Concepto |
|---------|----------|
| 50 | Retenciones/autorretenciones de renta practicadas **antes** de pertenecer al RST (solo 1.er bimestre del año) |
| 51 | Excedente anticipo SIMPLE del bimestre anterior |
| 52 | Saldo a favor por impuesto SIMPLE de la declaración (F-260) del año anterior |
| 53 | Saldo anticipo SIMPLE (49 − 50 − 51 − 52) |
| 56 | **Total a pagar anticipo impuesto SIMPLE** |
| 57 | Excedente anticipo impuesto SIMPLE |

**INC de comidas y bebidas:** 58 ingresos gravados · 59 INC 8 % · 60–65 excedentes/saldo · 64 total a pagar INC.
**IVA bimestral RST:** 66 IVA generado · 67 descontables · 68 saldo a favor F-300 año anterior · 70 ReteIVA que le practicaron · 71 saldo · 74 total a pagar IVA bimestral · 75 excedente.
**Valores a pagar:** 76 ICA municipios (hoja 2 casilla 104) · 77 anticipo SIMPLE (=56) · 78 INC (=64) · 79 IVA (=74) · 80/81 número y fecha del F-490 asociado.

**Hoja 2 — ICA consolidado territorial por municipio:** 82 departamento · 83 municipio · 84 ingresos brutos del municipio · 85-89 detracciones (devoluciones, exportaciones, venta activos fijos, excluidos, exentos) · 90 ingresos gravables · 91 CIIU · 92 ingresos gravados · 93 tarifa (por mil) · 94 impuesto · 95-99 totales ICA bimestral · 104 saldo a pagar componente ICA territorial · 106 ganancias ocasionales (informativa).

**Tarifas bimestrales por grupo (impresas en el formulario; rangos en UVT de ingresos brutos bimestrales 0–1.000 / 1.000–2.500 / 2.500–5.000 / 5.000–16.666):**

| Grupo | Tarifas por rango |
|-------|-------------------|
| Grupo 1 | 1,2 % · 2,8 % · 4,4 % · 5,6 % |
| Grupo 2 | 1,6 % · 2,0 % · 3,5 % · 4,5 % |
| Grupo 3 (comidas/transporte) | 3,1 % · 3,4 % · 4,0 % · 4,5 % `[el formulario imprime estos; el Art. 908 vigente para el cálculo anual lista 3,4 %/3,8 %/5,5 %/7,0 % para comidas+transporte — VERIFICAR el rango y la sobretasa INC con el texto vigente del Art. 908 antes de liquidar un caso real]` |
| Grupo 3 (sic) (profesionales) | 5,9 % · 7,3 % · 12,0 % · 14,5 % |
| Grupo 6 | 1,62 % (tarifa única) |

## Cuándo NO genera pago pero sí se presenta

- **Bimestre sin operaciones gravadas con ICA:** igual se diligencia la **hoja 2** registrando en la casilla 91 el CIIU de la actividad principal (lo exige el instructivo).
- **Anticipo SIMPLE en cero** (ingresos del bimestre = 0, o totalmente absorbido por descuentos/excedentes): el recibo se presenta para dejar trazabilidad del bimestre, aunque el valor a pagar sea cero.
- **Personas naturales del RST con ingresos brutos < 3.500 UVT** del año: NO están obligadas a pagar anticipos bimestrales; solo presentan la **declaración anual (F-260)**. Verificar antes de liquidar (evita generar anticipos innecesarios).

## Cuadres y cruces

- **Token DIAN ↔ contabilidad:** los ingresos del bimestre del token deben cuadrar con los ingresos facturados del auxiliar (movimientos, no saldo). Umbral material: diferencia ≥ 1 UVT o ≥ 0,5 % del total.
- **Suma de ingresos por grupo (casillas 26-35) = ingresos brutos del token** (sin ganancias ocasionales).
- **ICA de la hoja 2 ↔ ingresos por municipio** desglosados del token.
- **Acumulado de los 6 anticipos del año ↔ ingresos del F-260** (la consolidación anual debe cerrar contra los recibos) — ver *Protocolo Declaracion Anual Simple F-260*.
- **IVA del recibo ↔ declaración anual de IVA del RST** (*Proyecto - IVA 2026*).

## Calendario 2026

Plazos según D. 2229/2023 y calendario DIAN 2026 (último dígito del NIT). Confirmar el día exacto en `Calendario_Tributario_2026.pdf`:

| Anticipo F-2593 | Periodo (bimestre) | Vencimientos |
|------------------|--------------------|--------------|
| Bimestre 1 | ene-feb 2026 | 12 – 26 de mayo de 2026 |
| **Bimestre 2** | **mar-abr 2026** | **10 – 24 de junio de 2026** (próximo hito) |
| Bimestre 3 | may-jun 2026 | 9 – 23 de julio de 2026 |
| Bimestre 4 | jul-ago 2026 | 9 – 22 de septiembre de 2026 |
| Bimestre 5 | sep-oct 2026 | 11 – 25 de noviembre de 2026 |
| Bimestre 6 | nov-dic 2026 | 13 – 26 de enero de 2027 |

> Los anticipos del **AG 2026** se presentan a lo largo de 2026; el AG 2025 ya se consolida en el **F-260 de abril 2026** (*Protocolo Declaracion Anual Simple F-260*).

## Errores típicos

- **Tomar los ingresos por saldo contable acumulado** en vez de los **movimientos del bimestre del token** — error recurrente (regla D.5); infla la base.
- **No desglosar los ingresos por municipio** → ICA consolidado mal liquidado en la hoja 2.
- **Confundir "Grupo 3" con "Grupo 3 (sic)"** → tarifa errada (comidas 3,x % vs profesionales hasta 14,5 %).
- **Aplicar el descuento del 0,5 % por pagos electrónicos en el anticipo** — ese descuento (y el GMF) van en el **F-260 anual**, no en el F-2593.
- **No pagar el recibo:** el F-2593 sin pago no existe; la mora arriesga la **exclusión del RST** (Art. 914) y el retorno al régimen ordinario por todo el año.
- **Generar anticipos a una PN con ingresos < 3.500 UVT** que solo debía presentar el anual.
- Liquidar sobre un token de otro periodo o cliente (verificar año, periodo y NIT dentro del archivo).

## Clientes aplicables (RST con anticipos bimestrales)

- **Cliente - SALÓN DE BELLEZA I**
- **Cliente - EMPRESA Q**
- **Cliente - EMPRESA V**
- **Cliente - PLÁSTICOS AD**
- **Cliente - CONSTRUCTORA X**
- **Cliente - CENTRO CULTURAL M**
- **Cliente - EMPRESA DE TECNOLOGÍA K**
- **Cliente - CLIENTE DE GERENCIA FINANCIERA F**

> Cartera RST completa en *Proyecto - Regimen Simple RST* (incluye además CANTERA AE, CONSTRUCTORA AA, AGENCIA DE EVENTOS AH, CONSTRUCTORA W). En cada cliente confirmar la responsabilidad 47 en el RUT, el grupo de tarifa y si una PN está bajo el tope de 3.500 UVT (solo anual).

## Fuentes (consultadas 2026-06-08)

- DIAN — Formulario 2593 e instructivo (Res. 000081/2024 v6, casillas verificadas): https://www.dian.gov.co/atencionciudadano/formulariosinstructivos/Formularios/2024/Formulario_2593_2024.pdf
- DIAN — Guía práctica para diligenciar el F-2593 v6: https://www.dian.gov.co/impuestos/Regimen-Simple-de-Tributacion-RST/Documents/Guia-practica-diligenciar-recibo-electronico-F2593-2024.pdf
- DIAN — Micrositio RST (calendario y guías): https://micrositios.dian.gov.co/regimen-simple-tributacion/
- DIAN — Calendario Tributario 2026: https://www.dian.gov.co/Calendarios/Calendario_Tributario_2026.pdf
- Estatuto.co — Art. 908 ET (tarifas y grupos): https://estatuto.co/908
- Actualícese — Régimen simple (tarifas y novedades 2026): https://actualicese.com/regimen-simple/

## Relacionado

- *MOC - Conocimiento Tecnico* · [[Protocolo Elaboracion de Impuestos]] · [[Formularios DIAN - Catalogo]]
- *Protocolo Declaracion Anual Simple F-260* · [[Protocolo IVA Formulario 300]]
- *Proyecto - Regimen Simple RST* · *Proyecto - IVA 2026* · *Proyecto - ICA y Retenciones Municipales*
- [[Aux 20 - Interpretacion del Token DIAN]] · [[Manejo de Archivos Excel Corruptos]]
- *11-EspecialistaIVA-Master* · *13-EspecialistaRenta-Senior* · *21-MonitoreoNormativo-Senior*
- [[UVT y Topes]] · [[Margen de Error 2 por ciento]] · *Tablero de Alertas y Pendientes*
