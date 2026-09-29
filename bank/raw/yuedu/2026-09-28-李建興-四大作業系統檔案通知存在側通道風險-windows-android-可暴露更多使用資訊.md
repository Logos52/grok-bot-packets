---
id: 2026-09-28-李建興-四大作業系統檔案通知存在側通道風險-windows-android-可暴露更多使用資訊
kind: article
title: 四大作業系統檔案通知存在側通道風險，Windows、Android可暴露更多使用資訊
source: "https://www.ithome.com.tw/news/179240"
author: 李建興
published: 2026-09-28
captured: 2026-09-28
via: grok-bot/Yuedu
lane: yuedu
status: raw
private: false
---

奧地利格拉茲科技大學研究團隊
公開
檔案通知攻擊（File Notification Attacks）研究，指出Linux、Android、Windows與macOS的檔案通知機制可能形成側通道。攻擊程式不必讀取檔案內容，只要觀察檔案何時開啟、修改或刪除，就可能推測按鍵時間、瀏覽網站、通訊軟體媒體活動與應用程式使用情形。目前沒有已知實際攻擊案例。
四套作業系統都提供檔案通知功能，讓程式知道檔案系統發生的變化，Linux使用inotify、Android使用FileObserver、Windows使用ReadDirectoryChangesW，macOS則使用FSEvents。研究發現，部分平臺的檔案通知權限與檔案讀取權限並未完全同步，低權限程式因此可能收到無權讀取檔案的活動通知。
Linux的inotify允許程式監看具有讀取權限的目錄，即使無法讀取目錄內部分檔案，仍可能收到檔案活動通知。研究監看/dev/input目錄，取得鍵盤裝置檔案的活動時間，也能觀察另一名SSH使用者輸入文字時的按鍵時間。攻擊程式無法直接得知輸入內容，但按鍵間隔可用來分析輸入特徵。Linux核心已在2025年12月針對特殊檔案的存取與修改通知加入部分防護，漏洞編號為CVE-2025-68788。
Android的問題牽涉FileObserver與應用程式儲存空間隔離，一般應用程式無法直接查看WhatsApp受保護媒體目錄中的檔案，卻可能收到檔案活動、路徑與檔名通知。攻擊程式可依檔案所在目錄與檔名判斷媒體類型、傳送或接收方向，以及檔案刪除時間，但無法讀取訊息或媒體內容。
Windows的ReadDirectoryChangesW則可能從C:\根目錄暴露其他使用者的檔案活動與完整路徑，Firefox使用網站儲存功能時會建立帶有網站資訊的目錄，研究以1,000個熱門網站測試，網站辨識F1評分達97.8%。微軟已有目錄變更通知權限檢查政策可限制類似資訊外洩，但政策預設沒有啟用。
macOS的FSEvents暴露範圍較小，研究沒有發現與Linux、Android及Windows相同的私人檔案資訊洩漏，但所有使用者可讀取的檔案產生的通知仍可能透露應用程式與系統活動。研究中的攻擊需要能在裝置執行低權限程式碼，例如另一名本機使用者、遭控制的系統服務或遭植入惡意程式碼的軟體套件。
