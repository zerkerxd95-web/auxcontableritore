---
name: politica-html-formato-dian
description: "Todo HTML de un impuesto (borrador/formato) debe ser visualmente idéntico al formulario oficial de la DIAN, no un diseño propio."
metadata: 
  node_type: memory
  type: feedback
---

Cuando el usuario pida elaborar un **HTML de un impuesto** (renta, IVA, retención, etc.) para tener el formato o borrador, ese HTML **debe replicar el formulario oficial de la DIAN al 100%**: misma estructura, mismas casillas numeradas, mismas etiquetas/renglones, misma disposición (cabecera con el número de formulario, secciones con etiquetas verticales, dos columnas, bloque de firmas), no un diseño propio "bonito".

**Why:** el usuario usa esos HTML como borrador/prevalidación para transcribir al prevalidador DIAN; si el formato difiere, no le sirve como referencia y pierde confianza en el entregable. Ya ocurrió con la renta de EMPRESA AUDIOVISUAL BK (primero la hice con un diseño propio y hubo que rehacerla calcando el Formulario 110).

**How to apply:**
- Antes de generar, buscar en el vault un formulario oficial ya diligenciado del mismo impuesto (ej. Formulario 110 renta PJ, 300 IVA, 350 retención) y **calcar su estructura** (renderizar el PDF con PyMuPDF y extraer texto para copiar etiquetas y números de casilla exactos). Fuente usada para el 110: `TRABAJOS Y REQUERIMIENTOS/CLIENTES/EXOGENAS 2026/PRESENTADAS/EXPORTADORA DE SERVICIOS B/RENTA 2025/`.
- Respetar: cabecera DIAN + caja del número de formulario (110, 300, 350…), fila "1. Año", bloque "Datos del declarante" (NIT, DV, razón social, cód. seccional, actividad), datos informativos, la rejilla de casillas numeradas con sus etiquetas literales, y el bloque inferior de firmas (declarante / contador o revisor fiscal, cód. 982, tarjeta profesional 983, pago total 980).
- Separador de miles como en el formulario MUISCA de referencia; valores alineados a la derecha; ceros mostrados como "0".
- Solo cambian los VALORES (los del cliente) y la firma; la plantilla es idéntica a la DIAN.

**Refuerzo del titular (2026-09-08), regla general para TODA liquidación de impuestos:** cada vez que se liquide un impuesto se genera SIEMPRE (sin que lo pidan) el HTML calcado del formulario con las cifras completas, Y ese mismo HTML debe traer al pie la explicación del plan de ajustes propuesto en el Excel con TODAS las notas operativas para que la auxiliar sepa exactamente qué causar, qué reversar y qué registrar (documento, tercero, fecha, base, IVA/retención, cuenta y acción), más las decisiones que quedan del titular. Ejemplo aplicado: `TRABAJOS/COMERCIO DE BICICLETAS A/IVA CUAT2/CUAT 2 COMPLETO/FORMATO 300 IVA CUAT 2-2026 COMERCIO DE BICICLETAS A BORRADOR.html` (secciones A causar / B reversar / C notas crédito / D decisiones).

Relacionado: *(nota interna de la firma)*, *(nota interna de la firma)*.

**Segundo refuerzo (2026-09-15, EXPORTADORA DE SERVICIOS B IVA bim 4 + RTFT ago):** volví a entregar una versión "resumida" (solo los renglones con valor, diseño propio) y el titular la rechazó: **"el formato DIAN debe ser 100% igual al original, no una versión resumida"**. Resumida = mostrar solo las casillas con cifra. Correcto = TODAS las casillas del formulario aunque vayan en cero (el 300 tiene 68: 27-93 y 100; el 350 tiene 110: 29-138 con las dos columnas PJ/PN), más cabecera numerada (1, 3, 4, 5-12, 24-28), rótulos verticales de sección, anticipos SIMPLE (300) y el pie completo (101/139, 102/140, 981, 982, 983, 994, 997, 980, 996). La casilla 26 "No. Formulario anterior" va VACÍA salvo corrección (no poner ahí el formulario del período anterior). Generador reutilizable que ya cumple, GUARDADO EN EL VAULT: `Asesorias Contables FYT/herramientas/formularios_dian.py` — `render_300(F, meta, out, notas_html)` y `render_350(G, meta, out, notas_html)`, F/G = dict {casilla: valor}, meta = nit/dv/razon/anio/periodo/periodicidad/actividad. Usarlo SIEMPRE para IVA y retención de cualquier cliente; verificar con Edge headless (`msedge --headless=new --screenshot`) porque el panel del navegador no captura archivos locales. Las notas/observaciones van DEBAJO del formulario, nunca dentro.

**Tercer refuerzo (2026-09-15, CONSTRUCTORA AA agosto):** el titular volvió a recordar la regla ('cada vez que se liquide un impuesto se debe generar el formato HTML exactamente igual a la DIAN') porque el 350/300 de CONSTRUCTORA AA salieron con diseño propio y cajas de notas alrededor. Se rehicieron con `formularios_dian.py` del vault y las notas quedaron en un bloque DEBAJO del formulario. Referencia visual para el 350: el de julio 2026 de CONSTRUCTORA AA presentado (`2026/07- Julio/3510693746506.pdf`).

**Cuarto refuerzo (2026-10-13, COMERCIO DE BICICLETAS A RTFT septiembre): VOLVI A HACERLO MAL.** Entregue otra vez una version resumida con diseno propio (solo los renglones con cifra, cajas de notas alrededor del formulario) y el titular tuvo que recordarmelo: «recuerda generar el formulario 350, como debe ser presentado». Van cuatro veces.
**REGLA OPERATIVA, sin excepcion: NUNCA escribir un formulario de impuestos a mano.** Lo primero al liquidar cualquier impuesto es agregar al sys.path la carpeta `C:\Users\juan-\Desktop\Juan Manuel\Asesorias Contables FYT\herramientas` y hacer `from formularios_dian import render_300, render_350`. Se arma el dict de casillas, se pasan `meta` y `notas_html`, y se verifica con Edge headless. Si el entregable no salio de ese generador, esta mal.
- `render_350(G, meta, out, notas_html, pago_total)` con G = {casilla: valor}, casillas 29..138.
- Mapeo que uso COMERCIO DE BICICLETAS A: 32/45 rendimientos financieros PJ - 36/49 compras PJ - 83/99 arrendamientos PN - 59/68 autorretencion art. 114-1 - 130/136/138 totales.
- Cada casilla va aproximada al multiplo de mil mas cercano (art. 577 E.T.), y la suma de las casillas redondeadas debe dar el renglon 130: verificarlo con un assert.
- Captura: `msedge --headless=new --disable-gpu --hide-scrollbars --window-size=1000,2600 --screenshot=out.png "file:///C:/..."`. Construir la URL con `cygpath -m`, nunca con `sed` sobre las barras invertidas.
- Dato que no se pueda tomar de un formulario presentado (p. ej. la casilla 12 Cod. Direccion seccional) va EN BLANCO y se avisa al pie; no se inventa.
