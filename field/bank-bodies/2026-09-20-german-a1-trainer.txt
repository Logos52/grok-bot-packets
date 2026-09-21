# German A1 Trainer

German language learning application with interactive games and Anki deck generation.

## Quick Start

```bash
source .venv/bin/activate
python main.py
```

## Games

### 1. Verb Conjugation (`games/conjugation_game.py`)
Practice German verb conjugations through fill-in-the-blank sentences.
- 933 practice sentences covering 311 verbs
- Organized by Netzwerk textbook chapters
- SRS (spaced repetition) for efficient learning

### 2. Listening Comprehension (`games/listening_game.py`)
Practice listening to German numbers, letters, and symbols.
- Numbers 1-100
- Alphabet A-Z (including umlauts)
- Phone number dictation

### 3. Cases (`games/case_game.py`)
Practice German grammatical cases (Akkusativ/Dativ) in context.
- Fill-in exercises with case markers
- SRS-based practice

### 4. Number Writing (`games/writing_game.py`)
Practice writing German numbers.
- Hear a number, type it in German
- Supports numbers up to millions

## Anki Deck Generator

Generate Anki flashcard decks from CEFR vocabulary and Netzwerk textbook data.

```bash
python -m anki_generator.main
```

See [anki_generator/README.md](anki_generator/README.md) for details.

## Scripts

Data pipeline and enrichment scripts for vocabulary processing.

See [scripts/README.md](scripts/README.md) for details.

## Project Structure

```
german/
├── main.py                 # Main menu
├── pyproject.toml          # Project configuration
├── requirements.txt        # Dependencies
│
├── games/                  # Interactive games
│   ├── conjugation_game.py
│   ├── listening_game.py
│   ├── case_game.py
│   └── writing_game.py
│
├── lib/                    # Shared utilities
│   ├── srs.py              # Spaced repetition (FSRS)
│   ├── ui.py               # TUI framework
│   ├── german_numbers.py   # Number conversion
│   └── plural_expansion.py # Plural form expansion
│
├── anki_generator/         # Anki deck generation
│   ├── main.py             # CLI entry point
│   ├── cefr.py             # CEFR deck generator
│   ├── netzwerk.py         # Netzwerk deck generator
│   └── ...
│
├── scripts/                # Data pipeline
│   ├── pipeline/           # Core data processing
│   ├── enrichment/         # Data enrichment (DWDS, Wiktionary)
│   ├── utilities/          # Utility scripts
│   └── archived/           # One-time fix scripts
│
├── data/                   # Vocabulary data
│   ├── german_words.db     # Main SQLite database
│   ├── netzwerk/           # Netzwerk textbook data
│   ├── cefr_goethe/        # CEFR vocabulary lists
│   └── ...
│
├── config/                 # Application configuration
│   └── settings.json
│
├── user_data/              # User-specific data
│   ├── stats/              # Game statistics
│   └── srs/                # SRS state files
│
├── audio/                  # Audio files
│   └── cache/              # TTS cache
│
└── output/                 # Generated outputs
    └── anki/               # Generated Anki decks
```

## Controls

- Number keys: Select menu options
- `l`: Toggle language (DE/EN)
- `q` or `ESC`: Quit/Back
- During practice: Type answer, auto-submits when correct

## Installation

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Or install with optional dependencies
pip install -e ".[all]"
```

## Documentation

- [PLAN.md](PLAN.md) - Development plan and goals
- [ROADMAP.md](ROADMAP.md) - Feature roadmap
- [CLEANUP_PLAN.md](CLEANUP_PLAN.md) - Codebase cleanup plan
