# 當季食材小幫手—食材問題諮詢機器人

Bot 可以解決的問題
-------------

DEMO
-------------

檔案總覽/目錄
-------------
```
.
├── ingredient_bot.py  # main program，執行以啟動 bot，處理與 discord 間的互動
├── Loki.py            # 主要使用到 function runLoki 
├── model.py           # NLU model 以及相關的 function
├── README.md
├── requirements.txt
│  
├─info 
│  ├── ingredient.json # 紀錄每個月份的當季食材
│  └── inSeason.json   # 紀錄每個食材的作法、挑法與禁忌
│      
├─intent # 所有的 intent 都放在這邊
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
└─ref # 啟用 Loki 服務時，需要將裡面的所有檔案匯入 Loki project 中
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
1. 登入後進入 [Loki 控制台]([https://](https://api.droidtown.co/loki/))
2. 輸入專案名稱，點選 `建立專案`
3. 點選剛建立完成的專案名稱以進入專案
4. 點選 `選擇檔案` > 選擇所有 ref 內的檔案 > 點選 `讀取意圖`
5. 點選左上角房子圖示，回到 [Loki 控制台]([https://](https://api.droidtown.co/loki/))，點選 `複製` 專案金鑰
6. 將複製下來的金鑰貼上到檔案 account.info 中：
```
{
    "username" : " ***輸入USERNAME(註冊信箱)*** ",
    "apikey_ing" : " ***將專案金鑰貼到這裡*** ",
    "discord_token": ""
}
```

執行以啟動 Ingredient Bot / 當季食材小幫手
-------------
- 執行指令：`$ python ingredient_bot.py`

引用資料
-------------

參考資料
-------------

聯絡資訊
-------------
若您還有其他任何的疑問，或是對 Loki 與食材相關的問題有興趣 

歡迎透過E-mail聯繫，謝謝 

Joe Huang：[joehuangx@gmail.com](mailto:joehuangx@gmail.com)      

Lisi Yang：[lisi16810@gmail.com](mailto:lisi16810@gmail.com)







