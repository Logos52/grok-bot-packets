# Yuedu sources — pin this at `/workspace/yuedu-sources.md`

**Locked 2026-08-13.** Packet language: **全部繁體**. No English gloss. No 简体 sources. No CCP organs. No progressive/activist outlets.

**2026-08-28:** Dcard.tw is **not a live harvest**. Agent Dcard owns that site. Do not open dcard.tw. If 口語 shape is still needed, read `/workspace/dcard/latest.md` after that bot writes it. Own sources stay CNA / iThome / X.

**2026-08-13:** this file is the **source pin for tan channel 15 閱讀**, not a chat-packet recipe. The lesson is a graded rewrite + reader + 金多恩 in `/Users/n1/Projects/tan/library/yuedu/`. Spec: `/Users/n1/Projects/tan/docs/CHANNEL-YUEDU.md`. Partner-pack work stays a session product. The Grok Bot does not teach.

Cadence: Tue/Fri 07:30 Asia/Taipei. First-party fetches only. No Firecrawl. Personal-use volume.

---

## What kind of 中文 this list actually produces

| 種類 | 漢字 | 語體 | 從哪裡來 | 值不值得讀 |
|------|------|------|----------|------------|
| 台灣口語 | 繁 | 語氣詞、夾英文、故事形 | X 上台灣人的生活文；口語形可讀 `/workspace/dcard/latest.md`（agent Dcard 寫的，不是自己開站） | **主菜。** 那種生活中文 |
| 台灣新聞書面語 | 繁 | 中央社／科技報的句子 | CNA 生活／科技／產經；iThome | **配菜。** 當代 B3 末往上練閱讀，不是練說話 |
| 雜誌書面語 | 繁 | 較長、有論點 | 天下雜誌（挑產業／兩岸事實，丟掉減肥點擊文） | 每包最多 1 則 |
| 境外「普通話」電台 | 多半是**简体** | 對大陸廣播書面 | RFA Mandarin RSS（已抽樣：朱镕基、收护照） | **不要。** 繁體報表配簡體來源是兩套中文 |
| 大陸門戶 | 简 | 宣傳書面 | 澎湃、觀察者、新華、人民日報、環球 | **不要** |
| X `lang:zh` 大鍋炒 | 简為主 | 短句、垃圾 | VTuber、幣圈、約會帳號 | **不要。** 2026-08-13 抽樣幾乎沒有可用的台灣口語 |

Bot 寫 packet 時用台灣華語書面＋口語混寫（標題保留原文）。不要寫成對岸新聞腔。

---

## A. 口語形 — 讀檔，不開站

**禁止** 開 `dcard.tw`、六板 URL、或 Dcard API。那是 agent Dcard 的活。

若還需要 口語 shape：讀 `/workspace/dcard/latest.md`（該 bot 寫好才有）。檔不在或過舊 → footer 寫 `dcard/latest 沒有／過舊`，改用自己的 X＋書面。不要用模型記憶假裝有一篇熱門文。不要把六板當 live harvest 再掃一遍。

取捨（讀檔時仍適用）：

- 要：有情節的生活文（租屋、面試、同事、告白、家庭）。長度夠讀 3–8 分鐘。
- 不要：時事／政治板、性別運動文、純靠北、標題黨、引戰、轉載大陸通稿。
- 原文**不要整篇重貼**進 packet（tan 已裁定：shape 留下、原文不轉發）。給標題、一兩句為何值得讀、連結。詞 3–5 個可從可見摘要抽。

---

## B. X.com — 自抓（口語短篇）

Grok Bot 原生能搜。**禁止** `lang:zh` 無過濾。這是自己的源，不是 Dcard 的備援。

每個 run 用這些查詢（Latest，至少 15 fav，去掉回覆）：

```
(租屋 OR 面試 OR 同事 OR 告白 OR 下班) (台灣 OR 台北 OR 台中 OR 高雄 OR 台南) lang:zh min_faves:15 -filter:replies
```

```
(房東 OR 加班 OR 轉職 OR 室友) (台灣 OR 台北) lang:zh min_faves:20 -filter:replies
```

**取捨**

