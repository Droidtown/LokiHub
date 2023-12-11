#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for weight

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict

    Output:
        resultDICT    dict
"""

from random import sample
from ArticutAPI import Articut
import json
import os
import re

account_info = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "account.info"), encoding="utf-8"))
articut = Articut(account_info["username"], account_info["api_key"])
DEBUG_weight = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
# if CHATBOT_MODE:
#     try:
#         responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_weight.json"), encoding="utf-8"))
#     except Exception as e:
#         print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_weight:
        print("[weight] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[3000公克]":
        if CHATBOT_MODE:
            split_measure = re.search("公?[克斤]|[Kk]?[Gg]", args[0])
            num = articut.parse(args[0], level="lv3")["number"][args[0]]
            if split_measure in ["公斤", "斤", "KG", "Kg", "kg", "kG"]:
                weight = num*1000
            else:
                weight = num
            if weight < 2500:
                resultDICT["weight"] = False
                resultDICT["response"] = "那孩子出生後有沒有被診斷出什麼先天性或後天性疾病呢？"
            else:
                resultDICT["weight"] = True
                resultDICT["response"] = "那孩子出生後有沒有被診斷出什麼先天性或後天性疾病呢？"
        else:
            # write your code here
            pass

    if utterance == "3000":
        if CHATBOT_MODE:
            num = articut.parse(args[0], level="lv3")["number"][args[0]]
            if len(re.search(r"\d\.\d+", args[0])) == 0:
                if num < 2500:
                    resultDICT["weight"] = False
                    resultDICT["response"] = "那孩子出生後有沒有被診斷出什麼先天性或後天性疾病呢？"
                else:
                    resultDICT["weight"] = True
                    resultDICT["response"] = "那孩子出生後有沒有被診斷出什麼先天性或後天性疾病呢？"
            else:
                if num*1000 < 2500:
                    resultDICT["weight"] = False
                    resultDICT["response"] = "那孩子出生後有沒有被診斷出什麼先天性或後天性疾病呢？"
                else:
                    resultDICT["weight"] = True
                    resultDICT["response"] = "那孩子出生後有沒有被診斷出什麼先天性或後天性疾病呢？"
        else:
            # write your code here
            pass

    return resultDICT
