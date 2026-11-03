---
tipo: induccion
tags: [ritore, auxiliar, induccion]
estado: vigente
fecha: 2026-11-03
---

# Cómo trabaja la firma

## 1. Los roles

| Rol | Qué hace | Qué no hace |
|---|---|---|
| **Auxiliar contable** | recibe insumos, digita y causa con soporte, cruza el token, concilia, prepara borradores de impuestos y propone ajustes; entrega el período con su semáforo | no firma, no presenta, no crea cuentas ni cambia criterios |
| **Contador(a) Titular** | revisa la entrega, aprueba o devuelve ajustes, decide criterios, firma y presenta declaraciones y estados financieros | no recibe trabajo sin la estructura de entrega |
| **IA del auxiliar** (Claude u otra) | ejecuta el método: herramientas, cuadres, borradores, redacción; avisa lo que no cuadra | no decide por el contador ni inventa cifras |
| **Cliente** | envía insumos a tiempo y responde solicitudes | — |

La firma separa funciones (control de **cuatro ojos**): quien prepara no aprueba su propio trabajo.

## 2. El mes de un auxiliar

| Días hábiles | Qué pasa |
|---|---|
| último del mes | sale la solicitud de insumos al cliente; se crea la carpeta del período |
| 1–2 | token DIAN, extractos, novedades de nómina y soportes en `01-INSUMOS/` |
| 3 | causación del token completo y de los soportes no electrónicos |
| 4 | nómina, depreciaciones, conciliaciones bancarias y de pasarelas |
| 5 | cartera y proveedores; cuadre de impuestos y borradores |
| 6 | balance revisado, asientos propuestos, `ENTREGA.md` → **entrega al contador** |
| 7–8 | observaciones del contador y correcciones en el software; el contador presenta y paga antes del vencimiento |

El detalle, con lo que pasa si un vencimiento cae temprano o el cliente no envía insumos, está en el
[calendario de cierre](../02-MANUAL-DE-ENTREGA/02%20-%20Calendario%20de%20Cierre%20Mensual.md).

## 3. Las ocho áreas

1. **Token DIAN** — todo documento electrónico del mes está causado y todo lo causado tiene soporte.
2. **Bancos y pasarelas** — cada cuenta conciliada con diferencia cero.
3. **Cartera** — saldo por cliente = facturas abiertas; anticipos identificados.
4. **Proveedores y CxP** — saldo por proveedor = facturas abiertas; retenciones correctas.
5. **Impuestos** — lo que se declara sale de la contabilidad y la contabilidad cuadra con lo declarado.
6. **Nómina** — nómina = contabilidad = PILA = nómina electrónica.
7. **Costos, gastos y activos** — depreciaciones, diferidos, inventario y costo de ventas.
8. **Balance de prueba y terceros** — naturaleza de saldos, cuentas puente en cero, terceros reales.

## 4. Lo que hace que una entrega sea buena

- Llega **antes** del día pactado, completa y con el semáforo honesto (un 🔴 explicado vale más que un 🟢 falso).
- El contador puede revisarla **sin preguntarle nada al auxiliar**: todo está en `ENTREGA.md` y en las trazas.
- Las cifras de `ENTREGA.md` salen de los papeles de trabajo; los borradores salen de la contabilidad.
- Las decisiones del contador vienen con la opción recomendada y su efecto en pesos.
- Las observaciones del contador se corrigen en el software, no a mano en una salida.

## 5. Herramientas

- **Software contable del cliente** (formato S o W): donde se digita. Lo que se corrige, se corrige ahí.
- **Excel de la firma** ([07-PLANTILLAS-EXCEL](../07-PLANTILLAS-EXCEL/)) en paleta Ritoré.
- **Scripts de [herramientas/](../herramientas/)** para lo repetitivo y verificable.
- **Claude Code** con este repositorio (o la IA que use el auxiliar con [PROMPT-SISTEMA.md](../PROMPT-SISTEMA.md)).
- **Obsidian** para leer la escuela y el manual como un vault enlazado (opcional).

## 6. Confidencialidad

Los datos de cada cliente viven en su carpeta de trabajo y solo ahí. No se copian a este repositorio, no se mezclan
entre clientes y no se pegan en una IA pública sin anonimizar. Ver [CONFIDENCIALIDAD.md](../CONFIDENCIALIDAD.md).
