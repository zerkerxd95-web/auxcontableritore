---
tipo: leccion
tags: [ritore, escuela, auxiliar, conciliacion, bancos]
modulo: 7
estado: vigente
fecha: 2026-06-08
---

# Aux 22 - Conciliación Bancaria

## Objetivo

Que el auxiliar concilie cada mes, cuenta por cuenta, el **extracto bancario contra los libros** (cuenta 1110), tipifique y documente las partidas conciliatorias, produzca un papel de trabajo auditable y sepa detectar y escalar movimientos inusuales. Sin conciliación bancaria, los saldos de efectivo de los EEFF son inconfiables.

## Marco conceptual y normativo

- **Conciliar** = explicar la diferencia entre el saldo del extracto y el saldo en libros (1110) a una misma fecha de corte. La diferencia NUNCA se ajusta "a la brava": se explica con partidas conciliatorias o se corrige el error que la causa.
- **GMF (4×1.000):** Arts. 870-881 ET. Lo cobra el banco sobre retiros y transferencias; verificar exenciones del Art. 879 ET (cuenta marcada exenta, traslados entre cuentas del mismo titular). Es **deducible solo en el 50 %** en renta (Art. 115 ET).
- Las **pasarelas de pago** (Addi, Agaval, Plin, Wompi, etc.) se concilian igual que un banco: el dinero recaudado por la pasarela es un derecho (cuenta puente 1110/1355/13xx según política del cliente) hasta que lo transfiere, neto de sus comisiones.
- En el ecosistema, esta tarea es del agente [[03-AuxiliarConciliacionesBancarias-Senior]]; el auxiliar humano replica su método.

## Paso a paso

### 1. Insumos

- Extracto del mes (Excel, PDF o formato estructurado OFX/MT940).
- Libro auxiliar de la cuenta 1110xx del mismo periodo (por movimientos — regla C.2).
- Conciliación del mes anterior (las partidas pendientes se arrastran y se les hace seguimiento).

### 2. Matching movimiento a movimiento

Por cada línea del extracto, buscar su pareja en libros por **monto + fecha (±3 días) + descripción**. Lo que cruza queda conciliado; lo que no, se tipifica:

| Partida conciliatoria | Lado donde está | Tratamiento |
|----------------------|-----------------|-------------|
| Cheques girados pendientes de cobro | En libros, no en extracto | Esperar cobro; si > 30 días, seguimiento; > 60 días, alertar |
| Consignaciones en tránsito | En libros, no en extracto | Deben aparecer en los primeros días del mes siguiente |
| **GMF (4×1.000)** | En extracto, no en libros | Causar: DB 530595 (gasto GMF) / CR 1110 |
| Comisiones bancarias | En extracto, no en libros | Causar: DB 530520 / CR 1110 |
| Rendimientos financieros | En extracto, no en libros | Causar: DB 1110 / CR 421005 |
| Pagos de clientes no identificados | En extracto, no en libros | Identificar el tercero (NIT en la descripción, cartera); si no, "pendiente identificación" y consultar al cliente |
| Errores del banco | En extracto | Reclamar al banco vía cliente; documentar |
| Errores de libros (doble registro, valor errado) | En libros | Corregir la contabilidad con nota |

### 3. Formato del papel de trabajo

```
CONCILIACIÓN BANCARIA — [Cliente] — [Banco/Cuenta] — [Mes]

Saldo según extracto al cierre                      48.250.000
(−) Cheques girados pendientes de cobro             (3.500.000)
(+) Consignaciones en tránsito                       1.200.000
Saldo extracto ajustado                             45.950.000

Saldo según libros (1110) al cierre                 46.142.000
(−) GMF no contabilizado                              (152.000)
(−) Comisiones no contabilizadas                       (60.000)
(+) Rendimientos no contabilizados                      20.000
Saldo libros ajustado                               45.950.000

DIFERENCIA FINAL                                             0  ✔
```

