---

---
# SpendThrift 敗家子終止機器人

## 背景

隨著科技發達，人類的物質生活過得越來越奢華。在這個充滿各式各樣誘惑的社會，身為一位小資族，記帳幾乎是每天不可或缺的小動作。但是，如同看到月底存款時你的心情，市面上關於記帳的APP使用起來未免有些冰冷了，於是我們建構了一個人性化的機器人來幫助各位月光族們，不要再敗家啦！

他，就是錢包君最好的朋友；他，就是奢侈的噩夢；他，就是「敗家子終止機器人」！

- 輸入花費或收入，搭配時間、地點、理由等，他會幫你全部鉅細靡遺的記錄下來！
- 依照輸入條件查詢，他也能自動分析先前的紀錄並告訴你結果！
- 自己設定排程，他可以 ~~照三餐~~ 提醒各位記帳！
- 人性化設定，輸入時直接打入平常說的話語(自然語言)即可。
- 無法克制享受花大錢的時光？小心會挨罵！根據條件觸發特殊對話，他可是很難取悅的！

在處理輸入時，我們使用了 [卓滕語言科技](https://droidtown.co/zh-tw/) 的 [ArticutAPI](https://api.droidtown.co/document/) 與 [LOKI](https://github.com/Droidtown/LokiHub) ，相較於市面上的機器人大多採用關鍵字的方式檢測輸入條件，「敗家子終止機器人」使用 NLU 處理語料，比外面的記帳APP更準確、更聰明、更有溫度！

## 專案內容列表

- [專案目錄](##專案目錄)
- [環境設定](##環境設定)
- [使用說明](##使用說明)
- [使用者輸入範例](##使用者輸入範例)
- [作者](##作者)
- [參考文件](##參考文件)

## 專案目錄

[SpendThrift的Repository](https://github.com/Intern-CD/SpendThrift_bot/tree/main/SpendThrift_bot)

- \discord
  - discord 機器人運作程式
  - \user_data
    - 以.csv存放使用者的記帳資料，檔名為使用者的 `discord ID`。
- \intent
  - 利用 [LOKI](https://github.com/Droidtown/LokiHub) 建立的意圖檔
    - 記帳
      - Loki_earn_adv.py
      - Loki_spend_adv.py
    - 查詢
      - Loki_searching.py
  - USER_DEFINED的json檔
- \ref
  - [LOKI](https://github.com/Droidtown/LokiHub) 的意圖參考檔
- `SpendThrift_bot.py`
  - 主程式
- `function.py`
  - 自定義函式

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

## 使用說明

- 使用Discord來操作Transportation ChatBot，請點選 Discord 資料夾以瀏覽更多說明。

<!-- - 欲讀取已建立好的Loki意圖，請點選 ref 資料夾瀏覽更多說明。 -->

## 使用者輸入範例

在Discord輸入列標記ChatBot「@SpendThrift_bot」，並輸入「出來」以檢視ChatBot功能的使用說明。

- 記帳：至少須包含 `形式` 與 `金額`
  - 支出
    - 範例：@SpendThrift 昨天去全聯購物花了300元
  - 收入
    - 範例：@SpendThrift 上週五去打工賺了1400元
- 查詢：至少須包含一樣條件
  - 依時間查詢
    - 範例：@SpendThrift 查詢我上週五花了多少錢
  - 依收入查詢
    - 範例：@SpendThrift 查詢我上周收入多少
  - 依支出查詢
    - 範例：@SpendThrift 查詢我昨天支出多少

## 作者

- [Grammyship](https://github.com/Grammyship)
- [Yunyun0404](https://github.com/Yunyun0404)

## 參考文件

[Articut Document](https://api.droidtown.co/document/#Articut)
[LokiHub](https://github.com/Droidtown/LokiHub)

### How to contribute?

歡迎提出任何建議或者Pull Request。
