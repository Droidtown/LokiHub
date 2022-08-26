# SpendThrift 敗家子終止機器人

## 背景
身為小資族，記帳幾乎是每天不可或缺的小動作，幫助釐清自己的財務狀況。但是，市面上關於記帳的APP使用起來未免少了一些溫度。於是我們建構了"敗家子終止機器人"，只要把該機器人加到自己的discord頻道，他就可以 ~~照三餐~~ 提醒各位記帳，而在輸入上，直接以自然語言輸入即可。

## 專案內容列表
- [目錄](##目錄)
- [環境設定](##環境設定)
- [使用說明](##使用說明)
- [使用者輸入範例](##使用者輸入範例)
- [作者](##作者)

## 目錄
[SpendThrift的Repository](https://github.com/Intern-CD/SpendThrift_bot/tree/main/SpendThrift_bot)
- \discord
    - discord機器人運作程式
- \intent
    - intent的python檔
        - Loki_earn_adv.py
        - Loki_searching.py
        - Loki_spend_adv.py
    - USER_DEFINED的json檔
- \ref
- \user_data
    - 以.csv存放使用者的記帳資料，檔名為使用者的`discord ID`。
- `SpendThrift_bot.py`
    - 主程式
- `function.py`
    - 函式
    
## 環境設定
1. 請至[卓騰語言科技](https://api.droidtown.co/)官方網站註冊帳號並登入頁面。
2. 註冊會員 
![註冊會員](https://i.imgur.com/WLqveN1.jpg)
3. 註冊完成後的登入畫面
![登入](https://i.imgur.com/03aEksl.jpg)
4. 順利登入會員之後，到[這邊](https://api.droidtown.co/loki/)使用Loki。

### 安裝套件
本專案使用了以下套件：

- [ArticutAPI](https://pypi.org/project/ArticutAPI/)
```shell=
$ pip3 install ArticutAPI
```
### 參考文件
[Articut Document](https://api.droidtown.co/document/#Articut)

## 使用說明
- 使用Discord來操作Transportation ChatBot，請點選 Discord 資料夾以瀏覽更多說明。
<!-- - 欲讀取已建立好的Loki意圖，請點選 ref 資料夾瀏覽更多說明。 -->

## 使用者輸入範例

在Discord輸入列標記ChatBot「@SpendThrift_bot」，並輸入「出來」以檢視ChatBot功能的使用說明。

- 記帳
    - 支出
        - 範例：@SpendThrift 昨天去全聯購物花了300元
    - 收入
        - 範例：@SpendThrift 上週五去打工賺了1400元
- 查詢
    - 依時間查詢
        - 範例：@SpendThrift 查詢我上週五花了多少錢
    - 依收入查詢
        - 範例：@SpendThrift 查詢我上周收入多少
    - 依支出查詢
        - 範例：@SpendThrift 查詢我昨天支出多少

## 作者
- [Grammyship](https://github.com/Grammyship)
- [Yunyun0404](https://github.com/Yunyun0404)

### How to contribute?
歡迎提出任何建議或者Pull Request。