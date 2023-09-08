# **LDS_bot (Language Development Screening bot)**

* 是以臺北市學齡前兒童發展檢核表(中文)為設計藍圖的 **「學齡前孩童語言發展篩檢bot」**
* 依不同年齡層發展里程碑進行語言能力篩檢
* 整合收蒐到關於孩童現階段語言表現的資料後給予建議
* LDS_bot是就使用者回覆關於孩童當下語言發展表現的結果進行簡易yes/no篩檢，關於孩童完整的語言評估與診斷則需由專業醫療人員執行

# **檔案總覽**


# **操作說明**
### **環境設置**
* Python 版本：

### **套件安裝**
* pip3 install ArticutAPI
* logging
* re
* json
* os

### **Pull LDS_bot**
* 將本專案pull至本地電腦

### **啟用 Loki**
* 註冊/登入 [卓騰語言科技 AI -> NLP](https://api.droidtown.co/login/)
* 點選 Loki 
* 開始使用 Loki<br>
  <img src="https://github.com/FishInBed/LDS_bot/blob/main/image/Loki_1.png" width="600" />
* 建立專案
  共計九個，分別為：Under_1, Above_1, Above_2, Above_3, Above_4, Above_5, Above_6<br>
  <img src="https://github.com/FishInBed/LDS_bot/blob/main/image/Loki_2.png" width="600" />
* 點擊進入已設定之專案
* 點擊下方「選擇檔案」並匯入該專案所屬的所有.ref檔<br>
  <img src="https://github.com/FishInBed/LDS_bot/blob/main/image/Loki_3.png" width="600" />
* 點擊進入每個意圖進行「部署模型」<br>
  <img src="https://github.com/FishInBed/LDS_bot/blob/main/image/Loki_4.png" width="600" />

### **建立account.info檔案**
* 在 LDS_bot 資料夾底下建立 account.info.txt 檔案，並輸入下列內容<br>
  <img src="https://github.com/FishInBed/LDS_bot/blob/main/image/account.info.png" width="600" />

### **啟用 Discord Bot**
* 註冊/登入 Discord
* 連至 [developers/applications](https://discord.com/developers/applications) 
* 點選畫面右上角的「New Application」
* 填入 Bot 名稱後點選 create<br>
  <img src="https://github.com/FishInBed/LDS_bot/blob/main/image/discord_1.png" width="600" />

* 「Copy」下方的Token並將其存至 account.info.txt 中
  
* 左側選單中點選「OAuth2」-->點選「bot」<br>
  <img src="https://github.com/FishInBed/LDS_bot/blob/main/image/discord_2.png" width="600" />

* 左側選單中點選「OAuth2」-->BOT PERMISSIONS勾選「Send Messages」、「Manage Messages」、「Embed Links」、「Read Message History」<br>
  <img src="https://github.com/FishInBed/LDS_bot/blob/main/image/discord_3.png" width="600" />

* 左側選單中「BOT」-->features it needs勾選勾選「Send Messages」、「Manage Messages」、「Embed Links」、「Read Message History」<br>
  <img src="https://github.com/FishInBed/LDS_bot/blob/main/image/discord_4.png" width="600" />

* 複製 BOT 的連結至指定的伺服器
* 執行Discord_bot_LDS_bot.py


# **聯絡資訊**
若有任何問題，歡迎email聯繫<br>
[Cathy Yu](c5227c@gmail.com)<br>
[Ruo-Chi Yao](kireiyvette@gmail.com)
