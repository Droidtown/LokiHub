# 興趣使然的學群推薦機器人 Department Recommandation Bot

## 專案簡介

**興趣使然的學群推薦機器人** 是一個為那些對升學方向感到迷茫的使用者提供學群與科系推薦的機器人。使用者只需輸入自己的興趣，機器人將根據這些興趣提供適合的學群與科系建議。該機器人的資料來自 IOH 網站，旨在幫助使用者更好地了解各學群和科系的選擇。

## 安裝步驟

1. 下載專案文件。
2. 註冊 Discord Portal 並建立一個 discord bot。可參考教程：https://realpython.com/how-to-make-a-discord-bot-python/
3. 到 driodtown 網站 (https://api.droidtown.co/) 註冊登入
4. 到 Loki 頁面將 ref 資料夾中檔案匯入以建立與其一一對應的專案，專案名稱與檔案名稱一致。(interest 是國語意圖分析專案，其餘都是文本分類模型(NeuroKumoko))
5. 完成 Loki 專案模型部署後將各專案 `Loki_key` 與 `api_key` 、 `username` 及 `discord_token` 填入 `account.info` 檔案中的對應欄位。
6. 安裝專案所需的 Python 套件：
    ```bash
    pip install -r requirements.txt
    ```
7. 將 Discord 機器人添加到你的 Discord 伺服器中。
8. 開始與機器人互動！

## 使用方式

1. 在 Discord 伺服器中啟動機器人。
2. 輸入你的興趣，機器人將提供適合的學群與科系建議。

## 參考資料

1. IOH 個人經驗開放平台 (ioh.tw)
2. Collego 大學選才與高中育才輔助系統 (collego.edu.tw)

## 聯繫方式

如有問題或建議，請聯繫 patpatpat1015@gmail.com
