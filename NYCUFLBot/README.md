國立陽明交通大學外國語文學系聊天機器人
===
關於大學部修課的問題都來問我吧！
---
專案簡介
---
我可以以下八類問題：
1. 第二外語
2. 英語評鑑
3. 專業必修科目
4. 「英文作文 / 傳達技巧工作坊」修課與免修方式
5. 跨域學程
6. 最低畢業學分
7. 雙主修、輔系
8. 預修碩士學位

安裝步驟
---
1. 下載專案文件。
2. 註冊 Discord Portal 並建立一個 discord bot。可參考教程：https://realpython.com/how-to-make-a-discord-bot-python/
3. 到 driodtown 網站 (https://api.droidtown.co/) 註冊登入
4. 到 Loki 頁面將 ref 資料夾中檔案匯入以建立與其一一對應的專案，專案名稱與檔案名稱一致。(interest 是國語意圖分析專案，其餘都是文本分類模型(NeuroKumoko))
5. 完成 Loki 專案模型部署後將各專案 Loki_key 與 api_key 、 username 及 discord_token 填入 account.info 檔案中的對應欄位。
6. 安裝專案所需的 Python 套件：
pip install -r requirements.txt
7. 將 Discord 機器人添加到你的 Discord 伺服器中。
8. 開始與機器人互動！





