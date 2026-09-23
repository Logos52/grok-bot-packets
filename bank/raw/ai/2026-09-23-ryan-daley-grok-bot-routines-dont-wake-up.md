---
id: 2026-09-23-ryan-daley-grok-bot-routines-dont-wake-up
kind: article
title: Grok Bot Routines don't wake up at the beginning of a new day — queue delay not asleep
source: "https://forum.cursor.com/t/grok-bot-routines-dont-wake-up-at-the-beginning-of-a-new-day/172545"
author: Ryan_Daley
published: 2026-09-21
captured: 2026-09-23
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot Routines don't wake up at the beginning of a new day
URL: https://forum.cursor.com/t/grok-bot-routines-dont-wake-up-at-the-beginning-of-a-new-day/172545
Created: 2026-09-21T18:58:01.409Z

## @Ryan_Daley — 2026-09-21T18:58:01.452Z
Describe the Bug Grok Bot and sub agents never start their first routines at the beginning of the day. So, I realized I need to start the day by saying “wake up the sub agents” to the main agent, and then the main agent and all sub agents complete their routines. I have 5 sub agents, so I thought maybe the issue was having the routines all starting at the same time. After staggering their routines by 10 minutes, the issue persists. How can I get Grok Bot to execute routines every day without needing any human interaction to wake it up? Steps to Reproduce Have a Grok Bot and Sub agents with a routine to read different sectors of the news every morning at 6:00am. Expected Behavior I expect the Grok Bot to autonomously send me a news summary every morning without me needing to turn on the app or interface with it in any way. Operating System Windows 10/11 Version Information Grok Bot 0.51.0 Does this stop you from using Cursor No - Cursor works, but with this issue

## @Ryan_Daley — 2026-09-21T20:43:51.517Z
I also don’t understand why my routines don’t finish on time. For example, this routine is just a handoff of notes to another agent. It can’t possibly be computationally heavy. So why is it still thinking about it nearly 30 minutes later? image 276×572 28.5 KB

## @mohitjain (staff) — 2026-09-22T06:55:24.597Z
Hey @Ryan_Daley , your routines aren’t asleep or skipped, they’re firing. The issue is a queue: scheduled runs across Grok Bot wait in line before they start. Your 1:15 PM handoff didn’t actually begin until about 1:37, so at 1:42 it had only just started, which is why it looks like it’s been “thinking” for 30 minutes. It’s the wait, not the task being heavy. A direct message (“wake up the sub agents”) skips that queue, which is why that always works. The wait is worst in the early-morning US window (roughly 5 to 9 AM Pacific), where runs land 20 to 45 minutes late, but it happens at other busy times too (your 1:15 PM run was about 20 minutes). This is on our side and an issue we’re tracking. Two things that help now: For time-sensitive morning jobs, schedule them earlier. Before about 4:30 AM Pacific the delay is usually under 10 to 15 minutes (routines also carry up to ~10 min of built-in randomization, so leave a little slack). Since your prompts tell scouts not to catch up when late, they stand down silently. Have them send a one-line “skipped, ran too late” note instead, so you get a signal rather than silence. Staggering by 10 minutes won’t help here. I’ll follow up when there’s an update.
