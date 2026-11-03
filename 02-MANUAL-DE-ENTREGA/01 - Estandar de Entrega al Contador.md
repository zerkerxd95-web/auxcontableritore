---
tipo: estandar
tags: [ritore, auxiliar, entrega, estandar]
estado: vigente
version: 1.0
fecha: 2026-11-03
---

# 01 · Estándar de entrega al contador

> **La regla madre.** El auxiliar no entrega "la contabilidad digitada": entrega **un período cerrado y demostrado**. Cuando el contador abre la carpeta del mes debe poder revisar, firmar y presentar **sin preguntarle nada al auxiliar**. Si para entender la entrega hace falta una llamada, la entrega está incompleta.

## 1. Quién hace qué (separación de funciones)

| El auxiliar | El contador |
|---|---|
| Recibe y archiva los insumos tal como llegan | Revisa la entrega con el control de cuatro ojos |
| Digita la causación rutinaria que tiene soporte | Aprueba o rechaza los **asientos propuestos** (ajustes, reclasificaciones, criterios) |
| Concilia bancos, pasarelas, cartera, proveedores, impuestos y nómina | Decide los criterios y lo material (≥ 50 UVT, cambios de política, zonas grises) |
| Cruza el token DIAN documento por documento | Firma y presenta declaraciones; firma estados financieros |
| Prepara los **borradores** de F-350, F-300, ReteICA y F-2593 | Responde a la DIAN y al cliente en lo técnico |
| Arma el paquete de entrega y lo revisa con `revisar_entrega.py` | Devuelve observaciones por escrito en `04-TRAZAS/` |
| Documenta todo lo pendiente con responsable y fecha | Prioriza qué se presenta con la información disponible |

**Lo que el auxiliar nunca hace:** firmar, presentar, enviar algo a la DIAN o al cliente sin aprobación, crear cuentas contables, decidir un criterio que no está en la ficha del cliente, o "cuadrar" una diferencia con una cuenta puente sin nombre.

## 2. La carpeta del período (una sola, siempre igual)

```
<CLIENTE>/
├── _cliente.yaml                 ← criterios y obligaciones del cliente (lo mantiene el contador)
└── <AAAA-MM>/                    ← un período = una carpeta
    ├── ENTREGA.md                ← resumen de una página para el contador (plantilla en plantillas/)
    ├── 01-INSUMOS/               ← tal como llegaron. NUNCA se editan.
    │   ├── TOKEN_<AAAA-MM>.xlsx
    │   ├── EXTRACTO_<BANCO>_<ULT4>_<AAAA-MM>.pdf     (uno por cuenta y por pasarela)
    │   ├── BP_<AAAA-MM>_S.xlsx    y/o  BP_<AAAA-MM>_W.xlsx      (balance de prueba)
    │   ├── AUX_<AAAA-MM>_S.xlsx   y/o  AUX_<AAAA-MM>_W.xlsx     (libro auxiliar)
    │   ├── BPT_<AAAA-MM>.xlsx                                   (balance por tercero)
    │   ├── NOMINA_NOVEDADES_<AAAA-MM>.xlsx · PILA_<AAAA-MM>.pdf
    │   └── SOPORTES/              (facturas no electrónicas, contratos, recibos de caja menor)
    ├── 02-PROCESADO/             ← los papeles de trabajo del auxiliar
    │   ├── 01_CRUCE_TOKEN_<AAAA-MM>.xlsx
    │   ├── 02_CONCILIACIONES_<AAAA-MM>.xlsx          (una hoja por cuenta y por pasarela)
    │   ├── 03_CARTERA_Y_PROVEEDORES_<AAAA-MM>.xlsx
    │   ├── 04_CUADRE_IMPUESTOS_<AAAA-MM>.xlsx        (2365↔F-350, 2408↔F-300, 2368↔ReteICA, 1355↔sufridas)
    │   ├── 05_NOMINA_<AAAA-MM>.xlsx                  (nómina↔electrónica↔PILA↔banco)
    │   └── 06_BP_REVISADO_<AAAA-MM>.xlsx             (banderas comentadas)
    ├── 03-SALIDA/                ← lo que el contador revisa para firmar o presentar
    │   ├── ASIENTOS_PROPUESTOS_<AAAA-MM>.xlsx        (hoja única 02 ASIENTOS)
    │   ├── BORRADOR F-350 <MES AAAA>.html            (y F-300 / ReteICA / F-2593 si vencen)
    │   └── EEFF_<AAAA-MM>.xlsx                       (solo si el cliente tiene EEFF mensuales pactados)
    └── 04-TRAZAS/                ← memoria del período
        ├── NOTAS-Y-PENDIENTES.md
        ├── TABLA-DE-DIFERENCIAS.md
        ├── REGISTRO-DE-CORRIDAS.md                   (qué se rehízo, cuándo y por qué)
        └── OBSERVACIONES-DEL-CONTADOR.md             (las escribe el contador; el auxiliar responde debajo)
```

Reglas que no se discuten:

1. **`01-INSUMOS/` es intocable.** Si un insumo está mal, se corrige en el origen (software, banco, cliente) y se vuelve a exportar.
2. **Un archivo vive en un solo lugar.** Se referencia, no se copia.
3. **Prohibidos los sufijos** `v2`, `final`, `FINAL`, `(LIMPIA)`, `copia`, `nuevo`. La versión anterior va a `04-TRAZAS/` con una línea en `REGISTRO-DE-CORRIDAS.md`.
4. **Nombres en MAYÚSCULAS, sin tildes ni caracteres raros**, con el período `AAAA-MM`. El nombre del cliente no va en el archivo: ya está en la carpeta.
5. La estructura `01 · 02 · 03 · 04` es la misma que usa el contador en su repositorio. En el paquete comercial RITORE OS la carpeta `02` se llama `02-TRABAJO`; es la misma.

