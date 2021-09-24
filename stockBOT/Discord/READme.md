# **在**Discord上建立stockBOT

### 操作說明

#### 建立Loki專案stockBOT

1. 下載本資料夾的檔案

2. 登入[卓騰語言科技](https://api.droidtown.co/)

3. 點選畫面上方的**工具**進入**[Loki：語意理解引擎](https://api.droidtown.co/loki/)**

   ![Loki](https://github.com/sydneylin0218/Picture/blob/main/Loki.png?raw=true)

4. 在空白欄中輸入專案名稱stockBOT，再點選建立專案

   ![建立專案](https://github.com/sydneylin0218/Picture/blob/main/%E5%BB%BA%E7%AB%8B%E5%B0%88%E6%A1%88.png?raw=true)

5. 點選新建立的專案名稱進入專案

   ![進入專案](https://github.com/sydneylin0218/Picture/blob/main/%E5%BB%BA%E7%AB%8B%E5%B0%88%E6%A1%88_2.png?raw=true)

6. 進入專案後點選畫面下方的**選擇檔案**，選擇**ref**資料夾中的六個**ref**檔案

   ![讀取意圖](https://github.com/sydneylin0218/Picture/blob/main/REF.png?raw=true)

7. 點選**讀取意圖**

   ![讀取意圖](https://github.com/sydneylin0218/Picture/blob/main/%E8%AE%80%E5%8F%96%E6%84%8F%E5%9C%96.png?raw=true)

8. 點進意圖**symbol**

9. 下拉到**4. 勾選所選意圖所需參數的部分**進行設定，除了**年成長率**以外全部勾選

   ![symbol](https://github.com/sydneylin0218/Picture/blob/main/symbol.png?raw=true)

10. 生成模型**symbol**

   ![生成模型](https://github.com/sydneylin0218/Picture/blob/main/%E7%94%9F%E6%88%90%E6%A8%A1%E5%9E%8B.png?raw=true)

11. 點進意圖**profitability**

12. 下拉到**4. 勾選所選意圖所需參數的部分**進行設定，在**參數勾選工具**中輸入**聯發科**，再點選**全部勾選**

    ![profitability](https://github.com/sydneylin0218/Picture/blob/main/profitability.png?raw=true)

13. 生成模型**profitability**

    ![生成模型](https://github.com/sydneylin0218/Picture/blob/main/%E7%94%9F%E6%88%90%E6%A8%A1%E5%9E%8B_pro.png?raw=true)

14. 點進意圖**safty**

15. 下拉到**4. 勾選所選意圖所需參數的部分**進行設定，選取**聯發科**跟**股票**

    ![safty](https://github.com/sydneylin0218/Picture/blob/main/safety2.png?raw=true)

16. 生成模型**safty**

    ![生成模型](https://github.com/sydneylin0218/Picture/blob/main/%E7%94%9F%E6%88%90%E6%A8%A1%E5%9E%8B_safty.png?raw=true)

17. 點進意圖**growth**

18. 下拉到**4. 勾選所選意圖所需參數的部分**進行設定，選取**聯發科**

    ![勾選意圖](https://github.com/sydneylin0218/Picture/blob/main/%E7%94%9F%E6%88%90%E6%A8%A1%E5%9E%8B_growth.png?raw=true)

19. 生成模型**growth**

    ![](https://github.com/sydneylin0218/Picture/blob/main/%E6%A8%A1%E5%9E%8B_growth.png?raw=true)

20. 點進意圖**information**

21. 下拉到**4. 勾選所選意圖所需參數的部分**進行設定，選取**台積電**、**基本資料**與**資料**

    ![](https://github.com/sydneylin0218/Picture/blob/main/%E6%84%8F%E5%9C%96_info.png?raw=true)

22. 生成模型**imformation**

    ![](https://github.com/sydneylin0218/Picture/blob/main/%E7%94%9F%E6%88%90%E6%A8%A1%E5%9E%8B_info.png?raw=true)

23. 點進意圖what_is

24. 下拉到**4. 勾選所選意圖所需參數的部分**進行設定，選取**償債能力**

    ![意圖](https://github.com/sydneylin0218/Picture/blob/main/%E6%84%8F%E5%9C%96_what_is.png?raw=true)

25. 生成模型what_is

    ![模型what_is](https://github.com/sydneylin0218/Picture/blob/main/%E6%A8%A1%E5%9E%8B_what_is.png?raw=true)

26. 回到[Loki頁面](https://api.droidtown.co/loki/)

27. 複製stockBOT的金鑰

    ![KEY](https://github.com/sydneylin0218/Picture/blob/main/key.png?raw=true)

28. 打開**stockBOT_Loki**的檔案，分別在**username**、**lokikey**的地方填入**帳號名**與剛剛複製的**Loki金鑰**

    ```LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
    USERNAME = 
    LOKI_KEY = 
    ```

29. 存檔後即完成Loki部分的設定

#### 在Discord上建立stockBOT

1. 登入**[Dicscord](https://discord.com/login?redirect_to=%2Fdevelopers)**

   ![discord](https://github.com/sydneylin0218/Picture/blob/main/discord.png?raw=true)

2. 進入[DEVELOPER PORTAL](https://discord.com/developers/applications)

3. 點擊畫面右上方的**New Application**按鈕

   ![new_application](https://github.com/sydneylin0218/Picture/blob/main/new_application.png?raw=true)

4. 為這個BOT取個名字

   ![取名](https://github.com/sydneylin0218/Picture/blob/main/BOT%E5%8F%96%E5%90%8D2.png?raw=true)

5. 建立成功後，點選左側邊攔Bot進入頁面，再按**Add bot**按鈕

   ![add_a_bot](https://github.com/sydneylin0218/Picture/blob/main/add_a_bot.png?raw=true)

6. 完成後按下**copy**複製**token**

   ![copy_token.png](https://github.com/sydneylin0218/Picture/blob/main/copy_token.png?raw=true)

7. 打開**stockBOT_Discord.py**填入**token**

8. 在填入**stockBOT.py**檔中**token**

   ![token](https://github.com/sydneylin0218/Picture/blob/main/token.png?raw=true)

9. 回到開發者頁面並點選左側邊欄位的OAuth2，接著勾選BOT後複製連結

   ![](https://github.com/sydneylin0218/Picture/blob/main/%E5%8A%A0%E5%85%A5BOT.png?raw=true)

10. 利用此連結把BOT加入**discord**聊天室中

11. 執行**stockBOT_Discord.py**檔案後可以開始測試BOT

#### 輸入範例

1. 公司查詢基本資料

   ![基本資料](https://github.com/sydneylin0218/Picture/blob/main/%E7%AF%84%E4%BE%8B_%E5%9F%BA%E6%9C%AC%E8%B3%87%E6%96%99.png?raw=true)

2. 查詢最近公布的財報資料中，這家公司在安全性、成長性跟獲利性的表現

   ![安全性](https://github.com/sydneylin0218/Picture/blob/main/%E5%AE%89%E5%85%A8%E6%80%A7.png?raw=true)

   ![成長力](https://github.com/sydneylin0218/Picture/blob/main/%E6%88%90%E9%95%B7%E5%8A%9B.png?raw=true)

3. 查詢專有名詞

   ![專有名詞](https://github.com/sydneylin0218/Picture/blob/main/%E5%90%8D%E8%A9%9E%E8%A7%A3%E9%87%8B.png?raw=true)

#### 加入欲查詢的股票

目前這個BOT可以查詢上市半導體類股、食品類股、運輸類股還有營建類股的股票，如果要增加其他檔股票，可以到DICT.py的companyDICT字典中，以**"股票代碼"：["公司名稱","股票代碼"]**的格式增加公司名稱與股票代碼。

![DICT](https://github.com/sydneylin0218/Picture/blob/main/DICT.png?raw=true)
