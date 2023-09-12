#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 4.0 Template For Python3

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
                    "msg": "No matching Intent."
                }
            ]
        }
"""

from requests import post
from requests import codes
import json
import math
import os
import re
try:
    from intent import Loki_play_with_adults
    from intent import Loki_express_needs
    from intent import Loki_sharing
    from intent import Loki_imitate_actions
    from intent import Loki_understand_short_sentences
    from intent import Loki_reproduce_same_actions
    from intent import Loki_follow_directions
    from intent import Loki_yes_no
except:
    from .intent import Loki_play_with_adults
    from .intent import Loki_express_needs
    from .intent import Loki_sharing
    from .intent import Loki_imitate_actions
    from .intent import Loki_understand_short_sentences
    from .intent import Loki_reproduce_same_actions
    from .intent import Loki_follow_directions
    from .intent import Loki_yes_no


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
try:
    accountInfo = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "account.info"), encoding="utf-8"))
    USERNAME = accountInfo["username"]
    LOKI_KEY = accountInfo["loki_key_above1"]
except Exception as e:
    print("[ERROR] AccountInfo => {}".format(str(e)))
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
                    if "word_count_balance" in result:
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

def runLoki(inputLIST, filterLIST=[], refDICT={}):
    resultDICT = refDICT
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            lokiResultDICT = {}
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # play_with_adults
                if lokiRst.getIntent(index, resultIndex) == "play_with_adults":
                    lokiResultDICT = Loki_play_with_adults.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # express_needs
                if lokiRst.getIntent(index, resultIndex) == "express_needs":
                    lokiResultDICT = Loki_express_needs.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # sharing
                if lokiRst.getIntent(index, resultIndex) == "sharing":
                    lokiResultDICT = Loki_sharing.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # imitate_actions
                if lokiRst.getIntent(index, resultIndex) == "imitate_actions":
                    lokiResultDICT = Loki_imitate_actions.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # understand_short_sentences
                if lokiRst.getIntent(index, resultIndex) == "understand_short_sentences":
                    lokiResultDICT = Loki_understand_short_sentences.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # reproduce_same_actions
                if lokiRst.getIntent(index, resultIndex) == "reproduce_same_actions":
                    lokiResultDICT = Loki_reproduce_same_actions.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # follow_directions
                if lokiRst.getIntent(index, resultIndex) == "follow_directions":
                    lokiResultDICT = Loki_follow_directions.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # yes_no
                if lokiRst.getIntent(index, resultIndex) == "yes_no":
                    lokiResultDICT = Loki_yes_no.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

            # save lokiResultDICT to resultDICT
            for k in lokiResultDICT:
                if k not in resultDICT:
                    resultDICT[k] = []
                if type(resultDICT[k]) != list:
                    resultDICT[k] = [resultDICT[k]] if resultDICT[k] else []
                if type(lokiResultDICT[k]) == list:
                    resultDICT[k].extend(lokiResultDICT[k])
                else:
                    resultDICT[k].append(lokiResultDICT[k])
    else:
        resultDICT["msg"] = lokiRst.getMessage()
    return resultDICT

def execLoki(content, filterLIST=[], splitLIST=[], refDICT={}):
    """
    input
        content       STR / STR[]    要執行 loki 分析的內容 (可以是字串或字串列表)
        filterLIST    STR[]          指定要比對的意圖 (空列表代表不指定)
        splitLIST     STR[]          指定要斷句的符號 (空列表代表不指定)
                                     * 如果一句 content 內包含同一意圖的多個 utterance，請使用 splitLIST 切割 content
        refDICT       DICT           參考內容

    output
        resultDICT    DICT           合併 runLoki() 的結果

    e.g.
        splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？")                      # output => ["今天天氣"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？", splitLIST=splitLIST) # output => ["今天天氣", "後天氣象"]
        resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"])                # output => ["今天天氣", "後天氣象"]
    """
    resultDICT = refDICT
    if resultDICT is None:
        resultDICT = {}

    contentLIST = []
    if type(content) == str:
        contentLIST = [content]
    if type(content) == list:
        contentLIST = content

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
            resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST=filterLIST, refDICT=refDICT)
            if "msg" in resultDICT:
                break

    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

    if "msg" in resultDICT:
        print(resultDICT["msg"])

def testIntent():
    # play_with_adults
    print("[TEST] play_with_adults")
    inputLIST = ['不行','常常','不一定','不太會','沒辦法','看心情','不太理人','不太確定','會但不多','會但不常','看玩什麼','不跟大人玩','並不會每次','沒什麼反應','只看過一兩次','不喜歡跟大人玩','小孩很喜歡跟人玩','小孩不喜歡別人碰他']
    testLoki(inputLIST, ['play_with_adults'])
    print("")

    # express_needs
    print("[TEST] express_needs")
    inputLIST = ['不多','常常','很少','不一定','不太會','很少見','看心情','不太確定','好像不會','好像沒有','會但不多','會但不常','都用哭的','並不會每次','沒什麼反應','一直做一樣的動作']
    testLoki(inputLIST, ['express_needs'])
    print("")

    # sharing
    print("[TEST] sharing")
    inputLIST = ['不多','常常','很少','不一定','不太會','很少見','看心情','不太理人','不太確定','好像不會','好像沒有','拿著不放','會但不常','都只是拿著','都拿在手裡','只看過一兩次']
    testLoki(inputLIST, ['sharing'])
    print("")

    # imitate_actions
    print("[TEST] imitate_actions")
    inputLIST = ['不行','常常','很少','不一定','不太會','沒辦法','看心情','都可以','不太理人','不太確定','好像不會','好像沒有','會但不多','會但不常','沒什麼反應','只看過一兩次','玩自己的不理人']
    testLoki(inputLIST, ['imitate_actions'])
    print("")

    # understand_short_sentences
    print("[TEST] understand_short_sentences")
    inputLIST = ['常常','很少','不一定','不太會','沒辦法','看心情','還可以','都可以','不太理人','不太確定','好像不會','好像沒有','會但不常','可以但不多','沒什麼反應']
    testLoki(inputLIST, ['understand_short_sentences'])
    print("")

    # reproduce_same_actions
    print("[TEST] reproduce_same_actions")
    inputLIST = ['常常','很少','不一定','不太會','很少見','不太確定','好像不會','好像沒有','會但不多','會但不常','會一直重複動作','一直做一樣的動作']
    testLoki(inputLIST, ['reproduce_same_actions'])
    print("")

    # follow_directions
    print("[TEST] follow_directions")
    inputLIST = ['不行','常常','很少','不一定','不太會','不理人','沒辦法','看心情','都可以','不太理人','不太確定','好像不會','好像沒有','並不會每次','可以但不多']
    testLoki(inputLIST, ['follow_directions'])
    print("")

    # yes_no
    print("[TEST] yes_no")
    inputLIST = ['否','對','有','不對','可以','對啊','沒有','不可以']
    testLoki(inputLIST, ['yes_no'])
    print("")


if __name__ == "__main__":
    # 測試所有意圖
    testIntent()

    # 測試其它句子
    filterLIST = []
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    # 設定參考資料
    refDICT = {
        #"key": []
    }
    resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST=filterLIST, refDICT=refDICT)                      # output => {"key": ["今天天氣"]}
    resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST=filterLIST, splitLIST=splitLIST, refDICT=refDICT) # output => {"key": ["今天天氣", "後天氣象"]}
    resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"], filterLIST=filterLIST, refDICT=refDICT)                # output => {"key": ["今天天氣", "後天氣象"]}