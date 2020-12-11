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
USERNAME = "jacksugood@gmail.com"
LOKI_KEY = "ESNCSpXa-n1kelP5S=UQpoP_*QF3&X&"
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

moneyDICT = {'台幣': 'TWD','新台幣':'TWD','美元':'USD','鎂':'USD', '美金': 'USD', '歐元': 'EUR', '日圓': 'JPY', '英鎊': 'GBP', '瑞士法郎': 'CHF', '加幣': 'CAD', '澳幣': 'AUD', '巴西黑奧': 'BRL', '人民幣': 'CNY', '捷克克朗': 'CZK', '丹麥克羅納': 'DKK', '港幣': 'HKD', '匈牙利': 'HUF', '印尼盧比': 'IDR', '印度盧比': 'INR', '韓圜': 'KRW', '墨西哥披索': 'MXN', '挪威克?': 'NOK', '紐幣': 'NZD', '菲律賓披索': 'PHP', '波蘭茲羅提': 'PLN', '俄國盧布': 'RUB', '瑞典克郎': 'SEK', '新加坡幣': 'SGD', '泰銖': 'THB', '土耳其里拉': 'TRL', '南非幣': 'ZAR', '馬來西亞': 'MYR', '斯洛伐克克朗': 'SKK', '沙烏地阿拉伯利雅': 'SAR', '哥倫比亞披索': 'COP', '辛巴威': 'ZWD', '摩洛哥迪拉姆': 'MAD', '埃及鎊': 'EGP', '以色列謝克': 'ILS', '智利披索': 'CLP', '阿根廷披索': 'ARS', '玻利維亞幣': 'BOB', '厄爪多爾蘇克雷': 'ECS', '巴拿馬巴布亞': 'PAB', '委內瑞拉銀幣': 'VEB', '巴基斯坦盧比': 'PKR', '斯里蘭卡盧比': 'LKR', '哥斯大黎加': 'CRC', '新土耳其里拉': 'TRY', '肯亞先令': 'KES', '模里西斯盧比': 'MUR', '越南幣': 'VND', '冰島幣': 'ISK', '阿拉伯聯合大公國迪拉姆': 'AED', '秘魯索爾': 'PEN', '黃金': 'XAU', '境外人民幣': 'CNH', '科威特幣': 'KWD', '澳門幣': 'MOP'}
def moneyName(inputSTR):
    return moneyDICT[inputSTR]

    
#dict from
#import csv
#curDICT={}
#with open('currency_CE.csv', 'r') as file:
#    reader = csv.reader(file)
#    for row in reader:
#         curDICT[row[1]]=row[0]


def amountSTRConvert(inputSTR):
    resultDICT = articut.parse(inputSTR, level="lv3") 
    return resultDICT["number"]

def ListToString(MyInput):
    if isinstance(MyInput,str):
        return(MyInput)  
    else:
        return(MyInput[0])
    
    
if __name__ == "__main__":
    inputLIST = ["一百歐元可以換多少台幣?"]
    resultDICT = runLoki(inputLIST)
    #try "今天美金換台幣是多少" "我想要100鎂" "一百美元" "一百元美元"
    
     
    #converting
    source_1 = ListToString(resultDICT["src"])
    target_1 = ListToString(resultDICT["tgt"])
    amount_1 = ListToString(resultDICT["amt"])
    #dealing with 一百美元
    
    
    #get today's rate
    response = requests.get("https://tw.rter.info/capi.php")
    rateDICT = response.json()

    #change money name from Chinese to English, and amount to numbers
    Source= "USD"+moneyName(source_1)
    Target = "USD"+moneyName(target_1)
    Amount = amountSTRConvert(amount_1 )[amount_1]
    
    
    #search in dictionary
    Source_rate = rateDICT[Source]["Exrate"]
    Target_rate = rateDICT[Target]["Exrate"]
    #Exchange!
    Result = Amount*(Target_rate/Source_rate)
    
    print("您好~~\n{0}{1}可換得%2.2f{2}\n歡迎再次使用!" .format(Amount,source_1,target_1)%(Result))

#use request to download the data from: https://tw.rter.info/capi.php