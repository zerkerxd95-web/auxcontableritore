---
tipo: leccion
tags: [ritore, escuela, auxiliar, cierre]
modulo: 7
estado: vigente
fecha: 2026-06-08
---

# Aux 24 - Cierre Contable Mensual

## Objetivo

Que el auxiliar ejecute el cierre mensual completo de un cliente siguiendo el checklist de la firma, deje la contabilidad cuadrada contra el Token DIAN, los bancos y los impuestos del periodo, y entregue el **paquete de cierre mensual** a tiempo. El cierre mensual disciplinado es lo que hace que el cierre anual, la exógena y la renta sean trámites y no rescates.

## Marco conceptual y normativo

- El cierre mensual NO es un asiento: es un **proceso de verificación** que deja cada módulo (facturación, nómina, bancos, impuestos, terceros) conciliado con su fuente de verdad.
- El ritmo lo marca el *01-Orquestador-Master*: cada cliente tiene su calendario de cierre y sus dependencias (no se liquida IVA sin token causado; no se emiten EEFF sin bancos conciliados).
- Los saldos que se "congelan" en el cierre alimentan directamente: F-300 (2408), F-350 (2365), EEFF mensuales y, al final del año, la exógena (regla C.2).

## Paso a paso — checklist de cierre

Ejecutar EN ORDEN; cada punto depende de los anteriores:

| # | Verificación | Cómo se valida | Lección |
|---|--------------|----------------|---------|
| 1 | **Todas las facturas del token causadas** (emitidas, recibidas, NC/ND, DSEL) | Cruce token vs contabilidad sin diferencias materiales | [[Aux 20 - Interpretacion del Token DIAN]] · [[Aux 21 - Cruce Token vs Contabilidad]] |
| 2 | **Nómina y provisiones registradas** | Nómina causada = nómina electrónica transmitida; provisiones de prestaciones del mes al día | [[Aux 11 - Causacion de Nomina]] · [[Aux 12 - Provisiones y Prestaciones Sociales]] · [[Aux 13 - Nomina Electronica y Documento Soporte de Pago]] |
| 3 | **Depreciaciones del mes** | Asiento de depreciación corrido para todos los activos fijos activos | — |
| 4 | **Conciliaciones bancarias hechas** (todas las cuentas y pasarelas) | Diferencia final = 0; GMF y comisiones causados | [[Aux 22 - Conciliacion Bancaria]] |
| 5 | **Retenciones cuadradas** | Saldo/movimiento de 2365 del periodo = F-350 del periodo (o proyectado) | [[Aux 14 - Calculo de Retenciones]] |
| 6 | **IVA cuadrado** | Movimientos 240801/240802 = F-300 proyectado del periodo, cruzados contra el token | [[Aux 15 - IVA y Prorrateo]] |
| 7 | **Terceros depurados** | Sin movimientos sin NIT, sin terceros genéricos, sin duplicados | [[Aux 03 - Terceros y RUT]] |
| 8 | **Balance de prueba revisado** | Ecuación cuadrada; sin saldos de naturaleza contraria nuevos sin explicar | [[Aux 23 - Balance de Prueba y Libro Auxiliar]] |

Reglas transversales durante todo el cierre:

- Trabajar por **movimientos del periodo** y excluir "SALDO INICIAL" (reglas C.2 y D.5).
- Toda diferencia material (≥ 1 UVT individual o ≥ 0,5 % del rubro) se resuelve o se escala ANTES de cerrar — nunca se maquilla (C.8/D.10).
- Lo que quede pendiente (factura en disputa, partida bancaria envejecida) se documenta con responsable y fecha esperada.

## Entregable: paquete de cierre mensual

```
📁 Cierre_[Cliente]_[AAAA-MM]/
   ├── 01_Cruce_Token_vs_Contabilidad.xlsx     (hojas: Compras DIAN, Ventas DIAN, Cruce, Diferencias)
   ├── 02_Conciliaciones_Bancarias.xlsx        (una hoja por cuenta/pasarela)
   ├── 03_Cuadre_Impuestos.xlsx                (2408 vs F-300 proy., 2365 vs F-350)
   ├── 04_Balance_de_Prueba_revisado.xlsx      (banderas comentadas)
   ├── 05_EEFF_mensuales.xlsx                  (ESF + ER del mes y acumulado)
   └── 06_Notas_y_pendientes.md                (hallazgos, pendientes, responsables)
```

**Caso real de ritmo:** **Cliente - COMERCIO DE BICICLETAS A** recibe **EEFF mensuales antes del día 10** del mes siguiente. Eso obliga a tener el token causado y los bancos/pasarelas (Addi, Agaval, Plin) conciliados en la primera semana — el cierre no espera al fin de mes siguiente.

## Errores comunes (casos reales FYT)

- Emitir EEFF con el token sin causar completo → ingresos/costos subestimados (caso la titular de la FLORISTERÍA Y: $23,7M sin contabilizar — el cruce del paso 1 lo habría detectado de inmediato).
- Cerrar sin conciliar pasarelas de pago "porque no son bancos" (COMERCIO DE BICICLETAS A: Addi/Agaval/Plin son efectivo en tránsito).
- Cuadrar el IVA contra el saldo acumulado de 2408 en clientes con año sin cerrar (D.5) → usar movimientos del periodo.
- Dejar terceros genéricos "por afán de cerrar" (**Cliente - EMPRESA H**) → la exógena del año siguiente lo cobra con intereses.
- Saltarse el orden del checklist (liquidar IVA antes de causar el token completo).
- No documentar los pendientes → el mes siguiente nadie sabe qué quedó abierto (usar `06_Notas_y_pendientes.md`, mismo espíritu de la regla C.9 de continuidad).

## Checklist de calidad

- [ ] Los 8 puntos del checklist ejecutados EN ORDEN y con evidencia.
- [ ] Cruce token vs contabilidad sin diferencias materiales abiertas.
- [ ] Todas las cuentas bancarias Y pasarelas conciliadas a cero.
- [ ] 2365 = F-350 y 2408 = F-300 proyectado (por movimientos del periodo).
- [ ] BP sin banderas nuevas sin explicar; terceros depurados.
- [ ] Paquete de cierre completo y archivado en la carpeta canónica del cliente.
- [ ] EEFF entregados dentro del plazo pactado con el cliente (p. ej. día 10).
- [ ] Pendientes documentados con responsable y fecha.

## Relacionado

- Lección anterior: [[Aux 23 - Balance de Prueba y Libro Auxiliar]] · Lección siguiente: [[Aux 25 - Cierre Anual y Errores Comunes]]
- [[Aux 11 - Causacion de Nomina]] · [[Aux 12 - Provisiones y Prestaciones Sociales]] · [[Aux 14 - Calculo de Retenciones]] · [[Aux 15 - IVA y Prorrateo]]
- [[Protocolo IVA Formulario 300]] · *Lecciones Aprendidas Exogena*
- Agentes: *01-Orquestador-Master* · [[02-AuxiliarContable-Senior]] · [[04-AuxiliarFacturacionElectronica-Senior]]
- Casos: **Cliente - COMERCIO DE BICICLETAS A** · **Cliente - EMPRESA H**
- [[MOC - Escuela Auxiliar Contable]]
