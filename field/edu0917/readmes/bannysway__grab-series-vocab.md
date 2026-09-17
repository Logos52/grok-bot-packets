**English** · [简体中文](README.zh-CN.md) · [Español](README.es.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md)

# grab-series-vocab

> Turn any TV series into a deduplicated vocabulary corpus you can actually study.

![license](https://img.shields.io/badge/license-MIT-blue) ![data](https://img.shields.io/badge/data-CC%20BY%204.0-lightgrey) ![python](https://img.shields.io/badge/python-3.9%2B-3776ab) ![Anki](https://img.shields.io/badge/Anki-compatible-orange) ![headwords](https://img.shields.io/badge/headwords-14%2C413-informational)

> **The matrix** · 🧰 **[grab-series-vocab](https://github.com/bannysway/grab-series-vocab)** ← *you are here* · 🚔 [tv-vocab-nypd-blue](https://github.com/bannysway/tv-vocab-nypd-blue) · ☕ [tv-vocab-friends](https://github.com/bannysway/tv-vocab-friends) · 🎹 [tv-vocab-your-lie-in-april](https://github.com/bannysway/tv-vocab-your-lie-in-april) · 👤 [@bannysway](https://github.com/bannysway)

---

`grab-series-vocab` is an **agent skill** and a plain command-line tool in one folder. Point it at a directory of subtitle files and it builds a searchable vocabulary library — headword, gloss, IPA, difficulty — that exports to Anki, Markdown, or a single-file web page.

It exists because of one number, measured on my own deck of 33,270 cards: **35.9% of them were duplicates.** Here is how that happened, and what fixes it.

## The problem: a third of the work was wasted

I built my vocabulary deck one episode at a time. Every episode was a fresh session with a fresh agent, and that agent had no idea what the previous 258 episodes had already collected.

Merging all 22,477 accepted cards by headword left only 14,413 distinct words. The most frequently re-collected ones:

| Word | Times picked, independently, in different episodes |
|---|---:|
| `pick up` | 39 |
| `D.O.A.` | 37 |
| `check out` | 35 |
| `take off` | 33 |
| `work out` | 33 |
| `collar` | 30 |
| `wind up` | 28 |
| `canvass` | 27 |
| `dump` | 27 |
| `perp` | 24 |

Duplicate cards are not just wasted effort. They corrupt spaced repetition: three copies of a word means three times the reviews, and your interval scheduler is optimising against the wrong data. The fix is not a better prompt. It is a different data structure — **build the corpus first, and treat every export as a view of it.**

## Ready-made corpora

Three corpora are already published, in one repository each. Download and study them directly, or use the tool to build your own.

| Corpus | Scope | Headwords | What it is good for |
|---|---|---:|---|
| 🚔 **[tv-vocab-nypd-blue](https://github.com/bannysway/tv-vocab-nypd-blue)** | complete · 259 ep | 9,938 | Police, courtroom and legal English — a register you will not find in a textbook. |
| ☕ **[tv-vocab-friends](https://github.com/bannysway/tv-vocab-friends)** | S01–S05 · 121 ep | 4,754 | The everyday spoken English of the 1990s: phrasal verbs, idioms, and how people actually talk. |
| 🎹 **[tv-vocab-your-lie-in-april](https://github.com/bannysway/tv-vocab-your-lie-in-april)** | S01 · 22 ep | 1,175 | English subtitles of an anime. Short, emotional, and a natural bridge for Japanese-speaking learners. |

Adding a fourth show is one entry in `tools/matrix.json` plus one command — see [docs/MATRIX.md](docs/MATRIX.md).

## Install the skill

The skill is a plain `SKILL.md` folder, so it works in any agent that implements the Agent Skills standard.

```bash
npx skills add bannysway/grab-series-vocab --skill grab-series-vocab
```

Or copy the folder in yourself:

| Agent | Personal path | Project path |
|---|---|---|
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| WorkBuddy | `~/.workbuddy/skills/` | — |
| Codex CLI | `~/.codex/skills/` | `.agents/skills/` |
| Cursor | `~/.cursor/skills/` | `.cursor/skills/` |
| Gemini CLI | `~/.gemini/skills/` | `.gemini/skills/` |

Codex CLI reads skills from `~/.codex/skills/` as well; older builds also need `[features] skills = true` in `~/.codex/config.toml`.

Then start a **new** session and check that `grab-series-vocab` shows up in the slash-command or skill menu. A running session will not pick up a newly added folder.

## What the skill does

- Say *“turn my subtitle folder into a vocabulary deck”* and it runs the whole chain — scan, clean, dispatch, ingest, quality-check, export.
- The selection rules and the pitfalls live in `references/`: which words are worth teaching, and the mistakes agents make (fabricated examples, word-for-word translations, all-caps subtitle artefacts).
- It never invents an example sentence. Every `example` must be quoted from the episode it came from.

## Quickstart

The tool needs Python 3.9+ and nothing else. No third-party packages, no build step.

```bash
# 1. Try it with the bundled demo, no subtitle files needed
python3 tools/demo.py

# 2. Create a workspace
python3 skills/grab-series-vocab/scripts/grab.py -w ~/series-vocab init

# 3. Point it at a folder of subtitles
python3 skills/grab-series-vocab/scripts/grab.py -w ~/series-vocab \
    scan ~/Downloads/NYPD.Blue.S01 --show "NYPD Blue" --count 100

# 4. Hand the generated batch prompt to a fresh agent
python3 skills/grab-series-vocab/scripts/grab.py -w ~/series-vocab next --batch 5

# 5. Ingest what the agent wrote back — validated line by line
python3 skills/grab-series-vocab/scripts/grab.py -w ~/series-vocab \
    ingest ~/series-vocab/out/jsonl/*.jsonl

# 6. Quality-check, then export
python3 skills/grab-series-vocab/scripts/grab.py -w ~/series-vocab check
python3 skills/grab-series-vocab/scripts/grab.py -w ~/series-vocab \
    export --format anki --mode safe --out out
```

`--mode safe` exports headword, gloss and IPA only, with no subtitle text — that is the version you may publish. `--mode full` keeps the example sentence, for local study only.

## How it works

**1. Library first** — Every entry goes into SQLite before it becomes a card. Exports are views over the library, so slicing "B2 and above" or "season 3 only" is a query, not a regeneration.

**2. Schema first** — The agent is only allowed to emit JSONL, one entry per line, validated against [`entry.schema.json`](skills/grab-series-vocab/schema/entry.schema.json). Bad lines land in `rejects/` and never block the rest of the batch.

**3. Deduplicated by construction** — Before dispatching work, the tool exports every headword already in the library as a blocklist and hands it to the agent. Duplicates are prevented at the source instead of cleaned up afterwards.

## The study method

A word list on its own does not teach you a word. This is how these corpora are meant to be used:

1. **Pull the corpus.** Take the corpus for a show you actually watch, in season and episode order.
2. **Drill in context.** Each card carries the season and episode the word came from. Register *where* it appeared, not just what it means.
3. **Watch it with the subtitles off.** After every four or five episodes of drilling, watch those same episodes without subtitles. This is the step that turns recognition into recall.
4. **Back to the corpus.** Anything that slipped, search in the web index and pull it into your own hard-words deck.

Spaced repetition is good at making you *remember*. The episode is what tells you *when to use it*. Stack the two and every word carries a scene with it.

Full guide: [English](docs/LEARNING-METHOD.md) · [简体中文](docs/LEARNING-METHOD.zh-CN.md)

## Repository layout

```
grab-series-vocab/
├── skills/grab-series-vocab/    # the agent skill — SKILL.md, schema, references
│   └── scripts/grab.py          # single-file CLI, standard library only
├── tools/
│   ├── matrix.json              # numbers, repo names and links for this matrix
│   ├── build_readmes.py         # generates every README from tools/i18n/
│   ├── i18n/                    # one prose module per language
│   ├── corpus_i18n/             # the same, for the corpus repositories
│   ├── build_corpus_docs.py     # adds READMEs, LICENSE and NOTICE to a corpus
│   ├── validate_matrix.py       # cross-links, local links, figures, privacy
│   ├── import_legacy.py         # normalises hand-made two-column CSVs
│   ├── build_corpora.py         # exports one directory per corpus repository
│   ├── sync_docs.py             # keeps docs/ figures in step with matrix.json
│   ├── audit_public.py          # blocks subtitle text and private paths
│   └── demo.py                  # end-to-end run on a bundled sample
├── examples/demo/               # sample subtitles + expected output
├── docs/
│   ├── INSTALL.md               # per-agent install, verify, troubleshoot
│   ├── LEARNING-METHOD.md       # the four-step study method (+ zh-CN)
│   ├── PIPELINE.md              # how subtitles become a corpus (+ zh-CN)
│   ├── MATRIX.md                # the matrix map, and how to add a show
│   └── CORPUS-CATALOG.md        # what each corpus contains
└── README.md + 6 translations
```

## Documentation

[Install guide](docs/INSTALL.md) · [Study method](docs/LEARNING-METHOD.md) · [Pipeline](docs/PIPELINE.md) · [Matrix map](docs/MATRIX.md) · [Corpus catalogue](docs/CORPUS-CATALOG.md) · [Notices](NOTICE.md) · [Contributing](CONTRIBUTING.md) · [Release audit](tools/audit_public.py)

## Known gaps

| Gap | Scale | Note |
|---|---:|---|
| Historical cards with no headword | 10,929 | The gloss is known, the English headword was lost. Queued in the NYPD Blue corpus, not silently merged. |
| Structurally broken cards | 28 | Missing or malformed trailing block. |
| Glosses are Chinese only | all | English and other glosses are the most useful thing to contribute. |
| Difficulty labels | all | `level` is unset, so `--min-level` filtering does not do anything yet. |
| The tool's own CLI output | all | `grab.py` prints progress and the agent dispatch prompt in Chinese. The corpus data, the documentation and the metadata are translated; the CLI is not yet. |

## Contributing

Bug reports, corrections and corpus requests are all welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). The single biggest help right now is the repair queue: 10,929 entries whose English headword needs recovering from the gloss and the IPA.

## License

Code, skill and documentation are **MIT** ([LICENSE](LICENSE)). Vocabulary data in the corpus repositories is **CC BY 4.0**. No repository in this matrix contains or distributes subtitle files, and no published dataset contains subtitle text or dialogue translations — only headwords, glosses and IPA.

## Credits

The capability direction was inspired by [`gbro-series-vocab`](https://github.com/pyang5166/gbro-series-vocab) by 狗哥笔记 (MIT). `grab-series-vocab` is an independent implementation: the architecture (library-first, SQLite corpus, schema validation, export modes, blocklist deduplication), the code and the documentation were written from scratch and share no code or text with it.

---

> **The matrix** · 🧰 **[grab-series-vocab](https://github.com/bannysway/grab-series-vocab)** ← *you are here* · 🚔 [tv-vocab-nypd-blue](https://github.com/bannysway/tv-vocab-nypd-blue) · ☕ [tv-vocab-friends](https://github.com/bannysway/tv-vocab-friends) · 🎹 [tv-vocab-your-lie-in-april](https://github.com/bannysway/tv-vocab-your-lie-in-april) · 👤 [@bannysway](https://github.com/bannysway)

If this saved you time, a ⭐ helps other people find it.

Corrections and new corpora are welcome — open an issue.
