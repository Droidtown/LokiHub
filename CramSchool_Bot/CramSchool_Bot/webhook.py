from flask import Flask, request, jsonify

# 載入 json 標準函式庫，處理回傳的資料格式
import json

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

#從Loki叫過來
from CramSchool_Bot import execLoki
import pandas as pd

app = Flask(__name__)
access_token = '2888VCjR7/N/m0BaPi0UbXOAGSZXw8AjmUVjedz2e1bJABAToyvTTaAlI+itamNT3ummLB0BbHzfZBvsXr1sw/I/Ultb6RCG8MdGtCBBxHrRa/D1bW5I1TJlrg2+U31JOzBpevhhci+avlkTRAYSiwdB04t89/1O/w1cDnyilFU='
secret = '995ae6fdeb97bfdceb37a8789b5e9ef6'
line_bot_api = LineBotApi(access_token)              # 確認 token 是否正確
handler = WebhookHandler(secret)                     # 確認 secret 是否正確

user_state = {}

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)                    # 取得收到的訊息內容
    try:
        json_data = json.loads(body)                         # json 格式化訊息內容
        signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
        handler.handle(body, signature)                      # 綁定訊息回傳的相關資訊
        
        user_id = json_data['events'][0]['source']['userId']
        tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
        type = json_data['events'][0]['message']['type']     # 取得 LINe 收到的訊息類型
        
        if type=='text':
            msg = json_data['events'][0]['message']['text']  # 取得 LINE 收到的文字訊息
            if msg == '重新詢問':
                    user_state[user_id] = {'step': 'ask_username'}
                    reply = "請輸入您的使用者名稱以便重新查詢。"
            elif user_id not in user_state:
                user_state[user_id] = {'step': 'ask_username'}
                current_step = user_state[user_id]['step']
                reply = "請輸入使用者名稱"
            else:
                current_step = user_state[user_id].get('step', 'ask_username')
                if current_step == 'ask_username':
                    user_state[user_id]['username'] = msg  # 保存使用者輸入的 username
                    user_state[user_id]['step'] = 'ask_matter'  # 更新狀態到下一步
                    reply = "請問您需要什麼資料？"
                elif current_step == 'ask_matter': 
                    username_input = user_state[user_id]['username']
                    matter = msg  
                    user_state[user_id]['step'] = 'complete'             
                    filterLIST = []
                    refDICT = {"Class": [], "Need": [], "Chapter": []}
                    resultDICT = execLoki([matter], filterLIST=filterLIST, refDICT=refDICT)
                    sheet = resultDICT['Class'][0]
                    df = pd.read_excel('DT 補習班.xlsx', sheet_name=sheet)
                    filtered_rows = df[df['Username'] == user_state[user_id]['username']]
                    if resultDICT['Need'] == []:
                        choice = resultDICT['Chapter'][0]
                    else: 
                        choice = resultDICT['Need'][0]    
                    columns_to_keep = ['Username', '姓名', choice]
                    filtered_columns = filtered_rows[columns_to_keep]
                    reply = f"{filtered_columns}"
                else:
                    reply = "對話結束，輸入[重新詢問]，可再查詢其他資訊，謝謝！"
        else:
            reply = '你傳的不是文字呦～'

        line_bot_api.reply_message(tk,TextSendMessage(reply))# 回傳訊息
    except:
        print(body)                                          # 如果發生錯誤，印出收到的內容
    return 'OK'                                              # 驗證 Webhook 使用，不能省略

if __name__ == "__main__":
    app.run()

