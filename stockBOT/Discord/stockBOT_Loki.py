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
from ArticutAPI import Articut
from requests import post
from requests import codes
from fc_info import information
from fc_info import growth
from fc_info import profitability
from fc_info import safety
from DICT import companyDICT
from bs4 import BeautifulSoup
import requests
import json
import math
try:
    from intent import Loki_symbol
    from intent import Loki_Safety
    from intent import Loki_information
    from intent import Loki_what_is
    from intent import Loki_Profitability
    from intent import Loki_Growth
except:
    from .intent import Loki_symbol
    from .intent import Loki_Safety
    from .intent import Loki_information
    from .intent import Loki_what_is
    from .intent import Loki_Profitability
    from .intent import Loki_Growth



LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = ""
LOKI_KEY = ""

# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []

articut = Articut(username= "", apikey= "")

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
                # symbol
                if lokiRst.getIntent(index, resultIndex) == "symbol":
                    resultDICT = Loki_symbol.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)
                # Safety
                if lokiRst.getIntent(index, resultIndex) == "Safety":
                    resultDICT = Loki_Safety.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)
                # information
                if lokiRst.getIntent(index, resultIndex) == "information":
                    resultDICT = Loki_information.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)     
                
                # revenue
                if lokiRst.getIntent(index, resultIndex) == "revenue":
                    resultDICT = Loki_revenue.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)       
                # what_is
                if lokiRst.getIntent(index, resultIndex) == "what_is":
                    resultDICT = Loki_what_is.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)
                    
                # Profitability
                if lokiRst.getIntent(index, resultIndex) == "Profitability":
                    resultDICT = Loki_Profitability.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)          
                    
                # Growth
                if lokiRst.getIntent(index, resultIndex) == "Growth":
                    resultDICT = Loki_Growth.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)                

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)


if __name__ == "__main__":
    # symbol
    print("[TEST] symbol")
    inputLIST = ['台積電基本資料','台積電的成交價','台積電昨日收盤價','台積電的基本資料','關於台積電的資訊','我想知道台積電的基本資料']
    testLoki(inputLIST, ['symbol'])
    print("")
    
    # Safety
    print("[TEST] Safety")
    inputLIST = ['聯發科負債','聯發科安全嗎','聯發科安全性','聯發科流動比','聯發科負債比','聯發科速動比','聯發科償債能力','聯發科安全性分析','聯發科安全性指標','聯發科流速動比率','聯發科現金流量比','聯發科利息保障倍數','聯發科是不是安全的股票']
    testLoki(inputLIST, ['Safety'])
    print("")
    
    # information
    print("[TEST] information")
    inputLIST = ['台積電的基本資料','關於台積電個股的資料','關於台積電公司的資訊','關於台積電股票的資料']
    testLoki(inputLIST, ['information'])
    print("")
    
    # revenue
    print("[TEST] revenue")
    inputLIST = ['季營收台積電','台積電近一季營收','近一季營收台積電','台積電的近一季營收是多少']
    testLoki(inputLIST, ['revenue'])
    print("")
    
    # what_is
    print("[TEST] what_is")
    inputLIST = ['什麼是償債能力','償債能力是什麼']
    testLoki(inputLIST, ['what_is'])
    print("")
    
    # Profitability
    print("[TEST] Profitability")
    inputLIST = ['聯發科ROEROA','聯發科的ROA','聯發科的ROE','聯發科ROA及ROE','聯發科ROE及ROA','聯發科利潤比率','聯發科獲利情形','聯發科獲利情況','聯發科獲利指標','聯發科獲利能力','聯發科存貨周轉率','聯發科資產報酬率','聯發科營運周轉能力','聯發科獲利相關指標','聯發科股東權益報酬率','連發科應收帳款週轉率']
    testLoki(inputLIST, ['Profitability'])
    print("")
    
    # Growth
    print("[TEST] Growth")
    inputLIST = ['聯發科成長力','聯發科成長性','聯發科成長指標','聯發科成長力分析','聯發科的成長情形','聯發科營收年成長率','聯發科獲利年成長率','聯發科資產年成長率','聯發科每股盈餘成長率','聯發科營業利益年成長率','聯發科稅後淨利年成長率']
    testLoki(inputLIST, ['Growth'])
    print("")
    

    # 輸入其它句子試看看
    
    inputLIST = ["現金流量比是什麼"]
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Result => {}".format(resultDICT))
    
    print(resultDICT)
    
    if  "fun_information" in resultDICT.keys():
        result_infoDICT = information(resultDICT["symbol"])
        resultDICT.update(result_infoDICT)
    elif "fun_growth" in resultDICT.keys():
        result_growthDICT = growth(resultDICT["symbol"])
        resultDICT.update(result_growthDICT)
    elif "fun_profitability" in resultDICT.keys():
        result_profitabilityDICT = profitability(resultDICT["symbol"])
        resultDICT.update(result_profitabilityDICT)   
    elif "fun_safety" in resultDICT.keys():
        result_safetyDICT = safety(resultDICT["symbol"])
        resultDICT.update(result_safetyDICT)       
        
        

    if "fun_information" in resultDICT.keys():
        print(companyDICT[resultDICT["symbol"]][0]+resultDICT["symbol"]+"的公司基本資料如下！"+"\n公司名稱："+resultDICT["name"]+"\n產業別："+resultDICT["industry"]+"\n市值："+resultDICT["value"]+"\n主要業務："+resultDICT["business"])  
    elif "fun_growth" in resultDICT.keys():
        print(companyDICT[resultDICT["symbol"]][0]+resultDICT["symbol"]+"在"+resultDICT["quarter"]+"的獲利年成長率如下！"+"\n營收年成長率："+resultDICT["revenue_YOY"]+"\n毛利年成長率："+resultDICT["gross_profit_YOY"]+"\n營業利益年成長率："+resultDICT["operating_income_YOY"]+"\n稅前淨利年成長率："+resultDICT["NIBT_YOY"]+"\n稅後淨利年成長率："+resultDICT["NI_YOY"]+"\n每股稅後盈餘年成長率："+resultDICT["EPS_YOY"])    
    elif "fun_profitability" in resultDICT.keys():
        print(companyDICT[resultDICT["symbol"]][0]+resultDICT["symbol"]+"在"+resultDICT["quarter"]+"的獲利能力如下！"+"\n營業毛利率："+resultDICT["GPM"]+"\n營業利益率："+resultDICT["OPM"]+"\n稅前淨利率："+resultDICT["PTPM"]+"\n稅後淨利率："+resultDICT["NPM"]+"\n每股稅後盈餘："+resultDICT["EPS"]+"\n每股淨值(元)："+resultDICT["NASPS"]+"\n股東權益報酬率："+resultDICT["ROE"]+"\n資產報酬率："+resultDICT["ROA"])    
    elif "fun_safety" in resultDICT.keys():
        print(companyDICT[resultDICT["symbol"]][0]+resultDICT["symbol"]+"在"+resultDICT["quarter"]+"的償債能力如下！"+"\n現金比："+resultDICT["CR"]+"\n速動比："+resultDICT["QR"]+"\n流動比："+resultDICT["current_ratio"]+"\n利息保障倍數："+resultDICT["ICR"]+"\n現金流量比："+resultDICT["OCFR"]+"\n負債總額比(元)："+resultDICT["DR"])    
    elif "reply" in resultDICT.keys():
        print(resultDICT["reply"])
    elif resultDICT["symbol"] == None:
        print("不確定您要找哪一支股票的資訊！請再輸入一次股票名稱或是代號！")
    else:
        print("不確定您要找哪一類的資訊！請再輸入一次要查的資料類別！")
        
    
    
    
    