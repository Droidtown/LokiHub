#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Exchange

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

DEBUG_Exchange = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_Exchange.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Exchange:
        print("[Exchange] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[100元][美金][可以]兌換[台幣]多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = args[1]
            resultDICT["target"] = args[3]
            resultDICT["amount"] = args[0]

    if utterance == "[100元][美金][可以]兌換多少[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = args[1]
            resultDICT["target"] = args[3]
            resultDICT["amount"] = args[0]

    if utterance == "[100元][美金]要[台幣]多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = args[2]
            resultDICT["target"] = args[1]
            resultDICT["amount"] = args[0]

    if utterance == "[100元][美金]要多少[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = args[2]
            resultDICT["target"] = args[1]
            resultDICT["amount"] = args[0]

    if utterance == "[100台幣]換[美金]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = [x for x in userDefinedDICT if x in args[0]][0]
            resultDICT["target"] = args[1]
            resultDICT["amount"] = args[0]

    if utterance == "[100美金][能]換多少[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = [x for x in userDefinedDICT if x in args[0]][0]
            resultDICT["target"] = args[2]
            resultDICT["amount"] = args[0]

    if utterance == "[100美金]要[台幣]多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = args[1]
            resultDICT["target"] = [x for x in userDefinedDICT if x in args[0]][0]
            resultDICT["amount"] = args[0]

    if utterance == "[100美金]要多少[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = args[1]
            resultDICT["target"] = [x for x in userDefinedDICT if x in args[0]][0]
            resultDICT["amount"] = args[0]

    if utterance == "[今天][美金]兌換[台幣]是多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = args[1]
            resultDICT["target"] = args[2]
            resultDICT["amount"] = None

    if utterance == "[我]想要[100元][美金]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = None
            resultDICT["target"] = args[2]
            resultDICT["amount"] = args[1]

    if utterance == "[我]想要[美金][100元]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = None
            resultDICT["target"] = args[1]
            resultDICT["amount"] = args[2]

    if utterance == "[我]想買[100元][美金]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = None
            resultDICT["target"] = args[2]
            resultDICT["amount"] = args[1]

    if utterance == "[我]想買[美金][100元]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = None
            resultDICT["target"] = args[1]
            resultDICT["amount"] = args[2]

    if utterance == "[美金][100]要[台幣]多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = args[2]
            resultDICT["target"] = args[0]
            resultDICT["amount"] = args[1]

    if utterance == "[美金][100]要多少[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = args[2]
            resultDICT["target"] = args[0]
            resultDICT["amount"] = args[1]

    if utterance == "[美金][100元][可以]兌換[台幣]多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = args[0]
            resultDICT["target"] = args[3]
            resultDICT["amount"] = args[1]

    if utterance == "[美金][100元][可以]兌換多少[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = args[0]
            resultDICT["target"] = args[3]
            resultDICT["amount"] = args[1]

    if utterance == "[美金][100元]要[台幣]多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = args[2]
            resultDICT["target"] = args[0]
            resultDICT["amount"] = args[1]

    if utterance == "[美金][100元]要多少[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = args[2]
            resultDICT["target"] = args[0]
            resultDICT["amount"] = args[1]

    return resultDICT