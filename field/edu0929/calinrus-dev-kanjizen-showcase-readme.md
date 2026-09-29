# KanjiZen / Reconocer no es recordar.

**Japonés convertido en entrenamiento.** Leer, recuperar la respuesta y fijarla con el gesto. La primera ruta jugable combina hiragana, MECA y Flick; progresión por dominio demostrado, colección e historial local.

**Expo · React Native · TypeScript** · Recorrido previo en Dart y Flutter.

![Flick real de KanjiZen: entrenamiento gestual de kana.](assets/flick.png)

## Tres trabajos distintos

**La guía enseña. MECA exige recuperar. Flick añade memoria gestual.** Separar esas funciones importa: haber visto la respuesta no demuestra poder recordarla. El flujo completo del producto conserva progreso; la muestra pública de abajo se concentra en una pieza comprobable.

## Escribe «si». Debe aceptarlo.

[**Probar el evaluador real →**](https://calinrus-dev.github.io/kanjizen-showcase/) · [Código](samples/romaji.js) · [Pruebas](test/romaji.test.mjs)

El evaluador admite variantes completas como `si → shi`, `ti → chi` y `sya → sha`. El orden importa: una respuesta válida completa debe ganar a un prefijo. También admite kana directo en MECA.

[![Pruebas de la muestra](https://github.com/calinrus-dev/kanjizen-showcase/actions/workflows/verify.yml/badge.svg)](https://github.com/calinrus-dev/kanjizen-showcase/actions/workflows/verify.yml)

~~~sh
node --test test/*.test.mjs
~~~

## Una decisión que se puede discutir

Hay dos contratos explícitos: `evaluateStep` espera entrada normalizada; `mecaEvaluate` recorta espacios y normaliza mayúsculas. Esa diferencia está conservada y probada. No se maquilla para que el ejemplo parezca más uniforme que el producto.

La función pura no importa React Native, persistencia ni UI. Se puede probar en Node y utilizar en una interfaz sin arrastrar el framework. La muestra abre validación de entrada; SRS, recompensas, selección de ejercicios y progresión continúan privados.

**Estado del producto:** primera ruta jugable de hiragana, MECA y Flick. No se presenta el recorrido futuro de kanji como terminado.

[Capturas de la aplicación](docs/DEMOSTRACIONES.md) · [Recorrido de aprendizaje](docs/EXPERIENCIA.md) · [Origen y límites](docs/PROVENANCE.md) · [Verificación](docs/VERIFICATION.md) · [Portfolio](https://github.com/calinrus-dev/portfolio)


[Instagram @c4linrus](https://www.instagram.com/c4linrus/) · [LinkedIn / calinrus](https://www.linkedin.com/in/calinrus-dev/)
