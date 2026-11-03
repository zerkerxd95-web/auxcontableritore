---
tipo: leccion
tags: [ritore, escuela, auxiliar, cierre, cierre-anual]
modulo: 7
estado: vigente
fecha: 2026-06-08
---

# Aux 25 - Cierre Anual y Errores Comunes

## Objetivo

Que el auxiliar entienda y ejecute el **cierre anual de resultados**, la apertura del año siguiente y la distribución de utilidades, y conozca el TOP de errores reales documentados por la firma — con su prevención — porque el problema más recurrente de los clientes que heredamos es, precisamente, **el año sin cerrar**.

## Marco conceptual y normativo

- **Cierre anual** = cancelar al 31 de diciembre todas las cuentas de resultado (clases 4-ingresos, 5-gastos, 6-costos de ventas, 7-costos de producción) y llevar la diferencia al patrimonio como **utilidad del ejercicio (3605)** o **pérdida del ejercicio (3610)**.
- Al abrir el año siguiente, el resultado del ejercicio se reclasifica a **resultados acumulados (3705 utilidades / 3710 pérdidas)**, donde queda hasta que el máximo órgano social decida su distribución.
- **Por qué NO cerrar el año es el problema recurrente de la firma (regla D.5 del [[Protocolo IVA Formulario 300]]):** si las clases 4/5/6/7 y los acumulados de 2408 no se cancelan, las cuentas 41xx, 2408xx, 511570/731570 **arrastran saldos antiguos** al año nuevo. Consecuencias: el saldo de "ingresos del año" mezcla varios años, el IVA acumulado no cruza con ningún F-300, y toda liquidación obliga a trabajar **por movimientos del periodo** (excluyendo "SALDO INICIAL") en vez de por saldos. Se declara como hallazgo y se propone el cierre, pero la liquidación del periodo no se frena por ello.

## Paso a paso

### 1. Pre-cierre (diciembre-enero)

1. Cierre mensual de diciembre completo ([[Aux 24 - Cierre Contable Mensual]]): token causado, bancos conciliados, impuestos cuadrados.
2. Ajustes de fin de año: depreciaciones, provisiones de prestaciones consolidadas ([[Aux 12 - Provisiones y Prestaciones Sociales]]), juego/ajuste de inventarios ([[Aux 18 - Juego de Inventarios]]), deterioros, diferencia en cambio de cierre.
3. Depuración final de terceros y verificación del BP por tercero (insumo de exógena — regla C.2).

### 2. Asiento de cierre de resultados

Cancelar cada cuenta de resultado contra su propio saldo y llevar el neto a 3605/3610 (en la práctica, vía la cuenta puente 5905 "ganancias y pérdidas"):

```
Ejemplo (cifras del año):
  Ingresos (41xx)                      850.000.000  (saldo crédito)
  Costos de ventas (61xx)              480.000.000  (saldo débito)
  Gastos (51xx/52xx/53xx)              290.000.000  (saldo débito)

Asiento de cierre al 31-dic:
DB 41xx  Ingresos                       850.000.000
   CR 61xx Costo de ventas                          480.000.000
   CR 5xxx Gastos                                   290.000.000
   CR 590505 Ganancias y pérdidas                    80.000.000
DB 590505 Ganancias y pérdidas           80.000.000
   CR 3605 Utilidad del ejercicio                    80.000.000
```

Tras el cierre, **todas las cuentas de resultado quedan en cero**: el 1 de enero las 41xx/5xxx/6xxx arrancan limpias.

### 3. Apertura del año siguiente

```
DB 3605 Utilidad del ejercicio           80.000.000
   CR 3705 Utilidades acumuladas                     80.000.000
```

(En pérdida: DB 3710 / CR 3610.) El balance de apertura trae solo cuentas de balance (clases 1, 2, 3).

### 4. Distribución de utilidades

- Solo la decide el **máximo órgano social** (asamblea/junta) en acta; primero la **reserva legal** (10 % de la utilidad hasta el 50 % del capital — sociedades obligadas).
- Decretado el dividendo: DB 3705 / CR 2360 (dividendos por pagar); al pagar: DB 2360 / CR 1110, con la retención sobre dividendos que aplique.
- El auxiliar NUNCA distribuye utilidades sin acta: si el cliente "se llevó plata", eso es cuenta por cobrar al socio o dividendo decretado — se escala al Contador Titular.

