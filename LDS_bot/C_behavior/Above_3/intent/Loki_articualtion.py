#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for articualtion

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

DEBUG_articualtion = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_articualtion.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_articualtion:
        print("[articualtion] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[好像]沒有":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那請問一下，您的孩子現在可以理解大和小或多和少的概念了嗎？"
            resultDICT["q2"] = True
        else:
            # write your code here
            pass

    if utterance == "[對]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那請問一下，您的孩子現在可以理解大和小或多和少的概念了嗎？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "[很常][這樣]":
        if CHATBOT_MODE:
            if "不" in inputSTR:
                resultDICT["response"] = "了解...那請問一下，您的孩子現在可以理解大和小或多和少的概念了嗎？"
                resultDICT["q2"] = True
            elif "很" in inputSTR:
                resultDICT["response"] = "了解...那請問一下，您的孩子現在可以理解大和小或多和少的概念了嗎？"
                resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "[有時候]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那請問一下，您的孩子現在可以理解大和小或多和少的概念了嗎？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "不太[會]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "是":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那請問一下，您的孩子現在可以理解大和小或多和少的概念了嗎？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "沒[錯]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那請問一下，您的孩子現在可以理解大和小或多和少的概念了嗎？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "發音不[標準]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那請問一下，您的孩子現在可以理解大和小或多和少的概念了嗎？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "說得不[清楚]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那請問一下，您的孩子現在可以理解大和小或多和少的概念了嗎？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    return resultDICT