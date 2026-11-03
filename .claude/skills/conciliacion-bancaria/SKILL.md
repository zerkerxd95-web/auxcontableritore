---
name: conciliacion-bancaria
description: Concilia una cuenta bancaria o pasarela contra libros con cruces 1-1 y 1-a-N hasta diferencia cero, usando herramientas/conciliar_1aN.py. Úsala con "concilia el banco", "el banco no cuadra", "llegó el extracto", "partidas sin identificar".
---

# Conciliación bancaria

1. Extracto en `01-INSUMOS/EXTRACTO_<BANCO>_<ÚLTIMOS4>_<AAAA-MM>` y auxiliar de la cuenta (validado con
   `validar_auxiliar.py` si viene en formato W).
2. Saldo final del extracto y saldo de libros de la cuenta en el balance de prueba.
3. Ejecuta:
   ```bash
   python herramientas/conciliar_1aN.py --extracto "01-INSUMOS/EXTRACTO_…" --libro "AUX_cuenta.xlsx" --saldo-extracto 0 --saldo-libros 0 --cuenta "11100501 Banco …" --salida "02-PROCESADO/02_CONCILIACIONES_<AAAA-MM>.xlsx"
   ```
   Código 0 = cierra en cero; 2 = no cierra.
4. Si no cierra: revisa saldos digitados, movimientos de otra cuenta, fechas fuera del período, duplicados; vuelve a
   correr con `--dias 10 --max-grupo 6`. Solo entonces una partida queda "por identificar" (con valor y fecha).
5. Clasifica y actúa: GMF, comisiones y rendimientos → causar con el extracto de soporte; abonos sin identificar →
   cartera; giros no cobrados y consignaciones en tránsito → controlar el mes siguiente; más de 60 días → decisión del contador.
6. Registra la corrida en `04-TRAZAS/REGISTRO-DE-CORRIDAS.md` y las partidas abiertas en `TABLA-DE-DIFERENCIAS.md`.

Método completo: `02-MANUAL-DE-ENTREGA/05 - Conciliaciones.md` y `03-REGLAS-DE-LA-CASA/regla-conciliacion-cruces-1-a-n.md`.
