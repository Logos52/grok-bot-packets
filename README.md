# grok-bot-packets

Files the Grok Bot fleet writes under `/workspace` on the shared cloud computer, pushed here on weekdays by the Steward bot. **Private repo** (Wedge 2026-09-07). Still: no secrets, no Mac absolute paths (`/Users/...`), no tan/vault paths. `/workspace/secrets/` is never committed.

Read on the Mac by the `/fold` skill: pull, list files newer than the last fold, decide what to keep.

Layout mirrors `/workspace`: `watch/`, `field/`, `recap/`, `brief/`, `yuedu/`, `table/`, `corpus/`, `steward/`.

Rolling roster: [`steward/fleet-schema.md`](steward/fleet-schema.md). Steward rewrites it when bots are added or deleted.
