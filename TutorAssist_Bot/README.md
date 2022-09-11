# TutorAssist Bot 家教助理機器人
**TutorAssist Bot 不依賴按鍵或關鍵字來理解語言，使用者可以透過日常對話語句來與 Bot 溝通。** TutorAssist Bot 透過日常對話語句，辨識特定意圖及抽取資訊，並反覆予以回應確認，能隨時代為處理家教課程安排上的異動並將消息轉達給家教老師。

---
### TutorAssist Bot 的主要業務範圍
---
**TutorAssist Bot 並不是家教老師的分身，為保障師生雙方的個人隱私，未被授予課程及學生的相關資訊**，在這樣的前提之下，Bot 將不會回答上課時間地點及學生的個人資訊，僅負責處理學生課程異動事宜。

* **課程請假事宜**
* **課程時間調整**
* **改採線上授課**
* **恢復實體授課**
* **回應善意祝福**

---

### 實際操作

---

**操作時，請先和 TutorAssist Bot 打聲簡單的招呼，並且在訊息前標記```@ Bot``` 喔！**

[實際操作範例：](https://youtu.be/slSJLKAhcxs)

https://user-images.githubusercontent.com/86584322/189078205-7694952f-16aa-4c8b-a952-d27d804d58dc.mp4

---
### 檔案總攬
---
```
|   .gitignore ----------------------------------- # .gitignore：避免 account.info 上傳至 GitHub
|   Demo Video.mp4 ------------------------------- # Demo Video.mp4：多輪對話操作示範
|   README.md
|   requirements.txt ----------------------------- # Modules：包含 ArticutAPI、Discord 及 Regular Expression
|   
+---Discord
|   |   account.info
|   |   ArticutDemo.py
|   |   Discord_Jonathan_Boty.py ----------------- # Discord 主程式：處理 Bot 在 Discord 上的運作
|   |   README.md
|   |   Tutor_Assist_Bot.py ---------------------- # Loki NLU 主程式：用 Loki 進行自然語言理解
|   |   
|   \---intent ----------------------------------- # intent：utterance 及語句意圖處理抽取
|           account.info
|           Loki_agree_adv.py
|           Loki_class_arrangement.py
|           Loki_day_off.py
|           Loki_disagree_adv.py
|           Loki_infrom_time.py
|           Loki_online_course.py
|           Loki_physical_course.py
|           Loki_warm_blessing.py
|           Updater.py
|           USER_DEFINED.json
|           
\---ref ------------------------------------------ # ref：可供 Loki 讀取的 ref
        agree_adv.ref
        class_arrangement.ref
        day_off.ref
        disagree_adv.ref
        infrom_time.ref
        online_course.ref
        physical_course.ref
        warm_blessing.ref
```

---

### 環境設定

---

* **Python 3.6+**

* **安裝相關套件** ```$ pip install -r requirements.txt```

* **註冊成為 [Droidtown](https://api.droidtown.co/login/) 會員**

* **建立 account.info**  

  ```json
  {
      "username" : " 填入 Droidtown 帳號 ",
      "articut_key" : " 填入 Articut 金鑰 ",
      "loki_key":" 填入 Loki 專案金鑰 ",
      "discord_token":" 填入 Discord Token "
  }

---

### 啟用 Loki 服務

---

1. 登入 **[Droidtown](https://api.droidtown.co/login/)** 前往```服務資訊```
2. 選擇```Loki```並```開始使用```
3. 輸入專案名稱並```建立專案```
4. 前往```專案```並```選擇檔案```
5. 選擇```ref```中的所有.py檔案
6. 開啟並```讀取意圖```
7. 點選左上房子圖示回到 [**Loki控制台**](https://api.droidtown.co/loki/)
8. ```複製專案金鑰```並填入 ```account.info``` 中 ```loki_key```欄位

---

### 獲取 Aritcut API 金鑰

---

1. 登入 **[Droidtown](https://api.droidtown.co/login/)** 前往```服務資訊```
2. 選擇```Articut```並```複製 API 金鑰```
3. 將 ```API 金鑰```填入```account.info``` 中 ```articut_key```欄位

---

### 參考資料

[卓騰語言科技](https://www.droidtown.co/zh-tw/)

---

### 聯絡資訊

**Jonathan Chen:** chenjonathan901210@gmail.com
若您有任何疑問，歡迎來信討論，感謝您。
