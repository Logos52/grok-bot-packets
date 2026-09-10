---
id: 2026-09-10-neverether-kikubridge-premade-ja-anki-decks-kiku
kind: article
title: kikubridge — premade JA Anki decks → Kiku notes; idempotent merge; headless AnkiConnect
source: "https://github.com/neverether/kikubridge"
author: neverether
published: 2026-09-09
captured: 2026-09-10
via: grok-bot/Field
lane: learning
status: raw
private: false
---

# kikubridge

> **AI:** Developed almost entirely by LLMs for my personal use. Very new to the Anki ecosystem,
> so flying blind. No support or warranties.

kikubridge converts premade Japanese Anki decks into notes for the
[Kiku](https://github.com/youyoumu/kiku) note type and keeps an Anki collection in sync with
them through AnkiConnect.

You give it deck files such as Kaishi 1.5k or Ankidrone Essentials. It reads them, turns every
word into one Kiku note, merges words that appear in more than one deck into a single note with
several example sentences, and writes the result into a running Anki. Run it again after a deck
or the tool changes and only what changed is touched. Review history is never affected.

It is built for an Anki that runs headless in Docker, reached only over AnkiConnect, with a
self-hosted sync server feeding your phones. It also works against any Anki with the AnkiConnect
add-on installed.

## Why

- One note type for everything, so every card looks and behaves the same across decks and devices.
- Provenance kept as tags on each note, so you always know which deck a word came from and the
  bookkeeping can be rebuilt from the collection alone.
- Safe to rerun: importing is idempotent, nothing is deleted, cards are never moved between decks,
  and manual edits in the fields reserved for you survive. Imported cards land in one deck; arrange
  them into whatever decks you like.
- New decks are a single converter file away.

## Quick start

Requirements: [bun](https://bun.sh) 1.4 or newer and an Anki with the AnkiConnect add-on
reachable at `http://127.0.0.1:8765` (see [Running Anki headless](docs/headless-anki.md)).

```sh
bun install
# put your deck files (.apkg) in decks/
bun run kb setup      # downloads Kiku, installs it, deploys the plugin, writes manifest.toml
bun run kb plan       # what import would do
bun run kb import     # do it, then sync
```

`setup` writes a `[[sources]]` entry for every file in `decks/`. When it recognises the deck it
fills in the converter; when it does not, it leaves `converter = ""` and says so. Open
`manifest.toml`, set the converter (or [write one](docs/converters.md)), and run `setup` again.
Everything else in the manifest is optional. Note counts are learned from the first import.

Deck files are not part of this repository and must never be committed. `decks/`, `kiku/`,
`data/` and `out/` are ignored by git.

## What kikubridge puts in your collection

- **The Kiku note type**, installed from Kiku's own release package, unmodified.
- **One deck** (`日本語::Vocab` by default) where new notes land. Cards are never moved afterwards.
- **Notes, media and tags** for every word in your deck files.
- **A Kiku plugin.** Kiku loads a file named `_kiku_plugin.js` (and `_kiku_plugin.css`) from the
  collection's media folder if one exists. kikubridge installs its own, modified Kiku plugin: a small footer that shows
  which deck each word came from, read from the tags. Kiku's release ships a sample plugin under
  the same filenames, and `setup`, `upgrade-kiku` and `deploy-plugin` replace whatever is in
  those two slots. If you already use a Kiku plugin of your own, kikubridge will overwrite it;
  see [The footer plugin](docs/plugin.md) for what it does and how it is built.

## Read next

- [Guide](docs/guide.md): the ideas (Kiku, converters, the manifest, state, tags, merging,
  drift) and the workflows (first time, adding a deck, new deck or Kiku versions, lost state,
  editing notes by hand).
- [Command reference](docs/cli.md): every verb, flag, exit code and report row.
- [Adding a converter](docs/converters.md): how to support another deck.
- [Source decks](docs/sources.md): what Kaishi and Ankidrone contain and how they map.
- [Running Anki headless](docs/headless-anki.md): the Docker setup and sync.
- [The footer plugin](docs/plugin.md): what the card shows about a note's sources.
- [AGENTS.md](AGENTS.md): conventions for anyone, human or agent, changing the code.

## Versions this was developed against

| Component | Version | Where it is pinned |
|---|---|---|
| Kiku note type | v2.1.0 | `manifest.toml` (`kiku.version`); `setup` downloads it |
| Kiku plugin types | upstream commit `2a7b295` (2026-09-07) | `plugin/vendor/kiku-plugin-types.ts` |
| Kaishi 1.5k | v2.4.2 | `manifest.toml` (informational) |
| Ankidrone Essentials | V9 | `manifest.toml` (informational) |
| Anki | 26.8.1, headless in Docker | your compose `.env` |
| AnkiConnect | add-on 2055492159, API version 6 | image build |
| bun | 1.4.2 (1.4 or newer required) | `package.json` engines |
| zod / fflate / biome / TypeScript | 4.5 / 0.8 / 2.5 / 7.0 | `package.json` |

Reviewed on AnkiDroid. AnkiMobile has not been checked. A newer deck release is detected as
drift and refused until you accept it; a newer Kiku release is a deliberate `upgrade-kiku`.

## Third-party material

- `plugin/vendor/kiku-plugin-types.ts` is copied from [Kiku](https://github.com/youyoumu/kiku)
  (MIT, youyoumu) at the commit recorded in its header.
- `headless/compose.example.yaml` is adapted from the compose file in
  [ankimcp/headless-anki](https://github.com/ankimcp/headless-anki) (AGPL-3.0). It is
  configuration only; that project's code is built into your own image, not included here.
- Kiku itself is downloaded from its release page at setup time. Deck files are yours and are
  never part of this repository.
