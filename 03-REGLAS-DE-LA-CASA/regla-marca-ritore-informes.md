---
name: regla-marca-ritore-informes
description: "REGLA: todo informe HTML de la firma va con la identidad Ritoré (oro #f0bb25 / tinta #231f20 / blanco + logo); hay módulo reutilizable"
metadata:
  type: feedback
---

Todo informe en HTML que salga de la firma lleva la **identidad Ritoré**: oro `#f0bb25`, tinta `#231f20`, blanco, y el logo del membrete en el header negro (placa blanca, 58 mm). El titular lo pidió el 16-oct-2026 para el informe de octubre y enseguida para los anteriores de la misma tanda, así que **no hay que esperar a que lo pida**: se aplica de entrada.

**Why:** los informes se los entregan a los clientes y deben verse como documento de la firma, no como una salida genérica.

**How to apply:** usar `marca_ritore.py` del scratchpad — expone `CSS`, `IMG` (logo en base64) y `rebrand(path)`, que cambia la hoja de estilos, mete el logo en el `<header>`, pinta en oro la última palabra del `<h1>` y convierte los emojis de los `<h2>` en círculos dorados numerados. El logo sale de `Asesorias Contables FYT/Rentas PERSONA NATURAL/membrete.docx` → `word/media/image1.png` (ver *hoja-membrete-ritore*). El CSS cubre tanto las clases nuevas (`.card.alerta`, `h2 .n`) como las viejas (`.card.rojo/.verde/.amar`, `.nota.roja/.azul`, `.ok/.falta/.tarde`), así que sirve para rebrandear informes ya escritos sin tocar el cuerpo.
