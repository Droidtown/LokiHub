# Hippo Chamber 
## 使用情境

**Hippo Chamber** 可以減少在大量文章中搜尋過濾文章的難度並且透過語意對話縮短找尋文章的時間。本專案用IOH網站上面分享的大量內容作為範例，只要在Line上加入 Hippo Chamber 好友，就可以用關鍵字找出最相關的文章。

#### IOH 背景

[IOH](https://ioh.tw/) 全名是 Innovation Open House 計畫，他是一個跨領域的公開個人經驗分享平台。

其主旨在將個人經驗大眾化，所以使用者可以在網頁上瀏覽別人的求學與工作經驗。

## 環境設定
- 本專案需求 ```python 3.6以上```
- 安裝本專案所需套件

  - ```bash
    pip install -r requirement.txt
    ```

- 註冊Loki帳號

  1. ​	到[卓騰語言科技 ](https://api.droidtown.co/)官網註冊會員並登入頁面。順利登入後進入Loki頁面。

     <img src="https://raw.githubusercontent.com/Joshua0128/dobby/main/img/DT_register.png" alt="註冊 圖示" width=400 />

     <img src="https://raw.githubusercontent.com/Joshua0128/dobby/main/img/DT_login.png" alt="登入 圖示"  width=400 />
  2. 取得取得username, lokikey填入 ```nlu/account.json```


### Line Bot 設定

1. 用line帳號登入 [LINE DEVELOPER](https://developers.line.biz/en/)
2. 建立新的 ***Provider*** ，名字隨意
3. 點選 ***Create a new channel***，名字是bot的名字唷!
4. 選擇 ***Messaging API***，有和使用者聊天的功能
5. 其他如 ***Description, Category*** 沒有很重要，依自己bot內容填寫
6. 下載 [app.py](https://github.com/Joshua0128/dobby/blob/main/app.py) 
7. LINE_ACCESS_TOKEN: 複製貼上Messaging API的***LINE token***
8. LINE_CHANNEL_SECRET : 複製貼上Basic Setting的 ***Channel secret***
9. 將***LINE token*** 和　***Channel secret***　填入```linebot.json```中

### Heroku 設定

1.  到 [Heroku](https://dashboard.heroku.com/login) 建立伺服器，右上角 ***Create new app*** 
2.  給個App name， Region只有美國和歐洲，選什麼都沒差因為離你都很遠XD

***

### 串接 Line 和 Heroku

1. 到 Heroku 你剛布屬好的伺服器，點右上角 **Open App**，他會打開一個網站，我們要取它的網址
2. 複製網址到 Line Developer 的 Messaging API 的 ***Webhook settings***貼上剛的網址
3. 貼上後記得在網址最後加上 **/callback** 例子: https://testbotxxxxxxx.herokuapp.com/callback
4. 最後點 ***Verify*** 且下面***Use Webhook*** 打開，就全部設定完成了! 

### 使用自定義的資料集
資料集格式如下
```
{
  [{
    title:"文件的標題",
    ref:"文件的連結",
    content:"放文檔內容",
    result_segmentation:" 放/文檔/斷詞/後/的/結果"
  },{
    ...
  }]
}
```
詳細格式可以參考 ```dataset/ioh_sample.json```

## 開始使用
您可以透過輸入LINE Bot ID或是掃QR Code加入好友。

LINE Bot ID: @726tbyzw </br>
QR Code </br>
<img src="https://raw.githubusercontent.com/Joshua0128/dobby/main/img/qrcode.png" width = 200 />

## 使用範例
1. 輸入你有興趣的系所或是職業內容
2. Line Bot會回傳dataset中相關聯的資料
<img src="https://raw.githubusercontent.com/Joshua0128/dobby/main/img/demo.png" width = 200 />

## 聯絡資料
若您有任何疑問，歡迎透過email聯繫我們
- Wei : waiting.hchs@gmail.com
- Emily Fang: emilyfun199701@gmail.com