# README
## 目錄

1. [Intent](https://github.com/Intern-CD/SpendThrift_bot/tree/main/SpendThrift_bot/intent)
2. [SpendThrift_bot](https://github.com/Intern-CD/SpendThrift_bot/blob/main/SpendThrift_bot/SpendThrift_bot.py)

## 在這裡你可以知道：

- [環境設定與需求](##環境設定與需求)
- [如何建立一個DiscordBot](##如何建立一個DiscordBot)
- [如何在Discord上創建一個自己的伺服器](##如何在Discord上創建一個自己的伺服器)
- [如何取得Token](#如何取得Token)

## 環境設定與需求

### 程式語言版本
- Python3.6以上 
### 所需套件
- Discord
```shell=
$ pip install -U discord.py
```

## 如何建立一個Discord Bot
歡迎閱讀[Discord document](https://discordpy.readthedocs.io/en/stable/index.html)

## 如何在Discord上創建一個自己的伺服器
1. 此時，回到Discord App，選取右邊有“＋”的「新增一個伺服器」
2. 為你所創建的伺服器取名，即完成創建伺服器了！

### 創建完機器人之後，應該要出現這樣的畫面
![創建後的畫面](https://i.imgur.com/Dxx0qiD.png)
圖片來源：[Real Python](https://realpython.com/how-to-make-a-discord-bot-python)

## 如何取得Token
- 按照需求，勾選於OAuth2的核選方塊
- 複製在核選方塊下方的認證網址（URL）並貼入瀏覽器執行
- 到Bot/BUILD-A-BOT，並複製下方的TOKEN
- 到`discord`資料夾中，建立新的文件`account.info`，並輸入：
```
{	
    "discord_token":"TOKEN貼在這"
}
```
