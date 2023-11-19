# CampBot 營隊客服機器人

## CampBot是什麼?

Camp_bot 是以玩轉學校的夏令營為基礎，設計的營隊客服聊天機器人，透過對話來辨識家長的特定意圖並予以回應，只需要呼叫機器人並輸入小孩的年級即可開始對話。

## Camp_bot可以回答什麼?

如果家長想要了解下列有關營隊的項目細節皆可以詢問:

+ 營隊內容
+ 營隊師資
+ 營隊費用
+ 營隊時間
+ 營隊地點
+ 營隊餐食
+ 營隊保險
+ 營隊收穫
+ 營隊紀錄
+ 課表教材
+ 報名流程
+ 特殊需求
+ 行前準備
+ 安全措施

## 環境設置

+ 套件安裝
  + ```pip3 install ArticutAPI```

## 啟用Loki

1. 註冊並登入[卓騰語言科技AI](https://api.droidtown.co/member/)
1. 點選```Loki``` -> ```開始啟用Loki``` 進入Loki控制台
1. 輸入專案名稱並點選 ```建立專案``` ，並依序建立以下3個專案:

``` .
1. CampAge
2. five_nine_grade
3. two_four_grade
```

1. 進入設立完成之專案 ```CampAge```
1. 點擊 ```選擇檔案``` ->選擇 ```.ref 檔```->點選 ```讀取意圖``` 依序匯入目錄 ```.ref 檔``` 中所有的.ref檔案
1. 點選畫面左上角房子圖示，回到 Loki控制台，點選 ```複製``` 專案金鑰
1. 在目錄 ```CampAge``` 底下創建檔案 ```account.info```，並輸入以下內容

``` .
{
    "username":"--填入Loki註冊信箱--",
    "api_key" :"--填入ArticutAPI金鑰--",
    "loki_key":"--填入專案金鑰--"
}
```

5. 對剩餘2個專案重複步驟4~7

## 啟用DiscordBot

1. 註冊並登入 Discord 帳號
1. 進入Discord Developers
1. 點擊畫面右上方的 ```New Application``` ->填上 Bot 名稱-> 點擊 ```create``` 建立 Discord Bot
1. 點選右方欄位 SETTINGS 中的 ```Bot``` ->點選 ```Add Bot```
1. 點選右方欄位 SETTINGS 中的 ```OAuth2``` ->點選 ```URL Generator```
1. 於 SCOPES 欄位勾選「bot」
1. 於 BOT PERMISSIONS 欄位勾選「Send Messages」、「Embed Links」、「Attach Files」及「Read Message History」
1. 複製 GENERATED URL 到新分頁中貼上，選擇 Bot 欲加入之伺服器，即完成添加
1. 點選 ```SETTINGS``` 中的 ```Bot``` ->點選 ```Reset Token```
1. 在最外層的目錄下（與```Discord_bot.py```同一層）創建檔案 account.info
1. 將 Token 貼至 ```account.info``` 中

``` .
{
    "discord_token":"--填入token--"
}
```

## 互動說明

1. Tag @campbot之後輸入「hi」，向他打招呼。
![hello](https://cdn.discordapp.com/attachments/1139465672603226213/1149621123504406608/image.png)

2. 輸入年級
![grade](https://cdn.discordapp.com/attachments/1139465672603226213/1149621190835572797/image.png)

3. 輸入問題，可以從「我想了解營隊」開始。
![q1](https://cdn.discordapp.com/attachments/1139465672603226213/1149621291096227882/image.png)

4. 如果還有其他問題，輸入問題繼續問下去。
![q2](https://cdn.discordapp.com/attachments/1139465672603226213/1149621630100840579/image.png)

5. 如果沒有其他想問的問題，輸入「沒有」結束對話。
![end](https://cdn.discordapp.com/attachments/1139465672603226213/1149622415949824030/image.png)

## 作者

+ [Ting-Wei Hu "Lancy"](https://github.com/Lancyhu)

+ [Hsu-Chen Hsiao "Simon"](https://github.com/HS6103)

## 參考資料

[玩轉營隊](https://pleyschool.org/)
