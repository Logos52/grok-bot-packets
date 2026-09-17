# Wiki change scan — 2026-09-17 (Thu 09:00 Asia/Taipei)

**Canary (HEAD):** `83ec03b22964eb57c4de7aad6954fd38c9b5e17f`  
**Prior canary (packet #6):** `f143226ce2b5703fa3cc95ec12f6b1b8658877bd`  
**Window:** first change-scan run → last 48h (since ~2026-09-15 08:11 +07)  
**Author:** logos52 (both commits)

## Commits

1. `6a46f4a` — 2026-09-16 13:48 +07 — Notes page: plain lines for the sixteen entries  
   Paths: `notes/index.md`, `src/pages/notes.astro`, `src/lib/icons.ts`, `02 - System/Error Index.md`

2. `83ec03b` — 2026-09-16 16:50 +07 — Harden deploy and cut dead weight from the public wiki repo  
   687 files / ~68.8k deletions: dropped `_archive/`, bulk `outputs/`, diagram `assets/`, Obsidian themes; hardened `.github/workflows/deploy.yml`, `.githooks/pre-commit`, `.gitignore`; touched live site `src/` (graph/search/pulse islands, `index.astro`, `notes.astro`, `llm-knowledge-base.astro`), `AGENTS.md`, `README.md`, removed `00 Command Center/Finances.md`

## Note

Thin scan only — not the Monday five-check mold audit. Outside the 48h window (still after packet #6): three 2026-09-14 home-page commits (`0c218ef`, `cf03d1a`, `6cb8d9b`) plus `02 - System/Owner Writing Samples.md`.
