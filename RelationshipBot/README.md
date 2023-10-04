# 感情小助理 RelationshipBot
### 內容列表
- [Bot介紹](#Bot介紹)
- [專案目錄](#專案目錄)
- [環境設置](#環境設置)
- [Loki啟用說明](#loki啟用說明)
- [Discord Bot建置](#discordbot建置)
- [使用者互動說明](#使用者互動說明)
- [資源](#資源)
- [作者](#作者)
- [參考資料](#參考資料)
## Bot介紹 
談戀愛總是遇到相處上的難題嗎？感情小助理 RelationshipBot 是一款可以提供您和男/女朋友相處建議的小助手，
就像您最好朋友那樣，只要輸入您想問的問題，BOT就能透過NLU的LOKI理解您的煩惱，並為您提供方向，讓您和另一半相處起來更輕鬆愉快！

## 專案目錄
```
.
├── Discord_bot.py                     # DISCORD 連接
├── README.md
├── family                             # Context "家庭"
│   ├── intent                         # Context為"家庭"下的意圖
│   │   ├── Loki_family.py
│   │   ├── USER_DEFINED.json          
│   │   └── Updater.py
│   ├── family.py                      # Context"家庭"的主程式
│   └── reply                          # Context為"家庭"下的回覆
│       └── reply_family.json
├── life_style                         # Context "生活習慣"
│   ├── intent                         # Context為"生活習慣"下的意圖
│   │   ├── Loki_future.py
│   │   ├── Loki_habit.py
│   │   ├── Loki_long_distance.py
│   │   ├── Loki_work.py
│   │   ├── USER_DEFINED.json          
│   │   └── Updater.py
│   ├── life_style.py                  # Context"生活習慣"的主程式
│   └── reply                          # Context為"生活習慣"下的回覆 
│       ├── reply_future.json
│       ├── reply_habit.json
│       ├── reply_long_distance.json
│       └── reply_work.json
├── loyalty                             # Context "忠誠"
│   ├── intent                          # Context為"忠誠"下的意圖
│   │   ├── Loki_other.py
│   │   ├── Loki_self.py
│   │   ├── USER_DEFINED.json           
│   │   └── Updater.py
│   ├── loyalty.py                      # Context"忠誠"的主程式
│   └── reply                           # Context為"忠誠"下的回覆
│       ├── reply_other.json
│       └── reply_self.json
├── money                               # Context "經濟"
│   ├── intent                          # Context為"經濟"下的意圖
│   │   ├── Loki_money.py
│   │   ├── USER_DEFINED.json
│   │   └── Updater.py
│   ├── money.py                        # Context"經濟"的主程式
│   └── reply                           # Context為"經濟"下的回覆
│       └── reply_money.json
├── personality                         # Context "個性"
│   ├── intent                          # Context為"個性"下的意圖
│   │   ├── Loki_care.py
│   │   ├── Loki_care_adv.py
│   │   ├── Loki_fight.py
│   │   ├── Loki_trait.py
│   │   ├── Loki_trait_adv.py
│   │   ├── USER_DEFINED.json
│   │   └── Updater.py
│   ├── personality.py                  # Context"個性"的主程式
│   └── reply                           # Context為"個性"下的回覆
│       ├── reply_care.json
│       ├── reply_fight.json
│       └── reply_trait.json
├── sex                                 # Context "性事"
│    ├── intent                         # Context為"性事"下的意圖
│    │   ├── Loki_both.py
│    │   ├── Loki_boyfriend.py
│    │   ├── Loki_girlfriend.py
│    │   ├── USER_DEFINED.json
│    │   └── Updater.py
│    ├── sex.py                         # Context"性事"的主程式
│    └── reply                          # Context為"性事"下的回覆
│        ├── reply_both.json
│        ├── reply_boyfriend.json
│        └── reply_girlfriend.json
├── pingying_preprocessing              #前處理
│   ├── intent
│   │   ├── Loki_dcard.py
│   │   ├── Loki_ig.py
│   │   ├── Loki_line.py
│   │   ├── Loki_pow.py
│   │   ├── Loki_ptt.py
│   │   ├── Loki_sex.py
│   │   ├── USER_DEFINED.json
│   │   └── Updater.py
│   └── pingying_preprocessing.py
└── ref                                 #6個不同Context+前處理的ref檔
   ├── family_ref
   │   └── family.ref
   ├── life_style_ref
   │   ├── future.ref
   │   ├── habit.ref
   │   ├── long_distance.ref
   │   └── work.ref
   ├── loyalty_ref
   │   ├── other.ref
   │   └── self.ref
   ├── money_ref
   │   └── money.ref
   ├── personality_ref
   │   ├── care.ref
   │   ├── care_adv.ref
   │   ├── fight.ref
   │   ├── trait.ref
   │   └── trait_adv.ref
   ├── sex_ref
   │   ├── both.ref
   │   ├── boyfriend.ref
   │   └── girlfriend.ref
   └── pingying_preprocessing_ref
       ├── dcard.ref
       ├── ig.ref
       ├── line.ref
       ├── pow.ref
       ├── ptt.ref
       └── sex.ref
```
## 環境設置
- 套件安裝
    - `pip3 install ArticutAPI`
    - `pip install -r requirements.txt`
## Loki啟用說明
1. 註冊並登入[卓騰語言科技AI](https://api.droidtown.co/login/)
2. 點選 `Loki` -> `開始啟用Loki` 進入Loki控制台
3. 輸入專案名稱並點選 `建立專案`，並依序建立以下7個專案
```
1. family
2. life_style
3. money
4. personality
5. loyalty
6. sex
7. pingying_preprocessing
```
4. 進入設立完成之專案 **family**
5. 點擊 `選擇檔案` ->選擇 `.ref` 檔->點選 `讀取意圖` 依序匯入目錄 **family_ref** 中所有的`.ref`檔案
6. 點選畫面左上角房子圖示，回到 Loki控制台，點選 `複製` 專案金鑰
7. 在目錄 **family** 底下創建檔案 `account.info`，並輸入以下內容
```
{
    "username":"--填入Loki註冊信箱--",
    "api_key" :"--填入ArticutAPI金鑰--",
    "loki_key":"--填入專案金鑰--"
}
```
8. 對剩餘6個專案重複步驟4~7

## DiscordBot建置
1. 註冊並登入 Discord 帳號
2. 進入[Discord Developers](https://discord.com/developers/applications)
3. 點擊畫面右上方的 `New Application` ->填上 Bot 名稱-> 點擊 `create` 建立 Discord Bot
4. 點選右方欄位 SETTINGS 中的 `Bot` ->點選 `Add Bot`
5. 點選右方欄位 SETTINGS 中的 `OAuth2` ->點選 `URL Generator`
6. 於 SCOPES 欄位勾選「bot」
7. 於 BOT PERMISSIONS 欄位勾選「Send Messages」、「Embed Links」、「Attach Files」及「Read Message History」
8. 複製 GENERATED URL 到新分頁中貼上，選擇 Bot 欲加入之伺服器，即完成添加
9. 點選 SETTINGS 中的 `Bot` ->點選 `Reset Token`
10. 在最外層的目錄下（與`Discord_bot.py`同一層）創建檔案 `account.info`
11. 將 Token 貼至 `account.info` 中
```
{
    "discord_token":"--填入token--"
}
```
## 使用者互動說明
完成上述程序後，執行 `python3 Discord_bot.py` 即可開始與 Bot 互動<br>
### <互動示例>
```
1. Tag RelationshipBot. 跟他打聲招呼吧！
```
![say Hi image](https://cdn.discordapp.com/attachments/1149239616357027942/1149242784860094527/image.png)
```
2. Tag RelationshipBot. 跟他聊聊在感情方面遇到的「家庭/金錢/生活習慣/性格/忠誠/性事」六大類問題吧！
```
![ask relationshipBot image](https://cdn.discordapp.com/attachments/1149239616357027942/1149245208807088180/image.png)
<br><br>
![Ask RelationshipBot image](https://cdn.discordapp.com/attachments/1149239616357027942/1149245213940908073/image.png)
```
3. Tag RelationshipBot. Oops!別擔心，他會提示你的！
```
![prompt image](https://cdn.discordapp.com/attachments/1149239616357027942/1149249207216115742/image.png)
```
4. Tag RelationshipBot. 完美的結尾🤗
```
![ending image](https://cdn.discordapp.com/attachments/1149239616357027942/1149253616553689098/image.png)

## 資源
**Droidtown Youtube 搭配 Droidtown GitHub服用，效果最佳！**
+ [Droidtown Official Youtube Channel](https://www.youtube.com/@Droidtown/playlists) **`Must See!`**
+ [Droidtown free resources(GitHub)](https://github.com/Droidtown/NLP_TrainingLab)
+ [Droidtown document](https://api.droidtown.co/document/#Articut)
+ [Droidtown products](https://api.droidtown.co/)


## 作者
+ [Brian Ding](https://github.com/brian098091)
+ [Chris Chou](https://github.com/ChrisLoading)
+ [Emily Li](https://github.com/emilyli0521)

若您有興趣了解更多，或是遇到任何問題，請[點此聯絡](https://mail.google.com/mail/?view=cm&fs=1&to=brian098091@gmail.com,tsunghaochou@gmail.com,a0930591669@gmail.com)我們

## 參考資料
+ [感情｜天下雜誌](https://www.cw.com.tw/tag/%E6%84%9F%E6%83%85?page=2)
+ [兩性關係｜天下雜誌](https://www.cw.com.tw/article/5019816)
+ [感情版｜Dcard ](https://www.dcard.tw/f/relationship)
+ [兩性關係｜Bella](https://www.bella.tw/articles/sexuality/29173)
+ [兩性愛情｜COSMOPOLITAN ](https://www.dcard.tw/f/relationship)
