---
tipo: conocimiento
tags: [ritore, conocimiento, gestion-firma, seguridad]
estado: vigente
fecha: 2026-06-08
---

# Política de Seguridad de la Información

Política interna de Asesorías Contables FYT para proteger la información que custodia: credenciales de acceso (DIAN, municipios, seguridad social, bancos), información contable de los clientes y datos personales. Nace de un **riesgo real detectado**: hay **claves DIAN en texto plano** en carpetas sincronizadas de la firma (*Tablero de Alertas y Pendientes*, sección Seguridad). Esta nota define cómo cerrar ese riesgo y cómo operar de forma segura en adelante.

> El vault Obsidian **no contiene ninguna clave** y debe seguir así. Ninguna credencial se documenta en notas, ni en el repositorio, ni en chats.

## Riesgo detectado (estado actual)

Archivos con credenciales en texto plano identificados en `Empresas a cargo/otros doc/` y en la raíz:
- `claves y contraseñas.xlsx`, `Copia de CLAVES(1).xlsx` (incluye EMPRESA AV, EMPRESA AQ).
- `CONTRASEÑAS.txt` en la raíz.

Riesgo: un único archivo comprometido (robo de equipo, sincronización a una cuenta personal, enlace compartido por error) expone los accesos tributarios de varios clientes a la vez. Es además una debilidad de control interno frente a la responsabilidad de la firma sobre datos de terceros (Ley 1581).

## 1. Gestión de credenciales

- **Gestor de contraseñas obligatorio.** Todas las credenciales (DIAN, municipios, PILA/seguridad social, bancos, correos de clientes, ERP) viven **únicamente** en un gestor de contraseñas cifrado (p. ej. Bitwarden, 1Password, KeePass `[VERIFICAR cuál adopta la firma]`).
- **Prohibido** almacenar credenciales en: archivos `.xlsx`/`.txt`/`.docx`, notas del vault, cuerpos de correo, chats, papeles de trabajo o nombres de archivo.
- **Una bóveda por firma**, con carpetas/colecciones por cliente y permisos por usuario (solo quien atiende al cliente ve sus accesos).
- **Contraseña maestra fuerte** + **2FA** en el gestor y, donde sea posible, en los portales (DIAN, bancos).
- **Rotación** de contraseñas tras: salida de un colaborador, sospecha de compromiso, o cambio de responsable del cliente.

## 2. Control de accesos por cliente

- Asignación de accesos **según necesidad** (need-to-know): cada colaborador accede solo a los clientes que atiende.
- Registro de **quién tiene acceso a qué** (matriz de accesos por cliente y por usuario).
- Revocación inmediata de accesos al terminar la relación con un colaborador o un cliente (coherente con la cláusula de terminación del *Contrato de Prestacion de Servicios Contables*).
- No compartir cuentas personales del portal DIAN; usar los mecanismos de apoderamiento/usuarios que la DIAN provee cuando aplique.

## 3. Custodia y backup de la información contable

- **Estructura de carpetas canónicas** por cliente (ver [[Onboarding de Cliente Nuevo]]); nada de información de clientes en escritorios o carpetas personales sueltas.
- **Backup** periódico y verificado de la información contable y de los acuses/soportes (regla 3-2-1: 3 copias, 2 medios, 1 fuera de sitio `[VERIFICAR esquema que adopte la firma]`).
- **Cifrado** del almacenamiento y de los equipos (disco cifrado en portátiles).
- Cuidado con las **carpetas sincronizadas (OneDrive/Drive)**: además del riesgo de credenciales, los `.xlsx` abiertos se corrompen/truncan al sincronizar (ver [[Manejo de Archivos Excel Corruptos]]).

## 4. Manejo de datos personales (Ley 1581 de 2012)

FYT trata datos personales de representantes legales, empleados de clientes (nómina) y terceros. Como **Responsable/Encargado del Tratamiento**:

- **Autorización del titular** antes de tratar sus datos (se obtiene en el onboarding).
- **Política de Tratamiento de Datos** publicada y disponible para los titulares (finalidad, derechos, canal de atención).
- **Finalidad limitada:** los datos se usan solo para ejecutar el contrato y cumplir obligaciones legales.
- **Deberes del responsable/encargado:** garantizar el habeas data, conservar la información bajo condiciones de seguridad, actualizar/rectificar/suprimir cuando proceda y atender consultas y reclamos.
- **Atención de derechos del titular (plazos legales verificados):**
  - **Consulta:** se atiende en máximo **10 días hábiles**; si no es posible, se informa el motivo y se atiende dentro de los **5 días hábiles** siguientes al vencimiento.
  - **Reclamo:** se atiende en máximo **15 días hábiles** desde el día siguiente al recibo; prórroga de hasta **8 días hábiles** adicionales informando el motivo.
  - El titular solo puede acudir a la **SIC** tras agotar el trámite ante el responsable/encargado.
