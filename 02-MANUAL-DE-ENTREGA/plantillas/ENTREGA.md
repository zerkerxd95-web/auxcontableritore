# ENTREGA · {{CLIENTE}} · {{PERIODO}}

| | |
|---|---|
| **Cliente / NIT** | {{CLIENTE}} · {{NIT}} |
| **Período** | {{PERIODO}} |
| **Preparó** | {{AUXILIAR}} · {{FECHA_ENTREGA}} |
| **Vencimientos del mes** | F-350: ____ · F-300: ____ · ReteICA: ____ · F-2593: ____ |
| **Revisa y firma** | Contador(a) Titular · T.P. ________ |

## 1. Semáforo de las ocho áreas

| # | Área | Estado | Evidencia | Comentario |
|---|---|---|---|---|
| 1 | Token DIAN (causación completa) | 🟢 / 🟡 / 🔴 | `02-PROCESADO/01_CRUCE_TOKEN_{{PERIODO}}.xlsx` | |
| 2 | Bancos y pasarelas | | `02_CONCILIACIONES_{{PERIODO}}.xlsx` | |
| 3 | Cartera | | `03_CARTERA_Y_PROVEEDORES_{{PERIODO}}.xlsx` | |
| 4 | Proveedores y CxP | | ídem | |
| 5 | Impuestos | | `04_CUADRE_IMPUESTOS_{{PERIODO}}.xlsx` | |
| 6 | Nómina | | `05_NOMINA_{{PERIODO}}.xlsx` | |
| 7 | Costos, gastos y activos | | `06_BP_REVISADO_{{PERIODO}}.xlsx` | |
| 8 | Balance de prueba y terceros | | ídem | |

🟢 cerrada · 🟡 cerrada con un pendiente menor documentado · 🔴 no cerrada (explicar por qué)

## 2. Cifras clave del mes

| Concepto | Token DIAN | Libros | Diferencia |
|---|---|---|---|
| Ingresos (ventas brutas) | | | |
| IVA generado | | | |
| Compras y gastos con factura | | | |
| IVA descontable | | | |
| Retención en la fuente a declarar (F-350) | — | | |
| Autorretención | | | |
| Saldo de bancos conciliado | — | | (extracto) |

## 3. Decisiones para el contador

1. **…** — Opción que recomiendo: … · Efecto: $ …
2. **…**

## 4. Lo que falta del cliente

| Qué | Valor | Pedido el | Vence |
|---|---|---|---|
| | | | |

## 5. Archivos de la entrega

- `03-SALIDA/ASIENTOS_PROPUESTOS_{{PERIODO}}.xlsx` — n asientos, n comprobantes, cuadra: sí/no
- `03-SALIDA/BORRADOR F-350 ….html`
- `04-TRAZAS/NOTAS-Y-PENDIENTES.md` · `TABLA-DE-DIFERENCIAS.md` · `REGISTRO-DE-CORRIDAS.md`
- Resultado de `revisar_entrega.py`: sin rojos / con observaciones (explicar)
