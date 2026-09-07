# morsanki-data

Shared class schedule consumed by the MorsAnki Anki addon. Edited via Claude
Desktop through the GitHub connector; read by every classmate's Anki at startup
and after each collection sync.

## schedule.json

```json
{
  "exams":   [{"date": "2026-09-20", "name": "Biochem Exam 1"}],
  "unlocks": [{"date": "2026-09-08",
               "lectures": [{"label": "Amino Acid Metabolism",
                             "tags": ["MCOM::C1::Biochem::AAmetab"]}]}]
}
```

### Rules

- `date` is always ISO `YYYY-MM-DD`.
- `label` is the human-readable lecture name shown in the dialog.
- `tag` must be an Anki tag that actually exists in the collection, `::`-separated.
  A tag that does not exist makes "Open in Browse" return zero cards.
- Entries need not be sorted; the addon sorts by date on load.
- Extra keys are ignored, so new fields are safe to add.
- A malformed file is rejected client-side and the previous good copy is kept,
  so a bad commit degrades quietly rather than blanking everyone's schedule.
