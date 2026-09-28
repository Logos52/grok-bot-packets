# Hànyǔ Lab

An audio-led Mandarin course for everyday conversation. The site is static; there is no application build step.

Run locally:

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000`. Progress is saved in the browser and can be backed up from the course sidebar. Audio is generated locally and served from the same server.

## Learn through lesson albums

Each lesson opens as an album of tracks: a real conversation, useful phrases, a mini-story, the same story from another point of view, a grammar spotlight, mixed practice, and a hands-free listen-again queue. Tracks unlock in order. A reference page at `#/hello/notes` collects the transcript, phrase details, grammar, pronunciation, culture, stories, practice picker, and printable cheat sheet.

The first album is **你好，邻居！ Hello, neighbour!**. Phrase review lives at `#/phrases`, and spaced review lives at `#/review`. Learners choose a Chinese name and reuse it throughout the dialogue and story questions.

## Project structure

- `js/core.js` and `app.js`: lesson order, saved state, route registration, navigation, and settings.
- `js/components/audio.js`: shared audio player and local clip fallback.
- `js/components/narrator.js`: full-screen track player and hands-free narration queue.
- `js/components/drills.js`: reusable listening, speaking, writing, reading, matching, and sentence drills.
- `js/components/vocab.js`: phrase shelf and three-direction spaced repetition.
- `js/lessons/hello-album.js` and `hello-notes.js`: first lesson album and notes routes.
- `narration/hello.json`: source for lesson lines, Chinese audio inventory, phrases, tracks, stories, drills, and notes. `narration/hello.js` is generated from it.
- `docs/method.md` and `docs/roadmap/data.js`: teaching method and course plan.
- `js/components/motion.js` and `styles/motion.css`: orchestrator-owned animation and interaction APIs. Call `HanyuLab.Motion`; do not edit either file.

Read [docs/adding-a-lesson.md](docs/adding-a-lesson.md) and [narration/STYLE.md](narration/STYLE.md) before creating lesson content. Check JSON with `uv run tools/voice.py lint narration/<id>.json`, then build Edge audio with `uv run tools/voice.py build narration/<id>.json --engine edge`. MiniMax audio is rendered later by the orchestrator. Generated audio stays under ignored `audio/` and is never deployed.
