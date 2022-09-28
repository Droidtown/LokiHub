# FitBoty
FitBoty 透過計算基礎代謝率 (BMR)、紀錄飲食攝取及運動消耗，來幫助使用者達到健康控管。

## 檔案總覽
```
├── Discord_FitBoty.py        # 處理聊天對話，並連結 Discord 以驅動 FitBoty   
├── FitBoty.py                # 連動 Loki 以對應使用者的輸入意圖 
├── foodDICT.json             # 對照食物熱量
├── sports_dict.json          # 對照運動消耗
├── extra_sports_dict.json    # 估計未紀錄於 sports_dict.json 的運動消耗
├── README.md
|     
├── intent                    # 所有使用者的對話均透過 Loki 處理以匹配話語意圖
|   ├── Loki_gender.py
|   ├── Loki_age.py
|   ├── Loki_height.py
|   ├── Loki_weight.py
|   ├── Loki_correct.py
|   ├── Loki_incorrect.py
|   ├── Loki_food.py
|   ├── Loki_sports.py
|   ├── Updater.py
|   └── USER_DEFINED 
|
└── ref                       # 於 Droidtown 網站使用 Loki 服務時，需匯入 .ref 檔案
    ├── gender.ref
    ├── age.ref
    ├── height.ref
    ├── weight.ref
    ├── correct.ref
    ├── incorrect.ref
    ├── food.ref
    └── sports.ref
```

## 啟用 Loki 服務
* 於[卓騰語言科技網站](https://api.droidtown.co/)註冊會員。
* 登入後，從 `服務資訊` 進入 `Loki`。
* 選擇 `開始使用 Loki`。

![](https://i.imgur.com/ilWGxij.png)

* 輸入專案名稱，按下 `建立專案`。

![](https://i.imgur.com/dXirHXx.png)

* 進入建立好的專案，點選 `Choose Files`，上傳所有 ref 檔案後，按下 `讀取意圖`。
* 讀取完所有的意圖後，按下 `佈署全部模型`。

![](https://i.imgur.com/fjuo340.png)

* 回到 Loki 首頁，於 `專案金鑰` 欄複製金鑰。

![](https://i.imgur.com/eZEfA5N.png)
