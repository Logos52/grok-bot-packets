# 🇩🇰 Danish A1-A2 Complete Anki Deck & Learning System

**Study goal: A1 → PD2 by June 2027.** Start with the [current study overview](OVERVIEW.md) and [Anki review/import guide](study/ANKI_REVIEW.md). The existing package is a vocabulary foundation; the overview adds speaking, listening, reading, writing and exam checkpoints.

The [24-card skills starter](study/pd2_skills_starter.tsv) is an optional separate Basic-note import. Your existing package has not been changed. Topic counts below are **notes**, with two cards per note.

An all-in-one, beautifully-styled Danish language learning system for **Anki**. Designed specifically for English speakers starting from complete beginner (A1) progressing through elementary (A2) to intermediate (B1/B2).

---

## ⚡ Quick Start: How to Import into Anki

You have two convenient ways to import your cards into Anki:

### Option A: 1-Click Package Import
1. Open **Anki** on your computer.
2. Double-click [`danish_a1_a2_complete.apkg`](file:///Users/unicorn/Documents/AI-Workspace/Anki/danish_a1_a2_complete.apkg) (or click **File** → **Import...** inside Anki and choose `danish_a1_a2_complete.apkg`).

### Option B: Terminal Import (Fastest & Zero-Click)
You can import directly from your terminal using any of these commands:

```bash
# Method 1 (Built-in tool - silent 1-click import via AnkiConnect):
python3 generate_deck.py import

# Method 2 (macOS native open command):
open danish_a1_a2_complete.apkg

# Method 3 (Direct cURL via AnkiConnect API):
curl -s http://localhost:8765 -d '{"action": "importPackage", "version": 6, "params": {"path": "'"$PWD"'/danish_a1_a2_complete.apkg"}}'
```

### Option C: Direct Text / TSV Import
If your version of Anki prefers raw text import:
1. In Anki, go to **File** → **Import...**
2. Choose [`danish_a1_a2_cards.txt`](file:///Users/unicorn/Documents/AI-Workspace/Anki/danish_a1_a2_cards.txt).
3. Copy all `.m4a` files from the [`media/`](file:///Users/unicorn/Documents/AI-Workspace/Anki/media) folder into your Anki user `collection.media` folder.

---

## 📂 Included Decks & Curriculum

The package is hierarchically structured under the main deck **`Danish A1-A2 (Dansk for Begyndere)`**:

| Subdeck Name | Focus Areas & Contents | Cards | Level |
| :--- | :--- | :---: | :---: |
| **`01 - Core High-Frequency & Essentials`** | Top functional particles, question words (*hvad, hvem, hvor, hvornår*), conjunctions (*og, men, fordi*), pronouns, prepositions | 51 | `!Level::A1` |
| **`02 - Essential Verbs & Conjugations`** | Most common verbs with **bold irregular past/perfect forms** (*være, have, gå, spise, kunne, ville, skulle...*) | 52 | `!Level::A1`, `!Level::A2` |
| **`03 - Everyday Nouns (en & et with Plurals)`** | Essential nouns explicitly coded by gender (`en` vs `et`) with **bold irregular mutated plurals** (*børn, bøger, mænd*) | 40 | `!Level::A1` |
| **`04 - Numbers, Time, Days & Dates`** | Cardinal numbers (0–100), days of the week (*mandag–søndag*), time expressions, telling the time | 37 | `!Level::A1` |
| **`05 - Conversation, Greetings & Small Talk`** | Everyday social phrases, introductions (*Hvad hedder du?*), asking for help, polite expressions | 29 | `!Level::A1` |
| **`06 - Food, Drink & Daily Routine`** | Breakfast, lunch, dinner, grocery shopping, café & restaurant vocabulary | 24 | `!Level::A1`, `!Level::A2` |
| **`07 - Common Adjectives & Opposites`** | Core descriptive adjectives with regular/irregular comparatives (*god/dårlig, stor/lille, varm/kold...*) | 25 | `!Level::A1`, `!Level::A2` |
| **`08 - People, Family, Home & Places`** | Family members, parts of the house, rooms, city navigation and public places | 25 | `!Level::A1`, `!Level::A2` |
| **`09 - Custom & Vocabulary Expansion`** | Your custom vocabulary added over time via CLI or CSV | 2+ | Custom |
| **`10 - Essential Sentences & Syntax Patterns`** | Core conversational frames: modal verbs (*vil gerne*), V2 time inversion (*i dag skal jeg*), negation (*ikke*), supermarket phrases | 27 | `!Level::A1`, `!Level::A2` |
| **`11 - Work, Employment & Office Life`** | Applications, CV, interviews, boss, salary, workplace rights, unions (*fagforening, a-kasse*) | 22 | `!Level::A2`, `!Level::B1` |
| **`12 - Public Services, Health & Society`** | Living in Denmark: *sundhedskort, CPR, MitID, kommune, borgerservice, skat, NemKonto, lejekontrakt* | 16 | `!Level::A2`, `!Level::B1` |
| **`13 - Transport, Travel & City Navigation`** | Public transit: *Rejsekort, S-tog, metro, cykelsti, forsinkelse, perron, tjekke ind/ud* | 18 | `!Level::A1`, `!Level::A2` |
| **`14 - Weather, Seasons & Hygge Culture`** | Climate (*blæst, solskin, sne, regnfrakke*), four seasons, Danish holidays (*jul, påske*), and *hygge* | 16 | `!Level::A1`, `!Level::A2` |
| **`15 - Connectors, Logic & Discourse Adverbs`** | Transition words: *derfor, fordi, selvom, alligevel, desuden, faktisk, heldigvis, desværre, især* | 19 | `!Level::A2`, `!Level::B1` |

| **`16 - Housing Neighbourhood & Community`** | Renting, neighbours, house rules, repairs, shared facilities and community participation | 20 | `!Level::B1` |
| **`17 - Education Childcare & Leisure`** | Courses, exams, language learning, childcare, interests and participation | 20 | `!Level::B1` |
| **`18 - Health Body & Emergencies`** | Symptoms, appointments, treatment, body parts and urgent situations | 20 | `!Level::B1` |
| **`19 - Shopping Digital Life & Environment`** | Returns, complaints, budgeting, websites, MitID problems and sustainability | 20 | `!Level::B1` |
| **`20 - PD2 Speaking & Writing Functions`** | Opinion, narration, comparison, picture description, interaction and semi-formal writing frames | 33 | `!Level::B1` |

**Total Package:** **516 Curated Notes (1,032 Dynamic Cards)** across **20 Subdecks**. The [PD2 vocabulary coverage audit](study/PD2_VOCABULARY_AUDIT.md) explains what is covered and what still requires live exam practice. (See [`EXPANSION_LOG.md`](file:///Users/unicorn/Documents/AI-Workspace/Anki/EXPANSION_LOG.md) and [`OVERVIEW.md`](file:///Users/unicorn/Documents/AI-Workspace/Anki/OVERVIEW.md))

---

## 🗂 Dual-Card Anatomy & Layout

Each note automatically generates two complementary learning cards based on spaced-repetition cognitive science:
1. **Card 1: Receptive Recognition (🇩🇰 Dansk ➔ 🇬🇧 Engelsk)**: Builds reading and listening comprehension.
2. **Card 2: Active Production (🇬🇧 Engelsk ➔ 🇩🇰 Dansk)**: Prompts with the English concept and a contextual sentence cloze (`[ ... ]`), training you to actively produce Danish words in speech and writing.

All cards are styled with modern responsive HTML5 & CSS supporting Light Mode, Dark Mode (`.nightMode`, `.night_mode`, and `@media (prefers-color-scheme: dark)`), and mobile touch screens:

### 🎴 Front Side
- **Direction Badge**: Clear indicator (`🇩🇰 ➔ 🇬🇧 Genkendelse` or `🇬🇧 ➔ 🇩🇰 Aktiv Produktion`).
- **Grammatical Tag / Badge**: Color-coded part of speech indicator:
  - 🔵 **Blue badge**: Common Gender Noun (`en` / *fælleskøn*)
  - 🟠 **Amber badge**: Neuter Gender Noun (`et` / *intetkøn*)
  - 🟣 **Violet badge**: Verb (`vb.`) or Modal Verb (`modalvb.`)
  - 🟢 **Green badge**: Adjective (`adj.`)
  - 🟡 **Yellow badge**: Adverb (`adv.`)
  - 🔵 **Teal badge**: Expression / Sentence (`udtr.` / `sætning`)
  - 🟣 **Indigo badge**: Pronoun (`pron.`)
  - 🔵 **Cyan badge**: Plural Noun (`sb. pl.`)
- **Active Prompt**:
  - *Recognition Card*: Displays Danish word without gender article (`[ en / et ? ]` prompt for nouns) + IPA phonetics + native audio.
  - *Production Card*: Displays English definition + context sentence with cloze deletion blank (`[ ... ]`) where the word belongs.
- **Audio**: Auto-playing **synthetic Danish audio** generated via macOS voice `Sara` with touch-friendly replay pill button.

### 🃏 Back Side (Reveal)
- **Danish Term**: Complete Danish headword with correct article (`en bil`, `et hus`).
- **English Translation**: Clear, accurate primary and secondary meanings.
- **Bøjning / Grammatik (Inflections Box)**: Full inflection paradigm:
  - *Nouns*: Indefinite singular, definite singular, indefinite plural, definite plural (e.g. *en bil, bilen, biler, bilerne*).
  - *Verbs*: Present, past, and perfect (e.g. *spiser, spiste, har spist*).
  - *Adjectives*: Common form, neuter *t*-form, plural form (e.g. *god, godt, gode*).
- **Eksempelsætning (Example Sentence)**: Natural Danish example sentence with the target word highlighted in bold.
  - **Mobile-Friendly Translation Toggle**: Tap `Vis oversættelse (translation)` to reveal the English sentence translation.
- **📖 Ordnet.dk Button**: Direct link that opens the official entry on [Den Danske Ordbog (DDO)](https://ordnet.dk/ddo) in your browser.

---

## 🚀 Expanding Your Decks (Long-Term Progression)

### Article vocabulary builder

Paste a Danish article into the local **Læs & Lær** tool to identify repeated unfamiliar words, compare them with the existing deck, retain source sentences, edit definitions and save reviewed cards directly to the custom expansion dataset.

```bash
python3 vocab_builder/server.py
```

Then open [http://127.0.0.1:8787](http://127.0.0.1:8787). Use **Save to deck data**, then **Build .apkg**. The tool is dependency-free and processes article text locally in the browser. See [`vocab_builder/README.md`](vocab_builder/README.md) for the complete workflow.

### Learning progress dashboard

The optional desktop Anki add-on in [`anki_progress_dashboard/`](anki_progress_dashboard/) adds retention, daily completion, consistency, mature-card growth, backlog, lapses and review pace to the main deck screen. Build and install it with:

```bash
python3 build_progress_addon.py
```

Then choose **Tools → Add-ons → Install from file…** in Anki and select `dist/anki_progress_dashboard.ankiaddon`. It is read-only and does not change scheduling or review history.

As your Danish improves (transitioning from A1/A2 to B1/B2 and C1), you can easily add new words to your deck using the included Python CLI tool [`generate_deck.py`](file:///Users/unicorn/Documents/AI-Workspace/Anki/generate_deck.py).

### Method 1: Quick Add via CLI
To add a single word and immediately recompile the package with synthesized audio:
```bash
python3 generate_deck.py add "et arbejdsmarked" \
  --gender "et (intetkøn)" \
  --english "a job market / labor market" \
  --phonetics "[ˈɑːbɑjdsˌmɑːɡ̊əð]" \
  --inflections "et arbejdsmarked, arbejdsmarkedet, arbejdsmarkeder, arbejdsmarkederne" \
  --example "Det danske <b>arbejdsmarked</b> er kendt for flexicurity." \
  --example-en "The Danish job market is known for flexicurity." \
  --tag "!Level::A2 Type::Work"
```

### Method 2: Interactive Wizard
Run the guided interactive prompt:
```bash
python3 generate_deck.py interactive
```

### Method 3: Bulk Import from Custom CSV
Edit [`data/custom_expansion.csv`](file:///Users/unicorn/Documents/AI-Workspace/Anki/data/custom_expansion.csv) or create your own CSV file with the following headers:
```csv
Danish,Gender_Article,English,Phonetics,Inflections,Example_DA,Example_EN,Ordnet_Query,Subdeck,Tag
```
Then import and compile:
```bash
python3 generate_deck.py import-csv my_new_words.csv --subdeck "Danish A1-A2 (Dansk for Begyndere)::09 - Custom & Vocabulary Expansion"
```

### Rebuilding Decks Anytime
To re-synthesize missing audio tracks and re-create `danish_a1_a2_complete.apkg` (pure Python 3, zero external dependencies):
```bash
python3 generate_deck.py build
```

### Running Automated Quality Tests
To verify all audio files, phrase durations, HTML/cloze integrity, and SQLite package structure:
```bash
python3 test_audio.py
```

---

## 💡 Danish Grammar Cheat Sheet & Tips for Beginners

### 1. Noun Genders (*Fælleskøn* vs *Intetkøn*)
- **`en` (Fælleskøn / Common gender)**: Covers ~75% of all Danish nouns (*en bil*, *en kop*, *en mand*).
- **`et` (Intetkøn / Neuter gender)**: Covers ~25% of nouns (*et hus*, *et bord*, *et barn*).
- **Definite form (The...)**: Danish adds the article to the **end** of the word:
  - *en bil* (a car) ➔ *bil**en*** (the car)
  - *et hus* (a house) ➔ *hus**et*** (the house)

### 2. Verb Conjugation
- Danish verbs **do NOT conjugate by person** (I, you, he, she, we all use the same form!):
  - *Jeg taler* (I speak)
  - *Du taler* (You speak)
  - *Vi taler* (We speak)
- Present tense almost always ends in **`-r`**: *taler*, *spiser*, *bor*, *kommer*.

### 3. Word Order (The V2 Rule & *Ledsætninger*)
- **Main Clauses**: Follow the **V2 rule** (the finite verb is always in position 2):
  - *Jeg spiser et æble i dag.* (I eat an apple today.)
  - *I dag **spiser** jeg et æble.* (Today I eat an apple — subject & verb invert!)
- **Subordinate Clauses (*Ledsætninger*)**: Introduced by conjunctions like *fordi* (because), *hvis* (if), *at* (that). In subordinate clauses, central adverbs like **`ikke`** (not) or **`altid`** (always) go **before** the verb:
  - *Jeg kommer ikke, fordi jeg **ikke har** tid.* (I am not coming because I do not have time.)

### 4. Pronunciation & *Stød*
- **The Soft D**: Learn this sound by listening and imitating Danish examples such as *mad* and *rød*, with teacher feedback. Do not rely on an English “th” substitution.
- **Stød (`[ˀ]`)**: A subtle glottal stop / constriction in the vocal cords (e.g. *hund* vs *hun*).
- **Danish Vowels**:
  - **`Æ / æ`**: Similar to the 'a' in English *cat* or 'e' in *bed*.
  - **`Ø / ø`**: Similar to the 'i' in English *bird* or 'eu' in French *bleu*.
  - **`Å / å`**: Similar to the 'aw' in English *law* or 'o' in *more*.

---

## 🛠 Directory Structure

```
Anki/
├── danish_a1_a2_complete.apkg    # Ready-to-import complete Anki package
├── generate_deck.py              # Pure-Python CLI compiler & card manager
├── vocabulary_data.py            # Master curated A1-A2 vocabulary dataset
├── README.md                     # Documentation and learning guide
├── data/                         # CSV source datasets (one per module)
│   ├── 01_high_frequency_core.csv
│   ├── 02_essential_verbs.csv
│   ├── 03_everyday_nouns.csv
│   ├── 04_numbers_time_dates.csv
│   ├── 05_conversation_greetings.csv
│   ├── 06_food_drink_routine.csv
│   ├── 07_adjectives_opposites.csv
│   ├── 08_people_family_places.csv
│   └── custom_expansion.csv      # Template for your future vocabulary
└── media/                        # Generated .m4a audio tracks
```
