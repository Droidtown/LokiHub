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
    from intent import Loki_Exchange
except:
    from .intent import Loki_Exchange

from ArticutAPI import ArticutAPI

articut = ArticutAPI.Articut()


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = "peter.w@droidtown.co"
LOKI_KEY = "zhQi3kkkS$z^Ssv&$YsK4oYrXz6F@ab"
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
    lokiRst = LokiResult(inputLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # Exchange
                if lokiRst.getIntent(index, resultIndex) == "Exchange":
                    resultDICT = Loki_Exchange.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def getTodayExchangeRage():
    response = requests.get("https://tw.rter.info/capi.php")
    rateDICT = response.json()
    return rateDICT

def moneyName(inputSTR):
    moneyDICT = {"歐元": "EUR",
                 "美金": "USD",
                 "日幣": "JPY"}
    return moneyDICT[inputSTR]

def amountSTRConvert(inputSTR):
    resultDICT = articut.parse(inputSTR, level="lv3")
    return resultDICT["number"]


if __name__ == "__main__":
    inputLIST = ["歐元500元要多少日幣"]
    resultDICT = runLoki(inputLIST)
    print("Result => {}".format(resultDICT))
    src = moneyName(resultDICT["src"])
    tgt = moneyName(resultDICT["tgt"])
    amt = amountSTRConvert("五十萬")
    print("金額數字：", amt)