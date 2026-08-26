# Guides and useful posts: Grok 4.6 + Grok Bot
Compiled 2026-08-15. First-party pages opened or confirmed. X connector was down; public fetches only.

## Grok 4.6 (the model)

### Official
- [Grok 4.6 model page](https://docs.x.ai/developers/grok-4-6) — SpaceXAI docs. How to call `grok-4.6` (API, SDK, curl). 500k context, reasoning low/medium/high/xhigh, tools, pricing $2/$6 per 1M. Points to prompt caching and context compaction for long agent loops.
- [Introducing Grok 4.6](https://x.ai/news/grok-4-6) — SpaceXAI, 2026-08-12. Launch post: long-running agents, visual/interactive work. Available in Cursor, Grok Build, API, OpenRouter/Vercel/Cloudflare.
- [Grok 4.6 in GitHub Copilot](https://x.ai/news/grok-4-6-github-copilot) — SpaceXAI, 2026-08-14. How to pick it in Copilot (VS Code, CLI, cloud agents).
- [Reasoning](https://docs.x.ai/developers/model-capabilities/text/reasoning) — SpaceXAI docs. `reasoning_effort` on 4.6, including `xhigh`. Default is high; cannot disable.
- [Docs overview / first request](https://docs.x.ai/overview) — SpaceXAI docs. Quickstart snippet using `grok-4.6`.
- [Release notes](https://docs.x.ai/developers/release-notes) — SpaceXAI docs. 4.6 ship note + pricing tiers (cached input, >200k prompts).
- [Model card (PDF)](https://media.x.ai/v1/website/card-7f81d41b.pdf) — SpaceXAI, 2026-08-12. Eval/training card. Consumer Grok surfaces (web/X) said to come later.
- [Grok Build overview](https://docs.x.ai/build/overview) — SpaceXAI docs. 4.6 is the default coding-agent model.

### Official (Grok Build + long loops)
- [Grok 4.6 model detail](https://docs.x.ai/developers/models/grok-4.6) — short vs ≥200k pricing, rate limits, regions
- [Models](https://docs.x.ai/developers/models) — official routing: for everything else including code, use 4.6
- [Grok Build modes and commands](https://docs.x.ai/build/modes-and-commands) — `/model`, `/effort`, `/plan`, `/deep-research`, `/loop`
- [Plan Mode](https://docs.x.ai/build/features/plan-mode) — when to plan vs skip; approve/comment
- [Headless and scripting](https://docs.x.ai/build/cli/headless-scripting) — `grok -p`, CI flags
- [Maximizing cache hits](https://docs.x.ai/developers/advanced-api-usage/prompt-caching/maximizing-cache-hits) — `prompt_cache_key` / `x-grok-conv-id` for multi-turn 4.6
- [Context compaction](https://docs.x.ai/developers/advanced-api-usage/context-compaction) — compact long agent loops

### Named / partner how-to
- [Grok 4.6 – A field guide](https://www.linkedin.com/pulse/grok-46-field-guide-eric-zakariasson-vgkde) — Eric Zakariasson, 13 Aug 2026. Daily-driver prompting: “work very hard” did not help; highest-leverage line was verify-and-iterate until production-ready. Runs: Next.js spreadsheet, 3D frame-check, QA, inbox, Remotion, games, deck.
- [Grok 4.6 on Vercel AI Gateway](https://vercel.com/changelog/grok-4-6-now-available-on-ai-gateway) — 12 Aug 2026. `model: 'xai/grok-4.6'`, `reasoning: 'xhigh'`
- [Developers Digest release guide](https://www.developersdigest.tech/blog/grok-4-6-release-guide-2026) — 13 Aug 2026. OpenCode install + when to pick 4.6 vs Sol
- [Cursor forum: Share your thoughts on Grok 4.6](https://forum.cursor.com/t/share-your-thoughts-on-grok-4-6/168190) — 12–13 Aug. In Cursor context is 256k (not API 500k); xhigh fills it faster

### Practical how-to (not official)
- [How to Use the Grok 4.6 API?](https://apidog.com/blog/how-to-use-grok-4-6-api/) — Apidog, after 2026-08-12. End-to-end API walkthrough (key, curl, OpenAI-compatible SDK). Note: they write `grok-4-6` in one place; official model name is `grok-4.6`.
- [Grok 4.6 Is Live: Migrate From 4.5 Now](https://byteiota.com/grok-4-6-is-live-migrate-from-4-5-now/) — byteiota. One-line model swap; warns hyphen vs dot.

### Thin / skip
Generic “How to use Grok” posts (SurePrompts, GPT Prompt Coder, TheBizAIHub) are older Grok, not 4.6. Model card PDF at media.x.ai returned 500 on re-fetch.

## Grok Bot (the teammate app)

### Official how-to
- [Get started](https://docs.x.ai/grok-bot/get-started) — Install, sign in, create first Bot, first-task template (outcome / sources / constraints / deliverable / review point), login handoff.
- [Overview](https://docs.x.ai/grok-bot/overview) — What a Bot is; start with a real multi-tool task; no workflow builder required.
- [Use cases](https://docs.x.ai/grok-bot/use-cases) — Official role recipes: Sales Outbound, Talent Scout, Paid Media, Expense Manager, Product Performance, Bug Reproduction, Account Health, Chief of Staff. Pattern: own a repeatable outcome, then skill → routine.
- [Create and manage Bots](https://docs.x.ai/grok-bot/bots) — Name, job, description. Smallest useful roster. Do not use Bots as a security boundary.
- [Computer and apps](https://docs.x.ai/grok-bot/computer-and-apps) — Shared cloud computer, Agent Computer preview, takeover for 2FA, Plugins vs browser, `/workspace`.
- [Skills, routines, and automations](https://docs.x.ai/grok-bot/skills-routines-and-automations) — Skill vs routine, teach-by-demo, event triggers, test-before-enable, approval for send/buy/delete.
- [Chat and collaboration](https://docs.x.ai/grok-bot/chat-and-collaboration) — Group chats, @mentions, handoffs, threads.
- [Files and results](https://docs.x.ai/grok-bot/files-and-results) — Attachments, reviewable artifacts, evidence (links, screenshots, action log).
- [Approvals, security, and privacy](https://docs.x.ai/grok-bot/approvals-security-and-privacy) — Auto-review, never paste passwords in chat, shared-computer boundary.
- [FAQ](https://docs.x.ai/grok-bot/faq) — One computer per user, not per Bot.
- [Troubleshooting](https://docs.x.ai/grok-bot/troubleshooting) — Sign-in, computer recover/reset, stuck Bot, routines, attachments.
- [Mobile](https://docs.x.ai/grok-bot/mobile) — iOS companion.
- [Introducing Grok Bot](https://x.ai/news/introducing-grok-bot) — SpaceXAI, 2026-08-11. Launch post.
- [Teams and enterprises](https://docs.x.ai/grok-bot/teams-and-enterprises) — admin rollout, one computer per member, plugin policy, Legacy Privacy Mode blocks the product
- [Product page](https://x.ai/bot) — Teach a task, group handoffs, published prices

### Named posts people actually ran
- [@mattyp — Intro to Grok Bot](https://x.com/mattyp/status/2087252657589412119) — Matt Palmer, launch week. Demo Bot (approve → Cloud agent), Content Bot, Product Bot, 2FA handoff. Public fetch via `https://api.fxtwitter.com/mattyp/status/2087252657589412119`.
- [@mattyp — Content Bot + overnight computer](https://x.com/mattyp/status/2087314806596641159) — 2026-08-11. Daily X-bookmarks → draft prompt → ask approval → Cursor Cloud agent → record a demo. Also login/2FA handoff. (Grocery/delivery example is in the same post; skip if you only want the content pipeline.)
- [@ericzakariasson — 100 use cases](https://x.com/ericzakariasson/status/2087258914060664902) — Catalog of setups he had seen by launch day. Useful as a menu, not a how-to. `https://api.fxtwitter.com/ericzakariasson/status/2087258914060664902`.
- [Nate — Grok Bot review](https://natesnewsletter.substack.com/p/grok-bot-review) — Nate, 2026-08-14. 12 Bots in ~8 hours. Rule he kept: a Bot owns a theme, not a task. Mom login handoff.
- [Emily Gavrilenko — skippy EA + specialists](https://www.linkedin.com/posts/emily-gavrilenko_grokbot-activity-7493001034894626817-m4JC) — LinkedIn. EA plus specialist Bots; human gate.
- [Ariv Gupta — CoS bot “sandeep”](https://www.linkedin.com/posts/arivgupta_grokbot-activity-7493017815508090880-w5C3) — LinkedIn. Named chief-of-staff Bot.
- [jjcm — WhatsApp fabric sourcing](https://news.ycombinator.com/item?id=49261514) — HN. GUI-as-API over WhatsApp; token burn / coverage ceiling.
- [Ruben Hassid — daily digest via Gmail](https://ruben.substack.com/p/what-the-f-is-an-agent) — Substack, 2026-08-12. Quiet-when-nothing digest pattern.
- [VentureBeat — Matt Shumer on Grok Bot](https://venturebeat.com/orchestration/spacexais-grok-bot-turns-agents-into-persistent-digital-coworkers-that-can-operate-your-apps-for-120-per-month) — 2026-08-11. Secondary writeup of Shumer’s run (X original was 403).

### Secondary explainers (how-to-ish, not a named runner)
- [What Is Grok Bot?](https://atomicbot.ai/blog/what-is-grok-bot) — 2026-08-13. Comparison + shared-computer claim. Useful for the killed “one computer per bot” myth.
- [How to Set Up Grok Bot](https://www.mindstudio.ai/blog/grok-bot-setup-guide) — MindStudio. Secondary setup: name/title/description, Teach a task, Slack/GitHub/Teams triggers
- [The Verge launch recap](https://www.theverge.com/ai-artificial-intelligence/978666/spacexai-grok-bot-ai-agent-beta-launch) — Aug 12. No hands-on walkthrough
- [AY Automate explainer](https://www.ayautomate.com/blog/grok-bot-xai-ai-agents-explained) — walkthrough plus use cases it attributes to videos (those videos not opened)

Note: Zakariasson “100 use cases” public fetch stopped at item 40. Danny Limanseta 74-asset first-party post not found. Shumer/Lenny X originals not opened.
