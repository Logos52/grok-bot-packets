# Table fetch packet — EQL + WoW
Fetched: 2026-08-13 (today). Method: individual HTTP GET (curl, browser UA, ~20s timeout, follow redirects). No APIs, no logins, no other domains.

Index comparison dates: EQL 2026-07-22; WoW 2026-06-27 (newer of 2026-06-25 / 2026-06-27). An article is newer-than-index if its official date is **after** that game’s index date.

## 1. Per-URL status

| Requested URL | Redirects | Final URL | Final HTTP status | Note |
|---|---|---|---|---|
| https://www.everquestlegends.com/ | 1 (301 → `/home`) | https://www.everquestlegends.com/home | 200 | Marketing homepage. No news list, no event calendar. |
| https://www.everquestguides.com/legends | 1 (301 → trailing slash) | https://www.everquestguides.com/legends/ | 200 | Combo-builder page with printed changelog / “Beta Watch” dates. `Last-Modified: Tue, 11 Aug 2026 02:15:14 GMT`. Page footer: “Unofficial fan tool.” |
| https://worldofwarcraft.blizzard.com/en-us/news/ | 0 | https://worldofwarcraft.blizzard.com/en-us/news/ | 200 | News list (20 articles on page 1) with published dates. |
| https://news.blizzard.com/en-us | 0 | https://news.blizzard.com/en-us | 200 | JS news-feed shell (`blz-news-feed` / `blz-news-event-manager`). **No article headlines or dates in the fetched HTML.** No content invented. |

None returned 202/403/429/5xx.

## 2. EQL dates found

**https://www.everquestlegends.com/home — none posted.**
No launch, patch, maintenance, or season dates on the page. Printed time references only:
- Marketing copy: “At launch, EQL will feature the continents of Antonica, Faydwer, and Odus (pre-Kunark)…”
- Footer: “©2026 Daybreak Game Company LLC.”
- Nav has `/news` and `/patch-notes` links; those pages were **not** fetched (out of source list).

**https://www.everquestguides.com/legends/ — dates printed (unofficial fan tool, same host as requested source):**
- `v4.1 · Updated August 10, 2026`
- Builder Update tooltips dated **August 10, 2026**; **August 6, 2026**; **July 30, 2026**; **July 24, 2026**; **July 16, 2026**; **July 8, 2026**; **June 25, 2026**
- Launch week block: “(Source: EQL dev posts and official announcements, July 20–24, 2026.)”
- “Servers come up at noon Pacific on Tuesday, July 28.” / “Launch is noon PT Tuesday July 28 — queued entry, full wipe”
- “Beta ended July 21 and the launch patch touches nine classes”
- “Kunark is targeted for the end of 2026”
- “Splitpaw and Crushbone both landed in July with no advance notice.”
- “Recent coverage: EQL July 14, 2026 patch notes”
- HTTP `Last-Modified: Tue, 11 Aug 2026 02:15:14 GMT` (header, not body text)

Links: https://www.everquestguides.com/legends/ (no per-item article URLs on this page). Official site article links: none on the fetched homepage.

## 3. WoW news headlines

Format: game | headline | article date | newer-than-index | link

Dates are official `published` timestamps on the news page (YYYY-MM-DD). Visible relative labels (“a day ago”, “2 days ago”, …) were **not** used when an official date was present. Do not treat weekly reset as derived from this page.

