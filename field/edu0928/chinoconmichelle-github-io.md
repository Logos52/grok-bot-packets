# Chino con Michelle · 中文学习卡片

Tarjetas de estudio de chino mandarín para las clases con la profesora Michelle Hsu.
Mandarin study cards for classes with Michelle Hsu.

**Sitio / Site:** https://chinoconmichelle.github.io

Basado en las tarjetas HTML originales de Michelle, con su permiso.
Built on Michelle's original HTML flashcards, with her permission.

## Estructura / Structure

```
index.html        the single page you open
assets/style.css  themes and layout
assets/app.js     app logic (interface languages, study modes, progress, export/import)
data/topics.js    creates the topic list
data/<topic>.js   one file per topic; the order of <script> tags in index.html is the home-screen order
```

Progress is saved per user account (Supabase) and keyed by card `id`, so card ids must never be reused or renumbered.
