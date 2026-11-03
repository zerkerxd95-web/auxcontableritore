---
tipo: induccion
tags: [ritore, auxiliar, formacion]
estado: vigente
fecha: 2026-11-03
---

# Ruta de formación del auxiliar (4 semanas)

Cada semana termina con una **prueba práctica** que revisa el contador o un auxiliar senior. Quien ya tiene experiencia
puede presentar las pruebas directamente; lo que no pase, lo estudia.

## Semana 1 · Fundamentos y digitación

| Lee | Lecciones |
|---|---|
| [01-ESCUELA](../01-ESCUELA/MOC%20-%20Escuela%20Auxiliar%20Contable.md) | Aux 01 PUC · 02 Partida doble · 03 Terceros y RUT · 04 Soportes y papeles de trabajo · 05 Facturas de venta · 06 Compras y gastos · 07 Recibos de caja · 08 Egresos · 09 Notas crédito y débito · 10 Documento soporte |
| [02-MANUAL](../02-MANUAL-DE-ENTREGA/) | 04 Digitación y causación |
| [03-REGLAS](../03-REGLAS-DE-LA-CASA/README.md) | no crear cuentas nuevas · formato S y W |

**Prueba 1:** causar las facturas de venta y compra del cliente de práctica
([06-PRACTICA](../06-PRACTICA/cliente-demo-enero-2026/07-GUION-DE-SIMULACION.md)), con retención e IVA, en la tabla
de asientos de la firma. Debe cuadrar y coincidir con la clave.

## Semana 2 · Impuestos y nómina

| Lee | Lecciones |
|---|---|
| 01-ESCUELA | Aux 11 Nómina · 12 Provisiones y prestaciones · 13 Nómina electrónica · 14 Retenciones · 15 IVA y prorrateo · 16 GMF y bancos |
| 02-MANUAL | 07 Impuestos que prepara el auxiliar · 08 Nómina y seguridad social |
| 03-REGLAS | art. 383 antes del 6 % · cierre de retención mes por mes · formato DIAN en los borradores |
| 05-CONOCIMIENTO | normativa/VALORES-VIGENTES · tecnico/Protocolo Retención F-350 · tecnico/Protocolo IVA F-300 |

**Prueba 2:** liquidar la nómina de enero del cliente de práctica y preparar el borrador del F-350 con todas las
facturas del token que llevan retención.

## Semana 3 · Token, conciliaciones e inventarios

| Lee | Lecciones |
|---|---|
| 01-ESCUELA | Aux 17 Inventarios · 18 Juego de inventarios · 19 Estado del costo · 20 Token DIAN · 21 Cruce token vs contabilidad · 22 Conciliación bancaria |
| 02-MANUAL | 05 Conciliaciones · 06 Cruce token DIAN |
| 03-REGLAS | cruce token obligatorio · conciliación con cruces 1-a-N |
| herramientas | `cruce_token.py` · `conciliar_1aN.py` · `validar_auxiliar.py` |

**Prueba 3:** conciliar el banco y cruzar el token del cliente de práctica con las herramientas; la conciliación debe
cerrar en cero y cada hallazgo del token debe tener acción.

## Semana 4 · Cierre y entrega

| Lee | Lecciones |
|---|---|
| 01-ESCUELA | Aux 23 Balance de prueba y auxiliar · 24 Cierre mensual · 25 Cierre anual y errores comunes |
| 02-MANUAL | 01 Estándar de entrega · 02 Calendario · 03 Checklist · 09 Pendientes y comunicación · 10 Errores que no se repiten |
| 03-REGLAS | garantía de cierre · expediente activo · informes en lenguaje llano |
| 04-AGENTES | 02 Auxiliar Contable Senior (lo que se espera de un senior) |

**Prueba final:** cierre completo de enero del cliente de práctica: carpeta creada con `nuevo_periodo.py`, ocho áreas
con semáforo, asientos propuestos, borradores, trazas y `revisar_entrega.py` sin rojos. La revisa el contador como si
fuera un cliente real.

## Después de la ruta

- Primer mes con un cliente real **acompañado** por un senior (el senior hace la revisión de cuatro ojos).
- Cada error que el contador devuelva se registra en
  [Registro de Errores Recurrentes](../05-CONOCIMIENTO/mejora-continua/Registro%20de%20Errores%20Recurrentes.md); si se
  repite tres veces, entra a [10 - Errores que No se Repiten](../02-MANUAL-DE-ENTREGA/10%20-%20Errores%20que%20No%20se%20Repiten.md).
- Lo que se aprende y sirve a todos va a la [Bitácora de Aprendizajes](../05-CONOCIMIENTO/mejora-continua/Bitacora%20de%20Aprendizajes.md).
