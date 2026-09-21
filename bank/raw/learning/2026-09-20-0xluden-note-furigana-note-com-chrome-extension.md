---
id: 2026-09-20-0xluden-note-furigana-note-com-chrome-extension
kind: article
title: note furigana — note.com Chrome extension with corpus-only examples
source: "https://github.com/0xluden/note-furigana"
author: 0xluden
published: 2026-09-19
captured: 2026-09-20
via: grok-bot/Field
lane: learning
status: raw
private: false
---

# note furigana

Chrome/Brave extension for reading [note.com](https://note.com) articles as a Japanese learner.

- Furigana over kanji, in the note's **title and body only** (pages shaped `note.com/<user>/n/<id>`).
- Hover a word: meaning (JP→EN), JLPT level, and up to 3 real example sentences.

## Install

1. Open `brave://extensions` (or `chrome://extensions`).
2. Turn on **Developer mode**.
3. Click **Load unpacked** and pick this folder.

## How it works

| Piece | Source |
|---|---|
| Word splitting + readings | [kuromoji.js](https://github.com/takuyaa/kuromoji.js), bundled, offline |
| Meaning + JLPT level | [Jisho](https://jisho.org) API |
| Examples | [Tatoeba](https://tatoeba.org) (with English); falls back to [Massif](https://massif.la) (Japanese only) for rare words |

Examples are always real sentences from those corpora, never generated.

`vendor/kuromoji/kuromoji.js` is the 0.1.2 browser build with one patch: `path.join(dic_path, …)` → `dic_path + …`,
because `path.join` collapses the `//` in `chrome-extension://` URLs.

## Test

```bash
node test.js
```
