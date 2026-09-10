---
id: 2026-09-10-kishorekv-bot-routines-refuse-to-fire-supergrok
kind: article
title: Bot routines refuse to fire (SuperGrok vs Cursor Start)
source: "https://forum.cursor.com/t/bot-routines-refuse-to-fire/171173"
author: KishoreKV
published: 2026-09-07
captured: 2026-09-10
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Bot routines refuse to fire

- url: https://forum.cursor.com/t/bot-routines-refuse-to-fire/171173
- topic_id: 171173
- created_at: 2026-09-07T11:47:03.102Z
- author: KishoreKV
- via: grok-bot/Field
- lane: ai
- deposited: 2026-09-10

## @KishoreKV · 2026-09-07T11:47:03.102Z

Hi @Colin , and rest of the Cursor support team.. I am facing the same issue but across Windows, MacOS and iOS apps.. where the bot’s routines refuse to fire despite multiple resets and replacements of the bot collection and hte grok computer. The same issue seems to persist in the current latest Version 0.44.0 on Windows. This makes me curious: are ALL users on these past few releases facing this issue, and if so, why is there so little noise on this issue on X? (Hope it isn’t the algo messing with the zeitgeist for the Grok Bot.) Or is this issue sticky to certain accounts only, based on the short straw they might have drawn when creating their account recently? If it’s tied to the account, I am going to just nuke this whole thing and just move on to other agents, as it’s pretty disillusioning facing these issues after excitedly paying for the subscription to start building bots/agents to solve some frustrating problems. Any prognosis on how sticky this bug is to an account or release? Hope to get some clarity on the bug.

## @Colin [staff] · 2026-09-09T14:56:43.798Z

Hey @KishoreKV , sorry this has been frustrating. I moved this out of the other thread because your issue is a bit distinct. Your Grok Bot access comes from the SuperGrok account you linked, while your Cursor subscription is on the Start plan. Routines (scheduled runs) are the one part of Grok Bot that checks the Cursor plan, and Start does not include them, so the server refuses to schedule them no matter how often you reset the bot or the computer. I have flagged this for the team. In the meantime, if you want routines, moving your Cursor plan to Pro or higher will make them start syncing with no other changes. Everything else in Grok Bot continues to work as it does today.

## @KishoreKV · 2026-09-09T16:50:24.248Z

Hi @Colin .. thanks for clarifying.. though it’s a bummer since I subscribed to X Premium+ instead of Cursor Pro because both listed Grok Bot as a feature, and X Premium+ seemed to offer a better combo with the X features. No mention that routines wouldn’t work in this route. Please make this explicit in the comparisons in the documentation. I’ll go change my subscription! Thanks.

## @Wes_Anderson · 2026-09-09T17:14:36.025Z

Colin: k Bot that checks the Cursor I was likewise confused on where to subscribe to get Grok Bot. I decided to go with a Cursor tier plan but that was lucky I guess. Grok and Grok Bot are great, but we need a unified theory of subscriptions.
