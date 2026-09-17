# FSRS Flashcards

Create flashcards straight from your notes and review them with **FSRS-5** spaced repetition. Selection-based card creation, seven question types, automatic grading, wrong-answer review and media support, all inside Obsidian.

By **Helfas**. MIT licensed. The technical plugin id is `sfc-flashcards`.

## Highlights

- **Make cards from what you are reading.** Select text (or an image) and run the capture command; the passage keeps a `^sfc-xxxx` marker that links back to the cards made from it.
- **Seven question types:** recite, multiple choice, cloze, true/false, short answer, essay/worked solution, and custom.
- **Automatic grading** for multiple choice and cloze, with configurable strictness for short answers.
- **Wrong-answer review and sprint mode**, so mistakes come back before the exam does.
- **Images and audio** in questions and answers.
- **Card centre, card lists and deck tree**, with a study heatmap.
- **Optional AI drafts.** With the companion **AI Host** plugin, turn text, a selection or an image into an editable card draft. AI is off by default and bound by the host's permission model.
- **Chinese UI** and full mobile support.

## Installation

### Community plugins
Once listed: **Settings  Community plugins  Browse**, search for `FSRS Flashcards`, then **Install** and **Enable**.

### Manual installation
1. Download `main.js`, `manifest.json` and `styles.css` from the latest GitHub release.
2. Put them in `<vault>/.obsidian/plugins/sfc-flashcards/`.
3. Reload Obsidian and enable **FSRS Flashcards** in **Settings  Community plugins**.

## Getting started

1. Select a passage in a note.
2. Run the command **"从选区制卡"** (create a card from the selection).
3. Open the card centre and start a review session.
4. Rate each answer with **重来 / 困难 / 良好 / 简单**; FSRS-5 schedules the next review.

## AI card drafts (optional)

The flashcards plugin has no network code of its own. AI drafting requires the companion **AI Host** plugin, where the provider and key are configured. AI-drafted fields are written into an editable draft first, never silently into a card.

## Privacy

Card data and review history live under `.obsidian/plugins/sfc-flashcards/`; card sources remain in your notes. There is no telemetry and no network access unless you explicitly configure AI Host.

## Development

```bash
npm ci
npm run build
npm run verify
npm run typecheck
```

## License

MIT  2026 Helfas. See `LICENSE`. Third-party notices, including the FSRS reference projects, are in `THIRD-PARTY-NOTICES.md`.

## Vault access, filesystem and clipboard

FSRS Flashcards indexes your notes to find cards and their `^sfc-xxxx` markers, using Obsidian's vault API. Card sources stay in your notes and review state lives in the plugin folder inside your configuration directory. On desktop it uses Node's `fs` module only for atomic writes inside that plugin folder; it never reads or writes paths outside the vault. The system clipboard is touched only when you use a copy or paste action in the plugin's own interface. There is no telemetry and no network access unless you explicitly configure the AI Host companion plugin.