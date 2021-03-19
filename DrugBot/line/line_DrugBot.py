#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
$ pip3 install flask
"""
import requests
import logging
from bs4 import BeautifulSoup
from flask import Flask
from flask import request
from flask import jsonify
from line_sdk import Linebot

from DrugBot import runLoki as drugbot

LINE_ACCESS_TOKEN   = ""
LINE_CHANNEL_SECRET = ""

UserResponseDICT = {}
logging.basicConfig(level=logging.INFO) # 檢查Bug

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
        # replyToken = 聊天室ID , message = 送過來的內容
        
        dataLIST = linebot.parse(body, signature)
        for dataDICT in dataLIST:
            if dataDICT["status"]:
                if dataDICT["type"] == "message":
                    
                    # 多輪對話 - 收集更詳細的資訊
                    if UserResponseDICT != {}:
                        logging.error("UserResponseDICT: ", UserResponseDICT)
                        
                        # 把url中的"藥丸" or "藥片"換成"藥物形狀"
                        if UserResponseDICT["藥丸"] != {}:
                            logging.error("藥丸: ", UserResponseDICT["藥丸"])
                            msgLIST = UserResponseDICT["藥丸"].replace("藥丸",dataDICT["message"])
                            UserResponseDICT["藥丸"]={} # 用完歸0
                            
                        elif UserResponseDICT["藥片"] != {}:
                            logging.error("藥片: ", UserResponseDICT["藥片"])
                            msgLIST = UserResponseDICT["藥片"].replace("藥片",dataDICT["message"])
                            UserResponseDICT["藥片"]={} # 用完歸0
                            
                        # 讀取網頁，查看有無查詢到結果
                        r = requests.get(msgLIST)
                        soup = BeautifulSoup(r.text, 'html.parser')
                        tags = soup.select_one('li.media')
                        if tags == None: # 查無結果
                            linebot.respTexts(dataDICT["replyToken"], ["很抱歉，目前沒有長這個樣子的藥。\n要不要再描述得仔細一點？"])
                        else: # 有查到
                            linebot.respTexts(dataDICT["replyToken"], ["以下為查詢結果：\n", msgLIST])
                            
                    else:
                        # Call RunLoki
                        # dataDICT["message"]是input的string，用[]包起來變 InputLIST 傳給RunLoki
                        responseLIST = drugbot([dataDICT["message"]])
                    
                        # 沒有get到intent
                        if responseLIST == "https://drugs.olc.tw/drugs/outward/":
                            linebot.respTexts(dataDICT["replyToken"], ["這看起來不像藥物的外觀QQ"])
                            
                        # 抓到沒有明確形狀的「藥丸」或「藥片」
                        elif "藥丸" in responseLIST:
                            UserResponseDICT["藥丸"] = responseLIST # 把此次資訊不足的回答存進欄位中，準備進入多輪對話
                            linebot.respTexts(dataDICT["replyToken"], ["請問此藥丸是什麼形狀？"])
                        elif "藥片" in responseLIST:
                            UserResponseDICT["藥片"] = responseLIST # 把此次資訊不足的回答存進欄位中，準備進入多輪對話
                            linebot.respTexts(dataDICT["replyToken"], ["請問此藥片是什麼形狀？"])
                            
                        else:
                            # 讀取網頁，查看有無查詢到結果
                            r = requests.get(responseLIST)
                            soup = BeautifulSoup(r.text, 'html.parser')
                            tags = soup.select_one('li.media')
                            if tags == None: # 查無結果
                                linebot.respTexts(dataDICT["replyToken"], ["很抱歉，目前沒有長這個樣子的藥。\n要不要再描述得仔細一點？"])
                            else: # 有查到
                                linebot.respTexts(dataDICT["replyToken"], ["以下為查詢結果：\n", responseLIST])

        return jsonify({"status": True, "msg": "Line Webhook Success."})

    # OTHER
    else:
        return jsonify({"status": False, "msg": "HTTP_405_METHOD_NOT_ALLOWED"})





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8006)
