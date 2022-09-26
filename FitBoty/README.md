# FitBoty
FitBoty 是一個架構在 Discord 平台的聊天機器人，可以透過計算基礎代謝率 (BMR)、紀錄飲食攝取及運動消耗，來幫助使用者達到健康控管。

## 檔案總覽
```
├── Discord_FitBoty.py        # 處理聊天對話，並連結 Discord 以驅動 FitBoty   
├── FitBoty.py                # 連動 Loki 以對應使用者的輸入意圖 
├── foodDICT.json             # 對照食物熱量
├── sports_dict.json          # 對照運動消耗
├── extra_sports_dict.json    # 對照運動消耗 (未紀錄於 sports_dict 的項目)
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
└── ref                        # 於 Droidtown 網站使用 Loki 服務時，需匯入 ref 檔案
    ├── gender.ref
    ├── age.ref
    ├── height.ref
    ├── weight.ref
    ├── correct.ref
    ├── incorrect.ref
    ├── food.ref
    └── sports.ref
```
