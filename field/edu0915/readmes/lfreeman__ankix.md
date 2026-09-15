# ankix

Anki card CLI for Claude Code. Capture what you learn while you learn it, review it on your phone.

Cards are written with [fastanki](https://github.com/AnswerDotAI/fastanki), which keeps its own
collection file and syncs through AnkiWeb — so the Anki desktop app never has to be running,
and no AnkiConnect add-on is needed.

## Install

```bash
uv sync
uv tool install --editable . --force
ankix auth login                    # one time; prompts, then stores only a sync key
ankix skill install --no-dry-run    # symlinks skills/anki into ~/.claude/skills/anki
```

`auth login` trades your AnkiWeb password for a sync key and discards the password. The key is
written to `~/.config/ankix/auth.json` at mode 0600.

## Use

Ask Claude Code to remember something and the `anki` skill calls `ankix` for you:

> make an anki card for this

Directly:

```bash
ankix card add --front "..." --back "..." --tag coraza   # preview; writes nothing
ankix card add --front "..." --back "..." --tag coraza --no-dry-run
ankix card add --from-file cards.json --no-dry-run       # a whole batch in one call
ankix card list --tag coraza --json
ankix sync
```

`--from-file` takes a JSON array of cards — `front`/`back` or `cloze`, plus optional `tags` and
`deck`. The batch is validated in full before anything is written, so one bad card writes none of
them, and no shell quoting sits between the card text and the collection.

One deck, topics separated by tag — Anki schedules per card, so extra decks only split the daily
review queue. `--deck` exists if you ever want one.

Every write is a preview by default — `--no-dry-run` is what commits it. `sync` is the only
command that talks to AnkiWeb; nothing else pushes to your phone.

`ankix --help` for the full surface, `ankix doctor` when something looks wrong.

## Where things live

Everything sits in one directory, relocatable with `ANKIX_CONFIG_DIR`:

| Path | What |
|---|---|
| `~/.config/ankix/collection.anki2` | the Anki collection ankix owns |
| `~/.config/ankix/auth.json` | the AnkiWeb sync key, mode 0600 |
| `~/.config/ankix/config.json` | default deck, collection path, sync endpoint |

The Anki desktop app's own collection is never touched; the two meet only through AnkiWeb.

## Develop

```bash
uv run pytest
uv run ruff check src/ tests/
uv run mypy
```
