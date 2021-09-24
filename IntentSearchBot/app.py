#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pprint import pprint
import os
import json
from latent_search_engine import se
from IOHbot import LokiResult, runLoki
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot import (
    LineBotApi, WebhookHandler
)
from flask import Flask, request, abort
LINE_ACCESS_TOKEN = "tYSPdyTRv4Y2SOM8pNrlx5B8wckzD/XnICBhr9YCOtqgc38cbSY79IZZG6tXLA9sweiQPr3j8WX9zYLvFBwxUw2um2G/BDVViOAGSETqYAIPLFiTVoGE9qHj37YRSHOLbRgvM+vnC+wRfiatoPhmwAdB04t89/1O/w1cDnyilFU="
LINE_CHANNEL_SECRET = "862e704472f1a37fe1e7f006b9563fac"


app = Flask(__name__)

line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


def loadJson(filename):
    basedir = os.path.abspath(os.path.dirname(__file__))
    print(basedir)
    data_file = os.path.join(basedir, filename)
    print(data_file)
    with open(data_file, "r") as f:
        result = json.load(f)
    return result


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    msg = request.get_json()
    # pprint(msg)
    # text = msg['events'][0]['message']['text']

    app.logger.info("Request body: " + body)
    # inputLIST = [text] 
    # filterLIST = []
    # resultDICT = runLoki(inputLIST, filterLIST)
    # print("Result => {}".format(resultDICT))

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


from collections import defaultdict
session = defaultdict(list)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    pprint(event)
    # read in message
    text = event.message.text
    print(text)
    # session[event.message.id].append(text)
    # keywords.append(text)
    inputLIST = [text]
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)


    # read in json files
    # uniName = loadJson("school_name_dict.json")  # DICT
    # deptName = loadJson("dept_name_dict.json")

    content = "不好意思，我看不懂，要不要試著像個人類一樣說話呢？"


    loki_keys = resultDICT.values()
    flat_loki_keys = [item for sublist in loki_keys for item in sublist]

    user_id = event.source.user_id
    # print("="*20)
    # print(session)
    session[user_id].extend(flat_loki_keys)
    # print(session[user_id])
    
    query_machine = se.HippoChamber()
    query_machine.vectorize()
    
    num = -1
    keys = set()
    keywords = session[user_id]
    print(keywords)
    
    for key in keywords:
        sim_sorted = query_machine.get_similar_articles(query=key)
        key_list = [k for k, v in sim_sorted if v > 0.0]
        print(key, len(key_list))
        if num == -1:
            keys = set(key_list)
        else:
            print(type(keys))
            keys = set(key_list) & keys
        num = len(keys)

    print(num)

    num = max(num, 0)

    if 0 < num <= 10:
        result = list(keys)
        result_content = []
        for r in result:
            res = query_machine.source_doc[r]
            result_content.append(res[0])
            result_content.append(res[1])
        content = "\n".join(result_content)
        print(content)
        session[user_id] = []
    elif num == 0:
        content = "不好意思，目前IOH還沒有相關科系的分享"
        session[user_id] = []
    else:
        content = f"哇！你有興趣的內容在IOH上面有{num}篇相關的分享，請再多給我一點提示"



    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=content))


    #line_bot_api.reply_message(
        #event.reply_token,
        #TextSendMessage(text=content))
    

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
