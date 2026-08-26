# Grok Bot guides and use-case posts

Compiled Saturday 2026-08-15 (Asia/Saigon). Public first-party fetches only. No invented titles, dates, or quotes. Items are kept only if they are actually how-to or use-case. Times from UTC sources are also shown in ICT (UTC+7).

## Official docs and first-party pages

### Grok Bot (overview)
- **Who:** xAI / SpaceXAI docs
- **Date:** not stated on the page
- **URL:** https://docs.x.ai/grok-bot/overview
- **What it teaches:** What a Bot is, that all Bots share one user-scoped cloud computer, and a sample first handoff (Salesforce prospect list → research → LinkedIn/email drafts for approval).
- **Opened:** yes

### Get started
- **Who:** xAI / SpaceXAI docs
- **Date:** not stated on the page
- **URL:** https://docs.x.ai/grok-bot/get-started
- **What it teaches:** Install the macOS/Windows app, sign in with Cursor, create a first Bot, write a five-part request (outcome, sources, constraints, deliverable, review point), then take over the computer for logins.
- **Opened:** yes

### Use cases
- **Who:** xAI / SpaceXAI docs
- **Date:** not stated on the page
- **URL:** https://docs.x.ai/grok-bot/use-cases
- **What it teaches:** Eight starter roles (Sales Outbound, Talent Scout, Paid Media, Expense Manager, Product Performance, Bug Reproduction, Account Health, Chief of Staff) with copy-paste first tasks that stop at review, plus a 7-step path from one task to a skill then a routine.
- **Opened:** yes

### Use the computer and apps
- **Who:** xAI / SpaceXAI docs
- **Date:** not stated on the page
- **URL:** https://docs.x.ai/grok-bot/computer-and-apps
- **What it teaches:** How the shared computer works (sessions, files, `/workspace`), how to watch or take over Agent Computer for 2FA/CAPTCHA/payments, how to add Plugins, and how to update/recover/reset the computer.
- **Opened:** yes

### Skills and routines
- **Who:** xAI / SpaceXAI docs
- **Date:** not stated on the page
- **URL:** https://docs.x.ai/grok-bot/skills-routines-and-automations
- **What it teaches:** Save a successful task as a skill, optionally Teach a task by demonstration (up to 10 minutes), then schedule or event-trigger a routine (Slack/GitHub), with Test run and a 50-routine / 20-run-history cap.
- **Opened:** yes

### Create and manage Bots
- **Who:** xAI / SpaceXAI docs
- **Date:** not stated on the page
- **URL:** https://docs.x.ai/grok-bot/bots
- **What it teaches:** How to create, edit, pin, hide, duplicate, and delete Bots; put job/boundaries in the description; keep the roster small; account limit of 50 Bots and group chats combined.
- **Opened:** yes

### Message and collaborate
- **Who:** xAI / SpaceXAI docs
- **Date:** not stated on the page
- **URL:** https://docs.x.ai/grok-bot/chat-and-collaboration
- **What it teaches:** How to message a Bot (`/` skills, `@` mentions), start a 2–6 Bot group chat, hand work between Bots, redirect or “Stop now,” and write a kickoff that assigns Researcher / Writer / Reviewer without publishing.
- **Opened:** yes

### Files and results
- **Who:** xAI / SpaceXAI docs
- **Date:** not stated on the page
- **URL:** https://docs.x.ai/grok-bot/files-and-results
- **What it teaches:** What you can attach (up to six files; 25 MB docs/images/audio, 200 MB video), how to ask for a reviewable artifact with facts vs assumptions vs pending approvals, and how Bots share files in `/workspace`.
- **Opened:** yes

### Grok Bot for iOS
- **Who:** xAI / SpaceXAI docs
- **Date:** not stated on the page
- **URL:** https://docs.x.ai/grok-bot/mobile
- **What it teaches:** iPhone (iOS 18+) setup, messaging, computer takeover, and routine pause/resume; schedule edits, run history, Test run, and Teach a task still need desktop.
- **Opened:** yes

### Approvals, security, and privacy
- **Who:** xAI / SpaceXAI docs
- **Date:** not stated on the page
- **URL:** https://docs.x.ai/grok-bot/approvals-security-and-privacy
- **What it teaches:** How to fence sending/publishing/purchases/deletes/production changes, use Allow once / Deny / Always allow and Auto-review rules, enter secrets yourself (not in chat), and that separate Bots are not a security boundary.
- **Opened:** yes