La diferencia final debe ser **CERO**. Si no lo es, se busca hasta encontrar — nunca se cierra con diferencia sin explicar. Las partidas de libros ajustadas se causan de inmediato para que el saldo contable quede correcto.

### 4. Periodicidad y casos reales

- **Mensual, sin excepción**, dentro del cierre del mes ([[Aux 24 - Cierre Contable Mensual]]).
- Cuando se hereda un cliente atrasado se hace una **conciliación consolidada del periodo acumulado**: caso real **Cliente - EMPRESA CON SOCIO EXTRANJERO C**, conciliación consolidada Ene-Abr 2026, partiendo del último saldo conciliado confiable.
- **Pasarelas de pago:** caso real **Cliente - COMERCIO DE BICICLETAS A** — conciliaciones de **Addi, Agaval y Plin**. Particularidades: la pasarela abona neto de comisión (causar la comisión como gasto), los recaudos del último día quedan en tránsito, y cada pasarela tiene su propio reporte que hace las veces de "extracto".

### 5. Movimientos inusuales → escalar

Durante la conciliación se vigilan señales de alerta: depósitos fraccionados recurrentes (estructuración), transferencias internacionales sin soporte, contrapartes desconocidas o en listas restrictivas, retiros atípicos.

- Estas señales se escalan a *20-SAGRLAFT-Senior* por el **canal restringido**.
- **NUNCA se comenta con el cliente** (prohibición de tipping-off, Art. 39 Ley 1121/2006). La conciliación continúa con total normalidad.
- Los errores operativos (cargo duplicado del banco, comisión inusual) sí se informan al cliente — distinguir siempre entre error operativo y señal SAGRLAFT.

## Errores comunes (casos reales FYT)

- "Cuadrar" la diferencia contra un gasto o un ingreso genérico en vez de identificar la causa — prohibido (misma ética de C.8: no se maquilla).
- Olvidar causar GMF y comisiones cada mes → el saldo de 1110 se aleja del banco progresivamente.
- Deducir el 100 % del GMF en renta (solo procede el 50 % — Art. 115 ET).
- Dejar envejecer partidas conciliatorias: > 30 días exigen gestión; > 60 días, alerta al Contador Titular; 90+ días, propuesta de ajuste.
- En pasarelas, registrar el abono neto como ingreso (en vez de ingreso bruto + gasto comisión).
- Conciliar contra el saldo acumulado de libros en clientes con descuadres previos: validar primero que el auxiliar de 1110 cuadre (regla C.1).

## Checklist de calidad

- [ ] Todas las cuentas bancarias y pasarelas del cliente conciliadas (ninguna omitida).
- [ ] Diferencia final = 0, con todas las partidas tipificadas y documentadas.
- [ ] GMF, comisiones y rendimientos del mes causados.
- [ ] Partidas del mes anterior con seguimiento (resueltas o envejecidas con alerta).
- [ ] Partidas > 60 días alertadas al Contador Titular.
- [ ] Señales inusuales escaladas por canal restringido (sin tipping-off).
- [ ] Papel de trabajo archivado con extracto adjunto, fecha y responsable.

## Relacionado

- Lección anterior: [[Aux 21 - Cruce Token vs Contabilidad]] · Lección siguiente: [[Aux 23 - Balance de Prueba y Libro Auxiliar]]
- [[Aux 07 - Recibos de Caja]] · [[Aux 08 - Comprobantes de Egreso]] · [[Aux 16 - GMF y Cuentas Bancarias]]
- Agentes: [[03-AuxiliarConciliacionesBancarias-Senior]] · [[02-AuxiliarContable-Senior]] · *20-SAGRLAFT-Senior*
- Casos: **Cliente - EMPRESA CON SOCIO EXTRANJERO C** · **Cliente - COMERCIO DE BICICLETAS A**
- [[MOC - Escuela Auxiliar Contable]]
