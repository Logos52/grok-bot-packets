# JLPT Super 8.0

Clean-room Japanese study PWA. The repository does not use data from previous JLPT Super/JLPT Master conversations or databases.

## One-command Windows setup
Double-click `SETUP_WINDOWS.bat`. It installs dependencies, downloads fresh open upstream data, builds Master Data, validates the actual corpus, runs TypeScript + production build, installs Chromium for Playwright and runs E2E tests. It stops immediately if any gate fails.

## Data policy
The installer fetches full current JMdict English JSON and KANJIDIC2 from jmdict-simplified releases, plus open grammar/JLPT enrichment. The app does not fall back to starter/demo dictionary data. See `THIRD_PARTY_DATA.md` for attribution/licensing.

## Supabase
Apply migrations `001` through `005` in order and set the two public environment variables from `.env.example`. Never expose a service-role key in the browser.

## GitHub Auto Sync (v10)
Mở `GITHUB_AUTO_SYNC_GUIDE.md`. Bản v10 có Edge Function `github-sync`, migration `007_github_sync.sql` và màn `/github-sync`. Dữ liệu được lưu Supabase trước rồi snapshot lên GitHub; PAT không nằm trong frontend.
