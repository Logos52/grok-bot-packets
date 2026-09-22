# Idle Media Pause

An Anki add-on that pauses your music while you are away from a card, and
starts it again when you come back.

If you stop interacting with the card being shown, whatever is currently
playing gets paused. When you grade the card, exactly those players start
again — nothing else, and nothing that was not already playing.

## Behaviour

| What happens | What the add-on does |
| --- | --- |
| Question shown | Starts the idle timer |
| Answer revealed | Restarts the timer, and **stays paused** if it paused |
| Timer runs out | Pauses everything currently playing, and remembers it |
| Card graded | Resumes **only** what it paused |
| You leave the reviewer | Resumes what it paused |

Revealing the answer keeps the music paused on purpose — you are still on the
card. Only moving on brings it back.

Three rules it never breaks:

- If nothing is playing, nothing happens. It will not start your music.
- A player you paused yourself is never resumed, because it was not playing
  when the timer fired and so was never recorded.
- It sends explicit `Pause` and `Play`, never the `PlayPause` toggle your
  keyboard's media key sends. A toggle fired from a timer eventually does the
  opposite of what you wanted.

## How long is "idle"?

Eight seconds, out of the box. Change `idle_seconds` in the add-on config to
taste.

Setting it to `0` follows the deck's **Maximum answer seconds** (Deck options
→ Timers) instead, which is Anki's own idea of how long an answer should take
— 60 seconds unless you changed it, and different per deck if you set it that
way. A fixed number is usually better: if you raised the deck setting to stop
Anki capping your recorded answer times, the idle timeout would otherwise
inherit that long value.

## Requirements

Linux, and either `playerctl` or `gdbus` on your `PATH`. `gdbus` is part of
GLib, so it is almost certainly already installed; `playerctl` is preferred
when present. Any player speaking MPRIS works — Spotify, VLC, Firefox,
Chromium, and most others do.

On macOS and Windows the add-on loads and does nothing.

Your card audio is unaffected: Anki runs mpv with its own config directory,
which stops `mpv-mpris` loading, so Anki's player never appears on the bus.

## Install

From AnkiWeb: *not published yet.*

From a release file: Tools → Add-ons → Install from file, and pick the
`.ankiaddon`.

## Configuration

Tools → Add-ons → Idle Media Pause → Config. Every setting is documented in
the panel beside it; see `src/idle_media_pause/config.md`.

## Development

```sh
./dev-install.sh     # symlink into ~/.local/share/Anki2/addons21
./build.sh           # produce dist/idle_media_pause.ankiaddon
pytest tests/        # the MPRIS layer, no Anki needed
```

There is a flake, so `nix develop` puts Anki, `playerctl`, GLib, `zip` and
pytest on your `PATH` and none of the above needs anything else installed.
Without it, `build.sh` still needs `zip`.

```sh
nix develop          # the shell the three commands above expect
nix build            # the .ankiaddon, in result/share/anki/addons
nix flake check      # the test suite
```

Run Anki from a terminal to see the add-on's output, and drop
`idle_seconds` below the shipped 8 while testing — waiting out the timer on
every case gets old fast.

The code splits three ways:

- `mpris.py` — talking to media players. No Anki imports, which is what makes
  it testable without a GUI. All parsing lives here.
- `controller.py` — the timer and the record of what was paused.
- `__init__.py` — hook wiring, and nothing else.

### Testing against a bundled Anki

One bug only appears outside Nix and other distro packages: Anki's official
Linux bundle sets `LD_LIBRARY_PATH` to its own Qt and GLib, and a helper that
inherits it loads the wrong libraries and fails with symbol errors.
`mpris.build_env()` strips it, the same way Anki does before launching mpv. If
you change how subprocesses are spawned, test that change against an official
Anki build, because a Nix or distro Anki will not reveal the breakage.

## License

MIT

# Who wrote this?

It's vibe coded. 
