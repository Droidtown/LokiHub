#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for can_not_follow_directions

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

DEBUG_can_not_follow_directions = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_can_not_follow_directions.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_can_not_follow_directions:
        print("[can_not_follow_directions] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[不常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "如果您與孩子一起看書故事，孩子已經可以理解圖卡故事中的因果關係了嗎？例如：小孩滑倒是因為踩到地上的香蕉皮？"
                resultDICT["q3"] = True
            elif "常常" in inputSTR:
                resultDICT["response"] = "如果您與孩子一起看書故事，孩子已經可以理解圖卡故事中的因果關係了嗎？例如：小孩滑倒是因為踩到地上的香蕉皮？"
                resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "[都][可以]做到":
        if CHATBOT_MODE:
            resultDICT["response"] = "如果您與孩子一起看書故事，孩子已經可以理解圖卡故事中的因果關係了嗎？例如：小孩滑倒是因為踩到地上的香蕉皮？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[都]不知道要做什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = "如果您與孩子一起看書故事，孩子已經可以理解圖卡故事中的因果關係了嗎？例如：小孩滑倒是因為踩到地上的香蕉皮？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "不太[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "如果您與孩子一起看書故事，孩子已經可以理解圖卡故事中的因果關係了嗎？例如：小孩滑倒是因為踩到地上的香蕉皮？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "好[像都]聽不懂":
        if CHATBOT_MODE:
            resultDICT["response"] = "如果您與孩子一起看書故事，孩子已經可以理解圖卡故事中的因果關係了嗎？例如：小孩滑倒是因為踩到地上的香蕉皮？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "好像是":
        if CHATBOT_MODE:
            resultDICT["response"] = "如果您與孩子一起看書故事，孩子已經可以理解圖卡故事中的因果關係了嗎？例如：小孩滑倒是因為踩到地上的香蕉皮？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "沒[錯]":
        if CHATBOT_MODE:
            resultDICT["response"] = "如果您與孩子一起看書故事，孩子已經可以理解圖卡故事中的因果關係了嗎？例如：小孩滑倒是因為踩到地上的香蕉皮？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "沒辦法":
        if CHATBOT_MODE:
            resultDICT["response"] = "如果您與孩子一起看書故事，孩子已經可以理解圖卡故事中的因果關係了嗎？例如：小孩滑倒是因為踩到地上的香蕉皮？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "看[心情]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT