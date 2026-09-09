#!/usr/bin/env python3
import json
from pathlib import Path

state_path = Path("/workspace/watch-state.json")
state = json.loads(state_path.read_text())
ci = json.loads(Path("/workspace/watch-ci-out.json").read_text())

reach = {
  "https://tsumugu.cc/": "ok",
  "https://tsumugu.cc/blog/": "ok",
  "https://tsumugu-ed.com/": "ok",
  "https://tsumugu-ed.com/browse": "ok",
  "https://logos52.github.io/": "ok",
}
cf_cache = {
  "https://tsumugu.cc/": "MISS",
  "https://tsumugu.cc/blog/": "MISS",
  "https://tsumugu-ed.com/": "EXPIRED",
  "https://tsumugu-ed.com/browse": "EXPIRED",
}
cf_dynamic_streak = {u: 0 for u in cf_cache}

audience = {
  "ed": {"v7": 10, "pv7": 10, "ext_ref": 0, "prev_v7": 0, "prev_pv7": 0, "prev_ext_ref": 0},
  "cc": {"v7": 31, "pv7": 43, "ext_ref": 4, "prev_v7": 10, "prev_pv7": 20, "prev_ext_ref": 10},
}
audience_window = {"cur": "2026-09-02..2026-09-08", "prev": "2026-08-26..2026-09-01"}

search = state.get("search", {})
search["ed"] = {"clicks14": 0, "impr14": 1, "prev_clicks14": 0, "prev_impr14": 0}
search["cc"] = {"clicks14": 0, "impr14": 0, "prev_clicks14": 0, "prev_impr14": 6}
search["window"] = "2026-08-26..2026-09-08"
search["prev_window"] = "2026-08-12..2026-08-25"

goatcounter = {
  "site": "logos52",
  "host": "logos52.goatcounter.com",
  "pv7": 2,
  "prev_pv7": 17,
  "window": "2026-09-02..2026-09-08",
  "prev_window": "2026-08-26..2026-09-01",
}

primary = [
  "Logos52/tsumugu-core-dev",
  "Logos52/tsumugu-core",
  "Logos52/tsumugu",
  "Logos52/tsumugu-ed",
  "Logos52/tsumugu-wiki",
  "Logos52/logos52.github.io",
  "Logos52/grok-bot-packets",
]
ci_repos = {}
alerts = 0
for repo in primary:
  r = ci.get(repo, {})
  entry = {
    "conclusion": r.get("conclusion"),
    "status": r.get("status"),
    "name": r.get("name"),
    "html_url": r.get("html_url"),
    "updated_at": r.get("updated_at"),
    "default_branch": r.get("default_branch"),
    "alert": bool(r.get("alert")),
    "error": r.get("error"),
  }
  if entry["alert"]:
    alerts += 1
  ci_repos[repo] = entry

baselines_clean = 0 if alerts else (int((state.get("ci") or {}).get("baselines_clean") or 0) + 1)

lg = ci_repos.get("Logos52/logos52.github.io", {})
reach_actions = {
  "id": None,
  "name": lg.get("name"),
  "status": lg.get("status"),
  "conclusion": lg.get("conclusion"),
  "updated_at": lg.get("updated_at"),
}
if lg.get("html_url"):
  try:
    reach_actions["id"] = int(lg["html_url"].rstrip("/").split("/")[-1])
  except Exception:
    pass

state.update({
  "last_run": "2026-09-09",
  "last_run_at": "2026-09-09T08:01:34+08:00",
  "reach": reach,
  "reach_baselines_clean": int(state.get("reach_baselines_clean") or 0) + 1,
  "audience": audience,
  "audience_window": audience_window,
  "search": search,
  "goatcounter": goatcounter,
  "cf_cache_samples": cf_cache,
  "cf_dynamic_streak": cf_dynamic_streak,
  "keys": {"cf_analytics": True, "gsc": True, "github": True, "goatcounter": True},
  "run_count": int(state.get("run_count") or 0) + 1,
  "overlay_active": False,
  "reach_actions": reach_actions,
  "ci": {
    "baseline_date": "2026-09-09",
    "baselines_clean": baselines_clean,
    "repos": ci_repos,
    "primary": primary,
  },
})

state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n")

def age_str(hours):
  if hours is None or hours == "":
    return ""
  h = float(hours)
  if h >= 48:
    return f"~{round(h / 24)}d"
  return f"~{int(round(h))}h"

core = ci_repos["Logos52/tsumugu-core"]
ed = ci_repos["Logos52/tsumugu-ed"]
core_age = age_str(ci.get("Logos52/tsumugu-core", {}).get("age_h"))
ed_age = age_str(ci.get("Logos52/tsumugu-ed", {}).get("age_h"))

report = "\n".join([
  "**2026-09-09 · slowest TTFB ~0.26s** (tsumugu.cc/) · CF as-of 2026-09-08",
  "",
  "**REACH:** All green · 5/5",
  "Actions: success. CF cache MISS / MISS / EXPIRED / EXPIRED (not DYNAMIC).",
  "",
  "**AUDIENCE:**",
  "- ed (CF RUM): 10 visits / 10 pv · 7d (was 0/0) · ext-ref 0",
  "- cc (CF RUM): 31 visits / 43 pv · 7d (was 10/20) · ext-ref 4",
  "- gc (cc home): 2 pv · 7d (was 17)",
  "",
  "**NEW:** ed visits 0→10 · cc visits 10→31 (≥2×)",
  "",
  "**SEARCH:**",
  "- ed: 0 clicks / 1 impr · 14d (was 0/0)",
  "- cc: 0 clicks / 0 impr · 14d (was 0/6)",
  "",
  "**CI:**",
  f"- Logos52/tsumugu-core — Deploy Tsumugu Core — failure — {core['html_url']} — {core_age} (stale)",
  f"- Logos52/tsumugu-ed — validate corpus — failure — {ed['html_url']} — {ed_age}",
  "",
  "**DECISIONS:**",
  "1. tsumugu-ed validate corpus still red since Sep 2.",
  "2. tsumugu-core Deploy still red since Jul 4 — ignore or archive?",
  "3. tsumugu-core-dev recovered to success (Sep 7) — confirm it holds.",
  "",
])

Path("/workspace/watch").mkdir(parents=True, exist_ok=True)
Path("/workspace/watch/latest.md").write_text(report)
Path("/workspace/watch/report-2026-09-09.md").write_text(report)
print("run_count", state["run_count"], "reach_baselines_clean", state["reach_baselines_clean"], "ci.baselines_clean", baselines_clean, "ci_alerts", alerts)
print("---REPORT---")
print(report)
