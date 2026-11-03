---
tipo: conocimiento
tags: [ritore, conocimiento, calidad, control-interno]
estado: vigente
fecha: 2026-06-08
---

# Checklist de Revisión antes de Firmar

Control operativo de los **"cuatro ojos"** del [[Sistema de Control de Calidad de la Firma]]: las listas de verificación que el **revisor de calidad** (independiente del preparador) corre ANTES de que el Contador Titular firme. Materializa el **Paso 8** del [[Protocolo Elaboracion de Impuestos]] ("Revisión y FIRMA del Contador Titular").

> **Regla:** el checklist lo corre quien NO preparó el entregable. Se marca ítem por ítem, se firma digitalmente y se archiva como papel de trabajo ([[Gestion de Papeles de Trabajo y Archivo]]). Un ítem en ❌ **detiene** la firma.

## Quién revisa qué

| Entregable | Prepara | Revisa (independiente) | Firma |
|---|---|---|---|
| Declaración de impuestos | Aux / especialista del impuesto | Otro contador de la firma | Contador Titular |
| Estados financieros | Aux contable / *16-EstadosFinancieros-Senior* | Contador distinto | Contador Titular (y Revisor Fiscal si aplica, *19-RevisorFiscal-Senior*) |
| Exógena | *14-EspecialistaExogena-Master* | Otro contador | Contador Titular |
| Nómina | [[07-AuxiliarNomina-Senior]] | Contador / revisor de nómina | Contador Titular |

`[VERIFICAR]` los números de agente de EEFF y Nómina contra *el índice de agentes* si cambia la numeración.

## Ítems transversales (aplican a TODO entregable)

- [ ] **Identidad del insumo:** NIT y razón social DENTRO de cada archivo corresponden al cliente (un archivo mal rotulado es error grave).
- [ ] **Vigencia normativa:** formulario, versión, tarifas, **UVT del año/periodo correcto** (nunca de otro año).
- [ ] **Auxiliar cuadra** débitos = créditos; se trabajó por movimientos del periodo, excluyendo "SALDO INICIAL" (reglas C.1/C.2/D.5).
- [ ] **Rastreabilidad:** cada cifra del entregable amarra con el papel de trabajo y este con su origen (token DIAN o cuenta).
- [ ] **Diferencias materiales resueltas:** toda diferencia ≥ 1 UVT individual o ≥ 0,5 % del total está investigada, documentada y cerrada (no "explicada de palabra").
- [ ] **Cero maquillaje:** ninguna diferencia se forzó; los errores contables se corrigieron en la contabilidad (C.8/D.10).
- [ ] **Hallazgos** listados con severidad y plan de acción; lo que toca a una declaración ya presentada está escalado al Titular.
- [ ] **Convención de nombres** y archivo del entregable correctos.

## (a) Declaración de impuestos

Aplica a F-300 (IVA), F-350 (retención), F-2593/F-260 (RST), F-110 (renta PJ), F-210 (renta PN), ICA. Ver el protocolo del impuesto correspondiente.

- [ ] **Cuadres internos:** el papel de trabajo (totales de control) amarra con el formulario **casilla por casilla**.
- [ ] **Desglose base/impuesto:** se desglosó `Base = Total − Impuesto`; **sin tarifas planas** (no 19 % plano en IVA; nada de tarifa 21 % inexistente).
- [ ] **Casillas críticas según el formulario:**
  - F-300: casillas de compras **50-57 llevan la BASE sin IVA** (regla D.4); reteIVA y saldo a favor anterior solo si se arrastra por instrucción del cliente.
  - F-350: total retenciones ↔ movimiento 2365 del periodo (crédito − débito por tercero, **sin cierres a nombre de la DIAN**); reteIVA 2367, reteICA 2368; separación PJ/PN.
  - F-110: ingresos ↔ F-1007/exógena; costos y deducciones ↔ F-1001; patrimonio; TTD; conciliación 2516 → F-110.
- [ ] **Cruces contra fuentes:** Token DIAN ↔ contabilidad; ingresos ↔ facturación electrónica; los cruces son los mismos que hará la DIAN (ver *Conciliacion Exogena vs Declaraciones*).
- [ ] **Soportes:** costos/deducciones/IVA descontable con factura válida (Art. 617/771-2 ET) y bancarización donde aplique (771-5).
- [ ] **Pago:** en retención, **pago total** o la declaración es ineficaz (Art. 580-1 ET); F-490 listo.
- [ ] **Margen:** se presenta con ≥ 2 días hábiles antes del vencimiento, no el último día.
- [ ] **Firma** del Contador Titular obtenida antes de presentar.
- Protocolos: [[Protocolo IVA Formulario 300]] · [[Protocolo Retencion en la Fuente F-350]] · *Protocolo Renta Persona Juridica F-110* · *Protocolo Renta Persona Natural F-210* · [[Protocolo Anticipo Simple F-2593]] · *Protocolo Declaracion Anual Simple F-260*.

## (b) Estados financieros (NIIF)

