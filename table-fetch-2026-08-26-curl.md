# Table fetch packet — 2026-08-26 (curl)

Fetched: Wednesday 2026-08-26 (Asia/Taipei). HTTP `Date` headers: 2026-08-26 01:05 UTC = 08:05 ICT / 09:05 Asia/Taipei.
Method: one GET per listed URL (curl `-L`, browser UA, `--max-time 20`). No APIs, no logins, no Firecrawl, no Wowhead, no MediaWiki, no lodestone, no nintendo.com. GW dropped.

Index: EQL Latest-Builds **2026-07-22**; WoW **2026-06-27**. An article is newer-than-index if its official date is **after** that game’s index date. Dedup vs `/workspace/table-seen.json` (same url). Do not compute weekly reset.

## 1. Per-URL status

| Requested URL | Redirects | Final URL | Final HTTP status | Note |
|---|---|---|---|---|
| https://www.everquestlegends.com/ | 1 (301 → `/home`) | https://www.everquestlegends.com/home | 200 | Marketing homepage. No news list, no event calendar. |
| https://www.everquestguides.com/legends | 1 (301 → trailing slash) | https://www.everquestguides.com/legends/ | 200 | Unofficial fan combo-builder. Changelog / Beta Watch dates. `Last-Modified: Wed, 19 Aug 2026 17:36:45 GMT` (unchanged vs 2026-08-22 fetch). Footer: unofficial. |
| https://worldofwarcraft.blizzard.com/en-us/news/ | 0 | https://worldofwarcraft.blizzard.com/en-us/news/ | 200 | News list (20 articles on page 1) with `iso8601` published dates. |
| https://news.blizzard.com/en-us | 0 | https://news.blizzard.com/en-us | 200 | JS news-feed shell (`blz-news-feed`). **No article headlines or dates in the fetched HTML.** No content invented. |
| https://www.witchbrook.com/ | 0 | https://www.witchbrook.com/ | 200 | FAQ homepage. `Last-Modified: Tue, 25 Aug 2026 21:14:22 GMT` (was Fri, 21 Aug 2026 on 2026-08-22 fetch). TLS ok (`ssl_verify_result=0`). Body launch wording unchanged (year only). |
| https://www.hauntedchocolatier.net/ | 0 | https://www.hauntedchocolatier.net/ | 200 | Dev blog. No release date. |
| https://www.rockstargames.com/VI | 0 | https://www.rockstargames.com/VI | 200 | Official GTA VI page. Console platforms only. PC not listed. |
| https://www.thewitcher.com/en/en/songs-of-the-past | 0 | https://www.thewitcher.com/en/en/songs-of-the-past | 200 | Marketing hero. Static HTML: “Coming in 2027”. No more-specific date than 2027. |
| https://www.cdprojekt.com/en/media/news/the-witcher-3-wild-hunt-songs-of-the-past-announced/ | 0 | same | 200 | Corporate news post dated May 27, 2026. Launch still “2027”. See also: two 25 Aug same-host posts (not fetched). |
| https://press.cdprojektred.com/en/news/1835/the-witcher-3-wild-hunt-songs-of-the-past-at-gamescom-2026 | 0 | same | 200 | Press post dated July 21st, 2026. Launch still “2027”. No newer posts visible on this page. |
| https://larian.com/ | 0 | https://larian.com/ | 200 | Studio homepage. New Divinity: no calendar date. |
| https://divinity.com/ | 0 | https://divinity.com/ | 200 | Game site. `Last-Modified: Wed, 19 Aug 2026 20:35:22 GMT` (unchanged vs 2026-08-22 fetch). No release date. |

None returned 202/403/429/5xx. Witchbrook TLS ok (ssl_verify_result=0). No retries.

## 2. EQL calendar dates

**https://www.everquestlegends.com/home — none posted.**
No launch, patch, maintenance, or season dates on the page. Printed time references only:
- Marketing copy: “At launch, EQL will feature the continents of Antonica, Faydwer, and Odus (pre-Kunark)…”
- Footer: “©2026 Daybreak Game Company LLC.”
- Nav has `/news` and `/patch-notes` links; those pages were **not** fetched (out of source list).

