# Chinese Corrector Bot 華語病句修改機器人
## 華語吉Bot分
  Chinese Corrector Bot是基於真實的華語病句語料，使用者輸入華語句子後，經由Loki進行處理，判斷句子是否有誤和屬於哪種錯誤類型，再回覆使用者建議說法和錯誤之處，以提供使用者學習華語句子為目標。

# 檔案總覽

# Demo
- 必須先標註機器人@ChiCorrBot，並輸入「哈囉、嗨、你好」才可以開始使用喔！
- [實際操作示範](<https://youtu.be/eDiZ0xB37tw>)
  

# 環境設置
- Python 3.6+
- 安裝相關套件 requiremwnts.txt

# 建立account.info檔案
- __username__ 為註冊帳號的E-mail

```Python
{
"discord_token":"",
"username":"",
"articut_key":"",
"loki_key":""
}
```

# 建立Discord Bot
1. 進入[Discord開發者頁面](<https://discord.com/developers/applications/>)
2. 註冊後登入帳號
3. 點選 __New Application__
4. 輸入Bot的名稱後點選 __Add Bot__
5. 在 __TOKEN__ 點選 __Copy__
6. 填入account.info的 __discord_toke__ 欄位

# 啟動Loki服務
1. 進入[Droidtown](<https://www.droidtown.co/zh-tw/>)註冊並登入帳號
2. __服務資訊__ 點選 __Loki__
3. 點選 __開始使用Loki__
4. 輸入 __專案名稱__ 並建立
5. 進入專案後 __選擇檔案__
6. 選取ref的所有檔案並 __讀取意圖__
7. 點選左上角的小房子複製 __專案金鑰__
8. 填入account.info的 __loki_key__ 欄位

# Articut API
1. 進入[Droidtown](<https://www.droidtown.co/zh-tw/>)登入帳號
2. __服務資訊__ 點選 __Articut__
3. 複製 __API金鑰__
4. 填入account.info的 __articut_key__ 欄位

# 聯絡資訊
- 若您有其他建議或疑問，歡迎透過E-mail來信，謝謝。
- Joanne Chung : <joanne031913@gmail.com>