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
    from intent import Loki_appointmentClinic
    from intent import Loki_bodypart
    from intent import Loki_confirm
    from intent import Loki_request
    from intent import Loki_appointmentTime
    from intent import Loki_medicalHistory
    from intent import Loki_appointmentDoctor
except:
    from .intent import Loki_appointmentClinic
    from .intent import Loki_bodypart
    from .intent import Loki_confirm
    from .intent import Loki_request
    from .intent import Loki_appointmentTime
    from .intent import Loki_medicalHistory
    from .intent import Loki_appointmentDoctor


import re
import json
with open("account.info.py", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())
    
LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = accountDICT["username"]
LOKI_KEY = accountDICT["loki_project_key"]
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
                # appointmentDoctor
                if lokiRst.getIntent(index, resultIndex) == "appointmentDoctor":
                    resultDICT = Loki_appointmentDoctor.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)
                
                # appointmentClinic
                if lokiRst.getIntent(index, resultIndex) == "appointmentClinic":
                    resultDICT = Loki_appointmentClinic.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # bodypart
                if lokiRst.getIntent(index, resultIndex) == "bodypart":
                    resultDICT = Loki_bodypart.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # confirm
                if lokiRst.getIntent(index, resultIndex) == "confirm":
                    resultDICT = Loki_confirm.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # request
                if lokiRst.getIntent(index, resultIndex) == "request":
                    resultDICT = Loki_request.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # appointmentTime
                if lokiRst.getIntent(index, resultIndex) == "appointmentTime":
                    resultDICT = Loki_appointmentTime.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # medicalHistory
                if lokiRst.getIntent(index, resultIndex) == "medicalHistory":
                    resultDICT = Loki_medicalHistory.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)


expandDICT = {"腋下": ["胳肢窩","腋"],
              "比基尼線修型": ["該邊","該逼","胯下","比基尼線","比基尼"],
              "私密處全除": ["私密處","私處","三角地帶","妹妹","黑森林","恥","恥部","陰","陰部","陰毛","下面"],
              "上手臂": ["上臂"],
              "下手臂": ["前臂"],
              "全手": ["整隻手"],
              "手指手背": ["手指","手指頭","指頭","手背","手的背部","手的後面"],
              "全臉": ["整張臉"],
              "髮際線": ["髮線"],
              "眉心唇周下巴": ["眉毛中間","眉毛中間的部分","眉毛中間的位置","兩眉之間","嘴唇附近","嘴唇周邊","嘴唇周圍","嘴巴附近","嘴巴周圍","嘴巴周邊","下顎"],
              "前頸": ["脖子前面","脖子的前面","頸部前面"],
              "後頸": ["脖子後面","脖子的後面","頸部後面"],
              "胸部": ["胸"],
              "腹部": ["肚子"],
              "子母線": ["肚臍附近","肚臍周圍","肚臍周邊","肚臍下面","妊娠線","妊娠中線" ],
              "上背": ["上背部","背部上面","上面的背","上面的背部","背上方","背部上方"],
              "下背": ["下背部","背部下面","下面的背","下面的背部","背下方","背部下方"],
              "臀部": ["屁股","屁屁","屁"],
              "乳暈": ["乳頭周圍","奶頭周圍","乳頭的周圍","奶頭的周圍","乳頭附近","奶頭附近","乳頭的附近","奶頭的附近","乳頭周邊","奶頭周邊","乳頭的周邊","奶頭的周邊"],
              "鼻子": ["鼻","鼻孔"],
              "腳趾腳背": ["腳趾","腳背"],
              "鬍子": ["男性鬍子","鬍鬚"],
              "髮際線": ["髮際","髮線"],
              "腳部": ["腳"]
              }
    
    
def result(inputSTR, intentLIST=[]):
    punctuationPat = re.compile("[,\.\?;，。？、；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n") 
    print(inputLIST)
    
    filterLIST = intentLIST  
    
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Loki Result => {}".format(resultDICT))
        
    
    # get the full bodypart name
    if "bodypart" in resultDICT.keys():
        for full, short in expandDICT.items():
            if resultDICT["bodypart"] in short:
                resultDICT["bodypart"] = full
                print(resultDICT["bodypart"])
            
    if "msg" in resultDICT.keys() and resultDICT["msg"] == "No Match Intent!":
        return False
    else:
        return resultDICT
            

if __name__ == "__main__":
    inputSTR = "王小華醫師星期一有看診嗎"
    print(result(inputSTR))