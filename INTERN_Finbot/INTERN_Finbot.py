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
USERNAME = "60621032L@gapps.ntnu.edu.tw"
LOKI_KEY = "#5ULL2LpQIMyRZ-4W^iFWjNxjQ264UM"
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

currencyCodeDICT = {'台幣': 'TWD', '美金': 'USD', '鎂': 'USD', '美元': 'USD', '歐元': 'EUR', '日圓': 'JPY', '英鎊': 'GBP', '瑞士法郎': 'CHF', '加幣': 'CAD', '澳幣': 'AUD', '巴西黑奧': 'BRL', '人民幣': 'CNY', '捷克克朗': 'CZK', '丹麥克羅納': 'DKK', '港幣': 'HKD', '匈牙利': 'HUF', '印尼盧比': 'IDR', '印度盧比': 'INR', '韓圜': 'KRW', '墨西哥披索': 'MXN', '挪威克郞': 'NOK', '紐幣': 'NZD', '菲律賓披索': 'PHP', '波蘭茲羅提': 'PLN', '俄國盧布': 'RUB', '瑞典克郎': 'SEK', '新加坡幣': 'SGD', '泰銖': 'THB', '土耳其里拉': 'TRL', '南非幣': 'ZAR', '馬來西亞': 'MYR', '斯洛伐克克朗': 'SKK', '沙烏地阿拉伯利雅': 'SAR', '哥倫比亞披索': 'COP', '辛巴威': 'ZWD', '摩洛哥迪拉姆': 'MAD', '埃及鎊': 'EGP', '以色列謝克': 'ILS', '智利披索': 'CLP', '阿根廷披索': 'ARS', '玻利維亞幣': 'BOB', '厄爪多爾蘇克雷': 'ECS', '巴拿馬巴布亞': 'PAB', '委內瑞拉銀幣': 'VEB', '巴基斯坦盧比': 'PKR', '斯里蘭卡盧比': 'LKR', '哥斯大黎加': 'CRC', '新土耳其里拉': 'TRY', '肯亞先令': 'KES', '模里西斯盧比': 'MUR', '越南幣': 'VND', '冰島幣': 'ISK', '阿拉伯聯合大公國迪拉姆': 'AED', '秘魯索爾': 'PEN', '黃金': 'XAU', '境外人民幣': 'CNH', '科威特幣': 'KWD', '澳門幣': 'MOP'}

currencyCodeLIST = []
for x in currencyCodeDICT:
    currencyCodeLIST.append(x)
    currencyCodeLIST.extend(currencyCodeDICT[x])
print()
#dict from
#import csv
#curDICT={}
#with open('money_list.csv', 'r', encoding="utf-8",) as file:
    #reader = csv.reader(file)
    #for row in reader:
        #curDICT[row[1]]=row[0]
        
#print(curDICT)

def amountSTRConvert(inputSTR):
    resultDICT = articut.parse(inputSTR, level="lv3") 
    return resultDICT["number"]
#print(amountSTRConvert("50000"))

#建立貨幣匯率字典
currencyExRateDICT = {}

#currencyExRateDICT = requests.get("http://tw.rter.info/capi.php").json()

def getCurrencyExRate():
    """取得最新匯率 然後存在CurrencyExRateDICT"""
    global currencyExRateDICT
    currencyExRateDICT = requests.get("http://tw.rter.info/capi.php").json()
    
getCurrencyExRate()
print(currencyExRateDICT)

#def getCurrencyExRate():
    #"""取得最新匯率 然後存在CurrencyExRateDICT"""
    #currencyExRateDICT = requests.get("http://tw.rter.info/capi.php").json()
    #return currencyExRateDICT


#print(getCurrencyExRate()["USDBRL"]["Exrate"])
def getSrc2TgtCurrencyExRate(sourceCurrencySTR, targetCurrencySTR):
    if sourceCurrencySTR == None:
        source = "TWD"
        print("ver1"+source)
    else:
        source=currencyCodeDICT[sourceCurrencySTR]
        print("ver2"+source)
    if targetCurrencySTR == None:
        target = "TWD"
        print("ver1"+target)
    else:
        target=currencyCodeDICT[targetCurrencySTR]
        print("ver2"+target)
    exRate = (1/currencyExRateDICT["USD{}".format(source)]["Exrate"]*(currencyExRateDICT["USD{}".format(target)]["Exrate"]))
    return exRate
    


if __name__ == "__main__": #程式進入點
    inputLIST1 = [input("您好，請問您想怎麼換錢呢?")]
    #inputLIST = ["我想換100鎂"]
    resultDICT = runLoki(inputLIST1)
    source = resultDICT['src']
    target = resultDICT['tgt']
    amount = amountSTRConvert(resultDICT['amt'])[resultDICT['amt']]
    #print(amountSTRConvert(resultDICT['amt']))
    print("Result => {}".format(resultDICT))
    answer = getSrc2TgtCurrencyExRate(source, target)*amount
    print("您需要{}".format(answer)+target+"，歡迎下次光臨")