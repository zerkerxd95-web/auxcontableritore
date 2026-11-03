---
name: regla-cierre-retencion-mensual
description: "REGLA del titular - el cierre de la retención en la fuente se hace mes por mes contra cada F-350, nunca en un ajuste global del período."
metadata:
  node_type: memory
  type: feedback
---

El cierre contable de la retención en la fuente se registra **mes por mes, un asiento contra cada F-350**, nunca con un solo ajuste acumulado al cierre del período. Cada mes: las subcuentas de retención (2365xx) quedan en **cero** y la cuenta de cierre recibe **únicamente el valor declarado en el renglón 138 de ese mes**, que el pago del mes siguiente vuelve a dejar en cero.

**Why:** un ajuste global deja la cuenta de cierre inservible como control. Mes a mes la cuenta refleja en todo momento solo lo que se le debe a la DIAN por el mes en curso, y cualquier descuadre salta en el mes exacto en que se produjo en vez de quedar enterrado en un neto del semestre. Instrucción del titular el 11-oct-2026 sobre *(nota interna de la firma)*, donde yo había propuesto un único asiento global por $11.567.000.

**How to apply:**
- Un asiento por mes, fechado el último día del mes, con el número del formulario en el concepto.
- Débito a cada subcuenta por lo **causado en libros** (créditos netos de débitos de ese mes), crédito a la cuenta de cierre por lo **declarado**.
- La diferencia es el redondeo a miles de la declaración y se cancela contra `429581 AJUSTE AL PESO` (o la cuenta de ajuste que exista en el plan). En EXPORTADORA DE SERVICIOS B el neto del semestre fue $1.076 de débito.
- Una retención practicada y **no declarada** no es redondeo: se acredita a la cuenta del proveedor dentro del asiento de su propio mes, sobre todo si la base no alcanzaba la cuantía mínima (entonces la retención fue indebida y el dinero es del proveedor).
- Verificar siempre con un papel de trabajo que simule el saldo de la cuenta de cierre movimiento por movimiento: debe dar **cero después de cada pago** y quedar al corte solo con el mes pendiente.

Ver [[regla-cruce-token-obligatorio]] y la regla hermana del IVA en *(nota interna de la firma)* (el 2408 se cierra contra la declaración y el saldo a favor va al activo).
