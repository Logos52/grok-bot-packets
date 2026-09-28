# kids-study-app

**A study app for kids: practice tests at the right level, stories read aloud, and flashcards.**

*In plain words:* I built this for my own two children, who are in different grades at school. Each child signs in with their own code and gets practice tests written for their level. Stories are read aloud with each word lighting up as it is spoken, so they can follow along on their own. Mistakes come back later as flashcards, and a parent screen shows how everyone is doing.

A desktop study app for kids, built with Electron and TypeScript. Each child signs in with a PIN, gets practice tests written for their own grade, has stories read aloud with every word lighting up as it is spoken, and reviews their mistakes as spaced-repetition flashcards. A parent dashboard shows how everyone is doing.

![Parent dashboard](docs/screenshots/08-parent-dashboard.png)

## Why I built it

I have two kids in different grades, and I wanted two things for them. First, practice at the right level: worksheets online were either too easy for my older one or full of words my younger one could not read yet. Second, books read aloud, with the words highlighted so they could follow along on their own while I was still working.

So I built an app for our family computer. It started as a pile of scripts and grew into something the kids open on their own. This repository is a clean rebuild of that app for sharing. Every name, grade and progress number in it is invented (the demo family is Maya, Leo and a parent), and the stories are my own retellings of public domain fables.

## What it does

- **Profiles with PINs.** Each child has a profile; the parent has their own. PINs are hashed with scrypt and wrong guesses trigger an escalating lockout.
- **Practice tests at the right level.** Pick a subject and topic from a grouped list. The test is generated as JSON, validated against a schema, and then checked against a calibration table for the child's grade: which Bloom levels (remember, understand, apply, analyze, evaluate, create), which question types, how many options, how long a prompt can be. A test that fails either check is sent back to the provider with the list of problems.
- **A provider adapter, with a mock by default.** The app talks to "an LLM" through a small interface. The built-in mock is offline and deterministic and needs no key. Point it at any OpenAI-compatible endpoint with environment variables when you want real generation.
- **Read-aloud with karaoke highlighting.** The reader uses the system voice when there is one and follows its word boundary events. When the voice does not report boundaries, or there is no voice at all, it follows a timeline computed from syllables and punctuation, so highlighting works fully offline.
- **Flashcards with FSRS-5.** Every question a child gets wrong becomes a card. Reviews are scheduled with the FSRS-5 model, with a gentler target retention for younger grades.
- **XP, levels, streaks and badges.** Small rewards that my kids actually cared about.
- **Parent dashboard.** Per child: XP, streak, accuracy and minutes over 14 days, XP per day, average score per subject, cards due, books read and recent tests. The parent can add a student and change any PIN.
- **Progress sync that never loses progress.** Two computers can be used offline and synced later in any order. The merge only moves forward, and a local mock sync server is included.
- **Auto-update from GitHub releases** for installed builds, off in development.

## Run it

Needs Node.js 22 or newer.

```bash
npm install
npm start
```

`npm start` builds the app and opens it in mock mode. The first run creates the demo family, and the sign-in screen shows the PINs: **Maya 1111, Leo 2222, Parent 2468**. The first `npm start` also downloads the Electron binary.

## Screenshots

| | |
|---|---|
| ![Sign in](docs/screenshots/01-sign-in.png) | ![Student home](docs/screenshots/03-student-home.png) |
| ![Practice test](docs/screenshots/04-practice-test.png) | ![Test result](docs/screenshots/05-test-result.png) |
| ![Flashcards](docs/screenshots/06-flashcards.png) | ![Read aloud](docs/screenshots/07-reader.png) |

The screenshots are produced by the app itself: `npm run screenshots` runs a scripted walkthrough in a hidden data directory (under `xvfb-run` on a headless Linux machine) and saves one image per screen.

## Architecture

```
renderer (sandboxed page, plain TypeScript + DOM, strict CSP)
   |  window.study.invoke(channel, ...args)      typed by src/shared/ipc-contract.ts
preload (contextBridge, channel allowlist)
   |  ipcRenderer.invoke
main process
   ipc.ts        checks the sender frame, validates arguments with zod
   service.ts    every channel as a method; authorization lives here
     |-- llm/          provider interface, mock, OpenAI-compatible, repair loop
     |-- shared/       schema, calibration, FSRS-5, progress, merge, timings
     |-- store.ts      AES-256-GCM file, atomic writes, backup
     |-- sync-client   HTTP client for the sync server
     `-- updater.ts    electron-updater against GitHub releases
