---
tipo: politica
tags: [ritore, politica, confidencialidad, habeas-data, comercializacion]
estado: vigente
fecha: 2026-06-11
---

# Política de Separación de Datos y Confidencialidad

**Documento normativo interno.** La firma quiere **comercializar la metodología** del vault (agentes, skills, plantillas, escuela), pero el vault mezcla esa metodología con **datos de clientes reales**: NITs, cifras financieras, hallazgos, nombres de socios y empleados (130+ apariciones identificadas en la auditoría del 2026-06-11). Esa mezcla expone a la firma a la **Ley 1581 de 2012 (habeas data)**, al secreto profesional del contador (Art. 63 Ley 43/1990) y a la pérdida de confianza de los clientes. Esta política define **qué puede salir del vault y qué jamás**.

> **Principio rector:** la metodología es de la firma y se vende; los datos son del cliente y se protegen. Cuando una nota mezcla ambas cosas, manda la protección.

## 1. Clasificación de la información

Toda nota del vault pertenece a una de dos clases:

| Clase | Qué incluye | Tratamiento |
|---|---|---|
| 🟢 **VERDE** — metodología | Skills y sub-skills, plantillas (de nota y Excel), protocolos y conocimiento técnico, normativa, lecciones de la [[MOC - Escuela Auxiliar Contable]], estándares ([[00 - Estandar de Agentes RITORE]], *00 - Estandar de Skills RITORE*), perfiles de agentes | **Comercializable**, previa anonimización (§2) y checklist de exportación (§4) |
| 🔴 **ROJO** — datos de clientes | TODO lo de `04 - Clientes`, TODO lo de `TRABAJOS Y REQUERIMIENTOS`, y cualquier NIT, cifra, hallazgo, contrato, acta, certificado o nombre de cliente real / persona natural identificable, esté donde esté | **Confidencial. NUNCA sale del vault.** Ni en demos, ni en propuestas, ni en material de venta, ni en capturas de pantalla |

Reglas de aplicación:

- La clasificación es **por contenido, no por carpeta**: una nota VERDE (una skill, una lección de escuela) que cite un NIT o una cifra real contiene material ROJO y no puede exportarse tal cual.
- En caso de duda, la nota se trata como ROJA hasta que el dueño decida.
- Los criterios particulares de cliente (fichas `Cliente - X`, sección "Criterios particulares") son ROJOS por definición; las skills se mantienen genéricas justamente para eso (ver *00 - Estandar de Skills RITORE* §3).

## 2. Regla de anonimización

Los **casos reales** son el mejor material didáctico de las skills, la escuela y las lecciones aprendidas — se conservan, pero **se anonimizan antes de exportar** cualquier material VERDE:

| Dato real | Se reemplaza por |
|---|---|
| Nombre del cliente | Descriptor genérico estable: "Cliente retail A", "Cliente RST B", "Agencia de eventos C" |
| NIT / cédula | Se elimina o se sustituye por un NIT ficticio evidente (`900.000.000-1`) |
| Cifras financieras | Redondeadas o ficticias **proporcionales** (que conserven la relación que enseña la lección) |
| Personas naturales (socios, empleados, contactos) | Rol genérico: "el socio", "la representante legal", "el auxiliar" |
| Rutas de carpetas y nombres de archivo del cliente | Rutas genéricas: `EXTRACTOS/`, `carpeta del mes` |

- La anonimización se hace en una **copia de exportación**; la nota interna del vault conserva el caso real con su trazabilidad.
- Verificar que el caso no sea **re-identificable por contexto** (sector + municipio + cifra única pueden delatar al cliente aunque no haya nombre).

## 3. Regla de credenciales

- Claves, tokens, firmas digitales y credenciales (DIAN, bancos, software contable) **JAMÁS se escriben en el vault** — ni en notas, ni en frontmatter, ni en comentarios.
- Práctica ya vigente que esta política **formaliza**: las credenciales viven en `CLAVES.txt` **fuera del vault** (y de cualquier carpeta sincronizada o exportable junto con él), bajo la [[Politica de Seguridad de la Informacion]].
- Si una credencial aparece en una nota: se elimina de inmediato, se rota la clave y se registra el incidente como lección ([[Plantilla - Leccion Aprendida]]).

## 4. Protocolo de exportación comercial

**Checklist obligatorio** antes de compartir cualquier nota, plantilla, skill o material del vault fuera de la firma (cliente prospecto, comprador, publicación, demo):

- [ ] La nota es **VERDE** (§1) — nada de `04 - Clientes` ni `TRABAJOS Y REQUERIMIENTOS`.
- [ ] **Sin NIT real** (buscar patrones `9XX.XXX.XXX`, `8XX.XXX.XXX` y campos `nit:` del frontmatter).
- [ ] **Sin nombre real de cliente** (razón social, marca, nombre de carpeta fuente).
- [ ] **Sin cifra real** de un cliente (valores de balances, formatos de exógena, pérdidas/utilidades) — solo cifras redondeadas o ficticias proporcionales (§2).
- [ ] **Sin persona natural identificable** (socios, empleados, contactos, contadores que certifican).
- [ ] **Sin credenciales** ni referencias a su ubicación (§3).
- [ ] **Wikilinks resueltos o removidos**: ningún `**Cliente - X**` ni enlace que apunte a material ROJO; los enlaces internos restantes se convierten a texto o se eliminan para que el documento sea autocontenido.
- [ ] Revisión final leyendo el documento **como lo leería un tercero**: ¿puede deducir de quién se habla?

Un solo ítem sin cumplir = **no se exporta**.

## 5. Responsable

- **El dueño aprueba toda exportación** de material del vault fuera de la firma — sin excepciones. Nadie (agente, auxiliar, colaborador) comparte material por iniciativa propia.
- El dueño resuelve los casos dudosos de clasificación (§1) y puede endurecer, nunca relajar, el checklist (§4) para un caso concreto.
- Las violaciones a esta política se registran como lección aprendida y, si involucran datos personales, se evalúan como **incidente de habeas data** (Ley 1581/2012) con la [[Politica de Seguridad de la Informacion]] y el agente *20b-HabeasData-Senior*.

## Relacionado

- *INICIO* · [[Politica de Seguridad de la Informacion]]
- *00 - Estandar de Skills RITORE* · [[00 - Estandar de Agentes RITORE]]
- [[Sistema de Control de Calidad de la Firma]] · *Debida Diligencia y Conocimiento del Cliente*
- *20b-HabeasData-Senior* · *Proyecto - Suite de Plantillas FYT*
- [[Plantilla - Leccion Aprendida]] · [[Bitacora de Aprendizajes]]
