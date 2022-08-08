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

from requests import post
from requests import codes
import math
import re
try:
    from intent import Loki_rock
    from intent import Loki_climbingGym
    from intent import Loki_chat
    from intent import Loki_rules
    from intent import Loki_equipment
except:
    from .intent import Loki_rock
    from .intent import Loki_climbingGym
    from .intent import Loki_chat
    from .intent import Loki_rules
    from .intent import Loki_equipment


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = ""
LOKI_KEY = ""
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
                # rock
                if lokiRst.getIntent(index, resultIndex) == "rock":
                    resultDICT = Loki_rock.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # climbingGym
                if lokiRst.getIntent(index, resultIndex) == "climbingGym":
                    resultDICT = Loki_climbingGym.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # chat
                if lokiRst.getIntent(index, resultIndex) == "chat":
                    resultDICT = Loki_chat.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # rules
                if lokiRst.getIntent(index, resultIndex) == "rules":
                    resultDICT = Loki_rules.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # equipment
                if lokiRst.getIntent(index, resultIndex) == "equipment":
                    resultDICT = Loki_equipment.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

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
    # rock
    print("[TEST] rock")
    inputLIST = ['jug是什麼','jug長怎樣','pinch怎麼抓','岩點有哪些','jug有什麼特色','jug長什麼樣子','岩點有哪幾種','sloper可以怎麼爬','最好爬的是哪種','最好抓的是哪種點']
    testLoki(inputLIST, ['rock'])
    print("")

    # climbingGym
    print("[TEST] climbingGym")
    inputLIST = ['哪裡可以攀岩','有哪些岩館呢','東部有岩館嗎','苗栗能攀岩嗎','台中有哪些岩館','攀岩一次多少錢','新竹有幾間岩館','有推薦的岩館麻','去一次岩館多少錢','去攀一次岩多少錢','台北哪裡可以抱石','哪些縣市有岩館呢','哪間岩館離我最近','想抱石可以去哪裡','新手可以去哪攀岩','紅石攀岩一次多少','哪幾間岩館有速度攀','紅石攀岩一天多少錢','那東部有哪些岩館呢','台灣哪些縣市有岩館呢','推薦哪些距離近的岩館','離我近的岩館有比較推薦的嗎']
    testLoki(inputLIST, ['climbingGym'])
    print("")

    # chat
    print("[TEST] chat")
    inputLIST = ['你愛攀岩麻','抱石好玩嗎','我不喜歡上攀','攀岩好無聊！','你喜歡攀岩嗎？']
    testLoki(inputLIST, ['chat'])
    print("")

    # rules
    print("[TEST] rules")
    inputLIST = ['攀岩有規則嗎','抱石要注意什麼','攀岩有哪些規則','上攀要小心什麼？','攀岩有分難度嗎？','攀岩有難度之分嗎','攀岩的規則是什麼','上攀有什麼要注意的？','上攀有哪些要小心的？','怎麼知道我是哪個等級','要怎麼知道自己的等級']
    testLoki(inputLIST, ['rules'])
    print("")

    # equipment
    print("[TEST] equipment")
    inputLIST = ['攀岩要帶什麼','攀岩要穿什麼','可以不買裝備嗎','攀岩要準備什麼','攀岩要買鞋子嗎','衣著有限制嗎？','哪些裝備一定要買','岩粉可以去哪買？','岩粉哪裡買得到？','岩鞋大概多少錢？','穿短袖可以攀岩嗎','可以穿牛仔褲攀岩嗎','攀岩需要穿運動褲嗎','穿短袖可以去攀岩嗎','攀岩一定要穿運動服嗎','攀岩要穿長褲還短褲？']
    testLoki(inputLIST, ['equipment'])
    print("")


if __name__ == "__main__":
    # 測試所有意圖
    testIntent()

    # 測試其它句子
    filterLIST = []
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST)            # output => ["今天天氣"]
    resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST, splitLIST) # output => ["今天天氣", "後天氣象"]
    resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"], filterLIST)      # output => ["今天天氣", "後天氣象"]