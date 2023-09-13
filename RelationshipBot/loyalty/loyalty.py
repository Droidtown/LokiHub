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
    from intent import Loki_other
    from intent import Loki_self
except:
    from .intent import Loki_other
    from .intent import Loki_self


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
try:
    accountInfo = json.load(open(os.path.join(os.path.dirname(__file__), "account.info"), encoding="utf-8"))
    USERNAME = accountInfo["username"]
    LOKI_KEY = accountInfo["loki_key"]
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
                # other
                if lokiRst.getIntent(index, resultIndex) == "other":
                    lokiResultDICT = Loki_other.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # self
                if lokiRst.getIntent(index, resultIndex) == "self":
                    lokiResultDICT = Loki_self.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

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
    # other
    print("[TEST] other")
    inputLIST = ['對方出軌','對方劈腿','對方外遇','男友出軌','男友劈腿','男友外遇','對方是渣男','對方有炮友','對方好像出軌','對方好像劈腿','對方戴我綠帽','對方曾經約過炮','對方有兩支手機','對方腳踏兩條船','男友腳踏兩條船','對方好像戴我綠帽','對方帶別人去旅館','對方很多女生朋友','對方會偷看我兄弟','對方會和他妹上床','對方會和別人幽會','對方會載別人回家','對方無法讓我信任','對方瞞著我開小帳','對方約別人去旅館','對方被我捉姦在床','對方跟別人去旅館','對方追蹤很多正妹','對方騙我他沒出軌','對方騙我他沒劈腿','男人的嘴騙人的鬼','對方不讓我看他LINE','對方不讓我看他手機','對方和前任沒分乾淨','對方和前任藕斷絲連','對方好像腳踏兩條船','對方已經出軌好幾次','對方已經劈腿好幾次','對方愛和別人搞曖昧','對方會偷看我的兄弟','對方會和別人搞曖昧','對方會和她妹妹上床','對方會讓別人坐前座','對方讓我沒有安全感','對方騙我說他沒出軌','對方騙我說他沒劈腿','對方偷偷下載交友軟體','對方偷偷下載約炮軟體','對方和前女友沒分乾淨','對方和前女友藕斷絲連','對方已經出軌很多次了','對方已經劈腿很多次了','對方還留著前任的東西','對方不能接受開放性關係','對方會和別人傳曖昧訊息','對方不知道和別人保持距離','對方不知道和別人劃清界線','對方和他前女友還有在連絡','對方會載別的女生朋友回家','對方還留著他前女友的東西','對方不知道要和別人保持距離','對方不知道要和別人劃清界線','對方會讓別的女生朋友坐前座']
    testLoki(inputLIST, ['other'])
    print("")

    # self
    print("[TEST] self")
    inputLIST = ['我出軌','我劈腿','我被劈腿','我好像被劈腿','我常常精神出軌','我戴我女友綠帽','我會載別人回家','我被兄弟戴綠帽','我被腳踏兩條船','我不想再原諒他了','我只是去旅館休息','我只是去旅館開會','我會讓別人坐前座','我被我兄弟戴綠帽','我被我女友戴綠帽','我騙他我沒有出軌','我騙他我沒有劈腿','我和前女友只是朋友','我和前女友還有聯絡','我好像被兄弟戴綠帽','我已經出軌好幾次了','我已經出軌很多次了','我已經劈腿好幾次了','我已經劈腿很多次了','我沒辦法再相信他了','我還留著前任的東西','我騙他說我沒有出軌','我騙他說我沒有劈腿','對方逼我封鎖我前女友','我只是不小心就滑進去','我好像被我兄弟戴綠帽','我無法克制自己不出軌','我無法克制自己不劈腿','我認為他不應該原諒我','我還留著前女友的東西','我會載其他女生朋友回家','我會讓其他女生朋友坐前座','我只是犯了全天下男人都會犯的錯']
    testLoki(inputLIST, ['self'])
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