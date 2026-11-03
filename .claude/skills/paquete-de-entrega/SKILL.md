---
name: paquete-de-entrega
description: Arma y verifica el paquete de entrega de un período al contador (ENTREGA.md, semáforo de ocho áreas, asientos propuestos, borradores, trazas) y corre revisar_entrega.py. Úsala con "prepara la entrega", "¿está listo para el contador?", "revisa la carpeta de [período]".
---

# Paquete de entrega

1. `python herramientas/revisar_entrega.py "<RUTA>/<CLIENTE>/<AAAA-MM>"` → corrige todo lo rojo.
2. Pide al agente `revisor-de-entrega` la revisión de cuatro ojos.
3. Diligencia `ENTREGA.md`:
   - §1 un solo color por área (🟢 / 🟡 / 🔴) con su evidencia y comentario.
   - §2 cifras clave token vs libros con diferencia (salen de los papeles, no se digitan aparte).
   - §3 decisiones para el contador: qué, opción recomendada, efecto en pesos.
   - §4 lo que falta del cliente con valor, fecha de pedido y fecha límite.
   - §5 archivos de la entrega y resultado de `revisar_entrega.py`.
4. Vuelve a correr `revisar_entrega.py` (código 0, o 1 con los ámbar explicados).
5. Mensaje al contador, una línea:
   `Entrega <CLIENTE> <AAAA-MM> lista · semáforo: <verde/ámbar/rojo> · <n> decisiones para ti · vence <fecha>`.
6. Cuando vuelvan las observaciones (`04-TRAZAS/OBSERVACIONES-DEL-CONTADOR.md`): se corrige en el software contable,
   se re-exporta y se rehace lo afectado; las versiones viejas van a `04-TRAZAS/anteriores/`. Nada de sufijos v2 o final.

Detalle: `02-MANUAL-DE-ENTREGA/01 - Estandar de Entrega al Contador.md` y `09 - Pendientes Hallazgos y Comunicacion.md`.
