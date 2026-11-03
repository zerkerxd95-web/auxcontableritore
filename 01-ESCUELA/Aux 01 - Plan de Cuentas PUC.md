---
tipo: leccion
tags: [ritore, escuela, auxiliar, puc]
modulo: 1
estado: vigente
fecha: 2026-06-08
---
# Aux 01 - Plan de Cuentas PUC

## Objetivo
Al terminar esta lección el auxiliar sabrá leer cualquier código del PUC (clase → grupo → cuenta → subcuenta → auxiliar), identificar la naturaleza débito/crédito de cada clase, ubicar las cuentas que más usa la firma y crear cuentas auxiliares con criterio, entendiendo que **cada cuenta que crea terminará mapeada a un formato y concepto de exógena**.

## Marco conceptual y normativo
- **Decreto 2650 de 1993** — Plan Único de Cuentas para comerciantes. Sigue siendo la taxonomía operativa de todos los software contables colombianos (Siigo, World Office, Alegra, Helisa), aunque la medición y presentación se rigen por **NIIF para PYMES** (Decreto 2420 de 2015, Anexo 2).
- **Convivencia PUC ↔ NIIF:** el PUC da el *código* (dónde se registra); la NIIF da el *criterio* (cuánto y cuándo se reconoce). Ejemplo: un computador se codifica en 1528 (PUC) pero su vida útil y depreciación se definen por política NIIF (Sección 17), con la diferencia fiscal del Art. 137 ET marcada aparte.
- El plan de cuentas de cada cliente se valida al onboarding y semestralmente (skill `validar-plan-cuentas-cliente` de [[02-AuxiliarContable-Senior]]).

## Paso a paso

### 1. Estructura del código
Cada dígito agrega nivel de detalle:

| Nivel | Dígitos | Ejemplo | Significado |
|---|---|---|---|
| Clase | 1 | 1 | Activo |
| Grupo | 2 | 11 | Disponible |
| Cuenta | 4 | 1110 | Bancos |
| Subcuenta | 6 | 111005 | Moneda nacional |
| Auxiliar | 8+ | 11100501 | Bancolombia cta 7374 (lo crea la firma) |

### 2. Las nueve clases y su naturaleza

| Clase | Nombre | Naturaleza (aumenta por) |
|---|---|---|
| 1 | Activo | Débito |
| 2 | Pasivo | Crédito |
| 3 | Patrimonio | Crédito |
| 4 | Ingresos | Crédito |
| 5 | Gastos | Débito |
| 6 | Costos de ventas | Débito |
| 7 | Costos de producción o de operación | Débito |
| 8 | Cuentas de orden deudoras | Débito |
| 9 | Cuentas de orden acreedoras | Crédito |

Regla mnemotécnica: **lo que tengo y lo que gasto es débito (1-5-6-7); lo que debo, lo que es de los socios y lo que gano es crédito (2-3-4)**. Una cuenta con saldo contrario a su naturaleza es una alerta automática de revisión (ej.: un banco 1110 en crédito = posible sobregiro o error).

### 3. Cuentas más usadas en la firma

| Cuenta | Nombre | Uso típico en FYT |
|---|---|---|
| 1105 | Caja | Ventas de mostrador, caja menor |
| 1110 | Bancos | Bancolombia/BBVA; un auxiliar por cuenta bancaria |
| 1305 | Clientes | CxC por facturas de venta (auxiliar por tercero) |
| 1325 | Cuentas por cobrar a socios y accionistas | Gastos personales de socios = préstamo, NUNCA gasto (ver [[Aux 06 - Causacion de Facturas de Compra y Gastos]]) |
| 1355 | Anticipo de impuestos y contribuciones | 135515 retefuente que NOS practican, 135517 reteIVA, 135518 reteICA |
| 1435 | Mercancías no fabricadas por la empresa | Inventario de comercializadoras |
| 1524 / 1528 / 1540 | Equipo de oficina / cómputo / flota | Activos fijos (compras van al 15xx, no al gasto) |
| 2205 | Proveedores nacionales | CxP por compras de bienes |
| 2335 | Costos y gastos por pagar | CxP por servicios, honorarios, arrendamientos |
| 2365 | Retención en la fuente | Lo que el cliente RETIENE a terceros (por subcuenta de concepto) |
| 2367 | Impuesto a las ventas retenido | ReteIVA practicado (15% del IVA) |
| 2368 | Impuesto de industria y comercio retenido | ReteICA practicado |
| 2404 | De renta y complementarios | Impuesto de renta por pagar |
| 2408 | Impuesto sobre las ventas por pagar | IVA generado (crédito) y descontable (débito) |
| 2505 y ss. | Obligaciones laborales | 2505 salarios, 2510 cesantías, 2515 intereses, 2525 vacaciones |
| 2805 | Ingresos recibidos por anticipado / anticipos de clientes | Patrón **Cliente - SALÓN DE BELLEZA I**: plata recibida sin facturar |
| 3105 / 3115 | Capital suscrito y pagado / Aportes sociales | Capital según tipo societario |
| 3605 | Utilidad del ejercicio | Cierre anual |
| 4135 | Comercio al por mayor y al por menor | Ingresos de comercializadoras |
| 41xx | Operacionales por actividad | 4140 hoteles/restaurantes, 4145 transporte, 4155 servicios empresariales — según objeto social |
| 4175 | Devoluciones en ventas (DB) | Notas crédito emitidas |
| 5xxx | Gastos | 51 administración, 52 ventas, 53 no operacionales (¡no deducibles van al 53!) |
| 6xxx | Costos de ventas | 6135 comercio; 62 compras |
| 7xxx | Costos de producción | 71 materia prima, 72 mano de obra directa, 73 CIF — clientes industriales |

