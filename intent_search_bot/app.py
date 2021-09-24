#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pprint import pprint
import os
import json
from latent_search_engine import se
from nlu.IOHbot import LokiResult, runLoki
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

with open("./linebot.json", encoding="utf-8") as f:
    account_dict = json.loads(f.read())

LINE_ACCESS_TOKEN = account_dict["LINE_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = account_dict["LINE_CHANNEL_SECRET"]


app = Flask(__name__)

line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    msg = request.get_json()

    app.logger.info("Request body: " + body)

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
    text = event.message.text

    inputLIST = [text]
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)

    content = "不好意思，我看不懂，要不要試著像個人類一樣說話呢？"

    loki_keys = resultDICT.values()
    flat_loki_keys = [item for sublist in loki_keys for item in sublist]

    user_id = event.source.user_id
    session[user_id].extend(flat_loki_keys)
    
    query_machine = se.HippoChamber()
    query_machine.vectorize()
    
    num = -1
    keys = set()
    keywords = session[user_id]
    
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
    

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
