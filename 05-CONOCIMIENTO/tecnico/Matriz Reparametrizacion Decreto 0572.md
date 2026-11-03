---
tipo: conocimiento
tags: [ritore, retencion, normativa, parametrizacion]
estado: vigente
fecha: 2026-06-11
---

# Matriz de Reparametrización — Decreto 0572 de 2025

Nota **operativa** para la transición tarifaria de retención en la fuente de julio 2026. Contexto normativo y judicial completo en *Proyecto - Retencion en la Fuente*. Responsable: *12-EspecialistaRetenciones-Senior*.

## (a) Cronología

| Fecha | Hito |
|-------|------|
| 28/05/2025 | Se expide el **D. 0572** (vigente desde 01/06/2025): sube la autorretención especial (hasta 4,5 % por CIIU) y baja bases mínimas de retención. |
| 22/08/2025 | Consejo de Estado **niega** la primera solicitud de suspensión. |
| 07/05/2026 | Consejo de Estado (Sección 4ª) **suspende provisionalmente los arts. 2 a 8**. DIAN (Comunicado 070 del 08/05/2026): desde el 08/05/2026 se aplican las normas anteriores al D. 0572. El **art. 1 (CDAT equiparado a CDT) nunca se suspendió**. |
| 02/06/2026 | Consejo de Estado **revoca la suspensión** (auto exp. 11001-03-27-000-2025-00055-00 (30229) AC): los arts. 2–8 recobran vigencia desde el **primer día calendario del mes siguiente a la ejecutoria del auto** — previsiblemente el **01/07/2026** `[VERIFICAR ejecutoria antes de reparametrizar]`. |
| Pendiente | **Fallo de fondo**: si la sentencia anula el decreto, los efectos serían retroactivos — conservar trazabilidad por cliente. |

## (b) Regla práctica

- **Junio 2026:** se aplican las tarifas y bases del **DUR 1625/2016 anteriores al D. 0572** (estado generado por la suspensión del 07/05/2026, aún sin efectos la revocatoria).
- **Desde la fecha de efectos de la revocatoria** (primer día calendario del mes siguiente a la ejecutoria del auto del 02/06/2026 — **previsiblemente 01/07/2026**, `[VERIFICAR ejecutoria]`): se aplican las tarifas y bases del **D. 0572**.
- Criterio de imputación: la tarifa aplicable es la vigente en la **fecha del pago o abono en cuenta** (lo primero que ocurra), no la del periodo declarado.
- El **art. 1 del D. 0572 (CDAT = CDT)** aplica sin interrupción todo el tiempo.

## (c) Matriz de doble columna por concepto

`[VERIFICAR tarifas exactas contra el DUR y el D. 0572 antes de liquidar julio]` — columna "pre-decreto" verificada contra la tabla de *Proyecto - Retencion en la Fuente* (UVT 2026 = $52.374):

| Concepto | Régimen pre-D. 0572 (aplicar JUNIO 2026) | Régimen D. 0572 (aplicar desde efectos de la revocatoria) |
|----------|------------------------------------------|------------------------------------------------------------|
| Honorarios y comisiones — PJ y PN declarante | 11 % · base 0 UVT | `[VERIFICAR — el D. 0572 modificó principalmente bases mínimas y autorretención]` |
| Honorarios y comisiones — PN no declarante | 10 % · base 0 UVT | `[VERIFICAR]` |
| Servicios generales — declarante | 4 % · base 4 UVT ($209.496) | `[VERIFICAR tarifa y base]` |
| Servicios generales — no declarante | 6 % · base 4 UVT ($209.496) | `[VERIFICAR tarifa y base]` |
| Compras generales — declarante | 2,5 % · base 27 UVT ($1.414.098) | 2,5 % · base **10 UVT** ($523.740) `[VERIFICAR]` |
| Arrendamiento bienes inmuebles | 3,5 % · base 27 UVT ($1.414.098) | `[VERIFICAR]` |
| Compra productos agropecuarios sin procesamiento | 1,5 % · base 92 UVT | 1,5 % · base **70 UVT** `[VERIFICAR]` |
| Servicios hoteles, restaurantes y hospedaje | 3,5 % · base 4 UVT | 3,5 % · base **2 UVT** `[VERIFICAR]` |
| **Autorretención especial** (D. 2201/2016, arts. 1.2.6.6–1.2.6.8 DUR) | 0,55 % / 1,1 % / 1,6 % según sector (D. 261/2023 y D. 242/2024) | Por código **CIIU, hasta 4,5 %** (ej. manufactura 1,1 % → 2,2 %) `[VERIFICAR tarifa por CIIU de cada cliente]` |
| Rendimientos CDAT | Equiparados a CDT (art. 1 D. 0572) — **vigente sin interrupción** | Igual |

