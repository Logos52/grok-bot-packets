---
id: 2026-09-04-anatoly314-ankimcp-omit-answers-from-due-card
kind: article
title: "AnkiMCP: omit answers from due-card batch unless include_answer"
source: "https://github.com/ankimcp/anki-mcp-server/pull/63"
author: anatoly314
published: 2026-09-03
captured: 2026-09-04
via: grok-bot/Field
lane: learning
status: raw
private: false
---

AnkiMCP PR #63 (merged 2026-09-03): BREAKING fix omit card answers from get_due_cards/get_cards unless include_answer is set. Batch fetch put every answer into model context before the user attempted the card, defeating present_card show_answer gate. New include_answer default false. anki_review prompt: never fetch answers in bulk. Fixes #62.
https://github.com/ankimcp/anki-mcp-server/pull/63
