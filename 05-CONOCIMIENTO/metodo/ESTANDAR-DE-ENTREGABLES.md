# Estándar de entregables profesionales — la firma de la casa

> **Este archivo se sube a TODOS los proyectos de Claude, junto con el candado de valores.**
> Define cómo debe verse CUALQUIER cosa que el sistema produzca. La regla madre:
> **nada de lo que salga puede parecer una plantilla diligenciada — todo debe leerse
> como el trabajo de un profesional senior que conoce a ESTE cliente.**

---

## Las 7 reglas de todo entregable

1. **Nombre propio, siempre.** Todo documento abre identificando: cliente (razón social y NIT), período, obligación, fecha de elaboración y quién lo prepara/revisa. Nunca "la empresa", "el contribuyente", "el período" a secas.
2. **Cifras con historia.** Cada cifra relevante se acompaña de su origen ("según balance de prueba a jun-30, cuenta 1305") y, si cambió contra el período anterior, del porqué. Un número sin fuente es un número que no existe.
3. **Conclusión con criterio, no descripción.** Todo entregable termina diciendo QUÉ significa y QUÉ se recomienda hacer: "la cartera creció 34% mientras las ventas crecieron 8% — recomendamos revisar la política de crédito antes del próximo cierre", no "la cartera fue de $X".
4. **Lo pendiente se dice de frente.** Sección explícita de "Pendientes y salvedades": qué faltó, qué se asumió, qué debe resolver el cliente. Un entregable sin salvedades documentadas es un entregable que esconde riesgos.
5. **Lenguaje de profesional a cliente.** Sin jerga innecesaria con el gerente (se escribe "impuesto que la empresa retiene a sus proveedores", no solo "retefuente"); con rigor técnico total en los papeles de trabajo internos (ahí sí: artículo, inciso, tarifa, base).
6. **Bloque de responsabilidad.** Todo entregable cierra con: "Preparado por: [sistema + auxiliar] · Revisado y aprobado por: [contador, T.P. xxx]" — y NADA se marca como revisado si el contador no lo revisó de verdad.
7. **Cero texto de relleno.** Prohibidas las frases que delatan plantilla: "es importante mencionar que", "como se puede observar", "en el presente documento". Si una frase no agrega información de ESTE cliente, se borra.

## Los 8 entregables tipo del sistema

### E1 — Papel de trabajo (uso interno, va a 02-TRABAJO)
Encabezado (cliente, período, obligación, preparó/fecha) → objetivo del papel en una línea → fuente de cada insumo con fecha de descarga → desarrollo con fórmulas visibles → tabla de diferencias encontradas con explicación una a una → conclusión y destino ("alimenta el F-350 de julio").

### E2 — Tabla de diferencias / conciliación (el corazón del método)
Columnas fijas: concepto · valor fuente A · valor fuente B · diferencia · % · explicación · acción · estado (RESUELTA/PENDIENTE/ACEPTADA con criterio). **Regla:** ninguna diferencia ≥ 1 UVT o ≥ 0,5% puede quedar sin explicación escrita. Las resueltas dicen CÓMO; las aceptadas dicen POR QUÉ y QUIÉN decidió.

### E3 — Memorando tributario (acompaña toda declaración)
Para: gerencia · De: [contador] · Ref: [obligación y período]. Secciones: 1) Resumen en 5 líneas para no contadores (cuánto se paga, cuándo, por qué esa cifra); 2) Cómo se llegó al valor (depuración resumida); 3) Decisiones de criterio tomadas y su sustento normativo; 4) Riesgos y contingencias con probabilidad (alta/media/baja) e impacto en pesos; 5) Pendientes del cliente con fecha límite. Máximo 2 páginas: si no cabe, el anexo técnico va aparte.

### E4 — Informe gerencial mensual (lo que el cliente paga con gusto)
1 página + anexos. Estructura: cómo le fue al negocio en una frase → 4-6 indicadores con semáforo y comparación (mes anterior y mismo mes del año pasado) → las 3 cosas que la gerencia debe saber (hallazgos con plata: cartera, márgenes, costos que se movieron) → las 2-3 decisiones recomendadas → estado de obligaciones (presentado/pagado/próximos vencimientos) → pendientes del cliente. Los hallazgos nombran cifras y causas de ESTE negocio, jamás frases genéricas.

### E5 — Respuesta a requerimiento (defensa)
Encabezado formal con identificación completa del acto que responde (número, fecha, funcionario, plazo) → antecedentes → respuesta punto por punto EN EL MISMO ORDEN del requerimiento, cada punto con: lo solicitado (cita textual), la respuesta, el soporte que se anexa (numerado) → peticiones finales → anexos foliados. Tono: respetuoso, preciso, sin conceder más de lo preguntado ni agredir. Antes de redactar, la skill SIEMPRE pregunta al contador la estrategia (¿responder, corregir, o ambas?).

### E6 — Certificación / carta con destinatario externo
Papel formal: ciudad y fecha, destinatario, identificación del cliente, objeto, contenido certificado con cifras exactas y su corte, alcance y limitaciones ("esta certificación se expide con base en..."), firma con T.P. Nunca certifica más de lo que los papeles de trabajo soportan.

### E7 — Acta de cierre de campaña (va a 04-TRAZAS)
Qué se presentó (formulario, fecha, número de radicado/acuse), con qué cifras finales, qué diferencias quedaron aceptadas y por qué, qué criterios nuevos se adoptaron (para la ficha del cliente), qué quedó pendiente para la próxima campaña, y lecciones (alimenta la bitácora de mejora).

### E8 — Comunicación al cliente (WhatsApp/correo)
3 partes, siempre: qué pasó o qué se necesita (1-2 líneas) · qué significa para él en plata o riesgo · qué acción concreta se le pide y para cuándo. Sin tecnicismos sin traducir, sin párrafos de cortesía interminables.

## Control de calidad antes de entregar (la skill lo corre SIEMPRE)

- [ ] ¿Identifica cliente, período y obligación en el encabezado?
- [ ] ¿Toda cifra material tiene fuente? ¿Los totales cuadran entre secciones?
- [ ] ¿Usa EXCLUSIVAMENTE los valores del candado (`VALORES-VIGENTES.md`)?
- [ ] ¿Hay conclusión con recomendación, no solo descripción?
- [ ] ¿Las salvedades y pendientes están explícitos?
- [ ] ¿Pasaría la prueba del socio: "si esto lo firmara yo ante la DIAN o ante el gerente, ¿me da tranquilidad?"
- [ ] ¿Cero frases de plantilla?

**Si algún punto falla, el entregable NO sale. Se corrige o se documenta por qué no se pudo.**
