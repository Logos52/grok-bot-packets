# Apple Watch Ultra 4 (watchOS 27): AI assistants + apps
Researched 30 Sep 2026 for Wedge. Prices are US App Store (USD). The Vietnam store may differ. App Store ratings are as of today.

## Part 1: AI assistants on the watch

### Verdict
- **No chatbot has an official Apple Watch app.** That covers ChatGPT, Claude, Grok, Gemini, Perplexity and Grok Bot. Their App Store listings show iPhone/iPad (and Vision) only. I read the listings and the iTunes lookup device lists.
- **The only AI that is native on the watch is Apple's Siri AI.** On the Ultra 4 it is relayed to a nearby iPhone for processing. Third-party models cannot be selected on the watch today.

### Per assistant

| Assistant | Official watch app? | What actually works on the watch | Source |
|---|---|---|---|
| ChatGPT | No | **iPhone-relayed:** an "Ask ChatGPT" Shortcut shown on the watch. **Third-party:** Petey (free, 3.8★ from 349 ratings, Premium $6.99/mo or $59.99/yr, or bring your own API key). OpenAI staff replied to a feature request: "no timeline" for a native watch app. | OpenAI dev forum thread 1392290; petey.app; wearablexp.com |
| Claude | No (iPhone/iPad, iOS 18+) | **iPhone-relayed:** the "Ask Claude" App Intent (Siri, Spotlight, Share sheet, Shortcuts) is documented for iOS only. The Anthropic help page does not mention the watch. **Third-party:** Rover! (free, bring your own Anthropic API key, runs on the watch over Wi-Fi/cellular, needs watchOS 26.2+, brand new with 0 ratings). | support.anthropic.com article 10263469 (9 Jul 2026); App Store Rover! |
| Grok (xAI) | No. xAI's FAQ lists web, iOS and Android. | **Third-party:** Ask Watch AI (5.0★ from only 6 ratings) supports an xAI key. | x.ai/legal/faq; apps.apple.com Grok; askwatch.app |
| Gemini | No (iPhone/iPad, iOS 17.4+) | **Third-party:** the open-source gemini-watch and iGemini Shortcut need your own API key and Xcode sideloading or a Shortcut. | App Store; github.com/cyroz1/gemini-watch; github.com/gabrielerandazzo/iGemini |
| Perplexity | No (iOS 18+) | **Third-party:** Per Watch (free, 4.0★ from 12 ratings, watchOS 10.2+, ships complications and auto-speak). | App Store Per Watch |
| **Grok Bot** (X Corp, bundle by Cursor/Anysphere) | **No.** The listing says "iPhone, iPad". The docs name iPhone and Android as the mobile targets. | See the next section. | apps.apple.com/us/app/grok-bot/id6794501026; docs.x.ai/grok-bot/mobile |

The "bridge" apps (Petey, Rover, Ask Watch AI, Per Watch) are small indie developers with few ratings. Treat them as optional extras, not recommendations.

### Reaching Grok Bot from the watch
- **Notifications (iPhone-relayed):** Apple's own rule is that alerts go to the watch only when the iPhone is locked or asleep (support.apple.com/108274). Set it in Watch app → Notifications → Grok Bot → "Mirror my iPhone".
- **Caveat:** Grok Bot's docs say mobile push "is still rolling out and may not yet be enabled for every account". A Cursor forum thread is titled "Grok Bot iOS 1.0: push notifications never arrive". I only saw the title.
- **No replying from the watch:** nothing in the docs describes watch actions or replies.
- **No documented Siri, Shortcuts or Action-button integration for Grok Bot.** I searched docs.x.ai/grok-bot for watch, Siri, App Intents and Shortcuts. The only "shortcut" hits are keyboard shortcuts.
- **No iMessage or Messages channel to Grok Bot.** The "iMessage for Grok Bot" plugin (grokbot.dev) is a third-party macOS helper that reads the Mac's Messages database. It is not a way to text a Bot.
- **Slack:** a native Grok Bot plugin/channel exists per the docs. I did not verify its watch behavior.
- **Practical route:** take the notification on the watch, then open the Grok Bot app on the iPhone to reply, dictate, approve or deny.

