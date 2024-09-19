#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Grade_Inquiry

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict,
        pattern       str

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os

DEBUG = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_Grade_Inquiry.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[Grade_Inquiry] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "[他][數學課][第一章]分數是多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["Class"].append(args[1])
            resultDICT["Chapter"].append(args[2])
            pass

    if utterance == "[他][數學課]的[第一章]拿了多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["Class"].append(args[1])
            resultDICT["Chapter"].append(args[2])
            pass

    if utterance == "[他][數學課]的[第一章]考了多少分？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["Class"].append(args[1])
            resultDICT["Chapter"].append(args[2])
            pass

    if utterance == "[我]想知道[他][英文課]的[第一章]考試分數":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["Class"].append(args[2])
            resultDICT["Chapter"].append(args[3])
            pass

    if utterance == "[英文課][第十章]考多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["Class"].append(args[0])
            resultDICT["Chapter"].append(args[1])
            pass

    if utterance == "[英文課][第二章]分數多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["Class"].append(args[0])
            resultDICT["Chapter"].append(args[1])
            pass

    if utterance == "告訴[我][他][數學課][第一章]考多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["Class"].append(args[2])
            resultDICT["Chapter"].append(args[3])
            pass

    if utterance == "請告訴[我][他]在[數學課][第一章]的成績":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["Class"].append(args[2])
            resultDICT["Chapter"].append(args[3])            
            pass

    if utterance == "告訴[我][他][英文課][第二章]的分數":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["Class"].append(args[2])
            resultDICT["Chapter"].append(args[3])
            pass

    if utterance == "[數學課][第一章]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["Class"].append(args[0])
            resultDICT["Chapter"].append(args[1])
        pass
            
    return resultDICT