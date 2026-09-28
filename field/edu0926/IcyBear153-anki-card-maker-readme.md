# Anki Card Maker

Turn your **Google Translate "Saved Translations"** export into ready-to-import
Anki flashcards — complete with pronunciation audio — fully offline
Python, no AI/LLM needed.

## Why this exists

Google Translate lets you star ("save") words and phrases as you look them up,
and now lets you export that saved list as a spreadsheet. This project takes
that raw export and turns it straight into an Anki deck: cleaned-up
vocabulary, a phonetic reading for each entry, and a matching audio clip,
with zero manual spreadsheet editing.

The code is currently refined for my own personal use as I attempt to further my Japanese vocab
to be able to talk to inlaws. However, it could easily be altered for any first/second language
(I have marked all of the places in the code where slight alterations will be necessary).

An earlier version of this project I made a few years ago relied on ChatGPT to generate the
vocabulary lists which needed to be coppied and pasted by hand, which was slow and inconsistent.
All of this was before google let you export your google translate user data instantly.
This version doeseverything with plain Python — `pandas` for spreadsheet handling, `pykakasi`
for Japanese readings, and `gTTS` for audio — so it runs unattended.

## Features

- Reads the raw `.xlsx` export from Google Translate's Saved Translations
- Strips out the language-name columns and aligns text so the target
  language and your native language are always in consistent columns,
  regardless of which order Google exported them in
- Generates a hiragana (japanese language pronunciation) reading for every Japanese entry
- Generates an MP3 pronunciation clip for every entry via Google TTS
- Skips regenerating audio that already exists, so re-running the script
  after adding new saved words is fast
- Sanitizes filenames so odd punctuation in the source text can't break
  audio generation
- Outputs a comma-separated CSV in the exact format Anki's importer expects,
  with `[sound:...]` tags already wired up

## Requirements

- Python 3.9+
- Everything in requirements.txt:
    pandas, numpy, gTTS, pykakasi, and openpyxl  (the last one is what pandas uses under the hood to read .xlsx files)

Install everything with:

```bash
pip install -r requirements.txt
```

## Usage

1. In Google Translate, export your **Saved Translations** list as a
   spreadsheet and save it in this folder as `Saved translations.xlsx` ().

2. Run the script:

   ```bash
   python cardMaker.py
   ```

3. Two things are created:
   - `newCards.csv` — your flashcard data, one row per saved translation
   - `audio_files/` — one `.mp3` per entry, named to match the CSV's sound
     tags

## Getting the cards into Anki

1. Copy every file from `audio_files/` into Anki's media folder:
   - Windows: `%APPDATA%\Anki2\<Your Profile>\collection.media`
   - Mac: `~/Library/Application Support/Anki2/<Your Profile>/collection.media`
   - Linux: `~/.local/share/Anki2/<Your Profile>/collection.media`
2. In Anki, go to **File → Import** and select `newCards.csv`.
3. Set **Field separator** to **Comma**.
4. Map the four columns to your note type's fields, in order:
   `Expression → Meaning → Reading → Audio`.
5. Choose the destination deck and note type, then **Import**.

## Input format

The script expects the raw, unedited Google Translate export: four columns,
with the first two holding language names (e.g. `English`, `Japanese`) and
the last two holding the corresponding text. The script figures out which
row has which language and re-aligns everything automatically, so you don't
need to sort or reformat the export by hand.

## Limitations / roadmap

- Currently tuned for Japanese readings (hiragana via `pykakasi`); using this
  for another language means swapping the reading-generation step for
  something appropriate to that language
- Audio generation depends on Google Translate's TTS service being
  reachable — no offline fallback yet
- Not tuned to deal with more than one second language so currently
  less practicle for users with more than one scond language
- No de-duplication against cards already in your Anki deck; re-running the
  script on the same export will just regenerate the same cards

## License

MIT — do whatever you like with it.