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

from requests import post
from requests import codes
import math
try:
    from intent import Loki_Inquiry
    from intent import Loki_Location
    from intent import Loki_Career
    from intent import Loki_Company
except:
    from .intent import Loki_Inquiry
    from .intent import Loki_Location
    from .intent import Loki_Career
    from .intent import Loki_Company


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = "waiting.hchs@gmail.com"
LOKI_KEY = "XB*g%RrvHV4VMbuNhC@sCp+2^wHN$HF"
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

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
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

def runLoki(inputLIST, filterLIST=[]):
    resultDICT = {}
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # Inquiry
                if lokiRst.getIntent(index, resultIndex) == "Inquiry":
                    resultDICT = Loki_Inquiry.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # Location
                if lokiRst.getIntent(index, resultIndex) == "Location":
                    resultDICT = Loki_Location.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # Career
                if lokiRst.getIntent(index, resultIndex) == "Career":
                    resultDICT = Loki_Career.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # Company
                if lokiRst.getIntent(index, resultIndex) == "Company":
                    resultDICT = Loki_Company.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)


if __name__ == "__main__":
    # Inquiry
    #print("[TEST] Inquiry")
    #inputLIST = ['我要找成大外文系','我要找成大和台大外文系','我要找台大外文系和資訊系','我要找成大外文系和台大資訊系']
    #testLoki(inputLIST, ['Inquiry'])
    #print("")

    ## Location
    #print("[TEST] Location")
    #inputLIST = ['我要找台北市外文系','我要找台北和新竹外文系','我要找台北外文系和台中電機系']
    #testLoki(inputLIST, ['Location'])
    #print("")

    ## Career
    #print("[TEST] Career")
    #inputLIST = ['我想要當廚師','我要去拍攝電影','我要做煮飯的工作']
    #testLoki(inputLIST, ['Career'])
    #print("")

    ## Company
    #print("[TEST] Company")
    #inputLIST = ['我要去微軟上班','我要去聯發科工作']
    #testLoki(inputLIST, ['Company'])
    #print("")

    # 輸入其它句子試看看
    inputLIST = ["我想找成大外文系"]
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Result => {}".format(resultDICT))


    '{"destination":"Uc2436f4eee716f819544ec6d26d76f44","events":[{"type":"message","message":{"type":"text","id":"14791050218909","text":"人類"},"timestamp":1632322310046,"source":{"type":"user","userId":"Ufdbe56ce99a0dadb2365ba03605b70b1"},"replyToken":"c05cb953dff643f39f0f5937d0e51d28","mode":"active"}]}'