---
tipo: manual
tags: [ritore, auxiliar, impuestos, retencion, iva, reteica, simple]
estado: vigente
version: 1.0
fecha: 2026-11-03
---

# 07 · Impuestos que prepara el auxiliar

> El auxiliar **prepara borradores**; el contador **revisa, firma y presenta**. Un borrador bien hecho es el que el contador puede transcribir al formulario de la DIAN sin recalcular nada.

## 1. Qué prepara y cuándo

| Obligación | Periodicidad | Qué entrega el auxiliar | Dónde |
|---|---|---|---|
| Retención en la fuente F-350 | Mensual | Base y retención por concepto (PJ y PN), autorretención, ReteIVA, conciliado contra 2365 y contra el token | `04_CUADRE_IMPUESTOS` + borrador en `03-SALIDA/` |
| IVA F-300 | Bimestral o cuatrimestral (según la ficha; **nunca se asume**) | Generado y descontable por tarifa, devoluciones, prorrateo si aplica, por movimientos del período | ídem |
| ReteICA | Según el municipio (mensual o bimestral) | Base y retención por actividad; se presenta aunque dé cero si el municipio lo exige | ídem |
| Anticipo SIMPLE F-2593 | Bimestral (clientes del régimen SIMPLE) | Ingresos por grupo de actividad, tarifa, descuentos por pensión a cargo del empleador, componente ICA | ídem |
| Certificados de retención | Anual (marzo) y a solicitud | Certificado por proveedor desde la 2365 por tercero | `03-SALIDA/` del mes de expedición |

Fuentes del procedimiento completo: los protocolos en `05-CONOCIMIENTO/tecnico/` (F-350, F-300, F-2593 y el protocolo de elaboración de impuestos) y las skills del contador en `05-CONOCIMIENTO/skills-del-contador/`.

## 2. Reglas para el borrador del F-350

1. **Token completo.** El F-350 incluye toda factura del token que cumpla la base, esté o no causada.
2. **Cuantía mínima** según la ficha del cliente: por operación diaria por proveedor (regla general) o por factura (si el contador lo fijó para ese cliente). Nunca acumulada por mes.
3. Retención ya practicada sobre una factura bajo la cuantía: se declara igual (ya se le descontó al proveedor).
4. **Autorretención** sobre el mayor entre ingresos del token e ingresos contables, con la diferencia conciliada.
5. **Persona natural de servicios**: art. 383 antes del 6 %/4 %.
6. Después de presentar: un asiento de cierre de la 2365 por cada F-350, contra el pago.

## 3. Reglas para el borrador del F-300

1. Periodicidad confirmada en la ficha (RUT e ingresos del año anterior).
2. IVA generado y descontable **por movimientos del período**, nunca por saldo acumulado de la 2408.
3. IVA descontable solo de facturas del token a nombre del cliente y relacionadas con su actividad; los criterios particulares (por ejemplo, IVA al gasto en compras menores) salen de la ficha.
4. Si el cliente tiene ingresos gravados y excluidos a la vez, el contador decide el prorrateo; el auxiliar deja los datos para calcularlo.
5. Saldo a favor del período anterior y retenciones de IVA que le practicaron, cruzados contra el formulario anterior y el token.

## 4. Formato del borrador

Si la firma usa el repositorio del contador, el borrador se genera con sus **Formatos de Salida** (HTML idéntico al formulario DIAN, con todas las casillas y las notas operativas debajo). Si no, se entrega en la plantilla Excel `13_Liquidador_Retencion_F350.xlsx` o `12_Liquidador_IVA_F300.xlsx` de `07-PLANTILLAS-EXCEL/`. En los dos casos, cada casilla con valor debe poder rastrearse a una hoja de `04_CUADRE_IMPUESTOS`.

Debajo del borrador van **siempre** las notas operativas: qué asientos hay que digitar para que libros y formulario cuadren, qué quedó pendiente y cuándo vence.

## 5. Lo que el auxiliar no decide

Correcciones de declaraciones ya presentadas, sanciones e intereses, saldos a favor y su devolución, cambios de periodicidad, prorrateo, tratamientos de zona gris. Todo eso se anota como **decisión del contador** en `ENTREGA.md`.

## Relacionado

- [[Aux 14 - Calculo de Retenciones]] · [[Aux 15 - IVA y Prorrateo]] · [[Protocolo Retencion en la Fuente F-350]] · [[Protocolo IVA Formulario 300]] · [[Protocolo Anticipo Simple F-2593]]
- [[regla-cruce-token-obligatorio]] · [[regla-cierre-retencion-mensual]] · [[regla-retencion-pn-art-383]] · [[politica-html-formato-dian]]
