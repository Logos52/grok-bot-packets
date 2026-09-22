# 📚 Korean-Learning-Wikipedia（韓語學習百科知識庫）

歡迎來到 **Korean-Learning-Wikipedia**！本專案旨在打造一個結構完整、高檢索性、多維度的韓語學習百科系統與語料知識庫。

🌐 **線上發布網址（Firebase Hosting）**：[https://korean-learning-1ec2a.web.app](https://korean-learning-1ec2a.web.app)
（備用網址：[https://korean-learning-1ec2a.firebaseapp.com](https://korean-learning-1ec2a.firebaseapp.com)）

---

## 🌟 專案核心特色

1. **五星級核心詞彙矩陣**：
   - **TOPIK 5,666 基準詞庫**：收錄初中高級完整單字、品詞分類、中英雙語釋義與羅馬拼音。
   - **Kitty 自訂擴充詞庫**：動態收錄口語常用、敬語變形、雙收音特例與專有名詞。
2. **漢字詞與音變解碼大辭典**：
   - 收錄 6,278+ 筆漢字詞彙、1,044 組單音節發音矩陣與 242 筆常用外來語。
   - 連結中文漢字讀音、粵語音律與韓語發音規律，秒速破譯韓語漢字詞。
3. **生活與文化主題百科**：
   - 三麗鷗 10 大主題 100 道人氣韓式美食清單。
   - 後續擴充生活場景、文化習俗與文法句型百科。

---

## 📂 檔案目錄導覽

| 檔案名稱 | 格式 | 說明 |
|:---|:---:|:---|
| [`korean_vocab_5666.md`](./korean_vocab_5666.md) / [`.csv`](./korean_vocab_5666.csv) | MD / CSV | 韓語核心 5,666 基準詞庫全量總表 |
| [`korean_vocab_kitty_add.md`](./korean_vocab_kitty_add.md) / [`.csv`](./korean_vocab_kitty_add.csv) | MD / CSV | 自訂新增詞庫（#5667 起持續擴充） |
| [`korean_hanja.md`](./korean_hanja.md) / [`.csv`](./korean_hanja.csv) | MD / CSV | 韓語漢字詞、單音節矩陣與外來語辭典 |
| [`sanrio_korean_food_100.md`](./sanrio_korean_food_100.md) | MD | 三麗鷗家族 · 100 道人氣韓語食物主題速查手札 |
| [`AGENTS.md`](./AGENTS.md) | MD | 跨 Agent 通用專案藍圖與長期路線圖 |
| [`handoff.md`](./handoff.md) | MD | 跨工作階段 / 跨裝置交接紀錄檔 |

---

## 🤝 跨專案生態系

- 📱 **互動學習應用**：[`Korean-Learning`](../Korean-Learning)（前端互動樂園、造句積木火車、時態/助詞/敬語闖關）
- 📖 **繪本跟讀計畫**：[`Korean-Learning-OpenCode`](../Korean-Learning-OpenCode)（두루책방 124 本階梯閱讀與影子跟讀計畫）
- 🏛️ **百科與知識庫**：`Korean-Learning-Wikipedia`（即本專案：辭典、漢字音變、文法與語料百科）

---

## 🛠️ 開發與維護約定

本專案依循 **AGENTS.md 開放規範**：
- 任何 Agent 開工前請務必先閱讀 [`handoff.md`](./handoff.md) 與 [`AGENTS.md`](./AGENTS.md)。
- 結束階段任務時，請即時更新交接狀態。
