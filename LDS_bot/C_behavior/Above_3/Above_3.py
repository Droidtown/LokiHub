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

from copy import deepcopy
from requests import post
from requests import codes
import json
import math
import os
import re
try:
    from intent import Loki_hundreds_word
    from intent import Loki_wrong_answer
    from intent import Loki_complete_snetences
    from intent import Loki_answer_with_sentences
    from intent import Loki_wh_questions
    from intent import Loki_sentence_repetition
    from intent import Loki_function_for_objects
    from intent import Loki_know_color
    from intent import Loki_compare
    from intent import Loki_yes_no
    from intent import Loki_articualtion
    from intent import Loki_pronouns
    from intent import Loki_matching
except:
    from .intent import Loki_hundreds_word
    from .intent import Loki_wrong_answer
    from .intent import Loki_complete_snetences
    from .intent import Loki_answer_with_sentences
    from .intent import Loki_wh_questions
    from .intent import Loki_sentence_repetition
    from .intent import Loki_function_for_objects
    from .intent import Loki_know_color
    from .intent import Loki_compare
    from .intent import Loki_yes_no
    from .intent import Loki_articualtion
    from .intent import Loki_pronouns
    from .intent import Loki_matching


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
try:
    accountInfo = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "account.info"), encoding="utf-8"))
    USERNAME = accountInfo["username"]
    LOKI_KEY = accountInfo["loki_key_above3"]
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
    resultDICT = deepcopy(refDICT)
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            lokiResultDICT = {}
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # hundreds_word
                if lokiRst.getIntent(index, resultIndex) == "hundreds_word":
                    lokiResultDICT = Loki_hundreds_word.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # wrong_answer
                if lokiRst.getIntent(index, resultIndex) == "wrong_answer":
                    lokiResultDICT = Loki_wrong_answer.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # complete_snetences
                if lokiRst.getIntent(index, resultIndex) == "complete_snetences":
                    lokiResultDICT = Loki_complete_snetences.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # answer_with_sentences
                if lokiRst.getIntent(index, resultIndex) == "answer_with_sentences":
                    lokiResultDICT = Loki_answer_with_sentences.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # wh_questions
                if lokiRst.getIntent(index, resultIndex) == "wh_questions":
                    lokiResultDICT = Loki_wh_questions.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # sentence_repetition
                if lokiRst.getIntent(index, resultIndex) == "sentence_repetition":
                    lokiResultDICT = Loki_sentence_repetition.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # function_for_objects
                if lokiRst.getIntent(index, resultIndex) == "function_for_objects":
                    lokiResultDICT = Loki_function_for_objects.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # know_color
                if lokiRst.getIntent(index, resultIndex) == "know_color":
                    lokiResultDICT = Loki_know_color.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # compare
                if lokiRst.getIntent(index, resultIndex) == "compare":
                    lokiResultDICT = Loki_compare.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # yes_no
                if lokiRst.getIntent(index, resultIndex) == "yes_no":
                    lokiResultDICT = Loki_yes_no.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # articualtion
                if lokiRst.getIntent(index, resultIndex) == "articualtion":
                    lokiResultDICT = Loki_articualtion.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # pronouns
                if lokiRst.getIntent(index, resultIndex) == "pronouns":
                    lokiResultDICT = Loki_pronouns.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # matching
                if lokiRst.getIntent(index, resultIndex) == "matching":
                    lokiResultDICT = Loki_matching.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

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
    resultDICT = deepcopy(refDICT)
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
    # hundreds_word
    print("[TEST] hundreds_word")
    inputLIST = ['不行','很少','不太會','不太行','不說話','好像有','沒辦法','算有哦','都可以','好像不會','好像可以','好像沒有','會但不愛說','有而且超過','還不會說話','可以但不愛講','有說但聽不懂','會但不到一百個']
    testLoki(inputLIST, ['hundreds_word'])
    print("")

    # wrong_answer
    print("[TEST] wrong_answer")
    inputLIST = ['對','常常','很少','不太會','好像不會','很常這樣','會但不常','一直都是這樣']
    testLoki(inputLIST, ['wrong_answer'])
    print("")

    # complete_snetences
    print("[TEST] complete_snetences")
    inputLIST = ['不行','常常','不太會','不太行','沒辦法','算有哦','好像可以','很常這樣','會但不多','講不完整','會但不愛說','會但不愛講','都說很短的','都講很短的','有說但聽不懂']
    testLoki(inputLIST, ['complete_snetences'])
    print("")

    # answer_with_sentences
    print("[TEST] answer_with_sentences")
    inputLIST = ['不行','常常','很少','不太會','看心情','都可以','不太理人','不常這樣','好像不會','好像可以','會但不常','會但不愛說','會但不愛講']
    testLoki(inputLIST, ['answer_with_sentences'])
    print("")

    # wh_questions
    print("[TEST] wh_questions")
    inputLIST = ['不常','不行','不太會','不太行','沒辦法','算有哦','都可以','好像不會','好像可以']
    testLoki(inputLIST, ['wh_questions'])
    print("")

    # sentence_repetition
    print("[TEST] sentence_repetition")
    inputLIST = ['對','常常','不太會','好像有','很少見','好像不會','很常這樣']
    testLoki(inputLIST, ['sentence_repetition'])
    print("")

    # function_for_objects
    print("[TEST] function_for_objects")
    inputLIST = ['不常','不行','很少','不太會','不太行','沒辦法','都可以','好像不會','好像可以']
    testLoki(inputLIST, ['function_for_objects'])
    print("")

    # know_color
    print("[TEST] know_color")
    inputLIST = ['不行','不太會','不太行','沒辦法','算有哦','都可以','分不出來','好像不會','好像可以']
    testLoki(inputLIST, ['know_color'])
    print("")

    # compare
    print("[TEST] compare")
    inputLIST = ['不行','偶爾','不太會','不太行','沒辦法','算有哦','都可以','不太確定','好像不會','好像可以']
    testLoki(inputLIST, ['compare'])
    print("")

    # yes_no
    print("[TEST] yes_no")
    inputLIST = ['否','對','有','不對','可以','對啊','沒有','不可以']
    testLoki(inputLIST, ['yes_no'])
    print("")

    # articualtion
    print("[TEST] articualtion")
    inputLIST = ['對','是','沒錯','不太會','有時候','好像沒有','很常這樣','發音不標準','說得不清楚']
    testLoki(inputLIST, ['articualtion'])
    print("")

    # pronouns
    print("[TEST] pronouns")
    inputLIST = ['不常','不行','很少','不太會','會錯亂','沒辦法','你我不分','好像不會','好像可以','搞不清楚','有時會搞錯']
    testLoki(inputLIST, ['pronouns'])
    print("")

    # matching
    print("[TEST] matching")
    inputLIST = ['不常','不行','不太會','不太行','都可以','不太確定','分不出來','好像不會']
    testLoki(inputLIST, ['matching'])
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