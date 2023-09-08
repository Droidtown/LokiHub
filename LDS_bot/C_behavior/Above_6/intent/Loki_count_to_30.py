#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for count_to_30

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

DEBUG_count_to_30 = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_count_to_30.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_count_to_30:
        print("[count_to_30] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[不行]":
        if CHATBOT_MODE:
            resultDICT["response"] = "對了，想問問您孩子現階段是可以用句子描述三到四張的連續圖卡了嗎？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "[數]不完":
        if CHATBOT_MODE:
            resultDICT["response"] = "對了，想問問您孩子現階段是可以用句子描述三到四張的連續圖卡了嗎？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "不[完整]":
        if CHATBOT_MODE:
            resultDICT["response"] = "對了，想問問您孩子現階段是可以用句子描述三到四張的連續圖卡了嗎？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "不太[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "對了，想問問您孩子現階段是可以用句子描述三到四張的連續圖卡了嗎？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "唸不完":
        if CHATBOT_MODE:
            resultDICT["response"] = "對了，想問問您孩子現階段是可以用句子描述三到四張的連續圖卡了嗎？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "有[些][可以]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "沒[辦法]":
        if CHATBOT_MODE:
            if "問題" in inputSTR:
                resultDICT["response"] = "對了，想問問您孩子現階段是可以用句子描述三到四張的連續圖卡了嗎？"
                resultDICT["q6"] = True
            elif "辦法" in inputSTR:
                resultDICT["response"] = "對了，想問問您孩子現階段是可以用句子描述三到四張的連續圖卡了嗎？"
                resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "跳來跳去":
        if CHATBOT_MODE:
            resultDICT["response"] = "對了，想問問您孩子現階段是可以用句子描述三到四張的連續圖卡了嗎？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "跳著唸":
        if CHATBOT_MODE:
            resultDICT["response"] = "對了，想問問您孩子現階段是可以用句子描述三到四張的連續圖卡了嗎？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "錯亂":
        if CHATBOT_MODE:
            resultDICT["response"] = "對了，想問問您孩子現階段是可以用句子描述三到四張的連續圖卡了嗎？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    return resultDICT