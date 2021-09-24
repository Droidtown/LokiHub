# Lease_Dispute_Bot 租賃糾紛簡易法律諮詢機器人
### 在外租屋遇到租賃糾紛不知如何解決嗎 ？
### 別擔心，您的租賃法律問題小幫手已上線 ！
##### 您只需向Lease_Dispute_Bot說明您遇到的問題，Bot就會以白話文的方式提供您法律建議
##### 沒有看不懂的法律用語！以一般日常生活對話即可溝通！

------------

### Lease_Dispute_Bot 可以解決的問題
- 押金問題
- 水電費、網路費、瓦斯費問題
- 房東任意進出房客租處
- 租到凶宅
- 租屋處遭房東賣給第三人
- 租賃物修繕義務

### 環境設定
`Python 3.9.1 `

### 安裝套件
`pip install ArticutAPI`


------------



## 在Droidtown的Loki上建立模型

#### STEP 1 ：註冊一個[卓騰語言科技](https://api.droidtown.co/)的帳號
![註冊](https://github.com/yian-annie/Lease_Dispute_Bot/blob/main/media/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-09-20%20130858.png?raw=true)

#### STEP 2 ：登入
![登入](https://github.com/yian-annie/Lease_Dispute_Bot/blob/main/media/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-09-20%20130950.png?raw=true)

#### STEP 3 ：進入Loki 
按**開始使用Loki**
![Loki](https://github.com/yian-annie/Lease_Dispute_Bot/blob/main/media/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-09-20%20131031.png?raw=true)

#### STEP 4 ：建立一個新的專案
![建立專案](https://github.com/yian-annie/Lease_Dispute_Bot/blob/main/media/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-09-20%20131117.png?raw=true)

#### STEP 5 ：匯入ref檔
在建立意圖的下面，按**選擇檔案**，匯入全部的ref檔

(記得先從github上將Lease_Dispute_Bot 的資料夾整個clone下來喔)

然後按**讀取意圖**
![匯入ref檔](https://github.com/yian-annie/Lease_Dispute_Bot/blob/main/media/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-09-20%20131234.png?raw=true)


這樣所有的intent就都進來了
![所有的intent](https://github.com/yian-annie/Lease_Dispute_Bot/blob/main/media/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-09-20%20131315.png?raw=true)

#### STEP 6 ：生成模型
進到每一個intent裡面

滑到最下面

看到**綠色的**這個**生成模型**的按鈕，給他按下去 ！
![生成模型](https://github.com/yian-annie/Lease_Dispute_Bot/blob/main/media/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-09-20%20131355.png?raw=true)

#### 這樣Loki的部分就完成了


------------



## 在Discord上建立Bot

#### STEP 1 ：新建一個Application
首先，到[Discord Developers](https://discord.com/developers/applications)登入自己的Discord帳號

按下**藍色**那個按鈕，建立一個新的Application
![Appilcation](https://github.com/yian-annie/Lease_Dispute_Bot/blob/main/media/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-09-20%20131536.png?raw=true)

#### STEP 2 ：新增一個Bot
在 Application 裡，左邊切換到 Bot 的分頁
![Add Bot1](https://github.com/yian-annie/Lease_Dispute_Bot/blob/main/media/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-09-20%20131723.png?raw=true)

按下**藍色**那個**Add Bot**，並設定它的名字
![Add Bot2](https://github.com/yian-annie/Lease_Dispute_Bot/blob/main/media/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-09-20%20131751.png?raw=true)

#### STEP 3 ：取得Bot的Token
按下**藍色**那個**Copy**就可以複製Bot的Token

![Token](https://github.com/yian-annie/Lease_Dispute_Bot/blob/main/media/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-09-20%20132309.png?raw=true)

#### STEP 4 ：將Bot加入伺服器

將分頁切換到**OAuth2**
![server](https://github.com/yian-annie/Lease_Dispute_Bot/blob/main/media/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-09-20%20145154.png?raw=true)

在右邊的選單中勾選**Bot**
![server2](https://github.com/yian-annie/Lease_Dispute_Bot/blob/main/media/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-09-20%20145225.png?raw=true)

下面就會出現**Bot的網址**，讓伺服器管理員將你的Bot加入伺服器內就可以了！


------------



## 建立account.info

##### 在Lease Dispute Bot的資料夾內建立一個檔案，名為account.info
###### account.info內是一個字典，在裡面填入四個值，分別為：
- username：是你在卓騰語言科技申請的帳號(信箱)
- apikey：在[卓騰語言科技](https://api.droidtown.co/)登入後即可複製
- loki_key：在進入Loki後，每個專案會有自己的金鑰，按下複製即可
- discord_token：就是剛剛上面在[Discord Developers](https://discord.com/developers/applications)所複製的Token

![account.info](https://github.com/yian-annie/Lease_Dispute_Bot/blob/main/media/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-09-20%20145959.png?raw=true)

這樣就完成了！


------------

## 最後一步 ：執行 ！

在終端機內，移到Bot程式所在的目錄，執行它！

![laststep](https://github.com/yian-annie/Lease_Dispute_Bot/blob/main/media/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-09-20%20151144.png?raw=true)

##### 就可以在你的Discord頻道中呼叫Lease Dispute Bot了！



------------

## 使用範例
呼叫Bot，跟他打個招呼

再直接跟他說遇到的問題

Bot就會回覆簡易的法律建議給您 ~~~

![example](https://github.com/yian-annie/Lease_Dispute_Bot/blob/main/media/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-09-20%20152944.png?raw=true)



------------

## 聯絡資訊
若您還有其他任何的疑問，或是對Loki與法律的應用有興趣

歡迎透過E-mail聯繫，謝謝

Annie Chen ：yeeanniechen@gmail.com
