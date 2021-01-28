#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 2.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No Match Intent!"
                }
            ]
        }
"""

import requests
try:
    from intent import Loki_baseball
    from intent import Loki_badminton
except:
    from .intent import Loki_baseball
    from .intent import Loki_badminton

from ArticutAPI import ArticutAPI
articut = ArticutAPI.Articut()
import re
import math

LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = ""
LOKI_KEY = ""
# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []

        try:
            result = requests.post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": INTENT_FILTER
            })

            if result.status_code == requests.codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "Connect failed."
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST):
    resultDICT = {}
    resultDICT["baseball"] = 0
    resultDICT["badminton"] = 0
    lokiRst = LokiResult(inputLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # baseball
                if lokiRst.getIntent(index, resultIndex) == "baseball":
                    resultDICT = Loki_baseball.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # badminton
                if lokiRst.getIntent(index, resultIndex) == "badminton":
                    resultDICT = Loki_badminton.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

#看文本對到baseball的句子有幾個，看相似度
if __name__ == "__main__":
    articut = ArticutAPI.Articut(username="xww1748.fl06@g2.nctu.edu.tw", apikey="Lm%gmjE9UxFJLm%S4JKz$Zhcf*AqI_p")
    countBaseball = 0 # 對到幾個棒球的句子
    countBadminton = 0 # 對到幾個羽球的句子
    pat = "</?[a-zA-Z]+?_?[a-zA-Z]+?>"
    #inputLIST = ["輸入你的內容1", "輸入你的內容2"]
    inputSTR = """次局戴資穎很快取得6比2領先，但小戴出現較多失誤，先讓布里西費特5分首度取得領先，7平後又被對手打出一波6比1攻勢，但小戴努力追趕，在16比20的情況下先化解對手4個局末點，逼成「丟士」，隨後在22比21、自己首個賽末點就成功兌現，搶下冠軍戰門票。"""
    parseResultDICT = articut.parse(inputSTR)
    inputLIST = []
    for p in parseResultDICT["result_pos"]:
        if len(p) == 1:
            pass
        else:
            inputLIST.append(re.sub(pat, "", p))
    for i in range(math.ceil(len(inputLIST)/20)):
        resultDICT = runLoki(inputLIST[i*20:(i+1)*20])
        countBaseball += resultDICT["baseball"] # 對到的句子數量加進去，避免在runLoki歸0
        countBadminton += resultDICT["badminton"]
    print("Baseball Score:", countBaseball)
    print("Badminton Score:", countBadminton)
    cwNum = len(articut.getContentWordLIST(parseResultDICT)) # get [content_word] number
    print("Baseball similar:",countBaseball/cwNum) # 對到的/content_word = 相似度
    print("Badminton similar:",countBadminton/cwNum)
    #print(cwNum)
    #print("Result => {}".format(resultDICT))