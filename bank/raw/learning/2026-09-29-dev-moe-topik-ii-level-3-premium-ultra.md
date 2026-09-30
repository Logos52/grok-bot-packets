---
id: 2026-09-29-dev-moe-topik-ii-level-3-premium-ultra
kind: article
title: TOPIK II Level 3 Premium Ultra Pro (KO+Myanmar offline PWA)
source: "https://github.com/Dev-moe-kyawaung/TOPIKII-Level-3-pro-v3.0"
author: Dev-moe-kyawaung
published: 2026-09-29
captured: 2026-09-29
via: grok-bot/Field
lane: learning
status: raw
private: false
---

# TOPIK II 3급 Premium Ultra Pro · စာမေးပွဲပြင်ဆင်ရေး

Offline-first study app for **TOPIK II Level 3** with Korean + Myanmar (မြန်မာ) explanations.
React 18 · TypeScript · Vite · Tailwind CSS v4 · Zustand · React Router · Recharts · IndexedDB (`idb`) · Web Audio API · PWA (service worker + `workbox-window`).

## Features

| Area | What it does |
| --- | --- |
| Dashboard | Daily goal, streak, D-day, due cards, 14-day activity chart, today's plan |
| Grammar (100) | Browse/search/filter, detail cards (pattern, Myanmar meaning, usage, 3 examples, common mistake), **SRS review** |
| Vocabulary (300+) | 9 categories, detail cards (pronunciation, POS, definition, synonyms/antonyms, 2 examples, collocations), **SRS review**, multiple-choice quiz |
| Mock exam | Listening / Reading / Writing simulator: countdown timer, question navigator, flags, auto-scoring, level estimate, per-question review |
| Writing assistant | Editor with 원고지-style char counter, **rule-based checker** (style 다체 vs 합니다/해요, spelling, spacing, informal words, structure, connectors, grammar detection) + score estimate, 4 fill-in-the-blank templates × 4 paragraphs with useful expressions and 3 scored samples each |
| Listening | Audio player (chime via Web Audio API, TTS narration, speed control, live transcript, Myanmar translation), **shadowing recorder** (MediaRecorder + level meter, takes stored in IndexedDB) |
| Reading | Passages with highlighted key vocabulary, Myanmar translation toggle, explanations, tag chips that open grammar/vocab cards |
| Analytics | Recharts: activity, minutes, skill radar, SRS status donut, exam trend, weak tags, category mastery |
| Study plan | Generates a day-by-day plan (foundation → practice → mock) from exam date, hours/day and score gap |
| PWA | Service worker (shell precache, network-first navigation, stale-while-revalidate assets/fonts), offline banner, install prompt, Background Sync hook |

## Content (all under `src/data/`)

```
grammar/            10 files × 10 items  (category, form, pattern, match[], Myanmar meaning, usage, 3 examples, level, frequency, common mistake)
vocabulary/         18 files / 9 categories, 300+ words (compact row format, expanded in src/data/index.ts)
past-papers/        22 files = 11 years (2015–2025) × { listening, reading-writing }
writing-templates.json   4 templates × 4 paragraphs, blanks, expressions, 3 samples each
```

**Please read — content notes**

* The "past papers" are **original practice sets written in the style and topics of TOPIK II**. They are *not* the official exam papers (those are copyrighted). Chart data in writing tasks is fictional. Each file says so in its `source` field.
* Each year has 2 listening + 2 reading questions and 1 writing task (11 × Q53/Q54 alternating), so the mock exam is a short sampler, not a full 50-question paper. Add more items by dropping JSON files into `src/data/past-papers/` — they are discovered automatically via `import.meta.glob`.
* Myanmar translations were written for this project and should be reviewed by a native speaker before publication.
* The writing score is a heuristic **estimate**; real TOPIK writing is graded by humans.
* Audio uses the browser's speech synthesis (TTS). Devices without a Korean voice fall back to showing the script.

## Scripts

