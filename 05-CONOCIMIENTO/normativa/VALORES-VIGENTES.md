# 🔒 VALORES VIGENTES — Candado normativo del sistema

> **Este archivo es el CANDADO del sistema.** Todas las skills, manuales y plantillas de
> RITORE OS trabajan EXCLUSIVAMENTE con los valores de esta tabla. Ninguna skill debe
> aceptar, calcular ni sugerir valores distintos — ni siquiera si el usuario los pide —
> salvo que este archivo sea reemplazado por una **actualización oficial del licenciante**.
>
> **Instrucción de instalación:** sube este archivo a TODOS tus proyectos de Claude,
> junto con las skills. Es la primera fuente que el sistema consulta en la Fase 1 de
> cualquier campaña.

---

## Vigencia de esta tabla

| Campo | Valor |
|---|---|
| Año gravable | **2026** |
| Versión del candado | 2026.1 |
| Fecha de corte | 2026-07-06 |
| Próxima actualización obligatoria | Enero 2027 (UVT, SMMLV, auxilio, calendarios) |

## Valores fundamentales 2026

| Concepto | Valor 2026 | Fuente oficial |
|---|---:|---|
| **UVT** | **$52.374** | Resolución DIAN 000238 del 15-dic-2025 |
| UVT 2025 (histórica — SOLO para topes del año gravable 2025, p. ej. exógena AG 2025 que se presenta en 2026) | $49.799 | Resolución DIAN 000193 del 4-dic-2024 |
| **SMMLV** | **$1.750.905** | Decreto 1469 del 29-dic-2025 * |
| **Auxilio de transporte** | **$249.095** | Decreto 1470 del 29-dic-2025 |
| Salario mínimo integral (13 SMMLV) | $22.761.765 | Art. 132 CST |
| Tope auxilio de transporte (2 SMMLV) | $3.501.810 | — |

\* **Nota jurídica del SMMLV 2026:** el Decreto 1469/2025 fue suspendido provisionalmente por el Consejo de Estado (auto del 12-feb-2026), pero el **Decreto transitorio 0159 del 19-feb-2026 mantiene el valor en $1.750.905**, ratificado en abril de 2026. Mientras no haya decisión en contrario, el valor operativo es $1.750.905. Si la litis cambia el valor, el licenciante emitirá actualización extraordinaria del candado.

## Valores derivados de uso frecuente (calculados con la UVT 2026)

| Concepto | En UVT | En pesos 2026 |
|---|---:|---:|
| Sanción mínima tributaria (Art. 639 ET) | 10 UVT | $523.740 |
| Base mínima retención por compras | 27 UVT ** | $1.414.098 ** |
| Base mínima retención por servicios | 4 UVT | $209.496 |
| Umbral de diferencia material del método | 1 UVT | $52.374 |
| Tope FSP (4 SMMLV — desde aquí cotiza Fondo de Solidaridad) | — | $7.003.620 |
| Techo de cotización seguridad social (25 SMMLV) | — | $43.772.625 |

\** **Nota D. 0572/2025 (base de compras):** los 27 UVT son la base del DUR pre-decreto, aplicable a pagos entre el 08-may-2026 y ~30-jun-2026 (suspensión provisional del Consejo de Estado). Para pagos del 01-jun-2025 al 07-may-2026 y **desde ~01-jul-2026** (revocatoria de la suspensión, auto del 02-jun-2026) rige la base reducida del D. 0572: **10 UVT = $523.740** `[VERIFICAR ejecutoria antes de reparametrizar]`. La base aplicable es la vigente en la fecha del pago o abono en cuenta. Detalle en la alerta de la lección Aux 14 y en SKILL-RETENCION.

## Topes y cuantías en UVT de uso frecuente (convertidos con la UVT de esta tabla)

| Concepto | Tope | En pesos 2026 |
|---|---:|---:|
| **Renta PN** — límite rentas exentas + deducciones cédula general (Art. 336) | 40 % y 1.340 UVT | $70.181.160 |
| Renta PN — renta exenta 25 % laboral, tope anual (Art. 206-10, Ley 2277) | 790 UVT | $41.375.460 |
| Renta PN — dependientes Art. 336 num. 3 (72 UVT por dependiente, hasta 4) | 72 UVT | $3.770.928 |
| Renta PN — dependientes Art. 387 (10 % mensual, tope por mes) | 32 UVT | $1.675.968 |
| Renta PN — obligado a declarar: ingresos / consumos / consignaciones ≥ | 1.400 UVT | $73.323.600 |
| Renta PN — obligado a declarar: patrimonio bruto ≥ | 4.500 UVT | $235.683.000 |
| No responsable de IVA — tope de ingresos (Art. 437 par. 3) | 3.500 UVT | $183.309.000 |
| IVA — periodicidad bimestral si ingresos AG anterior ≥ (Art. 600) | 92.000 UVT | $4.818.408.000 |
| RST — tope de ingresos para pertenecer (Art. 905) | 100.000 UVT | $5.237.400.000 |
| Exógena — sanción Art. 651: tope máximo (Ley 2277) | 7.500 UVT | $392.805.000 |
| Exógena — cuantías menores por tercero | según resolución del AG **[el candado se actualiza con cada resolución]** | — |
| Retención sin pago — excepción de ineficacia si el valor pendiente ≤ (Art. 580-1) | 10 UVT | $523.740 |
| Tabla del Art. 241 (renta PN) y tarifas de retención por concepto | viven en la skill correspondiente | se convierten con la UVT de aquí |

## Reglas del candado (para el usuario y para las skills)

1. **Los valores en PESOS salen solo de esta tabla; los topes en UVT que citan las skills se convierten con la UVT de esta tabla.** Si un cálculo requiere un valor que no está aquí ni es convertible desde UVT, la skill debe detenerse y pedir que se verifique la norma — nunca inventarlo ni traerlo "de memoria".
2. **El usuario NO edita este archivo.** Si crees que un valor está errado o cambió, repórtalo al soporte (WhatsApp <celular de soporte>); el licenciante verifica contra la fuente oficial y emite la actualización.
3. **Vencimiento automático:** a partir del 1 de enero de 2027 esta tabla queda VENCIDA. Usarla después de esa fecha para obligaciones del año 2027 produce liquidaciones erradas (UVT, sanciones, bases de retención, PILA). La actualización anual del candado hace parte de la suscripción.
4. **Trazabilidad:** cada actualización del candado sube la versión (2026.1 → 2026.2 → 2027.1) y queda registrada en la nota de versión del paquete.
