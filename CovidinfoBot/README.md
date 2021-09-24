# Covid_Info_Bot，關注台灣疫情的最佳幫手!
### 你是否曾經覺得普通點擊資訊的聊天機器人非常不人性化呢?
### 是時候該使用我們的Covid_Info_Bot了!
### 讓你每天關注最新台灣疫情訊息不間斷 :)
----

## 註冊Loki

1. 註冊卓騰語言科技帳號

![markdown](https://camo.githubusercontent.com/43cf42b70b8ee596c020683174f344c38d49aef480087a1dc4e05109dc1641f9/68747470733a2f2f692e696d6775722e636f6d2f5458647342657a2e706e67 "Sign up")

<!--- 改變markdown成html

<img src='https://camo.githubusercontent.com/43cf42b70b8ee596c020683174f344c38d49aef480087a1dc4e05109dc1641f9/68747470733a2f2f692e696d6775722e636f6d2f5458647342657a2e706e67 "Sign up"' width = 100px>
--->

2. 登入Loki

![markdown](https://camo.githubusercontent.com/c39301f6e30c412ac839534ffa4a8bfa02bcad9e3783e17878a6be1d1388383a/68747470733a2f2f692e696d6775722e636f6d2f4c496152544a522e706e67 "log in")

----
## 安裝套件
- [ArticutAPI](https://pypi.org/project/ArticutAPI/)
- Python
  ```sh
  pip insatll ArticutAPI
  ```
## 快速上手
1. 登入[Loki](https://api.droidtown.co/loki/)
2. 建立`Covid_Info_Bot`專案
3. 在Github上clone此專案
    ```sh
    pip clone https://github.com/enjuichang/CovidInfoBot
    ```
4. 在`Covid_Info_Bot`的[Github](https://github.com/enjuichang/CovidInfoBot)上pull我們的`ref`檔
5. 進入專案後，下方選擇`ArticutModel`並依序點擊 `[瀏覽]` > 選擇`ref/Exchange.ref` > `[讀取意圖]` ，並進入意圖。
6. 讀取後，在每個intent內按下`[生成模型]`。
7. 完成後，在畫面最上面點擊左邊的「房子」圖示，回到專案頁。這裡有`Covid_Info_Bot`的專案金鑰。
8. 編輯`Covid_Info_Bot.py`:
   - USERNAME: 填入你的 Droidtown 使用者帳號 (email)
   - LOKI_KEY: 填入你產生的`Covid_Info_Bot`專案金鑰
9. 開始使用

## 使用者輸入範例
- 查詢 **XX疫苗副作用**:
    - 我想知道AZ疫苗副作用
- 查詢**XX疫苗在OO地區剩餘量**:
    - 我想知道Moderna在台北的剩餘量
- 查詢**XX類族群**:
    - 我想知道第一類族群

## 檔案說明
```
│
├── README.md             <- 最高層的README
│
├── intent
│   ├── intents           <- 透過Loki處理utterance至intent的Python檔
│   └── Updater.py        <- 更新Loki intents (請詳閱Loki說明).
│   
├── json                  <- 資料儲存
│
├── ref                   <- 儲存最新版本Loki intents的.ref檔
│
├── covid_info_bot.py     <- 最主要使用Loki處理語句的Python檔
│
├── discord_bot.py        <- 回傳、處理資料並連接至Discord的Python檔
│
├── vaccine_stock_api.py  <- 連接至covid-19.nchc.org.tw資料庫並回傳結果的Python檔
│
└── requirements.txt      <- 使用環境說明
```
---
## 作者
- [張恩睿Enjui Eric Chang](https://github.com/enjuichang)
- [Shi Shan Liu](https://github.com/ShiShanLiu)

## English Version

### Have you ever thought that "clicking" is not the way you speak with a "chat" bot?
### If you felt that way, then it's time for you to use our Covid_Info_Bot!
### We let you know the latest news on the COVID-19 information here in Taiwan :)
----

## Register for Loki

1. Register an account on Droidtown

![markdown](https://camo.githubusercontent.com/43cf42b70b8ee596c020683174f344c38d49aef480087a1dc4e05109dc1641f9/68747470733a2f2f692e696d6775722e636f6d2f5458647342657a2e706e67 "Sign up")

2. Log into Loki

![markdown](https://camo.githubusercontent.com/c39301f6e30c412ac839534ffa4a8bfa02bcad9e3783e17878a6be1d1388383a/68747470733a2f2f692e696d6775722e636f6d2f4c496152544a522e706e67 "log in")

## Download Packages
- [ArticutAPI](https://pypi.org/project/ArticutAPI/)
- Python
  ```sh
  pip insatll ArticutAPI
  ```
## Getting Started
1. Log into [Loki](https://api.droidtown.co/loki/).
2. Create a `Covid_Info_Bot` project.
3. Clone this repository on Github.
    ```sh
    pip clone https://github.com/enjuichang/CovidInfoBot
    ```
4. Pull `.ref` files from `Covid_Info_Bot` on [Github](https://github.com/enjuichang/CovidInfoBot).
5. After entering the project page, select the `ArticutModel` and click on `[瀏覽]` > choose `ref/Exchange.ref` > `[讀取意圖]` in order to enter the intent.
6. After reading, every click `[生成模型]` in every intent.
7. When finished, click the "house" button on the upper left side of your screen to got back to the Project page. There has the `Covid_Info_bot` project key.
8. Edit `Covid_Info_Bot.py`:
   - USERNAME: Enter your Droidtown account (email)
   - LOKI_KEY: Enter your `Covid_Info_Bot` project key
9. You're good to go

## Input Example
- Search for the **side effect of XX vaccine**:
    - 我想知道AZ疫苗副作用
- Search for the **number of XX vaccine in location OO**:
    - 我想知道Moderna在台北的剩餘量
- Search for information of **XX group**:
    - 我想知道第一類族群

## 檔案說明
```
│
├── README.md             <- The top-level README for developers using this project.
│
├── intent
│   ├── intents           <- Python files that process utterance to intent via Loki.
│   └── Updater.py        <- Update Loki intents (Please check Loki documentation).
│   
├── json                  <- Storage of data.
│
├── ref                   <- .ref files that stores the version of Loki intents.
│
├── covid_info_bot.py     <- Main python file that process and connect to Loki.
│
├── discord_bot.py        <- Python file that returns result, process and connect to Discord.
│
├── vaccine_stock_api.py  <- Python file that connects to covid-19.nchc.org.tw database and results.
│
└── requirements.txt      <- The requirements file for reproducing the analysis environment.
```
---
## Authors
- [Enjui Eric Chang](https://github.com/enjuichang)
- [Shi Shan Liu](https://github.com/ShiShanLiu)


