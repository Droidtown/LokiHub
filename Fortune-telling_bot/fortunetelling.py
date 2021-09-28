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
import json
import random
import pandas as pd
try:
    from intent import Loki_love
    from intent import Loki_destiny
    from intent import Loki_study
    from intent import Loki_career
    from intent import Loki_jobseeking
except:
    from .intent import Loki_love
    from .intent import Loki_destiny
    from .intent import Loki_study
    from .intent import Loki_career
    from .intent import Loki_jobseeking
with open("account.txt", encoding="utf-8") as f:
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
                # love
                if lokiRst.getIntent(index, resultIndex) == "love":
                    resultDICT = Loki_love.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # destiny
                if lokiRst.getIntent(index, resultIndex) == "destiny":
                    resultDICT = Loki_destiny.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # study
                if lokiRst.getIntent(index, resultIndex) == "study":
                    resultDICT = Loki_study.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # career
                if lokiRst.getIntent(index, resultIndex) == "career":
                    resultDICT = Loki_career.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # jobseeking
                if lokiRst.getIntent(index, resultIndex) == "jobseeking":
                    resultDICT = Loki_jobseeking.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)


if __name__ == "__main__":
    ## love
    #print("[TEST] love")
    #inputLIST = ['我單身很久','我想問感情','我想算愛情','我想請問感情','我何時可以脫單','我何時可以脫離單身','我想問感情順不順利','我想算感情順不順利','我想算我會有姻緣嗎','我想問最近的感情狀況','我想問近期的感情狀況','我想問關於感情的部分','我想算關於感情的部分','我想請問最近的感情狀況','我想請問近期的感情狀況','我的愛情運何時才可以順利點','想要請問我的正緣何時才會出現','不知道自己下個桃花何時才會出現','我想請問我跟另一半兩人相處狀況']
    #testLoki(inputLIST, ['love'])
    #print("")

    ## destiny
    #print("[TEST] destiny")
    #inputLIST = ['我想問運勢','我想請問運勢','最近運勢不太好','我想問最近的運勢','我想問運勢順不順利','我想算事業順不順利','我想請問最近的運勢','我想問最近的運勢如何','我想問關於運勢的部分','我想知道發生什麼事了','我想算關於運勢的部分','我想請問最近的運勢如何','我想知道到底發生什麼事了']
    #testLoki(inputLIST, ['destiny'])
    #print("")

    ## study
    #print("[TEST] study")
    #inputLIST = ['會考上嗎?','我想問學業','我想算學業','下禮拜有考試','我今年有考試','我想請問學業','我最近要考試','不知道順不順利','我想問最近的學業','我想知道結果如何','我想問學業順不順利','我想算考試順不順利','我想請問最近的學業','我想問最近的學業如何','我想問關於學業的部分','我想算關於學業的部分']
    #testLoki(inputLIST, ['study'])
    #print("")

    ## career
    #print("[TEST] career")
    #inputLIST = ['我想問事業','我想算事業','我想請問事業','我想問最近的事業','我想問事業順不順利','我想算事業順不順利','我想請問最近的事業','我想問最近的事業如何','我想問關於事業的部分','我想算關於事業的部分','我想問一下最近的事業運','我想問最近的新計畫會不會成功']
    #testLoki(inputLIST, ['career'])
    #print("")

    ## jobseeking
    #print("[TEST] jobseeking")
    #inputLIST = ['我想問求職','我想找工作','我想算求職','我有個面試','我想請問求職','不知道結果如何','我之後有一場面試','我想問求職順不順利','我想算求職順不順利','我想算關於求職的部分','我想請問最近的求職狀況如何']
    #testLoki(inputLIST, ['jobseeking'])
    #print("")

    # 輸入其它句子試看看
    inputLIST = ["在這邊可以測試句子"]
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Result => {}".format(resultDICT))
    ask=resultDICT["ask"]
    #利用Loki判斷ask
    #開頭引導句
    #互動第一句
    num1=random.randint(1,2)
    num2=random.randint(1,2)
    num3=random.randint(1,2)
    #互動第二句
    num4=random.randint(1,2)
    num5=random.randint(1,2)
    num6=random.randint(1,2)
    #結果呈現
    gua=int(str(num6)+str(num5)+str(num4)+str(num3)+str(num2)+str(num1))
    data = pd.read_csv('卜卦機器人資料庫.csv',encoding='utf-8')
    for i in range(0,64):
        if gua == data.iloc[i,0]:
            print("您占卜到的卦象為：",data.iloc[i,2],"卦","\n在此給予您小建議：")
            print(data.iloc[i,4])
            print("\n另外，根據您占卜之面向為：",ask)
            print("占卜的結果顯示：\n"," ",data.iloc[i][ask]) 
