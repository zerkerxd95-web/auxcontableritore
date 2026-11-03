# Confidencialidad

La firma separa dos clases de información (política completa:
[05-CONOCIMIENTO/Politica de Separacion de Datos y Confidencialidad.md](05-CONOCIMIENTO/Politica%20de%20Separacion%20de%20Datos%20y%20Confidencialidad.md)):

| Clase | Qué es | Dónde vive |
|---|---|---|
| 🟢 **VERDE** — metodología | escuela, manual de entrega, reglas, agentes, skills, plantillas, herramientas | **este repositorio** |
| 🔴 **ROJO** — datos de clientes | razón social, NIT, nombres de socios y empleados, cifras, extractos, tokens, nóminas, declaraciones, correos | **solo** en la carpeta de trabajo del cliente (`TRABAJOS/` u otra ruta de la firma), nunca aquí |

## Reglas del auxiliar

1. **Nada ROJO entra a este repositorio**, ni en ejemplos, ni en capturas, ni en una lección aprendida. Si un ejemplo
   real sirve para enseñar, se anonimiza: el cliente pasa a un descriptor ("un comercio de bicicletas"), los NIT a
   ficticios y las cifras a didácticas.
2. **`TRABAJOS/` está en `.gitignore`.** No lo saques de ahí ni guardes clientes en otras carpetas del repositorio.
3. **IA externa:** antes de pegar o adjuntar un archivo de cliente en una IA de chat pública, cambia razón social, NIT
   y nombres de personas. Con Claude Code en tu equipo, los archivos se leen localmente pero el contenido que la IA
   procesa sí sale hacia el proveedor del modelo: usa la cuenta de la firma, no una personal.
4. **Un cliente por conversación.** No mezcles datos de dos clientes en la misma sesión ni en el mismo archivo.
5. **Credenciales** (DIAN, bancos, software contable, correo del cliente): nunca en archivos, notas ni mensajes a la IA.
   Las maneja el auxiliar en el gestor de contraseñas de la firma.
6. **Antes de proponer un cambio al repositorio** (pull request o commit), corre:
   ```bash
   python herramientas/verificar_exportacion.py . --nombres RUTA/FUERA/DEL/REPO/nombres-reales.txt
   ```
   Debe dar **cero hallazgos**. Revisa también los Excel con `herramientas/anonimizar_xlsx.py` si tocaste plantillas.
7. Ante la duda, es ROJO.

Marco legal: Ley 1581 de 2012 (habeas data), secreto profesional del contador (art. 63, Ley 43 de 1990) y reserva de
las declaraciones tributarias (art. 583 E.T.).

## Cliente de práctica

Todos los ejemplos del repositorio usan **COMERCIALIZADORA EJEMPLO SAS, NIT 900.123.456-8**, terceros `901000001…`
y cifras inventadas. No corresponden a ningún contribuyente real.
