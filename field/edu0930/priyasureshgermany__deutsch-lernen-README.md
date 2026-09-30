# Deutsch lernen

Offline study app for German: **telc Deutsch A1** and **telc Deutsch B1** exam practice, **25 Gesprächsthemen** with A1/A2/B1 versions of every question and B1 model answers, and **Wörter erkennen** — ten A1/B1 texts where every word is tagged with its word type, case and sentence role.

Live: https://priyasureshgermany.github.io/deutsch-lernen/

- English translation, solutions, and a practice mode that hides answers and listening texts until tapped
- Read-aloud (▶) with a slow tempo, using the device's German voice
- Tap a word (or several with *Mehrere Wörter*) for its translation right in the popup: meaning, base form, article and plural for nouns, and the sentence in English
- Wörter erkennen: tap to colour by word type, subtype, case, sentence role or TeKaMoLo; tap again to see what it is, why, and all its forms; Satzbau shows each sentence in its parts; practice mode to guess type, subtype and case
- Search in German or English
- Installable (Add to Home Screen) and works offline; it only updates when you press the version button in the top bar

## Layout

| File | What |
|---|---|
| `index.html` | App shell: tabs, update button, service worker registration |
| `a1.html`, `b1.html`, `themen.html` | The three study sections, each self-contained |
| `woerter.html`, `woerter-data.js` | Wörter erkennen: the page, and the hand-tagged texts (format explained at the top of the data file) |
| `translate.js` | In-popup word translation (Google Translate + Wiktionary for article/plural) |
| `woerter-lex.js` | Grammar for Wörter erkennen: subtypes, verb conjugations, declension tables, TeKaMoLo |
| `tools/list-tekamolo.mjs` | Prints every adverbial phrase with its TeKaMoLo label, for review |
| `tools/check-woerter.mjs` | `node tools/check-woerter.mjs` — fails unless every text has every word type and all four cases |
| `sw.js` | Offline cache; replaced only through the Update button |
| `tools/make-icons.py` | Redraws `icons/` (needs Pillow) |
| `tools/import-modules.py` | Re-imports the sections from saved Claude artifact sources |

Releasing: bump the version in `index.html` (`APP_VERSION`), `sw.js` (`VERSION`) and `version.json` together, and add a line to `RELEASES.md`.
