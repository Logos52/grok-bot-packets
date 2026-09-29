<p align="center"><img src="assets/img/logo.svg" width="96" alt="Cherdak"></p>

<h1 align="center">CEFR Text Checker</h1>

<p align="center">Estimate the CEFR level (A1–C2) of an English text right in the browser.<br>
Made by <a href="https://t.me/engattic"><b>Cherdak</b></a> — a Telegram channel about English and digital teaching.</p>

<p align="center"><a href="README.ru.md">Читать на русском</a></p>

---

## What it does
- **Two modes:** *Text for reading* (choose or adapt material for a group) and *Student writing* (estimate the level of a learner's text).
- **Three dimensions:** vocabulary, sentences and grammar, each with its own level.
- **Level map:** words above the group level are underlined in the colour of their level; long sentences are tinted; typos are marked.
- **Adaptation advice:** which words to pre-teach or replace, which sentences to split, which structures to explain.
- **Vocabulary profile**, list of grammar structures with examples, text statistics.
- Russian and English interface. Works offline, no data leaves the browser.

## How it works
Words are looked up in the open **CEFR-J** (A1–B2) and **Octanove** (C1–C2) wordlists after lemmatisation; unknown words get a frequency-based estimate or are matched as typos. Grammar is checked for about 45 structures with levels from the English Grammar Profile. See [docs/METHOD.md](docs/METHOD.md) for details and validation results.

## Use it
Open `index.html` in any browser — no build step or server needed.

### Publish on GitHub Pages
1. Create a repository and upload the contents of this folder (keep the folder structure).
2. Go to **Settings → Pages**, choose **Deploy from a branch**, branch `main`, folder `/ (root)`.
3. After a minute the tool is available at `https://<your-username>.github.io/<repository>/`.

## Development
Requires Node.js 18+ (no dependencies).

```bash
npm test                 # run the tests (calibration, lemmatisation, grammar, typos)
npm run build            # rebuild data/cefr-wordlist.js and assets/js/examples.js
```

```
index.html                 page
assets/js/analyzer.js      analysis engine (browser + Node)
assets/js/app.js           interface
assets/js/i18n.js          RU / EN strings
assets/css/style.css       styles
data/cefr-wordlist.js      generated wordlist
data/source/               source wordlists
scripts/                   build and validation scripts
tests/                     tests and reference texts
```

## Licence
Code: [MIT](LICENSE). Word lists: see [DATA_LICENSE.md](DATA_LICENSE.md) (CEFR-J — free use with citation; Octanove and wordfreq — CC BY-SA 4.0).

The result is an automatic estimate for lesson planning. A CEFR level also depends on the task, the topic and the support learners get.
