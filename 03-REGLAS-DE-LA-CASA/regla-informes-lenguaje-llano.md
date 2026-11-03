---
name: regla-informes-lenguaje-llano
description: "REGLA: los informes para gerencia van en lenguaje llano, con pasos numerados (quién lo hace / para cuándo) y glosario al final"
metadata:
  type: feedback
---

Los informes que ve la gerencia de los clientes van **en lenguaje de calle**, no en lenguaje contable. El titular lo pidió dos veces (06-oct y 16-oct-2026) para las empresas de la gerente del salón I: *"que la persona así no tenga conocimiento lo lea y sepa exactamente qué debe hacer para organizar los faltantes"*.

**Why:** quien recibe el informe no es contador. Un informe que la gerente no entiende no produce ninguna acción, y el trabajo se pierde.

**How to apply:** tres cosas, además de la [[regla-marca-ritore-informes]]:
1. **Abrir explicando de qué se trata**, incluso lo obvio ("vender y facturar no son lo mismo"; "la nómina electrónica no es pagar, es avisarle a la DIAN"). Y un bloque `.resum` (fondo negro, texto en oro) con la conclusión en dos frases.
2. **Cerrar con `<ol class="pasos">`**: pasos numerados, cada uno con título en negrita, qué hay que hacer, y un chip `<span class="q">` que dice **quién lo hace y para cuándo**. Ordenados por dependencia, no por importancia: el paso 1 es el que destraba los demás.
3. **Glosario `<div class="glos">` al final** con las palabras técnicas que no se pudieron evitar (IVA, nota crédito, token, consumidor final, quedar a favor…).

Traducciones que ya quedaron probadas: *IVA descontable* → "el IVA que pagamos al comprar" · *saldo a favor* → "la DIAN quedaría debiéndonos" · *nota crédito* → "el documento que borra una factura" · *régimen SIMPLE* → "un sistema especial de impuestos en el que no cobra IVA" · *parametrización del facturador* → "la configuración del programa de facturación" · *abuso tributario (art. 869)* → "la DIAN lo ve como una maniobra para no pagar el impuesto". Los artículos del E.T. y los tecnicismos van solo en el pie del documento. Scripts: `simple_nomina.py`, `simple_sepoct.py`, `simple_jl.py` (todos reutilizan el cálculo del script original partiéndolo en el marcador `# ===== HTML`).
