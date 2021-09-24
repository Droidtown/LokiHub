# Jstorm Bot - 愛豆資訊一把抓！

## 簡介
Jstorm Bot運用爬蟲建立資料庫，提供Jstorm旗下成員的資料查詢功能。<br>
如果你是不認識他們的新朋友，可以運用Jstorm Bot得到各種基本資訊。<br>
如果你是已經熟悉的老朋友，也可以運用計算日期等功能，讓你慶祝不耽誤！<br>



## 專案内容列表
- [目錄](#目錄)
- [環境設定](#環境設定)
- [建立Discord機器人](#建立Discord機器人)
- [使用者輸入範例](#使用者輸入範例)
- [更新資料庫](#更新資料庫)
- [相關Repositories](#相關Repositories)
- [作者](#作者)



## 目錄
Jstorm Bot的Repository包含以下內容：

1. [intent](https://github.com/qinyanhao/LokiHub/tree/main/JstormBot/intent)
2. [ref](https://github.com/qinyanhao/LokiHub/tree/main/JstormBot/ref)
3. [web_crawler](https://github.com/qinyanhao/LokiHub/tree/main/JstormBot/web_crawler)
4. [Jstorm_Loki](https://github.com/qinyanhao/LokiHub/blob/main/JstormBot/Jstorm_Loki.py)
5. [Jstorm_infoBot](https://github.com/qinyanhao/LokiHub/blob/main/JstormBot/Jstorm_infoBot.py)


## 環境設定

### 註冊Loki帳號

1. 請至[卓騰語言科技](https://api.droidtown.co/)官方網站註冊帳號並登入頁面。

2. 註冊會員 

<img src="https://i.imgur.com/gQm1Pnz.jpg" height="250px"> <br>

註冊完成後的登入畫面↓

<img src="https://i.imgur.com/OntQ5T0.jpg" height="250px"> <br>


順利登入會員之後，藉由「服務資訊」區塊進入Loki應用程式頁面↓

<img src="https://i.imgur.com/nr6WG0w.jpg" height="200px"> <br>

### 建立Loki專案
1. 建立一個新的Loki專案
2. 進入該專案後，運用**讀取意圖**的功能，將ref中的檔案依序匯入。
3. 回到專案列表的頁面取得**專案金鑰**。
4. 複製金鑰以後，將金鑰貼入[Jstorm_Loki](https://github.com/qinyanhao/LokiHub/blob/main/JstormBot/Jstorm_Loki.py)中的```LOKI_KEY = ""```。
   ```USERNAME = ""```也要記得填入註冊的email。

### 安裝Discord套件
#### 環境設定與需求
* ##### 程式語言版本
    * Discord Bot 需要 Python3.6+ 才能執行
* ##### 所需套件
    * [Discord](https://pypi.org/project/discord.py/)
```shell=
$ pip install -U discord.py
```



## 建立Discord機器人
建立Discord機器人你需要以下內容：
* 帳號
* 伺服器
* 機器人

1. 建立帳號並且登入後，在頁面的左側按 **+** ，建立自己的伺服器。
2. 到[Discord Developer Portal－My Applications](https://discord.com/developers/applications) 的頁面，按左上角的**New Application**，建立新的APP。
3. 建立以後，按頁面左側的Bot。進入頁面後，再按右側的**Add Bot**。<br>
<img src="https://i.imgur.com/N7iaQpd.jpg" height="300px"> <br>

#### 創建完機器人之後，應該要出現這樣的畫面<br>
![](https://i.imgur.com/Dxx0qiD.png)
圖片來源：[Real Python](https://realpython.com/how-to-make-a-discord-bot-python)

4. 創建成功後，在**Build-A-Bot**的區塊中，有**TOKEN**的部分，按下**Copy**。
5. 把複製好的TOKEN貼到[Jstorm_infoBot](https://github.com/qinyanhao/LokiHub/blob/main/JstormBot/Jstorm_infoBot.py)中的```DISCORD_TOKEN=""```。
6. 接下來請按左側的**OAuth2**，下方的**SCOPES**中選擇**Bot**會得到一個網址。將網址貼近瀏覽器中就可以把機器人加入自己的伺服器囉！<br>
<img src="https://i.imgur.com/DSojxaP.jpg" height="300px"> <br>
7. 運用終端機執行[Jstorm_infoBot](https://github.com/qinyanhao/LokiHub/blob/main/JstormBot/Jstorm_infoBot.py)，你的機器人就正式上工了！



## 使用者輸入範例
在Discord的輸入欄用「@」呼叫你的機器人，跟他打招呼或單純叫他都可以得到可查詢的內容列表。<br>
查詢團體和成員的話用別名也是可以的喔！

* 打招呼<br>
<img src="https://i.imgur.com/KtX5h3T.jpg" width="400px"> <br>
* Jstorm資訊：「旗下有誰」「Jstorm有幾團」「Jstorm有那些團體」<br>
<img src="https://i.imgur.com/2VCbSFf.jpg" width="300px"> <br>

* 團體資訊：
1. 各團成員：「嵐有誰」「尼尼是嵐嗎」「櫻井翔是嵐的人嗎」<br>
<img src="https://i.imgur.com/OGpV68N.jpg" width="300px"> <br>
2. 出道日、結成日：「結成日是何時」<br>
<img src="https://i.imgur.com/n3SaPCm.jpg" width="350px"> <br>
3. 計算日期：「出道幾年了」、「離結成日還有幾天」<br>
<img src="https://i.imgur.com/APym2gy.jpg" width="350px"> <br>

* 個人資訊
1. 整體資訊：「松本潤是誰」<br>
<img src="https://i.imgur.com/Vx7aBX3.jpg" width="500px"> <br>
2. 日英姓名：「大貴姓什麼」「阿慧全名是什麼」「涼介的英文名字是什麼」「雄也的英文姓氏是什麼」<br>
<img src="https://i.imgur.com/zIs5L3Z.jpg" width="350px"> <br>
3. 年齡：「他幾歲」「最年長」「年齡順序為何」<br>
<img src="https://i.imgur.com/hu26ZQd.jpg" width="350px"> <br>
4. 生日：「幾年出生的」「生日是何時」「離念念的生日還有幾天」<br>
<img src="https://i.imgur.com/vd80pE4.jpg" width="350px"> <br>
5. 血型：「誰是O型」「KT有O型嗎」「KT各是什麼血型」<br>
<img src="https://i.imgur.com/7RFsUrz.jpg" width="350px"> <br>
6. 出身地：「誰是東京人」「雄也是哪裡人」「光是宮城人嗎」<br>
<img src="https://i.imgur.com/wkgjX0u.jpg" width="350px"> <br>
7. 身高：「他多高」「KT誰最矮」「最高到最矮」<br>
<img src="https://i.imgur.com/x2Zclza.jpg" width="300px"> <br>
8. 成員色：「誰是黃色」「代表色是什麼」「各是什麼顏色」「有人是紅色嗎」「阿智是藍色嗎」「有哪些應援色」<br>
<img src="https://i.imgur.com/c7mY77L.jpg" width="300px"> <br>

* 說掰掰－跟機器人說「謝謝/我問完了/掰掰/88/bye/byebye/再見/再會」將會結束對話並清除資料。<br>
<img src="https://i.imgur.com/7sHUiMX.jpg" width="350px"> <br>

## 更新資料庫
由於本Bot是採用靜態資料庫進行，如果想要獲取團體或是成員的最新圖片，請運用[web_crawler](https://github.com/qinyanhao/LokiHub/tree/main/JstormBot/web_crawler)中的[profile.py](https://github.com/qinyanhao/LokiHub/blob/main/JstormBot/web_crawler/profile.py)進行更新。


## 相關Repositories

- [LokiHub](https://github.com/Droidtown/LokiHub) — ☑️文意理解工具＆文字轉換API

## 作者

[@qinyanhao](https://github.com/qinyanhao) <br>
Email: sylvia.wang4837@gmail.com <br>
歡迎提出建言或是提出反饋！
