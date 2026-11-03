---
tipo: proceso
tags: [ritore, auxiliar, calendario, cierre]
estado: vigente
version: 1.0
fecha: 2026-11-03
---

# 02 · Calendario de cierre mensual

> **Por qué hay calendario.** La retención en la fuente (F-350) vence todos los meses entre el **día hábil 8 y el 22** del mes siguiente según el último dígito del NIT del cliente, y el IVA y el anticipo SIMPLE caen en la misma ventana cuando cierra el período. El contador necesita la entrega con tiempo para revisar, pedir correcciones y presentar **con dos días hábiles de margen**. El calendario se cuenta en **días hábiles del mes siguiente** al período que se cierra.

`[VERIFICAR]` cada enero las fechas exactas de vencimiento por dígito en el calendario tributario oficial del año (DIAN) y en el calendario de cada municipio para ReteICA. Se registran en la plantilla `29_Control_Maestro_de_Obligaciones.xlsx`.

## La semana de cierre

| Día hábil | Qué hace el auxiliar | Resultado que debe existir |
|---|---|---|
| **Último día hábil del mes que cierra** | Envía al cliente la solicitud de insumos (plantilla `SOLICITUD-DE-INSUMOS.md`) | Correo o mensaje enviado, con lista concreta |
| **1–2** | Descarga el **token DIAN** (emitidos y recibidos) y los **extractos** de todas las cuentas y pasarelas; recibe novedades de nómina y soportes; archiva todo en `01-INSUMOS/` | `01-INSUMOS/` completo o pendientes anotados |
| **3** | **Causa el token completo**: facturas de venta, compras, notas, documento soporte; causa los soportes no electrónicos | Cruce token preliminar sin facturas sin causar |
| **4** | **Nómina** causada con provisiones; **depreciaciones** y amortizaciones; **conciliaciones bancarias** y de pasarelas | `02_CONCILIACIONES` con diferencia cero |
| **5** | **Cartera y proveedores** (cruces 1-a-N); **cuadre de impuestos**: 2365 vs borrador F-350 por concepto; 2408 vs F-300 si cierra; ReteICA; autorretención | `03_` y `04_` terminados; borradores en `03-SALIDA/` |
| **6** | **Balance de prueba revisado**; asientos propuestos; `ENTREGA.md`; corre `revisar_entrega.py` | **Entrega al contador** |
| **7–8** | El contador revisa (cuatro ojos) y escribe observaciones; el auxiliar corrige en el software y re-exporta | Observaciones cerradas en `04-TRAZAS/` |
| **≥ 2 días hábiles antes del vencimiento** | El contador presenta y paga | Acuse y recibo 490 en `03-SALIDA/` |
| **10** (si se pactó) | Estados financieros mensuales e informe al cliente | Entregados |

### Si el vencimiento del cliente cae temprano (dígitos con vencimiento el día 8 o 9)

La entrega se adelanta: **día hábil 4** como máximo. Para lograrlo, ese cliente se cierra primero en la semana y la solicitud de insumos sale dos días antes del fin de mes.

### Si el cliente no envía insumos

1. Día hábil 2: recordatorio con la lista exacta de lo que falta.
2. Día hábil 3: segundo y último recordatorio; se anota en `NOTAS-Y-PENDIENTES.md`.
3. Día hábil 4: se escala al contador, que decide si se presenta con la información disponible. Esa decisión **la toma y la firma el contador**, nunca el auxiliar, y queda escrita en `04-TRAZAS/`.

## Orden obligatorio dentro del cierre

El orden importa: cada paso usa el resultado del anterior. Saltárselo produce el error más caro del cierre, liquidar un impuesto antes de tener causado todo el token.

```
TOKEN causado  →  NÓMINA y provisiones  →  DEPRECIACIONES  →  BANCOS y pasarelas
      →  CARTERA y PROVEEDORES  →  IMPUESTOS  →  TERCEROS depurados  →  BALANCE revisado  →  ENTREGA
```

## Calendario anual que el auxiliar debe tener presente

| Mes | Qué se suma al cierre mensual |
|---|---|
| Enero | Cierre del año anterior (traslado del resultado, ver Aux 25); certificados de retención a proveedores (marzo) se empiezan a preparar |
| Febrero–marzo | Certificados de ingresos y retenciones F-220 de empleados; información para la exógena |
| Abril–junio | Exógena nacional y municipal; renta de personas jurídicas (apoyo con papeles de trabajo) |
| Julio | Cambios de tarifas o recargos que entran en julio (verificar cada año) |
| Agosto–octubre | Renta de personas naturales (apoyo con exógena de terceros y certificados) |
| Diciembre | Consolidación de nómina, cesantías (se consignan en febrero), inventario físico de cierre |

## Relacionado

- [[01 - Estandar de Entrega al Contador]] · [[03 - Checklist de Cierre Mensual]] · [[Plantilla 29 - Control Maestro de Obligaciones]]
- [[Aux 24 - Cierre Contable Mensual]] · [[Aux 25 - Cierre Anual y Errores Comunes]]

## Historial de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-11-03 | Versión inicial |
