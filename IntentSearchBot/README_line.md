#### Line ChatBot 一起蓋個酷Bot吧

#### 環境設定

Line Bot 需要 Python3.6+ 才跑得起來

***

- [ ] ##### Line

1. 用line帳號登入 [LINE DEVELOPER](https://developers.line.biz/en/)
2. 建立新的 ***Provider*** ，名字隨意
3. 點選 ***Create a new channel***，名字是bot的名字唷!
4. 選擇 ***Messaging API***，有和使用者聊天的功能
5. 其他如 ***Description, Category*** 沒有很重要，依自己bot內容填寫
6. 下載 [app.py](https://github.com/Joshua0128/dobby/blob/main/app.py) 
7. LINE_ACCESS_TOKEN: 複製貼上Messaging API的***LINE token***
8. LINE_CHANNEL_SECRET : 複製貼上Basic Setting的 ***Channel secret***

***

- [ ] **Heroku**

1. 到 [Heroku](https://dashboard.heroku.com/login) 建立伺服器，右上角 ***Create new app*** 
2. 給個App name， Region只有美國和歐洲，選什麼都沒差因為離你都很遠XD

***

- [ ] **串接 Line 和 Heroku**

1. 到 Heroku 你剛布屬好的伺服器，點右上角 **Open App**，他會打開一個網站，我們要取它的網址
2. 複製網址到 Line Developer 的 Messaging API 的 ***Webhook settings***貼上剛的網址
3. 貼上後記得在網址最後加上 **/callback** 例子: https://testbotxxxxxxx.herokuapp.com/callback
4. 最後點 ***Verify*** 且下面***Use Webhook*** 打開，就全部設定完成了! 

