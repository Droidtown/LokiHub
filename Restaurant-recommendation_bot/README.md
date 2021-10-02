# Restaurant-recommendation_bot - 幫你推薦在地美食的機器人

## **背景**
你是否開開心心規劃要到外縣市遊玩時，雖然有大概查過資料，但還是有些隱藏的在地小吃想要嘗試，卻不知道要從何下手?
即使聽過該餐廳，但對該店的評價及住址還是有所不確定，又不想花時間看網路上大量的評價是不是適合自己。
只要在Discord上加入RestaurantAndHotel_bot，就能以自然語言找尋你要的餐廳的資訊喔。

## **專案列表**
+ 目錄
+ 環境建立
+ 使用說明
+ 使用者輸入範例
+ 作者及聯絡資訊

## **目錄**
Restaurant-recommendation_bot的Repository包含以下內容：

1. [restaurant_domain.json](https://github.com/WuSiangRu/LokiHub/blob/main/Restaurant-recommendation_bot/data/restaurant_domain.json)
2. [trip_discord_bot.py](https://github.com/WuSiangRu/LokiHub/blob/main/Restaurant-recommendation_bot/trip_discord_bot.py)
3. [ref](https://github.com/WuSiangRu/LokiHub/tree/main/Restaurant-recommendation_bot/ref)
4. [RestaurantAndHotel_bot](https://github.com/WuSiangRu/LokiHub/blob/main/Restaurant-recommendation_bot/RestaurantAndHotel_bot.py)

## **環境建立**
### **註冊帳號**
1. 請到 [卓騰語言科技](https://api.droidtown.co/) 官方網站註冊帳號並登入頁面
2. 註冊會員

![](https://raw.githubusercontent.com/WuSiangRu/RestaurantAndHotel_bot/main/pic/001.JPG "001")

3. 註冊成功後登入會員

![](https://raw.githubusercontent.com/WuSiangRu/RestaurantAndHotel_bot/main/pic/002.JPG "002")

4. 登入會員之後，選擇在「服務資訊」區塊底下第四個圖示並點選「開始使用Loki」

![](https://raw.githubusercontent.com/WuSiangRu/RestaurantAndHotel_bot/main/pic/003.JPG "003")

`使用本專案python環境建議版本3.6+`
1. 安裝該專案會使用的module
```
pip install ArticutAPI
```
```
pip install DateTime
```
## **使用說明**
### **Articut及Loki使用說明**
+ 登入帳號:[卓騰語言科技](https://api.droidtown.co/)
+ 複製Articut API金鑰
+ 選擇Loki應用後建立專案(英文名稱)
+ 複製Loki專案金鑰
+ 編輯`account.info`
```
{
"username":"your account",  #你的帳號
"articut_api_key":"your articut key",  #你的articut金鑰
"loki_api_key":"your loki key",  #你的loki專案金鑰
"discord_token": "your bot token"  #你的discord bot的token
}
```
+ 欲使用已建立好的Loki意圖(intent)，請點選 ref 資料夾 [如何讀取ref檔](https://api.droidtown.co/document/#Loki_3)

### **Discord使用說明**
#### **使用檔案**
1. [intent](https://github.com/WuSiangRu/RestaurantAndHotel_bot/tree/main/intent)
2. [RestaurantAndHotel_bot.py](https://github.com/WuSiangRu/RestaurantAndHotel_bot/blob/main/RestaurantAndHotel_bot.py)
3. [trip_discord_bot.py](https://github.com/WuSiangRu/RestaurantAndHotel_bot/blob/main/trip_discord_bot.py)

#### **環境設定**
+ python版本
    + python版本建議3.6+
+ 所需module
    + [Discord](https://pypi.org/project/discord.py/)
    
    `pip install -U discord.py`
#### **建立Discord bot**
如何建立Discord bot請參考 [How to Make a Discord Bot in Python](https://realpython.com/how-to-make-a-discord-bot-python/)
1. 建立好Discord Application後![](https://files.realpython.com/media/discord-bot-add-bot.4735c88ff16b.png "add_bot")

2. 將bot的token複製![](https://files.realpython.com/media/discord-bot-rename-bot.008fd6ed6354.png "copy_token")
以上圖片來源: [How to Make a Discord Bot in Python](https://realpython.com/how-to-make-a-discord-bot-python/)

3. 將複製好的token貼到`account.info`底下discord_token裡

## **使用者輸入範例**
在Discord以標記bot:@你的bot，就可以開始對話了。
1. 可以先問候bot![](https://raw.githubusercontent.com/WuSiangRu/RestaurantAndHotel_bot/main/pic/004.JPG "004")

2. 提供你現在所在的縣市地區(或捷運站)![](https://raw.githubusercontent.com/WuSiangRu/RestaurantAndHotel_bot/main/pic/005.JPG "005")

3. 從bot回覆的餐廳訊息裡選擇你要的餐廳名，並可詢問地址跟評價![](https://raw.githubusercontent.com/WuSiangRu/RestaurantAndHotel_bot/main/pic/006.JPG "006")

4. 使用者可詢問餐廳是否能預約，能的話bot就會詢問相關資訊![](https://raw.githubusercontent.com/WuSiangRu/RestaurantAndHotel_bot/main/pic/007.JPG "007")

5. 最後bot收集完預約的資訊，使用者再對bot回覆的訊息做確認![](https://raw.githubusercontent.com/WuSiangRu/RestaurantAndHotel_bot/main/pic/008.JPG "008")

## **作者及聯絡資訊**
Samuel Wu: 
+ Mail: sam253sam@gmail.com
+ GitHub: [GitHub](https://github.com/WuSiangRu)