- Inscripción de bases de datos en el **RNBD** de la SIC `[VERIFICAR si la firma supera el umbral de obligación vigente del RNBD]`. Coordinar con *20b-HabeasData-Senior*.

## 5. Retención y destrucción de documentos

- **Conservación de papeles de trabajo y soportes:** los documentos de comercio y sus soportes se conservan por **mínimo 10 años** (Art. 28 Ley 962/2005, que modificó el Art. 60 C.Co.) `[VERIFICAR vigencia y excepciones]`; papeles de trabajo del contador/revisor según la normativa profesional.
- **Destrucción segura** al cumplir el período de retención y la finalidad: borrado seguro de archivos digitales y destrucción física de papeles con datos personales/sensibles.
- No conservar credenciales más allá de su uso: al terminar con un cliente, los accesos se entregan/revocan y se eliminan de la bóveda.

## 6. Plan ante incidentes de seguridad

- **Detección y contención:** aislar el equipo/cuenta afectado; cambiar de inmediato las credenciales potencialmente expuestas.
- **Evaluación:** qué información/clientes se vieron afectados.
- **Notificación:** si hay vulneración de **datos personales**, reportar a la **SIC** conforme a la Ley 1581 y notificar a los clientes afectados `[VERIFICAR plazo de reporte vigente a la SIC]`. Coordinar con *20b-HabeasData-Senior*.
- **Registro y lección aprendida:** documentar el incidente y ajustar controles.

## Checklist de migración de las claves actuales a un gestor

- [ ] **1.** Adoptar/definir el gestor de contraseñas de la firma y crear la bóveda.
- [ ] **2.** Inventariar todas las credenciales hoy en texto plano (`claves y contraseñas.xlsx`, `Copia de CLAVES(1).xlsx`, `CONTRASEÑAS.txt`, y cualquier otro).
- [ ] **3.** Cargar cada credencial al gestor, organizada por cliente, con permisos por usuario.
- [ ] **4.** Verificar que cada acceso funciona desde el gestor.
- [ ] **5.** **Eliminar de forma segura** los archivos planos (no solo a la papelera: borrado seguro) y vaciar copias sincronizadas/versiones en OneDrive/Drive.
- [ ] **6.** Activar **2FA** en el gestor y en los portales que lo permitan (DIAN, bancos).
- [ ] **7.** **Rotar** las contraseñas que estuvieron expuestas en texto plano.
- [ ] **8.** Configurar la **matriz de accesos** por cliente/usuario.
- [ ] **9.** Comunicar la política al equipo y dejar constancia de lectura.
- [ ] **10.** Cerrar la alerta de seguridad en el *Tablero de Alertas y Pendientes*.

## Reglas críticas

- NUNCA almacenar credenciales en archivos planos, notas, correos o chats.
- NUNCA subir credenciales al vault ni al repositorio de conocimiento.
- SIEMPRE usar el gestor de contraseñas con 2FA.
- SIEMPRE obtener autorización de tratamiento de datos antes de manejar datos personales del cliente.
- SIEMPRE atender consultas (10 días hábiles) y reclamos (15 días hábiles) de titulares dentro del plazo legal.

## Hallazgos / advertencias

- Riesgo activo: archivos de claves en texto plano aún sin migrar (alerta abierta en el *Tablero de Alertas y Pendientes*). Prioridad alta.
- Marcados `[VERIFICAR]`: gestor de contraseñas a adoptar, esquema de backup, umbral RNBD, plazos exactos de reporte de incidentes a la SIC y vigencia del período de conservación documental. Confirmar con *20b-HabeasData-Senior* antes de fijar la versión definitiva.

## Relacionado

- *20b-HabeasData-Senior*
- *Tablero de Alertas y Pendientes*
- [[Onboarding de Cliente Nuevo]] · *Contrato de Prestacion de Servicios Contables* · *Debida Diligencia y Conocimiento del Cliente*
- [[Manejo de Archivos Excel Corruptos]]
