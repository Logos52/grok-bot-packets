---
id: 2026-09-27-benahordure-colin-grok-bot-ios-login-only-offers
kind: article
title: Grok Bot iOS login only offers accounts.x.ai — Cursor Apple SSO account not found
source: "https://forum.cursor.com/t/grok-bot-ios-login-only-offers-accounts-x-ai-cursor-apple-sso-account-not-found/173116"
author: Benahordure; Colin
published: 2026-09-27
captured: 2026-09-27
via: grok-bot/Field
lane: ai
status: raw
private: false
---

--- @Benahordure post 1 2026-09-27T10:16:37.460Z ---
Where does the bug appear (feature/product)?
Grok Bot
Describe the Bug
On desktop, Grok Bot is signed in with my Cursor account via Sign in with Apple. On iOS, there is no “Sign in with Cursor” option. The flow goes to accounts.x.ai and Apple offers to create a new account with a new email.  The only way to login is to find the email used by Apple then use the “Send link to email to log in”
Steps to Reproduce

Open Grok Bot on iPhone
Start sign-in.
Apple Sign in proposes creating a new account (not linking the existing Cursor session).
Stop before creating — creating would clearly be a separate identity.

Expected Behavior
“Sign in with Cursor” (or reuse the existing Cursor Apple SSO session), same Bots as desktop.
Screenshots / Screen Recordings
Capture d’écran 2026-09-27 à 12.10.00.png1206×2622 205 KB
Operating System
iOS
Version Information
iOS 27.0 / Grok bot 1.12
Does this stop you from using Cursor
No - Cursor works, but with this issue

--- @Colin post 7 2026-09-27T18:37:11.598Z ---
Hey @Benahordure, thanks for the report!
We’re working on it! Right now, sending the magic link is the correct workaround.
