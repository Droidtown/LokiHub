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
    from intent import Loki_play_alone
    from intent import Loki_say_color
    from intent import Loki_four_to_five_words_sentences
    from intent import Loki_function_of_4_objects
    from intent import Loki_point_and_count_to_5
    from intent import Loki_repeat_3_words_sentences
    from intent import Loki_location_words
    from intent import Loki_yes_no
    from intent import Loki_sentence_repetition
    from intent import Loki_articulation
except:
    from .intent import Loki_play_alone
    from .intent import Loki_say_color
    from .intent import Loki_four_to_five_words_sentences
    from .intent import Loki_function_of_4_objects
    from .intent import Loki_point_and_count_to_5
    from .intent import Loki_repeat_3_words_sentences
    from .intent import Loki_location_words
    from .intent import Loki_yes_no
    from .intent import Loki_sentence_repetition
    from .intent import Loki_articulation


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
try:
    accountInfo = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "account.info"), encoding="utf-8"))
    USERNAME = accountInfo["username"]
    LOKI_KEY = accountInfo["loki_key_above4"]
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
                # play_alone
                if lokiRst.getIntent(index, resultIndex) == "play_alone":
                    lokiResultDICT = Loki_play_alone.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # say_color
                if lokiRst.getIntent(index, resultIndex) == "say_color":
                    lokiResultDICT = Loki_say_color.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # four_to_five_words_sentences
                if lokiRst.getIntent(index, resultIndex) == "four_to_five_words_sentences":
                    lokiResultDICT = Loki_four_to_five_words_sentences.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # function_of_4_objects
                if lokiRst.getIntent(index, resultIndex) == "function_of_4_objects":
                    lokiResultDICT = Loki_function_of_4_objects.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # point_and_count_to_5
                if lokiRst.getIntent(index, resultIndex) == "point_and_count_to_5":
                    lokiResultDICT = Loki_point_and_count_to_5.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # repeat_3_words_sentences
                if lokiRst.getIntent(index, resultIndex) == "repeat_3_words_sentences":
                    lokiResultDICT = Loki_repeat_3_words_sentences.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # location_words
                if lokiRst.getIntent(index, resultIndex) == "location_words":
                    lokiResultDICT = Loki_location_words.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # yes_no
                if lokiRst.getIntent(index, resultIndex) == "yes_no":
                    lokiResultDICT = Loki_yes_no.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # sentence_repetition
                if lokiRst.getIntent(index, resultIndex) == "sentence_repetition":
                    lokiResultDICT = Loki_sentence_repetition.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # articulation
                if lokiRst.getIntent(index, resultIndex) == "articulation":
                    lokiResultDICT = Loki_articulation.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

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
    # play_alone
    print("[TEST] play_alone")
    inputLIST = ['對','常常','不太會','好像有','很少見','看心情','一直都是','好像不會','好像沒有','很常這樣','會但不常','不跟大人玩','小孩很怕生','小孩沒興趣','一直都是這樣','不喜歡跟大人玩','有聽學校老師說過','對都玩自己的不理人','從以前就不喜歡跟別人玩']
    testLoki(inputLIST, ['play_alone'])
    print("")

    # say_color
    print("[TEST] say_color")
    inputLIST = ['不行','偶爾','錯亂','不太行','會說錯','沒聽過','沒辦法','都可以','好像不會','好像可以','會但不常','還不太會','應該有超過','會但不愛說','會搞錯顏色','顏色都錯亂','可以但不愛講','會說但發音不清楚']
    testLoki(inputLIST, ['say_color'])
    print("")

    # four_to_five_words_sentences
    print("[TEST] four_to_five_words_sentences")
    inputLIST = ['對','不常','不行','很少','不太會','不太行','沒聽過','沒辦法','看心情','算有哦','還可以','都可以','不常這樣','好像沒有','會但不多','會但不常','講不完整','會但不愛說','會但不愛講','看跟誰說話','都說很短的','都講很短的','只聽過一兩次','有說但聽不懂','太長的話就不行了','會但都是說類似的','會但都是固定那幾句']
    testLoki(inputLIST, ['four_to_five_words_sentences'])
    print("")

    # function_of_4_objects
    print("[TEST] function_of_4_objects")
    inputLIST = ['不常','不行','很少','不太會','不太行','沒聽過','沒辦法','還可以','都可以','好像不會','好像可以','可以但不多','會但不愛說','會但不愛講','會但不到4個','只聽過一兩次','有而且超過四個','可以但沒那麼多種','要看是什麼樣的東西']
    testLoki(inputLIST, ['function_of_4_objects'])
    print("")

    # point_and_count_to_5
    print("[TEST] point_and_count_to_5")
    inputLIST = ['不常','不行','很少','不太會','不太行','沒辦法','都可以','好像不會','好像可以','會但不常','應該有超過','都只用指的','會但不到5個']
    testLoki(inputLIST, ['point_and_count_to_5'])
    print("")

    # repeat_3_words_sentences
    print("[TEST] repeat_3_words_sentences")
    inputLIST = ['不常','不行','很少','不一定','不太會','不太行','不說話','沒辦法','看心情','都可以','不到三個','會但不常','講不完整','停一下再講','可以但不多','斷斷續續的','會但不愛講','要看說什麼','都說很短的','都講很短的','可以但不愛說','有說但聽不懂','不能連在一起說','短的才有辦法說','長一點就不會講','太長的話就不行了']
    testLoki(inputLIST, ['repeat_3_words_sentences'])
    print("")

    # location_words
    print("[TEST] location_words")
    inputLIST = ['不行','偶爾','不一定','不太會','不太行','沒聽過','沒辦法','看心情','只會幾個','好像不會','好像可以','搞不清楚','會但不多','會但不常','會但不愛講','有時會搞錯']
    testLoki(inputLIST, ['location_words'])
    print("")

    # yes_no
    print("[TEST] yes_no")
    inputLIST = ['否','對','有','不對','可以','對啊','沒有','不可以']
    testLoki(inputLIST, ['yes_no'])
    print("")

    # sentence_repetition
    print("[TEST] sentence_repetition")
    inputLIST = ['對','不常','很少','不太會','好像有','火星語','看心情','算有哦','一直都是','好像不會','好像沒有','很常這樣','會但不多','會但不常','會一直重覆','一直都是這樣']
    testLoki(inputLIST, ['sentence_repetition'])
    print("")

    # articulation
    print("[TEST] articulation")
    inputLIST = ['對','不常','很少','沒錯','不太會','一直都是','好像不會','很常這樣','會但不多','會但不常','大家都聽不懂','大家都聽得懂','有幾個字會說不清楚']
    testLoki(inputLIST, ['articulation'])
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