### Apple Siri AI on the Ultra 4 (watchOS 27, released 14 Sep 2026)
- **Native on the watch:**
  - The Siri AI interface, a dedicated Siri app (conversations sync via iCloud with iPhone, iPad and Mac), the Digital Crown dynamic grid, and a Siri Modular face.
  - It can act in apps, use personal context, and use web world knowledge.
  - Source: apple.com/os/watchos, Apple newsroom 14 Sep 2026, MacRumors 14 Sep.
- **iPhone-relayed:** Siri AI on the watch needs a nearby Apple Intelligence-capable iPhone (iPhone 15 Pro or later) for processing (MacRumors 6 Jul; release notes).
  - Workout Buddy is the exception. It works without the iPhone on Wi-Fi/cellular.
  - A MacRumors commenter reports Siri AI is slow in standalone watch mode. That is one user's report, not a measurement.
- **Setup:** it is a beta and English only, with a waitlist. Go to Settings → Siri → Try Siri AI (Beta) (TNW, 15 Sep). Device and Siri language must both be English. It is not available in the EU or China.
- **Vietnam:** Apple Intelligence lists Vietnamese as supported (Apple Support 121115), but Siri AI itself is English-only. Dictation and Siri Speaks in Vietnamese appear in the watchOS feature list. Live Translation in Messages supports Vietnamese on Watch Series 9+ and Ultra 2+.
- **Extensions to ChatGPT, Claude or Grok on the watch: not available.**
  - Apple's feature table lists the "ChatGPT extension" for iPhone, iPad, Mac and Vision Pro. The Watch is not listed (support.apple.com/121115).
  - MacRumors (14 Sep) found code in the iOS 27 and macOS 27 release candidates showing a "Model Delegation" mechanism that would let Claude appear like the ChatGPT extension. The "Ask…" menu is limited to ChatGPT in the release candidate. Apple has not opened the entitlement to third parties, and it is not user-facing.
  - Assindo (a vendor blog, so secondary) says no Claude, Gemini or Grok extension is registered on shipping devices.
  - I found no source showing a Grok extension.
- **Audio Intelligence** (Ultra 4 and Series 12 only: Live Rewind, Siri Recap, Sound Recognition, faster Shazam) is "later this year". Live Rewind and Siri Recap need an iPhone 16 or later (excluding 16e) and are English at first.

### How to use each on the watch today

| Method | Where it runs | Fits |
|---|---|---|
| Siri AI (Crown → Siri) | Watch UI, processed on the iPhone | Best default |
| Action button → a Shortcut that runs "Ask ChatGPT" or "Ask Claude" | iPhone-relayed | Works for ChatGPT and Claude |
| Notification mirroring | iPhone to watch | Grok Bot alerts |
| Third-party watch apps | Some run on the watch itself, some via the iPhone | Optional; needs API keys |

The Action-button-to-Shortcut method is described in axup.substack.com (Mar 2026).

## Part 2: Recommended watch apps (8–10)

Selection rules: apps with 4.5★ or better on large rating counts, plus quoted owner reviews. No sponsored picks.

**How "owner reviews" were sourced.** I quote App Store reviews directly. My r/applewatchultra and r/AppleWatch threads did not load, so the Reddit consensus on WorkOutDoors, Bevel, Hevy and Gentler Streak comes from search-engine summaries of those threads. Treat that part as secondary.

