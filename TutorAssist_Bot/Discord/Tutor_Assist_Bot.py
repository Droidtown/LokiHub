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
import json
try:
    from intent import Loki_physical_course
    from intent import Loki_class_arrangement
    from intent import Loki_agree_adv
    from intent import Loki_warm_blessing
    from intent import Loki_disagree_adv
    from intent import Loki_online_course
    from intent import Loki_infrom_time
    from intent import Loki_day_off
except:
    from .intent import Loki_physical_course
    from .intent import Loki_class_arrangement
    from .intent import Loki_agree_adv
    from .intent import Loki_warm_blessing
    from .intent import Loki_disagree_adv
    from .intent import Loki_online_course
    from .intent import Loki_infrom_time
    from .intent import Loki_day_off


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
accountDICT = json.load(open("account.info",encoding="utf-8"))
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
        "intentLIST":[],
       #"key": []
    }
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # physical_course
                if lokiRst.getIntent(index, resultIndex) == "physical_course":
                    resultDICT = Loki_physical_course.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # class_arrangement
                if lokiRst.getIntent(index, resultIndex) == "class_arrangement":
                    resultDICT = Loki_class_arrangement.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # agree_adv
                if lokiRst.getIntent(index, resultIndex) == "agree_adv":
                    resultDICT = Loki_agree_adv.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # warm_blessing
                if lokiRst.getIntent(index, resultIndex) == "warm_blessing":
                    resultDICT = Loki_warm_blessing.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # disagree_adv
                if lokiRst.getIntent(index, resultIndex) == "disagree_adv":
                    resultDICT = Loki_disagree_adv.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # online_course
                if lokiRst.getIntent(index, resultIndex) == "online_course":
                    resultDICT = Loki_online_course.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # infrom_time
                if lokiRst.getIntent(index, resultIndex) == "infrom_time":
                    resultDICT = Loki_infrom_time.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # day_off
                if lokiRst.getIntent(index, resultIndex) == "day_off":
                    resultDICT = Loki_day_off.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

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
    # physical_course
    print("[TEST] physical_course")
    inputLIST = ['先實體','先線下','先進班','先面授','先到線下','先改到班','先改實體','先改線下','先改進班','先改面授','先用到班','先用實體','先用線下','先用進班','先用面授','先都到府','先都到班','先都實體','先都線下','先都進班','先都面授','先面對面','要先到班','要先實體','要先線下','要先進班','要先面授','先到府上課','先到府授課','先到班上課','先實體課程','先恢復到班','先恢復實體','先恢復線下','先恢復進班','先恢復面授','先改面對面','先用面對面','先都面對面','要先面對面','要實體課程','先到家中上課','先到家中授課','先恢復面對面','先改實體課程','先用實體課程','先調整為到班','先調整為實體','先調整為線下','先調整為進班','先調整為面授','先都實體課程','先恢復實體課程','先調整為實體課程']
    testLoki(inputLIST, ['physical_course'])
    print("")

    # class_arrangement
    print("[TEST] class_arrangement")
    inputLIST = ['8.OK嗎','改時間','8.你OK嗎','XX先改8.','討論時間','調整時間','8.老師OK嗎','XX先換到8.','XX先換成8.','XX先換至8.','XX先改到8.','XX先改至8.','XX先調到8.','XX先調成8.','XX先調至8.','8.你可以嗎','8.你方便嗎','XX先改八點','八點你OK嗎','弟弟先改8.','改XX的時間','改一下時間','改上課時間','XX先延後到8.','XX先提早到8.','XX先調整到8.','XX先調整成8.','XX先調整至8.','8.老師可以嗎','8.老師方便嗎','XX先換到八點','XX先換成八點','XX先換至八點','XX先改到八點','XX先改至八點','XX先調到八點','XX先調成八點','XX先調至八點','八點老師OK嗎','弟弟先換到8.','弟弟先換成8.','弟弟先換至8.','弟弟先改到8.','弟弟先改至8.','弟弟先調到8.','弟弟先調成8.','弟弟先調至8.','討論XX的時間','調整XX的時間','八點你方便嗎','弟弟先改八點','改弟弟的時間','改週四的時間','討論一下時間','討論上課時間','調整一下時間','調整上課時間','XX可能要先改8.','XX先延後到八點','XX先延後半小時','XX先提早到八點','XX先提早半小時','XX先調整到八點','XX先調整成八點','XX先調整至八點','弟弟先延後到8.','弟弟先提早到8.','弟弟先調整到8.','弟弟先調整成8.','弟弟先調整至8.','改一下XX的時間','八點老師可以嗎','八點老師方便嗎','弟弟先換到八點','弟弟先換成八點','弟弟先換至八點','弟弟先改到八點','弟弟先改至八點','弟弟先調到八點','弟弟先調成八點','弟弟先調至八點','改一下上課時間','討論弟弟的時間','討論週四的時間','調整弟弟的時間','調整週四的時間','8.可以幫XX上課嗎','XX可能要先換到8.','XX可能要先換成8.','XX可能要先換至8.','XX可能要先改到8.','XX可能要先改至8.','XX可能要先調到8.','XX可能要先調成8.','XX可能要先調至8.','XX先延後一小時半','XX先延後半個小時','XX先提早一小時半','XX先提早半個小時','XX可能要先改八點','弟弟可能要先改8.','討論一下XX的時間','調整一下XX的時間','弟弟先延後到八點','弟弟先延後半小時','弟弟先提早到八點','弟弟先提早半小時','弟弟先調整到八點','弟弟先調整成八點','弟弟先調整至八點','改一下弟弟的時間','改一下週四的時間','討論一下上課時間','調整一下上課時間','XX可能要先延後到8.','XX可能要先提早到8.','XX可能要先調整到8.','XX可能要先調整成8.','XX可能要先調整至8.','8.可以幫弟弟上課嗎','XX先延後一個小時半','XX可能要先換到八點','XX可能要先換成八點','XX可能要先換至八點','XX可能要先改到八點','XX可能要先改至八點','XX可能要先調到八點','XX可能要先調成八點','XX可能要先調至八點','弟弟可能要先換到8.','弟弟可能要先換成8.','弟弟可能要先換至8.','弟弟可能要先改到8.','弟弟可能要先改至8.','弟弟可能要先調到8.','弟弟可能要先調成8.','弟弟可能要先調至8.','弟弟先延後一小時半','弟弟先延後半個小時','弟弟先提早一小時半','弟弟先提早半個小時','弟弟可能要先改八點','討論一下弟弟的時間','討論一下週四的時間','調整一下弟弟的時間','調整一下週四的時間','XX可能要先延後到八點','XX可能要先延後半小時','XX可能要先提早到八點','XX可能要先提早半小時','XX可能要先調整到八點','XX可能要先調整成八點','XX可能要先調整至八點','弟弟可能要先延後到8.','弟弟可能要先提早到8.','弟弟可能要先調整到8.','弟弟可能要先調整成8.','弟弟可能要先調整至8.','禮拜天可以幫XX上課嗎','弟弟先延後一個小時半','弟弟可能要先換到八點','弟弟可能要先換成八點','弟弟可能要先換至八點','弟弟可能要先改到八點','弟弟可能要先改至八點','弟弟可能要先調到八點','弟弟可能要先調成八點','弟弟可能要先調至八點','XX可能要先延後一小時半','XX可能要先延後半個小時','XX可能要先提早一小時半','XX可能要先提早半個小時','弟弟可能要先延後到八點','弟弟可能要先延後半小時','弟弟可能要先提早到八點','弟弟可能要先提早半小時','弟弟可能要先調整到八點','弟弟可能要先調整成八點','弟弟可能要先調整至八點','禮拜天可以幫弟弟上課嗎','XX可能要先延後一個小時半','弟弟可能要先延後一小時半','弟弟可能要先延後半個小時','弟弟可能要先提早一小時半','弟弟可能要先提早半個小時','弟弟可能要先延後一個小時半']
    testLoki(inputLIST, ['class_arrangement'])
    print("")

    # agree_adv
    print("[TEST] agree_adv")
    inputLIST = ['ok','yes','好','對','是','okay','好的','正確','沒錯','沒問題']
    testLoki(inputLIST, ['agree_adv'])
    print("")

    # warm_blessing
    print("[TEST] warm_blessing")
    inputLIST = ['祝你','祝老師','假期快樂','假期愉快','中秋節快樂','中秋節愉快']
    testLoki(inputLIST, ['warm_blessing'])
    print("")

    # disagree_adv
    print("[TEST] disagree_adv")
    inputLIST = ['no','錯','不對','不是','錯誤','不正確']
    testLoki(inputLIST, ['disagree_adv'])
    print("")

    # online_course
    print("[TEST] online_course")
    inputLIST = ['先線上','先視訊','先遠距','先改線上','先改視訊','先改遠距','先用線上','先用視訊','先用遠距','先都線上','先都視訊','先都遠距','要先線上','要先視訊','要先遠距','先恢復線上','先恢復視訊','先恢復遠距','先維持線上','先維持視訊','先維持遠距','先調整為線上','先調整為視訊','先調整為遠距']
    testLoki(inputLIST, ['online_course'])
    print("")

    # infrom_time
    print("[TEST] infrom_time")
    inputLIST = ['8.','8.-10.','8.到10.','8.至10.','8:30-10.','8:30-10:30','8:30到10.','8:30至10.','8:30到10:30','8:30至10:30','八月三十','八點-十點','八月三十日','八點到十點','八點至十點','八月三十的10.-12.','八月三十的10.到12.','八月三十的10.至12.','八月三十的10:30-12.','八月三十日的10.-12.','八月三十的10:30-12:00','八月三十的10:30到12.','八月三十的10:30至12.','八月三十日的10.到12.','八月三十日的10.至12.','八月三十的10:30到12:00','八月三十的10:30至12:00']
    testLoki(inputLIST, ['infrom_time'])
    print("")

    # day_off
    print("[TEST] day_off")
    inputLIST = ['XX先休息','XX先停課','XX先暫停','XX先病假','XX先請假','先不用來','XX先請病假','今天先休息','今天先停課','今天先暫停','今天先病假','今天先請假','先不上課喔','弟弟先休息','弟弟先停課','弟弟先暫停','弟弟先病假','弟弟先請假','今天先請病假','先不用過來喔','弟弟先請病假','XX可能要先休息','XX可能要先停課','XX可能要先暫停','XX可能要先病假','XX可能要先請假','先不用幫XX上課','XX可能要先休息了','XX可能要先停課了','XX可能要先暫停了','XX可能要先請假了','XX可能要先請病假','今天可能要先休息','今天可能要先停課','今天可能要先暫停','今天可能要先病假','今天可能要先請假','先不用幫弟弟上課','今天可能要先請病假']
    testLoki(inputLIST, ['day_off'])
    print("")


if __name__ == "__main__":
    # 測試所有意圖
    #testIntent()

    # 測試其它句子
    #filterLIST = []
    #splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    #resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST)            # output => ["今天天氣"]
    #resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST, splitLIST) # output => ["今天天氣", "後天氣象"]
    #resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"], filterLIST)      # output => ["今天天氣", "後天氣象"]
    
    resultDICT = runLoki(["中秋節快樂!"])
    print(resultDICT)