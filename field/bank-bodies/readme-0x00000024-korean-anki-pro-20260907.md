# Korean Anki Pro

Generates Anki flashcard decks for Korean vocabulary, in frequency order, with
LLM-written dictionary content, Google TTS audio, and one generated
illustration per example sentence.

It is the Korean sibling of `french-anki-pro` and keeps the same architecture,
so fixes made in one project usually port to the other.

## What a card contains

Front: the word form, its example sentence, the illustration, and buttons that
play the word and sentence audio.

Back: a generated dictionary entry with basic info (romanization, dictionary
form, part of speech, word origin, Hanja where applicable, attached
particle/ending, politeness level), pronunciation including sound changes, a
three-language example sentence (한국어 / English / 繁體中文), an eojeol-by-eojeol
grammar breakdown, a usage-frequency chart, and etymology.

Tapping any word in the pronunciation and grammar tables plays its audio.

## Install

```bash
uv sync --extra dev
cp .env.example .env
```

## Generate

```bash
# First 20 words.
uv run korean-anki-pro --word-limit 20 --output outputs/topik_i_001_020.apkg

# A later block: skip 20, take the next 20.
uv run korean-anki-pro --word-offset 20 --word-limit 20 \
  --output outputs/topik_i_021_040.apkg --keep-audio --keep-images --resume
```

`--word-offset` both skips leading entries and selects the 20-word deck block
that receives the cards, so batches land in the right place in the tree.

Import the resulting `.apkg` with Anki.

## Deck structure

```text
한국어능력시험 TOPIK I - 초급 - 1000
└── 01 빈도 순위 (001-100)
    ├── 01 빈도 블록 (001-020)
    ├── 02 빈도 블록 (021-040)
    └── ...
```

Ten frequency ranges of 100 words, each split into five blocks of 20.

## Frequency data

The default list is built from the OPUS OpenSubtitles v2024 Korean corpus.
Entries are **eojeol** — a content word plus any attached particle or ending —
so `내가` and `거야` are their own rows. See `docs/data-sources.md` for the
method and for what that means when planning how many cards you need.

Rebuild it with:

```bash
uv run python scripts/build_frequency_list.py
```

## Configuration

Copy `.env.example` and adjust. Notable settings:

| Variable | Purpose |
|---|---|
| `OPENAI_BASE_URL` | Text generation endpoint (defaults to the local hub) |
| `KOREAN_ANKI_IMAGE_API_BASE_URL` | Illustration hub |
| `KOREAN_ANKI_MEDIA_CONCURRENCY` | Keep at `1`; concurrent image requests deadlock the hub |
| `KOREAN_ANKI_DECK_NAME` | Root deck name |
| `KOREAN_ANKI_MODEL_ID` | Anki notetype id (distinct from the French deck's) |

## Tests

```bash
uv run pytest
```

## License

MIT
