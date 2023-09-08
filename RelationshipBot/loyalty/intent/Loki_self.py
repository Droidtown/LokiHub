#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for self

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

DEBUG_self = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_self.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_self:
        print("[self] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[對方]逼[我]封鎖[我][前][女友]":
        if CHATBOT_MODE:
            if args[1] == "我" and args[2] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我][常常]精神出軌":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]不想再原諒[他]了":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]出軌":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]劈腿":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]和[前][女友][只是]朋友":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]和[前][女友]還有聯絡":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]好像被劈腿":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]好像被戴綠帽":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass


    if utterance == "[我]沒辦法再相信[他]了":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]無法克制[自己]不出軌":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]無法克制[自己]不劈腿":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]被劈腿":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]被戴綠帽":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]被腳踏[兩條]船":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]認為[他]不[應該]原諒[我]":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]還留著[前][女友]的[東西]":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]還留著[前]任的[東西]":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass
        
    if utterance == "[我][只是]不[小心]就滑進去":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]已經出軌好幾[次]了":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]已經出軌很多次了":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]已經劈腿好幾[次]了":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]已經劈腿很多次了":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]戴[我][女友]綠帽":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我][會]讓[別][人]坐[前]座":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我][會]讓其他[女生][朋友]坐[前]座":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我][會]載[別][人]回家":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我][會]載其他[女生][朋友]回家":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]騙[他][我]沒有出軌":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]騙[他][我]沒有劈腿":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]騙[他]說[我]沒有出軌":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我]騙[他]說[我]沒有劈腿":
        if CHATBOT_MODE:
            if args[0] == "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我][只是]去[旅館]休息":
        if CHATBOT_MODE:
            if args[0] in ("我","我們") and args[2] in userDefinedDICT["_hotel"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[我][只是]去[旅館]開會":
        if CHATBOT_MODE:
            if args[0] in ("我","我們")and args[2] in userDefinedDICT["_hotel"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass
        
    if utterance == "[我][只是]犯了[全]天下[男人][都][會]犯的[錯]":
        if CHATBOT_MODE:
            if args[0] in ("我","我們"):
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    return resultDICT