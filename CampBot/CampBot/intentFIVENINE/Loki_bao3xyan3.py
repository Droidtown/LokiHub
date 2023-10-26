#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for bao3xyan3

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

DEBUG_bao3xyan3 = True
CHATBOT_MODE = True

try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/replyfivenine/reply_bao3xyan3.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_bao3xyan3:
        print("[bao3xyan3] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[是]否提供[保險]":
        if args[1] in userDefinedDICT["as_insur"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                pass
        else:
            # write your code here
            pass

    if utterance == "[是]否要[自己]負責[保險]":
        if args[2] in userDefinedDICT["as_insur"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
                
        else:
            # write your code here
            pass

    if utterance == "[是]否需要[自己]投保[保險]":
        if args[2] in userDefinedDICT["as_insur"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
                
        else:
            # write your code here
            pass

    if utterance == "[是]否需要[自行]購買[保險]":
        if args[2] in userDefinedDICT["as_insur"]:
                resultDICT["response"] = getResponse(utterance, args)
                
        else:
            # write your code here
            pass

    if utterance == "保[保險]":
        if args[0] in userDefinedDICT["as_insur"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
                
        else:
            # write your code here
            pass

    if utterance == "在[保險]方面做了哪些準備？":
        if args[0] in userDefinedDICT["as_insur"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
                
        else:
            # write your code here
            pass

    if utterance == "在[保險]方面有怎樣的安排？":
        if args[0] in userDefinedDICT["as_insur"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
                
        else:
            # write your code here
            pass

    if utterance == "投保了什麼[保險]":
        if args[0] in userDefinedDICT["as_insur"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
                
        else:
            # write your code here
            pass

    if utterance == "包含[保險]":
        if args[0] in userDefinedDICT["as_insur"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有投什麼[保險]":
        if args[0] in userDefinedDICT["as_insur"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
                
        else:
            # write your code here
            pass

    if utterance == "有提供[保險]":
        if args[0] in userDefinedDICT["as_insur"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
                
        else:
            # write your code here
            pass

    if utterance == "有沒[有]投保[險]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            
        else:
            # write your code here
            pass

    if utterance == "需要[自己]保[保險]":
        if args[1] in userDefinedDICT["as_insur"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
                
        else:
            # write your code here
            pass

    if utterance == "有[保險]":
        if args[0] in userDefinedDICT["as_insur"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
                
        else:
            # write your code here
            pass

    if utterance == "有沒[有]投[保險]":
        if args[0] in userDefinedDICT["as_insur"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
                
        else:
            # write your code here
            pass

    if utterance == "負責[保險]":
        if args[0] in userDefinedDICT["as_insur"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
                
        else:
            # write your code here
            pass


    if utterance == "購買[保險]":
        if args[0] in userDefinedDICT["as_insur"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
                
        else:
            # write your code here
            pass


    if utterance == "保什麼[險]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "投什麼[保險]":
        if args[0] in userDefinedDICT["as_insur"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
                
        else:
            # write your code here
            pass

    if utterance == "投什麼[險]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "提供[保險]":
        if args[0] in userDefinedDICT["as_insur"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
                
        else:
            # write your code here
            pass


    return resultDICT