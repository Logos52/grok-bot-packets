---
id: 2026-09-14-constkolesnyak-gigaku-de-ja-netflix-migaku-anki
kind: article
title: gigaku — DE/JA Netflix→Migaku→Anki; i+1 card clarity scoring
source: "https://github.com/constkolesnyak/gigaku-lang"
author: constkolesnyak
published: 2026-09-14
captured: 2026-09-14
via: grok-bot/Field
lane: learning
status: raw
private: false
---

# gigaku (constkolesnyak/gigaku-lang)

Source: https://github.com/constkolesnyak/gigaku-lang
Author: constkolesnyak
Published: created 2026-09-14 (day-0 public ship of a mature personal DE/JA immersion toolkit).

## Field summary (portable gates)
- **i-plus-one**: `gigaku clarity` rates i+1 Anki cards by how obvious the unknown word is from the sentence; add-on studies the clearest card per word.
- **generated-input / immersion pipeline**: Netflix subtitle rip via Language Reactor (background tab, never plays video) → Migaku; known-word cache from Language Reactor + Migaku IndexedDB + AnkiMorphs.
- **prefer DE/JA**: German ASR spell-check + RU gloss; Japanese/German study pipeline; companion games-lang catalogues Steam games by language intensity for DE/JA.
- **quiet-when-nothing / teach-once**: one LLM transport (`claude -p`); contracts are plain lines with echoed ids; answers written after every request so rate limits cost one request.
- Named runner with portable mechanism: sentence clarity scoring for i+1 cards — not just another miner.

## README (excerpt)
<h1 align="center">gigaku</h1>
<p align="center"><b>Netflix, YouTube and Anki wired into one German and Japanese study pipeline</b></p>
<p align="center">
  <img alt="Python 3.14+" src="https://img.shields.io/badge/python-3.14%2B-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="macOS" src="https://img.shields.io/badge/platform-macOS-000000?style=flat-square&logo=apple&logoColor=white">
  <img alt="MIT" src="https://img.shields.io/badge/license-MIT-2ea44f?style=flat-square">
</p>

<p align="center"><img src="media/plots.png" width="900" alt="The vocabulary history page: known and learning words per language over time"></p>

gigaku is a language-learning toolkit for macOS: a Python CLI, a Chrome extension, an Anki
add-on and a few launchd agents. It tracks the words you know across Language Reactor, Migaku
and Anki, rips Netflix subtitles into Migaku without playing the video, and picks flashcard
sentences by how well they teach the word.

## What it does

- **Vocabulary history.** Imports known words from Language Reactor, Migaku and AnkiMorphs into one per-day cache, drawn as a self-contained HTML page.
- **Netflix subtitle ripping.** Exports a whole season through Language Reactor in a background tab, never playing the video, as aligned SRT pairs.
- **Proofread and glossed.** The ASR German is spell-checked and glossed into Russian line by line through the `claude` CLI, with ids echoed so nothing shifts.
- **Netflix catalogue.** Rips a browse gallery through Netflix's own client, joins IMDb's datasets and ranks the titles you have not watched.
- **Anki decks that teach.** Scores every i+1 card by how much its sentence reveals the unknown word; builds German decks from frequency lists or YouTube.
- **Mouse-wheel remote.** A signed launchd stub turns the wheel into Apple TV volume, the TV's own remote as fallback, and the buttons into Netflix keys.
- **Nightly backup and report.** Snapshots every word source into a git repo, publishes the page, and posts a weekly chart card to Telegram.

## Quick start

```bash
uv sync && uv run gigaku --help         # or: uv tool install --editable . --force
gigaku import && gigaku plots           # Language Reactor export in ~/Downloads first
gigaku subs                             # one Netflix tab open in Chrome
gigaku titles                           # a Netflix gallery, ranked by IMDb rating
anki/link.sh                            # symlink the add-on into Anki, then restart it
uv run python scripts/pair_appletv.py   # pair the Apple TV once, then: gigaku sound
```