### Troubleshooting
- **Who:** xAI / SpaceXAI docs
- **Date:** not stated on the page
- **URL:** https://docs.x.ai/grok-bot/troubleshooting
- **What it teaches:** Least-destructive fixes for sign-in, computer setup/unreachable, stuck Bots, login loops, plugin auth, attachments, missed routines, blocked approvals, and local-computer refusals.
- **Opened:** yes

### Grok Bot for teams and enterprises
- **Who:** xAI / SpaceXAI docs
- **Date:** not stated on the page
- **URL:** https://docs.x.ai/grok-bot/teams-and-enterprises
- **What it teaches:** Admin rollout: one computer per member (not per Bot), dashboard setup wizard, MCP/plugin policy, identity/sign-in limits, no model picker, Legacy Privacy Mode blocks the product, and that an audit view of Bot actions is coming.
- **Opened:** yes

### Introducing Grok Bot
- **Who:** SpaceXAI (x.ai/news)
- **Date:** Aug 11, 2026 (page date)
- **URL:** https://x.ai/news/introducing-grok-bot
- **What it teaches:** Launch framing plus internal SpaceXAI use cases: sales outbound overnight, demo-readiness, pipeline ops, account follow-up, CRM notes from call transcripts, ops seating new hires / Gmail invoices, and engineering bug-repro then handoff to a debugging Bot.
- **Opened:** yes

### Grok Bot: A new kind of colleague (product page)
- **Who:** SpaceXAI (x.ai)
- **Date:** not stated on the page
- **URL:** https://x.ai/bot
- **What it teaches:** Product pitch for messaging Bots, Teach a task, group handoffs, the same eight job names as the docs, and published prices (Cursor Ultra $200/mo, SuperGrok Heavy $300/mo, Cursor Premium Teams $120/seat/mo).
- **Opened:** yes

## Named-user practice

### Intro to Grok Bot
- **Who:** matt palmer (@mattyp), devex @spacexai
- **Date:** Tue Aug 11, 2026 18:59:47 UTC (Wed Aug 12, 2026 1:59 AM ICT)
- **URL:** https://x.com/mattyp/status/2087252657589412119 (opened via https://api.fxtwitter.com/mattyp/status/2087252657589412119)
- **What it teaches / what they ran:** Long X article on how Grok Bot actually works (shared Linux VM, login handoff, secure secret form, record-a-workflow routines, user/agent/project memory, Slack/git/schedule triggers, Cursor plugins, Settings > General > Agent allow/block reviewer) plus the jobs he ran: Demo Bot (X bookmarks → approved prompt → Cursor Cloud agent in a tech-demos repo), Content Bot (hourly Slack ships → Typefully drafts), Product Bot (daily announcement digest), grocery Bot (Instacart vs Amazon carts each Friday), DoorDash Bot (Slack `drd.sh` mentions → menu + join link).
- **Opened:** yes

### Reply comparing Grok Bot to ChatGPT Work
- **Who:** matt palmer (@mattyp)
- **Date:** Tue Aug 11, 2026 23:06:44 UTC (Wed Aug 12, 2026 6:06 AM ICT)
- **URL:** https://x.com/mattyp/status/2087314806596641159 (opened via https://api.fxtwitter.com/mattyp/status/2087314806596641159)
- **What it teaches / what they ran:** Step list of the X-bookmark → approve → Cursor Cloud MVP → recorded demo loop; the weekly Instacart/Amazon cart compare; plus an overnight Wii baseball emulator grind that learned controls and won.
- **Opened:** yes

### Grok Bot is in beta! here are 100 use cases ive seen so far
- **Who:** eric zakariasson (@ericzakariasson), tinkering @spacexai
- **Date:** Tue Aug 11, 2026 19:24:39 UTC (Wed Aug 12, 2026 2:24 AM ICT)
- **URL:** https://x.com/ericzakariasson/status/2087258914060664902 (opened via https://api.fxtwitter.com/ericzakariasson/status/2087258914060664902)
- **What it teaches / what they ran:** A numbered catalog of use cases he says he has seen (GTM crew, chief-of-staff hub, community ops, recruiting screen, Salesforce from phone, Gong win/loss, LinkedIn digest, QBR pack, Apple Search Ads pacing, competitor price watch, Outreach GUI enroll, security questionnaire, “what did we promise this customer,” and more). The opened fxtwitter payload stops at item 40 of the claimed 100; items 41–100 were not in the fetch.
- **Opened:** yes (partial; list truncated at 40)