## Errores comunes — TOP de casos reales FYT

| # | Error real | Cliente | Magnitud | Prevención |
|---|-----------|---------|----------|------------|
| 1 | **Año sin cerrar** contra 3605/3705: 41xx/2408/5115 arrastrando saldos de años anteriores | Varios clientes (patrón recurrente — regla D.5) | Distorsiona todo saldo acumulado | Cerrar cada año en enero; mientras tanto, trabajar SIEMPRE por movimientos del periodo |
| 2 | **Reclasificaciones erradas** en el auxiliar que descuadran los formatos contra la realidad | **Cliente - SERVICIOS SANITARIOS E** | $455M | No reclasificar "para que cuadre": se corrige la contabilidad con causa raíz documentada (regla C.8) |
| 3 | **Gastos personales del socio como gasto de la empresa** | **Cliente - EMPRESA DE TECNOLOGÍA K** | $273,8M | Filtro en causación: gasto sin relación de causalidad → CxC al socio (1365), no gasto; escalar |
| 4 | **CxC eliminadas sin contrapartida** (descuadre directo del balance) | **Cliente - EMPRESA DE TECNOLOGÍA K** | $90,8M | Toda baja de cartera exige asiento completo (deterioro/castigo aprobado), nunca borrar registros |
| 5 | **Terceros genéricos** ("varios", NIT 222222222 fuera de regla, "consumidor final" en todo) | **Cliente - EMPRESA H** | Bloquea exógena y cruces | Depurar terceros en cada cierre mensual ([[Aux 03 - Terceros y RUT]]); cuantías menores solo según la regla de 3 UVT |
| 6 | **Inventario sobrestimado** (no se reconoce el costo real / juego de inventarios sin hacer) | **Cliente - AGROPECUARIA D** | Utilidad inflada | Conteo físico + juego de inventarios al cierre ([[Aux 18 - Juego de Inventarios]]); cruzar con [[Aux 19 - Estado del Costo]] |

Lectura transversal del TOP: casi todos los errores nacen de **saltarse los cierres mensuales** o de **forzar cifras para que cuadren**. La ética de la firma (C.8/D.10) es la prevención maestra: nunca maquillar; corregir la contabilidad, documentar la causa raíz y escalar al Contador Titular.

## Checklist de calidad

- [ ] Cierre mensual de diciembre terminado ANTES del cierre anual.
- [ ] Ajustes de fin de año registrados (depreciación, provisiones, inventarios, deterioros, diferencia en cambio).
- [ ] Asiento de cierre: clases 4/5/6/7 en CERO al 1 de enero.
- [ ] Resultado del ejercicio en 3605/3610 = utilidad del Estado de Resultados.
- [ ] Apertura del año siguiente con reclasificación a 3705/3710.
- [ ] Distribuciones de utilidades solo con acta; retenciones sobre dividendos aplicadas.
- [ ] BP de cierre sin saldos de naturaleza contraria sin explicar ([[Aux 23 - Balance de Prueba y Libro Auxiliar]]).
- [ ] Hallazgos tipo TOP documentados con causa raíz y escalados — nunca maquillados.
- [ ] Paquete de cierre anual archivado: es el insumo directo de exógena y renta.

## Relacionado

- Lección anterior: [[Aux 24 - Cierre Contable Mensual]] — fin del Módulo 7.
- [[Aux 17 - Inventarios y Compras Multi-item]] · [[Aux 18 - Juego de Inventarios]] · [[Aux 19 - Estado del Costo]] · [[Aux 03 - Terceros y RUT]]
- [[Protocolo IVA Formulario 300]] · *Lecciones Aprendidas Exogena*
- Agentes: [[02-AuxiliarContable-Senior]] · *01-Orquestador-Master* · *16-EstadosFinancieros-Senior*
- Casos: **Cliente - SERVICIOS SANITARIOS E** · **Cliente - EMPRESA DE TECNOLOGÍA K** · **Cliente - EMPRESA H** · **Cliente - AGROPECUARIA D**
- [[MOC - Escuela Auxiliar Contable]]
