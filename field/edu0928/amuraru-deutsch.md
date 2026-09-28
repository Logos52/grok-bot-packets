# Deutsch A2 / B1 · telc Trainer

A self-contained, offline-capable web app to practice for the **telc Deutsch A2** and
**telc Deutsch B1** exams. No build step, no dependencies — it's a single `index.html`.

**▶️ Live: https://amuraru.github.io/deutsch/**

## Features

- **Two levels:** switch between **A2** and **B1** (toggle top-right). Progress is tracked separately per level.
- **Two modes:**
  - **Übungsmodus** (practice) — instant feedback + explanation per question.
  - **Prüfungssimulation** (exam) — full telc-format mock, timed, scored at the end (pass ≥ 60%).
- **All five exam parts:**
  - Leseverstehen (reading) · Sprachbausteine (grammar/vocab) · Hörverstehen (listening) — auto-graded.
  - Schreiben · Sprechen — self-assessed with model answers.
- **Listening** uses the browser's built-in German text-to-speech (Web Speech API) — no audio files needed; a transcript fallback is provided.
- **Progress dashboard**, per-part accuracy, exam history, dark/light theme — all stored locally in your browser (`localStorage`).

## Official telc material

The interactive exercises here are **original content built in the telc format** — they are
practice material, not real exam papers. For **authentic, official telc mock exams (with audio)**,
the app links directly to telc's own free downloads inside the "Offizielle telc Modelltests" section.

## Disclaimer

This is an **unofficial** study tool and is **not affiliated with or endorsed by telc gGmbH**.
"telc" is a trademark of telc gGmbH. Official telc exam papers are copyrighted (© telc gGmbH) and
are **not reproduced** in this project — they are only linked to their official source.

## Usage

Just open the live link, or download `index.html` and double-click it — it works fully offline
(the only online part is the optional links to telc's website).
