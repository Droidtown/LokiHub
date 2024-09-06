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

## 手把手教學
### 創立一個Line Chatbot
- 請參考：https://steam.oxxostudio.tw/category/python/example/line-developer.html
- 工具：N/A, 在Line的後台登入設定即可
### 建立webhook
- 什麼是webhook?
![image](https://github.com/user-attachments/assets/24e7e97f-3abe-4f1d-a427-32509c45f94b)
簡單來說，webhook 就像一座橋樑，讓你可以**連結**Chatbot的訊息與你的python聊天程式
- 請參考 https://steam.oxxostudio.tw/category/python/example/line-webhook.html
- 工具：Flask, Ngrok, python
### Loki: 使用我的 intent 與 Excel 檔（作為示範）
- 取得Loki
  
  