server/mock-sync-server.ts   local HTTP server that merges with the same rules
```

A few decisions worth explaining:

- **Nothing in `service.ts` imports Electron.** The whole flow (sign in, generate a test, grade it, review cards, sync) runs in plain Node, which is how the tests exercise it end to end without a window.
- **The page never sees an answer key.** Tests are stored in the main process; the renderer receives prompts and options only, and grading happens on submit.
- **Every provider goes through the same gate.** The mock answers like a chatty model would (prose around a fenced JSON block), so JSON extraction, schema validation, calibration and the repair loop run on every mock generation too. The extractor keeps the last complete JSON object, because models asked for "JSON only" sometimes send a draft and then a corrected version.
- **The merge is a join.** Counters take the maximum, daily stats merge per day and per field, cards keep the most reviewed state, results and badges are unioned with a fixed tie order. That makes the merge commutative, associative and idempotent, so sync order does not matter and syncing twice changes nothing. XP from different days on different computers adds up; two sessions on the same day on two computers count as the larger one. Without per-device counters that is the honest limit, and it never invents progress.

## Security

The threat model is a family computer: stop one child from opening a sibling's profile or the parent area, stop casual PIN guessing, and keep the data unreadable if the data folder is copied somewhere. It does not try to resist someone with full control of the machine.

- **Electron hardening.** `contextIsolation: true`, `nodeIntegration: false`, `sandbox: true` and `app.enableSandbox()`. A Content Security Policy with `default-src 'none'` and scripts only from the app itself. New windows are denied, navigation away from the app page is blocked, and every permission request (camera, microphone, notifications) is refused.
- **Typed, validated IPC.** The preload exposes a single `invoke` restricted to an allowlist of channels. The main process accepts calls only from the app's own frame and validates every argument tuple with zod before it reaches the service.
- **Authorization in the main process.** A student session can only read and write its own data; parent channels check the role on every call. The UI hides buttons for convenience, never for control.
- **PINs.** scrypt (N=16384, r=8, p=1) with a per-profile salt and a constant-time comparison. After five wrong PINs the profile locks for 30 seconds, then 1, 5 and 15 minutes. A four digit PIN is only 10,000 values, so the lockout is what really protects it; the hash keeps PINs out of plain sight.
- **Encrypted store.** All state is one JSON document sealed with AES-256-GCM (random IV per write, the format tag as associated data). The key is wrapped by the OS keychain through Electron's `safeStorage` when available, or kept in a key file for the portable Windows build so the data can travel on a USB stick. Writes are atomic (temp file, rename) with a backup of the last good file, and a file that fails authentication is never silently replaced by an empty store.
- **Secrets stay in the main process.** The LLM key is read from the environment and never crosses the bridge; provider errors report the HTTP status only, never the response body.
- **Sync.** Bearer token compared in constant time, request bodies capped at 1 MB and validated with the same schema the app uses. Plain HTTP is allowed to localhost only.

## Tests

```bash
npm run typecheck   # tsc for main/preload/server and for the renderer
npm test            # vitest
npm run smoke       # launches the real app headless and walks through it
```

The vitest suite covers:

- **FSRS-5:** interval ordering by rating, stability growth, lapses, difficulty bounds, retention by grade.
- **Merge:** the three lattice laws on 300 random pairs and triples, "no field ever goes down", offline work on two computers.
- **Schema and calibration:** invalid answer indexes, duplicate options and ids, missing blanks, grade mismatches, chatty model output, and the mock provider passing schema and calibration for every grade, topic and several seeds.
- **PIN and crypto:** hash and verify, salting, stored parameters, lockout steps, AES-GCM tamper detection, no plaintext on disk, backup recovery.
- **Service flows:** authorization boundaries, lockout and reset, generate and grade without leaking answers, the repair loop, flashcard scheduling, the OpenAI-compatible adapter against a fake server, and two computers converging through the real sync server.

`npm run smoke` starts Electron with a throwaway data directory, signs in with a PIN, generates and submits a test, reviews a card, checks that the read-aloud highlight is moving, opens the parent dashboard and confirms that a parent-only channel refuses a signed-out caller. It exits non-zero if any step fails.

## Configuration

| Variable | Default | Purpose |
|---|---|---|
| `SC_LLM_PROVIDER` | `mock` | `mock` or `openai` (any OpenAI-compatible chat completions endpoint) |
| `SC_LLM_BASE_URL` | `https://api.openai.com/v1` | Endpoint for `openai`, for example a local runtime at `http://127.0.0.1:8080/v1` |
| `SC_LLM_MODEL` | none | Model name, required for `openai` |
| `SC_LLM_API_KEY` | none | Sent as a bearer token when set |
| `SC_DATA_DIR` | app data folder | Where the encrypted store lives |
| `SC_SYNC_URL` | none | Sync server, for example `http://127.0.0.1:4817` |
| `SC_SYNC_TOKEN` | `local-demo-token` | Bearer token for the sync server |
| `SC_DISABLE_UPDATES` | none | `1` turns the updater off in a packaged build |

To try sync, run the server in one terminal and the app in another:

```bash
npm run sync-server
SC_SYNC_URL=http://127.0.0.1:4817 npm start
```

Then use **Sync now** in the parent dashboard.

## Packaging

On Windows, the same way the original family app was shipped:

- `scripts/windows/Package portable.bat` runs `package-portable.ps1`: checks Node, runs the type check and tests, builds the installer and the portable executable with electron-builder, and assembles a `KidsStudyApp` folder on the Desktop with the .exe and a short READ ME. The portable build keeps its encrypted data in `KidsStudyAppData` next to the .exe.
- `scripts/windows/Publish update.bat` runs `publish-release.ps1`: refuses to publish with uncommitted changes, builds, and creates (or updates) the GitHub release for the version in `package.json` with the installer, its blockmap, `latest.yml` and the portable .exe. Installed copies see it on their next start and offer to restart and update. The GitHub owner and repository are not hard-coded: electron-builder reads them from the `origin` remote of your clone, so a fork publishes to itself.

On Linux and macOS: `npm run dist:linux` (AppImage) and `npm run dist:mac` (dmg). `npm run dist:win` also works from any system with the right tooling.

## Project layout

```
src/main        Electron main process: window, IPC, service, store, updater, sync client
src/preload     the context bridge
src/renderer    the page: views, DOM helpers, styles
src/shared      pure logic shared by both sides: schema, calibration, FSRS, merge, timings
src/llm         provider interface, mock, OpenAI-compatible adapter, generation loop
src/content     stories and question banks (retellings of public domain tales)
src/server      the mock sync server
tests           vitest suites
scripts         build, launch, Windows packaging
```

## License

MIT, see [LICENSE](LICENSE).