**https://www.everquestguides.com/legends/ — dates printed (unofficial fan tool; same URL already in seen → already-seen, not NEW):**
- `v4.2 · Updated August 19, 2026` (newer-than-index vs 2026-07-22: yes; unchanged vs 2026-08-22 fetch)
- Builder Update tooltips: **August 19, 2026**; **August 10, 2026**; **August 6, 2026**; **July 30, 2026**; **July 24, 2026**; **July 16, 2026**; **July 8, 2026**; **June 25, 2026**
- v4.2 tooltip: “August 19, 2026 (Builder Update) — Beastlord warder damage raised … to reflect the Aug 18 substantial warder melee buff.”
- “(Source: EQL dev posts and official announcements, July 20–24, 2026.)”
- “Servers come up at noon Pacific on Tuesday, July 28.” / “Launch is noon PT Tuesday July 28 — queued entry, full wipe”
- “Beta ended July 21 and the launch patch touches nine classes”
- “Kunark is targeted for the end of 2026”
- “Splitpaw and Crushbone both landed in July with no advance notice.”
- “Recent coverage: EQL July 14, 2026 patch notes”
- HTTP `Last-Modified: Wed, 19 Aug 2026 17:36:45 GMT` (header, not body text; unchanged vs 2026-08-22 fetch)

Official site article links: none on the fetched homepage. Guides page has no per-item article URLs.

## 3. WoW headlines

Dates are official `iso8601` published timestamps on the news page (YYYY-MM-DD). Relative labels (“7 hours ago”, “8 hours ago”) were **not** used. Do not treat weekly reset as derived from this page.

Index date: **2026-06-27**. All 20 page-1 articles are newer-than-index.

### NEW (not in table-seen.json before this fetch)

| game | headline | article date | newer-than-index | link |
|---|---|---|---|---|
| wow | Set Out with the Hearthkeeper’s Wandering Caravan Mount | 2026-08-25 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24298583/set-out-with-the-hearthkeepers-wandering-caravan-mount |
| wow | Bloom Bright with the Vibrant Petalweave Collection | 2026-08-25 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24298582/bloom-bright-with-the-vibrant-petalweave-collection |
| wow | Hotfixes: August 25, 2026 | 2026-08-25 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24296142/hotfixes-august-25-2026 |
| wow | Curse of Ula’tek: The Venomous Abyss Story Mode and Raid Finder Wing 2 Now Live! | 2026-08-25 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24294062/curse-of-ulatek-the-venomous-abyss-story-mode-and-raid-finder-wing-2-now-live |
| wow | Carve, Climb, and Cruise Through the Skies of Northrend | 2026-08-25 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24295088/carve-climb-and-cruise-through-the-skies-of-northrend |
| wow | BCC Anniversary Edition: Black Temple Arrives August 27 | 2026-08-24 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24291476/bcc-anniversary-edition-black-temple-arrives-august-27 |
| wow | September is a Great Month to Celebrate Friendship at the Trading Post | 2026-08-24 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24295383/september-is-a-great-month-to-celebrate-friendship-at-the-trading-post |

(Article IDs 24296142 / 24294062 previously appeared under different slugs — “hotfixes-august-20-2026”, “curse-of-ulatek-the-venomous-abyss-raid-now-live”. Dedup is by full URL, so these slugs count as NEW.)

### Already-seen (same url; still on page 1)

