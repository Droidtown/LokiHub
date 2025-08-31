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
from glob import glob
from importlib.util import module_from_spec
from importlib.util import spec_from_file_location
from pathlib import Path
from requests import codes
from requests import get
from requests import post
import math
import os
import re

def import_from_path(module_name, file_path):
    spec = spec_from_file_location(module_name, file_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

PROJECT_NAME = "Money_add"
CWD_PATH = os.path.dirname(os.path.abspath(__file__))
MODULE_DICT = {
    "Account": import_from_path("{}_lib_Account".format(PROJECT_NAME), os.path.join(CWD_PATH, "Account.py")),
    "ChatbotMaker": import_from_path("{}_lib_ChatbotMaker".format(PROJECT_NAME), os.path.join(CWD_PATH, "ChatbotMaker.py")),
    "LLM": import_from_path("{}_lib_LLM".format(PROJECT_NAME), os.path.join(CWD_PATH, "LLM.py")),
}
"""
Account 變數清單
[變數] BASE_PATH         => 根目錄位置
[變數] LIB_PATH          => lib 目錄位置
[變數] INTENT_PATH       => intent 目錄位置
[變數] REPLY_PATH        => reply 目錄位置
[變數] ACCOUNT_DICT      => account.info 內容
[變數] ARTICUT           => ArticutAPI (用法：ARTICUT.parse()。 #需安裝 ArticutAPI.)
[變數] USER_DEFINED_FILE => 使用者自定詞典的檔案路徑
[變數] USER_DEFINED_DICT => 使用者自定詞典內容
"""
INTENT_PATH = MODULE_DICT["Account"].INTENT_PATH
ACCOUNT_DICT = MODULE_DICT["Account"].ACCOUNT_DICT
ARTICUT = MODULE_DICT["Account"].ARTICUT
USER_DEFINED_FILE = MODULE_DICT["Account"].USER_DEFINED_FILE
USER_DEFINED_DICT = MODULE_DICT["Account"].USER_DEFINED_DICT
COLOR_DICT = MODULE_DICT["ChatbotMaker"].COLOR_DICT
setColor = MODULE_DICT["ChatbotMaker"].setColor
callLLM = MODULE_DICT["LLM"].callLLM
getCosineSimilarityUtterance = MODULE_DICT["LLM"].getCosineSimilarityUtterance

lokiIntentDICT = {}
for modulePath in glob("{}/Loki_*.py".format(INTENT_PATH)):
    moduleNameSTR = Path(modulePath).stem[5:]
    lokiIntentDICT[moduleNameSTR] = import_from_path("{}_intent_{}".format(PROJECT_NAME, moduleNameSTR), modulePath)

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
            url = "{}/Loki/BulkAPI/".format(ACCOUNT_DICT["server"])
            result = post(url, json={
                "username": ACCOUNT_DICT["username"],
                "input_list": inputLIST,
                "loki_key": ACCOUNT_DICT["loki_key"],
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

def runLoki(inputLIST, filterLIST=[], refDICT={}, toolkitDICT={}):
    resultDICT = deepcopy(refDICT)
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            lokiResultDICT = {k: [] for k in refDICT}
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                if lokiRst.getIntent(index, resultIndex) in lokiIntentDICT:
                    lokiResultDICT = lokiIntentDICT[lokiRst.getIntent(index, resultIndex)].getResult(
                        key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex),
                        lokiResultDICT, refDICT, pattern=lokiRst.getPattern(index, resultIndex), toolkitDICT=toolkitDICT)

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

def execLoki(content, filterLIST=[], splitLIST=[], refDICT={}, toolkitDICT={}):
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
            resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST=filterLIST, refDICT=resultDICT, toolkitDICT=toolkitDICT)
            if "msg" in resultDICT:
                break

    if ACCOUNT_DICT["chatbot_mode"]:
        if "response" not in resultDICT:
            resultDICT["response"] = []
        if "source" not in resultDICT:
            resultDICT["source"] = []

        for i, content in enumerate(contentLIST):
            if i < len(resultDICT["response"]) and resultDICT["response"][i]:
                responseSTR = resultDICT["response"][i]
                sourceSTR = "reply"
            else:
                responseSTR = ""
                if ACCOUNT_DICT["utterance_count"]:
                    scoreDICT = getCosineSimilarityUtterance(content, ACCOUNT_DICT["utterance_count"])
                    if scoreDICT["utterance"] and scoreDICT["score"] >= ACCOUNT_DICT["utterance_threshold"]:
                        responseSTR = lokiIntentDICT[scoreDICT["intent"]].getReply(scoreDICT["utterance"], [])
                        if responseSTR:
                            responseSTR = "您的意思是指「{}」嗎？\n{}".format(scoreDICT["utterance"], responseSTR)
                            sourceSTR = "SIM_reply"

                if not responseSTR:
                    responseSTR, sourceSTR = callLLM(content)

            if i < len(resultDICT["response"]):
                resultDICT["response"][i] = responseSTR
            else:
                resultDICT["response"].append(responseSTR)

            if i < len(resultDICT["source"]):
                resultDICT["source"][i] = sourceSTR
            else:
                resultDICT["source"].append(sourceSTR)

    return resultDICT

def cosSimilarLoki(content, splitLIST=[], featureLIST=[]):
    resultDICT = {}

    contentLIST = []
    if type(content) == str:
        contentLIST = [content]
    if type(content) == list:
        contentLIST = content

    if not featureLIST:
        featureLIST = ACCOUNT_DICT["utterance_feature"]

    if contentLIST:
        inputLIST = []
        if splitLIST:
            # 依 splitLIST 做分句切割
            splitPAT = re.compile("[{}]".format("".join(splitLIST)))
            for c in contentLIST:
                tmpLIST = splitPAT.split(c)
                inputLIST.extend(tmpLIST)
            # 去除空字串
            while "" in inputLIST:
                inputLIST.remove("")
        else:
            # 不做分句切割處理
            inputLIST = contentLIST

        for inputSTR in inputLIST:
            inputSTR = inputSTR.strip()
            scoreDICT = getCosineSimilarityUtterance(inputSTR, ACCOUNT_DICT["utterance_count"])
            if scoreDICT["intent"] and scoreDICT["score"] >= ACCOUNT_DICT["utterance_threshold"]:
                if scoreDICT["intent"] not in resultDICT:
                    resultDICT[scoreDICT["intent"]] = {}
                resultDICT[scoreDICT["intent"]][inputSTR] = {
                    "utterance": scoreDICT["utterance"],
                    "score": scoreDICT["score"]
                }

    return resultDICT

def testLoki(inputLIST, filterLIST):
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

    return resultDICT

def testIntent():
    from pprint import pprint

    # money
    print("[TEST] money")
    inputLIST = ['500元']
    testLoki(inputLIST, ['money'])
    print("")

    # amount
    print("[TEST] amount")
    inputLIST = ['三杯星巴克','三杯好喝的咖啡','三杯超好喝的咖啡']
    testLoki(inputLIST, ['amount'])
    print("")

    # content
    print("[TEST] content")
    inputLIST = ['領了5000元','三杯星巴克','買麥當勞套餐','投資獲利1500元','飲料和咖啡150元','高鐵去台中800元','麥當勞套餐150元']
    testLoki(inputLIST, ['content'])
    print("")

    # check
    print("[TEST] check")
    inputLIST = ['?????','我好餓','我剛剛領了5000元','我買花花了我300元','我昨天買了1杯紅茶','剛剛花了200元買了一塊蛋糕','中秋節買了100顆月餅共花了900元']
    testLoki(inputLIST, ['check'])
    print("")

    # time
    print("[TEST] time")
    inputLIST = ['7月20日']
    testLoki(inputLIST, ['time'])
    print("")


def COMM_TEST(inputSTR):
    if not inputSTR and "utterance_count" in ACCOUNT_DICT and ACCOUNT_DICT["utterance_count"]:
        intentSTR = list(ACCOUNT_DICT["utterance_count"])[0]
        inputSTR = list(ACCOUNT_DICT["utterance_count"][intentSTR])[0]
        inputSTR = re.sub("[\[\]]", "", inputSTR)

    print(setColor("========== COMM_TEST 開始 ==========", COLOR_DICT["PURPLE"]))

    # Input
    print("\nInput: {}".format(inputSTR))

    # Server
    print(setColor("\n測試伺服器", COLOR_DICT["CYAN"]))
    print("Server: {}".format(ACCOUNT_DICT["server"]))
    try:
        r = get(ACCOUNT_DICT["server"])
        if r.status_code == 200:
            print("[狀態] {}".format(setColor("連線測試成功", COLOR_DICT["GREEN"])))
        else:
            print("[狀態] {}".format(setColor("連線測試失敗", COLOR_DICT["RED"])))
            print("[提示] {}".format(setColor("請檢查 account.info 中 server 欄位是否為有效的網址", COLOR_DICT["YELLOW"])))
            return
    except:
        print("[狀態] {}".format(setColor("連線測試失敗", COLOR_DICT["RED"])))
        print("[提示] {}".format(setColor("請檢查 account.info 中 server 欄位是否為有效的網址", COLOR_DICT["YELLOW"])))
        return

    # Articut
    print(setColor("\n測試 Articut", COLOR_DICT["CYAN"]))
    print("Username: {}".format(ACCOUNT_DICT["username"]))
    print("API Key: {}".format(ACCOUNT_DICT["api_key"]))
    atkResult = ARTICUT.parse(inputSTR, userDefinedDictFILE=USER_DEFINED_FILE)
    if atkResult["status"]:
        print("[狀態] {}".format(setColor("連線測試成功", COLOR_DICT["GREEN"])))
    else:
        print("[狀態] {}".format(setColor("連線測試失敗", COLOR_DICT["RED"])))
        if atkResult["msg"] == "Insufficient quota.":
            print("[提示] {}".format(setColor("Articut 額度不足，請至官網購買 Articut", COLOR_DICT["YELLOW"])))
        else:
            print("[提示] {}".format(setColor("請檢查 account.info 中 username 及 api_key 欄位是否正確", COLOR_DICT["YELLOW"])))

    # Loki
    print(setColor("\n測試 Loki", COLOR_DICT["CYAN"]))
    print("Username: {}".format(ACCOUNT_DICT["username"]))
    print("Loki Key: {}".format(ACCOUNT_DICT["loki_key"]))
    lokiResult = LokiResult([inputSTR], [])
    if lokiResult.getStatus():
        print("[狀態] {}".format(setColor("連線測試成功", COLOR_DICT["GREEN"])))
    else:
        print("[狀態] {}".format(setColor("連線測試失敗", COLOR_DICT["RED"])))
        if lokiResult.getMessage() == "Insufficient quota.":
            print("[提示] {}".format(setColor("Loki 額度不足，請至官網購買 Loki", COLOR_DICT["YELLOW"])))
        else:
            print("[提示] {}".format(setColor("請檢查 account.info 中 username 及 loki_key 欄位是否正確", COLOR_DICT["YELLOW"])))
            print("[提示] {}".format(setColor("請檢查 Loki 模型是否已部署", COLOR_DICT["YELLOW"])))

    print(setColor("\n========== COMM_TEST 結束 ==========", COLOR_DICT["PURPLE"]))


if __name__ == "__main__":
    from pprint import pprint

    # 測試所有意圖
    #testIntent()

    # 測試句子
    contentSTR = ""
    if not contentSTR and "utterance_count" in ACCOUNT_DICT and ACCOUNT_DICT["utterance_count"]:
        intentSTR = list(ACCOUNT_DICT["utterance_count"])[0]
        contentSTR = list(ACCOUNT_DICT["utterance_count"][intentSTR])[0]
        contentSTR = re.sub("[\[\]]", "", contentSTR)

    filterLIST = []
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    # 設定參考資料
    refDICT = { # value 必須為 list
        #"key": []
    }

    # 執行 Loki
    resultDICT = execLoki(contentSTR, filterLIST=filterLIST, splitLIST=splitLIST, refDICT=refDICT)
    pprint(resultDICT)