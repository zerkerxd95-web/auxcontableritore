---
tipo: conocimiento
tags: [ritore, conocimiento, calidad, control-interno]
estado: vigente
fecha: 2026-06-08
---

# Gestión de Papeles de Trabajo y Archivo

Sistematiza la **regla C.9** (*Lecciones Aprendidas Exogena*) y la lleva a política de firma: cómo se construye, indexa, archiva, versiona y conserva el papel de trabajo de cada encargo. Es la **evidencia** del [[Sistema de Control de Calidad de la Firma]]: sin papel de trabajo no hay calidad demostrable, y sin trazabilidad no hay firma.

> **Regla de oro:** el papel de trabajo manda. Cada cifra del entregable debe ser rastreable hasta su origen (token DIAN o cuenta contable). **Si no se puede rastrear, no se declara.**

## Qué es un papel de trabajo válido

Un papel de trabajo es la evidencia de que el entregable se construyó con método y se puede reconstruir. Es válido cuando:

1. **Tiene origen identificado:** referencia su fuente (token DIAN del periodo, libro auxiliar, balance de prueba, certificado, extracto) con NIT y razón social del cliente DENTRO del archivo.
2. **Es rastreable:** cada cifra amarra hacia atrás (hasta el soporte) y hacia adelante (hasta la casilla del formulario). Lleva **totales de control** que cuadran casilla por casilla.
3. **Está fechado y atribuido:** se sabe quién lo preparó, quién lo revisó y cuándo.
4. **Documenta los criterios y las diferencias:** criterios particulares del cliente, diferencias materiales y su causa raíz resuelta (no "explicada de palabra").
5. **Es reproducible:** otro contador, con el mismo papel, llega al mismo resultado.

Soportes que respaldan el papel de trabajo: factura válida Art. 617/771-2 ET, documento equivalente, documento soporte a no obligados, validación CUFE/CUDE contra el token. Detalle en [[Aux 04 - Soportes Contables y Papeles de Trabajo]].

## Estructura de carpetas canónica (por cliente / año / obligación)

Sobre la estructura base de [[Aux 04 - Soportes Contables y Papeles de Trabajo]], extendida para las campañas anuales (exógena, renta):

```
📁 [NIT]_[RazonSocial]/
   📁 [Año]/
      📁 [Mes]/
         📁 01_Facturacion/        (Emitidas / Recibidas / NC-ND / DSEL)
         📁 02_Bancos/             (Extractos / Conciliaciones)
         📁 03_Nomina/             (Liquidaciones / PILA / Nomina electronica)
         📁 04_Impuestos/          (Token DIAN / Borrador / Acuse / F-490 / Papel de trabajo)
         📁 05_Soportes_Diversos/
         📁 06_Cierre_Mensual/     (Balance_Prueba / Estado_Resultados / Reporte_Validaciones)
      📁 _Anual/
         📁 Cierre_Anual/          (Asiento de cierre / EEFF / Notas / Acta distribucion)
         📁 Renta/                 (F-110 o F-210 / 2516 o 2517 / papeles / acuse)
         📁 Exogena/               (Un subfolder por formato + AVANCE + acuses + XML)
            📁 1001/ 1003/ 1005/ 1006/ 1007/ 1008/ 1009/ 1010/ 2276/ ...
         AVANCE_EXOGENA_[cliente].md
         AVANCE_RENTA_[cliente].md
```

- Convención de nombres de entregables: `FORMATO [N°] [IMPUESTO] [PERIODO] [CLIENTE] - Claude.xlsx`, `INFORME EJECUTIVO [IMPUESTO] [PERIODO] [CLIENTE] - Claude.docx`.
- La carpeta canónica es **una sola fuente** por cliente; nada se trabaja "suelto" fuera de ella.

## Índice de papeles de trabajo

Cada campaña lleva un **índice** (en el `AVANCE_<obligación>_<cliente>.md`) que lista, por entregable:

| Formato / entregable | Fuente usada | Archivo de trabajo | Valor de control | Estado | Criterios aplicados | Pendientes |
|---|---|---|---|---|---|---|
| 1001 | Auxiliar por tercero | `FORMATO 1001 ...xlsx` | total pagos = $X | ✅ prevalidado | concepto 5007 multi-concepto | — |
| 1007 | Auxiliar por tercero | ... | ingresos = $Y | 🟡 en revisión | reconstruido desde BP | conciliar con F-110 |

El índice permite retomar la sesión sin reconstruir el contexto: **al reiniciar, se lee ANTES de continuar** (regla C.9).

