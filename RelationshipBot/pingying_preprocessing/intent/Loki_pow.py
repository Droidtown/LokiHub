#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for pow

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

DEBUG_pow = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_pow.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_pow:
        print("[pow] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[p]友":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT["_p"]:
                resultDICT["correct"] = inputSTR.replace(args[0],"炮")

    if utterance == "ㄩ[p]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
           if args[0] in userDefinedDICT["_p"]:
                resultDICT["correct"] = inputSTR.replace(args[0],"炮")

    if utterance == "ㄩ過[ㄆ]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT["_p"]:
                resultDICT["correct"] = inputSTR.replace(args[0],"炮")

    if utterance == "扌丁[P]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT["_p"]:
                resultDICT["correct"] = inputSTR.replace("扌丁"+args[0],"打炮")
    if utterance == "約[p]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT["_p"]:
                resultDICT["correct"] = inputSTR.replace(args[0],"炮")
    if utterance == "約過[p]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT["_p"]:
                resultDICT["correct"] = inputSTR.replace(args[0],"炮")

    if utterance == "打[P]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT["_p"]:
                resultDICT["correct"] = inputSTR.replace(args[0],"炮")

    if utterance == "騙[p]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT["_p"]:
                resultDICT["correct"] = inputSTR.replace(args[0],"炮")

    if utterance == "騙[我][p]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[1] in userDefinedDICT["_p"]:
                resultDICT["correct"] = inputSTR.replace(args[1],"炮")

    return resultDICT