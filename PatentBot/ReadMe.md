# PatentBot 專利範圍比對機器人
### 每次撰寫專利範圍時都會擔心內容與既有的專利過於相似而被駁回嗎?
### 想到茫茫廣大專利海中要用布林值搜尋將專利一一撈出比對就頭痛嗎?
#### PatentBot提供你一個不需要一板一眼輸入關鍵字的人性化對話方式解決煩惱!
#### 只要直接輸入想比對的領域、類型以及你的專利範圍，就可以輕輕鬆鬆找到最相似的專利囉!

---

## 快速上手

### 環境設定
1. 下載此專案資料夾

2. 此專案使用的 python 版本為 3.6+，請安裝這個專案會用到的套件:
	- ArticutAPI: 
	`pip3 install AriticutAPI`


---

### 在Loki上建立PatentBot
#### 1 註冊 [卓騰語言科技](https://api.droidtown.co/login/) 帳號
<img src="https://i.imgur.com/gVJon4J.png" width="500" alt="registration.png">

#### 2 建立 Loki Project
1. 登入 [Loki 控制台](https://api.droidtown.co/loki/)。
<img src="https://i.imgur.com/Cn2pfYE.png" width="500" alt="login.png">

2. 在 Loki 控制台中新建一個專案`PatentBot`，並進入專案。
<img src="https://i.imgur.com/GPrIeDi.png" width="500" alt="new_project.png">

3. 在專案下方選擇`ArticutModel`並將`IPC_Number.ref`,`Type.ref`,`Probe.ref`依照下列步驟操作以讀取意圖:
點擊 [瀏覽] > 選擇`PatentBot/ref/IPC_Number.ref` > [讀取意圖]。
<img src="https://i.imgur.com/tyanLl1.png" width="500" alt="ref_upload.png">
意圖(intent)建立完成
<img src="https://i.imgur.com/Ogp6AoI.png" width="500" alt="ref_upload_fin.png">

4. 進入每一個意圖，並在`5. 生成模型`區塊中點擊 [生成模型 (GetVenueAddress)]。
<img src="https://i.imgur.com/NYV9YWI.png" width="500" alt="create_model.png">

5. 完成後，點擊畫面上方左邊的「房子」圖示，回到專案頁。取得`PatentBot`的專案金鑰。
<img src="https://i.imgur.com/NfE35BK.png" width="500" alt="Loki_key.png">

6. 在`PatentBot`目錄下建立 `account.info `。
```
{
    "username":"",
    "apikey": "",
    "loki_key": "",
    "discord_token": ""
}
```
 - username 填入你的 Droidtown 使用者帳號 (email)
 - apikey 填入你的 [Articut 金鑰](https://api.droidtown.co/member/)
 - loki_key 填入你產生的`PatentBot`專案金鑰

7. 可以直接使用此專案裡寫好的intent code，也可以下載專案使用其提供的空白intent code自由發揮。
<img src="https://i.imgur.com/FaZp9uk.png" width="500" alt="download.png">

---

### 在Discord上建立PatentBot
#### 1 註冊 [Discord](https://discord.com/register) 帳號
<img src="https://i.imgur.com/6JWcS6X.png" width="500" alt="registration.png">

#### 2. 建立Discord Bot
1. 進入 [Discord開發者頁面](https://discord.com/developers/applications)，登入你的 Discord 帳號。
<img src="https://i.imgur.com/WyRO58k.png" width="500" alt="login.png">

2. 點擊畫面上方右邊的「New Application」建立一個Application。
<img src="https://i.imgur.com/d5axtgu.png" width="500" alt="new_application.png">

3. 設定Application的名字。
<img src="https://i.imgur.com/vuDfG9c.png" width="500" alt="create_new_application.png">

4. 在 Application 裡，左邊切換到 Bot 的分頁，[Add Bot]，並設定它的名字。
(建議設定一個和 Application 不同的名字。之後比較容易辨識)。
<img src="https://i.imgur.com/CXX2l6n.png" width="500" alt="add_bot.png">

5. 在 Bot 的分頁裡，取得 Bot 的 Token，並填入前述的 account.info 檔案中。
<img src="https://i.imgur.com/PeO9eOa.png" width="500" alt="token.png">

---

### 啟動PatentBot
1. 在終端機裡，移動到 PatentBot 目錄之下，執行：
`python3 discord_bot_patent.py`

2. 在 Discord 的裡 @<你的bot> 然後就可以和它對話了！

<a href="https://www.youtube.com/watch?v=DVxMMq-5-Jo"><img src="https://i.imgur.com/uc6xfrL.png" width="500"></a>

---

### 輸入步驟及範例
1. 分別輸入以下領域和類型中的任一詞彙，也可以是結合後再一起輸入。
	- 領域(IPC_Number):
	"G06Q_020_24": ["信用方案", "信用", "後付", "pay after", "24"]
	"G06Q_020_26": ["轉帳方案", "轉帳", "現付", "pay now", "26"]
	"G06Q_020_28": ["預付方案", "預付", "pay before", "28"]
	- 類型(英文大小寫沒有影響):
	"新型": ["新型", "m"]
	"發明": ["發明", "i"]
	- 例句：我想找發明的, 我想比對轉帳類別下跟發明相關的專利, 有後付的嗎

2. 當Bot確認完你想比對的領域和類型，會請你輸入想比對的專利範圍。
	- [範例內容](https://github.com/Droidtown/LokiHub/blob/main/PatentBot/Dataset/sample.txt)

3. 輸入後PatentBot會再次跟你確認比對的領域和類型，確認無誤進入Articut分析比對內容並獲得比對結果。

---

#### 聯絡資訊
如果有任何問題或建議，請與我們聯絡，謝謝您 :)
* Jan Yen : a4730440@gmail.com
* Meng-Chun Tsai : 96a4a19@gmail.com