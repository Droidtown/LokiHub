#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for describe_story_or_things

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

DEBUG_describe_story_or_things = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_describe_story_or_things.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_describe_story_or_things:
        print("[describe_story_or_things] {} ===> {}".format(inputSTR, utterance))

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
            if "不常" in inputSTR: #去reply裡面抓引導用問題
                resultDICT["response"] = getResponse(utterance, args)
            elif "常常" in inputSTR:
                resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問，您的孩子說話時，每十句會至少有兩句出現口吃、不流暢的情形嗎？"
                resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "[不行]":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問，您的孩子說話時，每十句會至少有兩句出現口吃、不流暢的情形嗎？"
            resultDICT["q4"] = False
        else:
            # write your code here
            pass

    if utterance == "[會]但不愛講":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問，您的孩子說話時，每十句會至少有兩句出現口吃、不流暢的情形嗎？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]跳來跳去":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問，您的孩子說話時，每十句會至少有兩句出現口吃、不流暢的情形嗎？"
            resultDICT["q4"] = False
        else:
            # write your code here
            pass

    if utterance == "[都]說很短的":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問，您的孩子說話時，每十句會至少有兩句出現口吃、不流暢的情形嗎？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "[都]講很短的":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問，您的孩子說話時，每十句會至少有兩句出現口吃、不流暢的情形嗎？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "不太行": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "很少": 
        if CHATBOT_MODE:
            if "多" in inputSTR:
                resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問，您的孩子說話時，每十句會至少有兩句出現口吃、不流暢的情形嗎？"
                resultDICT["q4"] = True
            elif "少" in inputSTR: #去reply裡面抓引導用問題
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有說但聽不懂":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問，您的孩子說話時，每十句會至少有兩句出現口吃、不流暢的情形嗎？"
            resultDICT["q4"] = False
        else:
            # write your code here
            pass

    if utterance == "沒聽過":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問，您的孩子說話時，每十句會至少有兩句出現口吃、不流暢的情形嗎？"
            resultDICT["q4"] = False
        else:
            # write your code here
            pass

    if utterance == "沒辦法":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問，您的孩子說話時，每十句會至少有兩句出現口吃、不流暢的情形嗎？"
            resultDICT["q4"] = False
        else:
            # write your code here
            pass

    if utterance == "看[心情]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "要看說什麼": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "講不[完整]":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問，您的孩子說話時，每十句會至少有兩句出現口吃、不流暢的情形嗎？"
            resultDICT["q4"] = False
        else:
            # write your code here
            pass

    return resultDICT