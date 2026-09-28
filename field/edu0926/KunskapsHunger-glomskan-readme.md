# Glömskan

*Det som ingen längre nämner, försvinner.*

A Swedish vocabulary card game where forgetting is the enemy. Every card is a word. You play a card by producing the
word from a Swedish clue, and a spaced-repetition scheduler (FSRS) decides which words are in your deck — so the game
loop and the learning schedule are the same thing. Built for Swedish schools (högstadiet and gymnasiet), entirely in
Swedish, with no accounts and no server: progress stays in the student's browser.

**▶ Play: https://kunskapshunger.github.io/glomskan/**

## What's playable now

A first slice, to find out whether the loop is fun:

- A run of four encounters and a boss. Each *Tystnad* is drawn from the letters of its own name, and every hit erases
  some of them.
- 50 hand-written B1–B2 words (*påverka, trovärdig, ifrågasätta, förmodligen …*).
- Word class is card type: verbs attack, nouns defend, adjectives strengthen the next card, adverbs draw cards.
- The task grows with your memory of the word: choose among four → type with a first-letter hint → type freely → type
  the right form in a sentence. Stronger memory, stronger card.
- Words you got right come back later; words you missed come back tomorrow.

Not in the slice yet: placement test, branching map, relics, grammar combos, the teacher page, save codes and sound.
See the design spec for the full game.

Keys: `1`–`5` pick a card · `E` ends the turn · `Enter` answers and continues · `Esc` closes the answer sheet.

## Run it locally

```bash
npm install
npm run dev     # → http://localhost:5174
npm test        # unit tests, including a check of every word card
npm run sim     # 60-day simulation of the learning engine
```

No build step: the browser loads native ES modules, and `ts-fsrs` is served from `vendor/` through an import map.

## Docs

- Design spec: [docs/superpowers/specs/2026-09-25-glomskan-design.md](docs/superpowers/specs/2026-09-25-glomskan-design.md)
- Learning-engine plan: [docs/superpowers/plans/2026-09-25-plan-1-learning-engine.md](docs/superpowers/plans/2026-09-25-plan-1-learning-engine.md)

## Credits

- Scheduling: [ts-fsrs](https://github.com/open-spaced-repetition/ts-fsrs) (MIT), vendored in `vendor/`.
- Word selection is guided by the Swedish [Kelly list](https://spraakbanken.gu.se/en/resources/kelly) (Språkbanken, CC BY 4.0).
- Fonts: IM Fell English and Spectral, via Google Fonts.
