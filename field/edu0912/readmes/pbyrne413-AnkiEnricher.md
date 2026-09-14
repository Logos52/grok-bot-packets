# Anki Enricher

A focused TypeScript CLI for safely enriching existing Anki notes in place.

## Current Features

- **Headword audio**: Generate pronunciation audio for French headwords
- **Sentence audio**: Generate audio for French sentences
- **French images**: Add contextual images from Wikimedia with Openverse fallback
- **Manual image override**: Force a single external image URL when the provider search is wrong or unavailable
- **Tag management**: Manage and refresh note tags
- **Grammar tag repair**: Use the configured Ollama model to classify missing or conflicting grammatical tags, then review/apply only safe, tag-only changes
- **Safe operations**: Dry-run mode and explicit apply workflow
- **Idempotent**: Safe to run repeatedly without duplication
- **Profile-based**: Configurable note profiles for different deck types
- **Validation**: Verify media references, files, fields, and note GUIDs
- **Backups**: Attempt an Anki backup before every applied run; create a native backup before runs over 100 notes or orphan deletion
- **Image confidence**: Rank candidates using French headword, English meaning, and sentence context

## Prerequisites

- Node.js 18+
- Anki with AnkiConnect addon installed
- AnkiConnect listening on `http://localhost:8765` (default)
- macOS `say` voices for French audio (`Thomas` is the default)

## Installation

```bash
npm install
npm run build
```

The CLI uses the configuration file `.enricher-config.json` in the current
working directory unless `--config` is supplied.

For the complete command reference:

```bash
npm start -- --help
```

## Usage

### Dry run - inspect all notes

```bash
npm start -- --scope all --mode dry-run --enrich all
```

Dry runs never call providers, upload media, or modify Anki.

### Enrich missing audio

```bash
npm start -- --scope all --mode missing --enrich audio --apply
```

Applied runs attempt an AnkiConnect backup first. Create a native Anki backup
before runs over 100 notes or orphan deletion. Use `missing` for safe
completion; use `refresh` only when existing enrichment should be replaced.

### Specific note by GUID

```bash
npm start -- --guid <guid> --mode missing --enrich headword-audio --apply
```

### Validation

```bash
npm start -- --scope all --mode validate --enrich all
```

Validation is read-only and reports present, missing, and broken media.

### Preview grammar tag repairs

```bash
npm start -- --scope all --mode dry-run --enrich tags --tag-review-output .enrichment/tag-review.json
```

The tag dry-run scans live Anki tags, sends only notes missing or conflicting
grammatical tags to the configured local Ollama model, and reports proposed
tag-only changes. The optional JSON artifact retains per-note operations for
review and historical analysis. It never modifies Anki.

The project uses the configured local Ollama provider from `.enricher-config.json`
(currently `qwen2.5:7b`). The rule enforced for grammar-tag cleanup is: each note
must have exactly one grammatical-category tag. `grammar` is treated as a
standalone category and never combined with another grammatical tag. Ambiguous
cases are manually reviewed rather than guessed.

After reviewing the artifact, apply its proposed tag-only changes with:

```bash
npm start -- --apply-tag-review .enrichment/tag-review.json --apply --confirm-native-backup
```

The apply step rechecks each live note by noteId + Front value, updates only Tags,
and verifies the result afterward. It does not rerun classification.

### Apply all implemented enrichment types to one note

```bash
npm start -- --front "le bagage" --mode missing --enrich all --apply
```

The currently implemented types are headword audio, sentence audio, images,
and managed tags. Provider failures are reported per note and retried using
the configured retry policy.

### Selective images

Set the profile's `imagePolicy` to `YES` to allow automatic image retrieval:

```json
"imagePolicy": "YES"
```

Confidence thresholds can limit automatic attachment:

```json
"imageThresholds": {
  "auto": 0.5,
  "review": 0.2
}
```

Image candidates are scored from the French headword, the optional `Back`
meaning, and `Sentence French`. This is a heuristic filter, not visual
verification; inspect ambiguous candidates before applying them.

Review data includes French match, English match, sentence-context match,
combined score, automatic and review thresholds, and a final decision:

```text
French match: 0.80
English match: 1.00
Context match: 0.20
Score: 0.76
Auto threshold: 0.50
Review threshold: 0.20
Decision: auto
```

`auto` candidates may be attached automatically, `review` candidates require
manual approval, and `reject` candidates are not attached.

When no candidate is available, the matrix lists each provider outcome:

```text
No candidates found
  wikimedia: error (Request failed with status code 429)
  openverse: no-candidates
```

This distinguishes a provider/rate-limit failure from a successful search that
found no usable image.

Use `REVIEW` to report candidates without changing notes, or `NO` to skip
images. Image providers may return no result or an unsuitable result; inspect
image candidates before applying them, especially for ambiguous words.
Wikimedia searches the French headword and sentence context. Openverse searches
the English meaning, falling back to the French headword and sentence when a
translation is unavailable.
Sentence-like expressions are skipped automatically. For semantically abstract
or otherwise non-visual entries, add one of these note tags to skip image
searches: `no-image`, `abstract`, `grammar`, `phrase`, `idiom`, or `expression`.
Image eligibility is configured independently from vision validation. The default
configuration uses Ollama with `qwen2.5:7b` to classify a selected review batch
in one local text-only request; only entries marked imageable are sent to
Wikimedia or Openverse. If the local classifier is unavailable, review generation
continues without it.

To fetch ranked candidates and local previews without changing Anki:

```bash
npm start -- --front "le balai" --review-images
```

