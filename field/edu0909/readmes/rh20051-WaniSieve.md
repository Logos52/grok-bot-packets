# WaniSieve

Generates an Anki Deck based on a given .txt file of Japanese text, parsed with Fugashi. Filters vocabulary to only above what has been learned from user's WaniKani account before creating the deck.

## How it works

1. Takes a text file of Japanese text (`.txt` file) as input.
2. Tokenizes it with [Fugashi](https://github.com/polm/fugashi) (a MeCab wrapper).
3. Calls the [WaniKani API](https://docs.api.wanikani.com/) to pull your current level and learned vocabulary.
4. Filters out anything at or below user level, keeping only new/unlearned words.
5. Pushes the remaining words as new notes into a specified Anki deck via [AnkiConnect](https://foosoft.net/projects/anki-connect/).

## Requirements

- Python 3.10+
- [Anki](https://apps.ankiweb.net/) installed and running, with the [AnkiConnect](https://foosoft.net/projects/anki-connect/) add-on installed (code `2055492159`)
- A WaniKani account and [API token](https://www.wanikani.com/settings/personal_access_tokens)
- [Fugashi](https://github.com/polm/fugashi)

## Usage

Anki must be open (with AnkiConnect installed) before running the script.

```bash
python wanisieve.py --api-key YOUR_WANIKANI_API_KEY --input chapter1.txt --deck "Chapter 1 Vocab"
```

### Arguments

| Argument | Short | Required | Description |
|---|---|---|---|
| `--api-key` | `-k` | Yes | Your WaniKani personal access token, used to fetch your current level and learned vocabulary. |
| `--input` | `-i` | Yes | Path to a `.txt` file containing the Japanese chapter/section text to process. |
| `--deck` | `-d` | Yes | Name of the Anki deck to create (or add to) with the generated cards. If it doesn't exist yet, it will be created automatically. |

### Example

```bash
python wanisieve.py -k abcd1234-5678-... -i vn_scripts/chapter3.txt -d "VN - Chapter 3"
```

This reads `chapter3.txt`, filters its vocabulary against your WaniKani account, and adds new cards for any unfamiliar words to the "VN - Chapter 3" deck in Anki.

## Notes

- Words already at or below your WaniKani level are skipped, so decks only contain genuinely new vocabulary.
- Duplicate cards are not added if a word already exists in the target deck.

## License

MIT