| headline | date | link |
|---|---|---|
| The Venomous Abyss, Season 2, and More Await in This Week’s WoW Weekly! | 2026-08-21 | https://worldofwarcraft.blizzard.com/en-us/news/24298584/the-venomous-abyss-season-2-and-more-await-in-this-weeks-wow-weekly |
| Into the Venomous Abyss: Midnight's Race to World First Begins | 2026-08-18 | https://worldofwarcraft.blizzard.com/en-us/news/24295087/into-the-venomous-abyss-midnights-race-to-world-first-begins |
| Midnight Season 2 is Now Live! | 2026-08-18 | https://worldofwarcraft.blizzard.com/en-us/news/24294369/midnight-season-2-is-now-live |
| WoW Weekly: Curse of Ula'tek, Blueprints, Endeavors, and More! | 2026-08-14 | https://worldofwarcraft.blizzard.com/en-us/news/24295094/wow-weekly-curse-of-ulatek-blueprints-endeavors-and-more |
| Curse of Ula’tek Now live! Journey to the Coiled Isle. | 2026-08-11 | https://worldofwarcraft.blizzard.com/en-us/news/24294370/curse-of-ulatek-now-live-journey-to-the-coiled-isle |
| Epic Savings Await: Get 40% off on Midnight™ and More Through September 13 | 2026-08-11 | https://worldofwarcraft.blizzard.com/en-us/news/24295091/epic-savings-await-get-40-off-on-midnight™-and-more-through-september-13 |
| Twitch Drop Now Live! Get the Ensemble: Sorcerer's Grassy Garb Transmog | 2026-08-11 | https://worldofwarcraft.blizzard.com/en-us/news/24294371/twitch-drop-now-live-get-the-ensemble-sorcerers-grassy-garb-transmog |
| Midnight: Curse of Ula'tek Pre-Season Details | 2026-08-10 | https://worldofwarcraft.blizzard.com/en-us/news/24295090/midnight-curse-of-ulatek-pre-season-details |
| Curse of Ula'tek Housing Updates: New Blueprints, Pets, and More Arrive for Your Home | 2026-08-10 | https://worldofwarcraft.blizzard.com/en-us/news/24295382/curse-of-ulatek-housing-updates-new-blueprints-pets-and-more-arrive-for-your-home |
| Undertake Four New Endeavors in Your Neighborhood! | 2026-08-10 | https://worldofwarcraft.blizzard.com/en-us/news/24296054/undertake-four-new-endeavors-in-your-neighborhood |
| WoW Weekly: Curse of Ula'tek, Twitch Drops, Decor Duels, WoW Portal Room, and More! | 2026-08-07 | https://worldofwarcraft.blizzard.com/en-us/news/24295089/wow-weekly-curse-of-ulatek-twitch-drops-decor-duels-wow-portal-room-and-more |
| Follow the Snakes to the Coiled Isle for New Adventures | 2026-08-06 | https://worldofwarcraft.blizzard.com/en-us/news/24293963/follow-the-snakes-to-the-coiled-isle-for-new-adventures |
| Curse of Ula'tek Content Update Notes | 2026-08-06 | https://worldofwarcraft.blizzard.com/en-us/news/24293281/curse-of-ulatek-content-update-notes |

(Previously seen page-1 titles from 2026-08-22 — “Hotfixes: August 20, 2026”, “Curse of Ula’tek: The Venomous Abyss Raid Now Live!”, plus older slugs that had already fallen off — are **not** on this page-1 URL list; seven newer/retitled slugs displaced them.)

**Patch / hotfix / season dates printed on the WoW news page (not weekly reset):**
- Featured masthead: “Midnight Season 2 is Now Live”
- Featured: “Curse of Ula’tek Now live!”
- Featured subtitle: “Prepare for all new challenges, rewards, and achievements in Season 2.”
- Article title: “Hotfixes: August 25, 2026” (article published 2026-08-25)
- Article title: “Curse of Ula’tek: The Venomous Abyss Story Mode and Raid Finder Wing 2 Now Live!” (published 2026-08-25)
- Article title: “BCC Anniversary Edition: Black Temple Arrives August 27” (published 2026-08-24)
- Article title: “Midnight Season 2 is Now Live!” (published 2026-08-18)
- “The Curse of Ula’tek content update launches the week of August 11”
- Embedded body text still on page-1 HTML: “Week of August 18” (raid / Mythic+ Season 2 / PvP Season 2 / Delves schedule blocks) and “When Season 2 begins on August 18”
- Sale: “Through September 13” / featured: “Save big from now through September 13.”
- Twitch Drop: “from August 11 at 10:00 am PDT until September 8, at 10:00 am PDT”
- Featured BlizzCon bundle: “Available through September 28, 2026.”
- Trading Post article title: “September is a Great Month to Celebrate Friendship at the Trading Post”
- Embedded: “Through August 24”
- Heading: “Prove Your Worth in Arena Season 3”

