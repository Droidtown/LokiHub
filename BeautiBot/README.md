# BeautiBot - 把你變漂漂！

## 背景
:bulb:不知道你有沒有像這樣的經驗：
夏天到了，想自在地換上背心短褲出門、穿上比基尼去海邊大展身材，卻因為毛毛的問題不堪其擾。好不容易鼓起勇氣私訊醫美診所小編，卻遲遲等不到回覆……這時候BeautiBot就是你的好幫手！不受時間和空間限制，一對一的聊天功能，不僅便利，也能讓你輕鬆進行預約，不用面對與人對話的尷尬。現在就在Discord上加入BeautiBot，替自己打造一個beauty body！

## 目錄
BeautiBot的Repository包含以下內容：

1. [Discord](https://github.com/marcnhwu/BeautiBot/blob/master/BeautiBot_For_Appointment.py)
2. [ref](https://github.com/marcnhwu/BeautiBot/tree/master/ref)
3. [BeautiBot_Loki](https://github.com/marcnhwu/BeautiBot/blob/master/BeautiBot_Loki.py)

## 環境設定

### 註冊Loki帳號

1. 請至[卓騰語言科技](https://api.droidtown.co/)官方網站註冊帳號並登入頁面。

2. 於網頁右上角點選註冊 

![](https://imgur.com/2v6Xhmy.jpg)

3. 註冊完成後即可登入

![](https://imgur.com/mpwBJKp.jpg)

4. 順利登入後，點選服務資訊區的「Loki」，接著點選「開始使用Loki」

![](https://imgur.com/440uQPf.jpg)


### 安裝套件
本專案使用了以下套件：

1. [ArticutAPI](https://pypi.org/project/ArticutAPI/)
```shell=
$ pip install ArticutAPI
```
* [Articut官方說明文件](https://api.droidtown.co/document/#Articut)

2. [discord](https://pypi.org/project/discord.py/)
```shell=
$ pip install discord.py
```
3. [DateTime](https://pypi.org/project/DateTime/)
```shell=
$ pip install DateTime
```

## 使用說明
* 欲使用Discord來操作，請點選 **Discord** 資料夾。
* 欲讀取已建立好的Loki意圖，請點選 **ref** 資料夾 [(如何讀取ref檔)](https://api.droidtown.co/document/#Loki_3)。

## 使用者輸入範例
在Discord輸入列標記機器人「@BeautiBot」，並且和它打聲招呼！
接著，你可以：
* 敘述問題：「我的腿毛好長好煩喔」
* 敘述需求：「我想預約南西診所的除毛療程」「我想預約星期一下午四點找程昭瑞醫生做除毛」
          
## 相關Repository

- [LokiHub](https://github.com/Droidtown/LokiHub) — 文意理解工具＆文字轉換API

## 作者

[@marcnhwu](https://github.com/marcnhwu)<br/>[@weilinglindachen](https://github.com/weilinglindachen)

## How to contribute?
歡迎[提出任何建議](https://github.com/marcnhwu/BeautiBot)或者Pull Request。
