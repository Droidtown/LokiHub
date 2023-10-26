#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for an1quuan2cwo4shi1

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

DEBUG_an1quuan2cwo4shi1 = True
CHATBOT_MODE = True

try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/replyfivenine/reply_an1quuan2cwo4shi1.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_an1quuan2cwo4shi1:
        print("[an1quuan2cwo4shi1] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[會]受傷":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "不[舒服]":
        if args[0] == "舒服":
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass

    if utterance == "出現[危險]的情況":
        if "危" in args[0]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "受傷了[該]怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "受傷怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "如何處理受傷":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有[危險]":
        if args[0] in ["危險", "意外"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass
        
    if utterance == "有[安全]保護措施":
        if args[0] == "安全":
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有[安全]措施":
        if args[0] == "安全":
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有[相關]的[安全]措施":
        if args[1] == "安全":
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有什麼[安全]措施":
        if args[0] == "安全":
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有沒[有][安全]措施":
        if args[0] == "安全":
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有防護措施":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "發生[危險]":
        if args[0] in ["危險", "意外"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "碰[上][危險]":
        if args[0] in ["危險", "意外"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "確保[安全]":
        if args[0] == "安全":
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "身體有狀況":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass
        
    if utterance == "[不適]":
        if args[0] == "不適":
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "在[你們]那受傷怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "出現[危險]的[情況]":
        if "危" in args[0]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "身體有[狀況]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT