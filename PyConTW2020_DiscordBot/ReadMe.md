# PyConTW2020_DiscordBot PyCon 2020 Discord 機器人

### 快速上手

### 1 建立 Discord Bot 環境
1. 把 template.env 檔案打開，在 [Discord Developer Portal](https://discord.com/developers/application) 中取得的 Bot Token 取代 **{DISCORD_BOT_TOKEN}** (包括左右兩個大括號也一起取代掉)。注意等號前後不留空格。

2. 完成後，檔案另存為 .env 。(注意！在 Linux/Mac 下，以「點」開頭的檔案預設是隱藏檔。)

### 2 建立 Loki Bot
1. 登入 [Loki 控制台](https://api.droidtown.co/loki/)。

2. 在 Loki 控制台中新建一個專案`PyConTW2020_DiscordBot`，並進入專案。

3. 在專案下方選擇`ArticutModel`並依序點擊 [瀏覽] > 選擇`ref/GetVenueAddress.ref` > [讀取意圖] ，並進入意圖。

4. 在`5. 生成模型`區塊中點擊 [生成模型 (GetVenueAddress)]。完成後，在畫面最上面點擊左邊的「房子」圖示，回到專案頁。這裡有`PyConTW2020_DiscordBot`的專案金鑰。

5. 編輯 `PyConTW2020_InfoBot.py `。
	- USERNAME 填入你的 Droidtown 使用者帳號 (email)
	- API_KEY 填入你的 [Articut 金鑰](https://api.droidtown.co/member/)
	- LOKI_KEY 填入你產生的`PyConTW2020_DiscordBot`專案金鑰

### 3 執行
    python3 DT_InfoBot.py