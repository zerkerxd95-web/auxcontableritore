# Ficha de cliente — COMERCIALIZADORA EJEMPLO SAS (cliente FICTICIO de práctica)

> ⚠️ Este cliente NO existe. NIT y cifras son inventados. Úsalo para tu primera corrida
> del sistema antes de trabajar con clientes reales. Copia esta ficha como plantilla
> (`_FICHA-CLIENTE.md`) para cada cliente real tuyo.

## Datos básicos

| Campo | Valor |
|---|---|
| Razón social | COMERCIALIZADORA EJEMPLO SAS |
| NIT | 900.123.456-8 *(ficticio)* |
| Régimen | Ordinario — responsable de IVA |
| Actividad (CIIU) | 4645 — Comercio al por mayor de productos de aseo |
| Municipio sede | Medellín (ICA Medellín) |
| Software contable | Genérico (exporta balance de prueba, auxiliar y balance por tercero a Excel) |
| Empleados | 8 |
| Contacto que envía insumos | Auxiliar administrativa (correo, primeros 3 días del mes) |

## Obligaciones y periodicidades

| Obligación | Periodicidad | Nota |
|---|---|---|
| Retención en la fuente (F-350) | Mensual | Agente de retención por compras y servicios |
| IVA (F-300) | Bimestral | Verificar periodicidad cada año contra ingresos |
| ReteICA Medellín | Bimestral | — |
| ICA anual Medellín | Anual | — |
| Exógena nacional | Anual | Formatos: 1001, 1003, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 2276 |
| Renta PJ (F-110 + 2516) | Anual | — |
| EEFF + informe gerencial | Mensual | Entrega el día 10 |

## Criterios particulares (con fecha y origen — así se documentan)

| Criterio | Origen | Fecha | Vigente |
|---|---|---|---|
| El IVA de compras menores a $200.000 se lleva como mayor valor del gasto (no se solicita descontable) | Política definida con el gerente | 2026-01-15 | Sí |
| Los terceros con doble NIT se consolidan en el NIT del RUT más reciente | Acuerdo con el contador anterior | 2026-01-15 | Sí |
| Las cuentas de socios (28xx) se revisan con el gerente antes de cualquier cierre | Antecedente de préstamos sin formalizar | 2026-02-08 | Sí |

## Antecedentes / vigilancia

- Sanción de ReteICA por período en $0 no presentado (año anterior a la vinculación). **Vigilancia reforzada:** verificar TODOS los bimestres que ReteICA se presente aunque dé cero.

## Pendientes vivos

- [ ] Formalizar el préstamo del socio mayoritario (documento + intereses) antes del cierre anual.
- [ ] Depurar 3 terceros con nombre "VARIOS" en el auxiliar (herencia del contador anterior).

---

## Ejercicio de práctica sugerido (tu primera corrida)

1. Abre el proyecto "Impuestos del mes" en Claude.
2. Dile: *"Vamos a simular el cierre de enero de COMERCIALIZADORA EJEMPLO SAS (usa la ficha adjunta). Guíame fase por fase por el bucle: qué insumos me pedirías, qué validarías, qué liquidarías y qué me entregarías."*
3. Claude te recorrerá el método completo sin datos reales. Cuando el flujo te sea familiar, repite con tu cliente real más simple.
