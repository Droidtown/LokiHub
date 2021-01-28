#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
$ pip3 install flask
"""

from flask import Flask
from flask import request
from flask import jsonify
from line_sdk import Linebot

from DrugBot import runLoki as drugbot

LINE_ACCESS_TOKEN   = "HkK5QBdyLPYKiNKrxL/e0yiir4sb2/7xJd3cfqDeePOhGabHYzCNzrq3oleK0cwLT+huhni7sQ34Qo9tiEMl2UCx7U7aGIfVJIZr7QHRLUvuQEV9Vt/dWsWVEWJQHk+UM0TuCMZqP8wd1IHF8cE+aAdB04t89/1O/w1cDnyilFU="
LINE_CHANNEL_SECRET = "cb223c772a0d9819cd81bee1aeb6ea13"

app = Flask(__name__)

@app.route("/Lanlanlu/", methods=["GET", "POST"])
def webhook():
    # GET
    if request.method == "GET":
        return jsonify({"status": True, "msg": "Line Webhook Success."})

    # POST
    elif request.method == "POST":
        body = request.get_data(as_text=True)
        signature = request.headers["X-Line-Signature"]

        # Line
        linebot = Linebot(LINE_ACCESS_TOKEN, LINE_CHANNEL_SECRET)

        # dataLIST = [{status, type, message, userID, replyToken, timestamp}]
        # replyToken=聊天室ID , message=送過來的內容
        
        dataLIST = linebot.parse(body, signature)
        for dataDICT in dataLIST:
            if dataDICT["status"]:
                if dataDICT["type"] == "message":
                    # Send Message

                    #dataDICT["message"]是input的string，用[]包起來變InputLIST傳給RunLoki
                    response = drugbot([dataDICT["message"]])
                    linebot.respTexts(dataDICT["replyToken"], ["以下為查詢結果：\n", response])
                    
                    #linebot.respText(dataDICT["replyToken"], "咩噗") #回應到哪裡
                    #linebot.respText(dataDICT["replyToken"], dataDICT["message"]) #回應跟input一樣的回答

        return jsonify({"status": True, "msg": "Line Webhook Success."})

    # OTHER
    else:
        return jsonify({"status": False, "msg": "HTTP_405_METHOD_NOT_ALLOWED"})





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8006)