Requirements: macOS, Python 3.14+, [uv](https://docs.astral.sh/uv/), and Chrome with
*View ▸ Developer ▸ Allow JavaScript from Apple Events* enabled. Per feature: Language
Reactor Pro, Migaku, Anki with AnkiConnect, the `claude` CLI on `PATH`, an Apple TV.

## How it works

```mermaid
flowchart TD
  subgraph in [Sources]
    LR[Language Reactor<br/>Migaku · AnkiMorphs]
    NF[Netflix tab<br/>in Chrome]
    YT[YouTube<br/>captions + audio]
  end
  CLI[gigaku CLI]
  LR --> CLI
  NF --> CLI
  YT --> CLI
  CLI --> CACHE[(words.json)]
  CLI --> SUBS[(subtitle library)]
  PAGE[HTML page<br/>Telegram card]
  EXT[Chrome extension<br/>→ Migaku]
  ANKI[Anki decks<br/>+ add-on]
  CACHE --> PAGE
  SUBS --> EXT
  CLI --> ANKI
```

Every source is read where it already lives: Language Reactor's export, Migaku's word list
straight out of Chrome's IndexedDB, AnkiMorphs' known morphs from the Anki collection. One
JSON cache holds the only per-day history; every page, report and backup derives from it.

Chrome is driven over AppleScript on a tab found by URL, so a rip runs in the background
while you keep working. Everything that needs a language model goes through one transport,
`lib/claude.py`; every Anki write goes through AnkiConnect.

<details><summary><b>Driving Chrome without stealing focus</b></summary>

- `subs` drives Language Reactor's own in-page controller and `titles` calls Netflix's own
  falcor client, so a Netflix build bump costs a probe (`gigaku titles --probe`), not a rewrite.
- Page visibility is spoofed in the page's main world, so Netflix keeps switching tracks and
  generating ASR in a hidden tab; the video is never played, not even for ASR.
- A main-world hop (`lib/platform/chrome.py`) reaches the page globals an isolated script
  cannot; JavaScript dialogs are captured rather than shown, because a dialog freezes every
  further call on that tab.
- Waits are adaptive: a stall reloads and retries, a rate limit is waited out, an episode that
  keeps failing is skipped, and a re-run resumes at the first episode without a `Primary.srt`.
- The exported text is checked by script, not by label: a track that silently reverted to
  Japanese is refused before anything is written.

</details>

<details><summary><b>One LLM transport</b></summary>

- `lib/claude.py` wraps `claude -p`: no API key, no SDK. Proofreading, glossing, clarity
  scoring and the deck builders share it, each with its own rubric.
- Every contract is plain lines matched on an echoed id, so a short reply becomes a named gap
  that is re-asked, and a cue can never receive another cue's text.
- Requests are hundreds of items with unasked neighbours as context; answers are written to
  disk after every request, so a rate limit costs one request, not a run.
- `spell` keeps a per-series ledger of character names, grouped once per show, so a name
  misheard five ways is settled the same way in every episode.
- `clarity` rates a word's cards against each other in one block, whole or not at all, and the
  add-on studies the clearest card per word.

</details>

<details><summary><b>The wheel daemon, TCC and the LAN</b></summary>

macOS binds the Accessibility grant to a signature and a path, so `launchd/GigakuSound.m` is
a 40-line stub that forks the Python daemon and stays its responsible process across
interpreter upgrades. Build, sign, grant, load (put your clone's path into the plist first):

```bash
mkdir -p launchd/GigakuSound.app/Contents/MacOS
clang -framework Foundation -x objective-c \
      -o launchd/GigakuSound.app/Contents/MacOS/GigakuSound launchd/GigakuSound.m
codesign --force --deep --sign - launchd/GigakuSound.app
# System Settings ▸ Privacy & Security ▸ Accessibility → add launchd/GigakuSound.app
cp launchd/com.gigaku.sound.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.gigaku.sound.plist
```

Rebuilding the stub drops the grant: re-sign, `tccutil reset Accessibility com.gigaku.sound`,
and re-add the app.

When the Apple TV cannot be reached, the same step goes to the Samsung TV's own remote — the
same speaker over HDMI-CEC. Devices are found by hardware MAC, never by a written-down IP;
`scripts/lan_bypass.README.md` covers an access point that isolates its clients.

</details>

## Commands

| Command | What it does |
|---|---|
| `gigaku import` | Language Reactor, Migaku, AnkiMorphs → word cache |
| `gigaku plots` / `gigaku publish` | the history as
