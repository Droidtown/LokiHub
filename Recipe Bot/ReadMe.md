# ReadMe.md

# Recipe Bot 冰箱食譜小助手

## 下班下課後打開冰箱，望著琳琅滿目的食材，卻不知道從哪裡下手嗎？

### 用聊天的方式和 Recipe bot 溝通你有的食材、要做的份數、預期上菜的時間，Recipe bot 就會推薦給你適合的食譜！

## Recipe Bot 使用步驟：

- 先 @RecipeBot 說 哈囉、嗨、你好、hi、hello ，喚醒機器人

1. 食材階段：告訴 Bot 你有什麼食材

   使用者：我有番茄和雞蛋
   Recipebot：好的，現在我們有番茄和雞蛋，請問要做幾人份的料理呢？

![螢幕擷取畫面 2025-08-29 155554.png](%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2_2025-08-29_155554.png)

2. 份數階段：說明要做幾人份

   使用者：兩人份
   Recipebot：2人份，沒問題！預計多久上菜呢？

![螢幕擷取畫面 2025-08-29 155706.png](%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2_2025-08-29_155706.png)

3. 時間階段：告知預期的烹飪時間
   
   使用者：30分鐘內
   Recipebot：開始推薦食譜...

![螢幕擷取畫面 2025-08-29 155722.png](%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2_2025-08-29_155722.png)

![螢幕擷取畫面 2025-08-29 155739.png](%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2_2025-08-29_155739.png)

- 若不滿意當前食譜，可以“換一個”、”不要”…

![螢幕擷取畫面 2025-08-29 155756.png](%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2_2025-08-29_155756.png)

![螢幕擷取畫面 2025-08-29 155815.png](%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2_2025-08-29_155815.png)

### 專案結構

```markdown
RecipeBot/
├── main.py
├── account.info
├── Discord_Recipebot       # Discord bot 主程式
├── recipe_recommender.py   # 食譜推薦邏輯     
├── response_manager.py     # 回應管理器
├── conversation_flow.py    # 流程處理
├── USER_DEFINED.json       # 自定義詞典
├── intent/                 # Loki intent 模組
│   ├── Loki_ingredient.py  # 食材意圖
│   ├── Loki_serving.py     # 份數意圖
│   └── Loki_time_limit.py  # 時間意圖
├── ref/                    # 建立意圖所需的 ref 檔
│   ├── ingredient.ref
│   ├── serving.ref
│   ├── time_limit.ref
├── lib/                   
│   ├── Account.py       
│   ├── LLM.py       
│   └── Project.py
└── README.md

```

# 設定說明

---

先下載這份專案文件

### **環境設置**

```jsx
Python 3.12.6
pip3 install ArticutAPI
pip3 install requests
```

## 在 LOKI 建立專案

搜尋卓騰並註冊帳號

![螢幕擷取畫面 2025-08-30 153836.png](%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2_2025-08-30_153836.png)

點開會員下拉選單 > 選取產品服務 LOKI >開始使用 LOKI

在最上方的欄位 「建立專案」輸入專案名稱「Recipebot」

![螢幕擷取畫面 2025-08-30 154649.png](%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2_2025-08-30_154649.png)

點入新建的專案「Recipebot」裡面 > 點選右上方的 「匯入意圖」

左方欄位選擇「Articut Model」，匯入專案文件裡的三個 ref 檔，就會建立三個意圖

![螢幕擷取畫面 2025-08-29 170428.png](%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2_2025-08-29_170428.png)

在「設定生成模型」打開「Chatbot 模式」，並選擇 LLM 

![螢幕擷取畫面 2025-08-29 170504.png](%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2_2025-08-29_170504.png)

回到上一頁 (LOKI 主頁)，複製專案的 LOKI key > 貼到專案文件裡的 account.info

再回到上一頁 (產品服務)，點選 Articut 複製下面的 api key > 貼到專案文件裡的 account.info

![螢幕擷取畫面 2025-08-30 163806.png](%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2_2025-08-30_163806.png)

```jsx
{
"username":"填入Loki註冊信箱",
"api_key" :"填入ArticutAPI金鑰",
"loki_key":"填入專案金鑰"
"discord_token": "填入機器人的discord token"}
```

## **建立Discord Bot**

1. 進入Discord開發者頁面
2. 註冊後登入帳號，點左上角的 Application
3. 點選 New Application
4. 在 Create an application 下面 Name 的欄位輸入 RecipeBot (你為 bot 取的名字)
5. 從左邊的的欄位按下「Bot」後，再點擊畫面最右邊的「Add Bot」
6. 輸入Bot名稱，並複製 token
7. 填入account.info的 discord_token 
8. 從左邊的欄位按下「OAuth2」後，再從SCOPES裡面點「bot」，接著複製連結
9. 在瀏覽器貼上連結，並將機器人加入伺服器
10. 執行 Discord_Recipebot.py
11. 可以開始測試 Recipebot 了！

## **Contact Me**
zoe29819@gmail.com
