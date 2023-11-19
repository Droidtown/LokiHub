#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for 7_digits

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

DEBUG_7_digits = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_7_digits.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_7_digits:
        print("[7_digits] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[偶爾]":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那另外想了解的是...孩子說話時的發音不清楚，只有同住的家人才聽得懂嗎？"
            resultDICT["q1"] = False
        else:
            # write your code here
            pass

    if utterance == "[數字]混淆":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那另外想了解的是...孩子說話時的發音不清楚，只有同住的家人才聽得懂嗎？"
            resultDICT["q1"] = False
        else:
            # write your code here
            pass

    if utterance == "不太行": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "唸錯":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那另外想了解的是...孩子說話時的發音不清楚，只有同住的家人才聽得懂嗎？"
            resultDICT["q1"] = False
        else:
            # write your code here
            pass

    if utterance == "跳著唸":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那另外想了解的是...孩子說話時的發音不清楚，只有同住的家人才聽得懂嗎？"
            resultDICT["q1"] = False
        else:
            # write your code here
            pass

    return resultDICT