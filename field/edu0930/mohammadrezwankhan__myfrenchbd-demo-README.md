# MyFrenchBD

[![CI](https://github.com/mohammadrezwankhan/myfrenchbd-demo/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/mohammadrezwankhan/myfrenchbd-demo/actions/workflows/ci.yml) · [MIT license](LICENSE) · [Verification and limits](QUALITY_REPORT.md)

Local-first French-learning demonstration for Bangla and English readers, with practice and device-local progress.

If MyFrenchBD helps you study this workflow, a star helps other Bangla/English learning-tool developers find it.

![Actual desktop demo](docs/repository/demo-desktop.png)

## Try the demo

[Open the hosted synthetic demo](https://mohammadrezwankhan.github.io/myfrenchbd-demo/) or run the identical standalone artifact locally:

Prerequisite: Node.js 22 or later; tested here with Node.js 24. This runs locally with synthetic examples. It does not connect to a live provider or publish user input.

```sh
git clone https://github.com/mohammadrezwankhan/myfrenchbd-demo.git
cd myfrenchbd-demo
node scripts/preview-demo.mjs
```

Open **http://127.0.0.1:4173**. Stop the server with Ctrl+C. The first screen is a demonstration, not verified current information. Keep private or real-world records out of this evaluation.

## Why inspect this project?

MyFrenchBD packages French practice for Bangla and English readers with device-local progress. Its build, storage and service-worker tests make offline learning behavior a practical engineering topic.

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

# MyFrenchBD — Champion Edition

**A local-first French-learning web app for Bangladeshi learners.**

Candidate **0.2.0-champion.1** · build **`champion-3f8a86d90bc6`** · 29 September 2026.

## Start learning

Open **`MyFrenchBD-Champion.html`** in your browser. It contains the complete app, styles, React runtime and icons: no account, API key or package installation is needed to open it. A browser may restrict storage for files; the app reports this and provides a copyable/exportable backup. This standalone file is not an installed PWA or a native Android/Windows application.

For a consistent local HTTP origin, with Node.js installed:

```sh
node scripts/serve.cjs
```

Open the localhost address printed by the server. It listens only on your device. Stop with Ctrl+C. The supplied Windows/macOS/Linux launch scripts run this same server. Moving between the standalone file, another port and a hosted app may create different browser storage locations; export/import progress to transfer it.

## What is included

Six original A1–B1 lessons, three text-first practice activities, a six-question **uncalibrated** orientation, actual learning evidence and review dates, a learning passport, four explicitly labelled demo discovery records, five source-linked France planning steps, local correction drafts, English/Bangla primary navigation, light/dark themes and accessible native dialogs. Search, level filters, saves, three-state checklist choices, backup preview/import and typed-confirmation reset are connected to real local behaviour.

There is **no** backend, login, microphone recording, AI assessment, live directory, report inbox, official credential, advanced B2–C2 curriculum, guardian-verification system or production telemetry. French and Bangla content still require qualified human review. Supporting operational copy is not fully translated.

## Rebuild and test without downloading dependencies

The included portable path uses the supplied React 19.2.8 runtime and a separately identified, bundled pure-JavaScript TypeScript 5.8.3 compiler. It is a scoped fallback, not a claim that the original Vite toolchain passed.

```sh
npm run typecheck:portable
npm run build:portable
npm run test:portable
```

**Do not run `npm install` first for this path.** The required runtime closure, type declarations, compiler and licences are in `vendor/`. The editable implementation remains React + TypeScript. New dependency families or additional unbundled Lucide icons require an ordinary dependency installation and an updated reviewed build graph.

Outputs: `dist/` for local/static hosting and `MyFrenchBD-Champion.html` for a self-contained file. A clean-copy offline rebuild was checked; see the evidence report.

The original Vite/Vitest path is retained for a normal development environment:

```sh
npm ci
npm run typecheck
npm test
npm run build
```

Its dependencies are pinned to versions already in the supplied lockfile; no broad upgrade was performed. The original archive included Windows-specific native build packages. In this Linux environment, Vite/Vitest commands were blocked and registry installation timed out. Docker and production hosting were **not** run or deployed.

## Verification, without overstating it

| Check | Result |
|---|---|
| Strict portable TypeScript | PASS — 12 application source files |
| Portable Node tests | PASS — 57; no failures or skips |
| Actual React browser scenarios | PASS — 32, with an explicit storage test double except the native-denial test |
| Responsive checks | PASS — 8 routes × 5 widths (320, 390, 768, 1024, 1440 px), no horizontal page overflow |
| Actual read-only HTTP server checks | PASS — 10 |
| Native browser URL navigation and installed service worker | BLOCKED by managed-browser policy |
| Real file/HTTP storage persistence and browser download delivery | NOT VERIFIED |
| Physical devices, screen readers, qualified language review, human UAT | NOT RUN |
| Production release | BLOCKED / NOT AUTHORISED; nothing deployed |

The browser tests render the actual bundled app inline; they are not screenshot mockups. They do **not** prove a hosted integration or real storage persistence. SW checks use a mocked Cache API and the worker source; served SW files were checked over real loopback HTTP, but installation/offline interception was not exercised in a browser.

Read [the audit and verification report](docs/champion/AUDIT_REPORT.md), [test matrix](docs/champion/TEST_MATRIX.md), [release preparation](docs/champion/RELEASE_PREPARATION.md) and [licence register](docs/champion/ASSETS_AND_LICENCES.md). Historical supplied documentation is explicitly marked and retained under `docs/original-reference/`.

## Your data

Progress is unencrypted browser-local data, not cloud sync or a secure account. Anyone with access to the same browser profile may be able to read it. Export regularly; browser clearing, private browsing and storage restrictions can remove it. No personal identity documents should be entered. A correction draft is **not submitted** to anyone.

The original v1 storage key is retained on migration. Invalid data is not silently overwritten; recovery copies and truthful session-only warnings are available. Known sequential other-tab changes pause autosave; this is not a guarantee of atomic multi-tab concurrency. See the recovery plan before release.


</details>
