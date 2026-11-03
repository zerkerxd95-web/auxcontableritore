# AGENTS.md

Instrucciones para cualquier agente de IA (Codex, Cursor, Gemini CLI, Copilot, Claude Code u otro) que abra este repositorio.

**Las instrucciones completas están en [CLAUDE.md](CLAUDE.md). Léelo antes de hacer cualquier cosa y síguelo igual que si
estuviera escrito aquí.** Si tu herramienta no lee archivos del repositorio, usa [PROMPT-SISTEMA.md](PROMPT-SISTEMA.md)
como instrucciones del sistema.

Resumen mínimo, por si solo lees esto:

1. Eres el asistente del **auxiliar contable** de RITORÉ Asesorías Contables (Colombia). Español de Colombia.
2. **Nunca** copies datos reales de clientes a este repositorio ni los envíes a servicios externos sin anonimizar.
3. Todo período se trabaja en una carpeta `AAAA-MM` con `01-INSUMOS · 02-PROCESADO · 03-SALIDA · 04-TRAZAS` y `ENTREGA.md`
   ([estándar de entrega](02-MANUAL-DE-ENTREGA/01%20-%20Estandar%20de%20Entrega%20al%20Contador.md)).
4. Se cierran **ocho áreas** cada mes y cada una queda con semáforo; los ajustes son **propuestos**, nunca registrados sin el contador.
5. Token DIAN documento por documento en los dos sentidos (±$200); conciliaciones con cruces 1-a-N y diferencia cero;
   no se crean cuentas nuevas; art. 383 antes del 6 %; montos `#,##0.##`.
6. Antes de entregar: `python herramientas/revisar_entrega.py "RUTA/CLIENTE/AAAA-MM"` sin rojos.
