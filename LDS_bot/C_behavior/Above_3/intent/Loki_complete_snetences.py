#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for complete_snetences

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

DEBUG_complete_snetences = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_complete_snetences.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_complete_snetences:
        print("[complete_snetences] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "那麼在遊戲活動或日常生活中，孩子可以理解物品功能的描述(例如：「用來喝水的是什麼」)並可以正確指出該物品嗎？"
                resultDICT["q4"] = False
            else:
                resultDICT["response"] = "那麼在遊戲活動或日常生活中，孩子可以理解物品功能的描述(例如：「用來喝水的是什麼」)並可以正確指出該物品嗎？"
                resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "[很常][這樣]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "那麼在遊戲活動或日常生活中，孩子可以理解物品功能的描述(例如：「用來喝水的是什麼」)並可以正確指出該物品嗎？"
                resultDICT["q4"] = False
            else:
                resultDICT["response"] = "那麼在遊戲活動或日常生活中，孩子可以理解物品功能的描述(例如：「用來喝水的是什麼」)並可以正確指出該物品嗎？"
                resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "[都]說很短的":
        if CHATBOT_MODE:
            resultDICT["response"] = "那麼在遊戲活動或日常生活中，孩子可以理解物品功能的描述(例如：「用來喝水的是什麼」)並可以正確指出該物品嗎？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "[都]講很短的":
        if CHATBOT_MODE:
            resultDICT["response"] = "那麼在遊戲活動或日常生活中，孩子可以理解物品功能的描述(例如：「用來喝水的是什麼」)並可以正確指出該物品嗎？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "不太[會]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "不太行": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有說但聽不懂":
        if CHATBOT_MODE:
            resultDICT["response"] = "那麼在遊戲活動或日常生活中，孩子可以理解物品功能的描述(例如：「用來喝水的是什麼」)並可以正確指出該物品嗎？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "算有哦":
        if CHATBOT_MODE:
            resultDICT["response"] = "那麼在遊戲活動或日常生活中，孩子可以理解物品功能的描述(例如：「用來喝水的是什麼」)並可以正確指出該物品嗎？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "講不[完整]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那麼在遊戲活動或日常生活中，孩子可以理解物品功能的描述(例如：「用來喝水的是什麼」)並可以正確指出該物品嗎？"
            resultDICT["q4"] = False
        else:
            # write your code here
            pass

    return resultDICT