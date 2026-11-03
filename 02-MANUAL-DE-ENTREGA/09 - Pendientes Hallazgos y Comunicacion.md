---
tipo: manual
tags: [ritore, auxiliar, pendientes, hallazgos, comunicacion]
estado: vigente
version: 1.0
fecha: 2026-11-03
---

# 09 · Pendientes, hallazgos y comunicación

> **Un hueco declarado es aceptable; un hueco silencioso no.** Lo que no se pudo resolver se nombra: cuánto, por qué, qué documento falta, a quién se le pidió y para cuándo.

## 1. Cómo se escribe un pendiente

Cada pendiente es una fila, con estas columnas, en `04-TRAZAS/NOTAS-Y-PENDIENTES.md`:

| # | Área | Qué falta o qué pasó | Valor | Responsable | Fecha límite | Estado |
|---|---|---|---|---|---|---|
| 1 | Bancos | Consignación del 14 sin identificar | $1.250.000 | Cliente (cartera) | 2026-02-10 | Pedido el 2026-02-04 |

Prohibido: "revisar banco", "ver con el cliente", "pendiente", sin valor ni responsable.

## 2. Cómo se escribe un hallazgo

Un hallazgo es algo que **cambia cifras o riesgo**. Se escribe con cuatro partes:

1. **Qué**: el hecho, con cuenta, tercero, documento y valor.
2. **Por qué importa**: efecto en impuestos, en estados financieros o en riesgo (sanción, glosa de exógena).
3. **Qué propongo**: el asiento propuesto (número de la hoja de asientos) o el documento a pedir.
4. **Quién decide**: si lo resuelve el auxiliar o es decisión del contador.

Ejemplo: *"Factura de venta FE-1043 del 18-ene por $2.380.000 + IVA $452.200 está en el token y no en libros. Subestima ingresos, IVA generado del bimestre y autorretención. Propongo el asiento 7 de la hoja. Lo resuelvo yo; solo informo."*

## 3. La tabla de diferencias

`04-TRAZAS/TABLA-DE-DIFERENCIAS.md`, con columnas fijas: **concepto · fuente A · fuente B · diferencia · % · explicación · acción · estado** (RESUELTA / PENDIENTE / ACEPTADA con criterio). Ninguna diferencia ≥ 1 UVT o ≥ 0,5 % puede quedar sin explicación escrita. Las resueltas dicen cómo; las aceptadas dicen por qué y quién decidió.

## 4. El resumen de la entrega (`ENTREGA.md`)

Una página. El contador debe saber en un minuto si puede firmar. Plantilla en `plantillas/ENTREGA.md`:

1. Encabezado: cliente, NIT, período, quién preparó, fecha, vencimientos del mes.
2. **Semáforo de las ocho áreas** (verde: cerrada; ámbar: cerrada con pendiente menor documentado; rojo: no cerrada).
3. Cifras clave: ingresos del mes (token y libros), IVA generado y descontable, retención por concepto, saldo de bancos conciliado.
4. **Decisiones para el contador**: lista numerada, cada una con la opción que recomienda el auxiliar y su efecto en pesos.
5. Lo que falta del cliente.
6. Archivos de la entrega.

## 5. Comunicación con el cliente

El auxiliar **pide insumos** y **confirma recibidos**; los hallazgos, las cifras a pagar y las recomendaciones **las comunica el contador** o se envían con su aprobación. Todo mensaje al cliente tiene tres partes: qué se necesita o qué pasó (1–2 líneas), qué significa para él en plata o riesgo, qué se le pide y para cuándo. Lenguaje llano, sin tecnicismos sin traducir, sin referencias religiosas.

## 6. Comunicación con el contador

- La entrega se anuncia en una línea (ver estándar de entrega §6).
- Una diferencia ≥ 500 UVT o una señal de irregularidad (gastos personales del socio, inventarios sin soporte, estados financieros "no reales", operaciones en efectivo inusuales) se avisa **el mismo día**, por fuera de la entrega.
- Las observaciones del contador se responden debajo de cada una en `OBSERVACIONES-DEL-CONTADOR.md`: qué se corrigió, dónde y cuándo.

## Relacionado

- [[01 - Estandar de Entrega al Contador]] · [[ESTANDAR-DE-ENTREGABLES]] · [[regla-informes-lenguaje-llano]]