https://news.blizzard.com/en-us: no headlines in static HTML.

## 4. Upcoming pins

- **Witchbrook** | 2026 (year only) | https://www.witchbrook.com/ — “Witchbrook will be coming to PC, Nintendo Switch, and Xbox in 2026.” Also: “Witchbrook will be coming to Steam, Nintendo Switch, Nintendo Switch 2, and Xbox.” No month/day. Last-Modified header 2026-08-25 not used as a body date. Same URL already-seen.
- **Haunted Chocolatier** | none posted | https://www.hauntedchocolatier.net/ — “The bottom line is, I don’t want to give a release date. The game will come out when it’s done.” Latest dated blog on the page: “Still here, still grinding…” June 25, 2026 (https://www.hauntedchocolatier.net/2026/06/25/still-here-still-grinding/). Same URL already-seen.
- **GTA VI (PC)** | PC not listed · console **November 19, 2026** PlayStation 5 / Xbox Series X|S · Extended Look **August 27** **3 PM ET** | https://www.rockstargames.com/VI — platforms printed: “PlayStation 5” “Xbox Series X|S” only. No PC / Windows / Steam listing. Same URL already-seen.
- **Witcher 3 — Songs of the Past** | launch still **2027** (no more-specific date printed on the three fetched pages after gamescom Opening Night Live) · gamescom floor **August 26–30, 2026** (business **August 26–28**; entertainment **August 26–30**) · Opening Night Live mentioned, no calendar day printed as a launch date | https://www.thewitcher.com/en/en/songs-of-the-past (“Coming in 2027”) · https://www.cdprojekt.com/en/media/news/the-witcher-3-wild-hunt-songs-of-the-past-announced/ (article **May 27, 2026**; “It will launch in 2027 on PlayStation 5, Xbox Series X|S, and PC”; “More details … late summer 2026”) · https://press.cdprojektred.com/en/news/1835/the-witcher-3-wild-hunt-songs-of-the-past-at-gamescom-2026 (article **July 21st, 2026**; “when it launches in 2027 on PlayStation 5, Xbox Series X|S, and PC”). Same three URLs already-seen.
  - Same-host “See also” on the fetched cdprojekt.com announcement page (those article bodies were **not** fetched): “The Witcher 3: Wild Hunt — Remastered Announced, Songs of the Past Gets First Look” **25 Aug** → https://www.cdprojekt.com/en/media/news/the-witcher-3-wild-hunt-remastered-announced-songs-of-the-past-gets-first-look/ ; “CD PROJEKT RED refreshes its brand and logo” **25 Aug** → https://www.cdprojekt.com/en/media/news/cd-projekt-red-refreshes-its-brand-and-logo/ . Printed date on the fetched page is “25 Aug” (no year next to the day; page copyright ©2026). Those two URLs were not in seen.json → NEW.
  - press.cdprojektred.com 1835 page: no newer posts than the pinned 1835 article are visible on that page (only `/en/news` hub link; no other `/en/news/NNNN/…` items).
- **Larian — Divinity** | none posted | https://larian.com/ · https://divinity.com/ — marketing copy only (“The gods are silent. Rivellon bleeds. New powers stir.”). Press-kit label “December 2025” is an asset pack date, not a game release date. Same URLs already-seen.

## 5. Failed sources

none (all 12 listed live URLs HTTP 200). news.blizzard.com/en-us returned 200 with no headlines in static HTML.

## 6. Newest official date among these pages

