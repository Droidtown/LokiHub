# 當季食材小幫手—食材問題諮詢機器人

Bot 可以解決的問題
-------------

DEMO
-------------

檔案總覽/目錄
-------------
```
.
├── ingredient_bot.py  # 啟動 bot，處理與 discord 間的互動
├── Loki.py            # 主要使用到 function runLoki 
├── model.py           # NLU model 以及相關的 function
├── README.md
├── requirements.txt
│  
├─info 
│  ├── ingredient.json # 紀錄每個月份的當季食材
│  └── inSeason.json   # 紀錄每個食材的作法、挑法與禁忌
│      
├─intent # 所有的 intent 都放在這
│  ├── Loki_all_ingre.py
│  ├── Loki_capability.py
│  ├── Loki_CheckInSeason.py
│  ├── Loki_InSeason.py
│  ├── Loki_price.py
│  ├── Loki_recipe.py
│  ├── Loki_recommend.py
│  ├── Loki_reject.py
│  ├── Loki_selection.py
│  ├── Loki_taboo.py
│  ├── Loki_which_season.py
│  ├── Updater.py
│  └── USER_DEFINED.json
│          
└─ref # 需要將裡面的所有檔案匯入 Loki project
   ├── all_ingre.ref
   ├── capability.ref
   ├── CheckInSeason.ref
   ├── InSeason.ref
   ├── price.ref
   ├── recipe.ref
   ├── recommend.ref
   ├── reject.ref
   ├── selection.ref
   ├── taboo.ref
   └── which_season.ref
```


設置環境
-------------
- 環境需求
    - Python 3 or above
    - pip or pip3 is installed
- 安裝相關套件
    - 執行指令：`$ pip install -r requirements.txt`

建立 Discord Bot
-------------

啟用 Loki 服務
-------------
- 匯入ref
- 新增account.info

執行
-------------

引用資料
-------------

參考資料
-------------

聯絡資訊
-------------
