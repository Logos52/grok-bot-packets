# MyGermanBD

[![CI](https://github.com/mohammadrezwankhan/mygermanbd-demo/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/mohammadrezwankhan/mygermanbd-demo/actions/workflows/ci.yml) · [MIT license](LICENSE) · [Verification and limits](QUALITY_REPORT.md)

Local-first German-learning and Germany-research workspace with practice, planning and explicitly unverified guidance.

If MyGermanBD helps you study this workflow, a star helps other Bangla/English learning-tool developers find it.

![Actual desktop demo](docs/repository/demo-desktop.png)

## Try the demo

[Open the hosted synthetic demo](https://mohammadrezwankhan.github.io/mygermanbd-demo/) or run the identical standalone artifact locally:

Prerequisite: Node.js 22 or later; tested here with Node.js 24. This runs locally with synthetic examples. It does not connect to a live provider or publish user input.

```sh
git clone https://github.com/mohammadrezwankhan/mygermanbd-demo.git
cd mygermanbd-demo
node scripts/preview-demo.mjs
```

Open **http://127.0.0.1:4173**. Stop the server with Ctrl+C. The first screen is a demonstration, not verified current information. Keep private or real-world records out of this evaluation.

## Why inspect this project?

MyGermanBD joins language practice with a Germany-research workspace. The design challenge is to preserve the unverified status of planning guidance while retaining useful local study progress.

Read the [engineering walkthrough](docs/engineering/CASE_STUDY.md) and [adjacent-tool comparison](docs/ALTERNATIVES.md), or follow the [source map](PROJECT_ANALYSIS.md).

- [Current verification and limits](QUALITY_REPORT.md)
- [Architecture and source map](docs/architecture/system-overview.md)
- [Contribution guide](CONTRIBUTING.md) and [small contribution tasks](docs/CHAMPION_QUESTS.md)
- [Security reporting](SECURITY.md), [support](SUPPORT.md), and [roadmap](ROADMAP.md)

## Develop and verify

Install source dependencies with `npm ci --ignore-scripts` when a package lock is present. Dependency-free applications need no install. Source commands are distinct from the bundled-demo quick start.

```sh
npm run typecheck
npm test
npm run build
```

Prior reports under `docs/` describe the supplied candidate. They do not replace the current [quality report](QUALITY_REPORT.md). Passing software checks is not clinical, educational, financial, safety, or production-service validation.

## License and scope

First-party source is available under [MIT](LICENSE). Bundled dependencies retain their upstream notices; trademarks and third-party content are not relicensed.

<details>
<summary>Supplied engineering guide, product boundaries, and detailed usage</summary>

# MyGermanBD Champion
## Your next chapter, one small step at a time.

A repaired and redesigned **local-first German-learning and Germany-research workspace**, built from your supplied MyGermanBD project. This is a downloadable review candidate, not a deployed service or a certified language course.

**Version:** 0.2.0 · **Build:** `cee159d5fc42d945` · **Prepared:** 29 September 2026

## Start here — no installation needed

Open **`OPEN-MYGERMANBD.html`** in a current desktop browser. It includes its JavaScript and styles; no package installation or account is needed. The file can be used without a network connection after it has been downloaded. External source links require connectivity, and optional audio requires a local German system voice.

Browser storage rules for `file:` URLs vary. Keep the file at a stable location, do not use private browsing for important progress, and use **Data & settings → Export backup** regularly. Moving or renaming the file, changing browser profiles or clearing site data can make the old workspace unavailable. A JSON export is your portable backup; this app does not cloud-sync it.

## Recommended local-server mode

For a stable local origin, use the included prebuilt `dist/` folder and Node.js 22.16 or later:

```sh
node scripts/serve.mjs
```

Open **http://127.0.0.1:4173** in your browser. The server binds only to your own computer. Stop it with Ctrl+C. On Windows, double-click **`START-APP.bat`** after installing Node.js. On macOS/Linux, run `sh START-APP.sh`.

Keep using the same hostname and port: `localhost`, `127.0.0.1`, another port and a direct HTML file are separate storage origins. The static server is for local review, not public production hosting. No package install is required to serve the included build.

A scoped service worker and manifest are included for served use. Real browser installation, offline relaunch and update behaviour remain **unverified in this environment**; do not treat the manifest as proof of installability. Direct HTML-file mode does not register a service worker.

## What is working in this candidate

- **An actual learning path:** 12 original beginner micro-lessons, 36 four-option questions, explanations, reading-text access, optional speech transcripts and best-result tracking. Six skills have two lessons each.
- **A real word-review queue:** 24 German/English/Bengali cards, reveal-and-recall controls, and transparent 1/3/7/14/30-day remembered-word scheduling. Forgotten words stay due today.
- **A personal dashboard:** actual lesson completion, due words, activity streak and checklist progress; no fabricated learner, minutes studied or proficiency percentage.
- **Germany Explorer:** six research routes with category/search filters, persistent bookmarks and source details.
- **A safer local claim check:** parses actual hostnames, distinguishes a listed domain from a copied organisation name, flags specific warning wording and never calls an offer or provider verified.
- **Journey Passport:** five user-marked research prompts, notes, guarded note deletion and a Markdown plan export.
- **Data controls:** optional nickname, goal and daily target; JSON export; validated import with preview and explicit replacement; typed confirmation before deleting only this app’s stored key.
- **Responsive navigation:** desktop sidebar, phone navigation, global Ctrl+K / Command+K search, light/dark themes, keyboard focus handling and reduced-motion styles.

The language switch translates primary navigation and page headings; word cards also contain Bengali meanings. Lesson explanations and detailed guidance remain English. A completed lesson is not a CEFR assessment, certificate, exam result or pronunciation grade. The learning time shown is a suggested target, not tracked study time.

## Source and privacy boundaries

The eight source records are inherited reference entries, including one explicitly illustrative record. Seven entries point to listed organisations. **They have not been independently rechecked in this work.** The app does not fetch source pages, verify providers, decide visa/admission eligibility, submit applications or guarantee outcomes.

No login, payment, analytics, cloud database or remote AI service has been added. Normal lesson and planning interactions use local state. External destination links open the named site. Local browser data and downloaded backups are not encrypted by this app: do not put passports, bank records or other sensitive documents in notes. Avoid simultaneous edits in multiple tabs; storage synchronisation is last-writer-wins, not a transactional database.

## Source development

The original React/Vite/TypeScript architecture is preserved, with focused modules for learning, planning, state and pure rules. Dependency versions are pinned to the exact versions already resolved by the supplied lockfile; no dependency upgrade was performed.

```sh
npm ci
npm test
npm run typecheck
npm run build
npm run preview
```

`npm ci` requires access to the package registry and installs native packages for your operating system. The uploaded dependency folder contained Windows binaries, so it is deliberately **not** included in this handoff. Install afresh rather than copying that folder to another platform.

### How the included build was made

The normal Vite pipeline could not run in the available Linux environment: the supplied tree lacks working Linux native bindings, and package downloads were blocked. The included build was generated with the reviewed **`scripts/build-portable.mjs`** alternate builder. It uses production React/React DOM/Scheduler, only the imported Lucide icons, and the available TypeScript **5.8.3 JavaScript compiler**. It does not fake a successful Vite build.

```sh
# Requires installed dependency packages and a TypeScript JS compiler.
# The supplied TypeScript 7 native package is not that JS compiler.
npm ci --ignore-scripts
npm run build:portable
```

The portable builder uses the locked `typescript-compat` 5.8.3 dependency installed by `npm ci`; global compilers and environment overrides are not used. The build script itself never downloads packages. `scripts/finalize.mjs` creates the standalone HTML and content-versioned public-asset worker after either supported build route.

## Evidence and test coverage

| Executed check | Result | Important boundary |
|---|---|---|
| Strict type check using TypeScript 5.8.3 | PASS | Alternative compiler; native TypeScript 7 toolchain not verified |
| Node rule/content/worker-contract tests | 58 passed; 0 failed/skipped | Worker tests use controlled fixtures |
| Real-bundle browser interaction groups | 22 passed | In-memory Chromium DOM; explicit MemoryStorage fixture |
| Responsive routes | 30 combinations passed | Six views at 320, 390, 768, 1024 and 1440 px; emulation only |
| Loopback HTTP serving checks | 8 passed | HTTP client, not browser navigation or service-worker lifecycle |
| Exact standalone HTML | PASS | Injected document; real storage denied, memory-only lesson verified |
| Native Vite build | BLOCKED | Native dependency environment |
| Real-origin storage, PWA install/offline relaunch, other browsers, human UAT | NOT VERIFIED | Required before public release |

The test harness explicitly supplies MemoryStorage and intercepts download clicks to inspect the generated Blob. These are not claims about operating-system download delivery, real browser reload persistence, production services or human acceptance.

```sh
# Optional UI evidence reproduction; requires Python Playwright and Chromium.
python tests/browser-harness.py local-review
python tests/http-standalone.py
```

Set `CHROMIUM_PATH` to the installed Chromium executable when it is not on PATH. No browser policies should be removed to run tests. The browser harness renders the real bundle in memory and does not navigate to a prohibited URL.

## Handoff documents

- `docs/champion/AUDIT_REPORT.md` — findings, repairs, architecture, scope and phase gates.
- `docs/champion/DESIGN_RELEASE.md` — design decisions, human-UAT tasks and controlled release/recovery preparation.
- `docs/champion/ISSUE_REGISTER.csv` — canonical issue and verification register.
- `docs/champion/BASELINE_RESULTS.csv` — baseline and final command results.
- `docs/champion/EVIDENCE_LOG.md` — concrete logs, screenshots and test references.
- `dist/candidate.json` — candidate identity and SHA-256 hashes.
- `THIRD_PARTY_NOTICES.md` — package licences and asset provenance.
- `docs/legacy/` — unchanged copies of the supplied v0.1 documentation, not current completion claims.

**Release status:** available for local review; **production release BLOCKED** pending native-build verification, real-browser persistence/PWA testing, human acceptance, current source review and an authorised deployment/recovery environment. No application was published, deployed or submitted to an app store.


</details>
