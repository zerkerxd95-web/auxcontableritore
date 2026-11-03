---
tipo: leccion
tags: [ritore, escuela, auxiliar, token-dian, cruces]
modulo: 6
estado: vigente
fecha: 2026-06-08
---

# Aux 21 - Cruce Token vs Contabilidad

## Objetivo

Que el auxiliar construya cada mes el **papel de trabajo de cruce** entre el Token DIAN y la contabilidad del cliente, identifique y tipifique las diferencias, y sepa cuáles corrige, cuáles documenta y cuáles escala. Este cruce es el control que hace que la contabilidad y la DIAN "cuenten la misma historia, factura por factura, peso por peso" ([[04-AuxiliarFacturacionElectronica-Senior]]).

## Marco conceptual y normativo

- El token es la **fuente de verdad** (regla D.1, [[Protocolo IVA Formulario 300]]): ante una diferencia, la hipótesis inicial es que la contabilidad está incompleta o errada — nunca se "maquilla" el formato para que cuadre (regla C.8 de *Lecciones Aprendidas Exogena* y D.10).
- La DIAN hace exactamente este mismo cruce de forma automática contra F-300, F-350, F-110 y exógena. Hacerlo nosotros primero, cada mes, es anticipar el requerimiento.
- Qué se cruza contra qué:

| Token (mensual) | Contabilidad (libro auxiliar / balance de prueba) |
|-----------------|---------------------------------------------------|
| Ventas `Emitido` netas de NC (base) | Movimiento crédito − débito de **4135** (y demás 41xx) |
| IVA generado del token | Movimiento crédito **240801** (2408 IVA generado) |
| Compras `Recibido` + DSEL (base) | Movimientos **1435 / 5xxx / 6xxx** (según destino) |
| IVA descontable del token | Movimiento débito **240802** |
| Nómina electrónica | Movimientos **51xx/52xx/72xx** laborales y 2505 |

- Regla C.2 / D.5: el cruce se hace con **MOVIMIENTOS del periodo** (débitos/créditos del libro auxiliar), nunca con saldos acumulados — especialmente si el año anterior no se cerró. Excluir filas "SALDO INICIAL".

## Paso a paso

### 1. Estructura del papel de trabajo (Excel)

| Hoja | Contenido |
|------|-----------|
| **Compras DIAN** | Detalle `Recibido` + DSEL: NIT, tercero, folio, fecha, Base (sin IVA), IVA, Total (con IVA) |
| **Ventas DIAN** | Detalle `Emitido` (sin DSEL), netas de NC: mismas columnas |
| **Cruce** | Totales token vs totales contables por rubro, con diferencia en $ y % |
| **Diferencias** | Lista documento a documento de lo que está en un lado y no en el otro, con tipo, causa y acción |

Las hojas de detalle separan SIEMPRE "Base (sin IVA)" y "Total (con IVA)" — regla D.9.

### 2. Ejecutar el cruce

1. Depurar el token (lección [[Aux 20 - Interpretacion del Token DIAN]]): duplicados, NIT receptor, DSEL, NC.
2. Exportar libro auxiliar y balance de prueba del mismo periodo ([[Aux 23 - Balance de Prueba y Libro Auxiliar]]).
3. Cruzar **totales** por rubro (tabla anterior).
4. Si hay diferencia, cruzar **documento a documento** por NIT + folio + valor para aislar exactamente cuáles faltan o sobran.
5. Tipificar cada diferencia y definir la acción.

**Ejemplo de hoja Cruce:**

| Rubro | Token DIAN | Contabilidad | Diferencia | Estado |
|-------|-----------:|-------------:|-----------:|--------|
| Ventas (base, netas) | 152.300.000 | 128.600.000 | 23.700.000 | 🔴 investigar |
| IVA generado | 28.937.000 | 24.434.000 | 4.503.000 | 🔴 ligado al anterior |
| Compras (base) | 96.450.000 | 96.450.000 | 0 | 🟢 |
| IVA descontable | 17.890.000 | 17.890.000 | 0 | 🟢 |

### 3. Tipos de diferencia y su causa