## 3. Lo mínimo que debe traer una entrega (si falta uno, no se entrega)

| # | Área | Evidencia obligatoria | Criterio de "cerrado" |
|---|---|---|---|
| 1 | **Token DIAN** | `01_CRUCE_TOKEN` con cruce por folio en los dos sentidos | Toda factura emitida, recibida, nota y documento soporte del mes está causada; diferencias por documento ≤ $200 o explicadas |
| 2 | **Bancos y pasarelas** | `02_CONCILIACIONES`, una hoja por cuenta, en formato contable | Saldo en libros + partidas = saldo del extracto, **diferencia CERO**; GMF y comisiones causados |
| 3 | **Cartera** | `03_CARTERA_Y_PROVEEDORES` hoja clientes | Saldo por tercero sin naturaleza contraria sin explicar; recaudos cruzados contra facturas (1-a-N) |
| 4 | **Proveedores y CxP** | misma, hoja proveedores | Pagos cruzados contra facturas; anticipos identificados |
| 5 | **Impuestos** | `04_CUADRE_IMPUESTOS` | 2365 del mes = borrador F-350 por concepto; 2408 = borrador F-300 si cierra período; ReteICA y autorretención calculadas |
| 6 | **Nómina** | `05_NOMINA` | Nómina causada = nómina electrónica = PILA = dispersión del banco |
| 7 | **Costos, gastos, activos** | en `06_BP_REVISADO` | Depreciaciones y amortizaciones del mes corridas; gastos con soporte y tercero real |
| 8 | **Balance de prueba** | `06_BP_REVISADO` | Débitos = créditos; sin saldos contrarios a la naturaleza nuevos sin explicar; terceros depurados |
| + | **Pendientes** | `NOTAS-Y-PENDIENTES.md` | Cada pendiente con valor, responsable y fecha |
| + | **Resumen** | `ENTREGA.md` | Semáforo de las 8 áreas y lista de decisiones para el contador |

El criterio de las ocho áreas viene de la regla de **garantía de cierre** de la firma: si al digitar los asientos propuestos la contabilidad no queda conciliada mes a mes, el trabajo no está terminado (ver `03-REGLAS-DE-LA-CASA/regla-auditoria-garantia-de-cierre.md`).

## 4. Umbrales (fuente única, no inventar otros)

| Concepto | Umbral | Qué hace el auxiliar |
|---|---|---|
| Diferencia material | ≥ 1 UVT por partida o ≥ 0,5 % del total del rubro | Investiga y deja fila en `TABLA-DE-DIFERENCIAS.md` antes de entregar |
| Diferencia crítica | ≥ 50 UVT | La marca en rojo en `ENTREGA.md` y la sube como decisión del contador |
| Diferencia mayor | ≥ 500 UVT | Avisa al contador el mismo día, sin esperar la entrega |
| Diferencia de cruce token | hasta $200 por documento | Se acepta como redondeo; más de $200 se explica |
| Insumo faltante | 24 h hábiles | Reitera una vez al cliente; luego lo escala al contador |

La UVT del año está en `05-CONOCIMIENTO/normativa/VALORES-VIGENTES.md`. Nunca de memoria.

## 5. Asientos: cuáles se digitan y cuáles se proponen

- **Se digitan directamente** (con soporte): causación de facturas de venta y compra del token, recibos de caja, egresos, notas crédito y débito, nómina del período, provisiones mensuales, depreciaciones, GMF y comisiones del extracto.
- **Se proponen** en `ASIENTOS_PROPUESTOS_<AAAA-MM>.xlsx` (una sola hoja, `02 ASIENTOS`) y no se registran hasta que el contador los aprueba: reclasificaciones, corrección de errores de meses anteriores, ajustes por criterio, castigos, cruces de anticipos, todo lo que toque cuentas de socios, patrimonio o impuestos ya declarados.

Columnas obligatorias de la hoja de asientos propuestos:
`N° · MES · COMPROBANTE · FECHA · CUENTA · NOMBRE CUENTA · TERCERO (NIT) · DÉBITO · CRÉDITO · QUÉ REGISTRA · SOPORTE`. Cada comprobante cuadra por separado; la hoja cuadra en total; las cuentas son **del plan de cuentas existente del cliente**. Asientos netos: una cuenta no se debita y se acredita en el mismo comprobante.

## 6. Cómo se entrega

1. Corre `python herramientas/revisar_entrega.py "<ruta>/<CLIENTE>/<AAAA-MM>"` y corrige todo lo que salga en rojo.
2. Completa `ENTREGA.md` (plantilla en `plantillas/ENTREGA.md`).
3. Avisa al contador por el canal de la firma con **una línea**: `Entrega <CLIENTE> <AAAA-MM> lista · semáforo: <verde/ámbar/rojo> · <n> decisiones para ti · vence <fecha>`.
4. Las observaciones vuelven en `04-TRAZAS/OBSERVACIONES-DEL-CONTADOR.md`. Se corrigen **en el software contable**, se re-exporta y se rehace lo afectado. Nunca se corrige a mano una salida.

## Relacionado

- [[02 - Calendario de Cierre Mensual]] · [[03 - Checklist de Cierre Mensual]] · [[09 - Pendientes Hallazgos y Comunicacion]]
- [[Aux 24 - Cierre Contable Mensual]] · [[Sistema de Control de Calidad de la Firma]] · [[ESTRUCTURA-DE-CARPETAS]]

## Historial de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-11-03 | Versión inicial: separación de funciones, carpeta del período, ocho áreas, umbrales y protocolo de entrega |