## Archivo del acuse + XML + formato firmado

Al cerrar cada obligación se archiva en la carpeta canónica:

- **Acuse de recibo** de la DIAN (PDF).
- **Archivo presentado:** XML (exógena) / formulario presentado (impuestos) / EEFF firmados.
- **Recibo de pago** F-490 / F-2593 cuando aplique.
- **Papel de trabajo** que sustenta el entregable.
- **Checklist de revisión firmado** ([[Checklist de Revision antes de Firmar]]).

Ninguna obligación se da por cerrada sin el acuse archivado (Paso 10 del [[Protocolo Elaboracion de Impuestos]]).

## Control de versiones

- El **archivo de trabajo vivo** lleva el nombre canónico; las versiones intermedias relevantes se conservan con sufijo de fecha/`vN` cuando hay un cambio material de criterio.
- **Backups `.xlk`** de balances y libros (convención de algunos clientes): **no se borran**, son la red de seguridad del papel de trabajo.
- **Archivos Excel en carpetas sincronizadas (OneDrive/Drive)** se corrompen/truncan abiertos en Excel: ante `BadZipFile`, NO reintentar en bucle — cerrar el archivo o "Guardar como" con nombre nuevo; verificar firma EOCD (`PK\x05\x06`); confirmar débitos = créditos antes de procesar (regla C.1, [[Manejo de Archivos Excel Corruptos]]).

## Copia de seguridad y seguridad de la información

- Backup periódico de la carpeta canónica según el esquema de la firma `[VERIFICAR esquema de backup vigente]`.
- Conservación y acceso bajo la [[Politica de Seguridad de la Informacion]] (control de acceso, confidencialidad, habeas data del titular de los datos).

## Tiempo de conservación

- **Documentos de comercio, libros y sus soportes: mínimo 10 años** — **Art. 28 Ley 962 de 2005**, que modificó el **Art. 60 del Código de Comercio**. `[VERIFICAR vigencia y excepciones cada ciclo]` (coherente con [[Politica de Seguridad de la Informacion]]).
- Papeles de trabajo del contador/revisor fiscal: según la normativa profesional y el marco de aseguramiento (NICC 1) `[VERIFICAR plazo profesional aplicable]`.
- Soportes con relevancia tributaria: conservarlos al menos mientras la DIAN conserve facultad de fiscalización (firmeza de la declaración) — no inferior al plazo del Art. 60 C.Co.

## Trazabilidad cuenta → formato → concepto

El corazón de la rastreabilidad en exógena: cada cuenta del PUC con movimiento tiene un camino documentado hasta su formato y concepto DIAN, vía la matriz `INFORMACION PARA FORMATOS.xlsx` (hoja "FORMATOS Y CONCEPTOS DIAN").

- Una cuenta sin mapeo claro se **escala**, no se asume.
- Se deja trazable **qué cuenta alimentó qué concepto** (auditable al 100 %).
- Ejemplo: cuenta 5135 (servicios) → Formato 1001, concepto 5004.
- Detalle del procedimiento: *Subskill B4 - Mapear Cuenta Formato Concepto* y la regla C.* de *Lecciones Aprendidas Exogena*.

Esta misma trazabilidad es la que permite a la **conciliación cruzada** (*Conciliacion Exogena vs Declaraciones*) cuadrar cada formato contra su declaración.

## Cierre y aprendizaje

Al cerrar el ciclo de cada cliente, el papel de trabajo alimenta la mejora continua (*Subskill B12 - Documentar y Aprender*): criterios aplicados, cuentas nuevas mapeadas, diferencias resueltas, margen de error real obtenido. Si una misma inconsistencia aparece en 3+ clientes, se propone ajuste estructural (ver el plan de mejora del [[Sistema de Control de Calidad de la Firma]]).

## Relacionado

- [[Sistema de Control de Calidad de la Firma]] · [[Checklist de Revision antes de Firmar]]
- [[Aux 04 - Soportes Contables y Papeles de Trabajo]] · *Lecciones Aprendidas Exogena* · *Subskill B12 - Documentar y Aprender*
- [[Protocolo Elaboracion de Impuestos]] · *Conciliacion Exogena vs Declaraciones* · *Subskill B4 - Mapear Cuenta Formato Concepto*
- [[Manejo de Archivos Excel Corruptos]] · [[Politica de Seguridad de la Informacion]] · [[Margen de Error 2 por ciento]]
- *MOC - Conocimiento Tecnico*
