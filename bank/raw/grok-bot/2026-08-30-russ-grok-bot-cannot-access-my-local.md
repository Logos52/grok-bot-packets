---
id: 2026-08-30-russ-grok-bot-cannot-access-my-local
kind: article
title: Grok Bot cannot access my local computer
source: "https://forum.cursor.com/t/grok-bot-cannot-access-my-local-computer/169924"
author: Russ
published: 2026-08-29
captured: 2026-08-30
via: grok-bot/Field
lane: grok-bot
status: raw
private: false
---

Russ: Grok Bot cannot access my local computer (0.30, Windows). Chat stays up while the local-computer hook never registers. Known bug shape (not Tailscale, not missing Administrator). Staff note: helper starts, then drops its connection to their servers; there is no attach button.

Staff (Dean Rie): matches tracked issue — helper that connects Grok Bot to local computer starts but does not finish registration, so chat keeps working but local computer access stays unavailable. Workaround: fully quit via tray Quit (not just close window); Task Manager end remaining Grok Bot processes; relaunch and wait a couple minutes. If still missing, sign out/in to recreate helper. Check for 0.31.0. Not subscription-related.

Portable: chat-up ≠ local attached. Kill claim that Always-allow / Tailscale / Admin will fix a helper that never finishes registration.
