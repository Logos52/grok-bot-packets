---
id: 2026-09-09-ellisfan-grok-bot-conversation-history-rolled-back
kind: article
title: "Grok Bot: Conversation history and newly created bots/groups suddenly rolled back and synchronized across all devices"
source: "https://forum.cursor.com/t/grok-bot-conversation-history-and-newly-created-bots-groups-suddenly-rolled-back-and-synchronized-across-all-devices/171008"
author: ellisfan
published: 2026-09-08
captured: 2026-09-09
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot: Conversation history and newly created bots/groups suddenly rolled back and synchronized across all devices
URL: https://forum.cursor.com/t/grok-bot-conversation-history-and-newly-created-bots-groups-suddenly-rolled-back-and-synchronized-across-all-devices/171008
Created: 2026-09-08T08:19:45.312Z

## ellisfan — 2026-09-08T08:19:45.386Z
Where does the bug appear (feature/product)? Grok Bot Describe the Bug Today, all conversation history after a specific point in the day, along with newly created groups and bots, suddenly disappeared. The loss was immediately synchronized across macOS, Windows, and iOS. After the incident, all three platforms showed the exact same truncated state — earlier history remained, but everything after that cutoff point (including today’s new bots and groups) was gone. This does not appear to be a local cache or single-client issue. The account history state itself was rolled back and then synced everywhere. I have not performed any Reset of the Agent Computer. Support has so far only responded with automated replies stating they cannot restore the missing data and recommending to recreate the bots. Steps to Reproduce Use Grok Bot normally across multiple devices. Create new bots / groups and continue conversations. After a backend event, the account history is truncated at a specific timestamp. All devices (macOS, Windows, iOS) then rehydrate to the same truncated state. Expected Behavior Conversation history, newly created groups, and bots should persist and remain consistent across all devices. A silent server-side rollback that truncates account history and synchronizes the loss to every client should not occur. Users should be able to recover lost data when such an incident happens. Operating System MacOS Version Information Grok Bot (latest stable versions across macOS, Windows, and iOS) For AI issues: which model did you use? Not applicable – this is a data persistence / account history issue, not a model response issue. Additional Information This is a multi-device data loss incident. After a backend event, all conversation history after a specific cutoff point today, plus newly created groups and bots, were wiped. The truncated state was then synchronized across macOS, Windows, and iOS simultaneously. I did not perform any Reset of the Agent Computer. Support responses so far have been automated and stated that no restore is possible. Key questions: Does any earlier snapshot of the account history still exist? Why was the durable history rolled back and then propagated as a permanent loss across all devices? Is there any recovery path for the missing conversations and bots? This is a serious data integrity problem. A tool that can silently erase conversation history and user-created bots across every device is not reliable for ongoing work. Does this stop you from using Cursor Yes - Cursor is unusable

## Adam7 — 2026-09-08T08:28:38.643Z
I have this also, very frustrating this morning to find this also, I had created some new routines and a complex agent, to find this morning it had all been removed, including the conversation

## ellisfan — 2026-09-08T08:31:48.895Z
Thanks for confirming. Same here — multi-device sync (macOS / Windows / iOS) all showed the truncated history after a certain cutoff point today. New bots, groups, and conversations after that point are gone. Support only gave automated “cannot restore” replies so far.

## Adam7 — 2026-09-08T08:35:27.025Z
Yes Luckily I run codex Computer history so my grok agent could reconstruct from that

## jay_desu — 2026-09-08T09:04:10.399Z
Same exact bug and issue - no way to recover? Quite frustrating as I’d just finished putting together a new complicated bot and routines. How did this happen and what are the chances of this happening again?

## ellisfan — 2026-09-08T09:06:58.817Z
Same here. I also lost all conversations after a specific cutoff point today, plus newly created bots and groups. It synchronized across macOS, Windows, and iOS at the same time. Support has only given automated replies saying they cannot restore the data. No clear explanation yet of why the durable history was rolled back, or whether any earlier snapshot still exists. I’m also concerned about how often this can happen. If the account history can be silently truncated and pushed to every device, it’s hard to trust the product for any serious ongoing work. Hope the team can give a real technical answer soon.

## jay_desu — 2026-09-08T09:08:20.885Z
(post deleted by author)

## jay_desu — 2026-09-08T09:08:55.949Z
Completely agree - hard to tell exactly, but I think I’ve lost several days of work and conversation, and custom bot configuration and information across 10+ bots.

## ellisfan — 2026-09-08T09:10:41.513Z
Yeah, same feeling. It’s not just a few chats — it’s days of context, custom bot setups, and accumulated work that disappeared without warning. The worst part is that it synchronized the loss across every device. If the durable history can be rolled back like this, it’s really hard to trust putting important ongoing work into Grok Bot.