- 要：台灣人在講自己的生活。繁體。有一段落，不是一句幹話。
- 不要：藍綠戰、仇中口號當全文、幣圈、約會廣告、簡體大號、VTuber 宣發。
- 每包最多 **3** 則 X。`/workspace/dcard/latest.md` 已有夠用的口語時，X 讓位。

帳號先不釘死。你之後點名誰，再寫進本檔。

---

## C. 台灣書面語 — 配菜（自抓）

只掃這些。標題＋連結＋一句為何讀。不要做成早報。

| 源 | 取什麼 | URL |
|----|--------|-----|
| 中央社 生活 | 台灣日常、非競選 | https://feeds.feedburner.com/rsscna/lifehealth |
| 中央社 科技 | 產業／AI，非通稿堆 | https://feeds.feedburner.com/rsscna/technology |
| 中央社 產經 | 公司、市場事實 | https://feeds.feedburner.com/rsscna/finance |
| iThome | 台灣科技、資安 | https://www.ithome.com.tw/rss |
| 天下雜誌 | 產業／兩岸事實稿 | https://www.cw.com.tw/RSS/cw_content.xml |

2026-08-13 抽樣：以上五個 RSS 都回 200、繁體標題。CNA 國際／政治能抓，但**不要當主菜**（會把 Yuedu 變成 Brief 的中文版）。

**試過、不要用**

| 源 | 原因 |
|----|------|
| `https://udn.com/rssfeed/news/2/6638?ch=news` | 200 但 item 標題是空的 |
| `https://www.storm.mg/feed` | 回 HTML 訂閱頁，不是 feed |
| BBC 中文繁體 RSS | 這台 12s timeout |
| RFA Mandarin RSS | 活的，但是**简体** |
| DIGITIMES `/tech/rss/rss.asp` | 回網站 HTML，不是 feed |

聯合報首頁 `https://udn.com/news/breaknews/1` 可以當備援瀏覽，不當穩定 RSS。

---

## D. 學中文 meta — 每包最多 1 則，仍用繁體寫

只在真的有政策／方法變動時：

- TOCFL／教育部國語會公告（該 run 才去找官方 URL）
- https://www.hackingchinese.com/ （英文站；**報告仍寫繁體**）

不要每包硬塞一篇「如何背單字」。

---

## 明確排除

**中共宣傳／對岸門戶**

- 人民日報、新華社、央視、求是、學習強國
- 環球時報、觀察者網、澎湃新聞、界面、澎湃系
- 中國時報、中天、旺旺系（統戰風險，不當「藍營平衡」）
- `thepaper.cn`、`cn.nytimes.com`、`bbc.com/zhongwen/simp`（舊 gold stub，已刪）

**左翼／進步宣傳口**

- 關鍵評論網 thenewslens.com
- 報導者 twreporter.org
- 報橘 buzzorange.com
- 沃草 watchout.tw
- 自由時報 ltn.com.tw（黨派社論當新聞）
- Newtalk、風傳媒社論／性別專欄
- 端傳媒 theinitium.com

一則好調查報導出現在排除網域 → 仍不進包。要讀自己點。Bot 不開例外。

**其他**

- Intake 的英文研究（AI／學習科學／wiki craft）
- 改 tsumugu 詞條
- 付費牆繞過
- 用模型記憶生假 URL
- **開 dcard.tw 或掃六板**（那是 agent Dcard 的活）

---

## 評分（維持 gold）

興趣 1–5 × 練習價值 1–5。合計 ≥ 6 才進包。上限：READ 8（口語至少一半：X 自抓 ＋ 可選讀 dcard/latest.md）＋ meta 1。

腳本欄位永遠是 `繁`。出現簡體標題 → 丟棄，不要「轉成繁體充數」。

---

## 每個 run 的取件順序

1. 若需要口語形：讀 `/workspace/dcard/latest.md`（檔不在就跳過）。**不要開 dcard.tw。**
2. X 兩條查詢（自抓）。
3. CNA 生活／科技／產經 ＋ iThome。天下最多掃標題列。
4. 寫 **整包繁體**。
5. 更新 `/workspace/yuedu-seen.json`。60 天內不重複 URL。
6. 同一內容覆寫 `/workspace/yuedu/latest.md`（Steward 備份）。
