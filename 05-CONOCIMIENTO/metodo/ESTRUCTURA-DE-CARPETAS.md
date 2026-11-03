# El Método RITORE — estructura de carpetas y reglas anti-reproceso

*Esta es la mitad del valor del sistema. Las skills hacen el trabajo; el método evita rehacerlo.*

---

## 1. La estructura única (para TODOS los clientes y TODOS los trabajos)

```
CLIENTES/
└─ NOMBRE DEL CLIENTE/
   ├─ _FICHA-CLIENTE.md          ← cómo se trabaja este cliente (ver 04-CLIENTE-DEMO)
   ├─ 2026-01/                   ← un período = una carpeta (AAAA-MM)
   │  ├─ 01-INSUMOS/             ← lo que llega: token, extractos, balances. INTOCABLE.
   │  ├─ 02-TRABAJO/             ← papeles de trabajo: anexos, cruces, cálculos
   │  ├─ 03-SALIDA/              ← lo que se entrega/presenta: formularios, XML, EEFF, informe, acuses
   │  └─ 04-TRAZAS/              ← registro de la corrida: qué difirió, qué se corrigió, versiones anteriores
   ├─ 2026-02/
   ├─ EXOGENA-AG2025/            ← las campañas anuales son carpetas hermanas de los meses
   │  ├─ 01-INSUMOS/ … 04-TRAZAS/
   └─ RENTA-AG2025/
      └─ (estructura canónica de la skill de renta)
```

## 2. Las reglas del método

1. **`01-INSUMOS/` es intocable.** Lo que llega, como llegó. Si un insumo está mal, se corrige EN EL ORIGEN (el software contable, el banco, el cliente) y se vuelve a exportar. Jamás se edita un insumo a mano.
2. **Un archivo vive en un solo lugar.** ¿Necesitas el extracto en dos trabajos? Se referencia ("ver 2026-01/01-INSUMOS/"), no se copia. Los duplicados son la fuente #1 de "¿cuál es la versión buena?".
3. **Prohibidos los sufijos `v2`, `final`, `FINAL2`, `(LIMPIA)`.** Cuando un archivo de salida se regenera: el nuevo conserva el nombre canónico, el anterior se mueve a `04-TRAZAS/` con una línea en el registro: fecha, qué cambió, por qué.
4. **Toda cifra entregada es rastreable:** salida ← papel de trabajo ← insumo. Si no puedes seguir el camino, no se entrega.
5. **Toda diferencia material (≥ 1 UVT individual o ≥ 0,5 % del total) tiene una fila** en el registro de diferencias: cruce, tercero, valor, causa, ajuste, estado. Diferencia sin fila resuelta = trabajo no terminado.
6. **El cierre incluye la traza.** Un período sin `04-TRAZAS/` escrito no está cerrado, aunque el formulario esté presentado.
7. **Regla del 3:** lo que corriges 2 veces se documenta como lección; a la tercera vez, se cambia el procedimiento (la skill o el manual), no se vuelve a corregir a mano.

## 3. Los bucles (tu semana de trabajo)

**Bucle diario (15 min, al empezar):** ¿qué vence en los próximos 7 días? ¿llegó algún insumo o correo DIAN? → se clasifica a su carpeta → se eligen los 1–3 clientes del día.

**Bucle mensual por cliente:** INGESTA → VALIDACIÓN → LIQUIDACIÓN → CIERRE → ENTREGA → APRENDIZAJE (la skill de impuestos recurrentes lo ejecuta completo). Si un dato cambia después del cierre, se corrige el insumo y **se re-corre el bucle** — nunca se parcha la salida.

**Bucle anual (campañas):** la exógena y la renta ya no arrancan de cero: consolidan los períodos mensuales ya validados. Doce meses limpios = una exógena en días, no en semanas.

**Bucle de mejora:** cada traza alimenta las lecciones; cada lección con 3 ocurrencias cambia el método. Así el sistema mejora solo, campaña tras campaña.

## 4. La ficha del cliente (el archivo que evita preguntarle dos veces lo mismo)

Cada cliente tiene `_FICHA-CLIENTE.md` con: datos básicos (NIT, régimen, actividad), obligaciones y periodicidades, criterios particulares acordados (con fecha y origen: "el cliente confirmó el 2026-03-10 que…"), antecedentes (sanciones, requerimientos), y pendientes vivos. **Los criterios del cliente viven AQUÍ, nunca dentro de un procedimiento** — así el procedimiento sirve para todos los clientes y la ficha guarda lo particular.

Ver el ejemplo completo en `04-CLIENTE-DEMO/`.

## COMPLEMENTO V2 — Convivencia con estructuras de campaña

Algunas skills (p. ej. Renta PJ) definen una estructura interna de campaña con nombres propios. La regla que manda: **la taxonomía 01-INSUMOS / 02-TRABAJO / 03-SALIDA / 04-TRAZAS es la capa externa SIEMPRE**; la estructura de la skill vive dentro: sus papeles y anexos en `02-TRABAJO/`, sus declaraciones, formatos oficiales y acuses en `03-SALIDA/`, y su registro de decisiones en `04-TRAZAS/`. Ninguna campaña crea un árbol paralelo por fuera de las cuatro carpetas.
