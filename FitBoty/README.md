# FitBoty
FitBoty 透過計算基礎代謝率 (BMR)、紀錄飲食攝取及運動消耗，來幫助使用者達到健康控管。

<img src=readme_pic/FitBoty_demo_ver3.gif width=60% />

    需在每句對話中 @FitBoty 或回覆機器人前面的對話，才可以使用喔！

## 檔案總覽
```
├── Discord_FitBoty.py           # 處理聊天對話，並連結 Discord 以驅動 FitBoty   
├── FitBoty.py                   # 連動 Loki 以對應使用者的輸入意圖 
├── requirements.txt             # 需求套件
├── README.md
|     
├── intent                       # 所有使用者的對話均透過 Loki 處理以匹配話語意圖
|   ├── Loki_gender.py
|   ├── Loki_age.py
|   ├── Loki_height.py
|   ├── Loki_weight.py
|   ├── Loki_correct.py
|   ├── Loki_incorrect.py
|   ├── Loki_food.py
|   ├── Loki_sports.py
|   ├── Loki_update_info.py
|   ├── Updater.py
|   └── USER_DEFINED 
|
├── ref                          # 於 Droidtown 網站使用 Loki 服務時，需匯入 .ref 檔案
|   ├── gender.ref
|   ├── age.ref
|   ├── height.ref
|   ├── weight.ref
|   ├── correct.ref
|   ├── incorrect.ref
|   ├── food.ref
|   ├── sports.ref
|   └── update_info.ref
|
└── misc
    ├── foodDICT.json            # 對照食物熱量
    ├── sports_dict.json         # 對照運動消耗
    └── extra_sports_dict.json   # 估計未紀錄於 sports_dict.json 的運動消耗    
```
## 環境設定
* Python 版本：3.6+

## 啟用 Discord Bot
* 請進入[ Discord developer ](https://discord.com/login?redirect_to=%2Fdevelopers)後註冊並登入
* 點選右上角的 `New application` 後，為 application 取名並點選 `create`，就可以創建一個 app
<img src="https://i.imgur.com/nos2aUs.png" width='60%'>

* 點擊剛剛創立的 app 後，點下左邊欄位的 `Bot` 後，按下頁面右邊的 `Add Bot`，就可以建立機器人了
<img src="https://i.imgur.com/U8wvJaH.png" width='60%'>

* 往下滑看到 Bot permissions 後，勾選同意 Bot 執行的動作
<img src="https://i.imgur.com/pyDIqQ2.png" width='60%'>

* 最後在 TOKEN 的地方按下 `copy`，在另外創建的 account.info.json 檔中，輸入剛複製的 token，就成功建立一個 Discord bot 了 
<img src="https://i.imgur.com/369bFau.png" width='60%'>

```
{"discord_token":"貼上 token"}
```

## 啟用 Loki 服務
* 於[卓騰語言科技網站](https://api.droidtown.co/)註冊會員。
* 登入後，從 `服務資訊` 進入 `Loki`。
* 選擇 `開始使用 Loki`。
<img src=readme_pic/enter_Loki.png width=65% />

* 輸入專案名稱，按下 `建立專案`。
<img src=readme_pic/new_project.png width=60% />

* 進入建立好的專案，點選 `Choose Files`，上傳所有 ref 檔案後，按下 `讀取意圖`。
* 讀取完所有的意圖後，按下 `佈署全部模型`。
<img src=readme_pic/upload_ref.png width=60% />

* 回到 Loki 首頁，於 `專案金鑰` 欄複製金鑰，並輸入在 account.info.json 檔案中。
<img src=readme_pic/Loki_key.png width=60% />

```
{"loki_key":"貼上 loki 金鑰"}
```

## 聯絡資訊
* 如果您對於使用 FitBoty 有任何問題，歡迎來信詢問喔！
    * Carol Hsu: 109555003@g.nccu.edu.tw
    * Ting Tsai: 109555005@nccu.edu.tw


