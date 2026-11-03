---
tipo: conocimiento
tags: [ritore, exogena, calidad]
estado: vigente
fecha: 2026-06-07
---

# Margen de Error < 2 % — Umbral de Bloqueo

El **2 % no es una aspiración: es un umbral de bloqueo**. La *Skill Maestra - Desarrollar Informacion Exogena Completa* está diseñada para NO presentar si el control de calidad (*Subskill B8 - Control Calidad 2pct*) mide un error superior. En la práctica, con insumos conciliados + cruces + prevalidador + firma humana, el error esperado queda muy por debajo del 2 %.

## Cómo se mide

- **Muestreo:** revisión manual del 2 % de registros de mayor valor + 1 % aleatorio.
- **Error estimado = registros con hallazgo / registros revisados.**
- Si > 2 % → NO avanza: regresa a depuración (*Subskill B5 - Depurar Terceros y Cuantias Menores* / *Subskill B6 - Generar Formato XML*) hasta bajar del umbral.
- KPI post-presentación: (registros con error detectado) / (registros totales) < 2 %.

## Mecanismos que garantizan el margen (B.13)

| Mecanismo | Cómo reduce el error |
|-----------|----------------------|
| **Insumos pre-conciliados (B-3)** | No se construye sobre datos crudos; cada insumo viene cuadrado en su origen |
| **Mapeo trazable (B-4)** | Cada peso tiene camino documentado cuenta→formato→concepto; no hay asignaciones "a ojo" |
| **Depuración de terceros (B-5)** | NITs validados con dígito de verificación; cuantías menores agrupadas por regla |
| **Conciliación cruzada (B-7)** | La exógena se cuadra contra IVA, Retención y Renta ANTES de presentar — los mismos cruces que hará la DIAN |
| **Control de calidad muestral (B-8)** | Medición objetiva con umbral duro de 2 %; si se supera, no avanza |
| **Prevalidador (B-9)** | Validación técnica oficial; cero advertencias antes de presentar |
| **Aprobación humana (B-10)** | El Contador Titular es la última barrera de control |
| **Aprendizaje (B-12)** | Cada error encontrado mejora la matriz y los controles del año siguiente |

## Umbral de materialidad asociado

La skill maestra no avanza al siguiente paso si el anterior dejó una inconsistencia material sin resolver: **cualquier diferencia individual ≥ 1 UVT o acumulada ≥ 0,5 % del total del formato** — ver *Conciliacion Exogena vs Declaraciones*.

## Relacionado

- *Skill Maestra - Desarrollar Informacion Exogena Completa* · *Subskill B8 - Control Calidad 2pct*
- *Conciliacion Exogena vs Declaraciones* · *Sancion Art 651 ET* · [[UVT y Topes]]
- *Protocolo de Razonamiento 10 Pasos* · *Lecciones Aprendidas Exogena*
- *14-EspecialistaExogena-Master* · *MOC - Conocimiento Tecnico*
