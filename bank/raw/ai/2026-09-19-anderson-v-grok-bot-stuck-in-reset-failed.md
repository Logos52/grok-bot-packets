---
id: 2026-09-19-anderson-v-grok-bot-stuck-in-reset-failed
kind: article
title: Grok Bot stuck in Reset failed / partial state loop — Retry Reset hangs at “Getting ready” 0%
source: "https://forum.cursor.com/t/grok-bot-stuck-in-reset-failed-partial-state-loop-retry-reset-hangs-at-getting-ready-0/172142"
author: Anderson_V_Leite / deanrie
published: 2026-09-18
captured: 2026-09-19
via: grok-bot/Field
lane: ai
status: raw
private: false
---

Title: Grok Bot stuck in Reset failed / partial state loop — Retry Reset hangs at “Getting ready” 0%
URL: https://forum.cursor.com/t/grok-bot-stuck-in-reset-failed-partial-state-loop-retry-reset-hangs-at-getting-ready-0/172142
Created: 2026-09-18T11:45:34.672Z

--- USER @Anderson_V_Leite (Anderson V. Leite) #1 2026-09-18T11:45:34.711Z ---
Where does the bug appear (feature/product)?

Grok Bot

Describe the Bug

Reset failed / partial state em loop. Retry Reset trava em Getting ready 0% e volta para Reset failed. Não vou mais clicar Reset. Conta SuperGrok, pago hoje. Pedir recovery manual do Agent Computer no backend. Horário: 18/09/2026 ~00:17 BRT - 18/09/2026 ~08:45 BRT.

Steps to Reproduce

Grok Bot cannot reach the Agent Computer. After “Can’t reach your computer”, Recover/Reset entered a loop:

Dialog:

Reset failed. The reset couldn’t finish. Grok Bot’s computer may be in a partial state — retry to run the reset again.

Buttons: Dismiss / Retry Reset

Clicking Retry Reset opens “Resetting Grok Bot’s Computer”:

Getting ready (spinner)

Wiping your data

Creating Grok Bot’s computer

Starting Grok Bot’s computer

Cleaning up

Reconnecting

Progress bar stays at 0% and never leaves “Getting ready”.

After a while it returns to the same Reset failed / partial state dialog.

Internet works. Kaspersky was disabled (including later attempts to stop HTTPS scanning). Same failure on home Wi‑Fi. Plan: SuperGrok, purchased on 2026-09-17. I will not click Reset again. Please recover the Agent Computer on the backend and keep Bots, files, and logins.

Steps to Reproduce

Open Grok Bot desktop, signed in to the SuperGrok / Cursor account that owns the Bots.

App shows “Connecting to Grok Bot’s computer”, then:

Can’t reach your computer. Your Bots are safe — they just can’t be loaded right now. If it doesn’t come back on its own, recover it — your files and logins are kept, but installed apps and packages are removed.

Click Retry — still unreachable.

Choose Recover computer / Reset Grok Bot’s Computer from the error state or Settings → Updates.

Reset starts: “Resetting Grok Bot’s Computer” → stuck on Getting ready at 0%.

Dialog appears: Reset failed / partial state.

Click Retry Reset.

Same wizard at 0% “Getting ready”, then the same Reset failed dialog again. Loop.

Expected Behavior

App should attach to the existing Agent Computer and load existing Bots. If the computer is unhealthy, Recover should finish. Reset should not loop at 0% / partial state.

Operating System

Windows [10 or 11 — complete]

Grok Bot version: [Settings → scroll to the bottom, e.g. 0.xx.x Stable]

Timezone: America/Maceio (BRT, UTC−3)

Plan

SuperGrok, paid 2026-09-17 (same account used in the app).

What I already tried

Retry from the unreachable-computer screen

Fully quit from the tray (not only closing the window) and reopen

Disabled Kaspersky / antivirus

Network works for normal browsing

Reset → Reset failed (partial state)

Retry Reset → hangs at Getting ready 0% → Reset failed again

I stopped clicking Reset/Recover/Update after the loop. Please do a manual backend recovery of the Agent Computer. Do not ask me to Reset again from the client.

Additional Information

First connection failure: night of 2026-09-17 ~23:30–00:20 BRT.

Reset failed loop still present on 2026-09-18 morning.

Screenshots attached: “Can’t reach your computer”, “Reset failed / partial state”, “Resetting Grok Bot’s Computer” at 0% Getting ready.

Operating System

Windows 10/11

Version Information

For Grok Bot

Does this stop you from using Cursor

No - Cursor works, but with this issue

--- STAFF @deanrie (Dean Rie) #4 2026-09-18T12:30:53.676Z ---
Hey, thanks for the detailed report. Here’s the key point right away: your Agent Computer is fine. There’s nothing we need to restore on our side. It was created when you signed in from your phone, your Bot is on it, and it’s healthy. None of the Reset attempts from the Windows app ever reached our servers, so nothing got wiped and nothing is stuck halfway. The wording “partial state” is misleading in this case, sorry about that. For now, don’t click Reset or Recover, they won’t help here.

What’s happening: the PC app logs in successfully, but every request after that fails on the PC before it ever reaches us. Almost always this is because something on the PC is inspecting HTTPS traffic using its own certificate. Browsers trust the Windows system certificate store, so the website works. Grok Bot currently trusts only public certificate authorities, so it fails. Kaspersky with “Encrypted connections scanning” enabled does exactly this, and an important detail is that pausing protection does not disable the interception.

Try these steps in order:

In Edge or Chrome, open https://api2.cursor.sh, click the lock icon, then “Connection is secure”, then the certificate icon, and check the “Issued by” field. It should be Amazon RSA 2048 M01. If it shows Kaspersky or something else, that’s the cause.
Open Kaspersky, go to Settings (gear icon), then Security settings, then Network settings, then Scan encrypted connections, and select “Do not scan encrypted connections”. Alternatively, under Threats and Exclusions, add Grok Bot to Trusted applications and tick “Do not scan encrypted traffic”.
Pause any VPN or proxy (Cloudflare WARP / 1.1.1.1, Clash, v2ray) and make sure Windows Settings > Network & Internet > Proxy is fully turned off.
Fully quit Grok Bot. Right click the tray icon and choose Quit, then open Task Manager and end any remaining Grok Bot processes. Reboot the PC, open Grok Bot, and wait a couple of minutes.
Repeat step 1. Once “Issued by” shows Amazon RSA 2048 M01, the app should connect.

Let me know what “Issued by” showed before and after, and what AV, VPN, or proxy you have installed on the PC. If it still won’t connect, attach the file %APPDATA%\Grok Bot\desktop-structured-log-spill.v1.json and I’ll dig deeper. Your phone app should keep working with the same Bot as usual in the meantime.

--- USER @Anderson_V_Leite (Anderson V. Leite) #6 2026-09-18T16:42:29.235Z ---
Thanks, that was exactly it.

The Agent Computer was fine — the Windows app never reached your servers because Kaspersky was intercepting HTTPS.

I went to Settings → Security settings → Network settings → Scan encrypted connections and selected Do not scan encrypted connections. Pausing protection was not enough.

After a full Quit from the tray and reopening Grok Bot, it connected. No Reset or Recover needed. Bot, files, and logins are intact.

Appreciate the clear steps and the note that “partial state” was misleading here.
