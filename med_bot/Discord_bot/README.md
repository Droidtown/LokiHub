# Discord 檔案使用說明
## 1. 檔案內容
在這個資料夾中有一個資料夾與三個主要的.py檔案: `intent`,`med_bot_for_discord.py`,`med_bot_for_Loki.py`,`reference.py`

----
## 2. 環境設定

### 如果想要在discord上面建構自己的chatbot請參考以下連結: https://realpython.com/how-to-make-a-discord-bot-python
----

## 3. 檔案內容
###  `intent`資料夾
這個資料夾存取了兩個intent，分別是body_part以及symptom，其功能是依據身體部位(body_part)或身體病症(symptom)

### `med_bot_for_discord.py`
本程式用於連接`med_bot_for_Loki.py`與discord的聊天機器人。

### `med_bot_for_Loki.py`
本程式用於串接Loki的intents，主要有三個functions:`RunLoki`、`FindDepartment`以及`Result`，`RunLoki`功能為與線上Loki進行連結並偵測意圖，也會進一步回傳使用者標記的參數。`FindDepartment`功能為將`RunLoki`回傳的參數與`reference.py`裡面之字典檔進行比對，以找出病症或身體部位所對應知科別。`Result`則將最後的結果存成另一個字典檔，並於`med_bot_for_discord.py`中被imported。

### `reference.py`
本檔案儲存所有在前述兩張script所需的LIST與DICT。

## 4. 備註
`from account_info import accountInfoDICT`這行的意思是 import 進來 `account_info` 的py 檔，
這個檔案裡面可以存成一個叫做 `accountInfoDICT` 的 dictionary 放您們重要的金鑰