### 4. Crear cuentas auxiliares con criterio
1. **Verifica que no exista** una cuenta que ya sirva (cuentas duplicadas "en intención" son hallazgo de auditoría).
2. **Respeta la jerarquía:** el auxiliar hereda el sentido de su subcuenta. Nunca cuelgues un gasto bajo un activo "porque ahí cabía".
3. **Nombra describiendo el QUÉ, no el quién:** el tercero va en el campo tercero del asiento, no en el nombre de la cuenta (excepto auxiliares de bancos, donde sí se identifica la cuenta bancaria).
4. **Piensa en exógena ANTES de crear:** cada cuenta nueva debe poder mapearse a un formato/concepto DIAN (la 5135 → F-1001 concepto 5004; la 1305 → F-1008; la 2408 → F-1005/1006). Una cuenta sin mapeo claro se escala, no se asume — ver *Subskill B4 - Mapear Cuenta Formato Concepto*.
5. **Documenta** la cuenta nueva en el perfil del cliente para mantener la matriz de mapeo al día.

## Errores comunes
- **Mandar todo a "diversos" (5195/529595):** vuelve imposible el mapeo a conceptos de exógena y dispara el "cajón de sastre" 5016 que el control de calidad rechaza.
- **Registrar compras de activos fijos en el gasto 5xxx** en lugar del 15xx: distorsiona renta y el F-1001 (concepto 5008 vs 5016).
- **Usar cuentas 53 como si fueran 51:** la clase 53 (no operacionales) marca no deducibilidad en el F-1001 (columna O, regla C.3 del agente de exógena). Clasificar mal cambia la renta del cliente.
- **Planes de cuenta heredados sin CLIENTE DEL CLIENTE:** en **Cliente - EMPRESA H** la contabilidad la lleva un tercero y FYT debió emitir documento de observaciones cuenta por cuenta (1105, 1305, 1355, 2335, 2805…) antes de poder reportar exógena.
- **No cerrar el año contra 36/37:** las cuentas de resultado arrastran saldos viejos y los reportes salen contaminados (regla D.5: trabajar con movimientos del periodo, nunca con saldo acumulado).

## Checklist de calidad
1. ¿Sé decir la clase, grupo y cuenta de cualquier código de 6 dígitos sin mirar el PUC?
2. ¿La cuenta que voy a usar tiene la naturaleza correcta para el movimiento que registro?
3. ¿Existe ya una cuenta equivalente antes de crear una nueva?
4. ¿La cuenta nueva quedó bajo la subcuenta correcta de la jerarquía?
5. ¿Sé a qué formato/concepto de exógena mapea esta cuenta?
6. ¿Las cuentas con saldo contrario a su naturaleza están justificadas o reportadas?
7. ¿El plan del cliente tiene cuentas para TODAS sus obligaciones (IVA, retefuente, reteICA, INC si aplica)?

## Relacionado
- Siguiente: [[Aux 02 - Partida Doble y Asientos Contables]]
- [[MOC - Escuela Auxiliar Contable]] · [[02-AuxiliarContable-Senior]]
- *Subskill B4 - Mapear Cuenta Formato Concepto* · *Formato 1001 - Pagos y Retenciones*
- **Cliente - EMPRESA H** (caso real de saneamiento de plan de cuentas)
