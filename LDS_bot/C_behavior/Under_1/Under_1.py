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
    from intent import Loki_quiet
    from intent import Loki_find_dropped_objects
    from intent import Loki_play_with_adults
    from intent import Loki_family_and_stangers
    from intent import Loki_yes_no
    from intent import Loki_play_sounds
    from intent import Loki_cooing
    from intent import Loki_combined_sounds
    from intent import Loki_look_at_face
    from intent import Loki_laughing
    from intent import Loki_different_sounds
    from intent import Loki_eye_contact
    from intent import Loki_understand_their_own_name
    from intent import Loki_understand_no
except:
    from .intent import Loki_quiet
    from .intent import Loki_find_dropped_objects
    from .intent import Loki_play_with_adults
    from .intent import Loki_family_and_stangers
    from .intent import Loki_yes_no
    from .intent import Loki_play_sounds
    from .intent import Loki_cooing
    from .intent import Loki_combined_sounds
    from .intent import Loki_look_at_face
    from .intent import Loki_laughing
    from .intent import Loki_different_sounds
    from .intent import Loki_eye_contact
    from .intent import Loki_understand_their_own_name
    from .intent import Loki_understand_no


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
try:
    accountInfo = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "account.info"), encoding="utf-8"))
    USERNAME = accountInfo["username"]
    LOKI_KEY = accountInfo["loki_key_under1"]
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
                # quiet
                if lokiRst.getIntent(index, resultIndex) == "quiet":
                    lokiResultDICT = Loki_quiet.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # find_dropped_objects
                if lokiRst.getIntent(index, resultIndex) == "find_dropped_objects":
                    lokiResultDICT = Loki_find_dropped_objects.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # play_with_adults
                if lokiRst.getIntent(index, resultIndex) == "play_with_adults":
                    lokiResultDICT = Loki_play_with_adults.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # family_and_stangers
                if lokiRst.getIntent(index, resultIndex) == "family_and_stangers":
                    lokiResultDICT = Loki_family_and_stangers.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # yes_no
                if lokiRst.getIntent(index, resultIndex) == "yes_no":
                    lokiResultDICT = Loki_yes_no.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # play_sounds
                if lokiRst.getIntent(index, resultIndex) == "play_sounds":
                    lokiResultDICT = Loki_play_sounds.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # cooing
                if lokiRst.getIntent(index, resultIndex) == "cooing":
                    lokiResultDICT = Loki_cooing.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # combined_sounds
                if lokiRst.getIntent(index, resultIndex) == "combined_sounds":
                    lokiResultDICT = Loki_combined_sounds.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # look_at_face
                if lokiRst.getIntent(index, resultIndex) == "look_at_face":
                    lokiResultDICT = Loki_look_at_face.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # laughing
                if lokiRst.getIntent(index, resultIndex) == "laughing":
                    lokiResultDICT = Loki_laughing.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # different_sounds
                if lokiRst.getIntent(index, resultIndex) == "different_sounds":
                    lokiResultDICT = Loki_different_sounds.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # eye_contact
                if lokiRst.getIntent(index, resultIndex) == "eye_contact":
                    lokiResultDICT = Loki_eye_contact.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # understand_their_own_name
                if lokiRst.getIntent(index, resultIndex) == "understand_their_own_name":
                    lokiResultDICT = Loki_understand_their_own_name.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # understand_no
                if lokiRst.getIntent(index, resultIndex) == "understand_no":
                    lokiResultDICT = Loki_understand_no.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

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
    # quiet
    print("[TEST] quiet")
    inputLIST = ['是啊','沒錯','是不會','對不太有聲音','不會哦他都很吵','對一般都很安靜']
    testLoki(inputLIST, ['quiet'])
    print("")

    # find_dropped_objects
    print("[TEST] find_dropped_objects")
    inputLIST = ['常常','很少','不一定','不太會','很少見','看心情','不太確定','會但不常','並不會每次','要看是什麼','只看過一兩次','要看是什麼樣的東西']
    testLoki(inputLIST, ['find_dropped_objects'])
    print("")

    # play_with_adults
    print("[TEST] play_with_adults")
    inputLIST = ['不多','常常','很少','不一定','不太會','很少見','沒辦法','看心情','不太理人','不太看人','不太確定','會但不多','會但不常','不跟大人玩','並不會每次','小孩沒興趣','只看過一兩次','不喜歡跟大人玩']
    testLoki(inputLIST, ['play_with_adults'])
    print("")

    # family_and_stangers
    print("[TEST] family_and_stangers")
    inputLIST = ['不行','常常','不一定','不太會','很少見','沒辦法','看心情','不太確定','分不出來','小孩很害羞','小孩很怕生','沒什麼反應','小孩不太理人','小孩很喜歡跟人玩','小孩不喜歡別人碰他']
    testLoki(inputLIST, ['family_and_stangers'])
    print("")

    # yes_no
    print("[TEST] yes_no")
    inputLIST = ['否','對','有','可以','對啊','沒有','不可以']
    testLoki(inputLIST, ['yes_no'])
    print("")

    # play_sounds
    print("[TEST] play_sounds")
    inputLIST = ['不多','常常','很多','不一定','不太會','看心情','不太確定','會但聲音都很像','不太會而且聲音很少','會但聲音沒什麼變化']
    testLoki(inputLIST, ['play_sounds'])
    print("")

    # cooing
    print("[TEST] cooing")
    inputLIST = ['不多','常常','很多','不太會','沒聽過','沒辦法','看心情','不太確定','會但不多','只聽過一兩次']
    testLoki(inputLIST, ['cooing'])
    print("")

    # combined_sounds
    print("[TEST] combined_sounds")
    inputLIST = ['不多','常常','很多','不一定','不太會','沒聽過','沒辦法','看心情','不太確定','會但不多','只聽過一兩次','可以但沒那麼多種']
    testLoki(inputLIST, ['combined_sounds'])
    print("")

    # look_at_face
    print("[TEST] look_at_face")
    inputLIST = ['不多','常常','看人','不一定','不太會','很少見','沒辦法','不太確定','會但不常','只看過一兩次']
    testLoki(inputLIST, ['look_at_face'])
    print("")

    # laughing
    print("[TEST] laughing")
    inputLIST = ['不多','常常','不一定','不太會','很少見','沒辦法','看心情','不太確定','只看過一兩次']
    testLoki(inputLIST, ['laughing'])
    print("")

    # different_sounds
    print("[TEST] different_sounds")
    inputLIST = ['不多','不常','很多','不一定','不太會','看心情','不太確定']
    testLoki(inputLIST, ['different_sounds'])
    print("")

    # eye_contact
    print("[TEST] eye_contact")
    inputLIST = ['不多','常常','很少','不一定','不太會','很少見','看心情','不太確定','會但不常','小孩不太看人']
    testLoki(inputLIST, ['eye_contact'])
    print("")

    # understand_their_own_name
    print("[TEST] understand_their_own_name")
    inputLIST = ['不行','常常','很少','不一定','不太會','不理人','沒辦法','看心情','不太確定','會但不常','並不會每次','沒什麼反應','只看過一兩次','小孩不太理人']
    testLoki(inputLIST, ['understand_their_own_name'])
    print("")

    # understand_no
    print("[TEST] understand_no")
    inputLIST = ['是','不行','常常','不一定','不太會','看心情','不太理人','不太確定','會但不多','會但不常','並不會每次','沒什麼反應','玩自己的不理人','玩自己的沒反應']
    testLoki(inputLIST, ['understand_no'])
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