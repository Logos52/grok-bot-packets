# jlpt-bot

Discord bot for JLPT quiz practice (N5–N1, fastest-finger scoring).

Built on **discord.py 2.7.1** exactly as documented in `docs/discord-py/`
(`api.md`, `ext-commands-api.md`, `ext-tasks-index.md`, `interactions-api.md`).

## Features

- `/jq start` opens a setup embed: level (N5–N1/ALL), question category
  (Vocabulary / Grammar / Reading, bilingual labels), count (5/10/15/20).
- Questions are random every session (`random.sample`).
- Anti pattern-recognition: options are shuffled per session and the
  correct index is remapped. The original order is never sent to Discord.
- Fastest finger wins: first correct answer gets +1 and auto-advances.
  Wrong answers are ignored (ephemeral only).
- One active session per process, single server + single channel enforced.
- Buttons `1/2/3/4` + `Stop` (starter or server admin with
  `Administrator`/`Manage Guild`). Idle 5 minutes auto-closes.
- Session-only leaderboard embed when the quiz ends.
- Full logs to `log.txt` plus console.

## Quick start

Requirements: Python 3.14, `uv`.

```bash
cp .env.example .env
# edit .env with your token and IDs
uv sync
uv run pytest
uv run jlpt-bot
```

Or use the launcher (used by systemd on the VPS):

```bash
./start.sh
```

## Configuration (.env)

| Key | Required | Example |
| --- | --- | --- |
| `DISCORD_TOKEN` | yes | bot token (never commit) |
| `JLPT_GUILD_ID` | yes | your guild id (never commit real id) |
| `JLPT_CHANNEL_ID` | yes | your channel id (never commit real id) |
| `JLPT_DATA_DIR` | no | `data` |
| `JLPT_LOG_PATH` | no | `log.txt` |
| `JLPT_IDLE_TIMEOUT_SEC` | no | `300` |

## Architecture

Modular monolith with one-way dependencies (blast radius isolation):

```
quiz_cog.py / views.py / embeds.py / bot.py   (discord layer)
  -> quiz.py                                   (session state machine, pure)
    -> store.py / models.py                    (data, pure)
      -> config.py
```

- `config.py`, `store.py`, `quiz.py`, `categories.py` never import `discord`:
  testable without a connection.
- `embeds.py` owns every `discord.Embed`.
- `views.py` owns every `discord.ui.View/Select/Button`.
- `quiz_cog.py` owns `/jq start` and the `tasks.loop` idle watcher.
- `QuizManager` enforces a single active session with `asyncio.Lock`.

Pipeline: `start.sh` → `uv run jlpt-bot` → load settings + JSON →
`/jq start` (guard) → setup view → sample + shuffle → per-question
embed + fresh `QuizView` → first correct +1 auto-next → leaderboard →
cleanup. Idle watcher (`tasks.loop(30s)`) closes sessions idle over
`JLPT_IDLE_TIMEOUT_SEC`.

## Data format

See `data/template.md`. Each JSON item:

`id, instruction, passage|null, stem, target|null, options[4], answer(1-4), correctOrder|null`

`passage` is shared reading text (or null). `target` is the underlined
word asked about. `correctOrder` is for star-ordering questions.

## Tests

```bash
uv run pytest -v
```

- `test_store`: loading, mondai grouping, sampling bounds.
- `test_shuffle`: shuffled answer stays correct, positions vary.
- `test_quiz`: first-correct-wins, wrong ignored, stale ignored,
  single-session enforcement, stop permission.
- `test_guards`: server/channel guard + settings validation.
- `test_embeds`: embed size limits.

## Deploy (VPS + systemd)

VPS layout mirrors other bots (`ruri`, `hinari`, `ayumi`, `phix`):

- Code: `/root/jlpt-bot`
- Env: `/root/jlpt-bot/.env` (token lives only here)
- Service: `/etc/systemd/system/jlpt-bot.service` (from `systemd/jlpt-bot.service`)

```bash
sudo cp systemd/jlpt-bot.service /etc/systemd/system/jlpt-bot.service
sudo systemctl daemon-reload
sudo systemctl enable --now jlpt-bot
journalctl -u jlpt-bot -f
tail -f /root/jlpt-bot/log.txt
```

GitHub Actions (`.github/workflows/`): `ci.yml` runs pytest;
`deploy.yml` pulls `/root/jlpt-bot` and restarts only the
`jlpt-bot` service via SSH key secrets. The Discord token is never
stored in git or in workflow files.

## License

MIT.
