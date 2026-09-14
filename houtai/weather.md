date: 2026-09-14
checked_at: 2026-09-14T13:08 Asia/Taipei
cities:
  Taipei:
    lat: 25.033
    lon: 121.565
    max: 31.2
    min: 24.6
    now: 31.1
    feels: 36.2
    precip_mm: 2.0
    normal_max: 31.64
    normal_rain: 6.99
    normal_n: 70
  Osaka:
    lat: 34.69
    lon: 135.50
    max: 29.4
    min: 22.9
    now: 28.4
    feels: 33.6
    precip_mm: 0.2
    normal_max: 29.61
    normal_rain: 4.57
    normal_n: 70
source: open-meteo forecast; open-meteo archive (±3d Sep 14, 2016–2025); CWA RSS cwa_warning.xml; NCDR CAP JSON; scweb recent EQ list; JMA quake list + targetTc/TC2630
cwa_key: no
now_md: missing (his city default Taipei)
warnings: CWA RSS 陸上強風特報 (桃園/新竹/苗栗/臺中/彰化/雲林/嘉義/屏東/臺東/澎湖/連江 — 無臺北市); CWA/NCDR 高溫黃色 屏東縣 only — 非臺北; no 大雨/豪雨; no 海上/陸上 typhoon warning (TY_NEWS has no active 警報 for TW); JMA TC2630 = TD near Truk, track toward Minami-Torishima/Ogasawara/south of Japan — Kansai not in forecast track
quakes_TW: CWA 063 09/14 06:44 規模4.9 臺灣東南部海域 (臺東最大4、花蓮3 — 無臺北); 062 09/14 03:21 規模4.7 花蓮萬榮; neither 規模≥5 nor 臺北震度≥3
quakes_JP: 24h max M4.5 Tsugaru Strait 震度3 (Hokkaido/Aomori only); also M2.9 Iwate; no M≥5.0; no 大阪震度≥3
water: no Taipei city water-restriction / 減壓供水 / 限水 stage; NCDR 停水 are local pipe works only
holiday: not this routine
outliers: none
heat_gate_TPE: max≥34.64 or ≥36 or CWA 高溫 臺北 — no (31.2; 高溫 is 屏東)
rain_gate_TPE: ≥40mm or CWA 大雨/豪雨 臺北市 — no (2.0mm)
cold_gate_TPE: max≤26.64 or ≤12 or CWA 低溫 — no (31.2)
typhoon_gate: 海上/陸上 warning / Kansai in JMA track — no
quake_gate: 24h 規模≥5 or 臺北震度≥3 / 大阪震度≥3 — no
water_gate: Taipei restriction stage — no
heat_gate_OSA: max≥32.61 or ≥36 — no (29.4)
rain_gate_OSA: ≥40mm — no (0.2)
cold_gate_OSA: max≤24.61 or ≤5 — no (29.4)
snow_gate_OSA: no
