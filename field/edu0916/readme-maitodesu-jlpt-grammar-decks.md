# JLPT Grammar Decks

Every grammar point of the JLPT N5 - N3 syllabus, as presentable slides. One
self-contained HTML page per chapter, 47 chapters, ~6,500 slides.

**[Browse the decks →](https://maitodesu.github.io/jlpt-grammar-decks/)**

Arrow keys move, `?` lists the presenter controls (laser pointer, pen, blackout,
overview grid). Practice answers are hidden until you step onto them.

## What a deck contains

Every grammar point walks the same short path, so a point runs about 19 slides
and a chapter is one sitting:

| Section | What it covers |
| --- | --- |
| Formation | what it attaches to, and how |
| Examples | the pattern in real sentences |
| Nuance & register | when it fits, and who says it |
| Contrast | how it differs from its lookalikes |
| Common mistakes | the errors worth pre-empting |
| Practice | questions, with answers you reveal |

| Level | Chapters | Grammar points | Slides |
| --- | --- | --- | --- |
| N5 | 18 | 84 | 1,572 |
| N4 | 13 | 120 | 2,197 |
| N3 | 16 | 161 | 2,822 |

## Source

The prose, example sentences, translations and practice questions all come from
[**jlpt-grammar-enhanced**](https://github.com/maitodesu/jlpt-grammar-enhanced),
an mdBook grammar reference. Nothing here is written for the slides: the build
reformats that book's Markdown into deckrun slides, splitting each page into
slide-sized blocks and turning its collapsible practice answers into
step-through reveals.

Pages are rendered by [deckrun](https://github.com/arpitbbhayani/deckrun), whose
HTML export inlines its own stylesheet and navigation runtime — so each page is
one file that works off any static host, with no build step and no server.

The generators live in the source repository:

```sh
python scripts/build_chapter_deck.py n5 1 1.25   # one chapter -> deckrun Markdown
python scripts/build_level_deck.py n5            # stitch a level, add its overview slide
python scripts/export_decks.py <out dir>         # every chapter -> standalone HTML + index
```

Fonts, and the KaTeX/Mermaid/highlight.js assets deckrun pins, load from public
CDNs, so an offline viewer sees fallback faces.

## Licence

Slide content is **CC BY-SA 4.0**, inherited from the source book. You may share
and adapt it, including commercially, provided you give credit, link to the
licence, indicate changes, and license derivatives the same way. Changes made
here: the book's pages were reformatted into slides, with no edits to the text.

The deckrun runtime and stylesheet embedded in each page are MIT, © 2026 Arpit
Bhayani. See [LICENSE](LICENSE) for both.

The grammar-point inventory — which patterns sit at which JLPT level — follows
the list at [jlptgrammarlist.neocities.org](https://jlptgrammarlist.neocities.org/),
which supplied the syllabus only and is unaffiliated with this project. The JLPT
is administered by the Japan Foundation and JEES, neither of which publishes an
official grammar list; treat the level labels as a study ordering, not a
syllabus guarantee.
