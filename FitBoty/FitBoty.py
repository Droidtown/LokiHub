#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 3.0 Template For Python3

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

import json
import math
import re
from requests import post
from requests import codes

try:
    from intent import Loki_weight
    from intent import Loki_height
    from intent import Loki_age
    from intent import Loki_gender
    from intent import Loki_correct
    from intent import Loki_incorrect
    from intent import Loki_sports
    from intent import Loki_food
    from intent import Loki_update_info
except:
    from .intent import Loki_weight
    from .intent import Loki_height
    from .intent import Loki_age
    from .intent import Loki_gender
    from .intent import Loki_correct
    from .intent import Loki_incorrect
    from .intent import Loki_sports
    from .intent import Loki_food
    from intent import Loki_update_info

with open("account.info.json", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.load(f)
LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = accountDICT["username"]
LOKI_KEY = accountDICT["loki_key"]
# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []
INPUT_LIMIT = 20

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
                self.message = "{} Connection failed.".format(result.status_code)
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
    # 將 intent 會使用到的 key 預先設爲空列表
    resultDICT = {
       #"key": []
    }
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # correct
                if lokiRst.getIntent(index, resultIndex) == "correct":
                    resultDICT = Loki_correct.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # gender
                if lokiRst.getIntent(index, resultIndex) == "gender":
                    resultDICT = Loki_gender.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # sports
                if lokiRst.getIntent(index, resultIndex) == "sports":
                    resultDICT = Loki_sports.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # food
                if lokiRst.getIntent(index, resultIndex) == "food":
                    resultDICT = Loki_food.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # incorrect
                if lokiRst.getIntent(index, resultIndex) == "incorrect":
                    resultDICT = Loki_incorrect.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)
                
                # update_info
                if lokiRst.getIntent(index, resultIndex) == "update_info":
                    resultDICT = Loki_update_info.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # age
                if lokiRst.getIntent(index, resultIndex) == "age":
                    resultDICT = Loki_age.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # weight
                if lokiRst.getIntent(index, resultIndex) == "weight":
                    resultDICT = Loki_weight.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # height
                if lokiRst.getIntent(index, resultIndex) == "height":
                    resultDICT = Loki_height.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def execLoki(content, filterLIST=[], splitLIST=[]):
    """
    input
        content       STR / STR[]    要執行 loki 分析的內容 (可以是字串或字串列表)
        filterLIST    STR[]          指定要比對的意圖 (空列表代表不指定)
        splitLIST     STR[]          指定要斷句的符號 (空列表代表不指定)
                                     * 如果一句 content 內包含同一意圖的多個 utterance，請使用 splitLIST 切割 content

    output
        resultDICT    DICT           合併 runLoki() 的結果，請先設定 runLoki() 的 resultDICT 初始值

    e.g.
        splitLIST = ["！", "，", "。", "？", "!", ",", "
", "；", "　", ";"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？")                      # output => ["今天天氣"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？", splitLIST=splitLIST) # output => ["今天天氣", "後天氣象"]
        resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"])                # output => ["今天天氣", "後天氣象"]
    """
    contentLIST = []
    if type(content) == str:
        contentLIST = [content]
    if type(content) == list:
        contentLIST = content

    resultDICT = {}
    if contentLIST:
        if splitLIST:
            # 依 splitLIST 做分句切割
            splitPAT = re.compile("[{}]".format("".join(splitLIST)))
            inputLIST = []
            for c in contentLIST:
                tmpLIST = splitPAT.split(c)
                inputLIST.extend(tmpLIST)
            # 去除空字串
            while "" in inputLIST:
                inputLIST.remove("")
        else:
            # 不做分句切割處理
            inputLIST = contentLIST

        # 依 INPUT_LIMIT 限制批次處理
        for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
            lokiResultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)
            if "msg" in lokiResultDICT:
                return lokiResultDICT

            # 將 lokiResultDICT 結果儲存至 resultDICT
            for k in lokiResultDICT:
                if k not in resultDICT:
                    resultDICT[k] = []
                resultDICT[k].extend(lokiResultDICT[k])

    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

    if "msg" in resultDICT:
        print(resultDICT["msg"])

