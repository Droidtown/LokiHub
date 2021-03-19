# Line ChatBot 加入方法
## 目錄
1. [Intent](https://github.com/milanochuang/transportationBot/tree/master/Line/intent)
2. [line_app](https://github.com/milanochuang/transportationBot/blob/master/Line/line_app.py)
3. [line_sdk](https://github.com/milanochuang/transportationBot/blob/master/Line/line_sdk.py)
4. [LokisTransportationBot](https://github.com/milanochuang/transportationBot/blob/master/Line/LokisTransportationBot.py)
## 在這裡你可以知道：
* [環境設定與需求](#環境設定與需求)
* [如何建立一個LineBot](#如何建立一個LineBot)
* [如何取得Token](#如何取得Token)
## 環境設定與需求
* ### 程式語言版本
    * Line Bot 需要 Python3.6+ 才跑得起來喔
## 如何建立一個Line Bot
1. 首先，你要先有個Line帳號（只要是台灣人應該都有吧？🤔）
2. 登入[LINE DEVELOPER](https://developers.line.biz/zh-hant/)
3. 請選擇Product中的Message API

![](https://i.imgur.com/cZ03aFx.png)

4. 按下Start Now

![](https://i.imgur.com/Mv2wGA7.png)

5. 填入基本資訊
    * Provider: 填入你自取的名字，這不是機器人的名字，不用擔心
    * Channel Name: 這就是機器人的名字，想個有趣又好記的名字吧
    * Channel Description: 描述你的機器人在幹嘛
    * Category: 選擇聊天機器人服務的種類
    * Subcategory: 選擇細項的服務內容 
## 如何取得Token
1. 選取**Basic Setting**，並將LINE Secret貼到[line_app.py](https://github.com/milanochuang/transportationBot/blob/master/Line/line_app.py)中，```LINE_CHANNEL_SECRET = "" ""```的```""```內
2. 選取**Messaging API**，並將LINE token貼到[line_app.py](https://github.com/milanochuang/transportationBot/blob/master/Line/line_app.py)中，```LINE_ACCESS_TOKEN = ""```的```""```內
## 建立伺服器
1. 建立LineBot也需要建立伺服器，可將聊天機器人放入Heroku伺服器，並將伺服器網址放入Messaging API的Webhook URL中
2. Webhook顯示成功後，聊天機器人就完成囉！

:bulb: 記得將data裡的三個檔案跟thsr_bot放在同一個資料夾再執行喔！