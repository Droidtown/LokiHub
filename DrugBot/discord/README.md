# Discord 上的 DrugBot
## 操作手冊

### 在Loki上建立DrugBot

1. 把本資料夾Pull下來

4. 進入[Loki](https://api.droidtown.co/loki/)

6. 輸入專案名稱(英文)，並建立專案
![](https://i.imgur.com/DtFeyxp.png)

7. 點擊你的「專案名稱」，進入專案頁面
![](https://i.imgur.com/kxfoQO3.png)

8. 點擊「選擇檔案」，把ref資料夾內的ref檔打開
![](https://i.imgur.com/TvWcbG5.png)

9. 按下「讀取意圖」，4個intent就建立好了
![](https://i.imgur.com/cQbOkId.png)

10. 點進**每個**意圖中，滑到最下面，按下「生成模型」
```
❈注意: 不可按「全句分析」，否則就要重新輸入此ref檔
```
![](https://i.imgur.com/sbwq2Jo.png)

12. 從左上角的房子返回
![](https://i.imgur.com/rtx7h13.png)

13. 複製屬於你的Loki_Key
![](https://i.imgur.com/zhtxyyY.png)

14. 打開discord資料夾中的「DrugBot.py」
15. 把 Loki的帳號(username) 跟 Loki_Key 填入
![](https://i.imgur.com/SnpJ8c5.png)



| 到這邊你已經完成建立Loki上的DrugBot了！ | 
| -------- | 

---
### 在Discord上建立DrugBot

1. 進入discord的[開發者頁面]  (https://discord.com/developers/applications/)
2. 註冊並登入  
![](https://i.imgur.com/bIOPBLW.png)
3. 點擊右上角的「New Application」  
![](https://i.imgur.com/JFiNjz0.png)

4. 建立屬於你的 Application  
![](https://i.imgur.com/rcDplqR.png)

5. 從左邊欄位中選擇**Bot**，並點擊「Add Bot」  
![](https://i.imgur.com/DraxHYp.png)

6. 建立好Bot之後，Copy它的**Token**  
![](https://i.imgur.com/Jn4lNvJ.png)

7. 開啟 **discord_DrugBot.py**  
![](https://i.imgur.com/aOJDXmQ.png)

8. 把剛剛copy的Token填入  
![](https://i.imgur.com/NZBK2Yy.png)

9. 把pull下來的整個資料夾放入你自己的server

10. 從server中執行 **discord_DrugBot.py**

11. 開始測試Bot!

### 輸入範例
![](https://i.imgur.com/i1vqxL3.png)


### 輸出範例
![](https://i.imgur.com/x1hYCox.png)
![](https://i.imgur.com/QqizyqD.png)
