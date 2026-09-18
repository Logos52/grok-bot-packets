# Grok Bot Galaxy — Day 2 + Day 3 summary

Compiled: 2026-09-18 by dr stewbot from Galaxy's EOD notes.
Sources:
- `notes/2026-09-16-day-2-grok-bot-galaxy.md`
- `notes/2026-09-17-day-3-grok-bot-galaxy.md`

---

## Day 2 — 2026-09-16 · Game Studio LIVE

- **URL:** https://x.com/i/broadcasts/1PKqrNyvmYwGb
- **Length / views:** ~8:23 player · ~378K views
- **Schedule spine:** Sales Engineering (Amrita) → Sales → SDRs (Simon Lackowski) → Customer Support (David Gan) → Cupcake build / sound design → end card (“Final day starts tomorrow 8:30am PST”)
- **Gap:** midday Sales block sparsely scrubbed

### What happened (field)
- **SE / templates:** Grok Bot Templates framed as characters with attributes (CHA/DEX/INT…); agenda Welcome → Introducing → Why → SE use cases → Demo → Learned → Q&A → Build.
- **Product pitch:** bots for jobs, message like teammates, retain context, connect tools, automations/routines.
- **Travel/support demo:** Postgres row locks + 10-min hold so two customers can’t claim same seat; Serena/Sherlock support workflow; Southwest/Spirit test plan.
- **SDR (Simon):** Prospecting (ICP → titles) · Sequencing (CSV/XLSX) · Account Research · Drafting Copy. Wrap: Go End to End · Be Intentional · Think Systematically.
- **Ping demo:** inbox + task kanban; mention listener.
- **Cupcake fleet:** Chief, Bake, Glow, Crit, Pixel, Ping, Shardul, Data, arena, Tone (audio); Notion as SsOT (Crit hit Notion **404**); cloud-agent PR swarm on `shipbythursday/cupcake`.
- **Support Agent Rules:** (1) read Plain thread (2) Public Docs answer / Internal Policies decide-only never paste (3) Reply vs Handoff by confidence (4) Act if needed e.g. Stripe (5) write reply + note; Auto-review before Slack.
- **Sound design:** Tone → Foley stubs + Suno/Strudel into Notion; on-air listen.
- **Promo:** free month via duplicate **dr eggbot** (first 1,000).

### Themes
1. Department playbooks (SE → Sales → SDR → Support), not one generic agent
2. Templates + competition / attribute framing
3. Notion as single source of truth (and connector fragility)
4. Named single-duty fleet
5. Support discipline: public vs internal + confidence handoff
6. Creative pipeline bots (audio → Foley/Suno)
7. Audience affinity for poteto / dr eggbot

### Top improvements (for Wedge’s fleet — recs only)
1. SsOT + connector honesty (Steward + Watch)
2. Reply vs Handoff confidence gate (Intake + Brief)
3. Public vs internal knowledge split (Corpus + Steward)
4. Fleet-tell / shared memory broadcast on rule changes
5. Named single-duty clarity (no new bots)
6. Auto-review before external write
7. Dated creative artifacts stay in Galaxy notes
8. poteto-mode for nontrivial build-adjacent work
9. Token/cost opacity watchline

---

## Day 3 — 2026-09-17 · Launch day / company in 3 days

- **URL:** https://x.com/i/broadcasts/1YGNrbXEeazGw
- **Length / views:** ~7:58 player · ~183.5K views
- **Hub:** https://x.ai/galaxy · Luma https://luma.com/3ifrgttw
- **Schedule spine:** MarOps (Silberman/Hsu) → Build / Cupcake → Post-Sales/CS (Blake Schuller) → Thursday Arena → Marketing (Josh Kim / Dan Hill on-stream) → wrap + showcase + credits → thanks card

### What happened (field)
- **Open / build:** Cupcake eng (tater, bento, +40); free month promo; Bake PRs/Vercel; CUPCAKE leaderboard (@roshan_s / @poteto GOLD); fleet overlay sample 43 bots / 120 messages.
- **MarOps:** Why Grok Bot tiles (iMessage-easy, 24/7, uses your tools, finishes work, shareable templates). Dream team: **OP-1** CoS · **Fisher** EA · **Juno** PM · **Ondes** Eng. **Territory Planner** Approve vs Hold. Juno locks Lead Deck md → Ondes/cloud Accept/Skip/Reject. First Contact preview (Sofia Reyes). Learned: staff dream team · governed agency beats ask-each-time or YOLO · you are a PM, product is revenue.
- **Midday Cupcake:** card-game UI; fleet steve/bento/ping/crumb/tater; HITL **hold — leave WAF** (no DDoS bypass); Poteto Mode + `/verify-cupcake`; funnel metrics (practice → X convert); Cerebro distribution doc.
- **CS Dream Team:** Franny Form (ROI form draft-only, won’t send) · Wally Writer · Trudy Truth · Frankie Follow Up · Scout.
- **Thursday Arena:** practice/public WR ~47%; ghosts eating new players; Season 1 metrics.
- **Marketing learned:** (1) Scope bots like a job description (2) Then trust them (3) Invest + copy marketplace templates.
- **Showcase:** matt palmer (@mattyp) — Bookmarks → Cursor Agent → screenshot/video validate → Cloudflare preview → morning Bot link. “If you can do it, it can be automated.”
- **Close:** chat “credits” → $200 Grok Bot credits for livestream viewers; end card thanks.

### Themes
1. Governed agency (Approve/Hold; leave WAF)
2. Scope then trust
3. Named single-duty fleets (MarOps / CS / Cupcake)
4. Spec/draft artifacts before side effects
5. Swipe / keyword HITL surfaces
6. Feeder → agent → validate → ship link
7. Game studio as company proof
8. Templates / marketplace as distribution

### Top improvements (for Wedge’s fleet — recs only)
1. Governed agency pin — external writes + destructive infra default Hold (Steward)
2. Scope-like-a-JD before agency (Intake; Galaxy stays notes-only)
3. Draft-only before send (Brief Accept/Skip/Reject)
4. Spec-handoff path before multi-bot builds
5. Bookmark/research feeder → validated ship link (Watch, no auto-post)
6. Template/marketplace demand flags (Watch)
7. poteto-mode + verify skill before swarm-like runs
8. Connector/path honesty (Steward + Watch)
9. Promo/credits awareness only — no bot change

---

## Cross-day through-lines
- Named single-duty bots beat bloated multi-duty context
- HITL gates (Hold / Handoff / draft-only / Auto-review) over YOLO
- SsOT + connector failure honesty
- Cupcake / game studio as the live multi-bot proof spine across Day 2–3
- Improvements stay recommendations — Galaxy does not create/edit fleet bots

## Full notes (source paths)
- Day 2: `/home/box/agent-data/agents/6330ef4d-4d6f-463b-924e-8403b6d8c5cd/notes/2026-09-16-day-2-grok-bot-galaxy.md`
- Day 3: `/home/box/agent-data/agents/6330ef4d-4d6f-463b-924e-8403b6d8c5cd/notes/2026-09-17-day-3-grok-bot-galaxy.md`
