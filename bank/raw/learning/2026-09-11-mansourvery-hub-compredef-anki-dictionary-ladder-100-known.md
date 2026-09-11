---
id: 2026-09-11-mansourvery-hub-compredef-anki-dictionary-ladder-100-known
kind: article
title: CompreDef Anki dictionary ladder 100% known-kanji early exit
source: "https://github.com/mansourvery-hub/CompreDef"
author: mansourvery-hub
published: 2026-09-11
captured: 2026-09-11
via: grok-bot/Field
lane: learning
status: raw
private: false
---

===== README.md =====
# CompreDef

Anki add-on for automatically generating Japanese vocabulary definitions strictly tailored to your known vocabulary and kanji levels.

**[Download from AnkiWeb](https://ankiweb.net/shared/info/1619602654)**

## Core Concept: The Dictionary Ladder

CompreDef frees you from the circular lookup trap of Japanese monolingual dictionaries by searching your dictionaries in an **ordered ladder** — and the order is yours to choose:

- Dictionaries are tried **top to bottom** in the exact order you configure.
- The first dictionary whose definition is **fully comprehensible to you** (100% of its kanji on your mature cards) wins — the search stops there (early exit).
- If none passes, the definition with the highest comprehension score is used (maximal fallback).

**Recommended setup:** put the **richest dictionary you can comfortably read at the top** (e.g. 三省堂国語辞典), with simpler ones (e.g. 小学館例解学習国語) below as fallback. You get the richest definition you can actually read, falling back to simpler dictionaries exactly when needed — and as your kanji knowledge grows, more words naturally come from the richer sources.

> The comprehension gate counts kanji characters only; kana words are not checked — so order the ladder by what you can genuinely read, not just decode.

> For an in-depth mathematical specification and flowcharts, see the [Algorithm Specification Wiki (WIKI.md)](WIKI.md).

---

## Features

- **Dictionary Ladder GUI**: Add, remove, and reorder dictionaries using Move Up/Down buttons or native Drag-and-Drop.
- **Folder Auto-Scanner**: Point CompreDef at a folder containing multiple unzipped Yomitan dictionaries to auto-detect and add all of them.
- **ZIP Archive Support**: Add Yomitan dictionaries directly as `.zip` files for zero-disk footprint and instant loading.
- **Auto-Matching Fields**: Automatically detects and maps your Target Word (`Expression`, `Word`) and `Definition` fields.
- **Card Editor Button**: One-click definition generation directly inside Anki's card editor toolbar.
- **Bulk Generation**: Generate definitions for hundreds of selected cards at once from the Anki Browser (via `Edit -> Generate CompreDef Definitions...` or `Ctrl+Shift+D`).
- **Independent Disk Caching**: Each dictionary is parsed once and cached in `user_files/cache/dictionaries.db`, enabling instant (0.08ms) B-tree lookups and instant reordering without re-parsing.
- **100% Faithful Yomitan HTML**: Renders rich Yomitan structured-content with `<ruby>`, `data-sc-*` attributes, inline CSS, and `用例` blocks directly into Anki notes.

---

## Installation

1. Download or build `CompreDef.ankiaddon` (see **Testing & Local Installation** below).
2. In Anki: **Tools → Add-ons → Install from file...** → select it → restart Anki.
3. Configure your Note Type and Dictionaries under **Tools → Add-ons → CompreDef → Config**.

---

## Configuration

1. **Note Types & Field Mappings**: Check every note type CompreDef should
   generate definitions for (e.g., `Japanese`, `Mining`, `Animecards`).
   Select a type's row to map its fields — each type keeps its **own**
   Word / Reading / Definition fields, auto-matched from the type's
   schema. Unchecked types are ignored by generation.
2. **Dictionary Ladder**:
   - Click **Add Zip Archive...** to select a Yomitan `.zip` file.
   - Click **Add Folder...** to select an unzipped dictionary folder.
   - Click **Scan Folder...** to select a parent folder containing multiple dictionaries (both `.zip` files and subfolders).
   - Use **Move Up ↑** and **Move Down ↓** (or drag and drop) to position simpler dictionaries at the top and advanced dictionaries at the bottom.

---

## Testing & Local Installation

Run the regression suite (no Anki/PyQt needed — the Anki API is stubbed automatically; real-dictionary smoke tests self-skip if the dictionaries are absent):

```bash
python3 tests/test_regression.py
```

Build the installable package to test the current code in Anki:

```bash
./scripts/build.sh        # → dist/CompreDef.ankiaddon
```

Then install it: **Anki → Tools → Add-ons → Install from file...** → select `dist/CompreDef.ankiaddon` → restart Anki.

Prefer a live checkout while developing? Symlink the repo instead of installing the package:

```bash
ln -sfn /path/to/CompreDef ~/.local/share/Anki2/addons21/CompreDef
```

For test + commit + push + full release in one go:
```bash
./scripts/ci.sh          # → GitHub Release + AnkiWeb upload via CI
```
For a full release with an explicit version:
```bash
./scripts/release.sh [vX.Y.Z]
```

**Testing a released change (no manual installs):**
1. Restart Anki — the add-on update check fires.
2. Anki detects the new version → "Update All" / auto-installs (~1s download).
3. Restart Anki again — the new code is active.
4. Test the feature.

The regression suite verifies (among others) that definitions stay **rich Yomitan HTML** (never plain text), furigana readings never pollute kanji scoring, the dictionary ladder respects user order and exits early on the first fully comprehensible dictionary, cross-reference titles lose to real definitions, `.zip` archives produce byte-identical output to their unzipped folders, and Tab-to-Generate never overwrites an existing definition.

---

## Architecture & Code Structure

```
CompreDef/
├── __init__.py         # Add-on entry point & hook registration
├── gui.py              # Config dialog, Scope picker, Learner Knowledge window
├── editor_browser.py   # Editor button, Tab-to-Generate, Browser bulk actions
├── core.py / engine.py # Wiring/singletons; Dictionary Ladder algorithm
├── scoring.py          # Interval-weighted kanji/vocab scoring + filters
├── anki.py             # Learner-knowledge snapshot (native DB wrapper only)
├── scope.py            # Deck Scope (drives generation + knowledge)
├── provider.py         # DictionaryProvider interface + SQLite implementation
├── renderer.py / models.py / utils.py  # Yomitan HTML, data types, helpers
├── parser.py           # Compat layer over provider/renderer/utils
├── yomitan.py / yomitan_installer.py    # Optional Yomitan-API source + bridge
├── PRODUCT.md / MVP.md / ARCHITECTURE.md / QUALITY.md  # What / scope / how / invariants
├── TEST_STRATEGY.md / IMPLEMENTATION_PLAN.md / AGENTS.md  # Verification / work / agent ops
├── tests/
│   └── test_regression.py  # Fundamental regression suite (run before committing)
├── debug/              # On-demand diagnostics (never shipped, never in CI)
├── icons/              # UI toolbar icons (compredef.svg)
├── config.json         # Default configuration settings
└── WIKI.md             # In-depth algorithm & architecture wiki
```

---

## Development & Safety Rules

- **CI/CD**: Use `./scripts/ci.sh` for testing and pushing, and `./scripts/release.sh` for tagged releases.
- **AnkiWeb Publishing**: Upon creating a GitHub Release, the `danny900714/upload-anki-addon` action automatically updates the [AnkiWeb listing (1619602654)](https://ankiweb.net/shared/info/1619602654). Ensure `ANKI_WEB_USERNAME` and `ANKI_WEB_PASSWORD` secrets are configured in the repository.
- **Native DB Access Only**: Never open `collection.anki2` with raw sqlite3. CompreDef strictly uses `mw.col.db` to prevent database locks.
- **Non-Blocking Concurrency**: All dictionary parsing and scoring operations execute in background threads using `mw.taskman.run_in_background()`.
- **PyQt Compatibility**: Imports use `aqt.qt` for multi-version Qt compatibility.
- **SQLite Caching**: Dictionary lookups use indexed B-tree tables in `user_files/cache/dictionaries.db` for ~0.08ms performance with 0MB RAM footprint.

---

## License

GNU General Public License v3 or later.

===== WIKI.md =====
# CompreDef Wiki - Algorithm & Architecture Specification

## Overview

CompreDef is designed around Stephen Krashen's **$i+1$ Comprehensible Input Hypothesis**: language acquisition occurs most effectively when learners are exposed to messages that are slightly beyond their current level, but still almost entirely comprehensible.

Traditional Japanese-Japanese (国語) dictionaries (like 大辞林, 大辞泉, or 広辞苑) frequently define target words using obscure literary vocabulary or unlearned kanji. For a beginner or intermediate learner, looking up a word in such a dictionary creates an infinite lookup loop. Conversely, children's dictionaries (like 例解学習国語) provide simpler explanations using elementary kanji and grammar, but lack coverage of advanced terms.

CompreDef solves this deterministically through the **Dictionary Ladder with Early Exit & Kanji Matrix Scoring**.

---

## 1. The Algorithm

```mermaid
flowchart TD
    Start([User Requests Definition for Target Word]) --> ScanDB[Scan Anki DB for Known Kanji<br>Cards with interval > 0]
    ScanDB --> LoopDicts[Inspect Next Dictionary in User Ladder Order]

    LoopDicts --> LookupWord{Does Dictionary<br>contain Target Word?}
    LookupWord -- No --> HasMoreDicts{More Dictionaries<br>in Ladder?}

    LookupWord -- Yes --> FilterRefs[Filter out cross-reference titles]
    FilterRefs --> ScoreDefs[Score each Definition in Dictionary<br>Score = Known Base Kanji / Total Base Kanji]

    ScoreDefs --> Check100{Any Definition<br>has Score = 1.0?<br>100% Known Kanji}

    Check100 -- Yes --> EarlyExit([EARLY EXIT: Return Definition Immediately!<br>Skip all subsequent dictionaries])

    Check100 -- No --> TrackBest[Update Maximal Definition if<br>Score > Best Score so far]
    TrackBest --> HasMoreDicts

    HasMoreDicts -- Yes --> LoopDicts
    HasMoreDicts -- No --> ReturnMaximal([Return Maximal Definition<br>Least complicated candidate found])
```

### Step-by-Step Execution

1. **Known Kanji Extraction (The Kanji Matrix)**:
   - The add-on queries Anki's native database:
     ```sql
     SELECT DISTINCT notes.id, notes.flds
     FROM notes
     JOIN cards ON notes.id = cards.nid
     WHERE cards.ivl > 0
     ```
   - Only cards with `interval > 0` are analyzed (ensuring only reviewed/retained material is counted as "known").
   - A compiled C-level regular expression `[\u4e00-\u9fff]` extracts all kanji from the field blobs in **0.18 seconds** across 60,000+ card rows.
   - The result is a set $\mathcal{K}_{\text{known}}$ of all kanji the learner currently knows.

2. **The Dictionary Ladder Traversal**:
   - The user arranges their installed dictionaries in any order they prefer — order is a *preference*, not a difficulty rating:
     1. **Recommended top rung**: the richest dictionary the user can comfortably read (e.g., 三省堂国語辞典) — its definitions win whenever they pass the comprehension gate.
     2. **Fallback rungs**: progressively simpler dictionaries (e.g., 小学館例解学習国語) that catch words the richer sources explain with too-difficult kanji.
   - The generator iterates through this ladder **one dictionary at a time**.

3. **HTML Processing for Scoring**:
   - Before scoring, definitions are processed to extract **base text** for comprehension scoring:
     - Strip all `<rt>` (furigana) and `<rp>` tags.
     - Remove remaining HTML tags.
     - Unescape HTML entities.
   - This ensures only base kanji are counted for the Kanji Matrix Scoring, while the full rich HTML with furigana is preserved for Anki display.

4. **Candidate Filtering**:
   - Short cross-reference headwords (e.g., `"会社更生法"`, `"参照"`) that do not contain sentence punctuation (`。`, `、`) are filtered out so that real explanatory sentences are always selected.

5. **Kanji Comprehension Scoring**:
   - For every candidate definition HTML string $D$, let $K(D)$ be the multiset of kanji characters appearing in $D$ (base text only, no furigana).
   - The comprehension score $S(D)$ is calculated as:
     $$S(D) = \begin{cases} 1.0 & \text{if } |K(D)| = 0 \\ \frac{\sum_{c \in K(D)} [c \in \mathcal{K}_{\text{known}}]}{|K(D)|} & \text{if } |K(D)| > 0 \end{cases}$$
   - Pure hiragana/katakana definitions have $S(D) = 1.0$ (fully readable).

6. **Early Exit (Short-Circuit Evaluation)**:
   - If a definition yields $S(D) = 1.0$ (100% of the kanji are known):
     - **The loop immediately halts and returns that definition.**
     - Dictionaries further down the ladder are **never queried**.
     - **Benefits**:
       - *Comprehension-tailored*: The learner receives the preferred (top-of-ladder) dictionary's definition whenever they can fully read it, and falls back to simpler rungs exactly when they cannot. Since $S(D)$ measures kanji only — kana words are not checked — the ladder order is the user's control for stylistic difficulty.
       - *Computational*: Avoiding further lookups keeps execution time at **0.05 seconds**.

7. **The Maximal Fallback**:
   - If no dictionary in the entire ladder yields a 100% match, the algorithm returns the candidate definition with the highest comprehension score $S(D)$ found across all evaluated dictionaries.
   - This fallback is **order-independent**: every dictionary contributes its best candidate, and the highest score wins regardless of ladder position.
   - This ensures the learner always receives the **least complicated definition available**.

---

## 2. SQLite-Cached Dictionary Indexing

CompreDef now uses **SQLite caching** for dictionary lookups instead of pickle files, providing faster B-tree lookups with zero RAM footprint.

### Dictionary Sources

CompreDef supports both:
- **Unzipped Directories**: Contains `term_bank_*.json` files and `index.json` metadata.
- **ZIP Archives**: Yomitan `.zip` dictionaries loaded directly from compressed archives (zero-disk footprint, instant access).

### SQLite Database Structure

The cache database (`user_files/cache/dictionaries.db`) contains:
- `dictionaries` table: Stores dictionary path, title, signature, and entry count.
- `entries` table: Maps `(dict_path, term)` to rich HTML definitions.

### Cache Invalidation

- **Signature**: Computed from dictionary source (file modification times and sizes for folders, mtime + size for ZIPs).
- **Update Trigger**: When dictionary files change, the signature updates, triggering re-indexing.
- **Performance**: First lookup (~0.5s) indexes the dictionary; subsequent lookups are **instant (0.08ms)** via indexed B-tree queries.

### Yomitan HTML Rendering

CompreDef renders 100% faithful Yomitan structured-content:
- **Ruby Furigana**: `<ruby>` tags with `<rt>` readings preserved for Anki display.
- **Data Attributes**: `data-sc-*` attributes for accessibility and tooling.
- **Inline CSS**: Yomitan's `style` field converted to inline CSS (e.g., `fontSize: 14em` becomes `font-size: 14em`).
- **Special Tags**: `<data-sc-name="用例">` for example sentences.
- **Rich Elements**: `<span class="gloss-sc-span">`, `<div class="gloss-sc-div">`, table cells with `colSpan`/`rowSpan`.
- **Output**: Full HTML with all styling and semantics for direct insertion into Anki note fields.

---

## 3. Database Safety Mandate

In strict accordance with Anki development standards:
- **No Direct SQLite Connections**: External sqlite3 connections to `collection.anki2` can cause database corruption and SQLite locks. CompreDef exclusively accesses the database through Anki's native Python wrapper: `mw.col.db.all()`.
- **Non-Blocking Background Threads**: All dictionary searches, scoring calculations, and database scans execute asynchronously using `mw.taskman.run_in_background()` with a completion callback to the main thread.

---

## 4. Regression Testing Mandate

The fundamental regression suite lives at `tests/test_regression.py` and **must be run green before every commit** (`python3 tests/test_regression.py`). Each test maps to a real historical bug:

| Historical bug | Guarding test |
|---|---|
| Plain-text definitions (121 chars) served instead of rich Yomitan HTML (~7000 chars) | `test_structured_content_html_fidelity` + real-dictionary `先ず` smoke test |
| Renderer upgraded but SQLite cache kept serving stale plain text forever | `test_renderer_version_invalidates_cache` (verifies `RENDERER_VERSION` is embedded in signatures) |
| Furigana `<rt>` readings polluted the kanji comprehension score | `test_scoring_ignores_furigana` |
| Ladder fell through to an advanced dictionary despite a simpler comprehensible definition | `test_ladder_early_exit_order` |
| Cross-reference titles ("see also") won over real definitions | `test_reference_title_filtering` |
| ZIP archive and unzipped folder produced different output | `test_zip_folder_parity` |
| `data-sc-*` attributes drifted from Yomitan's DOM naming (breaking the user's CSS compactor) | `test_data_sc_attribute_names` |
| Nonsense word `駿ってさ` froze Anki at 100% CPU and crashed it | `test_nonsense_word_returns_none_fast` |
| Indexing accumulated ~1.3 GB of rendered HTML in RAM (OOM freeze on giant dictionaries like 大辞泉) | `test_indexing_streams_in_batches` (verifies bounded `_INDEX_BATCH_SIZE` + streamed commits) |
| SQLite connections never closed (`with conn:` commits but does not close), leaking a handle per lookup | `test_db_connections_are_closed` |
| Renderer upgrade left duplicate/orphan rows behind | `test_renderer_upgrade_reindexes_cleanly` |

The suite stubs `aqt` so it runs on both system Python and Anki's bundled Python without Anki installed. Smoke tests against the real installed dictionaries self-skip when those dictionaries are absent.

## 5. On-Demand Debugging

Beyond the per-commit suite, `debug/` holds the learner-knowledge
snapshot spec (SP1–SP6), use cases (U1–U5), copy-paste Debug Console
recipes for the live collection (`console_snippets.md`), and a
standalone sanity script (`python3 debug/sanity_knowledge.py`) that is
deliberately **not** run by CI — it is for triage when something looks
wrong (e.g. 0 known kanji after an Anki upgrade).
