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
    from intent import Loki_say_relative_words
    from intent import Loki_describe_3_or_4_pictures
    from intent import Loki_point_and_count_to_13
    from intent import Loki_self_talking
    from intent import Loki_can_not_follow_directions
    from intent import Loki_cause_effect
    from intent import Loki_yes_no
    from intent import Loki_complete_sentences
    from intent import Loki_disfluent
    from intent import Loki_articulation
    from intent import Loki_basic_knowledge
    from intent import Loki_count_to_30
except:
    from .intent import Loki_say_relative_words
    from .intent import Loki_describe_3_or_4_pictures
    from .intent import Loki_point_and_count_to_13
    from .intent import Loki_self_talking
    from .intent import Loki_can_not_follow_directions
    from .intent import Loki_cause_effect
    from .intent import Loki_yes_no
    from .intent import Loki_complete_sentences
    from .intent import Loki_disfluent
    from .intent import Loki_articulation
    from .intent import Loki_basic_knowledge
    from .intent import Loki_count_to_30


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
try:
    accountInfo = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "account.info"), encoding="utf-8"))
    USERNAME = accountInfo["username"]
    LOKI_KEY = accountInfo["loki_key_above6"]
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
                # say_relative_words
                if lokiRst.getIntent(index, resultIndex) == "say_relative_words":
                    lokiResultDICT = Loki_say_relative_words.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # describe_3_or_4_pictures
                if lokiRst.getIntent(index, resultIndex) == "describe_3_or_4_pictures":
                    lokiResultDICT = Loki_describe_3_or_4_pictures.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # point_and_count_to_13
                if lokiRst.getIntent(index, resultIndex) == "point_and_count_to_13":
                    lokiResultDICT = Loki_point_and_count_to_13.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # self_talking
                if lokiRst.getIntent(index, resultIndex) == "self_talking":
                    lokiResultDICT = Loki_self_talking.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # can_not_follow_directions
                if lokiRst.getIntent(index, resultIndex) == "can_not_follow_directions":
                    lokiResultDICT = Loki_can_not_follow_directions.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # cause_effect
                if lokiRst.getIntent(index, resultIndex) == "cause_effect":
                    lokiResultDICT = Loki_cause_effect.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # yes_no
                if lokiRst.getIntent(index, resultIndex) == "yes_no":
                    lokiResultDICT = Loki_yes_no.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # complete_sentences
                if lokiRst.getIntent(index, resultIndex) == "complete_sentences":
                    lokiResultDICT = Loki_complete_sentences.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # disfluent
                if lokiRst.getIntent(index, resultIndex) == "disfluent":
                    lokiResultDICT = Loki_disfluent.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # articulation
                if lokiRst.getIntent(index, resultIndex) == "articulation":
                    lokiResultDICT = Loki_articulation.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # basic_knowledge
                if lokiRst.getIntent(index, resultIndex) == "basic_knowledge":
                    lokiResultDICT = Loki_basic_knowledge.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # count_to_30
                if lokiRst.getIntent(index, resultIndex) == "count_to_30":
                    lokiResultDICT = Loki_count_to_30.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

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
    # say_relative_words
    print("[TEST] say_relative_words")
    inputLIST = ['不多','不常','很少','不太會','不太行','會但不多','有些可以']
    testLoki(inputLIST, ['say_relative_words'])
    print("")

    # describe_3_or_4_pictures
    print("[TEST] describe_3_or_4_pictures")
    inputLIST = ['不常','不行','不太會','不太行','沒辦法','看心情','講不完整','會跳來跳去','會斷斷續續的']
    testLoki(inputLIST, ['describe_3_or_4_pictures'])
    print("")

    # point_and_count_to_13
    print("[TEST] point_and_count_to_13")
    inputLIST = ['不太會','不太行','不完整','沒問題','跳著唸','只會幾個','跳來跳去','都用指的']
    testLoki(inputLIST, ['point_and_count_to_13'])
    print("")

    # self_talking
    print("[TEST] self_talking")
    inputLIST = ['對','不常','很少','沒錯','不太會','火星語','看心情','一直都是','會一直重覆']
    testLoki(inputLIST, ['self_talking'])
    print("")

    # can_not_follow_directions
    print("[TEST] can_not_follow_directions")
    inputLIST = ['不常','沒錯','不太會','好像是','沒辦法','看心情','都可以做到','好像都聽不懂','都不知道要做什麼']
    testLoki(inputLIST, ['can_not_follow_directions'])
    print("")

    # cause_effect
    print("[TEST] cause_effect")
    inputLIST = ['不行','不太會','有時候','沒辦法','還不懂','不太確定','有些可以','還不理解']
    testLoki(inputLIST, ['cause_effect'])
    print("")

    # yes_no
    print("[TEST] yes_no")
    inputLIST = ['否','對','有','可以','對啊','沒有','不可以']
    testLoki(inputLIST, ['yes_no'])
    print("")

    # complete_sentences
    print("[TEST] complete_sentences")
    inputLIST = ['不多','不常','很少','不太會','看心情','會但不多','講不完整','要看說什麼','都講很短的','可以但不愛說','有說但聽不懂','太長的話就不行了']
    testLoki(inputLIST, ['complete_sentences'])
    print("")

    # disfluent
    print("[TEST] disfluent")
    inputLIST = ['不常','很少','沒錯','不太會','看跟誰說話','緊張的時候會','講得快的時候']
    testLoki(inputLIST, ['disfluent'])
    print("")

    # articulation
    print("[TEST] articulation")
    inputLIST = ['不多','不常','很少','不太會','看跟誰說話','有幾個字會說不清楚']
    testLoki(inputLIST, ['articulation'])
    print("")

    # basic_knowledge
    print("[TEST] basic_knowledge")
    inputLIST = ['不常','不行','不太會','沒辦法','看心情','有些可以','沒什麼反應','要看是什麼問題']
    testLoki(inputLIST, ['basic_knowledge'])
    print("")

    # count_to_30
    print("[TEST] count_to_30")
    inputLIST = ['不行','錯亂','不太會','不完整','唸不完','數不完','沒辦法','跳著唸','有些可以','跳來跳去']
    testLoki(inputLIST, ['count_to_30'])
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