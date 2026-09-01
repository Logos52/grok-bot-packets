===== PASTE INTO GROK BUILD =====
多恩刊 · 2026-09-01 · 收成好了
Standing assignment: /Users/n1/Projects/tan/handoffs/HANDOFF-DUOEN-KAN.md

window: 00:00 Asia/Taipei → 00:47
canary: 2026-08-31 21:17

AI | 沈文 | https://arxiv.org/abs/2608.28553 | 插件改成獨立進程，工具週期四個殺點後八十場都能冷切續跑且不重做已落盤的效果
生活 | 阮草 | https://www.cna.com.tw/news/ahel/202608310307.aspx | 億元基因治療納健保後，患者須與署方簽至少十年追蹤契約換真實世界療效資料
visible (2–4 original sentences per beat, for shape only):
- AI：arXiv 8月28日上，作者說現有 agent 把插件全塞進同一進程，一掛全掛，升級一個工具也要整桌重開。
- 他們做 Logos，像 ROS 的跨進程匯流排：插件是進程，共用狀態只剩一份 append-only transcript，router 只存路由表。
- 在工具呼叫週期的四個邊界（執行中、回傳未持久化、已持久化未廣播、已廣播）各殺進程，八十場全部冷切續跑，且重做的工作剛好等於 transcript 還沒寫下的那段。
- 同故障對照裡，單進程參考組一次故障打斷同機所有 session；同行程組故障只停在一個節點。匯流排一跳中位 0.215 ms，約莫是模型首 token 的 1/823。
- 生活：健保陸續納入千萬到億元級基因治療後，健保署要求患者與署方簽行政契約，接受至少十年追蹤，爭議走高等行政法院。
- 署方說重點不是天價本身，而是這類藥原則上一生一劑，怕人以為打完就不用回診；要的是真實世界療效資料，對齊國際作法，目前沒預期用法院追訴未回診者。
- 自2023年SMA一劑約4900萬、再到台灣研發的AADC一劑1億納入後，管理才往這條契約路走；旅居國外若能提供適當評估資料，仍可依協議個案處理。

failed: Dcard Cloudflare 封鎖（讀 dcard/latest，未開站）· X plugin failed_to_load，無可用可核驗繁體生活 status URL · EQL 官網無新日期頭條 · WoW 官網最新為數日前 Black Temple／Season 2，今晚不另立 gaming 欄
===== END PASTE =====
