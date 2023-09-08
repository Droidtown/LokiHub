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
    from intent import Loki_ten_words
    from intent import Loki_imitate_and_say
    from intent import Loki_gesture
    from intent import Loki_say_with_gestures
    from intent import Loki_combined_words
    from intent import Loki_imitate_and_act
    from intent import Loki_100_words
    from intent import Loki_two_steps_directions
    from intent import Loki_not_listen
    from intent import Loki_yes_no
    from intent import Loki_point_pictures
    from intent import Loki_4_body_parts
    from intent import Loki_reading_books
except:
    from .intent import Loki_ten_words
    from .intent import Loki_imitate_and_say
    from .intent import Loki_gesture
    from .intent import Loki_say_with_gestures
    from .intent import Loki_combined_words
    from .intent import Loki_imitate_and_act
    from .intent import Loki_100_words
    from .intent import Loki_two_steps_directions
    from .intent import Loki_not_listen
    from .intent import Loki_yes_no
    from .intent import Loki_point_pictures
    from .intent import Loki_4_body_parts
    from .intent import Loki_reading_books


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
try:
    accountInfo = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "account.info"), encoding="utf-8"))
    USERNAME = accountInfo["username"]
    LOKI_KEY = accountInfo["loki_key_above2"]
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
                # ten_words
                if lokiRst.getIntent(index, resultIndex) == "ten_words":
                    lokiResultDICT = Loki_ten_words.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # imitate_and_say
                if lokiRst.getIntent(index, resultIndex) == "imitate_and_say":
                    lokiResultDICT = Loki_imitate_and_say.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # gesture
                if lokiRst.getIntent(index, resultIndex) == "gesture":
                    lokiResultDICT = Loki_gesture.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # say_with_gestures
                if lokiRst.getIntent(index, resultIndex) == "say_with_gestures":
                    lokiResultDICT = Loki_say_with_gestures.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # combined_words
                if lokiRst.getIntent(index, resultIndex) == "combined_words":
                    lokiResultDICT = Loki_combined_words.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # imitate_and_act
                if lokiRst.getIntent(index, resultIndex) == "imitate_and_act":
                    lokiResultDICT = Loki_imitate_and_act.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # 100_words
                if lokiRst.getIntent(index, resultIndex) == "100_words":
                    lokiResultDICT = Loki_100_words.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # two_steps_directions
                if lokiRst.getIntent(index, resultIndex) == "two_steps_directions":
                    lokiResultDICT = Loki_two_steps_directions.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # not_listen
                if lokiRst.getIntent(index, resultIndex) == "not_listen":
                    lokiResultDICT = Loki_not_listen.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # yes_no
                if lokiRst.getIntent(index, resultIndex) == "yes_no":
                    lokiResultDICT = Loki_yes_no.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # point_pictures
                if lokiRst.getIntent(index, resultIndex) == "point_pictures":
                    lokiResultDICT = Loki_point_pictures.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # 4_body_parts
                if lokiRst.getIntent(index, resultIndex) == "4_body_parts":
                    lokiResultDICT = Loki_4_body_parts.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # reading_books
                if lokiRst.getIntent(index, resultIndex) == "reading_books":
                    lokiResultDICT = Loki_reading_books.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

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
    # ten_words
    print("[TEST] ten_words")
    inputLIST = ['不行','很少','不太會','有時候','沒辦法','看心情','算有哦','都可以','不太確定','好像沒有','都用叫的','都用哭的','可以但不多','拉大人去拿','還不會說話','會但不到10個','只聽過一兩次','有說但聽不懂','不說話都用指的','可以但沒那麼多','有而且超過十個','沒聽過小孩說話']
    testLoki(inputLIST, ['ten_words'])
    print("")

    # imitate_and_say
    print("[TEST] imitate_and_say")
    inputLIST = ['不行','常常','很少','沒有','不一定','不太會','沒聽過','沒辦法','看心情','算有哦','都可以','不太理人','不太確定','好像不會','好像沒有','會但不多','會但不常','講不完整','並不會每次','沒什麼反應','還不會說話','都說很短的','都講很短的','只會出個聲音','只聽過一兩次','有說但聽不懂','只會動一下嘴巴','沒聽過小孩說話','短的才有辦法說','長一點就不會講','可以但沒那麼多種','太長的話就不行了']
    testLoki(inputLIST, ['imitate_and_say'])
    print("")

    # gesture
    print("[TEST] gesture")
    inputLIST = ['常常','很少','不一定','不太會','很少見','看心情','算有哦','一直都是','不太確定','好像不會','好像沒有','會但不多','會但不常','只看過一兩次']
    testLoki(inputLIST, ['gesture'])
    print("")

    # say_with_gestures
    print("[TEST] say_with_gestures")
    inputLIST = ['不多','常常','很少','沒有','不一定','不太會','不說話','很少見','沒聽過','沒辦法','看心情','算有哦','不太確定','好像不會','好像沒有','會但不多','會但不常','都用叫的','都用哭的','都用指的','並不會每次','都只用指的','只看過一兩次','只聽過一兩次']
    testLoki(inputLIST, ['say_with_gestures'])
    print("")

    # combined_words
    print("[TEST] combined_words")
    inputLIST = ['不多','常常','很多','沒有','不太會','不太行','不說話','好像有','沒聽過','沒辦法','看心情','算有哦','都可以','不太確定','不常這樣','好像不會','好像可以','好像沒有','會但不多','會但不常','都說很短的','都講很短的','只聽過一兩次','可以但不愛說','可以但不愛講','有說但聽不懂']
    testLoki(inputLIST, ['combined_words'])
    print("")

    # imitate_and_act
    print("[TEST] imitate_and_act")
    inputLIST = ['不行','常常','很少','不太會','不太行','沒辦法','看心情','算有哦','都可以','不太確定','不常這樣','好像不會','好像可以','好像沒有','會但不常','可以但不多','小孩沒興趣','只看過一兩次','可以但沒那麼多種']
    testLoki(inputLIST, ['imitate_and_act'])
    print("")

    # 100_words
    print("[TEST] 100_words")
    inputLIST = ['不常','不行','沒有','不太會','不太行','不說話','好像有','沒聽過','沒辦法','火星語','算有哦','不太確定','好像不會','好像可以','好像沒有','都用哭的','應該有超過','會但不愛講','會但不會說','還不會說話','都只用指的','只會出個聲音','只聽過一兩次','可以但不愛說','會但不到100個','有說但聽不懂','可以但沒那麼多','沒聽過小孩說話']
    testLoki(inputLIST, ['100_words'])
    print("")

    # two_steps_directions
    print("[TEST] two_steps_directions")
    inputLIST = ['不行','常常','很少','不太會','都可以','不太確定','好像不會','好像可以','好像沒有','會但不多','沒什麼反應']
    testLoki(inputLIST, ['two_steps_directions'])
    print("")

    # not_listen
    print("[TEST] not_listen")
    inputLIST = ['是的','不一定','看心情','不會這樣','好像不會','就是這樣','常常這樣','有時候不聽']
    testLoki(inputLIST, ['not_listen'])
    print("")

    # yes_no
    print("[TEST] yes_no")
    inputLIST = ['否','對','有','可以','對啊','沒有','不可以']
    testLoki(inputLIST, ['yes_no'])
    print("")

    # point_pictures
    print("[TEST] point_pictures")
    inputLIST = ['不行','常常','不太會','不太行','好像有','沒辦法','看心情','不太確定','好像不會','好像可以','會但不常','小孩沒興趣']
    testLoki(inputLIST, ['point_pictures'])
    print("")

    # 4_body_parts
    print("[TEST] 4_body_parts")
    inputLIST = ['不行','常常','不太會','沒辦法','看心情','算有哦','都可以','好像不會','好像可以','好像沒有','會但不多','沒什麼反應','會但不到四個']
    testLoki(inputLIST, ['4_body_parts'])
    print("")

    # reading_books
    print("[TEST] reading_books")
    inputLIST = ['不常','不行','咬書','很少','撕書','不太會','沒辦法','看心情','都可以','好像不會','好像可以','好像沒有','會把書丟掉','會把書用壞']
    testLoki(inputLIST, ['reading_books'])
    print("")


if __name__ == "__main__":
    # 測試所有意圖
    # testIntent()

    # 測試其它句子
    filterLIST = ["yes_no", "combined_words"]
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    # 設定參考資料
    refDICT = {
        #"key": []
    }
    # resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST=filterLIST, refDICT=refDICT)                      # output => {"key": ["今天天氣"]}
    resultDICT = execLoki("可以", filterLIST=filterLIST, splitLIST=splitLIST, refDICT=refDICT) # output => {"key": ["今天天氣", "後天氣象"]}
    # resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"], filterLIST=filterLIST, refDICT=refDICT)                # output => {"key": ["今天天氣", "後天氣象"]}
    print(resultDICT)