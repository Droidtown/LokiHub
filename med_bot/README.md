# 看病小幫手 My MedBot
「肚子有點痛」

「怎麼辦，心臟有點痛」

不知道你會不會有時候覺得這裡痛、那裡痛，但是不確定要看哪科？

上網查覺得有點懶，然後問櫃台的人員覺得有點害羞

那看病小幫手就是你最好的夥伴，是一個醫療分科機器人，只要詢問他就可以得到看哪科的建議喔~ 

你是怎麼問醫院服務台的人，就怎麼問看病小幫手!!!

目前可以在**Line以及Discord**找到我們的看病小幫手!

----
# 目錄 :
1. [檔案總覽](#First)
2. [使用者說明](#Second)
3. [開發者說明](#Third)
4. [文本訓練方式](#Fourth)

# <h1 id="First">1.檔案總覽</h1>
在這個repository 中總共有3個檔案夾，分別是
1. `Discord_bot`：把My MedBot 放入Discord 的必要程式和檔案
2. `LINE_bot`：把My MedBot 放入 LINE 的必要程式和檔案
3. `Ref`：這個資料夾是開發者需要用到的，裡面是已經設定好的Loki Ref檔案 (Loki為 droidtown 的可以用來設計聊天機器人的工具) 

# <h1 id="First">2. 使用者說明</h1>
本機器人可於以下兩平台執行
1. [Discord](#Fifth)
2. [LINE](#Sixth)

----
# <h2 id="Fifth">使用Discord: 步驟解說</h1>
1. 安裝Discord
   請到以下連結下載Discord: https://discord.com/
   
2. 下載完成後請申請帳號
   
4. 加入 my_med_bot 到discord 
   邀請Link: https://discord.gg/yRCp2PjF
   
5. 使用@my_med_bot呼叫機器人來幫忙~

6. 接著和 my_med_bot 說你哪裡不舒服，可以多說說你是什麼病症，或是哪邊不舒服，接下來就med bot 就會和你說你可以去哪一科看診喔~
  
  ![喉嚨痛](https://upload.cc/i1/2021/03/05/Z3qtp0.png)

---

# <h2 id="Sixth">使用LINE: 步驟解說</h1>
1. 安裝LINE
   請到以下連結下載LINE: https://line.me/zh-hant/
   
2. 下載完成後請申請帳號
   
4. 請掃描以下QRcode 

   ![](https://upload.cc/i1/2021/03/19/yMOE3d.png)

5. 接著和 my_med_bot 說你哪裡不舒服，可以多說說你是什麼病症，或是哪邊不舒服，接下來就med bot 就會和你說你可以去哪一科看診喔~

# <h1 id="Third">3. 開發者說明</h1>
## 環境設定
1. 註冊 Loki 
2. 註冊 LINE Developer 
3. 註冊 Discord Portal 
4. python 3.6 以上

## Loki 使用說明
1. 請到 driodtown 網站 (https://api.droidtown.co/)
2. 連結應用服務，然後選擇Loki

<img src="https://upload.cc/i1/2021/03/12/CO61Ua.png" width="50%" height="50%" />

3. 進入Loki後，創一個新的專案，取名為 med_bot
<img src="https://upload.cc/i1/2021/03/12/cvlfjG.png" width="50%" height="50%" />

4. 請到 Ref 文件夾中，到如下圖的地方，上傳這些ref 檔案
<img src="https://upload.cc/i1/2021/03/12/3KDYbW.png" width="50%" height="50%" />

## LINE DEVELOPER 使用說明
[請詳見資料夾](https://github.com/howardsukuan/med_bot/tree/master/LINE_bot)
## Discord Portal 使用說明
[請詳見資料夾](https://github.com/howardsukuan/med_bot/tree/master/Discord_bot)

# <h1 id="Fourth">4. 文本訓練方式</h1>
1. 我們是參考以下網站
    1) 衛生福利部台北醫院就醫指南 https://www.tph.mohw.gov.tw/?aid=12
    2) 臺大醫院 該看哪一科 https://www.ntuh.gov.tw/ntuh/Fpage.action?muid=70&fid=2972
    3) 醫聯網- 醫師獻聲諮詢平台 https://expert.med-net.com/index?gclid=CjwKCAiAp4KCBhB6EiwAxRxbpGjtZfNqJif2RC_sm9_400q7kUImkAYOfqOHxo1n95UHMntRtts1oBoCWUYQAvD_BwE

## 訓練方式 
1. 我們從諮詢論壇、自身經驗和實係測試收集問診的句子。
2. 我們把句子分為兩類：
   1) 身體部位：只要句子中出現身體部位，我們就會分在這個類別，例如手臂斷掉了。
   2) 病症: 只要是和病症相關，或是斷詞後和身體部位斷在一起，例如頭痛，我們就會歸類在此類。
3. 把這兩類句子放入droidtown的Loki。接著Loki 就可以把那些句子斷詞，然後整理成不同的句型。依句型分類。
4. 接著把這些問診句子和我們查的資料用python 串接起來，然後回復使用者可以看哪一科。

