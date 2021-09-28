# Discord 檔案使用說明
## 1. 檔案內容
在Discord這個資料夾中，有一個資料夾`intent`，以及三個.py檔案：`BeautiBot_For_Appointment.py`,`BeautiBot_Loki.py`,`botREF.py`

----
## 2. 環境設定
### 如果想要在Discord上建立自己的Chatbot，請參考：[How to Make a Discord Bot in Python](https://realpython.com/how-to-make-a-discord-bot-python)
----

## 3. 檔案內容
###  `intent`資料夾
這個資料夾存取了七個Loki意圖，包括：Loki_appointmentClinic, Loki_appointmentDoctor, Loki_appointmentTime, Loki_bodypart, Loki_confirm, Loki_medicalHistory以及Loki_request。這些Loki意圖分別處理客戶進行醫美療程預約時會使用到的資訊，分別為預約診所、預約醫師、預約時間、欲施作療程的身體部位、療程確認、個人醫療史以及是否有施作醫美療程的要求。

### `BeautiBot_For_Appointment.py`
本程式用於在Discord上驅動我們的聊天機器人BeautiBot。

### `BeautiBot_Loki.py`
本程式為Loki的主程式，用於串連Loki的各項意圖。

### `botREF.py`
本程式儲存所有在前述兩支程式所需的LIST與DICT。