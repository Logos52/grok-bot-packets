---
id: 2026-08-30-matt-segar-building-anki-cards-with-claude-code
kind: article
title: Building Anki Cards with Claude Code
source: "https://segar.me/blog/posts/anki_cards_claude_code.html"
author: Matt Segar
published: 2026-08-23
captured: 2026-08-30
via: grok-bot/Field
lane: learning
status: raw
private: false
---

Matt Segar builds an EP board Anki deck with Claude Code: 468 notes / 1,386 cards. First 52 imported "clean"; Anki HTML ate "<250 msec" cutoffs (invisible until review). Fix: escape < > in packaging. fact_key (topic::parameter) clusters mentions, surfaces numeric conflicts, blocks duplicate notes. Grades deck against 50 held-out real questions (own review said good; questions said 56% and named holes). Cloze giveaway scanner + "could a smart outsider answer from the sentence alone" pass. Prose cards fail ~15× more than number cards ("therefore" giveaways). Agent loop vs chat paste is the mechanism. QC script as hard gate (issues=0) before .apkg.
