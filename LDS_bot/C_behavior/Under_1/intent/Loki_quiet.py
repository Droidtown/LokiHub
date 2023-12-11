#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for quiet

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
import json
import os

DEBUG_quiet = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_quiet.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_quiet:
        print("[quiet] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一般][都]很安靜":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那如果孩子正在做某個動作，突然聽到大人說「不可以」時，孩子會不會停下來或短暫停止當下的動作呢？"
            resultDICT["q11"] = False
        else:
            # write your code here
            pass

    if utterance == "[不太]有聲音":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那如果孩子正在做某個動作，突然聽到大人說「不可以」時，孩子會不會停下來或短暫停止當下的動作呢？"
            resultDICT["q11"] = False
        else:
            # write your code here
            pass

    if utterance == "[他][都]很吵":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那如果孩子正在做某個動作，突然聽到大人說「不可以」時，孩子會不會停下來或短暫停止當下的動作呢？"
            resultDICT["q11"] = True
        else:
            # write your code here
            pass

    return resultDICT