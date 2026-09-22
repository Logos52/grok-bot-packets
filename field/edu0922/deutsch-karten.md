# Deutsch Karten

A German vocabulary dataset (**5,684 words, A1–C2**, curriculum-ordered) and a solo Android
flashcard app built on it. Swipe to grade, hear every word and sentence, always know where you are.

<p align="center">
  <img src="app-android/screenshots/30-phone-home.png" width="24%" alt="Home: level progress, streak, six CEFR levels"/>
  <img src="app-android/screenshots/71-onboarding-first-launch.png" width="24%" alt="First-run placement: pick your level from real sample words"/>
  <img src="app-android/screenshots/45-phone-card-back-redesign.png" width="24%" alt="Card back: meaning, example, verb forms"/>
  <img src="app-android/screenshots/31-phone-tts-controls.png" width="24%" alt="Hear the word, the sentence and every verb form"/>
</p>

## What's here

| Path | What it is |
| --- | --- |
| `out/german_vocab_a1_c2.csv` | The dataset — one row per word, `source`-tagged (5,684 rows) |
| `out/german_vocab_a1_c2.json` | Same data with all senses and a meta block |
| `out/anki_import.csv` | Ready to import into Anki |
| `app-android/` | The Android app (Kotlin + Jetpack Compose) — see [its README](app-android/README.md) |
| `build.py` | Pipeline that builds the dataset from the upstream sources |
| `gloss_coverage.py` | Feasibility study for word-by-word glosses (96.6% token coverage) |
| `fetch_sources.sh` | Downloads the upstream sources into `raw/` |
| `sync_asset.sh` | Copies the generated CSV into the app's assets |

## The dataset

**Ordering is the point:** level first (A1 → C2), commonality second. A learner meets the most
frequent words of their level before the rarer ones.

| Level | Words | Source |
| --- | --- | --- |
| A1 | 655 | Goethe 5000 |
| A2 | 590 | Goethe 5000 |
| B1 | 1,826 | Goethe 5000 |
| B2 | 1,938 | Goethe 5000 |
| C1 | 355 | wordfeather |
| C2 | 320 | wordfeather |

Each row carries article, plural, English gloss, IPA, example sentence **with its English
translation**, verb conjugation, an audio URL for the word, a thematic category, and stable `id` +
`content_version` columns so a client can rebuild the list without losing the user's progress.

| Coverage | |
| --- | --- |
| English gloss | 5,682 / 5,684 |
| example DE + EN | 5,684 / 5,684 |
| IPA | 5,435 / 5,684 |
| pronunciation audio | 5,404 / 5,684 |

## Quick start

```bash
# use the data
head -3 out/german_vocab_a1_c2.csv

# rebuild it from scratch
./fetch_sources.sh      # ~50 MB of upstream files into raw/
python3 build.py        # queries de.wiktionary.org, batched and cached
./sync_asset.sh         # copy the result into the Android app

# build the app
cd app-android && ./gradlew assembleDebug     # -> app/build/outputs/apk/debug/app-debug.apk
```

`build.py` needs only Python 3.9+ — no packages. It is polite to the Wikimedia API (batched
requests, backoff on HTTP 429).

## Data repairs worth knowing about

The upstream Goethe export had **two systematic errors in every present-tense table**, both found by
rendering the forms as a table and both confirmed against wordfeather's independent conjugation data:

* the `ihr` form repeated the `er/sie/es` form for strong verbs — `ihr isst` instead of *esst*,
  `ihr gibt` instead of *gebt* (144 of 480 verbs);
* `du` lost the `-t-` for stems ending in `-d/-t` — `du hälst` instead of *hältst*.

`repair_present_tense()` in `build.py` fixes both, only overriding the upstream value when the
derivation is unambiguous, and preserving separable prefixes (`ich sehe aus` → `ihr seht aus`).

## Licences

**The code is MIT. The data is not** — it is assembled from four sources under three licences, and
the C1/C2 layer is **non-commercial**. Every row is tagged in the `source` column so you can separate
the layers; see **[LICENCE-DATA.md](LICENCE-DATA.md)** for the full breakdown.

Short version: study with it, fork it, share it — but do not sell it or run ads against it, because of
the CC BY-NC 4.0 C1/C2 content. For a commercially usable subset, keep `source == "goethe-5000"`.

## Caveats

* A1–B2 example sentences come from the source Anki deck and their English translations are machine
  translations — a reading aid, not a reference. C1/C2 examples are from wordfeather and read more
  naturally.
* English glosses follow the source lists and can bundle several meanings (`der` → `the; that, those;
  who, that`).
* The 30% of C1/C2 entries that are multi-word phrases (idioms like *das A und O*) can be filtered on
  `word` containing a space.
* `DDR` (B1) and `SPÖ` (B2) are the only rows without an English gloss.
