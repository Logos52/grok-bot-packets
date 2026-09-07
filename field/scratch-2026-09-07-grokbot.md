# grokbot.dev — 2026-09-07 education sweep (fourteenth)

- feed: fetched `/api/v1/feed.json` → `scratch-2026-09-07-feed.json` (HTTP 200)
- **generated_at**: `2026-09-06T17:03:17.823Z` (00:03 ICT 7 Sep)
- **count**: **638 → 668** (+30 vs prior feed `scratch-2026-09-06-feed.json` generated_at `2026-09-05T17:41:09.799Z` count 638)
- newest_added_at: `2026-09-06T14:05:41.816Z`
- types overall: template 467 · use-case 138 · plugin 45 · collection 16 · news 2
- **delta vs Sep-6 feed**: **+30 templates only** (use-cases 0 · plugins 0 · collections 0 · news 0)
- Confirmed: **no new awesome_score ≥80 education/language use-case**; newest use-cases remain ≤2026-08-28 and none new are education/tutor/Anki lane.
- Skip list: `scratch-2026-09-07-seen-urls.txt` (640 URLs) — 0 new delta URLs matched.

## New template slugs since prior feed — bounce as library
(cutoff = prior feed generated_at `2026-09-05T17:41:09.799Z`; 28 templates with added_at ≥ cutoff; +2 pre-cutoff slugs appear in slug-diff vs Sep-6 file — listed for completeness)

1. `cue` (2026-09-05T18:56Z)
2. `prototype-designer` (2026-09-05T19:06Z)
3. `product-designer` (2026-09-05T19:31Z)
4. `lyric-guard` (2026-09-05T19:39Z)
5. `agent-manager` (2026-09-05T20:02Z)
6. `domain-tracker` (2026-09-05T20:02Z)
7. `campusops` (2026-09-05T20:19Z) — cats student/learning; syllabi→study plan — **library bounce** (template)
8. `jobs-2` (2026-09-05T21:00Z) — cats include learning; product-coach wedge metric — **library bounce**
9. `hire-bot` (2026-09-05T21:14Z)
10. `lot-ghost` (2026-09-05T21:22Z)
11. `petty-bot` (2026-09-05T21:35Z)
12. `adie` (2026-09-05T22:53Z)
13. `ucd-bot` (2026-09-05T23:01Z)
14. `forja` (2026-09-05T23:18Z)
15. `slacker` (2026-09-05T23:28Z)
16. `raven` (2026-09-06T01:26Z)
17. `radar` (2026-09-06T03:10Z)
18. `crew` (2026-09-06T03:13Z) — cats include learning; manager coaching — **library bounce**
19. `habit-referee` (2026-09-06T03:28Z)
20. `arthur` (2026-09-06T03:30Z)
21. `illy` (2026-09-06T03:34Z)
22. `user-researcher` (2026-09-06T06:41Z)
23. `botops-chief-of-staff` (2026-09-06T07:10Z)
24. `content-writer` (2026-09-06T07:56Z)
25. `call-desk` (2026-09-06T08:40Z)
26. `interaction-designer` (2026-09-06T09:07Z)
27. `ai-master` (2026-09-06T11:03Z)
28. `personal-assistant` (2026-09-06T14:05Z)

Pre-cutoff slugs present in delta file compare only:
- `japanese-registry-certificate` (2026-09-05T12:04Z) — JP company registry cert walkthrough; not language-learning
- `printerbot` (2026-09-05T17:20Z) — 3D character portraits for bot fleet

## Education / language gate
- Strict filter (edu cats or anki/tutor/language-learning keywords on **use-case**): **0 new** in window.
- score≥80 use-cases in catalog are all Aug GTM/personal (Amazon cart, CFO, content team, etc.) — **not education lane**; none added since cutoff; all already in prior feed.
- Templates with `learning`/`student` cats in delta (`campusops`, `crew`, `jobs-2`) remain **marketplace library** — bounce per Field rule. `campusops` is closest (syllabi→study plan) but still a template, not a named education use-case ≥80.

## News / tool announcements
- **0 new news** items (catalog still news=2, unchanged). No Brief bounce one-liners for Claude Code / Grok Build / Grok Bot / Cursor Cloud Agents / Obsidian.

## Fetch notes
- Primary: `https://grokbot.dev/api/v1/feed.json` → 200, 610445 bytes written.
- RSS fallback not needed.
- Removed slugs vs prior: 0.
- Fourteenth sweep (yesterday thirteenth).

## Result for education hunter
- grokbot.dev contributes **0 KEEP** this packet.
- All 30 new slugs → **bounce as library/templates** (28 since cutoff + 2 pre-cutoff slug-diff).
