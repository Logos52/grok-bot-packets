===== PASTE INTO GROK BUILD =====
多恩刊 · 2026-08-31 · 收成好了
Standing assignment: /Users/n1/Projects/tan/handoffs/HANDOFF-DUOEN-KAN.md

window: 00:00 Asia/Taipei → 00:11
canary: 2026-08-30 20:17

AI | 沈文 | https://arxiv.org/abs/2608.26218 | 同一模型只換 harness，緊上下文下修過的測項與完整解都明顯變多
生活 | 阮草 | https://www.cna.com.tw/news/ahel/202608300170.aspx | 信義線東延廣慈/奉天宮站下午2時通車，三小時近萬人次
visible (2–4 original sentences per beat, for shape only):
- AI：arXiv 8月28日新上，作者把編碼 agent 拆成模型加 harness，問權重與題目固定時，改 harness 會不會改結果。
- 對照組把整段對話依時間全塞進窗口，用完就停；處理組留下完整紀錄，但舊工具輸出會依規則縮短，並對重複失敗或空轉下固定提醒。
- 緊窗口 20,480 token、169 題 SWE-bench Verified 裡，每題平均 fail-to-pass 從 28% 升到 49%，完整解從 43 題變 72 題；SWE-bench Pro 完整解從 31 題變 72 題。窗口幾乎不受限時，Verified 與 Pro 兩臂靠近，作者主張評測要把模型與 harness 當成同一個 solver。
- 生活：北捷信義線東延段廣慈/奉天宮站30日下午2時通車，到傍晚5時這站已近萬人次；全系統營運站增到118站、里程132.5公里。
- 象山末班與新站首班一起長鳴6秒，現場有人拿手機拍「一鳴驚人」。以往要先坐公車再轉捷運的人，現在可一車到北車、北投、淡水。
- 通車首月象山到廣慈/奉天宮不計票價，辦到9月28日；前四天還有機票抽獎，當天下午人很多。

failed: Dcard Cloudflare 封鎖（讀 dcard/latest，未開站）· X plugin failed_to_load，無可用可核驗繁體生活 status URL · EQL 官網未取到
===== END PASTE =====