### Grok Bot Review: Is the $200 AI Agent Team Worth It?
- **Who:** Nate (natesnewsletter.substack.com)
- **Date:** Aug 14, 2026
- **URL:** https://natesnewsletter.substack.com/p/grok-bot-review
- **What it teaches / what they ran:** Public preview: in about eight hours he built twelve working Bots (Chief of Staff, landing-page lead, customer-language research, plus Gmail/Slack/Calendar/LinkedIn, travel, exercise, contact research, and a backyard-sauna search) on one shared computer; paid remainder (Super Doer Bot / Business in a Box Bot details) was not visible.
- **Opened:** yes (public preview only; rest is paid)

### I hate agents. (subtitle on page: I hated AI agents. Until this:)
- **Who:** Ruben Hassid (How to AI / ruben.substack.com)
- **Date:** Aug 12, 2026
- **URL:** https://ruben.substack.com/p/what-the-f-is-an-agent
- **What it teaches / what they ran:** Public how-to for a first Grok Bot: go to x.ai/bot, create a Bot with “Daily digest of AI news in my industry,” then refine to top-3 AI / creator-economy / consulting items plus a ruben.substack.com how-to check, optionally emailed via Gmail; paid “advanced agent” prompt was not visible.
- **Opened:** yes (public portion only; rest is paid)

### Emily Gavrilenko’s Post
- **Who:** Emily Gavrilenko (Building SpaceXAI)
- **Date:** LinkedIn showed “3d” when fetched on 2026-08-15 (about 2026-08-12); no calendar date on the public page
- **URL:** https://www.linkedin.com/posts/emily-gavrilenko_grokbot-activity-7493001034894626817-m4JC
- **What it teaches / what they ran:** Named work Bots (skippy EA/router, cloudie enterprise cloud-agent PM, grokie first-party model PM, webie cursor.com experiments, inboundie email SDR, pmm comms) plus personal tasks she says she delegated: dentist appointment, 70mm IMAX Odyssey tickets, Point Reyes campsite.
- **Opened:** yes

### Ariv Gupta’s Post
- **Who:** Ariv Gupta (Little Cursor, Big Planet)
- **Date:** LinkedIn showed “3d” when fetched on 2026-08-15 (about 2026-08-12); no calendar date on the public page
- **URL:** https://www.linkedin.com/posts/arivgupta_grokbot-activity-7493017815508090880-w5C3
- **What it teaches / what they ran:** Practice with a Bot he calls sandeep (chief of staff): streamlined outbound, managed inbound, and helped plan a study-abroad trip; he describes Grok Bot as the way he works with many agents at once on a shared computer.
- **Opened:** yes

### jjcm comment on HN “Grok Bot”
- **Who:** jjcm (Hacker News)
- **Date:** thread shown as “3 days ago” when fetched on 2026-08-15 (about 2026-08-12); no calendar date on the page
- **URL:** https://news.ycombinator.com/item?id=49261514 (comment id 49263241)
- **What it teaches / what they ran:** About a month of use: domain-separated Bots with their own routines; token spend was very high; a fabric-supplier Bot contacted ~40 Vietnam suppliers (started at 5, then 5 more, then he pushed +30), negotiated, locked a supplier, and worked with a prototyper Bot to send a generated logo pattern as a .ai file for samples.
- **Opened:** yes

## Secondary recaps

### SpaceXAI's Grok Bot turns agents into persistent digital coworkers that can operate your apps for $120-per-month
- **Who:** Carl Franzen / VentureBeat
- **Date:** August 11, 2026, 2:07 pm PT (Aug 12, 2026 4:07 AM ICT)
- **URL:** https://venturebeat.com/orchestration/spacexais-grok-bot-turns-agents-into-persistent-digital-coworkers-that-can-operate-your-apps-for-120-per-month
- **What it recaps:** Launch, pricing ($120 Teams Premium / $200 Ultra / SuperGrok Heavy), official role names, and quotes from Lenny Rachitsky and Matt Shumer (Shumer: researcher + writer + Chief of Staff coordination “worked out of the box”; no user model picker). Original Shumer/Lenny X posts were not opened.
- **Opened:** yes

