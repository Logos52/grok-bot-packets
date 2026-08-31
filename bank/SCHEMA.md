# SCHEMA — the frontmatter block on every bank file

Every file under `raw/<lane>/` and `cards/<lane>/` starts with this block. `scripts/bank.py` writes it. Nobody writes it by hand.

```yaml
---
id: 2026-08-15-basic-logic-a-question-for-the-maga-movement
kind: transcript
title: A Question For The MAGA Movement
source: "https://www.youtube.com/watch?v=hL6DwOjm_ko"
author: Basic Logic
published: 2025-12-05
captured: 2026-08-15
via: web-clipper
lane: politics
status: raw
private: false
description: (optional, first 300 characters of the capturing app's description)
---
```

| key | values | who sets it |
|---|---|---|
| `id` | capture date + author + first six title words. Also the filename. Never changes. | bank.py |
| `kind` | `transcript` (YouTube) · `thread` (X) · `podcast` · `article` · `post` (forum) · `packet` (bot) · `paper` · `bank` (agent research folder) | bank.py from the URL; `--kind` overrides |
| `title` | as captured | the source |
| `source` | the URL. Dedupe key. | the source |
| `author` | channel, handle, or byline | the source |
| `published` | date the source went up | the source |
| `captured` | date it entered a capture tool or the bank | bank.py |
| `via` | `web-clipper` · `bank-cli` · `grok-bot/<bot>` · `opus-bank` · `grok-bank` · `dcard-safari` · `fold` | bank.py `--via` |
| `lane` | `ai` · `learning` · `politics` · `money` · `ideas` · `culture` · `yuedu` · `cast` · `gaming` · `grok-bot` · `misc` | bank.py guesses from author and title; `--lane` overrides |
| `status` | `raw` → `carded` → `compiled` → `dead`. One direction. | bank.py, the index, or a hand edit of this one line |
| `private` | `true` or `false`. A file under `raw/private/` is private whatever this says. | bank.py `--private`, or the folder |

A card adds two lines: `card_version: 1` and `raw: raw/<lane>/<id>.md`.

## Two marks for private

1. The folder. Anything under `raw/private/` or `cards/private/` is private because of where it sits. Paid courses, book PDFs, the Refold and ICS material.
2. The flag. `private: true` marks one item inside a normal lane. Dcard posts in `raw/yuedu/`, a pasted email.

Nothing with either mark leaves this Mac.

## Lanes

A lane is a folder under `raw/` and the same word in the block. Adding a lane is making the folder and adding the word to `LANES` in `scripts/bank.py`.

| lane | what goes in |
|---|---|
| `ai` | models, agents, tools, Claude, Grok, Cursor, Hermes |
| `learning` | how to learn, memory, focus, language method, Notion, study systems |
| `politics` | Basic Logic, Triggernometry, Implicitly Pretentious, culture war, immigration |
| `money` | markets, macro, freight, SpaceX and Tesla as businesses |
| `ideas` | Naval, Chamath, All-In, Gurwinder, general thinking |
| `culture` | film, anime, minimalism, Kiki |
| `yuedu` | Chinese reading material: Dcard posts, RSS articles. Mostly private. |
| `cast` | material for the tsumugu cast bots |
| `gaming` | WoW, EQL, Guild Wars |
| `grok-bot` | packets and docs from the bot fleet |
| `misc` | not yet sorted. Should be empty. |

## Index

`index.jsonl` is one JSON object per item with the block's keys plus `raw`, `card`, `body_sha`, `used_by`. `INDEX.md` is made from it. Both are rebuilt by `python3 scripts/bank.py --index`. Neither is edited by hand.
