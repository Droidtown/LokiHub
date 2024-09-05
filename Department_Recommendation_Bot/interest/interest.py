#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import aiohttp
import asyncio
from copy import deepcopy
from glob import glob
from importlib import import_module
from pathlib import Path
import json
import math
import os
import re

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
CWD_PATH = str(Path.cwd())

lokiIntentDICT = {}
for modulePath in glob("{}/intent/Loki_*.py".format(BASE_PATH)):
    moduleNameSTR = Path(modulePath).stem[5:]
    modulePathSTR = modulePath.replace(CWD_PATH, "").replace(".py", "").replace("/", ".").replace("\\", ".")[1:]
    globals()[moduleNameSTR] = import_module(modulePathSTR)
    lokiIntentDICT[moduleNameSTR] = globals()[moduleNameSTR]

LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
try:
    accountInfo = json.load(open(os.path.join(BASE_PATH, "account.info"), encoding="utf-8"))
    USERNAME = accountInfo["username"]
    LOKI_KEY = accountInfo["loki_key"]
except Exception as e:
    print(f"[ERROR] AccountInfo => {str(e)}")
    USERNAME = ""
    LOKI_KEY = ""

INTENT_FILTER = []
INPUT_LIMIT = 20

class LokiResult():
    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        self.filterLIST = filterLIST if filterLIST else INTENT_FILTER
        self.inputLIST = inputLIST

    async def fetch(self):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(LOKI_URL, json={
                    "username": USERNAME,
                    "input_list": self.inputLIST,
                    "loki_key": LOKI_KEY,
                    "filter_list": self.filterLIST
                }) as response:
                    if response.status == 200:
                        result = await response.json()
                        self.status = result["status"]
                        self.message = result["msg"]
                        if result["status"]:
                            self.version = result["version"]
                            if "word_count_balance" in result:
                                self.balance = result["word_count_balance"]
                            self.lokiResultLIST = result["result_list"]
                    else:
                        self.message = f"{response.status} Connection failed."
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
        return self.lokiResultLIST[index]["status"] if index < len(self.lokiResultLIST) else False

    def getLokiMessage(self, index):
        return self.lokiResultLIST[index]["msg"] if index < len(self.lokiResultLIST) else ""

    def getLokiLen(self, index):
        return len(self.lokiResultLIST[index]["results"]) if index < len(self.lokiResultLIST) and self.lokiResultLIST[index]["status"] else 0

    def getLokiResult(self, index, resultIndex):
        return self.lokiResultLIST[index]["results"][resultIndex] if resultIndex < self.getLokiLen(index) else None

    def getIntent(self, index, resultIndex):
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        return lokiResultDICT["intent"] if lokiResultDICT else ""

    def getPattern(self, index, resultIndex):
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        return lokiResultDICT["pattern"] if lokiResultDICT else ""

    def getUtterance(self, index, resultIndex):
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        return lokiResultDICT["utterance"] if lokiResultDICT else ""

    def getArgs(self, index, resultIndex):
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        return lokiResultDICT["argument"] if lokiResultDICT else []


async def runLoki(inputLIST, filterLIST=[], refDICT={}):
    resultDICT = deepcopy(refDICT)
    lokiRst = LokiResult(inputLIST, filterLIST)
    await lokiRst.fetch()
    
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            lokiResultDICT = {k: [] for k in refDICT}
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                intent = lokiRst.getIntent(index, resultIndex)
                if intent in lokiIntentDICT:
                    lokiResultDICT = await lokiIntentDICT[intent].getResult(
                        key, 
                        lokiRst.getUtterance(index, resultIndex), 
                        lokiRst.getArgs(index, resultIndex),
                        lokiResultDICT, 
                        refDICT, 
                        pattern=lokiRst.getPattern(index, resultIndex)
                    )
    
            if lokiResultDICT is not None:
                for k in lokiResultDICT:
                    if k not in resultDICT:
                        resultDICT[k] = []
                    if isinstance(resultDICT[k], list):
                        resultDICT[k].extend(lokiResultDICT[k])
                    else:
                        resultDICT[k] = lokiResultDICT[k]
    else:
        resultDICT["msg"] = lokiRst.getMessage()
    
    return resultDICT




async def execLoki(content, filterLIST=[], splitLIST=[], refDICT={}):
    resultDICT = deepcopy(refDICT) or {}
    contentLIST = [content] if isinstance(content, str) else content

    if splitLIST:
        splitPAT = re.compile(f"[{''.join(splitLIST)}]")
        inputLIST = []
        for c in contentLIST:
            inputLIST.extend(splitPAT.split(c))
        inputLIST = [i for i in inputLIST if i]
    else:
        inputLIST = contentLIST

    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = await runLoki(inputLIST[i * INPUT_LIMIT:(i + 1) * INPUT_LIMIT], filterLIST=filterLIST, refDICT=resultDICT)
        if "msg" in resultDICT:
            break

    return resultDICT


async def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = await runLoki(inputLIST[i * INPUT_LIMIT:(i + 1) * INPUT_LIMIT], filterLIST)
    if "msg" in resultDICT:
        print(resultDICT["msg"])


async def testIntent():
    inputLIST = [
        '我很喜歡物理', '他很喜歡當導師', '我享受創作文字和故事', '我對說服他人很感興趣',
        '我熱衷於探索人類行為', '我熱衷於閱讀科幻小說', '我一直都很喜歡處理問題', '我對思維模式的研究感興趣',
        '我對醫學和健康科學感興趣', '我熱衷於學習新的藝術技巧', '我一直都對處理問題很有興趣',
        '我喜歡學習如何製作數位內容', '我對數據分析有強烈的好奇心', '我對機器學習的應用感到興奮',
        '我喜歡參加戶外活動，探索自然', '我對哲學和倫理學有濃厚的興趣', '我對心理學的理論有濃厚的興趣',
        '我從高中時起就很喜歡處理問題', '我對創新思維和解決方案很感興趣', '我對文化交流和全球化現象感興趣'
    ]
    await testLoki(inputLIST, [])
