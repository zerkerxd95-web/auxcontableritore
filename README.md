# Escuela del Auxiliar Contable · RITORÉ Asesorías Contables

Todo lo que un auxiliar contable de la firma necesita para **digitar, causar, conciliar y entregarle al contador un
período completo, cuadrado y trazable a tiempo**, y para que su IA (Claude u otra) trabaje con el mismo método desde
el primer minuto.

> Este repositorio es **metodología** (🟢 VERDE). No contiene ni debe contener datos de clientes reales.
> Los ejemplos usan un cliente ficticio: COMERCIALIZADORA EJEMPLO SAS, NIT 900.123.456-8. Ver [CONFIDENCIALIDAD.md](CONFIDENCIALIDAD.md).

## Empieza aquí

1. **Instala** (5 minutos): [INSTALACION.md](INSTALACION.md).
2. **Entiende cómo trabaja la firma**: [00-EMPIEZA-AQUI/COMO-TRABAJA-LA-FIRMA.md](00-EMPIEZA-AQUI/COMO-TRABAJA-LA-FIRMA.md).
3. **Sigue la ruta de formación** (4 semanas): [00-EMPIEZA-AQUI/RUTA-DE-FORMACION.md](00-EMPIEZA-AQUI/RUTA-DE-FORMACION.md).
4. **Abre Claude Code en esta carpeta** y pídele, por ejemplo: *"Crea el período 2026-01 del cliente de práctica y
   guíame en el cierre"*. Claude lee [CLAUDE.md](CLAUDE.md) y trabaja con el método de la firma.

## Qué hay

| Carpeta | Contenido |
|---|---|
| [00-EMPIEZA-AQUI/](00-EMPIEZA-AQUI/) | cómo trabaja la firma y ruta de formación de cuatro semanas |
| [01-ESCUELA/](01-ESCUELA/MOC%20-%20Escuela%20Auxiliar%20Contable.md) | 25 lecciones: PUC, partida doble, terceros, causación, nómina, retenciones, IVA, GMF, inventarios, token DIAN, conciliación, cierre mensual y anual |
| [02-MANUAL-DE-ENTREGA/](02-MANUAL-DE-ENTREGA/) | **el estándar de entrega al contador**: carpeta del período, calendario de cierre, checklist, digitación, conciliaciones, token, impuestos, nómina, pendientes y errores que no se repiten, con plantillas |
| [03-REGLAS-DE-LA-CASA/](03-REGLAS-DE-LA-CASA/README.md) | las reglas permanentes de la firma (garantía de cierre, cruces 1-a-N, token obligatorio, no crear cuentas, art. 383…) |
| [04-AGENTES/](04-AGENTES/) | perfiles completos de los agentes auxiliares de la firma (estándar RITORE) y guía de carga |
| [05-CONOCIMIENTO/](05-CONOCIMIENTO/) | técnico (protocolos F-350, F-300, F-2593, RADIAN, papeles de trabajo), normativa (UVT y valores vigentes, laboral, seguridad social, sanciones), método y mejora continua |
| [06-PRACTICA/](06-PRACTICA/) | cliente ficticio de enero de 2026 con balance, auxiliar, extracto, token y prenómina, guion de simulación y clave de respuestas |
| [07-PLANTILLAS-EXCEL/](07-PLANTILLAS-EXCEL/) | plantillas Excel de la firma: causación, conciliación, token, IVA, retención, nómina, PUC, obligaciones |
| [herramientas/](herramientas/) | scripts Python: carpeta del período, validación del auxiliar, cruce token, conciliación 1-a-N, revisión de entrega |
| [.claude/](.claude/) | subagentes y skills de Claude Code para el auxiliar |
| [claude-desktop/skills/](claude-desktop/skills/) | skills para Claude Desktop / claude.ai |
| [CLAUDE.md](CLAUDE.md) · [AGENTS.md](AGENTS.md) · [PROMPT-SISTEMA.md](PROMPT-SISTEMA.md) | instrucciones para Claude, para otras IA que leen el repositorio y para IA de chat (ChatGPT, Gemini, Copilot) |

## La entrega en una imagen

```
<CLIENTE>/
├── _cliente.yaml                 ficha: régimen, periodicidad IVA, retención, bancos, criterios (la mantiene el contador)
└── 2026-01/
    ├── ENTREGA.md                semáforo de 8 áreas · cifras token vs libros · decisiones para el contador
    ├── 01-INSUMOS/               TOKEN_ · EXTRACTO_ · BP_ · AUX_ · SOPORTES/   (nunca se editan)
    ├── 02-PROCESADO/             01_CRUCE_TOKEN · 02_CONCILIACIONES · 03_CARTERA_Y_PROVEEDORES
    │                             04_CUADRE_IMPUESTOS · 05_NOMINA · 06_BP_REVISADO
    ├── 03-SALIDA/                ASIENTOS_PROPUESTOS_2026-01.xlsx · BORRADOR F-350 / F-300
    └── 04-TRAZAS/                NOTAS-Y-PENDIENTES · TABLA-DE-DIFERENCIAS · REGISTRO-DE-CORRIDAS
                                  CHECKLIST-DE-CIERRE · OBSERVACIONES-DEL-CONTADOR · SOLICITUD-DE-INSUMOS
```

```bash
python herramientas/nuevo_periodo.py "TRABAJOS" "COMERCIALIZADORA EJEMPLO SAS" 2026-01 --nit 900123456
```

```bash
python herramientas/revisar_entrega.py "TRABAJOS/COMERCIALIZADORA EJEMPLO SAS/2026-01"
```

## Principios

- **El auxiliar prepara, el contador decide y firma.** Los ajustes de cierre son propuestos; las declaraciones son borradores.
- **Nada se da por cerrado sin prueba:** diferencia cero en conciliaciones, token cruzado documento por documento en
  los dos sentidos, cada cuenta en su saldo correcto.
- **Todo pendiente tiene valor, responsable y fecha.** Toda diferencia tiene causa y acción.
- **Lenguaje llano** para el cliente; paleta Ritoré (negro, dorado, blanco) en todo lo que sale de la firma.

## Licencia

Uso interno de RITORÉ Asesorías Contables y de quienes la firma autorice. Ver [LICENSE.md](LICENSE.md).
