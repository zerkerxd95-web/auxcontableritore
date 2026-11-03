---
name: regla-cruce-token-obligatorio
description: REGLA de retención en la fuente — nunca liquidar solo con contabilidad; el token DIAN es fuente de verdad; cuantía mínima por OPERACIÓN DIARIA por proveedor (nunca acumulada por mes); el Excel de diferencias es para ajustar contabilidad.
metadata: 
  node_type: memory
  type: feedback
---

Al liquidar retención en la fuente (Formulario 350) de cualquier empresa: **el token DIAN nunca se deja de lado**. La liquidación se hace con el cruce completo token ↔ contabilidad, no solo con contabilidad.

**Why:** El 2026-07-08 liquidé COMERCIO DE BICICLETAS A e INVERSIONES N solo con las retenciones contabilizadas y el titular rechazó ambos informes: el 350 debe salir con TODAS las retenciones correctas (token + contabilidad) y el Excel de diferencias es para AJUSTAR la contabilidad. Luego precisó el criterio de cuantía: él NO consolida por mes por proveedor — consolida **por operación diaria**: si las facturas del mismo proveedor del mismo día superan la base, retiene; si no, no, aunque la suma del mes cumpla la base. La retención se reconoce factura por factura (o grupo del día) siempre que cumpla la base.

**How to apply:**
1. El 350 incluye toda factura del token que cumpla la base de retención, esté o no causada en contabilidad; la factura sin causar es además hallazgo contable con asiento propuesto en el Excel.
2. Cuantía mínima **por operación diaria por proveedor**: sumar facturas del mismo NIT y mismo día de emisión; si el día supera la cuantía (2026: compras 27 UVT $1.414.098, servicios 4 UVT $209.496), se retiene sobre las facturas de ese día. NUNCA acumular por mes.
3. Retención ya practicada sobre factura bajo cuantía: se declara y consigna igual (ya se descontó al proveedor); a futuro no practicarla.
4. La autorretención se liquida sobre el total de ingresos gravados: el mayor entre token e ingresos contables, conciliando la diferencia.
5. El Excel de diferencias = ajustes contables a registrar ANTES de presentar (asientos DB/CR propuestos) + hoja "REGLA TOKEN".
6. **Cuantía POR FACTURA (no por día) cuando el titular lo indique:** lo decidió para INVERSIONES N (sep-2026) y para CONSTRUCTORA AA (15-sep-2026: "la retención calcúlala por factura, no por día"). Para esos clientes cada factura se compara sola con la base; preguntar el criterio en clientes nuevos.
7. Verificar SIEMPRE que las retenciones liquidadas estén iguales en el software contable del cliente (cruce documento a documento, hoja 'Cruce software').
8. Excepciones vigentes: financieras/autorretenedores designados, servicios públicos domiciliarios, tarifa PN según RUT (sin RUT → no declarante, tarifa mayor).

Aplicada en *(nota interna de la firma)* (V1 aceptada — ya cumplía el criterio diario), *(nota interna de la firma)* ($1.559.000) e *(nota interna de la firma)* ($1.748.000). Aplica a todo cliente futuro.

9. **El cruce es documento por documento, nunca por el agregado.** (COMERCIO DE BICICLETAS A septiembre 2026, el titular preguntó «¿verificaste que todas las facturas del token sí estén contabilizadas?» y yo solo había cuadrado el total de las emitidas.) Que la base agregada coincida al peso no prueba nada: dos errores que se compensan dan el mismo total. Cruzar por folio en los dos sentidos (token→libros y libros→token), verificar que la serie de facturación no tenga huecos, y contrastar valor e IVA de cada folio. Dos trampas: (a) usar tolerancia de ±$2 marca como "sin causar" documentos que solo tienen redondeo — usar ±$200 y reportar aparte las diferencias pequeñas; (b) restringir la prueba a las cuentas "típicas" (4135/4175/4180) deja fuera ingresos que van a otras cuentas, como el arriendo en la 4220, y produce falsos positivos enormes.