### Grok is now an AI ‘teammate’ you can assign work
- **Who:** Jess Weatherbed / The Verge
- **Date:** Aug 12, 2026, 11:58 AM UTC (Aug 12, 2026 6:58 PM ICT)
- **URL:** https://www.theverge.com/ai-artificial-intelligence/978666/spacexai-grok-bot-ai-agent-beta-launch
- **What it recaps:** Launch recap of messaging Bots, parallel/group coordination, workflow learning, and beta access (SuperGrok Heavy, Cursor Ultra, Cursor Teams Premium). No original hands-on walkthrough.
- **Opened:** yes

### How to Set Up Grok Bot and Build Your First AI Agents
- **Who:** MindStudio (mindstudio.ai/blog)
- **Date:** not stated on the page
- **URL:** https://www.mindstudio.ai/blog/grok-bot-setup-guide
- **What it recaps:** Secondary setup write-up: name/title/description, conversational onboarding, shared plugins, scheduled vs Slack/GitHub/Teams triggers (invite the Slack app into the channel), Teach a task, and a claim that an agent self-edited a “like posts” skill after spotting ambiguity.
- **Opened:** yes

### What Is Grok Bot? How It Works, Pricing, and Alternatives
- **Who:** Atomic Bot (atomicbot.ai)
- **Date:** 13 August 2026
- **URL:** https://atomicbot.ai/blog/what-is-grok-bot
- **What it recaps:** Competitor explainer that checks official docs (shared computer, no per-Bot isolation, Teach a task, no model picker, trial/pricing). It also attributes a pre-launch use case to Danny Limanseta (74 game assets in ~2 hours via his art tool); that original Limanseta post was not found/opened here.
- **Opened:** yes

### Grok Bot Explained: xAI's Always-On AI Agents (2026)
- **Who:** Adel Dahani / AY Automate (ayautomate.com)
- **Date:** not stated; article says Grok Bot shipped August 11, 2026 and uses walkthroughs from that week
- **URL:** https://www.ayautomate.com/blog/grok-bot-xai-ai-agents-explained
- **What it recaps:** Product walkthrough plus four use cases it says came from same-week videos by Paul J Lipsky and Brendan Jowett: Beehiiv stats via Teach a task, 30-minute X-account watch routine, Gmail MCP inbox triage, Salesforce computer-use research. Those two source videos were not opened.
- **Opened:** yes

### Grok Bot (Hacker News thread)
- **Who:** submitted by rvz; 343 points / 331 comments when fetched
- **Date:** shown as “3 days ago” when fetched on 2026-08-15 (about 2026-08-12)
- **URL:** https://news.ycombinator.com/item?id=49261514
- **What it recaps:** Launch discussion. The how-to/use-case substance is mostly jjcm’s fabric-sourcing comment (listed above). Much of the thread is token-cost, prompt-injection, and “bots emailing 40 suppliers” debate, not a guide.
- **Opened:** yes

## Opened but not kept as how-to / use-case

None of the required URLs were skipped. Extra official pages opened and kept because they are how-to (get-started, bots, skills, chat, files, mobile, approvals, teams).

## Could not open, or original not found

- **Eric items 41–100:** fxtwitter returned the note through item 40 only. https://twiscan.com/en/x/ericzakariasson/2087258914060664902 hit a Cloudflare challenge and did not return the rest.
- **Danny Limanseta Grok Bot post:** mentioned by atomicbot.ai; public search did not surface an openable Grok Bot how-to URL (only older Grok 3 / Grok 4.5 game posts).
- **Matt Shumer and Lenny Rachitsky X posts:** quoted in VentureBeat / Techmeme; original status URLs were not found/opened.
- **Other launch-day X posts** (Alex Finn, Lauren / @poteto, Andrew Milich, Shane / @shaneapollo, Ben Lang, etc.): seen only as Techmeme snippets, not opened as first-party pages, so not listed as KEEP items.
- **X MCP:** not used (dead, per brief).

## Search note

Additional search on 2026-08-15 for `"Grok Bot" (guide OR tutorial OR "how to" OR "use cases" OR "I built" OR routine) 2026 August` plus named-user queries. Extra how-to pages that opened and qualified: official get-started / bots / skills / chat / files / mobile / approvals / teams, MindStudio setup guide, AY Automate explainer. Several search hits were launch scrapes, Grok Voice Agent Builder, or OpenClaw/Hermes guides and were not Grok Bot how-tos.
