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
from ArticutAPI import Articut
try:
    from intent import Loki_restaurant_booking
    from intent import Loki_restaurant_loc
    from intent import Loki_restaurant_eva
    from intent import Loki_restaurant_time
    from intent import Loki_hotel_booking
    from intent import Loki_hotel_eva
    from intent import Loki_hotel_price
    from intent import Loki_hotel_time
    from intent import Loki_city_confirmation
    from intent import Loki_restaurant_price
    from intent import Loki_hotel_loc
    from intent import Loki_reserve_trigger

except:
    from .intent import Loki_restaurant_booking
    from .intent import Loki_restaurant_loc
    from .intent import Loki_restaurant_eva
    from .intent import Loki_restaurant_time
    from .intent import Loki_hotel_booking
    from .intent import Loki_hotel_eva
    from .intent import Loki_hotel_price
    from .intent import Loki_hotel_time
    from .intent import Loki_city_confirmation
    from .intent import Loki_restaurant_price
    from .intent import Loki_hotel_loc
    from .intent import Loki_reserve_trigger

with open(r"./account.info", encoding="UTF-8") as f:
    accountINFO = json.load(f)
LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = accountINFO["username"]
LOKI_KEY = accountINFO["loki_api_key"]
Articut_key = accountINFO["articut_api_key"]
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
            # print(result.status_code)
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
                # restaurant_booking
                if lokiRst.getIntent(index, resultIndex) == "restaurant_booking":
                    resultDICT = Loki_restaurant_booking.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # restaurant_loc
                if lokiRst.getIntent(index, resultIndex) == "restaurant_loc":
                    resultDICT = Loki_restaurant_loc.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # restaurant_eva
                if lokiRst.getIntent(index, resultIndex) == "restaurant_eva":
                    resultDICT = Loki_restaurant_eva.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # restaurant_time
                if lokiRst.getIntent(index, resultIndex) == "restaurant_time":
                    resultDICT = Loki_restaurant_time.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # hotel_booking
                if lokiRst.getIntent(index, resultIndex) == "hotel_booking":
                    resultDICT = Loki_hotel_booking.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # hotel_eva
                if lokiRst.getIntent(index, resultIndex) == "hotel_eva":
                    resultDICT = Loki_hotel_eva.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # hotel_price
                if lokiRst.getIntent(index, resultIndex) == "hotel_price":
                    resultDICT = Loki_hotel_price.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # hotel_time
                if lokiRst.getIntent(index, resultIndex) == "hotel_time":
                    resultDICT = Loki_hotel_time.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # city_confirmation
                if lokiRst.getIntent(index, resultIndex) == "city_confirmation":
                    resultDICT = Loki_city_confirmation.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # restaurant_price
                if lokiRst.getIntent(index, resultIndex) == "restaurant_price":
                    resultDICT = Loki_restaurant_price.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # hotel_loc
                if lokiRst.getIntent(index, resultIndex) == "hotel_loc":
                    resultDICT = Loki_hotel_loc.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                #reserve_trigger
                if lokiRst.getIntent(index, resultIndex) == "reserve_trigger":
                    resultDICT = Loki_reserve_trigger.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)


if __name__ == "__main__":
    """
    # restaurant_booking
    print("[TEST] restaurant_booking")
    inputLIST = ['五人位子','我們有5人','我要預約8人的','預約2人的位子','我要預訂三人位子']
    testLoki(inputLIST, ['restaurant_booking'])
    print("")

    # restaurant_loc
    print("[TEST] restaurant_loc")
    inputLIST = ['這間店在哪','這間餐廳位在哪裡','我不清楚這家店的位置','我不知道這間餐廳在哪']
    testLoki(inputLIST, ['restaurant_loc'])
    print("")

    # restaurant_eva
    print("[TEST] restaurant_eva")
    inputLIST = ['這家好吃嗎','這店家好嗎','這間食物好吃嗎','這間餐廳評價如何','那這家餐廳評價如何啊']
    testLoki(inputLIST, ['restaurant_eva'])
    print("")

    # restaurant_time
    print("[TEST] restaurant_time")
    inputLIST = ['我要預約8點的位子','我要預定9點50分的位子','我要預約上午11點的位子','我要預約下午六點的位子']
    testLoki(inputLIST, ['restaurant_time'])
    print("")

    # hotel_booking
    print("[TEST] hotel_booking")
    inputLIST = ['我要預定3人房','想要訂1個雙人房','想要訂1間三人房','我要訂3個人的旅館']
    testLoki(inputLIST, ['hotel_booking'])
    print("")

    # hotel_eva
    print("[TEST] hotel_eva")
    inputLIST = ['這家旅館好嗎?','這間旅館好嗎?','這間旅館評價如何?','那這間旅館大家推薦嗎']
    testLoki(inputLIST, ['hotel_eva'])
    print("")

    # hotel_price
    print("[TEST] hotel_price")
    inputLIST = ['住一晚要多少','住2天要花多少','住一晚要多少錢','住1個晚上要多少','這間旅館一晚要多少','這間旅館住兩晚要多少錢']
    testLoki(inputLIST, ['hotel_price'])
    print("")

    # hotel_time
    print("[TEST] hotel_time")
    inputLIST = ['什麼時候可以入住','幾點開始可以入住','入住時間是幾點開始','大約幾點可以開始入住']
    testLoki(inputLIST, ['hotel_time'])
    print("")

    # city_confirmation
    print("[TEST] city_confirmation")
    inputLIST = ['在臺中','在高雄市','我人在台南','我在台北市','我現在在台南','我在的縣市是台中']
    testLoki(inputLIST, ['city_confirmation'])
    print("")

    # restaurant_price
    print("[TEST] restaurant_price")
    inputLIST = ['這家店會貴嗎','這間餐廳價位多少','吃這家店大概要花多少','這間餐廳的低銷是多少']
    testLoki(inputLIST, ['restaurant_price'])
    print("")

    # hotel_loc
    print("[TEST] hotel_loc")
    inputLIST = ['這間旅館在哪附近','這間旅館的位置在哪']
    testLoki(inputLIST, ['hotel_loc'])
    print("")
    
    # reserve_trigger
    print("[TEST] reserve_trigger")
    inputLIST = ['我想預約', '我要預約', '能預約嗎', '可以預訂嗎', '我想先預約', '我想要預定', '我想要預約', '方便預約嗎', '可以先預約嗎', '可以預訂位子嗎', '我想要預定座位', '我要先預約位子']
    testLoki(inputLIST, ['reserve_trigger'])
    print("")
    """
    # 輸入其它句子試看看
    # inputLIST = ["我要預約十點的位子"]
    # inputLIST = ["預定下午六點半"]
    # inputLIST = ["這間店家評價如何"]
    # inputLIST = ["這間吃飯處在哪裡"]
    # inputLIST = ["這間餐廳要花多少"]
    # inputLIST = ["我在台南市"]
    # inputLIST = ["我要預訂5人位子"]
    # inputLIST = ["蝦老爹美食海鮮"]
    # inputLIST = ["在中西區"]
    inputLIST = ["預定上午十點半"]
    # inputLIST = ["我要先預約"]
    # inputLIST = ["想要預約下午8:23的位子"]
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Result => {}".format(resultDICT))
    # print(resultDICT["area"])


