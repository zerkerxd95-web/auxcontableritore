---
tipo: leccion
tags: [ritore, escuela, auxiliar, balance, libro-auxiliar]
modulo: 7
estado: vigente
fecha: 2026-06-08
---

# Aux 23 - Balance de Prueba y Libro Auxiliar

## Objetivo

Que el auxiliar sepa leer, verificar y usar correctamente los dos reportes contables de trabajo de la firma: el **balance de prueba** (BP) y el **libro auxiliar**, sepa cuál es la fuente correcta para cada propósito (regla C.2 — movimiento vs saldo) y detecte las banderas rojas antes de que contaminen liquidaciones, cruces y exógena.

## Marco conceptual y normativo

- **Balance de prueba:** listado de TODAS las cuentas con saldo inicial, débitos, créditos y saldo final del periodo. Es la "foto" de saldos. Puede pedirse **por tercero** (cada cuenta abierta por NIT).
- **Libro auxiliar:** detalle movimiento a movimiento de cada cuenta (fecha, comprobante, tercero, débito, crédito). Es la "película" del periodo.
- **Regla C.2 de *Lecciones Aprendidas Exogena* — fuente correcta por propósito:**

| Necesito... | Fuente | Ejemplos |
|-------------|--------|----------|
| **MOVIMIENTOS** del periodo | **Libro auxiliar por tercero** | Formatos 1001, 1005, 1006, 1007, 2276, retenciones; cruces token vs contabilidad; liquidaciones de IVA |
| **SALDOS** a una fecha | **Balance de prueba por tercero** | Formatos 1008, 1009, 1012; CxC/CxP al 31-dic; verificación de EEFF |

- Matiz verificado: el auxiliar suele ser más completo que el BP por tercero exportado (caso **Cliente - SERVICIOS SANITARIOS E**: BP con $5,2M de ingresos de menos). Por eso siempre se **valida el total del aux contra el BP**.

## Paso a paso

### 1. Exportación correcta desde el software (Siigo / World Office)

- Exportar **ambos** reportes a la **misma fecha de corte** — un BP de una fecha y un aux de otra producen diferencias fantasma (caso **Cliente - COMERCIO DE BICICLETAS A**: BP por tercero desactualizado, $554M vs $401M; hubo que reconstruir SF_tercero = SI(BP) + Débitos − Créditos del aux y pedir re-exportar).
- Pedir el BP **por tercero** (con NIT) cuando se vaya a usar para saldos por tercero.
- Pedir el aux **con tercero en cada movimiento** y todas las cuentas del rango necesario.
- En Excel: verificar integridad del archivo (regla C.1 — `BadZipFile`, OneDrive) antes de procesar.
- Ojo con el formato del exportado: en algunos auxiliares (caso **Cliente - EXPORTADORA DE SERVICIOS B**) la fila del código de cuenta **también trae el primer movimiento**; saltarla pierde el primer movimiento de cada cuenta (~$80M perdidos hasta detectarlo).

### 2. Verificaciones obligatorias del libro auxiliar

1. **Débitos totales = Créditos totales** (el aux SIEMPRE cuadra; si no cuadra, el problema es del parseo o de la exportación — regla C.1).
2. **Excluir las filas "SALDO INICIAL"** (fecha 31-dic del año anterior) al procesar movimientos.
3. Todo movimiento con tercero identificado; los movimientos sin NIT se listan aparte para depurar.
4. Verificar que el rango de fechas corresponda exactamente al periodo solicitado.

### 3. Verificaciones obligatorias del balance de prueba

1. **Suma de saldos débito = suma de saldos crédito** (ecuación contable).
2. **Saldos de naturaleza contraria = bandera roja:**

| Bandera | Significado probable | Caso real |
|---------|---------------------|-----------|
| Activo con saldo crédito (caja negativa) | Pagos registrados sin haber registrado los ingresos de caja, o doble egreso | **Cliente - EMPRESA H** — caja negativa; **Cliente - CARNICERÍA S (PN)** — caja crédito $-415M |
| Pasivo con saldo débito | Pagos en exceso, anticipos mal clasificados o causaciones faltantes | Frecuente en 2365/2408 |
| Ingreso con saldo débito | Reclasificaciones o NC mal aplicadas | — |

   Una bandera roja no se "arregla" reclasificando a ciegas: se investiga la causa y se escala si es material.