| game | headline | article date | newer-than-index | link |
|---|---|---|---|---|
| wow | Curse of Ula’tek Now live! Journey to the Coiled Isle. | 2026-08-11 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24294370/curse-of-ulatek-now-live-journey-to-the-coiled-isle |
| wow | Epic Savings Await: Get 40% off on Midnight™ and More Through September 13 | 2026-08-11 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24295091/epic-savings-await-get-40-off-on-midnight™-and-more-through-september-13 |
| wow | Twitch Drop Now Live! Get the Ensemble: Sorcerer's Grassy Garb Transmog | 2026-08-11 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24294371/twitch-drop-now-live-get-the-ensemble-sorcerers-grassy-garb-transmog |
| wow | Midnight: Curse of Ula'tek Pre-Season Details | 2026-08-10 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24295090/midnight-curse-of-ulatek-pre-season-details |
| wow | Curse of Ula'tek Housing Updates: New Blueprints, Pets, and More Arrive for Your Home | 2026-08-10 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24295382/curse-of-ulatek-housing-updates-new-blueprints-pets-and-more-arrive-for-your-home |
| wow | Undertake Four New Endeavors in Your Neighborhood! | 2026-08-10 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24296054/undertake-four-new-endeavors-in-your-neighborhood |
| wow | WoW Weekly: Curse of Ula'tek, Twitch Drops, Decor Duels, WoW Portal Room, and More! | 2026-08-07 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24295089/wow-weekly-curse-of-ulatek-twitch-drops-decor-duels-wow-portal-room-and-more |
| wow | Follow the Snakes to the Coiled Isle for New Adventures | 2026-08-06 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24293963/follow-the-snakes-to-the-coiled-isle-for-new-adventures |
| wow | Curse of Ula'tek Content Update Notes | 2026-08-06 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24293281/curse-of-ulatek-content-update-notes |
| wow | Curse of Ula’tek: Link Your Battle.net Account to Discord | 2026-08-06 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24296228/curse-of-ulatek-link-your-battlenet-account-to-discord |
| wow | Keep Track of Potions, Trinkets and More with New User Interface Updates | 2026-08-03 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24294064/keep-track-of-potions-trinkets-and-more-with-new-user-interface-updates |
| wow | WoW Weekly: Curse of Ula'tek, Midnight Season 2, August Trading Post, and More! | 2026-07-31 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24295086/wow-weekly-curse-of-ulatek-midnight-season-2-august-trading-post-and-more |
| wow | Stream and Listen to the World of Warcraft: Azeroth Housing Soundtrack | 2026-07-31 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24291433/stream-and-listen-to-the-world-of-warcraft-azeroth-housing-soundtrack |
| wow | World of Warcraft: Midnight Comic, “Legacy of Rage” | 2026-07-31 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24295084/world-of-warcraft-midnight-comic-legacy-of-rage |
| wow | Craft New Adventures with D&D: World of Warcraft | 2026-07-31 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24293053/craft-new-adventures-with-dd-world-of-warcraft |
| wow | Get Ready for a Showdown in August’s Trading Post | 2026-07-30 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24294061/get-ready-for-a-showdown-in-augusts-trading-post |
| wow | Step Into Lairs and Face the Foes Inside | 2026-07-30 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24295085/step-into-lairs-and-face-the-foes-inside |
| wow | Hotfixes: July 28, 2026 | 2026-07-29 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24287397/hotfixes-july-28-2026 |
| wow | The Shadows Deepen: Midnight Season 2 Begins August 18 | 2026-07-28 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24294369/the-shadows-deepen-midnight-season-2-begins-august-18 |
| wow | Curse of Ula’tek: The Venomous Abyss Raid Goes Live August 18 | 2026-07-28 | yes | https://worldofwarcraft.blizzard.com/en-us/news/24294062/curse-of-ulatek-the-venomous-abyss-raid-goes-live-august-18 |

**Patch / hotfix / season dates printed on the WoW news page (not weekly reset):**
- Hotfix article title: “Hotfixes: July 28, 2026” (article date 2026-07-29)
- “Midnight Season 2 Begins August 18”
- “The Venomous Abyss Raid Goes Live August 18”
- “The Curse of Ula’tek content update launches the week of August 11”
- Featured masthead: “Curse of Ula’tek Now live!”
- Sale: “Through September 13” / featured: “Save big from now through September 13.”
- Twitch Drop: “from August 11 at 10:00 am PDT until September 8, at 10:00 am PDT” / featured: “Available until September 8 at 10:00 am PDT.”
- Featured BlizzCon bundle: “Available through September 28, 2026.”

https://news.blizzard.com/en-us: no headlines in static HTML.

## 4. EQL news headlines

Official homepage: **none posted** (no news articles on the fetched page).

Dated items printed on https://www.everquestguides.com/legends/ (changelog / Beta Watch; all share that page URL):