- [ ] **Marco aplicado correcto:** NIIF para PYMES (Grupo 2) o NIIF Plenas (Grupo 1) según el cliente (*NIIF PYMES - Secciones Clave* / *NIIF Plenas - Normas Clave*).
- [ ] **Ecuación contable:** **Activo = Pasivo + Patrimonio** (ESF cuadra); el Estado de Resultados cierra contra el patrimonio (utilidad/pérdida del ejercicio).
- [ ] **Año anterior cerrado:** resultados del ejercicio reclasificados a acumulados; sin saldos antiguos arrastrados (patrón recurrente D.5 — [[Aux 25 - Cierre Anual y Errores Comunes]]).
- [ ] **Conciliaciones soporte:** bancos = 0, cartera, proveedores, terceros depurados, impuestos (2365/2408) cuadrados ([[Aux 24 - Cierre Contable Mensual]]).
- [ ] **Ajustes de cierre corridos:** depreciaciones, provisiones de prestaciones, inventarios, deterioros, diferencia en cambio.
- [ ] **Notas a los EEFF** completas y consistentes con las cifras (políticas, desgloses, hechos posteriores).
- [ ] **Comparativo** con el periodo anterior presentado y coherente.
- [ ] **Revisor Fiscal:** si el cliente está obligado, dictamen/opinión gestionada (*Revisoria Fiscal - Marco y Obligados*).

## (c) Exógena (información tributaria)

- [ ] **Prevalidador DIAN limpio:** cada formato pasó **sin errores ni advertencias** sin resolver.
- [ ] **Versión y resolución vigentes** confirmadas para el año gravable (no por inercia del año anterior).
- [ ] **Fuente correcta por formato** (regla C.2): movimiento (1001/1005/1006/1007/2276) → auxiliar por tercero; saldo (1008/1009/1012) → BP por tercero.
- [ ] **Cuantías menores** agrupadas por la regla (3 UVT en 1001; 12 UVT en 1007/1008/1009) sin esconder terceros que SÍ superan el tope; terceros del exterior NUNCA en cuantías menores ([[Cuantias Menores 3 UVT]]).
- [ ] **Terceros depurados:** NIT con dígito de verificación válido, tipo de documento correcto (13 vs 31; 42 exterior + país), sin duplicados, direcciones reales para PJ.
- [ ] **Mapeo cuenta→formato→concepto** trazable, sin "cajón de sastre" injustificado en el 5016.
- [ ] **Conciliación cruzada cerrada:** 1007↔ingresos, 1001↔costos/deducciones y F-350, 1005/1006↔F-300, 1008/1009↔patrimonio/pasivo, 1010↔patrimonio/SAGRLAFT (ver *Conciliacion Exogena vs Declaraciones*).
- [ ] **Llaves únicas** respetadas (sin registros duplicados).
- [ ] **Muestreo de calidad** ejecutado: error medido < 2 % ([[Margen de Error 2 por ciento]]).
- Formatos: *Formato 1001 - Pagos y Retenciones* · *Formato 1003 - Retenciones que le practicaron* · *Formato 1005 y 1006 - IVA* · *Formato 1008 y 1009 - CxC y CxP* · *Formato 1010 - Socios y Accionistas* · *Formato 2276 - Rentas de Trabajo*.

## (d) Nómina

- [ ] **IBC correcto** por trabajador (incluye/excluye conceptos según ley; tope 25 SMMLV; factor prestacional).
- [ ] **Aportes a seguridad social** liquidados sobre el IBC: salud, pensión, riesgos laborales (clase de riesgo correcta) y **parafiscales** (SENA, ICBF, Caja) donde apliquen (exoneración Art. 114-1 ET cuando proceda). `[VERIFICAR]` tarifas vigentes del periodo.
- [ ] **Prestaciones sociales** provisionadas y/o pagadas: cesantías, intereses a las cesantías, prima, vacaciones; cesantías = saldo de 2510/2515 por tercero (criterio de caja confirmado).
- [ ] **Retención en la fuente laboral** (Art. 383/procedimiento 1 o 2) calculada; pagos Art. 383 a PN sin retención van al 2276, no al 1001.
- [ ] **Nómina electrónica** transmitida y validada DIAN = nómina causada.
- [ ] **Cruce con exógena:** conceptos laborales coherentes con F-2276 y excluidos del F-1001 (regla C.3).
- [ ] **PILA** cuadra con la nómina del periodo.

## Cierre del checklist

1. El revisor marca cada ítem (✅ / ❌ / N/A con nota).
2. Si hay ❌ → devuelve al preparador; **no pasa a firma**.
3. Con todo en ✅, el revisor firma digitalmente y entrega al Contador Titular (papel de trabajo + borrador + hallazgos).
4. El Titular revisa, **firma y autoriza** la presentación (Paso 9 del protocolo).
5. El checklist firmado se **archiva** como papel de trabajo del encargo.

## Relacionado

- [[Sistema de Control de Calidad de la Firma]] · [[Gestion de Papeles de Trabajo y Archivo]]
- [[Protocolo Elaboracion de Impuestos]] · *Conciliacion Exogena vs Declaraciones* · [[Margen de Error 2 por ciento]]
- [[Protocolo IVA Formulario 300]] · [[Protocolo Retencion en la Fuente F-350]] · *Protocolo Renta Persona Juridica F-110* · *Protocolo Renta Persona Natural F-210*
- [[Aux 24 - Cierre Contable Mensual]] · [[Aux 25 - Cierre Anual y Errores Comunes]] · *Revisoria Fiscal - Marco y Obligados*
- *MOC - Conocimiento Tecnico*
