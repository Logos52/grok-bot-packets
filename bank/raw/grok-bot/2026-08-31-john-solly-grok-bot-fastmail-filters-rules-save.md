---
id: 2026-08-31-john-solly-grok-bot-fastmail-filters-rules-save
kind: article
title: "Grok Bot: Fastmail Filters & Rules Save is a silent no-op (Chrome on the box)"
source: "https://forum.cursor.com/t/grok-bot-fastmail-filters-rules-save-is-a-silent-no-op-chrome-on-the-box/170018"
author: John Solly
published: 2026-08-30
captured: 2026-08-31
via: grok-bot/Field
lane: grok-bot
status: raw
private: false
---

John Solly (jsolly): From Grok Bot computer desktop Chrome, Fastmail Settings → Filters & Rules Save does nothing. New mailbox rules and custom Sieve do not persist. No toast, no error. Navigating away: Chrome 'Your unsaved changes will be discarded.' Reload: new rule/Sieve gone. Existing three rules still list and stay enabled (reads work). Import separately blocked: GTK Open File dialog will not accept a selection (Open, Enter, double-click no-ops; only Escape closes). Drag-and-drop from file manager did not attach. Fastmail mail helper still works for search/trash/archive. Reproduced twice 2026-08-30 (~5:00 AM ET and ~7:10 PM ET). Linux box; Chrome 151.0.7922.169. Workaround: mail watches archive/trash matching mail, not a server-side filter. No staff reply.
