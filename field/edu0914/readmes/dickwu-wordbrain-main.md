# WordBrain

Local-first English vocabulary builder. Read imported material, choose the meaning you want to
learn, and practice it in short daily sessions. Words remain **known / learning / unknown** by
your explicit choice; reading exposure and practice counts are shown as evidence, not mastery.

Built with **Tauri v2**, **Next.js 16**, **React 19**, **Tiptap 3**, **Turso SQLite**, and
**ts-fsrs**. Vocabulary and practice history stay on your machine. Dictionary lookups use your
configured server. Optional AI activities run the local Claude CLI, with Codex CLI as fallback.

## Install

### Homebrew (macOS)

```bash
brew install dickwu/tap/wordbrain
```

The cask lives in [`dickwu/homebrew-tap`](https://github.com/dickwu/homebrew-tap). It installs the
latest universal `.dmg` into `/Applications/WordBrain.app`, and updates land automatically every
time you run `brew upgrade wordbrain`.

> **First launch on macOS** — the build is not Apple-notarized yet, so Gatekeeper quarantines the
> bundle. After install (or upgrade), clear the quarantine attribute once:
>
> ```bash
> sudo xattr -d com.apple.quarantine /Applications/WordBrain.app/
> ```
>
> Then open WordBrain normally. Notarization will be wired up in a future release.

### Direct download

Pick your platform from the
[Releases page](https://github.com/dickwu/wordbrain/releases/latest):

- **macOS**: `.dmg` (universal — Apple Silicon + Intel)
- **Windows**: `.msi` installer (x86_64)
- **Linux**: `.deb` package or portable `.AppImage` (x86_64)

macOS releases include signed updater artifacts and `latest.json` for in-app updates. Windows
and Linux releases provide standalone installers.

### Build from source

Requirements: [Bun](https://bun.sh), [Rust](https://rustup.rs) (stable toolchain), macOS 12+ /
Windows 10+ / Ubuntu 22.04+.

```bash
git clone https://github.com/dickwu/wordbrain
cd wordbrain
bun install
bun run tauri dev
```

See [Development](#development) for the full loop.

## Features

- **Reading and capture** — known, learning, and unknown words have distinct highlighting.
  Dictionary lookup lets you save a focus meaning and accepted answers for offline review.
- **Daily practice** — choose a 5, 10, or 15 minute budget. Due cards, older weak words, and a
  shared daily allowance for new cards feed a resumable plan. Form recall is optional.
- **FSRS reviews** — meaning and form directions keep independent schedules. Rating previews
  come from the same scheduler used for submission. Skips and assisted answers do not count as
  independent recall successes.
- **Story and writing practice** — try story blanks before requesting choices. Writing drafts
  and submitted originals are retained when AI feedback fails, so you can retry later.
- **Words and evidence** — filter all three vocabulary states, edit notes, and inspect review
  history, source material, and practice evidence for each word.
- **Material library** — import EPUB chapters, subtitles, Markdown, or plain text. Partial EPUB
  failures identify the chapters that were saved. Reading recommendations use the proportion
  of unknown words; the word network shows co-occurrence in saved material.
- **Private Dictionary API** — server settings stay local; its API key is kept in the
  macOS Keychain or encrypted Stronghold vault and used by Rust, never passed to the renderer.
- **macOS auto-updates** — optional background checks and manual checks are available in the app.

## Data storage

Version 0.4 uses `wordbrain-v2.db` in the application data directory, with dictionary API keys
kept separately in the macOS Keychain or encrypted Stronghold vault:

- macOS: `~/Library/Application Support/com.lifefarmer.wordbrain/wordbrain-v2.db`
- Windows: `%APPDATA%\com.lifefarmer.wordbrain\wordbrain-v2.db`
- Linux: `~/.local/share/com.lifefarmer.wordbrain/wordbrain-v2.db`

On upgrade, WordBrain migrates the existing `wordbrain.db` through a staging database and retains
the original file. Previously reviewed cards need a fresh review to establish their missing
scheduler state; their old due dates and history remain available. Do not replace the new database
with the old file after practicing in the upgraded app: the files can contain different histories.
Close WordBrain before copying the data directory for a backup.

If an externally modified legacy database uses rollback-journal mode, the upgrade stops without
changing it. Open and close it with the previous WordBrain release, then retry the upgrade.

See [the memory redesign](docs/wordbrain-memory-redesign.md) and
[acceptance specification](docs/wordbrain-memory-test-spec.md) for the data and review contracts.

## Tech stack

| Layer         | Choice                                                               |
| ------------- | -------------------------------------------------------------------- |
| Desktop shell | Tauri v2 (Rust)                                                      |
| Frontend      | Next.js 16 (static export), React 19, Ant Design 6, Tailwind CSS 4   |
| Editor        | Tiptap 3 + a custom ProseMirror decoration extension                 |
| State         | Zustand (sync) + TanStack React Query (async IPC)                    |
| Database      | Turso SQLite (Rust-native, embedded)                                 |
| Tokenizer     | `wink-lemmatizer` (runs in the renderer, no IPC round-trip)          |
| Dictionary    | Private Dictionary API                                               |
| Spaced rep    | `ts-fsrs`                                                            |
| Graph         | cytoscape + `react-cytoscapejs` + `cytoscape-fcose`                  |
| Secrets       | macOS Keychain / `tauri-plugin-stronghold`                           |
| Auto-update   | `tauri-plugin-updater` (signed update archives from GitHub Releases) |

## Development

```bash
bun install              # install JS deps (Bun only — no npm/yarn)
bun run dev              # Next.js dev server on :3000
bun run tauri dev        # full Tauri desktop session
bun run tauri build      # production build (dmg/msi/AppImage)
bun run format           # prettier write
bun run test             # vitest unit + component tests
```

Rust backend (`cd src-tauri`):

```bash
cargo check              # fast type check
cargo build              # full build
cargo test               # backend unit + integration tests
```

Conventions enforced in [`CLAUDE.md`](CLAUDE.md) / [`AGENTS.md`](AGENTS.md):

- All SQLite writes go through Rust `#[tauri::command]` handlers; the frontend never opens the DB
  directly.
- `App.useApp()` for AntD `message` / `modal` / `notification` — never the module-level static
  exports.
- Components `PascalCase`, stores + hooks `camelCase`.

## Releasing

```bash
scripts/publish.sh <next-version> --ci    # bump version, tag, push; GitHub Actions builds + releases
```

The `--ci` path is the normal one — it bumps `package.json`, `src-tauri/tauri.conf.json`, and
`src-tauri/Cargo.toml`, commits, tags, and pushes. GitHub Actions
([`release.yml`](.github/workflows/release.yml)) then builds release bundles for all three
platforms, signs updater archives, generates `latest.json` for the macOS updater, and creates a GitHub release. A second workflow
([`homebrew.yml`](.github/workflows/homebrew.yml)) downloads the macOS DMG, computes its SHA-256,
and writes an updated cask to the [`dickwu/homebrew-tap`](https://github.com/dickwu/homebrew-tap)
tap repo so `brew upgrade wordbrain` lands the new version.

See [`CHANGELOG.md`](CHANGELOG.md) for version history.

One-time prerequisites (maintainers only):

- `TAURI_SIGNING_PRIVATE_KEY` + `TAURI_SIGNING_PRIVATE_KEY_PASSWORD` secrets for updater signing.
- `HOMEBREW_TAP_TOKEN` fine-grained PAT with `Contents: read/write` on the tap repo.
- Optional: Apple notarization secrets (`APPLE_CERTIFICATE`, `APPLE_ID`, `APPLE_TEAM_ID`,
  `APPLE_PASSWORD`) to drop the Gatekeeper warning on macOS.

## License

MIT © Peilin Wu
