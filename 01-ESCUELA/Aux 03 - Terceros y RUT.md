---
tipo: leccion
tags: [ritore, escuela, auxiliar, terceros, rut]
modulo: 1
estado: vigente
fecha: 2026-06-08
---
# Aux 03 - Terceros y RUT

## Objetivo
El auxiliar sabrá leer un RUT, interpretar los códigos de responsabilidad de la casilla 53, deducir de ellos qué retenciones e impuestos aplican a cada tercero, calcular el dígito de verificación de un NIT y mantener el maestro de terceros depurado — la base de una exógena sana.

## Marco conceptual y normativo
- **RUT (Registro Único Tributario):** Art. 555-2 ET y Decreto 1625/2016. Es la "cédula tributaria" del tercero: identifica NIT, dirección, actividad económica (CIIU) y **responsabilidades** (casilla 53).
- **Códigos de responsabilidad vigentes más usados** (verificados jun-2026 — fuente: [DIAN](https://www.dian.gov.co/impuestos/personas/Paginas/Responsabilidades-y-Usuarios-Aduaneros.aspx), [Actualícese](https://actualicese.com/codigos-de-responsabilidades-tributarias-rut-casilla-53/)):

| Código | Responsabilidad | Qué implica para nosotros |
|---|---|---|
| 05 | Renta y complementarios — régimen ordinario | Declarante; se le practica retefuente normal |
| 07 | Retención en la fuente a título de renta | Es agente retenedor: nos retendrá al pagarnos |
| 09 | Retención en la fuente en IVA (reteIVA) | Practica reteIVA (15% del IVA) |
| 13 | Gran contribuyente (en factura aparece "O-13") | Calidad especial; suele ser autorretenedor — verificar resolución |
| 47 | Régimen Simple de Tributación (RST) | NO se le practica retefuente a título de renta (Art. 911 ET) |
| 48 | Responsable de IVA | Factura con IVA; su IVA es descontable para nosotros |
| 49 | No responsable de IVA | Factura sin IVA; posible documento soporte ([[Aux 10 - Documento Soporte a No Obligados]]) |

- **Por qué importa:** la combinación de responsabilidades del tercero **determina la retención aplicable** en cada pago (detalle de tarifas en [[Aux 14 - Calculo de Retenciones]]). Pagarle a un RST con retención, o no retenerle a un ordinario, son errores que luego revientan en el F-350 y en exógena.

## Paso a paso

### 1. Leer el RUT de un tercero nuevo
1. Pide el **RUT actualizado** (PDF oficial con fecha de generación reciente; no pantallazos).
2. Verifica: NIT + DV, razón social EXACTA, dirección, municipio, actividad CIIU, casilla 53.
3. Registra el tercero en el maestro con tipo de documento correcto (13 cédula, 31 NIT, 22 cédula extranjería, 41/42 documento extranjero, 43 solo para cuantías menores en exógena).
4. Anota las responsabilidades que afectan la operación (48/49, 47, 07, 13).

### 2. Calcular el dígito de verificación (DV)
Algoritmo oficial DIAN: a cada dígito del NIT, de **derecha a izquierda**, se le aplican los pesos `3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71`. Se suma, se toma módulo 11: si el residuo es 0 o 1, ese es el DV; si no, `DV = 11 − residuo`.

**Ejemplo verificable — NIT de la DIAN 800.197.268:**

| Dígito (der→izq) | 8 | 6 | 2 | 7 | 9 | 1 | 0 | 0 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| Peso | 3 | 7 | 13 | 17 | 19 | 23 | 29 | 37 | 41 |
| Producto | 24 | 42 | 26 | 119 | 171 | 23 | 0 | 0 | 328 |

Suma = 733 → 733 mod 11 = 7 → DV = 11 − 7 = **4** ✓ (la DIAN es 800.197.268-4).

Un NIT cuyo DV no valida es un NIT mal digitado: se corrige ANTES de seguir, nunca se reporta errado (*Subskill B5 - Depurar Terceros y Cuantias Menores*).

### 3. Depurar el maestro de terceros
1. Busca **duplicados** (mismo NIT con dos razones sociales, o misma empresa con NIT con y sin DV pegado).
2. Detecta **genéricos**: "CONSUMIDOR FINAL", "VARIOS", "CLIENTES NACIONALES", NIT 222222222 usado por fuera de la regla de cuantías menores.
3. Completa **dirección, municipio y país** — la exógena los exige en varios formatos.
4. Cruza contra el RUT: razón social contable = razón social RUT (los "alias" comerciales dañan los cruces DIAN).
5. Documenta los terceros corregidos para que el software del cliente también se actualice (si la contabilidad es de un tercero, se emite documento de observaciones como en **Cliente - EMPRESA H**).

### Asiento de ejemplo — el tercero importa tanto como la cifra
Compra de papelería $300.000 + IVA a PAPELERÍA EL CID SAS (NIT 901.111.222, responsable de IVA, régimen ordinario). Sin retención por estar bajo la base de compras (27 UVT = $1.414.098 en 2026):

| Cuenta | Nombre | Tercero | Débito | Crédito |
|---|---|---|---:|---:|
| 519530 | Útiles, papelería y fotocopias | 901111222 | 300.000 | |
| 240802 | IVA descontable | 901111222 | 57.000 | |
| 233595 | Costos y gastos por pagar | 901111222 | | 357.000 |

El mismo asiento con tercero "VARIOS" es contablemente "igual"… y tributariamente una bomba de tiempo: en el F-1001 ese pago no tendría beneficiario identificable.

## Errores comunes
- **Terceros genéricos en cuentas de movimiento:** lección real de **Cliente - EMPRESA H** — la contabilidad llegó de un tercero con saldos sin tercero depurado y hubo que sanear cuenta por cuenta (1105, 1305, 1355, 2335, 2805…) antes de poder construir la exógena. Un "CONSUMIDOR FINAL" en compras es inaceptable: las compras SIEMPRE tienen proveedor real.
- **Crear terceros sin RUT/NIT verificado:** regla absoluta de la firma — NUNCA. El DV se valida al crear, no al reportar.
- **No registrar la responsabilidad RST (47):** se le retiene indebidamente y toca devolver/corregir certificados.
- **Asumir que "no responsable de IVA" (49) = informal:** puede ser un prestador grande de servicios exentos/excluidos; igual exige soporte válido.
- **Mezclar el NIT con el DV en el campo de identificación** (9011112221 en vez de 901111222 + DV 1): duplica terceros y revienta el prevalidador.
- **Razón social "como la conocemos"** ("EL CID" en vez de "PAPELERIA EL CID SAS"): rompe los cruces de la DIAN, que compara contra el RUT.

## Checklist de calidad
1. ¿Tengo el RUT (o consulta del NIT en DIAN) de cada tercero nuevo del periodo?
2. ¿El DV valida con el algoritmo para todos los terceros creados?
3. ¿Tipo de documento correcto (13/31/22/41/42) según el tercero?
4. ¿Cero genéricos ("VARIOS", "CONSUMIDOR FINAL") en cuentas que van a exógena por tercero?
5. ¿Responsabilidades clave anotadas (47, 48/49, 07, 13) para decidir retenciones?
6. ¿Dirección y municipio poblados?
7. ¿Sin duplicados en el maestro (búsqueda por NIT y por nombre)?
8. ¿Las correcciones quedaron documentadas y comunicadas al cliente?

## Relacionado
- Anterior: [[Aux 02 - Partida Doble y Asientos Contables]] · Siguiente: [[Aux 04 - Soportes Contables y Papeles de Trabajo]]
- [[MOC - Escuela Auxiliar Contable]] · [[02-AuxiliarContable-Senior]]
- *Subskill B5 - Depurar Terceros y Cuantias Menores* · [[Cuantias Menores 3 UVT]] · [[Aux 14 - Calculo de Retenciones]]
- **Cliente - EMPRESA H** (saneamiento real de terceros)
