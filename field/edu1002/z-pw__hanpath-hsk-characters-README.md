# HSK 3.0 Chinese characters & word lists — machine-readable

A clean, dependency-free dataset of **every Chinese character used by the HSK 3.0 word
lists (levels 1–6)**, with pinyin, radical, stroke count and HSK level — plus the full
**HSK 3.0 word lists by level** (word, pinyin, frequency rank).

No definitions. No share-alike obligations. Just the facts, in JSON and CSV.

```
1,804 characters   ·   10,993 words   ·   2 files you can load in one line
```

Maintained alongside [**HanPath**](https://hanpathhub.com) — a free Chinese-learning site
that explains Chinese **in the learner's own language** (13 language editions).

---

## What's in here

| File | What it is |
|---|---|
| `data/hsk-characters.json` | 1,804 characters: `char`, `pinyin`, `radical`, `strokes`, `hsk_level` |
| `data/hsk-characters.csv` | The same table as CSV (UTF-8, no BOM, LF) |
| `data/hsk-words-by-level.json` | HSK 3.0 words by level: `word`, `pinyin`, `freq_rank` |
| `data/summary.json` | Counts only — read this first if you just need to know the shape |

### Character counts by HSK level

| HSK level | Characters |
|---|---|
| 1 | 300 |
| 2 | 298 |
| 3 | 301 |
| 4 | 300 |
| 5 | 300 |
| 6 | 300 |
| outside HSK 1–6 (level `0`) | 5 |
| **total** | **1,804** |

### Word counts by HSK level

| HSK level | Words |
|---|---|
| 1 | 511 |
| 2 | 755 |
| 3 | 959 |
| 4 | 972 |
| 5 | 1,061 |
| 6 | 1,126 |
| 7 (combined 7–9) | 5,609 |
| **total** | **10,993** |

---

## What `hsk_level` means

The level of a character is **derived, not hand-assigned**: each HSK level's word list is
scanned, and a character takes the **lowest** level whose word list uses it.

- Levels are cumulative in the official standard, so taking the minimum is the only
  assignment that answers *"the first level at which I must know this character"*.
- `hsk_level: 0` means the character is **not** used by any HSK 1–6 word list.
  It exists in the source set for other reasons (classical poetry and phrase corpora).
  Treat `0` as "outside the standard", **not** as "harder than level 6".

---

## Usage

```js
const fs = require("fs");
const { characters } = JSON.parse(fs.readFileSync("data/hsk-characters.json", "utf8"));

// all level-1 characters, easiest strokes first
const l1 = characters.filter(c => c.hsk_level === 1);

// which level must you reach before you can write 赢 ?
const w = characters.find(c => c.char === "赢");
console.log(w); // { char: '赢', pinyin: 'yíng', radical: '贝', strokes: 17, hsk_level: 6 }
```

```python
import json, csv

chars = json.load(open("data/hsk-characters.json", encoding="utf-8"))["characters"]
by_level = {}
for c in chars:
    by_level.setdefault(c["hsk_level"], []).append(c["char"])
```

**Pinyin** is given with tone marks (not numbers): `nǐ`, `lǜ`, `ér`.
**Radicals** are single characters in the form they take when they appear as a component
(`忄`, `氵`, `讠`), not the standalone dictionary form.

---

## Why there are no definitions

Two deliberate omissions, both about licensing:

1. **No CC-CEDICT definitions.** CEDICT is CC BY-SA 4.0. Shipping its text would put a
   share-alike obligation on this whole dataset, which is the single fastest way to make
   a dataset useless to other developers. If you want definitions, take them from
   [CC-CEDICT](https://cc-cedict.org/) directly and accept its licence knowingly.
2. **No 13-language glosses.** The per-language meanings we publish on HanPath are our own
   writing and are not part of this dataset.

What *is* here is factual: character, pronunciation, radical, stroke count, and a level
assigned by a documented rule from a published standard.

---

## Provenance

| Layer | Source |
|---|---|
| Character list, pinyin, radical, stroke count | HanPath |
| HSK level assignment | Derived from the published HSK 3.0 word lists |
| HSK 3.0 word lists (`word`, `pinyin`, `freq_rank`) | [TheOpenDictionary/complete-hsk-vocabulary](https://github.com/TheOpenDictionary/complete-hsk-vocabulary) (MIT) |

The HSK 3.0 standard (国际中文教育中文水平等级标准) is published by the Chinese
Ministry of Education's Center for Language Education and Cooperation.

---

## Licence

- **`data/hsk-characters.json`, `data/hsk-characters.csv`, `data/summary.json`** —
  **CC0 1.0** (public domain dedication). Use them for anything; no attribution required.
- **`data/hsk-words-by-level.json`** — **MIT**, with the upstream attribution above.
  (It is MIT rather than CC0 because the word list is redistributed from an MIT project.)

Attribution is welcome but not required. If you use this in something public, a link to
[hanpathhub.com](https://hanpathhub.com) is appreciated.

## Corrections

Radical assignments follow 《新华字典》 where the source data disagrees with it. If you
find a wrong radical, stroke count or level, please open an issue — fixes are applied to
the dataset and to the site together.