| Tipo | Descripción | Caso real FYT | Acción |
|------|-------------|---------------|--------|
| **En token, no en contabilidad** | Facturas emitidas o recibidas sin causar | la titular de la FLORISTERÍA Y: **$23,7M facturados sin contabilizar**, detectados en el cruce | Causar las facturas faltantes ([[Aux 05 - Causacion de Facturas de Venta]] / [[Aux 06 - Causacion de Facturas de Compra y Gastos]]) |
| **En contabilidad, no en token** | Ventas registradas que nunca se facturaron electrónicamente | **Cliente - SALÓN DE BELLEZA I**: ingresos no facturados reclasificados a **2805** mientras se regulariza la facturación | Hallazgo GRAVE: riesgo sanción Art. 652-1 ET; escalar al Contador Titular y regularizar facturación |
| **Documento de otro periodo** | Emitido en un mes, recibido/causado en otro | Recurrente en todos los clientes | Asignar al periodo correcto; para IVA descontable aplicar Art. 496 ET (ver Aux 20) |
| **Anulaciones** | FV + NC 100 % contabilizadas a medias | — | Contabilizar la pareja completa o ninguna |
| **Duplicados** | Mismo CUFE dos veces (en token o causado doble) | — | Deduplicar por CUFE; reversar la causación doble |
| **DSEL mal clasificado** | DSEL sumado como venta | Regla D.3 | Reclasificar como compra |

### 4. Umbral de materialidad y escalamiento

- Diferencia **individual ≥ 1 UVT** o **acumulada ≥ 0,5 % del total del rubro** → es MATERIAL: se investiga hasta resolver y se documenta con causa raíz. No se cierra el mes con cruces materiales abiertos.
- Diferencias inferiores → se documentan en la hoja Diferencias y se monitorean.
- Si la diferencia revela un error en una declaración ya presentada o ventas sin facturar → **escalar al Contador Titular**. Nunca ajustar el token ni forzar la contabilidad para "que dé".

### 5. El cruce como producto de la firma

Este papel de trabajo es el insumo del análisis **token-vs-contabilidad** que la firma entrega como diagnóstico: el caso **Cliente - EMPRESA CON SOCIO EXTRANJERO C** se documentó en un libro de **8 hojas** con este mismo esqueleto (detalles DIAN, cruce, diferencias, conclusiones). Un cruce mensual bien hecho se convierte, al final del año, en la conciliación anual de exógena y renta casi sin esfuerzo adicional.

## Errores comunes (casos reales FYT)

- Cruzar contra **saldos acumulados** en clientes con año sin cerrar (regla D.5) → diferencias fantasma. Usar movimientos del periodo.
- No excluir "SALDO INICIAL" del auxiliar → infla la contabilidad.
- Olvidar sumar los **DSEL** a las compras → compras contables "sobran" frente al token.
- Comparar ventas token **brutas** (sin restar NC) contra contabilidad neta.
- Dar por "explicada de palabra" una diferencia material sin documento: toda diferencia cerrada queda con causa escrita en la hoja Diferencias.

## Checklist de calidad

- [ ] Token depurado según Aux 20 antes de cruzar.
- [ ] Auxiliar del MISMO periodo, por movimientos, sin filas SALDO INICIAL.
- [ ] Cruce de totales por rubro + cruce documento a documento de las diferencias.
- [ ] Cada diferencia tipificada con causa y acción en la hoja Diferencias.
- [ ] Ninguna diferencia material (≥ 1 UVT individual o ≥ 0,5 % acumulada) abierta al cierre.
- [ ] Hallazgos graves (ventas sin facturar, declaraciones afectadas) escalados al Contador Titular.
- [ ] Papel de trabajo archivado en la carpeta del cliente con fecha y responsable.

## Relacionado

- Lección anterior: [[Aux 20 - Interpretacion del Token DIAN]] · Lección siguiente: [[Aux 22 - Conciliacion Bancaria]]
- [[Aux 09 - Notas Credito y Debito]] · [[Aux 23 - Balance de Prueba y Libro Auxiliar]]
- [[Protocolo IVA Formulario 300]] · *Lecciones Aprendidas Exogena*
- Agentes: [[04-AuxiliarFacturacionElectronica-Senior]] · [[02-AuxiliarContable-Senior]]
- Casos: **Cliente - EMPRESA CON SOCIO EXTRANJERO C** · **Cliente - SALÓN DE BELLEZA I**
- [[MOC - Escuela Auxiliar Contable]]
