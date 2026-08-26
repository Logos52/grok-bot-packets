# Yuedu X/Twitter candidates (from already-fetched HTML)

Parsed on disk only. No Firecrawl. No invented posts.

Also checked: `/workspace/yuedu-rss-shortlist.md` **does not exist**.

---

## 1. What each HTML file actually is

### `/tmp/xcancel1.html` (11 354 bytes)

**Antibot / captcha wall. Zero tweets.**

- Title: `Verifying your browser…`
- Visible h1: `Checking your browser`
- Body is a Cap WASM / JS-challenge spinner (`/antibot/assets/js-challenge.js`, `/antibot/captcha`).
- No tweet text, handles, `status/` URLs, timestamps, or like counts.
- No Chinese text at all.
- This is the xcancel/nitter-style interstitial, not a search-results page.

### `/tmp/xsearch1.html` (274 552 bytes) — query A attempt

**Logged-out X.com JS shell. Empty tweet store. Search failed 401.**

- `lang="zh-Hant"`, preloads `bundle.LoggedOutShell` + `bundle.LoggedOutRoutes`.
- `__META_DATA__.isLoggedIn`: **false**
- `session`: guest (`guestId` present), `country: "XX"`, `language: "zh-Hant"`
- `entities.tweets.entities`: **{}**
- `entities.users.entities`: **{}**
- `entities.users.errors.search`: `ApiError` **HTTP 401** on `userByRestId` / `FETCH_USER_BY_SCREEN_NAME` (code 50)
- `users.fetchStatus.search`: **failed**
- Visible noscript/plain text is only the “JavaScript 無法使用 / enable JS to continue using x.com” error plus footer links (說明中心、服務條款、隱私政策、Cookie 使用政策、廣告資訊).
- No `status/{id}` URLs, no `full_text`, no `favorite_count`, no query string (`租屋` / `面試` / search `q=` not in file).
- Chinese tokens in the whole file: those six footer/error phrases only.

### `/tmp/xsearch2.html` (274 552 bytes) — query B attempt

**Same logged-out X.com JS shell as xsearch1. Still no tweets.**

- Same length, same structure, same empty `tweets.entities`, same 401 search error, same `isLoggedIn: false`.
- Byte-level diffs are CSP nonces, guest IDs, `userHash`, and `serverDate` — not result content.
- Query B keywords (`房東` / `加班` / `轉職` / `室友`) are **not** in the file.

Both search dumps are the SPA bootstrap HTML. Tweets would have been filled later by authenticated GraphQL; that never happened.

---

## 2. Real candidates

None. Zero extractable posts (no URL / handle / text / time / faves).

---

## 3. Verdict

X 取不到

原因：三份 HTML 都沒有真實推文。

- `xcancel1.html` = antibot captcha wall（瀏覽器驗證頁），不是搜尋結果。
- `xsearch1.html` / `xsearch2.html` = 未登入 X.com JS shell；`tweets.entities` 空；search 401；可見文字只有「請開 JavaScript」與頁尾條款。查詢 A/B 的關鍵字與任何 `x.com/*/status/*` 都不在檔裡。
