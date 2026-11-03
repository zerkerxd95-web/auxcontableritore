---
name: cierre-mensual
description: Cierre mensual completo de un cliente con el método RITORÉ (ocho áreas, garantía de cierre, entrega al contador). Úsala cuando digan "cierra el mes de [cliente]", "haz el cierre de [mes]", "deja al día [cliente]" o "prepara la entrega de [período]".
---

# Cierre mensual (método RITORÉ)

**Resultado:** la carpeta `<CLIENTE>/<AAAA-MM>` lista para el contador, con `revisar_entrega.py` sin rojos.

1. **Preparar.** Ruta del período (si no existe: `python herramientas/nuevo_periodo.py RAIZ "CLIENTE" AAAA-MM --nit NIT`),
   ficha `_cliente.yaml`, observaciones del contador del mes anterior, pendientes heredados.
2. **Insumos.** Token, extractos de todas las cuentas de la ficha, balance de prueba, auxiliar, prenómina, soportes.
   Lo que falte → skill `solicitud-de-insumos`. Sin token o sin extracto, esa área queda 🔴 con fecha de reiteración.
3. **Validar el auxiliar:** `python herramientas/validar_auxiliar.py --libro 01-INSUMOS/AUX_… --nit-empresa NIT`.
4. **Área 1 · Token** → skill `cruce-token`.
5. **Área 2 · Bancos y pasarelas** → skill `conciliacion-bancaria`.
6. **Áreas 3-4 · Cartera y proveedores:** saldo por tercero = facturas abiertas; anticipos identificados; saldos
   contrarios explicados → `03_CARTERA_Y_PROVEEDORES_<AAAA-MM>.xlsx`.
7. **Área 5 · Impuestos:** cuadre de retenciones (toda factura del token con retención; art. 383 primero para PN;
   cuantía mínima por día y proveedor), IVA según la periodicidad de la ficha, autorretención, ReteICA →
   `04_CUADRE_IMPUESTOS_<AAAA-MM>.xlsx` y borradores en formato DIAN en `03-SALIDA/` (manual 07).
8. **Área 6 · Nómina** → agente `auxiliar-nomina`.
9. **Áreas 7-8 · Gastos, activos y balance:** depreciaciones, diferidos, costo de ventas, naturaleza de saldos, cuentas
   puente en cero, terceros sin genéricos → `06_BP_REVISADO_<AAAA-MM>.xlsx`.
10. **Ajustes:** todo lo que no se digita va a `ASIENTOS_PROPUESTOS_<AAAA-MM>.xlsx` (hoja `02 ASIENTOS`) con la prueba
    de que cada cuenta queda en su saldo correcto (garantía de cierre, `03-REGLAS-DE-LA-CASA/regla-auditoria-garantia-de-cierre.md`).
11. **Entregar** → skill `paquete-de-entrega`.

Reglas: no crear cuentas, no cambiar criterios, no inventar cifras, ajustes propuestos y no registrados, umbrales del
manual 01 §4, todo pendiente con valor, responsable y fecha.