def testIntent():
    # sports
    print("[TEST] sports")
    inputLIST = ['沒有','沒有運動','跳繩30分鐘','30分鐘的瑜伽','做瑜伽30分鐘','打排球30分鐘','爬樓梯30分鐘','和40分鐘的跳繩','跳國標舞30分鐘','騎腳踏車30分鐘','跳繩和重訓各30分鐘','跳繩30分鐘和重訓1小時','30分鐘的瑜伽和40分鐘的跳繩']
    testLoki(inputLIST, ['sports'])
    print("")

    # food
    print("[TEST] food")
    inputLIST = ['沒吃','吃白飯','和白飯','一碗白飯','中午沒吃','早餐沒吃','沒吃晚餐','加一杯奶茶','吐司加奶茶','吐司配奶茶','和一碗白飯','晚餐吃白飯','晚餐是雞排','配一杯奶茶','雞排和紅茶','一盤義大利麵','吃了一碗白飯','中午吃義大利麵','午餐吃義大利麵','午餐是義大利麵','一碗白飯和一碗湯','吃了一盤義大利麵','早上吃了一碗白飯','早上吃吐司加奶茶','早上吃吐司配奶茶','早餐吃吐司加奶茶','早餐吃吐司配奶茶','一片吐司加一杯奶茶','一片吐司配一杯奶茶','晚餐還吃了一碗白飯','中午吃了一盤義大利麵','午餐吃了一盤義大利麵','吃了一碗白飯和一碗湯','早上吃一片吐司加一杯奶茶','早上吃一片吐司配一杯奶茶','早上吃了一碗白飯和一碗湯','早餐吃一片吐司加一杯奶茶','早餐吃一片吐司配一杯奶茶','晚餐吃了一碗白飯和一碗湯']
    testLoki(inputLIST, ['food'])
    print("")

    # age
    print("[TEST] age")
    inputLIST = ['17']
    testLoki(inputLIST, ['age'])
    print("")

    # weight
    print("[TEST] weight")
    inputLIST = ['50','50公斤']
    testLoki(inputLIST, ['weight'])
    print("")

    # gender
    print("[TEST] gender")
    inputLIST = ['女生','是女生','不是女的','是個男的','不是個男的']
    testLoki(inputLIST, ['gender'])
    print("")

    # height
    print("[TEST] height")
    inputLIST = ['150','1米5','150公分','1米5公分']
    testLoki(inputLIST, ['height'])
    print("")

    # update_info
    print("[TEST] update_info")
    inputLIST = ['180','16歲','性別','180公分','180寫錯','180打錯','16歲錯了','180打錯了','我不是180','身高寫錯','體重打錯','180公分寫錯','180公分打錯','我不是男的','身高打錯了','180公分打錯了','我不是180公分']
    testLoki(inputLIST, ['update_info'])
    print("")

    # incorrect
    print("[TEST] incorrect")
    inputLIST = ['no','否','有錯','錯誤']
    testLoki(inputLIST, ['incorrect'])
    print("")

    # correct
    print("[TEST] correct")
    inputLIST = ['yes','是','正確','沒錯']
    testLoki(inputLIST, ['correct'])
    print("")


if __name__ == "__main__":
    # 測試所有意圖
    #testIntent()

    # 測試其它句子
    filterLIST = []
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    #resultDICT = execLoki("我15歲", filterLIST)            # output => ["今天天氣"]
    #resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST, splitLIST) # output => ["今天天氣", "後天氣象"]
    #resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"], filterLIST)      # output => ["今天天氣", "後天氣象"]
    
    #resultDICT = runLoki(["你的性別是"])
    #print(resultDICT)
    #print("你想問他是{}".format(resultDICT["sex"]))
    
    resultDICT = runLoki(["五十多公斤"])
    print(resultDICT)