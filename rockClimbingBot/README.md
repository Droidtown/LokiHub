# 台灣攀岩 Sport Climbing TW
### 內容列表
- Bot介紹
- 專案目錄
- 環境設置
- Discord Bot建置
- Loki啟用說明
- 參考資料
- 作者
### Bot介紹 
運動攀登，俗稱攀岩，近年來獲得越來越多的關注，亦於2021年東京奧運，首度列為正式運動項目。伴隨著這股熱潮，此Bot應運而生，其提供了想在台灣攀岩的新手會遇到的，各種疑難雜症的解答，舉凡攀岩需要的裝備、治裝花費、攀岩規則、岩點介紹等，都可詢問，即便是老手，也可從對話中快速取得各縣市岩館的資訊。歡迎對攀岩有興趣的朋友下載使用！

### 專案目錄
```txt=.
├── README.md
├── data #會用到的資料集
│    ├── climbingGym.csv
│    ├── defaultResponse.json
│    ├── rocks.json
│    └── what_is.json
├── intent #16種Loki意圖分析
│    ├── Loki_chat.py
│    ├── Loki_equipment_list.py
│    ├── Loki_equipment_price.py
│    ├── Loki_equipment_whereGet.py
│    ├── Loki_equipment_yesNo.py
│    ├── Loki_gym_city.py
│    ├── Loki_gym_distance.py
│    ├── Loki_gym_howMany.py
│    ├── Loki_gym_name.py
│    ├── Loki_gym_price.py
│    ├── Loki_gym_time.py
│    ├── Loki_gym_yesNo.py
│    ├── Loki_location.py
│    ├── Loki_rock.py
│    ├── Loki_rules.py
│    ├── Loki_whatIs.py
│    ├── USER_DEFINED.json
│    └── Updater.py
├── ref #於登入Loki並創建專案後讀取，即可更動原始意圖
│    ├── chat.ref
│    ├── equipment_list.ref
│    ├── equipment_price.ref
│    ├── equipment_whereGet.ref
│    ├── equipment_yesNo.ref
│    ├── gym_city.ref
│    ├── gym_distance.ref
│    ├── gym_howMany.ref
│    ├── gym_name.ref
│    ├── gym_price.ref
│    ├── gym_time.ref
│    ├── gym_yesNo.ref
│    ├── location.ref
│    ├── rock.ref
│    ├── rules.ref
│    └── whatIs.ref
├── rockClimbing.py #主程式
├── Discord_rockClimbing.py #discord連線
├── rockClimbingFunc.py #所有運作主程式會用到的自定義函式
└── rockClimbingNLUmodel.py #連接主程式和discord的NLU模型
```
### 環境設置

### Discord Bot建置

### Loki啟用說明

### 參考資料
- 岩館資料：
  - [轟菌體能](https://shenlee799.com/climbinggyms-taiwan/) 
  - [CRAG FLOW](https://willisclimber.com/taiwanboulderinggym/)
- 岩點資訊及圖片：
    - [HHH-VOCUS](https://vocus.cc/article/62316539fd897800011dbd54)
- 規則及術語：
    - [運動視界](https://www.sportsv.net/articles/86153)
    - [Yinggan Chen-Medium](https://yinggan.medium.com/%E7%B0%A1%E6%98%93%E6%94%80%E5%B2%A9%E8%A1%93%E8%AA%9E%E4%B8%80%E6%AC%A1%E4%BA%86%E8%A7%A3-223387bf04e7)
- NLU模型＆Loki操作
    - [Driodtown Linguistic Tech](https://api.droidtown.co/document/#Loki_9)

### 作者
Ansley Hung
倘若使用上有任何疑問，歡迎提出pull request或透過Email聯繫
 <a href="https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox">ansleyh125@gmail.com</a>
