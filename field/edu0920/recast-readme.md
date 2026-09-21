# ReCast · Entrenador de Speaking

App personal para practicar conversación en inglés. La conversación ocurre fuera, en una
app de voz. Esta app prepara la sesión, evalúa la transcripción, recuerda los fallos y
genera tarjetas para Anki. La idea completa está en [docs/plan.md](docs/plan.md).

**App publicada:** https://machaksauriorex.github.io/ReCast/

## Estructura

```
ReCast/
├── app/                  ← la aplicación (PWA estática, sin build)
│   ├── index.html
│   ├── manifest.webmanifest
│   ├── sw.js             ← caché offline (sube VERSION al cambiar archivos)
│   ├── css/app.css
│   ├── fonts/            ← IBM Plex, sacadas del diseño
│   ├── icons/
│   └── js/
│       ├── main.js         pantallas y navegación
│       ├── planificador.js rotación de formatos, tema, ítems, prueba de control, escape
│       ├── memoria.js      ciclo de vida de los ítems (se recalcula desde las sesiones)
│       ├── prompts.js      prompt del conversador, prompt del evaluador, lectura del JSON
│       ├── anki.js         exportación TSV
│       ├── store.js        persistencia en IndexedDB
│       └── temas.js        banco de temas inicial
└── docs/
    ├── plan.md           idea y planeamiento
    └── diseno/inicio.html  propuesta de interfaz original
```

## Cómo se usa

1. **EMPEZAR.** Se planifica la sesión y el prompt se copia solo.
2. Pégalo en la app de voz (Claude, ChatGPT, Gemini) y habla.
3. **He terminado → evaluar.** Pega la transcripción, copia el prompt del evaluador,
   pégalo en un chat nuevo (siempre con el mismo modelo) y trae el JSON de vuelta.
4. **Parte.** Revisa los veredictos, corrígelos si hace falta, ignora los fallos de
   transcripción y guárdalo en memoria.
5. **Tarjetas.** Filtra lo que quieres estudiar. Exporta desde *Memoria → tarjetas*.

Anki: *Archivo → Importar* el `.txt`. Las cabeceras del archivo ya fijan el tabulador
como separador y la columna de etiquetas.

## Probar en el ordenador

```bash
python -m http.server 5173 --directory app
```

Abre http://localhost:5173.

## Instalar en Android

La app tiene que servirse por HTTPS para instalarse y funcionar offline. Lo más sencillo:

- **GitHub Pages:** sube el repositorio y publica la carpeta `app/`.
- **Netlify Drop:** arrastra la carpeta `app/` a https://app.netlify.com/drop.

Ábrela en Chrome desde el móvil → menú → *Añadir a pantalla de inicio*. Los datos se
guardan en el propio móvil (IndexedDB). **Haz copias** desde *Memoria → ajustes*:
si borras los datos de Chrome, se pierde el histórico.

## Pendiente

- Evaluación automática con API (ahora mismo solo hay modo manual).
- `.apkg` con identificador estable por tarjeta, para importar directamente en AnkiDroid.