| # | App | Why (one line) | Price | Rating |
|---|---|---|---|---|
| 1 | **Hevy** (strength, pull-ups) | Free watch app with routines, set logging and heart rate. Rep logging is manual, so it does not auto-count pull-ups. v3.1.10 added reps-only progressive overload for pull-ups and push-ups. | Free. Pro $23.99/yr, $2.99–3.99/mo, or $74.99 lifetime. Free tier: 4 routines, 7 custom exercises, 3 months of history. | 4.9★ / 95K |
| 2 | **Gentler Streak** (ring motivation without burnout) | Readiness-based daily suggestions, rest-day-friendly streaks, and data stays on-device. Siri intents were added for iOS 27. Owner caveat: its effort estimate is off for non-cardio work such as yoga, and you must edit it manually. | Free core. Premium $8.99/mo, $39.99/yr, or lifetime (listed at several tiers, $59.99–179.99). | 4.7★ / 8.8K |
| 3 | **Athlytic** (HRV, recovery) | Recovery, exertion and sleep score from watch data. It supports the Ultra 4's new Recovery HRV. Owners call it a cheaper WHOOP alternative ("$30/yr"). | Pro $4.99/mo or $29.99/yr. 7-day trial. | 4.8★ / 11K |
| 4 | **Bevel** (HRV, recovery; pick 3 or 4) | Free tier is the full tracker: recovery, sleep, strain, strength routines, watch app. Pro adds the AI coach, health records and biological age. | Free. Pro $14.99/mo or $99.99/yr. | 4.85★ / 16.6K |
| 5 | **WorkOutDoors** (running, hiking) | Customizable workout screens and offline maps. Most-cited Ultra-owner pick, and a one-time purchase. | $8.99 once (the App Store lists $11.99 in Canada and $12.99 in Australia). | 4.7★ / 1.7K |
| 6 | **Strava** (social motivation, optional) | Standard running log and community. Only worth it if you want the social layer. | Free. App Store text lists subscription $19.99/mo or $49.99/yr; confirm in-app. | 4.8★ / 375K |
| 7 | **AutoSleep** (sleep) | Automatic sleep tracking from the watch. | $8.99 once. | 4.7★ / 61.7K |
| 8 | **Streaks** (habit rings) | Habit tracker with a watch app. | $5.99 once. | 4.8★ / 27K |
| 9 | **Things 3** (tasks) | Task manager with a watch app. | $9.99 (iPhone). | 4.8★ / 28K |
| 10 | **Google Maps** (navigation) | Gives step-by-step directions on the watch. Directions are mirrored from a trip started on the iPhone (Google help page). | Free. | 4.67★ / 7.4M |

Strong is the alternative to Hevy: 4.9★ / 109K, watch logging with or without the phone, Pro $29.99/yr, $4.99/mo, or $99.99 forever. Neither app auto-counts pull-ups. The only hands-free rep counters I found were new apps such as Motra, Sonar Fit and RepWatch. Their accuracy varies and they are unproven.

### Vietnam notes (from Apple's watchOS 27 feature-availability page)
- **Apple Maps:** Vietnam is **not** on the turn-by-turn navigation list. It is also not on the Transit, Cycling or Custom Routes lists. Google Maps is the practical option.
- **Grab, Be, Xanh SM (Green SM):** no Apple Watch app found in their App Store listings. They are phone-only.
- **Weather and air quality:** Vietnam is **not** on the watchOS Air Quality Index list, so the native watch AQI does not apply. **IQAir AirVisual** (free, 4.82★ / 44.8K, has a watch app) is the fallback.
- **Apple Pay:** supported in Vietnam.
- **Apple Fitness+:** available in Vietnam.
- **Health features:** ECG, Irregular Rhythm, Sleep Apnea, Blood Oxygen and Hypertension notifications are listed for Vietnam.
- **Apple's own Translate watch app** is rated 2.35★ (about 10K ratings). For translation, use Live Translation in Messages (Vietnamese supported) rather than that app.
- **Overcast** (podcasts, free, 4.54★) has a watch app. Apple Podcasts is available in Vietnam.

### Creator check (only what was found)
- **Waveform / MKBHD** ("Our Favorite Apps of All Time", 1 Apr 2026): Marques named **Athlytic** as an honorable mention. He said it takes the Apple Watch data and shows it WHOOP-style. He also named Carrot Weather, Waze and TickTick. A co-host who has since moved to Android said he used **Gentler Streak** with his Apple Watch Ultra and misses it. The episode carries sponsor reads, but these app picks were personal.
- **Minimalist Sibu:** his Aug 2026 post says he uses an Apple Watch Series 11 only as a remote viewfinder and shutter for the iPhone camera. That post was an Apple-hosted press trip to Apple Park (he says Apple gave him the opportunity), so I treated it as PR and drew no recommendations from it.
- **Sasaki Fumio:** a 2018 Oggi interview lists iPhone apps (Way of Life!, Staccal 2), not watch apps.
- **A minimalist blogger (kotakotablog, not one of your named creators):** is summarized by search results as recommending AutoSleep and Things 3 on the watch, matching picks 7 and 9. I did not open that page myself.
- I found nothing watch-specific from the other creators on your list.