## Adam7 — 2026-09-08T09:41:38.560Z
Following up, because this still needs a proper answer from Cursor support or engineering — not another automated “cannot restore” reply. What happened on my account Overnight / this morning (8 Sep), Grok Bot conversation history after a cutoff point disappeared, along with newly created bots/groups and related setup (including new routines and a more complex agent configuration). The truncated state then showed consistently across devices — this was not a single-client cache problem, and I did not run Reset of the Agent Computer. That matches what others here are describing: Ellis Fan’s original report of multi-device sync of a rolled-back history, and jay_desu’s report of losing substantial bot configuration and days of work across many bots. So this looks like an account-history / sync integrity failure on Cursor’s side, not user error. What I was able to do I was lucky in one respect: I run Codex Computer History (local activity summaries on my Mac). My Grok Bot agent was able to reconstruct a lot of the missing operational context from that. That is a personal safety net I already had in place. Most users will not have an equivalent second memory layer, and for them this incident is silent, multi-device data loss with no recovery path. Even with that reconstruction, the experience was disruptive, and it raises a basic trust problem: if durable history, bots, groups and routines can be truncated and then synchronised everywhere as the new truth, Grok Bot is hard to rely on for ongoing work. What I need from support / the team Please can a human from Cursor support or engineering reply on this thread with a technical answer, not an auto-response? Specifically: What caused the durable account history to roll back and then propagate to every client? Does any earlier snapshot of the account state still exist on your side? Is there any recovery path for lost conversations, bots, groups and routines — even partial? What has been done (or will be done) so this cannot happen again without a clear user-visible failure mode and a restore option? Until there is a clear explanation and a durability story, it is difficult to treat Grok Bot as a safe place to keep serious day-to-day agent work. Happy to provide account details privately to support if that helps investigation.

## ellisfan — 2026-09-08T10:21:07.918Z
I just uninstalled Grok Bot, and Cursor is next.

## Andy3379 — 2026-09-08T10:59:13.606Z
Did anyone find the solution already?

## Adam7 — 2026-09-08T11:00:18.215Z
Nope, still waiting for official support

## Andy3379 — 2026-09-08T11:00:53.570Z
Its too painful for i paid whole morning to build skills to bots, kill me plzzz.

## rwhalen — 2026-09-08T13:02:40.868Z
I had the same issue today. This is actually the second time I’ve experienced the issue, but the first time I had minimal activity during the data loss period, so I just re-created my work. This time, I’d had more significant activity, which will be a real pain to recreate. Not to mention, wasted usage credits.

## notdimax — 2026-09-07T22:31:48.088Z
Where does the bug appear (feature/product)? Grok Bot Describe the Bug Hi team, I’m reporting a serious issue with Grok Bot. What happened: My girlfriend was setting up Grok Bot for about 1 hour (creating and configuring bots). She used roughly 15% of the weekly usage. At some point she Alt+Tabbed away from the app. When she came back, all the bots had completely disappeared. The app now shows either an empty state (“No saved Bots yet”) or behaves as if it’s a brand new account. What we already tried (nothing worked): Fully closed and reopened the app multiple times Signed out and signed back in Tried Recover computer / Recover Agent Computer Tried Update Agent Computer Restarted the computer Tested on another device / mobile companion app Waited and retried several times The bots simply do not come back. There is no “Your Bots are safe” message that allows recovery either — they just vanished. Account email: victoriapersonal.111@gmail.com Additional context: The issue happened right after Alt+Tab during the initial setup phase. Weekly usage was only around 15% at the time. We did not intentionally delete any bots or run a full Reset Agent Computer. Could you please check on the backend whether the Agent Computer and the bots still exist for this account and restore access? Happy to provide any extra details (app version, OS, screenshots, etc.) if needed. Thank you! Steps to Reproduce Fix it. Operating System MacOS Version Information Grok bot on mac os Does this stop you from using Cursor No - Cursor works, but with this issue

## Brian_Miller2 — 2026-09-08T04:23:53.683Z
This happened to me today as well. I was working in Grok Bot all day. Spent many hours building up my bot team and giving it context, planning. The team of bots helped me ship several features today. We were running strong then suddenly when I checked back, they were all gone. No history of the bots on my account. Very strange and extremely frustrating since I spent all day building up the team and giving them context. Help restore our bots! DM me for account info if the support team can restore please!

## Toby_L — 2026-09-08T12:34:11.927Z
I think, I had the same issue this morning. I reported it with ticket T-F60936.

## notdimax — 2026-09-08T12:45:38.690Z
Fixed, by now the bots just appeard again thanks.

