#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 4.0 Template For Python3

    [URL] https://nlu.droidtown.co/Loki_EN/BulkAPI/

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
                    "msg": "No matching intent."
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

PROJECT_NAME = "RSBot"
CWD_PATH = os.path.dirname(os.path.abspath(__file__))
MODULE_DICT = {
    "Account": import_from_path("{}_lib_Account".format(PROJECT_NAME), os.path.join(CWD_PATH, "Account.py")),
    "ChatbotMaker": import_from_path("{}_lib_ChatbotMaker".format(PROJECT_NAME), os.path.join(CWD_PATH, "ChatbotMaker.py")),
    "LLM": import_from_path("{}_lib_LLM".format(PROJECT_NAME), os.path.join(CWD_PATH, "LLM.py")),
}
"""
Account Variables
[Variable] BASE_PATH         => path of root
[Variable] LIB_PATH          => path of lib folder
[Variable] INTENT_PATH       => path of intent folder
[Variable] REPLY_PATH        => path of reply folder
[Variable] ACCOUNT_DICT      => account.info
[Variable] ARTICUT           => ArticutAPI (Usage: ARTICUT.parse()。 #ArticutAPI Required.)
[Variable] USER_DEFINED_FILE => path of UserDefined
[Variable] USER_DEFINED_DICT => UserDefined data
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

# Filter descrption
# INTENT_FILTER = []        => All intents (Default)
# INTENT_FILTER = [intentN] => Only use intent of INTENT_FILTER
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
        # Default: INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            url = "{}/Loki_EN/BulkAPI/".format(ACCOUNT_DICT["server"])
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
            # split by splitLIST
            splitPAT = re.compile("[{}]".format("".join(splitLIST)))
            inputLIST = []
            for c in contentLIST:
                tmpLIST = splitPAT.split(c)
                inputLIST.extend(tmpLIST)
            # remove empty
            while "" in inputLIST:
                inputLIST.remove("")
        else:
            # don't split
            inputLIST = contentLIST

        # batch with limitation of INPUT_LIMIT
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
                            responseSTR = "Do you mean「{}」?\n{}".format(scoreDICT["utterance"], responseSTR)
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
            # split by splitLIST
            splitPAT = re.compile("[{}]".format("".join(splitLIST)))
            for c in contentLIST:
                tmpLIST = splitPAT.split(c)
                inputLIST.extend(tmpLIST)
            # remove empty
            while "" in inputLIST:
                inputLIST.remove("")
        else:
            # don't split
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

    # Get_brand
    print("[TEST] Get_brand")
    inputLIST = ['__brandname__ brand','a __brandname__ one','an __brandname__ mac','probably __brandname__','I like __brandname__ products','__brandname__ or __brandname__']
    pprint(testLoki(inputLIST, ['Get_brand']))
    print("")

    # Want_args_0
    print("[TEST] Want_args_0")
    inputLIST = ['I would choose one']
    pprint(testLoki(inputLIST, ['Want_args_0']))
    print("")

    # Get_purpose
    print("[TEST] Get_purpose")
    inputLIST = ['for studying','for VR gaming','for managing emails','for accounting software','to run educational apps','for work documents and spreadsheets','For managing emails and office tasks','for studying and taking online classes','for presentations and business meetings']
    pprint(testLoki(inputLIST, ['Get_purpose']))
    print("")

    # Want_args_1
    print("[TEST] Want_args_1")
    inputLIST = ['I would choose something','I would choose a Mac book.','I would choose a new product','I would like to buy a laptop','I\'d purchase a silver laptop','I would choose a brand new one.','I would choose a top spec laptop','I would choose to buy a Chromebook','I would probably get a chromebook.','I would buy a MacBook in Rose Gold.','I would choose a laptop from a brand','I would need some kind of a MacBook.','I would choose a higher end gaming laptop.','I would chose a mac book as a replacement.','I would choose an efficient and modern laptop','I would choose something small and lightweight','I would like a silver or gold coloured laptop.','I would choose a more reliable high spec laptop','I would choose as a replacement another Macbook','I would want to purchase a Mac book from Apple.','I would also want it to be as light as possible.','I would choose to replace it with a tablet style laptop','I would want to purchase a Chromebook as a replacement.','I would ideally like a Macbook but they are too expensive.','I would choose either a black or grey finish to the laptop.','I would like to replace the laptop with an updated version of an Apple laptop','I would probably get a netbook as I would mainly be using it to surf the web.','I would choose a laptop from a brand that I had heard of and new to be reliable.']
    pprint(testLoki(inputLIST, ['Want_args_1']))
    print("")

    # Want_args_2
    print("[TEST] Want_args_2")
    inputLIST = ['I\'d get an msi laptop.','I would want a Dell laptop.','I\'d also prefer windows OS.','I would choose a Macbook Pro','I would want a Mac book pro.','I would like mircosoft office.','I would buy a mid price laptop.','I would choose a dell or an HP.','I would purchase a Macbook Pro.','I would want to buy a Mac book.','I would like to get a MacBook Pro.','I’d like to buy an Apple laptop.','I\'d probably get an ASUS or Lenovo.','I would like at least 8GB of memory.','I would ideally like an Apple laptop.','I would probably buy an apple laptop.','I\'d like a better and more HD screen.','I would chose a Razer Blade right now.','I would most likely buy and HP laptop.','I would probably pick an Apple laptop.','I would want an SSD of at least 500 GB.','I would want a Mac laptop as my replacement.','I would like my knew lap top to be an Apple one.','I would like to buy a MAC book pro this time round.','I would look at memory and speed and size of screen','I would want to buy an apple laptop as a replacement.','I would probably choose an Apple iMac as a replacement.','I\'ll probably move to a hybrid laptop as a replacement.','I would like to choose an apple laptop as a replacement.','I would probably choose a macbook as a replacement laptop.','I would choose a laptop made by Apple as like their design.','I\'d like to get HP or Acer, as I\'m kinda loyal to these brands.','I would be looking at something, small, compact and lightweight.','I would probably buy a Dell or HP, although if I had no budget I would buy a Mac']
    pprint(testLoki(inputLIST, ['Want_args_2']))
    print("")

    # Want_args_3
    print("[TEST] Want_args_3")
    inputLIST = ['I would buy a two in one laptop.','I would pick a macbook pro laptop.','I would choose an Apple MacBook Air.','I would buy a hp touch screen laptop.','I would choose a HP envy line up laptop.','I would prefer a Hewlett Packard laptop.','I would want a thin, lightweight laptop.','I\'d prefer an SSD and at least 8Gb of RAM','I\'d like to get a Microsoft Surface laptop.','I\'d also like it do have a light up keyboard.','I would like a lightweight touchscreen laptop.','I would look at buying a mac or a dell laptop.','I would prefer a laptop In the color space grey.','I would want it to run a Windows operating system.','I would choose a mid range laptop, probebly an Acer.','I would hope to buy another, more recently Macbook Pro model.','I would like to buy a light weight laptop, since I travel often.','I’d buy the Apple Mac laptop as i usually always purchase Apple products']
    pprint(testLoki(inputLIST, ['Want_args_3']))
    print("")

    # Want_args_4
    print("[TEST] Want_args_4")
    inputLIST = ['I\'d like to buy a refurbishment Mac Book Pro.','I would also want either a 1TB HDD or a 500GB SSD.','i would want a touch screen monitor and a mouse pad','I would purchase an Apple Macbook pro laptop as a replacement.','I would like it to have 16gb RAM and at least a 512gb SSD drive.','I would most likely consider a Dell laptop or an Asus laptop first.']
    pprint(testLoki(inputLIST, ['Want_args_4']))
    print("")

    # Want_args_5
    print("[TEST] Want_args_5")
    inputLIST = ['I would get a galaxy case and keyboard cover to match to protect my laptop.','I would personally choose an Apple Macbook Pro or possibly a Macbook Air as a replacement']
    pprint(testLoki(inputLIST, ['Want_args_5']))
    print("")


def COMM_TEST(inputSTR):
    if not inputSTR and "utterance_count" in ACCOUNT_DICT and ACCOUNT_DICT["utterance_count"]:
        intentSTR = list(ACCOUNT_DICT["utterance_count"])[0]
        inputSTR = list(ACCOUNT_DICT["utterance_count"][intentSTR])[0]
        inputSTR = re.sub("[\[\]]", "", inputSTR)

    print(setColor("========== COMM_TEST Start ==========", COLOR_DICT["PURPLE"]))

    # Input
    print("\nInput: {}".format(inputSTR))

    # Server
    print(setColor("\nTest Server", COLOR_DICT["CYAN"]))
    print("Server: {}".format(ACCOUNT_DICT["server"]))
    try:
        r = get(ACCOUNT_DICT["server"])
        if r.status_code == 200:
            print("[Status] {}".format(setColor("Connection test successful.", COLOR_DICT["GREEN"])))
        else:
            print("[Status] {}".format(setColor("Connection test failed.", COLOR_DICT["RED"])))
            print("[Hint] {}".format(setColor("Please check if the server field in account.info is a valid URL.", COLOR_DICT["YELLOW"])))
            return
    except:
        print("[Status] {}".format(setColor("Connection test failed.", COLOR_DICT["RED"])))
        print("[Hint] {}".format(setColor("Please check if the server field in account.info is a valid URL.", COLOR_DICT["YELLOW"])))
        return

    # Articut
    print(setColor("\nTest Articut", COLOR_DICT["CYAN"]))
    print("Username: {}".format(ACCOUNT_DICT["username"]))
    print("API Key: {}".format(ACCOUNT_DICT["api_key"]))
    atkResult = ARTICUT.parse(inputSTR, userDefinedDictFILE=USER_DEFINED_FILE)
    if atkResult["status"]:
        print("[Status] {}".format(setColor("Connection test successful.", COLOR_DICT["GREEN"])))
    else:
        print("[Status] {}".format(setColor("Connection test failed.", COLOR_DICT["RED"])))
        if atkResult["msg"] == "Insufficient quota.":
            print("[Hint] {}".format(setColor("Insufficient quota of Articut. Please purchase Articut from the official website.", COLOR_DICT["YELLOW"])))
        else:
            print("[Hint] {}".format(setColor("Please check if the username and api_key fields in account.info are correct.", COLOR_DICT["YELLOW"])))

    # Loki
    print(setColor("\nTest Loki", COLOR_DICT["CYAN"]))
    print("Username: {}".format(ACCOUNT_DICT["username"]))
    print("Loki Key: {}".format(ACCOUNT_DICT["loki_key"]))
    lokiResult = LokiResult([inputSTR], [])
    if lokiResult.getStatus():
        print("[Status] {}".format(setColor("Connection test successful.", COLOR_DICT["GREEN"])))
    else:
        print("[Status] {}".format(setColor("Connection test failed.", COLOR_DICT["RED"])))
        if lokiResult.getMessage() == "Insufficient quota.":
            print("[Hint] {}".format(setColor("Insufficient quota of Loki. Please purchase Loki from the official website.", COLOR_DICT["YELLOW"])))
        else:
            print("[Hint] {}".format(setColor("Please check if the username and api_key fields in account.info are correct.", COLOR_DICT["YELLOW"])))
            print("[Hint] {}".format(setColor("Please check if the Loki model has been deployed.", COLOR_DICT["YELLOW"])))

    print(setColor("\n========== COMM_TEST End ==========", COLOR_DICT["PURPLE"]))


if __name__ == "__main__":
    from pprint import pprint

    # Test all intents
    #testIntent()

    # Test sentence
    contentSTR = ""
    if not contentSTR and "utterance_count" in ACCOUNT_DICT and ACCOUNT_DICT["utterance_count"]:
        intentSTR = list(ACCOUNT_DICT["utterance_count"])[0]
        contentSTR = list(ACCOUNT_DICT["utterance_count"][intentSTR])[0]
        contentSTR = re.sub("[\[\]]", "", contentSTR)

    filterLIST = []
    splitLIST = ["!", ",", ".", "\n", "\u3000", ";"]
    # set references
    refDICT = { # value is a list
        #"key": []
    }

    # Run Loki
    resultDICT = execLoki(contentSTR, filterLIST=filterLIST, splitLIST=splitLIST, refDICT=refDICT)
    pprint(resultDICT)