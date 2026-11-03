---
tipo: conocimiento
tags: [ritore, exogena, herramientas]
estado: vigente
fecha: 2026-06-07
---

# Manejo de Archivos Excel Corruptos (regla C.1)

Esta regla evita ~50 % del retrabajo en campañas de exógena e IVA.

## Síntoma

`BadZipFile: File is not a zip file` o `KeyError: There is no item named 'xl/sharedStrings.xml' in the archive` al leer un .xlsx.

## Causa

Los .xlsx en carpetas sincronizadas (**OneDrive/Drive**) se corrompen o truncan mientras están abiertos en Excel o mientras se sincronizan. El archivo conserva los Local File Headers (`PK\x03\x04`) pero pierde el Central Directory (`PK\x01\x02`) y/o el End of Central Directory (`PK\x05\x06`).

## Protocolo

1. **NO reintentar en bucle.** Si falla 2 veces, pasar a recuperación manual.
2. **Pedir al usuario** que cierre el archivo en Excel o haga **"Guardar como" con nombre nuevo** (fuerza escritura completa desde cero).
3. **Verificar integridad** a nivel binario: el archivo debe empezar con `PK` y terminar con la firma EOCD `PK\x05\x06`. Sin esa firma está truncado.
4. **Verificar el contenido:** antes de procesar un libro auxiliar, confirmar que total débitos = total créditos (el aux contable SIEMPRE cuadra).
5. Al generar archivos propios, regenerar con timestamp nuevo si el usuario los abre.

## Recuperación manual (validada en campaña 2026)

Existe una función Python `recover_xlsx` que parsea los Local File Headers manualmente, descomprime cada entrada con zlib y reempaca el zip, agregando un `sharedStrings.xml` vacío si falta. Código completo en `EXOGENAS 2026/MEJORAS_SKILL_EXOGENA_2026.md`, sección 9.

Advertencias:
- Si la recuperación pierde hojas críticas → pedir al cliente una versión nueva del archivo.
- Verificar siempre las celdas string después de recuperar: sin sharedStrings, los strings referenciados (`t="s"`) quedan vacíos.

## Relacionado

- *Lecciones Aprendidas Exogena*
- *Subskill B3 - Consolidar Insumos* · [[Protocolo IVA Formulario 300]]
- *14-EspecialistaExogena-Master* · *Proyecto - Exogena 2026* · *MOC - Conocimiento Tecnico*
