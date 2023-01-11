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

from pprint import pprint
from requests import post
from requests import codes
import json
import math
import os
try:
    from intent import Loki_Weather
except:
    from .intent import Loki_Weather

BASEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"

try:
    infoPath = "{}/account.info".format(BASEPATH.replace("/WeatherMan", ""))
    infoDICT = json.load(open(infoPath, "r"))
    USERNAME = infoDICT["username"]
    LOKI_KEY = infoDICT["WeatherMan_loki_key"]
except:
    # HINT: 在這裡填入您在 https://api.droidtown.co 的帳號、Articut 的 API_Key 以及 Loki 專案的 Loki_Key
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
    #視需要做些正規化的操作 (例如「台/臺」或是 "11:30" 變為「十一點三十」)
    lokiRst = LokiResult([x.replace("台", "臺") for x in inputLIST], filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            # 正常輸入
            if lokiRst.getLokiLen(index) > 0:
                for resultIndex in range(0, lokiRst.getLokiLen(index)):
                    # Weather
                    if lokiRst.getIntent(index, resultIndex) == "Weather":
                        resultDICT = Loki_Weather.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)
            # 錯誤輸入
            else:
                resultDICT[key] = {'answer': "我只是個天氣機器人，如果您發現我無法理解您的話，可能是因為您的輸入有語法錯誤或是我的知識範圍無法回答您的問題。請再次檢查您的輸入，或著提出其他的話題以便我幫助您。"}
    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)


if __name__ == "__main__":
    # Weather
    print("[TEST] Weather")
    inputLIST = [
                 #'今天台北熱不熱',
                 #'今天台北會下雨嗎',
                 #'台北今天可以不用帶傘嗎',
                 #'今天台北可以不用帶傘嗎',
                 #'今天台北需不需要帶傘',
                 #'今天台北需不需要帶陽傘',
                 #'今天台北中午過後天氣如何',
                 #'後天晚上台北適合慢跑嗎',
                 #'今天台北午後天氣如何',
                 #'今天台北很熱嗎',
                 #'今天台北會熱嗎',
                 #'今天台北熱嗎',
                 #'今天台北是不是很熱',
                 #'台北今天很熱嗎',
                 #'台北今天會很熱嗎',
                 #'台北今天會熱嗎',
                 #'台北今天熱嗎',
                 #'台北今天是不是很熱',
                 #'今天台北會不會下雨',
                 #'今天天氣好嗎',
                 #'今天天氣怎麼樣',
                 #'今天中午過後台北天氣如何',
                 #'今天午後台北天氣如何',
                 #'今天晚上氣溫如何',
                 #'今日台北體感溫度',
                 #'今日白日氣溫',
                 #'今日白日氣溫如何',
                 #'今日夜晚氣溫',
                 #'台北今天會下雨嗎',
                 #'台北今天熱不熱',
                 #'台北今天會不會下雨',
                 #'台北今天需不需要帶陽傘',
                 #'台北今天需不需要帶傘',
                 #'台北今天中午過後天氣如何',
                 #'台北今天午後天氣如何',
                 #'台北天氣',
                 #'台北天氣如何',
                 #'台北天氣怎麼樣',
                 #'台北後天晚上適合慢跑嗎',
                 #'台北明天天氣',
                 #'台北晚上下雨嗎',
                 #'台北晚上要帶傘嗎',
                 #'台北氣象報告',
                 #'明天台北天氣',
                 #'今天天氣是否熱',
                 #'今天的天氣是溫暖還是寒冷',
                ]
    #testLoki(inputLIST, ['Weather'])
    #print("")

    # 輸入其它句子試看看
    #inputLIST = ["輸入你的內容1", "輸入你的內容2"]
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Result => ")
    pprint(resultDICT)