## Jiyae_Choi — 2026-09-08T02:21:11.058Z
Where does the bug appear (feature/product)? Grok Bot Describe the Bug After my macbook turned back on after sleep mode, one of the bots is totally missing.. The other bot exists. Unable to find it from the GrokBot app. Steps to Reproduce The missing bot had a working session in youtube page through screen. I paused it. And kept the macbook in sleep mode for a while. When I turned it on, there is no trace of that agent. Expected Behavior All the bots should have continuing session. Operating System MacOS Tahoe 26.3.1 Version Information Grok Bot : 0.44.0 Track: Stable Does this stop you from using Cursor No - Cursor works, but with this issue

## Roberth_Lopez — 2026-09-08T13:39:49.455Z
Where does the bug appear (feature/product)? Grok Bot Describe the Bug My bots are disappearing or losing the history, theres any way to recover them? Steps to Reproduce Im not sure it has happen to me 2 times, today after I opened the macbook, it was on sleep mode. Expected Behavior Macbook Air M3 Sequoia Version 15.3.2 (24D81) Operating System MacOS Version Information Version: 0.44.0 Release Track: stable OS: darwin Does this stop you from using Cursor No - Cursor works, but with this issue

## pvandesande — 2026-09-08T13:28:10.839Z
Where does the bug appear (feature/product)? Grok Bot Describe the Bug I created multiple bots during the day, when I came back 3 hrs later my MacBook was in sleeping mode. When I went Into Grok Bot the bots I created today were gone. Bots I created the day before were visible but todays updates were also gone? Steps to Reproduce I asked yesterdays bot where the bots are but he can’t find anything? Expected Behavior Missing Bots Operating System MacOS Version Information Grok Bot version 0.44.0 Mac OS Tahoe 26.6.2 Does this stop you from using Cursor Sometimes - I can sometimes use Cursor

## Brian_Miller2 — 2026-09-08T14:50:22.701Z
Update on my account: My bots are back as of this morning. My account seems to have been resolved.

## Prometheus_Labs — 2026-09-08T14:57:14.472Z
Windows – all conversation history after 8pm EST Sept 7, 2026 truncated after Update (multiple bots) Hi team, I’m on Windows (Grok Bot 0.44.0 Stable) and am experiencing the same overnight history rollback reported in this thread. What happened: I have lost all conversation history with multiple bots after 8pm EST on September 7, 2026 . Earlier history remains, but everything after that cutoff point is completely gone. I did not create any new bots — I am only missing conversation history across multiple existing bots. What I’ve already tried: Fully quit + reopen the app Ran Update Grok Bot’s Computer from Settings → Updates The update completed successfully Files and logins were preserved as expected Conversation history is still exactly the same truncated state (everything after 8pm EST Sept 7 is missing) I have not run Reset Grok Bot’s Computer. This matches the multi-device account-level history rollback others are describing. Support replies so far have indicated the missing data cannot be restored, but I’m posting here so my case is on the record with the precise cutoff time. Please let me know if any earlier snapshot of the conversation history still exists, or if there is any recovery path for the messages after 8pm EST on Sept 7. Thanks.

## Bill_Kimberlin — 2026-09-08T17:31:14.719Z
This is messed up! Losing 10 hours of work sends me back to codex and claude. I want this to be stable, but lost 10 hours of logic building. Has this happened before? I’m paying $300 a month and just got SCREWED.

## Colin — 2026-09-08T19:12:10.659Z
Hi everyone, We recently identified an issue where some Grok Bot users were mistakenly provisioned a duplicate computer. For a period of time, some user sessions were routed to the duplicate computer rather than the original. We’ve fixed the underlying issue. For each affected user, we removed the duplicate and pointed them back to the computer that held the most history. If this happened to you, you may be missing some conversations or state from that period. We sincerely aplogize for the disruption. If you notice missing conversations or state, please send an email hi@cursor.com and we’ll work to make it right.

## Adam7 — 2026-09-08T20:25:10.950Z
Thanks for the explanation — that matches what we saw (history/bots/groups jumping back across devices). We were affected: recent chat and a group room rolled back, and some short-lived state from that window is gone. We’ve rebuilt what we needed and aren’t missing enough to need recovery, so no action required on our account. Appreciate the clear post.

## Chase_Adams — 2026-09-08T21:02:00.437Z
I had this same issue overnight last night. Had Grok Bot handle a pricing cutover at midnight for a Labor Day Sale I was running and it flawlessly executed it all. Then this morning, all history of that conversation is gone and it is still asking me if I want to do the pricing cutover, telling me it hasn’t run yet, and I’m having to tell it that it did indeed run, it just has no memory of it now for whatever reason. Extremely concerning to just have massive gaps in your chat and execution history go missing with no explanation.
