---
name: regla-conciliacion-cruces-1-a-n
description: "REGLA de conciliación bancaria — agotar cruces uno-a-varios (subset-sum) antes de reportar faltantes; las facturas suelen estar contabilizadas y los ajustes son de reclasificación, no de registro."
metadata: 
  node_type: memory
  type: feedback
---

En toda conciliación bancaria: antes de reportar cualquier "faltante" o "sobrante", agotar los cruces uno-a-varios y varios-a-uno entre banco y libro. Confirmado por el titular el 2026-07-14 ("exactamente, así funciona").

**Why:** En la conciliación de un cliente de servicios se reportaron como faltantes pagos que en realidad cruzaban en combinación: un retiro de efectivo del representante legal paga varios egresos; un solo ce del libro cruza contra varias salidas del banco (un egreso a un proveedor = 3 transferencias nominadas + 2 retiros, suma exacta al peso); un ce de "reembolso" puede ser parte del pago de otro concepto; los reembolsos cruzan retiros encadenados incluso entre meses. Las facturas casi siempre ESTÁN contabilizadas — lo que genera diferencia es el crédito acreditado a otra cuenta (caja vs banco) o valores parciales.

**How to apply:**
1. Cruce en capas: (a) 1:1 exacto por valor y fecha ±6 días; (b) bloques por categoría (nómina quincenal individual↔ce, GMF diario↔NC mensual, consignaciones múltiples↔un rc); (c) subset-sum sobre los residuales: combinaciones de movimientos del banco que sumen un registro del libro y viceversa, incluso cruzando meses.
2. Solo lo que sobrevive a las 3 capas es diferencia real, y el ajuste típico es RECLASIFICACIÓN (caja↔banco, corregir valor del ce) o reversión de notas sin soporte — no registrar facturas "faltantes".
3. Verificación obligatoria: la suma de diferencias reales debe igualar la diferencia de saldos al centavo; si no cierra, faltan cruces.
4. Presentar en el informe: hoja de cruces confirmados (sin ajuste) separada de las diferencias reales (con asiento propuesto) y comprobación libro ajustado = extracto.

Aplicada en *(nota interna de la firma)*. Complementa [[regla-cruce-token-obligatorio]] (retención) — mismo espíritu: cruzar todo antes de concluir.
