#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for pronouns

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

DEBUG_pronouns = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_pronouns.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_pronouns:
        print("[pronouns] {} ===> {}".format(inputSTR, utterance))

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
                resultDICT["response"] = "那在平常時，孩子總是會說一些自己想說的話，或重覆說出同樣的句子嗎？"
                resultDICT["q9"] = True
        else:
            # write your code here
            pass

    if utterance == "[不行]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那在平常時，孩子總是會說一些自己想說的話，或重覆說出同樣的句子嗎？"
            resultDICT["q9"] = False
        else:
            # write your code here
            pass

    if utterance == "[你][我]不分":
        if CHATBOT_MODE:
            resultDICT["response"] = "那在平常時，孩子總是會說一些自己想說的話，或重覆說出同樣的句子嗎？"
            resultDICT["q9"] = False
        else:
            # write your code here
            pass

    if utterance == "[好像][可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那在平常時，孩子總是會說一些自己想說的話，或重覆說出同樣的句子嗎？"
            resultDICT["q9"] = True
        else:
            # write your code here
            pass

    if utterance == "[好像]不[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那在平常時，孩子總是會說一些自己想說的話，或重覆說出同樣的句子嗎？"
            resultDICT["q9"] = False
        else:
            # write your code here
            pass

    if utterance == "[會]錯亂":
        if CHATBOT_MODE:
            resultDICT["response"] = "那在平常時，孩子總是會說一些自己想說的話，或重覆說出同樣的句子嗎？"
            resultDICT["q9"] = False
        else:
            # write your code here
            pass

    if utterance == "[有時][會]搞錯":
        if CHATBOT_MODE:
            resultDICT["response"] = "那在平常時，孩子總是會說一些自己想說的話，或重覆說出同樣的句子嗎？"
            resultDICT["q9"] = False
        else:
            # write your code here
            pass

    if utterance == "不太[會]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "很少": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            if "多" in inputSTR:
                resultDICT["response"] = "那在平常時，孩子總是會說一些自己想說的話，或重覆說出同樣的句子嗎？"
                resultDICT["q9"] = True
            elif "少" in inputSTR: #去reply裡面抓引導用問題
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "搞不[清楚]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那在平常時，孩子總是會說一些自己想說的話，或重覆說出同樣的句子嗎？"
            resultDICT["q9"] = False
        else:
            # write your code here
            pass

    if utterance == "沒辦法":
        if CHATBOT_MODE:
            resultDICT["response"] = "那在平常時，孩子總是會說一些自己想說的話，或重覆說出同樣的句子嗎？"
            resultDICT["q9"] = False
        else:
            # write your code here
            pass

    return resultDICT