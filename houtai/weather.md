date: 2026-09-15
checked_at: 2026-09-15T13:12 Asia/Taipei
cities:
  Taipei:
    lat: 25.033
    lon: 121.565
    max: 27.0
    min: 24.3
    now: 27.0
    feels: 30.0
    precip_mm: 4.0
    normal_max: 31.47
    normal_rain: 7.01
    normal_n: 70
  Osaka:
    lat: 34.69
    lon: 135.50
    max: 27.8
    min: 22.0
    now: 27.8
    feels: 31.9
    precip_mm: 1.9
    normal_max: 29.5
    normal_rain: 6.26
    normal_n: 70
source: open-meteo forecast; open-meteo archive (±3d Sep 15, 2016–2025); CWA RSS cwa_warning.xml; NCDR CAP JSON; NCDR EQ; JMA quake list + targetTc/TC2630
cwa_key: no
now_md: missing (his city default Taipei)
warnings: CWA RSS 陸上強風特報 (桃園/新竹/苗栗/臺中/彰化/雲林/嘉義/屏東/臺東/澎湖/連江 — 無臺北市); CWA 大雨特報 東北部及新北山區 — 非臺北市; CWA/NCDR 高溫黃色 嘉義縣 only — 非臺北; no 海上/陸上 typhoon warning (TY_NEWS inactive; JMA TC2630 = TD near Truk → Minami-Torishima/Ogasawara track — Kansai not in forecast)
quakes_TW: NCDR 063 09/14 06:44 規模4.9 臺灣東南部海域 (outside 24h window from check); 062 09/14 03:21 規模4.7 花蓮萬榮 (outside 24h); neither 規模≥5 nor 臺北震度≥3 in last 24h
quakes_JP: 24h max M4.4 Fukushima coast 震度1; M4.0 Kumamoto 震度3 (Kumamoto only); no M≥5.0; no 大阪震度≥3
water: no Taipei city water-restriction / 減壓供水 / 限水 stage; NCDR 停水 are local pipe works only
holiday: not this routine
outliers: none
heat_gate_TPE: max≥34.47 or ≥36 or CWA 高溫 臺北 — no (27.0; 高溫 is 嘉義)
rain_gate_TPE: ≥40mm or CWA 大雨/豪雨 臺北市 — no (4.0mm; 大雨 is 東北部/新北山區)
cold_gate_TPE: max≤26.47 or ≤12 or CWA 低溫 — no (27.0)
typhoon_gate: 海上/陸上 warning / Kansai in JMA track — no
quake_gate: 24h 規模≥5 or 臺北震度≥3 / 大阪震度≥3 — no
water_gate: Taipei restriction stage — no
heat_gate_OSA: max≥32.5 or ≥36 — no (27.8)
rain_gate_OSA: ≥40mm — no (1.9)
cold_gate_OSA: max≤24.5 or ≤5 — no (27.8)
snow_gate_OSA: no
