---
id: 2026-09-14-robhelgeson-日本語-known-word-stories-ankimorphs-gated
kind: article
title: 日本語 Known-Word Stories — AnkiMorphs-gated graded readers + tap-reveal furigana
source: "https://github.com/RobHelgeson/japanese-stories"
author: RobHelgeson
published: 2026-09-13
captured: 2026-09-14
via: grok-bot/Field
lane: learning
status: raw
private: false
---

# 日本語 Known-Word Stories (RobHelgeson/japanese-stories)

Source: https://github.com/RobHelgeson/japanese-stories
Author: RobHelgeson
Published/pushed window: created 2026-09-12; mechanism pushes through 2026-09-13 (~21:30Z) — gist progress sync, tap-reveal furigana, level-5 story, linked reader rebuild.
Live reader: https://robhelgeson.github.io/japanese-stories/

## Field summary (portable gates)
- **i+1 / known-word ceiling**: every story is written against a vocabulary list from a real Anki collection (AnkiMorphs lemmas past a 21-day interval). Small declared new-word budget; each new word must be framed in a sentence that teaches meaning before plain use.
- **reveal-schedule / taste-gate**: furigana on tap (not always-on); meaning is a second gesture (double-tap) so English is not one tap from pronunciation — anti-gloss-leak.
- **leech marking**: red sesame = known word that keeps failing; teal = approved new word for this story.
- **wiki-craft authoring**: AUTHORING.md + corpus.json briefs; Ichiran segmentation + AnkiConnect/AnkiMorphs; `check.py` validates every token is known or decomposes into known pieces.
- **quiet-when-nothing**: reader is offline HTML; only optional gist sync hits network.

## README (excerpt)
# 日本語 Known-Word Stories

Short Japanese stories written entirely inside a fixed known-word set, and a reader that shows furigana only when you ask for it.

**📖 Read them: <https://robhelgeson.github.io/japanese-stories/>**

The constraint is the whole idea. Every story is written against a vocabulary list derived from a real Anki collection, so a reader who has learned those words can read a whole story without a dictionary. Each story is allowed a small, declared budget of new words, and each of those has to be introduced in a sentence that frames its meaning before it is ever used plainly.

## The reader

A story is a small HTML shell beside a shared `reader.css`, `reader.js` and `sync.js`, with its own annotated text in `data/<slug>.js`. Classic `<link>` and `<script src>`, no modules — so a story still opens straight off the filesystem; it needs its siblings, so copy the folder rather than the one file. The only network request the reader ever makes is the optional progress sync below, and without it nothing is fetched at all.

Stories were self-contained single files until the site was published, which was the right shape for mailing one around and the wrong one to maintain: `reader.css` and `reader.js` were inlined into all eleven readers, so a one-line CSS change rewrote 2.5MB and had to re-segment every story through Ichiran to do it. `docs/versions/` is still built the old way — see [Publishing](#publishing).

Text is vertical by default, as Japanese literary prose is, and a page never scrolls: an authored page too big for the screen is split across screens that keep its page number.

|                            |                                                      |
| -------------------------- | ---------------------------------------------------- |
| Tap a kanji word           | its reading, in place, attached to the kanji         |
| Tap again                  | put the reading away                                 |
| Double tap a kanji word    | its meaning, in a sheet at the foot of the page      |
| Tap between words          | the reading for the whole sentence                   |
| Double tap between words   | that sentence in English                             |
| `f`                        | reveal every reading at once (also 設 → ふりがな)    |
| Swipe                      | turn the page (touch; on a mouse use the arrows)     |
| `←` `→`                    | turn pages, following the binding direction          |
| Tap the top or bottom edge | bring the bars back after they fade                  |
| `設`                       | writing mode, 改行, 綴じ, type size, theme, ふりがな |
| `目次`                     | back to the contents page                            |

Kana, particles and punctuation are not wrapped as words, so "between words" is about half of every line and easy to hit with a thumb. Which is also why the bars have their own gesture: every tap on the text now means something, so the strip the bars occupy is what is left to summon them with.

On a mouse, hovering a word reveals its reading and a double click opens the sheet. `Tab` reaches every kanji word and every translated sentence, and `Enter` opens the sheet directly — a sentence with no translation is not a tab stop, because there would be nothing to open.

The reading and the meaning stay one gesture apart on purpose: a story built from words you already know should not put the English in reach of the same tap that asks how a kanji is pronounced. That separation used to be three buttons in the bar — ふ, 訳, 意 — which meant the page did nothing at all until one of them was armed. Moving it into the gesture is what let them go.

Two kinds of word are marked, with 傍点 — the sesame dots Japanese prose uses to draw attention to a word. **Red sesame** is a leech: a known word on a card that keeps being failed, with its reading hidden. **Teal circles with the reading shown** is a new word, approved for this story but not yet learned.

Preferences and your place in each story are remembered per device.

## Keeping your place

Progress is written to `localStorage` as you read, and that is the working copy. Browsers throw it away, though: WebKit deletes all script-writable storage after seven days of browser use without a visit, and a Home Screen web app starts with a storage container of its own rather than the Safari tab's. Two things address that, and they are meant to be done in this order.

**Connect a gist.** 読書記録の同期 on the contents page takes a GitHub token — fine-grained, **Gists: write**, nothing else — and keeps a copy of your progress in a secret gist. Every device that pastes the same token finds the same gist by filename and shares it; you never carry a gist id around. Per slug the later timestamp wins, so two devices converge without a lock, and a push that would write what is already there is skipped, which keeps the gist's revision list usable as an undo history rather than a log of page turns.

The store is a plain JSON file on github.com, so correcting a bad record is something you can do by hand in the gist editor, with its revision history behind you. `?nosync` disables the whole thing for a load, the way `?nostore` does for `localStorage`.

**Then add it to the Home Screen.** That is what stops the seven-day eviction, because a standalone web app gets its own counter of days of use. Do it after connecting, not before: the install begins with an empty store, so it will read as zero progress until you paste the token into it and let it pull.

編集 on the contents page opens per-story controls — mark 読了 or 未読, move the resume page, clear one story — alongside 書き出し / 読み込み for the whole record as JSON. Import merges by the same rule the gist does, so pasting an older export cannot pull a story backwards. Clearing writes a dated empty record rather than deleting the key, because a deletion merges back to whatever the gist still holds and would undo itself on the next pull.

## Layout

```
scripts/          the engine — build, validate, segment, inflect
stories/          story sources (.txt) and stories-index.md (summaries + afterwords)
docs/             what GitHub Pages serves
  reader.css      one copy, shared by every live story
  reader.js       one copy
  sync.js         one copy — progress sync, shared with the contents page
  manifest.webmanifest, icon-*.png     the Home Screen install
  data/<slug>.js  one story's annotated text
  <slug>.html     a ~5KB shell linking the three
  versions/       archived drafts, self-contained and frozen
AUTHORING.md      the craft spec a new story is written against
```

A story source is plain text: a `# title` line, then alternating Japanese sentences and `>` English translations, with a blank line between pages. Furigana is authored inline as `｜漢字《かんじ》`. Everything else — level, brief, new-word budget, reading order — lives in `scripts/corpus.json`.

## Building

```bash
cd scripts
export ICHIRAN_URL=http://localhost:3005
python3 rebuild.py
