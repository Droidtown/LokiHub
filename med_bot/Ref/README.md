# Ref 檔案使用說明
## 1. 檔案內容
在這個資料夾中有兩個檔案: `body_part.ref`以及`symptom.ref`，這些檔案之後我們會匯入到Loki裡頭。

----
## 2. 環境設定
1. 請到卓騰科技網站 (https://api.droidtown.co/)
2. 連結應用服務，然後選擇LOKI

<img src="https://upload.cc/i1/2021/03/12/CO61Ua.png" width="80%" height="80%"/>

3. 進入LOKI後，創一個新的專案，取名為 med_bot
<img src="https://upload.cc/i1/2021/03/12/cvlfjG.png"/>

4. 請到 Ref 文件夾中，到如下圖的地方，上傳這些ref 檔案
<img src="https://upload.cc/i1/2021/03/12/3KDYbW.png"/>

----

## 3. 檔案內容
### `body_part.ref`
- 當有發現需要加入新的判斷句型，且與患者身體部位相關請使用這個檔案，請點擊雙紅底線處以增加句型，入句型後請按下右方的單句分析，請見下圖。
![](https://upload.cc/i1/2021/03/12/ahgqQU.png)

- 請勾選參數(即文字後的方框)，一旦勾選表示該詞彙容易變動，完成後請按下模型生成按鈕，如下圖中的雙紅線處。即完成新的句型的建置
![](https://upload.cc/i1/2021/03/12/Dxe3s4.png)

### `symptom.ref`
- 使用時機為，如果想要加入新句型，且與較屬於病症(如暈眩、飛蚊症等等)，即加入此類。
- 建置方法如上檔案
