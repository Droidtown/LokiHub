#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for age

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
from datetime import datetime
import json
import os
import re

DEBUG_age = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_age.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_age:
        print("[age] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[20]歲":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[0]
            

    if utterance == "[20]歲到[50]歲":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = str((int(args[0])+int(args[1]))/2)
            

    if utterance == "[20]足歲":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[0]
            

    if utterance == "[我][20]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[1]
            

    if utterance == "[我][今]年[20]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[2]
            

    if utterance == "到[50]歲":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[0]
            

    if utterance == "[都][44]了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[1]
            

    if utterance == "[大概][20]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[1]
            

    if utterance == "[現在][20]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[1]
            

    if utterance == "剛滿[20]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[0]
            

    if utterance == "剛過[20]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[0]
            

    if utterance == "滿[20]了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if re.search(r'\d+了', inputSTR):
                resultDICT['age'] = args[0]
            

    if utterance == "[我]朋友[30]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[1]
            resultDICT['person'] = '朋友'

    if utterance == "年齡[30]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[0]
            

    if utterance == "我[媽媽][30]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[1]
            resultDICT['person'] = args[0]
            

    if utterance == "歲數[30]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[0]
            

    if utterance == "[20]了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if re.search(r'\d+了', inputSTR):
                resultDICT['age'] = args[0]
            

    if utterance == "[中]年":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = "50"
            

    if utterance == "[我]朋友[今]年[30]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[2]
            resultDICT['person'] = "朋友"
            

    if utterance == "[我]朋友[現在][30]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[2]
            resultDICT['person'] = "朋友"
            

    if utterance == "[老]年":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = "65"
            

    if utterance == "成年":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = "20"
            

    if utterance == "我[媽媽][今]年[30]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[2]
            resultDICT['person'] = args[0]
            

    if utterance == "我[媽媽][現在][30]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = args[2]
            resultDICT['person'] = args[0]
            

    if utterance == "未成年":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = "10"
            

    if utterance == "民國[88]年生":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = str((datetime.now().year-1911)-int(args[0]))
            

    if utterance == "讀大學的年紀":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = "22"
            

    if utterance == "退休的年紀":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = "66"
            

    if utterance == "高中生":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['age'] = "17"
            

    return resultDICT