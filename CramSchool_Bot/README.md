# CramSchool Bot

CramSchool Bot 是一個設計來幫助補習班處理家長查詢的機器人，能夠自動回應有關學生成績和表現的問題，減少教師的負擔。

## 功能
- 家長可以即時查詢小孩成績
- 家長可以得到老師對小孩的評語
- 補習班櫃檯更新資料庫，即可讓家長做查詢

## 使用工具
- python: 撰寫背後所有程式碼
- flask, ngrok: 創造與Line連結的webhook網址
- Loki: 分析使用者傳入的訊息
- pandas: 讀取補習班端的Excel檔案
- Excel: 適合補習班端記錄學生與課程資料

## 簡略步驟
### 創立一個Line Chatbot
- 請參考：https://steam.oxxostudio.tw/category/python/example/line-developer.html
- 工具：N/A, 在Line的後台登入設定即可
  *取得access_token與secret*
### 建立webhook
- 什麼是webhook?
![image](https://github.com/user-attachments/assets/24e7e97f-3abe-4f1d-a427-32509c45f94b)
簡單來說，webhook 就像一座橋樑，讓你可以**連結**Chatbot的訊息與你的python聊天程式
- 請參考 https://steam.oxxostudio.tw/category/python/example/line-webhook.html
- 工具：Flask, Ngrok, python
  *我的webhook.py便是一個示範檔案；他接受使用者輸入的訊息，以及產出相對應回覆給使用者*
### Loki: 使用我的 intent 與 Excel 檔（作為示範）
- 取得Loki的api_key與loki_key
- 從CramSchool_Bot.py import execLoki 到 webhook.py: 在webhook.py中透過Loki分析使用者訊息的意圖
- 工具：python, Loki
  *這一步後，應該要能使用Loki分析使用者輸入的訊息*
### 讀取補習班端Excel與回覆
- 用pandas在webhook.py讀取你欲讀取的Excel檔案（我這裡是「DT 補習班」作為一個示範檔）
- 然後依照Loki讀取到的意圖，設計回覆
- 工具：python, pandas
### 運行 webhook.py
- 家長就可以像以下影片與Line Chatbot 互動囉！


https://github.com/user-attachments/assets/7c151e44-7979-48fd-9124-c6aa36a5f82d


## 聯絡資訊
- 如果有任何問題，請聯絡我：Randy Wang(youthrw@gmail.com)，歡迎與我交流
