# Flashcards

[![CI](https://github.com/emeryray2002/flashcard-go-go/actions/workflows/ci.yml/badge.svg)](https://github.com/emeryray2002/flashcard-go-go/actions/workflows/ci.yml)

A spaced-repetition flashcard app that runs entirely on your own Mac. One Go binary, one JSON file,
no account, no cloud, no network access. It starts when you log in and sits in the background using
a few megabytes of RAM, waiting at `http://localhost:17632`.

Cards are scheduled with **FSRS-6**, the same algorithm Anki has shipped since 23.10 — and because
you *type* your answers rather than rating yourself, three of the four grades come from evidence
instead of self-assessment.

```bash
brew install go
git clone https://github.com/emeryray2002/flashcard-go-go.git
cd flashcard-go-go
./scripts/install.sh
```

That's the whole install. It builds the binary, registers a launchd agent so the server comes back
after every reboot, waits until the server actually answers, and opens the app in your browser.

---

## Why this exists

Most flashcard apps ask you to grade yourself: you look at the answer, decide you "sort of knew it,"
and press a button. That self-report is the weakest link in the whole loop — it is exactly the
judgment that hindsight bias ruins.

Here you type the answer. An exact match is **Good**. If you needed a hint, or typed a wrong
character and corrected it, it is **Hard** — the grade reflects what actually happened during
retrieval, not how the text box looked at the end. Only "I got this wrong" and "I knew it instantly"
are yours to declare.

The other reason is ownership. There is no server to pay for, no account to lose, no API to be
deprecated. Your cards are a JSON file in your home directory and your entire review history is an
append-only log next to it. If this project disappears tomorrow, you still have everything.

## What you get

**Studying**
- FSRS-6 scheduling with real due dates, computed server-side and unit-tested against the reference
  implementation's own golden vectors.
- Typed answers with optional **Continuous Check** — live green/red feedback as you type.
- **Hints** that reveal the answer one character at a time (and honestly downgrade the grade).
- Daily limits (20 new, 200 reviews by default) so a session *ends*. When the queue empties, you are
  done for the day.
- Learning steps (1 min, 10 min) for new cards; a forgotten card drops to a 10-minute step with its
  stability damped rather than erased.
- **Bury** (hide until tomorrow, schedule untouched), **Postpone** (move the due date),
  **Suspend** (park it indefinitely) and **Forget** (reset to new).

**Content**
- Rich text via Quill, Markdown, or plain text, per card.
- Images, pasted or uploaded, stored locally.
- Import from JSON or CSV with a preview before anything is written — see
  [`docs/import-format.md`](docs/import-format.md).

**Knowing how you're doing**
- Per-topic predicted retention — what you would recall *right now* — plus due and new counts.
- A stats panel over your full review log: measured true retention, grade distribution, card states,
  calibration, reviews per day, the next seven days of workload, average seconds per card, leech
  count.

## Requirements

- macOS (the installer uses launchd). The server itself is portable Go — see
  [Running it elsewhere](#running-it-elsewhere).
- Go 1.22 or newer, only to build. `brew install go` and you're set. The finished binary embeds its
  own frontend and has no runtime dependencies whatsoever.

## Where your data lives

Everything is under `~/.flashcard/`:

| Path | What it is |
| --- | --- |
| `data.json` | Topics, cards and scheduling state. The whole app state. |
| `reviews.jsonl` | Append-only review log, one JSON line per answered card. |
| `images/` | Uploaded images. |
| `bin/flashcard-server` | The installed binary. |
| `logs/` | `stdout.log` and `stderr.log`. |

`data.json` is rewritten in full on every change, via a temp file and an atomic rename, so a crash
mid-write cannot corrupt it. To back up, copy the directory — that is genuinely all there is to it.

**`reviews.jsonl` is the part worth protecting.** The scheduler is replaceable; your review history
is not, and cannot be reconstructed after the fact. It is also what you would feed an FSRS parameter
optimizer later (see below).

## Everyday commands

```bash
./scripts/install.sh      # install, or rebuild + restart after a git pull
./scripts/uninstall.sh    # stop and remove the service (your data is kept)

launchctl print gui/$(id -u)/io.github.emeryray2002.flashcard        # status, PID, paths
launchctl kickstart -k gui/$(id -u)/io.github.emeryray2002.flashcard # force a restart
tail -f ~/.flashcard/logs/stderr.log                                 # what went wrong
```

To update: `git pull && ./scripts/install.sh`. The installer is idempotent, so that is the right way
to pick up any change.

To use a different port: `PORT=18000 ./scripts/install.sh`. The port is baked into the launchd job,
so it survives restarts.

## Tuning

`GET`/`PUT /api/config` exposes the scheduling knobs, and the app's Scheduling panel edits them:
desired retention (0.90 default), learning and relearning steps, maximum interval, interval fuzz,
new-cards-per-day and reviews-per-day caps, rollover hour (4am default, so a late-night session still
counts as the previous day), and leech threshold.

The 21 FSRS parameters live in `data.json` rather than in the binary, so they can be replaced without
a rebuild. Once you have accumulated a few thousand reviews you can fit them to your own memory
instead of the population average — [`scripts/export-reviews.sh`](scripts/export-reviews.sh) converts
your review log into the CSV that
[`fsrs-optimizer`](https://github.com/open-spaced-repetition/fsrs-optimizer) expects. The defaults
beat SM-2 for roughly 99.5% of people, though, so there is no hurry.

## A note on security

The server binds to `127.0.0.1` only, never `0.0.0.0`, and there is no authentication of any kind —
the loopback bind *is* the security model. It is a single-user tool for the machine it runs on.

Don't put it behind a reverse proxy, forward its port, or change the bind address unless you are
adding an auth layer yourself. Anyone who can reach the port can read and delete every card.

## Running it elsewhere

Nothing but `scripts/install.sh` is macOS-specific. On Linux or anywhere else Go runs:

```bash
go build -o flashcard-server .
PORT=17632 ./flashcard-server
```

It will create `~/.flashcard/` and serve on loopback. Supervise it with systemd, a
`--user` service, or whatever you already use.

## Architecture in one screen

A single Go binary with **no third-party Go dependencies** — `go.mod` has no `require` block. The
frontend and all its vendored JS/CSS are baked in with `//go:embed`, so the binary is self-contained
and the app works with the network off.

```
main.go        HTTP handlers, storage, queue building, daily caps
srs.go         FSRS-6, a faithful port of py-fsrs
config.go      Scheduling knobs, validation and clamping
reviewlog.go   Append-only review log
templates/     The frontend: one vanilla JS/HTML file, no build step
static/vendor/ Quill, DOMPurify, marked, Tailwind — vendored, not CDN
```

Two design decisions worth knowing:

- **All scheduling is server-side.** The frontend asks `GET /api/queue` what to show and posts a 1–4
  grade to `POST /api/cards/{id}/review`. It contains no scheduling logic at all. The previous
  design had the algorithm in the browser, where it could not be tested, and it accumulated three
  silent bugs there.
- **`srs.go` is a port, not an original.** Every formula, parameter index and clamp mirrors
  [py-fsrs](https://github.com/open-spaced-repetition/py-fsrs). The golden vectors in `srs_test.go`
  come from upstream's own test suite and exist to prove the port is faithful. Changing the maths
  would fork the algorithm and invalidate the fitted parameters.

[`docs/srs-redesign.md`](docs/srs-redesign.md) explains why the original scheduler was replaced and
what the research says. [`CLAUDE.md`](CLAUDE.md) is the working guide for the codebase.

## Tests

```bash
go test ./... -race        # FSRS conformance, migration, queues, caps, HTTP handlers
go vet ./...
gofmt -l .                 # should print nothing
./scripts/test-grading.sh  # frontend grade derivation, runs on JavaScriptCore
```

Develop against a scratch home directory and a non-default port so you never touch real data or lose
a bind race with the installed service:

```bash
rm -rf /tmp/fc-dev-home && mkdir -p /tmp/fc-dev-home
HOME=/tmp/fc-dev-home PORT=17699 go run .
```

## Credits

Spaced repetition by [FSRS](https://github.com/open-spaced-repetition/fsrs4anki); `srs.go` is a hand
port of [py-fsrs](https://github.com/open-spaced-repetition/py-fsrs).

This is a from-scratch Go rewrite of an earlier Flask/Google Cloud version of the same app, done to
run permanently on one laptop instead of on App Engine — Firestore, Cloud Storage, Firebase Auth and
Google OAuth are all gone, along with the multi-user concept. The content-editing half of the
frontend still descends from that version, which is why some field names (`question_type`,
`answer_type`) read the way they do.

Bundled frontend libraries and their licenses are listed in
[`THIRD-PARTY-NOTICES.md`](THIRD-PARTY-NOTICES.md).

## License

[MIT](LICENSE).
