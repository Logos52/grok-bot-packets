# italian-words

Turn the words you highlight in Italian books on Apple Books into Anki cards.

Each card shows the word in the sentence where you found it. The back gives
the French translation and a short Italian dictionary entry. You also get a
reversed card: French meaning plus the sentence with a blank, and you recall
the Italian word.

Run it as often as you like while reading. Only new highlights become cards,
and a word you already have is never added twice.

## What you need

1. **A Mac with Apple Books.**
2. **Node.js 24 or newer.** Check with `node --version`. Install from
   [nodejs.org](https://nodejs.org) if needed.
3. **Anki** from [apps.ankiweb.net](https://apps.ankiweb.net), with the
   **AnkiConnect** add-on: in Anki, Tools → Add-ons → Get Add-ons, enter
   `2055492159`, then restart Anki. Anki must be open when you run the tool.
4. **An Anthropic API key.** Sign up at
   [console.anthropic.com](https://console.anthropic.com), add credit ($5 is
   plenty to start), and create a key. Then copy `.env.example` to `.env`
   in the project folder and paste your key there:

   ```
   ANTHROPIC_API_KEY=sk-ant-...
   ```

   `.env` is ignored by git, so the key stays on your machine. You can also
   `export ANTHROPIC_API_KEY=...` in your shell instead; a key set in the
   shell wins over the file. The API is billed separately from any Claude
   subscription.

## Install

```sh
git clone <this repo> italian-words
cd italian-words
npm install
npm run build
npm link
```

`npm link` makes the `italian-words` command available everywhere.

## Use

```sh
italian-words                      # pick a book from a list
italian-words "citta invisibili"   # or name it (accents optional)
italian-words --dry-run            # preview the cards, add nothing
italian-words --deck "Calvino"     # use another deck (default: Italiano)
italian-words --all                # also list books that don't look Italian
italian-words --model claude-opus-5     # use a stronger (pricier) model
```

The first run creates the deck and a card type called
"Italian Words (Apple Books)" in Anki.

The first time, macOS may ask whether your terminal can access data from
other apps. Allow it: that's how the tool reads Apple Books' highlights. It
only ever reads them, never changes them.

## Cost

With the default model (Claude Sonnet 5), expect roughly 12–25 US cents per
100 new highlights. Highlights already in Anki cost nothing. Each run ends with
the tokens used and their cost.

## Good to know

- Deleting a card in Anki doesn't stop it from coming back: the next run
  will add it again if the highlight is still in Apple Books.
- The same word highlighted twice (in one book or across books) only gets one
  card. Different forms of a word (*sbadigliava*, *sbadigliare*) count as
  different words.
- If some cards fail (network trouble, for example), just run it again. It
  picks up where it left off.

## Development

```sh
npm test           # unit tests (no network, no Anki needed)
npm run typecheck
npm start -- --help
```

## License

MIT
