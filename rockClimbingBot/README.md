# 台灣攀岩 Sport Climbing TW Bot
### 內容列表
- [Bot介紹](##Bot介紹)
- [專案目錄](##專案目錄)
- [環境設置](##環境設置)
- [Loki啟用說明](##Loki啟用說明)
- [Discord Bot建置](##DiscordBot建置)
- [使用者互動說明](##使用者互動說明)
- [參考資料](##參考資料)
- [作者](##作者)
## Bot介紹 
運動攀登，俗稱攀岩，近年來獲得越來越多的關注，亦於2021年東京奧運，首度列為正式運動項目。伴隨著這股熱潮，「台灣攀岩」Bot 應運而生，其提供了想在台灣攀岩的新手會遇到的，各種疑難雜症的解答，舉凡攀岩需要的裝備、治裝花費、攀岩規則、岩點特色等，都可詢問，即便是老手，也可從對話中快速取得各縣市岩館的資訊。歡迎對攀岩有興趣的朋友下載使用！

## 專案目錄
```
.
├── README.md
├── data        #資料集
│    ├── climbingGym.csv
│    ├── defaultResponse.json
│    ├── rocks.json
│    └── what_is.json
├── intent     #16種Loki意圖分析
│    ├── Loki_chat.py
│    ├── Loki_equipment_list.py
│    ├── Loki_equipment_price.py
│    ├── Loki_equipment_whereGet.py
│    ├── Loki_equipment_yesNo.py
│    ├── Loki_gym_city.py
│    ├── Loki_gym_distance.py
│    ├── Loki_gym_howMany.py
│    ├── Loki_gym_name.py
│    ├── Loki_gym_price.py
│    ├── Loki_gym_time.py
│    ├── Loki_gym_yesNo.py
│    ├── Loki_location.py
│    ├── Loki_rock.py
│    ├── Loki_rules.py
│    ├── Loki_whatIs.py
│    ├── USER_DEFINED.json
│    └── Updater.py
├── ref       #於登入Loki並創建專案後讀取，即可更動原始意圖
│    ├── chat.ref
│    ├── equipment_list.ref
│    ├── equipment_price.ref
│    ├── equipment_whereGet.ref
│    ├── equipment_yesNo.ref
│    ├── gym_city.ref
│    ├── gym_distance.ref
│    ├── gym_howMany.ref
│    ├── gym_name.ref
│    ├── gym_price.ref
│    ├── gym_time.ref
│    ├── gym_yesNo.ref
│    ├── location.ref
│    ├── rock.ref
│    ├── rules.ref
│    └── whatIs.ref
├── rockClimbing.py         #Loki主程式
├── Discord_rockClimbing.py #discord連線
├── rockClimbingFunc.py     #所有會用到的自定義函式
└── rockClimbingNLUmodel.py #連接Loki主程式和discord的NLU模型
```
## 環境設置
- 環境需求
    - Python 3.6+ (此 Bot 以 python 3.7 製作)
- 套件安裝
    - `pip3 install ArticutAPI`
    - 其他常用套件：pandas, random, re, datetime
## Loki啟用說明
1. 註冊並登入[卓騰語言科技AI](https://api.droidtown.co/login/)
2. 點選 `Loki` -> `開始啟用Loki` 進入Loki控制台
3. 輸入專案名稱並點選 `建立專案`
4. 點擊進入設立完成之專案
5. 點擊 `選擇檔案` ->選擇 `.ref` 檔->點選 `讀取意圖` 匯入檔案<br>⚠一次最多可匯10筆，共16筆，最少需分兩次匯入
6. 點選畫面左上角房子圖示，回到 Loki控制台，點選 `複製` 專案金鑰
7. 在 rockClimbingBot 資料夾底下創建 `account.info` 檔案，並輸入以下內容
```
{
    "discord_token":"",
    "username":"--填入Loki註冊信箱--",
    "lokiKey":"--填入專案金鑰--",
}
```
## DiscordBot建置
1. 註冊並登入 Discord 帳號
2. 進入[Discord Developers](https://discord.com/developers/applications)
3. 點擊畫面右上方的 `New Application` ->填上 Bot 名稱-> 點擊 `create` 建立 Discord Bot
4. 點選右方欄位 SETTINGS 中的 `Bot` ->點選 `Add Bot`
5. 點選右方欄位 SETTINGS 中的 `OAuth2` ->點選 `URL Generator`
6. 於 SCOPES 欄位勾選「bot」
7. 於 BOT PERMISSIONS 欄位勾選「Send Messages」、「Embed Links」、「Attach Files」及「Read Message History」
8. 複製 GENERATED URL 到新分頁中貼上，選擇 Bot 欲加入之伺服器，即完成添加
9. 點選 SETTINGS 中的 `Bot` ->點選 `Reset Token`
10. 將 Token 貼至 `account.info` 中
```
{
    "discord_token":"--填入token--",
    "username":"",
    "lokiKey":"",
}
```
## 使用者互動說明
完成上述程序後，執行 `python3 Discord_rockClimbing.py` 即可開始與 Bot 互動<br>
<互動示例><br>
[![youtube img]("https://img.youtube.com/vi/UiLrlxRH-aU/0.jpg")](https://www.youtube.com/watch?v=UiLrlxRH-aU)
<br>
❗與Bot對話不要忘了@它哦❗<br>

## 參考資料
- 岩館資訊：
  - [轟菌體能](https://shenlee799.com/climbinggyms-taiwan/) 
  - [CRAG FLOW](https://willisclimber.com/taiwanboulderinggym/)
- 岩點資訊及圖片：
    - [HHH-VOCUS](https://vocus.cc/article/62316539fd897800011dbd54)
- 規則及術語：
    - [運動視界](https://www.sportsv.net/articles/86153)
    - [Yinggan Chen-Medium](https://yinggan.medium.com/%E7%B0%A1%E6%98%93%E6%94%80%E5%B2%A9%E8%A1%93%E8%AA%9E%E4%B8%80%E6%AC%A1%E4%BA%86%E8%A7%A3-223387bf04e7)
- NLU模型＆Loki操作：
    - [Droidtown Linguistic Tech](https://api.droidtown.co/document/#Loki_9)
    - [LokiHub](https://github.com/Droidtown/LokiHub/tree/main/StatsBot)

## 作者
[Ansley Hung](https://github.com/Chilinhung) <br>
倘若使用上有任何疑問，歡迎提出 pull request 或透過 <a href="https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox">Email</a>  聯繫
