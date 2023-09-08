#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for girlfriend

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

DEBUG_girlfriend = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_girlfriend.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_girlfriend:
        print("[girlfriend] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[對方][假]高潮":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]叫得[很奇怪]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]叫得很難聽":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]是死亡海鮮":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]的[私密處]很臭":
        if CHATBOT_MODE:
            if args[1] in userDefinedDICT["_vagina"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]的[私密處]有[異味]":
        if CHATBOT_MODE:
            if args[1] in userDefinedDICT["_vagina"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]的叫聲[很奇怪]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]的叫聲很難聽":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]騙[我][他]是處女":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]騙[我]說[他]是處女":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]嫌[我]很乾":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]說[我]很乾":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]的[私密處]好臭":
        if CHATBOT_MODE:
            if args[1] in userDefinedDICT["_vagina"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    return resultDICT