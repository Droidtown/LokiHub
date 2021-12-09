#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask
from flask import request
from flask import jsonify
from line_sdk import Linebot

LINE_ACCESS_TOKEN   = ""
LINE_CHANNEL_SECRET = ""

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def webhook():
    # GET
    if request.method == "GET":
        return "Line Webhook Success."

    # POST
    elif request.method == "POST":
        body = request.get_data(as_text=True)
        signature = request.headers["X-Line-Signature"]

        # Line
        linebot = Linebot(LINE_ACCESS_TOKEN, LINE_CHANNEL_SECRET)

        # dataLIST = [{status, type, message, userID, replyToken, timestamp}]
        # replyToken = 回覆需要的ID , message = 使用者輸入的內容

        dataLIST = linebot.parse(body, signature)
        for dataDICT in dataLIST:
            if dataDICT["status"]:
                if dataDICT["type"] == "message":
                    try:
                        # 這裡輸入客製化內容
                        # dataDICT["message"] => 使用者輸入的內容
                        msgSTR = "[MSG] {}".format(dataDICT["message"])
                    except Exception as e:
                        msgSTR = "[ERROR] {}".format(str(e))

                    # respText(聊天室ID, 要回覆的內容)
                    linebot.respText(dataDICT["replyToken"], msgSTR)

        return jsonify({"status": True, "msg": "Line Webhook Success."})

    # OTHER
    else:
        return "HTTP_405_METHOD_NOT_ALLOWED"


if __name__ == "__main__":
    app.run()