The command writes `review.json` and preview files under `.enrichment/runs/`.
It is subject to Wikimedia rate limits; retry later if the provider returns
`429`.

Open the generated `review.json`, inspect a preview, and add
`"approved": true` to the candidate you want. Apply approved candidates with:

```bash
npm start -- --apply-image-review ".enrichment/runs/image-review-.../review.json" --mode missing --apply
```

If provider search results are unusable, you can also bypass the automatic ranking
and apply a single external image URL directly:

```bash
npm start -- --front-exact "l'encre, la" --mode missing --enrich image --apply --manual-image-url "https://example.com/image.jpg"
```

Only explicitly approved candidates are applied, and the recorded note GUID is
checked before writing.

### Image review task

1. Generate a review artifact for a small selection:

  ```bash
  npm start -- --front-exact "l'encre, la" --review-images
  ```

2. Open the `review.json` path printed by the command. Inspect each local
  `previewFile` and compare it with the French word, English meaning, and
  French sentence.

3. Mark only the chosen candidate with:

  ```json
  "approved": true
  ```

4. Apply the approved candidate:

  ```bash
  npm start -- --apply-image-review ".enrichment/runs/image-review-.../review.json" --mode missing --apply
  ```

5. Validate the note afterward:

  ```bash
  npm start -- --front-exact "l'encre, la" --mode validate --enrich image
  ```

The review command does not modify Anki. The apply command writes only
explicitly approved candidates and checks the recorded note GUID first.

## Project Structure

```
src/
├── cli/               # Command-line interface
├── anki/              # AnkiConnect integration
│   ├── AnkiClient.ts          # Interface definition
│   ├── AnkiConnectClient.ts   # HTTP implementation
│   ├── MediaStorage.ts         # Media upload, reuse, and verification
│   └── SafeNoteWriter.ts        # Explicit, identity-checked field writes
├── model/             # Core data models
│   ├── types.ts                # Type definitions
│   └── ProfileValidator.ts     # Profile validation
├── selection/         # Note selection logic
├── enrichment/        # Enrichment operations
│   ├── Enricher.ts            # Base enricher interface
│   └── index.ts               # Enricher implementations
├── providers/         # External service providers
│   ├── audio/        # Text-to-speech providers
│   ├── stt/          # Speech-to-text providers
│   └── image/        # Image providers
├── cache/            # Caching and persistence
├── validation/       # Validation logic
└── reporting/        # Result reporting
```

## Development Status

Completed: connectivity, selection, profiles, dry runs, safe writes, media
storage, headword audio, sentence audio, caching, validation, image enrichment,
manual image override, managed tags, retries, provider diagnostics, image review,
backups, and automated tests.

The implemented image pipeline includes provider provenance metadata and,
when configured, optional visual-content validation via an OpenAI-compatible
vision model. The project also includes OpenAI-compatible TTS and STT providers
for configured environments, while keeping the default macOS `say` provider as
the local fallback. Release packaging is now validated through the npm tarball
flow, and the tool still does not manipulate Anki's SQLite database.

## Configuration

The repository includes `.enricher-config.json` as a working example:

```json
{
  "profiles": {
    "french-vocab": {
      "name": "french-vocab",
      "modelName": "French FlashCard Model",
      "fields": {
        "front": "Front",
        "headwordAudio": "Front Audio",
        "sentenceFrench": "Sentence French",
        "sentenceAudio": "Sentence French Audio",
        "image": "French Image"
      },
      "managedTags": ["category", "grammatical-type", "register"],
      "tagging": {
        "required": [],
        "managedPrefixes": []
      }
    }
  }
}
```

Only tags listed in `managedTags` or matching `managedPrefixes` may be removed
during `refresh`. Unmanaged user tags are preserved.

## Development

```bash
npm run build       # Compile TypeScript
npm test            # Run unit and integration-boundary tests
npm run type-check  # Type-check without emitting files
```

Generated JavaScript and declarations are written to `dist/`. Local cache and
manifest data are written to `.enrichment/`, which is excluded from Git.

## Current Next Steps

The four missing sentence-audio results from the latest 4,324-note run have
been investigated. The large-run backup policy is now: create a native Anki
backup before a run targeting more than 100 notes or before orphan deletion.
When AnkiConnect reports that its `backup` action is unsupported, applied runs
over 100 notes and orphan deletion require `--confirm-native-backup` after the
native backup has been created.

The project is otherwise in a stable, tested state: release packaging is
validated via `npm pack --dry-run`, image review artifacts include source URL,
author, license, and retrieval time, and OpenAI-compatible TTS/STT is available
when an API key is configured. See [HANDOFF.md](./HANDOFF.md) for the current
status and operational commands.

Wikimedia requests are spaced using `rateLimit.delayMs` from
`.enricher-config.json` (500 ms by default), with additional `Retry-After`
backoff when Wikimedia returns HTTP 429.

Headword audio removes trailing dictionary article metadata and normalizes
typographic apostrophes to the plain apostrophe while preserving French
liaisons such as `l'encre`. Sentence audio still uses the exact `Sentence French` value. Use
`--mode refresh --enrich headword-audio --apply` once to replace audio created
with the previous full-Front behavior.

Dictionary-form Front values that contain punctuation or a comma should use
`--front-exact`, for example `l'encre, la`. The Wikimedia provider normalizes
this form to the concept search `encre` before ranking candidates.

## See Also

- [Project Specification](./French-Anki-Media-Enricher-Project-Spec-v1.0.md)
- [Project Handoff and Remaining Work](./HANDOFF.md)
