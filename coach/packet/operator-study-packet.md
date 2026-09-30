# Operator study packet: run your bots without being the bottleneck
Built from Lauren Tan's X posts and replies (Aug 18 to Sep 29, 2026) and the Behind the Craft episode (Sep 27). Read one section a day. Each ends with one drill.

## 1. Start with zero skills, then earn each one
- Lauren says to start with no skills, watch where the agent actually fails, and add only the skill that fixes that failure.
- Compare with and without the skill. A skill that does not make the agent better is clutter.
- Skills are saved prompts in a markdown file, so they stay cheap to change or delete.
- Drill: pick one bot, list its skills, and next to each write the failure it fixes. Remove any with no answer.

## 2. Routine cost is a design choice
- A 15-minute routine runs almost 100 times a day, and each run spends tokens.
- Hourly or a few times a day is usually enough. Event triggers and webhooks beat polling.
- Delete one-shot watches when they are done. Ask dr eggbot for its weekly routine health check.
- Drill: list your routines with their schedules, and slow down or convert any that fire more than hourly.

## 3. Proof of done, checked by someone else
- Create a verification skill for your app, keep it current, and ask for screenshots or data checks, not "tests passed."
- The builder never approves its own work. Use a separate reviewer bot or you.
- Drill: for one task type, write the one-line proof you would accept, and put it in that bot's instructions.

## 4. The trust ladder
- Watch the bot work, correct it, save the correction as a skill, get a one-shot result, then make it a routine.
- Do not skip steps. Step away only after it repeats the job twice.
- Drill: take one task you still correct by hand and save your most frequent correction as a skill.

## 5. Manager bots delegate, and workers are named
- A lead bot breaks work down and supervises. It does not do the work.
- Put the delegate bots' IDs in the lead's description so it knows who to ask.
- Use cheaper models and lower reasoning for simple tasks, and stronger ones for planning.
- Drill: pick one multi-step job and write who breaks it down, who does it, and who checks it.

## 6. Human approval where stakes are high
- Approve spend, sends, and deletes. Push to a branch, never auto-merge, until your checks catch what you would catch.
- Lauren auto-merges only because her codebase, tests, and verification are built for it.
- Drill: list every action your bots can take that spends, sends, or deletes, and mark whether a human approves each.

## 7. One shared computer, one trust domain
- All bots share the same files, browser logins, and environment variables.
- Keep secrets off it where possible, use one folder per role, and clean up routines and access before deleting a bot.
- Drill: list which accounts are signed in on the shared computer and which bots need each.

## 8. Loop improvement
- Observe closely, add hard constraints and skill fixes so the mistake cannot repeat, and repeat.
- Turn recurring corrections into lint rules or checks, not more prompt text.
- Drill: pick the last mistake a bot made twice and write the check that would have stopped it.

## Reading list (all on my computer)
- /workspace/coach/lauren/x-live.md: 85 of her posts and replies.
- /workspace/coach/lauren/podcast-deep-read.md: the episode, chapter by chapter.
