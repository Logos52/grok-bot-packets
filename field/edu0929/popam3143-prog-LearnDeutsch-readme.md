# Wortgarten — plain HTML, CSS & JavaScript

Extract the ZIP and double-click index.html. Keep these three files together:

- index.html — the page
- styles.css — responsive layouts and all six themes
- app.js — all 256 vocabulary cards, SVG pictures, and practice logic

No install, server, account, internet connection, or build step is needed. You can also upload these three files to the root of a GitHub Pages repository.

## What is included

- Black by default; Midnight, Forest, Plum, Paper and Sand themes.
- 1.1 only (134 cards), 1.2 only (122 cards), or all 256 cards together.
- All eight lessons: 1.1a–1.1d and 1.2a–1.2d, including every row in the supplied photos.
- German → English, English → German, or mixed practice.
- 10-card, 20-card, or full-collection rounds.
- Picture clues, noun-article checking, hints, missed-card review, and a searchable word book.
- Large phone controls, 16–17px answer inputs, layouts for phones/tablets/desktops, six colour palettes, reduced-motion support.
- First correct answers count immediately. A correct answer with a hint also counts as correct, while “without hints” is tracked separately. Revealed answers count as incorrect.
- Enter checks an answer. Enter again continues exactly one card. On a phone you can use Check answer and Next card.
- Clear written feedback, a check/cross symbol, coloured borders and score animation.
- Theme preferences and learning progress stay in the current browser. Clearing browser data clears progress.

Learning progress is separate from the round score: two unassisted correct answers in a row in a direction mark that word learned. Gendered nouns accept either listed gender form. Any listed translation is accepted; case and punctuation are ignored, and ae/oe/ue/ss can replace ä/ö/ü/ß.

Original lessons may contain repeated words; lesson cards are kept separate to match the source. The 95 previous cards were preserved. The additions are 39 cards in 1.1d and 122 cards in 1.2. All picture clues are bundled SVGs.

## Verification

Local DOM/event tests covered 702 accepted answer variants, scoring, check/continue state transitions, focus, hints, reveals, review rounds, chapter and lesson filters, search, all six themes, and saved preferences. CSS syntax and text contrast were checked. Browser policy prevented opening local files in the available test browser, so actual phone-browser rendering and native keyboard behaviour could not be verified here.
