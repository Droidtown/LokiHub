# 恐懼貪婪指數機器人

#### 不同於CNN的恐懼貪婪指數，我們背後運用到的是語意理解所做出的市場投資情緒，是利用網路輿情所訓練出的模型

![恐懼貪婪指數](https://raw.githubusercontent.com/Chenct-jonathan/final-project/main/img/FearGreed.png)

指標定義：<br>
極度恐懼（Extreme Fear）為0-25           
恐懼（Fear）為26-44                       
中立（Neutral）為45-55                     
貪婪（Greed）為56-74                   
極度貪婪（Extreme Greed)為75-100<br>
#### 由此可知，數字愈小反映出市場呈現愈恐懼的狀態；數字愈大表示市場愈貪婪。

## 環境設定
##### Step1. 進入[卓騰語言科技](https://www.droidtown.co/zh-tw/)註冊帳號<br>
##### Step2. 點選Loki服務，建立新專案並命名為"FearGreed"<br>
##### Step3. 新增檔名為account.info<br>
{username：申請卓騰語言科技的帳號,<br>apikey：Articut中的API金鑰,<br>
lokikey：FearGreed專案的金鑰,<br>
discord＿token：申請discord機器人的APPLICATION ID}
![](https://github.com/Chenct-jonathan/final-project/blob/main/img/account.info%E7%AF%84%E4%BE%8B.jpg?raw=true)
##### Step4. 將refs資料夾內的五個ref檔下載後一一上傳至FearGreed專案內並逐一按"全句分析"及"生成模型"<br>
##### Step5. 最後，將"finalproject"內的py檔打開，並執行final_project.py即可做測試

***歡迎與我們聯絡：<br>
陳畯田chenjonathan901210@gmail.com<br>
高芷茜kao86200@gmail.com***