```bash
npm install
npm run dev        # local dev
npm run build      # production build -> dist/ (single-file build via vite-plugin-singlefile)
npm run preview    # serve dist/
npx tsc --noEmit   # type-check
npx eslint src     # lint (eslint.config.js)
npx prettier --check "src/**/*.{ts,tsx,css,json}"
```

## Project layout

```
src/
  components/ui/        Button, Input/Textarea/Select, Card, Modal (focus trap), Progress, Badge, Bi (bilingual text)
  components/features/  GrammarCard, VocabCard, FlashSession (SRS UI), AudioPlayer, Recorder, QuestionView, PracticeShell, TemplatePanel, Charts
  components/layout/    Layout (sidebar + bottom nav), ErrorBoundary
  pages/                Dashboard, Grammar, Vocabulary, Exam, Writing, Listening, Reading, Analytics, StudyPlan, Settings
  hooks/                useSRS, useTimer, useAudio (useSpeech + useRecorder), useProgress, usePwa
  store/                Zustand store persisted to IndexedDB
  utils/                srs (SM-2), db (idb), writingChecker, studyPlan, pwa (Workbox + sync), tts, date
  data/                 JSON content + loader
public/                 sw.js, manifest.webmanifest, icons
```

## Deploy (Vercel + GitHub Actions)

1. Create a Vercel project and run `vercel link` locally to get `VERCEL_ORG_ID` and `VERCEL_PROJECT_ID`.
2. Add GitHub repo secrets: `VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID` (optional: `VITE_SYNC_ENDPOINT`).
3. Push to `main`. `.github/workflows/ci.yml` runs type-check/lint/prettier (non-blocking at first), builds, runs Lighthouse CI (`lighthouserc.json`, target ≥ 0.9) and deploys with the Vercel CLI. Pull requests get preview deployments.

`vercel.json` adds SPA rewrites, security headers and `Service-Worker-Allowed`.

## Technical notes / honest limitations

* **Service worker:** this scaffold locks `vite.config.ts`, so `vite-plugin-pwa` could not be wired in. `public/sw.js` implements Workbox-style strategies by hand and is registered with `workbox-window`. If you control the Vite config you can swap it for `vite-plugin-pwa` (`injectManifest`) without touching app code.
* **Single-file build:** the provided Vite config uses `vite-plugin-singlefile`, so the whole app (including JSON data) is inlined into `dist/index.html` (~1.1 MB, ~310 KB gzip).
* **Routing:** `HashRouter` is used so the build works from any static host/sub-path without rewrites.
* **Lighthouse:** the app is built for ≥ 90 (lazy routes, semantic HTML, contrast-checked palette, no layout-shifting images), but no score was measured in this environment — the CI job will report it.
* **Background Sync:** queued via the Sync API when going offline; the service worker wakes a client, which POSTs a snapshot to `VITE_SYNC_ENDPOINT` if you configure one. Without an endpoint it is a no-op (data stays in IndexedDB).
* **Accessibility:** skip link, focus-visible ring, labelled controls, `role=progressbar/timer/radiogroup/tablist`, focus-trapped dialogs, reduced-motion support, color never used as the only signal. Not audited with a screen reader.
* **ESLint/Prettier:** packages were installed with the project's package tool and therefore live in `dependencies`; move them to `devDependencies` if you prefer.

## Data format quick reference

Grammar file: `{ "category", "ko", "my", "items": [ { form, pattern, match[], meaning, meaningKo, usage, examples[{ko,my}], level 1-3, frequency 1-5, mistake{wrong,right,note} } ] }`

Vocabulary compact row: `[word, pronunciation, pos, meaning(my), definition(ko), synonyms(csv), antonyms(csv), ex1 ko, ex1 my, ex2 ko, ex2 my, collocations(csv), frequency]` — or use a `words: []` array with full objects.

Past-paper files: `{ year, round, source, section: "listening" | "reading-writing", items | reading[] | writing[] }`.
