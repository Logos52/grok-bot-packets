# Lauren Tan (@poteto): latest public talk / appearance
Researched 2026-09-27 (Sun), times in ET. Baseline: `/workspace/logos52.github.io/wiki/Systems/Agentic Workflows/Poteto Paved Path.md` (created 2026-09-22).

## Bottom line
- **Latest solo talk = the paved-path talk you already have.** It was recorded for Cursor Compile London and posted on X on **Mon Sep 21, 2026, about 11:01 AM ET**, with the text "here's how i shipped 2,500 PRs last month to production". Link: https://x.com/poteto/status/2102050467505430555 (X returns 403; the text is mirrored at https://unrollnow.com/status/2102050467505430555). I found no newer solo talk.
- **Newest public appearance (newer than the talk) = a podcast interview, not a talk.** It is Behind the Craft (Peter Yang), "We Built Grok Bot. Here Are Our 14 Best Bots | Peng Zheng & Lauren Tan", published **Sun Sep 27, 2026** (today), about 45 min.
  - YouTube: https://www.youtube.com/watch?v=xZ5TEaleUdg
  - Show notes: https://creatoreconomy.so/p/grok-bot-team-14-best-bots-peng-zheng-lauren-tan
  - Podcast listing: https://getpodcast.com/uk/podcast/behind-the-craft2/we-built-grok-bot-here-are-our-14-best-bots-peng-zheng-and-lauren-tan_8859475d40
