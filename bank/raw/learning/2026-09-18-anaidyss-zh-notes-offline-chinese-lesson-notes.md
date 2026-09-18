---
id: 2026-09-18-anaidyss-zh-notes-offline-chinese-lesson-notes
kind: article
title: "zh-notes: offline Chinese lesson-notes CLI → Obsidian ruby → Anki (single source of truth)"
source: "https://github.com/anaidyss/zh-notes"
author: anaidyss
published: 2026-09-17
captured: 2026-09-18
via: grok-bot/Field
lane: learning
status: raw
private: false
---

# zh-notes — anaidyss/zh-notes
Source: https://github.com/anaidyss/zh-notes
Created: 2026-09-17T13:58:06Z · pushed through 2026-09-17T17:08:37Z · MIT
Lane: education / wiki-craft / human-gate / quiet-when-nothing / teach-once

Named runner: zh-notes — CLI for Chinese lesson notes. Type pinyin or paste hanzi → offline CC-CEDICT (+ optional Russian BKRS) lookup → one markdown ruby line appended to the active lesson note. Obsidian renders ruby; same line feeds Anki deck builder. Note file is sole source of truth (no separate word DB).

Portable gates:
- quiet-when-nothing: `zh -q` refuses when it cannot uniquely choose
- human-gate: `zh -i` fuzzel/fzf picker for multi-reading words; Mod+Shift+Z asks for your own meaning
- teach-once / wiki-craft: lesson markdown is the vault; HSK 2.0/3.0 tags; `zh find` / `zh ruby` / `zh undo`
- `zh anki --open` builds deck from notes

125071 dict entries; 101223 with Russian gloss (gloss language is data — lookups work for any meaning language). Install: ./install.sh [--with-bkrs] [--with-timer]. Needs python3; full path wants fcitx5+pinyin, Obsidian, Anki.

Day-0 NEW URL 2026-09-17. Prefer ZH.