3. **Saldo final = saldo inicial + débitos − créditos**, fila por fila (detecta exportados corruptos).
4. Si el año anterior no se cerró (regla D.5 del [[Protocolo IVA Formulario 300]]): las cuentas 41xx, 2408xx, 511570/731570 arrastran saldos antiguos → para cualquier dato del periodo usar **movimientos**, no el saldo acumulado, y declarar el hallazgo.

### 4. Ejemplo numérico — leer una cuenta del BP por tercero

```
Cuenta 130505 — Clientes nacionales
Tercero                SI         Débitos     Créditos    SF
NIT 900.000.000-1 ABC SAS  4.000.000  10.000.000   8.000.000  6.000.000
NIT 900.000.000-1 XYZ LTDA 0           2.380.000   2.380.000          0
TOTAL CUENTA           4.000.000  12.380.000  10.380.000  6.000.000
```

- Para el **formato 1008** (CxC al 31-dic) tomo los **SF por tercero** (6.000.000 de ABC SAS).
- Para el **formato 1007** (ingresos del año) NO uso esta cuenta: voy al **auxiliar de 4135 por tercero** (movimiento).
- XYZ LTDA facturó y pagó todo en el año: tiene movimiento (va en 1007 si es ingreso) pero no saldo (no va en 1008).

## Errores comunes (casos reales FYT)

- Tomar saldos del aux y movimientos del BP — al revés de la regla C.2 (caso EXPORTADORA DE SERVICIOS B: el 1007 desde un aux incompleto dio $773M; reconstruido desde BP por tercero, $854M — por eso se validan ambos entre sí).
- Procesar el aux sin verificar débitos = créditos → parser roto pasa inadvertido (caso EXPORTADORA DE SERVICIOS B, primer movimiento de cada cuenta perdido).
- No excluir "SALDO INICIAL" → movimientos inflados con saldos del año anterior.
- Usar saldos acumulados de 41xx/2408 con el año sin cerrar (regla D.5).
- BP por tercero desactualizado frente al aux (COMERCIO DE BICICLETAS A) → reconstruir SF = SI + D − C y pedir re-exportación a la misma fecha.
- Ignorar la caja negativa "porque siempre ha estado así" — **Cliente - EMPRESA H**: toda naturaleza contraria se investiga y documenta.

## Checklist de calidad

- [ ] BP y aux exportados a la misma fecha de corte, por tercero, archivo íntegro (C.1).
- [ ] Aux: débitos = créditos; filas SALDO INICIAL excluidas del procesamiento.
- [ ] BP: ecuación cuadrada; SF = SI + D − C verificado.
- [ ] Saldos de naturaleza contraria listados, investigados o escalados.
- [ ] Total del aux validado contra el BP (y viceversa).
- [ ] Fuente correcta por propósito: movimiento → aux; saldo → BP (regla C.2).
- [ ] Hallazgo de "año sin cerrar" declarado si aplica (D.5), trabajando por movimientos.

## Relacionado

- Lección anterior: [[Aux 22 - Conciliacion Bancaria]] · Lección siguiente: [[Aux 24 - Cierre Contable Mensual]]
- [[Aux 01 - Plan de Cuentas PUC]] · [[Aux 02 - Partida Doble y Asientos Contables]] · [[Aux 03 - Terceros y RUT]] · [[Aux 04 - Soportes Contables y Papeles de Trabajo]]
- *Lecciones Aprendidas Exogena* · [[Protocolo IVA Formulario 300]]
- Agentes: [[02-AuxiliarContable-Senior]] · [[04-AuxiliarFacturacionElectronica-Senior]]
- Casos: **Cliente - EMPRESA H** · **Cliente - EXPORTADORA DE SERVICIOS B** · **Cliente - COMERCIO DE BICICLETAS A** · **Cliente - SERVICIOS SANITARIOS E** · **Cliente - CARNICERÍA S (PN)**
- [[MOC - Escuela Auxiliar Contable]]
