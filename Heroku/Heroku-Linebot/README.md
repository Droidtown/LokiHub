# Linebot in Heroku

## 事前準備

### 1. 註冊 Heroku 帳號

在 [Heroku 網站](https://www.heroku.com)註冊帳號並登入。

### 2. 安裝 Heroku CLI 工具

下載 [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) 或使用指令進行安裝。

![](./img/img01.png)

### 3. 建立 Linebot

請先至 [Line Developers](https://developers.line.biz/zh-hant/) 註冊帳號，進入 `LINE Developers Console`，準備開始建立 bot。

![](./img/img02.png)

建立一個 `Provider`，接著點擊 `Create a new channel`，並選擇 `Messaging API`。

![](./img/img03.png)

進入 bot 點擊上方的 `Messaging API`，點擊 `Auto-reply messages` 右側的 `Edit`，回應模式設爲`聊天機器人`，自動回應訊息設爲`停用`，Webhook 設爲`啟用`，到此設定完成。

![](./img/img04.png)

### 4. 設定 line_app.py

打開 `line_app.py`，填入你的 `LINE_ACCESS_TOKEN` 及 `LINE_CHANNEL_SECRET`，並調整 35 - 37 行客製化內容。

![](./img/img05.png)
![](./img/img06.png)

```python
LINE_ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
LINE_CHANNEL_SECRET = "YOUR_CHANNEL_SECRET"
...
# 這裡輸入客製化內容
resp = "我是一個機器人"
linebot.respText(dataDICT["replyToken"], resp)
```

## 開始使用

### 1. 建立 App

登入 [Heroku 網站](https://www.heroku.com)後，點擊右上角的 `New` 按鈕，並選擇 `Create new app`。

![](./img/img07.png)

`App name` 會決定 App 的網址 (Ex. https://simple-linebot.herokuapp.com/)，填入想要的 `App name` 後點擊 `Create app`。

![](./img/img08.png)

建立完成後將會看到以下畫面，說明使用現有 repo 或建立新 repo，本教學以建立新 repo 爲例。

![](./img/img09.png)

### 2. 佈署 App (以 Heroku Git 爲例)

Heroku 最少需要佈署四個檔案

- **Procfile**: 啟動 Web Service 的指令。
- **requirements.txt**: Web Service 需要使用到的套件。
- **runtime.txt**: 指定使用的 Python 版本。
- **app.py**: 主程式 (這裡使用 flask)。

首先打開終端機移動至目標目錄 (simple-linebot) 下輸入 `heroku login` 登入 Heroku CLI，登入後輸入 `git init` 及 `heroku git:remote -a YOUR_APP_NAME` 初始化 Heroku git。

```sh
$ cd YOUR_PROJECT
$ heroku login
$ git init
$ heroku git:remote -a YOUR_APP_NAME
```

![](./img/img10.png)

將佈署所須依次輸入 `git add YOUR_FILE`，再輸入 `git commit -m "YOUR_COMMIT"`，最後輸入 `git push heroku master` 進行佈署。

```sh
$ git add Procfile
$ git add requirements.txt
$ git add runtime.txt
$ git add line_app.py
$ git add line_sdk.py
$ git commit -m "Init a Linebot."
$ git push heroku master
```

![](./img/img11.png)

### 3. 測試 Line Webhook

在 [Line Developers](https://developers.line.biz/zh-hant/) 中進入 bot 的 `Messaging API` 標籤，在 `Webhook URL` 填入 Heroku App 網址 `https://{YOUR_APP_NAME}.herokuapp.com/`，並點擊 `Verify` 測試是否成功接通。

![](./img/img12.png)