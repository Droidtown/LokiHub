#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for sex

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

DEBUG_sex = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_sex.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_sex:
        print("[sex] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "X愛":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["correct"] = inputSTR.upper().replace(utterance,"做愛")

    if utterance == "ㄋㄞˇ":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["correct"] = inputSTR.replace(utterance,"奶")

    if utterance == "ㄞˋ":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["correct"] = inputSTR.replace(utterance,"愛")

    if utterance == "假ㄋ":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["correct"] = inputSTR.replace(utterance,"假奶")

    if utterance == "做X":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["correct"] = inputSTR.upper().replace(utterance,"做愛")

    if utterance == "做i":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["correct"] = inputSTR.lower().replace(utterance,"做愛")

    if utterance == "大ㄋ":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["correct"] = inputSTR.replace(utterance,"大奶")

    if utterance == "女乃":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["correct"] = inputSTR.replace(utterance,"奶")

    if utterance == "小ㄋ":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["correct"] = inputSTR.replace(utterance,"小奶")

    if utterance == "忄生":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["correct"] = inputSTR.replace(utterance,"性")

    if utterance == "扌丁":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["correct"] = inputSTR.replace(utterance,"打")

    if utterance == "捉i":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["correct"] = inputSTR.lower().replace(utterance,"做愛")

    if utterance == "氵查":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["correct"] = inputSTR.replace(utterance,"渣")

    if utterance == "p腿":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["correct"] = inputSTR.lower().replace(utterance.lower(),"劈腿")

    return resultDICT