## (d) Protocolo de documentación en papeles de trabajo

Cada **F-350** liquidado durante la transición (junio–agosto 2026) debe dejar registrado en el papel de trabajo:

1. **Qué régimen tarifario se aplicó** (pre-D. 0572 o D. 0572) y a qué fechas de pago/abono en cuenta corresponde.
2. **Por qué**: cita del hito judicial que lo sustenta (suspensión 07/05/2026 / revocatoria 02/06/2026 + fecha de ejecutoria verificada).
3. Evidencia de la **verificación de la ejecutoria** antes de liquidar julio (pantallazo/auto o comunicado DIAN).
4. Si un mes mezcla regímenes (pagos antes y después de la fecha de efectos), detalle por tercero/fecha.

Razón: si el fallo de fondo anula el decreto con efectos retroactivos, la trazabilidad por cliente es la defensa. Nunca maquillar: regla de oro C.8.

## (e) Checklist de reparametrización del software (antes de liquidar julio 2026)

- [ ] Confirmar **fecha de ejecutoria** del auto del 02/06/2026 y la fecha exacta de efectos `[VERIFICAR — previsiblemente 01/07/2026]`.
- [ ] Verificar comunicado/instrucción **DIAN** posterior a la revocatoria.
- [ ] Actualizar en el software contable de cada cliente las **bases mínimas** (compras 27→10 UVT, agro 92→70, hoteles 4→2, y demás del D. 0572 `[VERIFICAR lista completa]`).
- [ ] Actualizar las **tarifas de autorretención especial por CIIU** de cada cliente con responsabilidad 15 en el RUT (contra la tabla del D. 0572).
- [ ] Probar la liquidación con un caso de cada concepto (pago bajo base nueva vs vieja) antes del primer F-350 de julio.
- [ ] Dejar **respaldo de la parametrización anterior** (export/pantallazos) por si el fallo de fondo obliga a reversar.
- [ ] Registrar en el papel de trabajo de cada cliente el protocolo del punto (d).
- [ ] Avisar a los clientes autorretenedores el **impacto en caja** del alza de autorretención (hasta 4,5 %).

## (f) Clientes afectados (agentes de retención mensuales — F-350)

- **Cliente - EXPORTADORA DE SERVICIOS B**
- **Cliente - COMERCIO DE BICICLETAS A**
- **Cliente - SERVICIOS SANITARIOS E**
- **Cliente - EMPRESA CON SOCIO EXTRANJERO C**
- **Cliente - EMPRESA DE SOFTWARE O**
- **Cliente - EMPRESA Z**
- **Cliente - PERSONA NATURAL J (TALLER DE DISEÑO J)**
- **Cliente - TALLER AUTOMOTRIZ U**

> Revisar en cada uno la **responsabilidad 15** (autorretenedor especial — los más impactados por el D. 0572) y las responsabilidades de reteIVA/reteICA en el RUT.

## Relacionado

- *Proyecto - Retencion en la Fuente* (cronología, tabla completa de tarifas y fuentes consultadas)
- *12-EspecialistaRetenciones-Senior* · *MOC - Skills* (skill `retencion-master`)
- [[UVT y Topes]] · *Tablero de Alertas y Pendientes*
- *MOC - Conocimiento Tecnico*
