# Discord ChatBot 加入方法
## 目錄
1. [Intent](https://github.com/milanochuang/transportationBot/tree/master/Discord/intent)
2. [thsr_bot](https://github.com/milanochuang/transportationBot/blob/master/Discord/thsr_bot.py)
3. [LokisTransportationBot](https://github.com/milanochuang/transportationBot/blob/master/Discord/LokisTransportationBot.py)
## 在這裡你可以知道：
* [環境設定與需求](#環境設定與需求)
* [如何建立一個DiscordBot](#如何建立一個DiscordBot)
* [如何在Discord上創建一個自己的伺服器](#如何在Discord上創建一個自己的伺服器)
* [如何取得Token](#如何取得Token)
## 環境設定與需求
* ### 程式語言版本
    * Discord Bot 需要 Python3.6+ 才跑得起來喔
* ### 所需套件
    * [Discord](https://pypi.org/project/discord.py/)
```shell=
$ pip install -U discord.py
```
## 如何建立一個Discord Bot
1. 帳號
2. 應用程式
3. 機器人
### 更多資訊：[How to Make a Discord Bot in Python](https://realpython.com/how-to-make-a-discord-bot-python/)
## 如何在Discord上創建一個自己的伺服器
1. 此時，回到你的Discord App，選取右邊有“＋”的「新增一個伺服器」
2. 為你所創建的伺服器取名，即完成創建伺服器了！
### 創建完機器人之後，應該要出現這樣的畫面
![](https://i.imgur.com/Dxx0qiD.png)
圖片來源：[Real Python](https://realpython.com/how-to-make-a-discord-bot-python)
## 如何取得Token
* 按照您的需求，勾選於OAuth2的核選方塊後...
* 複製在核選方塊下方的認證網址（URL）並貼入瀏覽器執行
* 到Bot/BUILD-A-BOT，並複製下方的TOKEN
* 將Token貼入[thsr.bot](https://github.com/milanochuang/transportationBot/tree/master/Discord)中的```DISCORD_TOKEN=""```再執行，你的機器人就上線囉！

:bulb: 記得將data裡的三個檔案跟thsr_bot放在同一個資料夾再執行喔！