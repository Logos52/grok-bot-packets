# Fleet audit — executive summary

- Audited **17** bots from `profiles.json` (sand-subagent skipped). No `poteto-mode` / `design-grok-bot` under plugins (gmail + x only).
- **Full report:** `/workspace/fleet-audit/REPORT.md`

### Worst three
1. **New Bot** — empty shell; **delete-or-merge**.
2. **Brief** — claims daily push but routine **`enabled: false`**; memory/automation drift → **rewrite**.
3. **後台** — Tokyo/Osaka profile vs Taipei/Taipei-only weather automations; stale XIAOTU-E + ghost Dcard → **rewrite**.

### Snapshot
- Feeders sound; Field/Intake/Yuedu profiles thinner than automations (lift cadence/delivery/anti-jobs).
- Recap↔Arguments fence healthy; Recap LIST omits Frontpage. Ghost **Dcard** breaks Yuedu oral handoff.
- Galaxy meets the bar; 多恩刊 file-only delivery clean; Haggle/Table/Arguments mostly ok.

### pstack
Cursor plugin of workflow skills centered on **poteto-mode** (playbooks, verified unslopped work, deliberate subagents). For this fleet: poteto-mode, unslop, reflect/interrogate, arena/swarm.

### Next (cheap → dear)
1. Delete/assign New Bot  2. Arm or de-claim Brief  3. Unify 星野/後台 TZ + weather cities  4. Restore or cut Dcard  5. TZ on Corpus + Steward Friday  6. Lift pins into short profiles  7. Sync Recap Frontpage  8. poteto-mode for eggbot + clean 後台 memory
