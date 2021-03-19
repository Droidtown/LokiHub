# Line 上的 DrugBot
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

14. 打開line資料夾中的「DrugBot.py」  
15. 把 Loki的帳號(username) 跟 Loki_Key 填入  
![](https://i.imgur.com/SnpJ8c5.png)


| 到這邊你已經完成建立Loki上的DrugBot了！ |   
| -------- | 

---

### 在Line上建立DrugBot
1. 進入Line的[開發者頁面](https://developers.line.biz/zh-hant/)  

2. 登入Line  
![](https://i.imgur.com/yXz28V1.png)

3. 建立一個 Provider 並點擊進入  
![](https://i.imgur.com/smmWoN9.png)

4. 點擊Create a new channel 並選擇 Message API  
![](https://i.imgur.com/j0JzHLa.png)  
![](https://i.imgur.com/15nvz0A.png)  

5. 填入必要欄位後點擊 **Create**
6. 在`Basic setting` 中可以找到 Channel secret
7. 在`Message API`的最下面找到 **Channel access token**，點擊 **issue** 取得Token
8. 打開 **line_app.py**  
![](https://i.imgur.com/4VGKMFk.png)

8. 填入 Channle secret 和 Access token  
![](https://i.imgur.com/imi1OTt.png)

9. 把pull下來的整個資料夾放入你自己的server
10. 從server中執行 **line_DrugBot.py**
11. 開始測試Bot！

### 輸入範例  
![](https://i.imgur.com/e8qEdnb.png)

### 輸出範例  
![](https://i.imgur.com/i6K1Efp.png)
![](https://i.imgur.com/0DGUepo.png)