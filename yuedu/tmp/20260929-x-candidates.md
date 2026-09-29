# Yuedu X harvest 2026-09-29

## Access status
- Query A: **login wall** (0 posts scanned)
- Query B: **login wall** (0 posts scanned)
- Guest: unavailable. Closing the login dialog left `https://x.com/` marketing splash (“Happening now.” / footer links / “Scan to get the app”), not a timeline. Re-opening Latest search immediately redirected again to login onboarding. No captcha. No credentials entered. No posts invented.

## What was tried
1. Deep link Latest Query A → `https://x.com/i/jf/onboarding/web?...&mode=login` with dialog **“Log in to X” / “See what's happening”**: Continue with phone, Continue with Google, Continue with Apple, or Email or username. No timeline, no “Not now”.
2. Dismissed dialog once (guest attempt) → logged-out homepage splash only.
3. Re-navigated Query A Latest → same onboarding login wall.
4. Deep link Latest Query B → same onboarding login wall (`mode=login`, redirect_after_login encodes the search).

## Counts
- A scanned: 0
- B scanned: 0
- KEEP: 0

## KEEP
None. Timeline never loaded.

## Rejects
None (nothing visible to reject). Already-seen list not applied because no posts were returned.

## Screenshots
- `/workspace/yuedu/tmp/20260929-x/query-a-login-wall.png`
- `/workspace/yuedu/tmp/20260929-x/query-b-login-wall.png`

## Result
Thin oral week. Same pattern as 2026-09-22 and 2026-09-25: box-chrome Latest blocked by login wall; guest view unavailable. Stopped without inventing posts.