| game | headline | article date | newer-than-index | link |
|---|---|---|---|---|
| eql | v4.1 · Updated August 10, 2026 | 2026-08-10 | yes | https://www.everquestguides.com/legends/ |
| eql | Leveling Pillar Weight Curve (v4.1) | 2026-08-10 | yes | https://www.everquestguides.com/legends/ |
| eql | Leveling Mode — Burst Scoring (v4.0) | 2026-08-10 | yes | https://www.everquestguides.com/legends/ |
| eql | Pet Scoring Pass 2 — Shaman + Enchanter (v3.9) | 2026-08-06 | yes | https://www.everquestguides.com/legends/ |
| eql | Caster Penalty Retirement + SK Plate Fix (v3.8) | 2026-07-30 | yes | https://www.everquestguides.com/legends/ |
| eql | Launch is noon PT Tuesday July 28 — queued entry, full wipe | 2026-07-28 | yes | https://www.everquestguides.com/legends/ |
| eql | Launch Patch Pass — Ranger, Warrior Cleave, AA Rescores (v3.7) | 2026-07-24 | yes | https://www.everquestguides.com/legends/ |
| eql | Beastlord Pet Rescore (v3.6) | 2026-07-16 | no | https://www.everquestguides.com/legends/ |
| eql | EQL July 14, 2026 patch notes (coverage citation) | 2026-07-14 | no | https://www.everquestguides.com/legends/ |
| eql | Pet Scaling, Paladin Self-Heal, Warrior Frenzy (v3.5) | 2026-07-08 | no | https://www.everquestguides.com/legends/ |
| eql | Ranger Sustain, Beastlord Slow, Caster Cleanup (v3.3) | 2026-06-25 | no | https://www.everquestguides.com/legends/ |

Also printed, not given a unique headline row: “Beta ended July 21”; “Kunark is targeted for the end of 2026”; “July 20–24, 2026” launch-week source window.

## 5. Failed sources

None. All four requested URLs returned final HTTP 200. (news.blizzard.com returned 200 but contained no extractable headlines.)

## 6. Newest official date among successful pages

**2026-08-11** — WoW news published date for “Curse of Ula’tek Now live! Journey to the Coiled Isle.” (and two other WoW articles that day). EQL guides body stamp is August 10, 2026; that host’s HTTP Last-Modified is 2026-08-11.

## 7. Raw notable quotes of printed dates (verbatim)

**everquestlegends.com/home**
- “At launch, EQL will feature the continents of Antonica, Faydwer, and Odus (pre-Kunark), and all of the EverQuest playable races (including Iksar, Frogloks, and Kerran)”
- “©2026 Daybreak Game Company LLC. Daybreak, the Daybreak logo and EverQuest Legends are trademarks or registered trademarks of Daybreak Game Company LLC.”

**everquestguides.com/legends/**
- “v4.1 · Updated August 10, 2026”
- “August 10, 2026 (Builder Update) — Leveling mode now uses its own pillar weight curve”
- “(Source: EQL dev posts and official announcements, July 20–24, 2026.)”
- “Servers come up at noon Pacific on Tuesday, July 28. Entry is batched with queues while the team watches server stability, the same process used for open beta. Pre-orders stay open through launch week for the name reservation and the exclusive in-game title. Launch is a full wipe — nothing from beta carries over, and everything made from the 28th is permanent.”
- “Beta ended July 21 and the launch patch touches nine classes — treat these as starting points to re-test, not settled facts.”
- “Kunark is targeted for the end of 2026”
- “Splitpaw and Crushbone both landed in July with no advance notice.”
- “Recent coverage: EQL July 14, 2026 patch notes; in-game logs and creator streams June–July 2026”

**worldofwarcraft.blizzard.com/en-us/news/**
- “Hotfixes: July 28, 2026”
- “The Shadows Deepen: Midnight Season 2 Begins August 18”
- “Curse of Ula’tek: The Venomous Abyss Raid Goes Live August 18”
- “The Curse of Ula’tek content update launches the week of August 11, but you’ll have a whole pre-season week to get gear, hunt treasure, claim rewards, and more!”
- “Watch any eligible World of Warcraft stream on Twitch.tv from August 11 at 10:00 am PDT until September 8, at 10:00 am PDT to claim the Ensemble: Sorcerer's Grassy Garb transmog.”
- “Epic Savings Await: Get 40% off on Midnight™ and More Through September 13”
- Featured subtitle: “Save big from now through September 13.”
- Featured subtitle: “Available until September 8 at 10:00 am PDT.”
- Featured subtitle: “Available through September 28, 2026.”
- Visible relative stamps on the same cards (converted only if no official date; official dates were present): “a day ago”, “2 days ago”, “3 days ago”, “6 days ago”, “7 days ago”, “10 days ago”, “13 days ago”, “14 days ago”, “15 days ago”, “16 days ago”.

**news.blizzard.com/en-us**
- No printed article dates in the fetched HTML.