- **Next scheduled talk: Compile Amsterdam, "I Shipped 2,000 PRs Last Month", Jan 27, 2:30 PM** (https://cursor.com/compile/amsterdam). The page gives no year. https://cursor.com/compile lists it after NYC Nov 5, so it is almost certainly 2027. She is not on the Sydney (Oct 14) or New York (Nov 5) agendas.

## Evidence it's the latest
- Her timeline mirror (https://twiscan.com/en/x/poteto, fetched today, posts up to Sep 26) shows these after Sep 21:
  - Sep 23: Galaxy game-studio recap post.
  - Sep 25: she reposted Matt Pocock's review of the Sep 21 talk.
  - Sep 25: Starship-invite promo.
  - Sep 26: Peter Yang's teaser for the podcast.
  - Otherwise only jokes and reposts. No new talk, meetup or broadcast.
- The Compile London page (https://cursor.com/compile/london, Sep 16) lists "I Shipped 2,000 PRs Last Month – Lauren Tan, 2:30 PM". She did not appear in person: her Sep 21 post says she "couldn't make it since i was livestreaming for Grok Bot Galaxy". Emre Cavunt's London notes agree: the programme listed her, but his notes record Tomas Reimers in that slot (https://emrecavunt.com/blog/cursor-compile-london-series).
- Other items that turned out to be older:
  - Facebook "Great Grok Bot training by … Lauren Tan" (56:30): posted Aug 30 (https://www.facebook.com/brian.hanson1/videos/…/28252076597722367/).
  - MTS interview with Roshan Sadanani, recorded around Grok Bot launch / Grok 4.6 day: https://www.youtube.com/watch?v=A63sedG-p5Q and clip https://www.youtube.com/watch?v=p8Ceadxc1Q4.
  - The Maven workshop / YouTube Cmoh-yR-usA that the baseline already cites.
- Confidence: **high** that the Sep 21 recording is her latest solo talk and that the Sep 27 podcast is her latest public appearance. The caveat is that X itself is blocked, so I relied on mirrors.

## Content of the newest appearance: Behind the Craft, Sep 27
Source: YouTube auto-captions, obtained through WebFetch of the watch page. The captions garble names: "Grockbot" = Grok Bot, "PAC/PSA/P stack" = pstack, "Omachi" = Omarchy, "Tuki/Suki" = her assistant bot. Quotes below are caption text, lightly de-garbled only where noted.

Chapters (from show notes):
- 00:00 bots the team uses
- 01:23 Peng's chief of staff
- 06:31 PM/design/eng bots in one room
- 10:07 photo-to-diorama
- 14:16 how Lauren's bots test their own work before merging
- 17:59 Dr. Eggbot
- 21:27 assistant booked multi-city trip
- 25:22 eng bots that land PRs before she reads them
- 38:59 how to trust bots with more work, one skill at a time

### Lauren's segments
1. **Verifying on real environments.**
   - She is adding Grok Bot support for Omarchy (DHH's Linux distro). She runs a special build of it in a VM on her Mac.
   - Her bot uses Grok Bot's local-execution daemon to script and control the VM and install Grok Bot inside it.
   - The point is the agent verifying its own work on her machine, in addition to its own cloud computer.
   - Caption: "that's like one thing I always talk about is like you know the importance of actually uh having the agent be able to verify its own work."
2. **A bot named "crumb"** finds and deletes disk-space hogs on her machine.
3. **pstack is maintained through evals.**
   - She kicks off Cursor cloud agents from Grok Bot to work on pstack.
   - pstack has an eval playbook: spawn subagents on different models, try the prompt, and check that the intended goal was achieved. "only if it does achieve it, it will actually uh you know land that that pull request."
4. **Dr. Eggbot, a bot that designs bots** (https://x.ai/bot/marketplace/bots/dr-eggbot-v2).
   - It builds bots "with all of the engineering rigor that I expect".
   - It gives them food-themed names.
   - It runs a routine that reads all your bots and their transcripts and proposes new skills, a new bot, or routine changes.
   - It audits routines for cost: "if you do like I don't know every 10 minutes that's like a lot of wakeups."
   - Her reason for splitting bots: one agent used for too many things piles up diverse context "which can be like maybe confusing."
5. **Assistant bot booked a complex trip.**
   - Route: Orange County → Denver → London → Amsterdam → home, through Navan, with hotels near the venue.
   - Her only input was a link to a Slack message and "check in with me before you hit book".
   - She says she is going "to give a talk soon uh in London and Amsterdam as part of the compile on the road conference", which suggests the episode was recorded before Sep 16.
   - She calls it her biggest purchase through the bot. She still approves before booking so she doesn't end up on "some crazy redeye".
   - The assistant also reorders Amazon items. It has its own phone number (third-party service) so it can text her lunch reminders, and it orders DoorDash.
6. **Eng org of bots.**
   - Chain: she talks to her chief of staff → eng lead "Matcha" → engineer bots. The count is uncertain: she says "I have three" at about 25:26, and later the caption says "delegate to those four bots" at about 26:12. The show notes give no count. (Corrected 2026-09-27 from the timestamped captions.)
   - Dr. Eggbot wrote the lead's job description as "never do work on your own and always delegate".
   - The engineer bots don't code themselves either. They spawn Cursor cloud agents, which lets her choose model and reasoning level per task.
   - Caption: "lets me orchestrate like really massive agent swarms."
   - For big projects the chief of staff first plans phases in a Notion doc, then delegates.
7. **Auto-merge.**
   - The Grok Bot codebase was made "very agent friendly", so "a lot of times it actually just lets me automerge my PRs … sometimes I actually don't even look at the PR until after it's landed and then I'm like, 'Oh, okay. Yeah, that looks good.'"
8. **Michelin kitchen vs "software factory".**
   - "I like to call it the Michelin kitchen" because it implies quality and craft at scale (50–100 seats).
   - The word "factory" carries a connotation of mass-produced slop, per caption and Peter Yang's quote.
   - "how do we get quality at scale."
9. **Mode skills compound.**
   - Internally many people have their own mode skill: "lauren mode" (= poteto-mode in pstack) and Peng's "peng mode".
   - Redesigning the Grok Bot codebase was motivated by letting "everyone … contribute at a high level not just engineers."
   - Cursor and Grok Bot plugins interoperate, so pstack installs in both. Plugins can bundle skills and MCP; the X plugin includes a skill.
10. **Social bot as outer loop.**
    - A bot named "Potato" checks her X mentions about every 30 min. Her meme: say "potato" three times and she gets notified.
    - It aggregates reports, e.g. "five users have reported the same bug."
    - She treats socials as her outer loop feeding the inner loop: "go talk to potato and figure it out … come back to me with a design proposal." No copy-pasting context between bots.
11. **Trust ladder (her advice at 38:59).**
    - Caption: "it ultimately comes back to trust … spend the time to sort of observe the bot or agent doing the work and then you course correct it … at the end of the conversation, you turn that into a skill."
    - Example: an /expense-report skill. Once it one-shots, "set up a routine" (e.g. file expenses whenever a receipt email arrives).
    - Trust "has to be kind of gradual."
    - She agrees with Peter's framing of hiring and onboarding virtual employees.
    - Peter Yang's thread condenses this into a punchier line, "First, watch your bot work and correct it. Turn what worked into a skill. Once it nails the task in one shot, make it a routine." That wording is his summary, not verbatim caption text.

### Peng Zheng (Grok Bot design lead, SpaceXAI), same episode
- Chief-of-staff bot as the default router. It buys 3D-printing filament and updates a Notion inventory.
- Marketplace-listing chain: price research, local competitors, drafting in his style by consulting his writer bot, then auto-dropping $5/week.
- Email, calendar and podcast bots.
- A PM/design/eng group chat to debate ideas.
- A photo → clay-diorama → personal-website check-in pipeline driven by a playbook in a private repo.
- Designer bot with Figma MCP plus a skill describing his file setup and design system: "I will do the first 5% … one key frame and then ask it to scale it into the whole flow."
- Product philosophy: persistent, named agents with their own identity, memory and tools. Capabilities are shared; memory and preferences are per bot. Chats are ephemeral, roles persist.
- The goal is to match users' mental model ("my mom would never know what is a [skill/agents] MD"), like calling an agent at your insurer.
- Advice: overstretch it to find the limit; start simple → recurring task → routines → tune token burn; "building a relationship between you and the bot."

### Numbers in the episode
- Titled "14 bots" (show notes).
- Engineer-bot count is uncertain: "I have three" (25:26) vs "those four bots" (26:12). The show notes give no number.
- $5/week price drop (Peng).
- X-mention check about every 30 min (Lauren).
- No PR counts were cited in this episode.

## Content of the latest solo talk (Sep 21)
The baseline page already summarizes it slide by slide. Additional verifiable facts:
- 38 minutes long (https://folkfox.com/pstack-2500-ai-agent-prs-verification/).
- The headline figure is 2,500 PRs last month. The Compile schedule title says 2,000; per folkfox these are her own numbers for different months, and neither is audited.
- Follow-up post in the same thread: "very bullish on Bend … when you have a codebase that can formally verify itself, you can ship at an incredible pace. code review is solved" (unrollnow mirror above).
- The baseline wiki page says 5000+ PRs from its slide; the tweet says 2,500 in the last month. These may be cumulative vs monthly. Do not conflate them.
- Secondary summary by @AYi_AInotes (https://bittide.aicompass.dev/article/a8efacf7-f756-461e-beed-922d6e49b0e0), not first-party. It mentions CDP-driven UI proof and CPU traces, useEffect banned via CI, comments banned with a cleanup tool, pstack's 23 playbooks and 23 principles, and an outer loop from user feedback. Verify against the video before relying on these details.

## What's new vs the baseline page
1. **Bot org chart.** Chief of staff → eng lead Matcha → engineer bots → Cursor cloud agents, where each layer is told not to do work itself. The baseline has Grok Bot as "line cook" and cloud agents as a station, but not this delegation hierarchy or per-task model and reasoning choice.
2. **Dr. Eggbot as a meta-gardener for bots.** It audits bots, transcripts and routines, and proposes skills, new bots or cost cuts. This is the gardener idea applied to agents instead of code.
3. **Eval-gated skill changes.** pstack PRs land only if a multi-model eval shows the goal was achieved. The baseline mentions skills but not evals as the gate.
4. **Auto-merge stated plainly:** "don't even look at the PR until after it's landed". The baseline stops at "a helper does not merge", which conflicts in spirit. Her auto-merge applies to her agent-friendly codebase, and the wiki's rule is the reader's own practice.
5. **Explicit trust ladder for non-code work:** watch → correct → skill → one-shot → routine. The baseline has the "whenever you correct your agent" hierarchy for code. This is the same idea for any workflow.
6. **Socials as outer loop:** the X-mention bot aggregates bug reports and hands context bot-to-bot.
7. **She defends the "Michelin kitchen" name against "software factory"** because "factory" connotes slop.
8. **Verification on the user's own machine** through the local-exec daemon (Omarchy VM), not only in the cloud.
9. Nothing in the episode revises the codebase > lint/CI > rules > skills > style guide hierarchy, Dune, or the feature map. None of these are discussed in detail.

## What named SpaceXAI / Grok Bot / Cursor people said
- **Peng Zheng** (Grok Bot design lead, SpaceXAI) is her co-guest on the Sep 27 episode (above). He jokes that pstack should be complemented by his own "peng mode". He doesn't comment on her talk.
- **Peter Yang** (host; not a SpaceXAI/Cursor employee as far as I found).
  - Sep 26 teaser (twiscan mirror): "Who better to learn Grok Bot from than the people who built it?"
  - Sep 27 thread: https://www.unrollnow.com/status/2104213287353356531
- **Matt Pocock** (independent TS educator; NOT a Cursor/xAI employee, as far as I found). He posted on Sep 25 about the Sep 21 talk, and Lauren reposted it: https://www.unrollnow.com/status/2103431302527508886. His key points:
  - (1) Lock down agents: agents do better in "extremely locked-down environments"; lint enforces the abstractions; Dune.
  - (2) Verification infra: custom CLIs to drive and measure the app; make the app "factory ready" from day one.
  - (3) Feature maps: kept in sync via automations. He usually warns against such docs but concedes navigation docs are worth it "if they enable new behavior".
  - "Banger talk - watch the whole thing on 2x."
- **Ash Osborne (@aiAshos)** described a COBOL migration factory "inspired by @poteto pStack". Kiara (SpaceXAI field engineer, @kiaraplds) shared it on Sep 17 with "This is incredible". This is about pstack, not the talk, and predates it.
- **No SpaceXAI, Grok Bot or Cursor engineer commentary on the Sep 21 talk or the Sep 27 episode was found.** I checked twiscan mirrors of mattyp, pengzheng_, roshan_s, ericzakariasson, jediahkatz, leerob, MarkVillacampa, bot, cursor_ai, kiaraplds, threepointone, mntruell, amanrsanger and benln. The only Lauren mentions were Galaxy-livestream posts.

## Gaps / blocked
- x.com is 403 to WebFetch; xcancel is suspended; nitter returned nothing. X replies and quote-tweets could not be read directly, so employee reactions may exist in replies I couldn't see.
- YouTube captions: yt-dlp and youtube-transcript-api were blocked (bot check / IP block). The transcript came from WebFetch of the watch page: auto-captions with no timestamps, so quote positions are approximate.
- The full Behind the Craft Substack post is paywalled beyond the first two takeaways.
- The Sep 21 video itself (on X) could not be re-watched; content relies on the baseline page's slides plus secondary write-ups.
- HN Algolia search returned non-JSON (failed), so HN was not checked.
