# anki-flashcard-exporter

Turns a notes file into question-answer flashcard pairs formatted for spaced-repetition import, on-device. Built with [Tether's QVAC SDK](https://github.com/tetherto/qvac) — the model runs on-device, so nothing leaves your machine.

## What it does

Turns a notes file into question-answer flashcard pairs formatted for spaced-repetition import, on-device.

**QVAC functions used:** `loadModel` and `completion`.

![anki-flashcard-exporter demo](demo.png)

## Why I built it

Writing flashcards by hand from lecture notes takes longer than studying them.

## Requirements

- Node.js >= 22
- `@qvac/sdk` `^0.19.0` (installed automatically via `npm install`)

## Install

```bash
git clone https://github.com/dummieeasy-gif/anki-flashcard-exporter.git
cd anki-flashcard-exporter
npm install
```

## Run

```bash
npm start
```

See the comments at the top of `index.js` for the exact input this app expects (a file path, folder, or argument). On first run, QVAC downloads the model it needs once and caches it locally; every run after that is fully offline.

## SDK version used

`@qvac/sdk` `0.19.0`

## License

MIT — see [LICENSE](LICENSE).
