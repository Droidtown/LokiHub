# 憂鬱指數評估
## 憂鬱指數計算
### 參考論文
- **Language Use of Depressed and Depression-Vulnerable College Students**
    - Authors: Stephanie S. Rude, Eva-Maria Gortner, and James W. Pennebaker
    
### 抑鬱語言的3種特性
1. 使用更多「第一人稱單數代名詞」，顯著減少使用第二和第三人稱代名詞。
2. 慣常使用「絕對性詞彙」。
3. 大量「負面」的形容詞和副詞。

### 定義權重
- 透過搜集的52篇文本，計算出「第一人稱代名詞」、「絕對性詞彙」以及「負向詞彙」在各文本中的佔比，再分別取出平均值。
- 取得平均值後，計算三者之比。
    - **第一人稱佔比：絕對性詞彙佔比：負向詞彙佔比 ≒ 25：54：21**  
以此比例作為**權重**進行計算。

### 公式
- **憂鬱指數 ＝ 第一人稱佔比 * 25 + 絕對性詞彙佔比 * 54 + 負向詞彙佔比 * 21**  
- 舉例：第一人稱佔比 = 0.98%, 絕對性詞彙佔比 = 7.84%, 負向詞彙佔比 = 1.96%
    - 憂鬱指數  
      = 第一人稱佔比 * 25 + 絕對性詞彙佔比 * 54 + 負向詞彙佔比 * 21  
      = 0.98% * 25 + 7.84% * 54 + 1.96% * 21  
      = 4.90

### 設計目的
- 設計一個可以協助分析使用者文本之憂鬱傾向的LINE Bot。
- 透過代名詞、絕對性詞彙與負向詞彙之佔比，計算**憂鬱指數**。
- 期望讓使用者了解其文本與一般憂鬱文本的相似程度。

### 功能
- 此工具的用途為分析有**潛在憂鬱傾向**的文本。
- 輸入文本後，LINE Bot回傳抑鬱語言的3種特性（代名詞、絕對性詞彙與負向詞彙）之使用情況，並進行憂鬱文本分析，計算憂鬱指數。
- 協助判斷使用者輸入的文本與其他憂鬱文本的相似度。
- 若使用者輸入的文本之憂鬱指數超過***5.5***，代表此文本與其他憂鬱文本之相似度較高。
- 此指數僅提供給使用者作為**參考**。

## 設置環境
` Python 3.8.8 ` 

### 安裝套件
- ArticutAPI
```command
pip install ArticutAPI
```
- Requests
```command
pip install requests
```

### Articut 使用
- 註冊帳號：[卓騰語言科技](https://api.droidtown.co/login/)  
- 複製 Articut API金鑰  
- 編輯 ` account.json `  
    - username：輸入 Droidtown 使用者帳號  
    - apikey：輸入先前複製的 Articut API金鑰    

### 架設平台
- LINE Developers  
- Heroku

## 注意事項
- 由於個人的表達習慣及方式不同，使用的詞彙傾向、頻率也不盡相同。因此，此憂鬱指數**僅供參考**。

## 開始使用
您可以透過輸入LINE Bot ID或是掃QR Code加入好友。
- LINE Bot ID: ` @703xvlcr `
- QR Code  

![QR Code](https://github.com/Melody-Lin/Depression-Language-Evaluation/blob/main/Media/DLE.png "QR Code")
<!-- {:height="50%" width="50%"} -->
<!-- <img src="https://github.com/Melody-Lin/Depression-Language-Evaluation/blob/main/Media/DLE.png" width="200"/> -->

## 使用範例
1. 輸入有**潛在憂鬱傾向的文本**。
2. LINE Bot會回傳代名詞、絕對性詞彙與負向詞彙之使用情況，以及憂鬱文本分析。
![Example](https://github.com/Melody-Lin/Depression-Language-Evaluation/blob/main/Media/Example.jpg "Example")
<!-- <img src="https://github.com/Melody-Lin/Depression-Language-Evaluation/blob/main/Media/Example.jpg" width="400"/> -->

## 聯絡E-Mail
##### <font color=#0000FF>若您有任何疑問，歡迎透過email聯繫我們</font>
- Melody Lin：yiihsuanlin@gmail.com
- Helena Yang：mandy871019@gmail.com




