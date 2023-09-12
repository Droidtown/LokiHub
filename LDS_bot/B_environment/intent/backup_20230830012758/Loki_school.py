#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for school

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

DEBUG_school = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
# if CHATBOT_MODE:
#     try:
#         responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_school.json"), encoding="utf-8"))
#     except Exception as e:
#         print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_school:
        print("[school] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[幼兒園]":
        if CHATBOT_MODE:
            if ("幼兒園" in inputSTR or "幼稚園" in inputSTR or "托嬰中心" in inputSTR) and "不" not in inputSTR and "沒" not in inputSTR:
                resultDICT["school"] = True
                resultDICT["response"] = "那麼孩子是否每日使用3C產品(包括：手機、平版、電腦、電視)總時間超過2小時呢?"
            else:
                resultDICT["school"] = False
                resultDICT["response"] = "那麼孩子是否每日使用3C產品(包括：手機、平版、電腦、電視)總時間超過2小時呢?"
        else:
            # write your code here
            pass

    return resultDICT