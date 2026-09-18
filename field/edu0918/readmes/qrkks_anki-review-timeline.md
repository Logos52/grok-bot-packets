# Anki Review Timeline

[简体中文](README.zh-CN.md)

A template-independent Anki Desktop add-on that places a compact creation and
review timeline at the end of the card front. Hover over, or focus, the whole
timeline to inspect the card's review history and current FSRS state.

![Anki Review Timeline in English](docs/timeline-en.png)

## Why this add-on?

Anki card templates cannot read card creation time or review-log history. This
add-on reads those values directly from the local collection, so it works
across note types without adding fields or editing card templates.

## Features

- Keeps the timeline at the end of the front on both the question and answer
  sides.
- Uses a neutral creation marker and rating-colored review markers.
- Opens one complete status panel when the timeline is hovered or focused.
- Shows creation time, first and latest review, total reviews, and rating
  counts.
- Lists each answered review with its exact time, resulting interval, answer
  time, and historical FSRS difficulty when Anki stored one.
- Shows current retrievability, stability, normalized difficulty, and desired
  retention when an FSRS memory state is available.
- Automatically follows Anki's Simplified Chinese or Traditional Chinese UI;
  all other interface languages use an English fallback while preserving the
  locale's date formatting.
- Flips and clamps the panel near viewport edges, with a compact mobile-width
  layout.
- Isolates its styles in a Shadow DOM to avoid conflicts with card CSS.
- Excludes manual forget/reschedule records (`ease = 0`) from answered-review
  counts.

## Compatibility

- Anki Desktop only. AnkiMobile and AnkiDroid do not load desktop add-ons.
- Developed and tested on Anki 26.8.1 for Windows.
- Review history works with or without FSRS. Current-state metrics and
  historical difficulty appear only when Anki has stored the corresponding
  FSRS data.

## Install

1. In Anki, open **Tools > Add-ons > Get Add-ons...**.
2. Enter the AnkiWeb add-on code `1232577300` and confirm.
3. Restart Anki.

[Open the AnkiWeb add-on page](https://ankiweb.net/shared/info/1232577300).

### Install manually

1. Download `anki-review-timeline.ankiaddon` from the
   [latest GitHub release](https://github.com/qrkks/anki-review-timeline/releases/latest).
2. In Anki, open **Tools > Add-ons > Install from file...** and select the
   downloaded package.
3. Restart Anki.

### Build from source

1. Clone this repository.
2. Run the tests and build the package:

   ```powershell
   python -m unittest discover -s tests -v
   powershell -ExecutionPolicy Bypass -File .\scripts\build.ps1
   ```

3. In Anki, open **Tools > Add-ons > Install from file...** and select
   `dist/anki-review-timeline.ankiaddon`.
4. Restart Anki.

For local development, the following command builds, installs, and verifies
the add-on in the current Windows user's Anki profile:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-local.ps1
```

The installer preserves Anki's `meta.json` and any files not owned by this
project.

## Use and configuration

Review a card normally. The timeline appears after the front content and stays
at the front/back boundary after the answer is revealed. Hover over it with a
mouse, or focus it with the keyboard, to open the panel.

Use Anki's add-on configuration screen to change:

```json
{
  "max_visible_reviews": 30,
  "show_time": false
}
```

- `max_visible_reviews` controls how many recent review dots are drawn
  (clamped to 1–100). The panel still lists the complete history.
- `show_time` adds hours and minutes to dates in the top summary. Individual
  review rows always include time to the minute.

## Understanding the FSRS values

- **Retrievability** is an estimate of the probability of recalling the card
  now. It changes as time passes.
- **Stability** is the interval over which retrievability is expected to fall
  from 100% to 90%.
- **Difficulty** is Anki's FSRS difficulty normalized from its internal 1–10
  scale to 0–100%.
- **Target** is the desired retention configured for the card.

These are descriptive values read from Anki; the add-on does not alter
scheduling.

## Privacy and data safety

All processing happens inside Anki. The add-on makes no network requests and
does not modify notes, cards, templates, review history, or scheduling data. It
only reads the active card and its local review log to render the panel.

## Development

```text
src/anki_review_timeline/  Add-on source packaged for Anki
tests/                     Pure-Python data tests and browser fixture
scripts/build.ps1          Builds the .ankiaddon package
scripts/install-local.ps1  Installs and verifies a local development copy
docs/                      README screenshots
```

Run the verification steps before submitting changes:

```powershell
python -m unittest discover -s tests -v
node --check .\src\anki_review_timeline\web\timeline.js
powershell -ExecutionPolicy Bypass -File .\scripts\build.ps1
```

## License

Copyright © 2026 qrkks. Licensed under the GNU Affero General Public License,
version 3 or later (`AGPL-3.0-or-later`). See [LICENSE](LICENSE).