**2026-08-25** — WoW “Set Out with the Hearthkeeper’s Wandering Caravan Mount” published timestamp `2026-08-25T18:23:00.000Z` on https://worldofwarcraft.blizzard.com/en-us/news/24298583/set-out-with-the-hearthkeepers-wandering-caravan-mount

(Next: WoW “Bloom Bright with the Vibrant Petalweave Collection” `2026-08-25T18:21:00.000Z`; WoW “Hotfixes: August 25, 2026” `2026-08-25T17:10:32.100Z`. cdprojekt.com See-also labels “25 Aug” on the May 27 announcement page; those article bodies were not fetched. EQL official homepage: none posted. EQL guides body date August 19, 2026 is unofficial. Witchbrook body year 2026 only; Last-Modified header 2026-08-25 not used as a body date.)

## 7. Verbatim date quotes

- EQL official: none posted (only “©2026 Daybreak Game Company LLC.” / “At launch…”)
- EQL guides: “v4.2 · Updated August 19, 2026”
- EQL guides: “August 19, 2026 (Builder Update) — Beastlord warder damage raised … to reflect the Aug 18 substantial warder melee buff.”
- EQL guides: “Launch is noon PT Tuesday July 28 — queued entry, full wipe”
- EQL guides: “Servers come up at noon Pacific on Tuesday, July 28.”
- EQL guides: “Beta ended July 21 and the launch patch touches nine classes”
- EQL guides: “Kunark is targeted for the end of 2026”
- EQL guides: “Splitpaw and Crushbone both landed in July with no advance notice.”
- EQL guides: “Recent coverage: EQL July 14, 2026 patch notes”
- WoW: “Midnight Season 2 is Now Live”
- WoW: “Midnight Season 2 is Now Live!”
- WoW: “Hotfixes: August 25, 2026”
- WoW: “Curse of Ula’tek: The Venomous Abyss Story Mode and Raid Finder Wing 2 Now Live!”
- WoW: “BCC Anniversary Edition: Black Temple Arrives August 27”
- WoW: “Curse of Ula’tek Now live!”
- WoW: “The Curse of Ula’tek content update launches the week of August 11”
- WoW: “Week of August 18”
- WoW: “When Season 2 begins on August 18”
- WoW: “from August 11 at 10:00 am PDT until September 8, at 10:00 am PDT”
- WoW: “Save big from now through September 13.”
- WoW: “Available through September 28, 2026.”
- WoW: “September is a Great Month to Celebrate Friendship at the Trading Post”
- Witchbrook: “Witchbrook will be coming to PC, Nintendo Switch, and Xbox in 2026.”
- Haunted Chocolatier: “The bottom line is, I don’t want to give a release date. The game will come out when it’s done.”
- Haunted Chocolatier: “Still here, still grinding…” / “June 25, 2026”
- GTA VI: “Coming November 19, 2026”
- GTA VI: “PlayStation 5” “Xbox Series X|S”
- GTA VI: “An Extended Look, Coming August 27”
- GTA VI: “August 27” “3 PM ET”
- GTA VI: “Grand Theft Auto VI is Now Set to Launch November 19, 2026”
- Witcher songs page: “Coming in 2027”
- CDPR news: “May 27, 2026”
- CDPR news: “It will launch in 2027 on PlayStation 5, Xbox Series X|S, and PC”
- CDPR news: “More details on Songs of the Past will be released in late summer 2026.”
- CDPR news See also (printed on this page only): “The Witcher 3: Wild Hunt — Remastered Announced, Songs of the Past Gets First Look” / “25 Aug”
- CDPR news See also (printed on this page only): “CD PROJEKT RED refreshes its brand and logo” / “25 Aug”
- CDPR press: “July 21st, 2026”
- CDPR press: “Showcases will be available in the business area from August 26 to August 28”
- CDPR press: “Showcases will be available in the entertainment area from August 26 to August 30”
- CDPR press: “when it launches in 2027 on PlayStation 5, Xbox Series X|S, and PC”
- Larian / Divinity: none posted (press kit “December 2025” only)
