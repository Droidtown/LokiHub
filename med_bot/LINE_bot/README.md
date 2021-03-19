# LINE 檔案使用說明
## 1. 檔案內容
在這個資料夾中有一個資料夾與三個主要的.py檔案: `intent`,`line_app.py`,`line_sdk.py`,`reference.py`, `med_bot_for_Loki.py`

----
## 2. 環境設定
如果想要在LINE上面建構自己的chatbot，請參考以下步驟

1. 請至 LINE DEVELOPER (https://developers.line.biz/zh-hant/) ，以您的Line帳號登入
2. 登入之後，按product，選擇 Message Api ，並按下 START

<img src="https://upload.cc/i1/2021/03/12/31OUhy.png" width="50%" height="50%" />

<img src="https://upload.cc/i1/2021/03/12/i9gxDm.png" width="50%" height="50%" />

3. create api 中設定以下5項必要資訊，了解LINE Official Account Terms of Use 和 LINE official Account API Terms of Use 之後，點下Create 
      
    - Provider: 請選擇 create a new provider，然後下面的名字可以自己取名 (以本圖為例，取作 MED_BOT) 
   
<img src="https://upload.cc/i1/2021/03/12/s3jnXt.png" height="50%" />

      
   - Channel name: 請自行取名 channel name 這裡是您LINE 的名字 
   
   - Channel description: 請描述此聊天機器人用途
   
   - Category: 請選擇您的聊天機器人的服務內容範圍 (e.g. 醫療相關) 
   
   - Subcategory: 選擇細項的內容服務
   

4. 在Basic setting 中可以找到您的 LINE secret，請貼到 line_app 檔案取代原本 accountInfoDICT["LINE_CHANNEL_SECRET"] (line 15)

例如 : LINE_CHANNEL_SECRET = "your secret"

5. 在Messaging API 中可以到到您的 LINE token，請貼到 line_app 檔案取代原本 accountInfoDICT["LINE_ACCESS_TOKEN"] (line 14)

例如 : LINE_ACCESS_TOKEN   = "your token"

6. 這邊需要一個Server 放在LINE DEVELOPER裡面，這邊可以參考 Heroku，如果已經可以把這個聊天機器人放入那個server，就把這個server 的網誌放在 Messaging API 下 WebHook 中，建議參考書籍 LINE Bot by Python 全攻略 (作者饒孟桓)

<img src="https://upload.cc/i1/2021/03/12/rb2x0V.png" width="50%" height="50%" />

7. 如果 Web hook 是顯示成功，那這樣這個聊天機器人就可以在LINE中運作了 


----

## 3. 檔案內容
###  `intent`資料夾
這個資料夾存取了兩個intent，分別是body_part以及symptom，其功能是依據身體部位(body_part)或身體病症(symptom)

### `line_app.py`  
本程式用於連接 `med_bot_for_Loki.py`與line的聊天機器人。

### `line_sdk.py`
本程式置放LINE chatbot 需要的程式必要內容


### `med_bot_for_Loki.py`
本程式用於串接Loki的intents，主要有三個functions:`RunLoki`、`FindDepartment`以及`Result`，`RunLoki`功能為與線上Loki進行連結並偵測意圖，也會進一步回傳使用者標記的參數。`FindDepartment`功能為將`RunLoki`回傳的參數與`reference.py`裡面之字典檔進行比對，以找出病症或身體部位所對應知科別。`Result`則將最後的結果存成另一個字典檔，並於`med_bot_for_discord.py`中被imported。

### `reference.py`
本檔案儲存所有在前述兩張script所需的LIST與DICT。


