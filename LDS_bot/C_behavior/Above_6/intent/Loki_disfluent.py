#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for disfluent

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

DEBUG_disfluent = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_disfluent.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_disfluent:
        print("[disfluent] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[不常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "另一個也是關於數數的問題...在沒有任何的提示或幫忙之下，孩子可不可以從一點數到十三呢？"
                resultDICT["q8"] = True
            elif "常常" in inputSTR:
                resultDICT["response"] = "另一個也是關於數數的問題...在沒有任何的提示或幫忙之下，孩子可不可以從一點數到十三呢？"
                resultDICT["q8"] = False
        else:
            # write your code here
            pass

    if utterance == "不太[會]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "很少":
        if CHATBOT_MODE:
            if "多" in inputSTR:
                resultDICT["response"] = "另一個也是關於數數的問題...在沒有任何的提示或幫忙之下，孩子可不可以從一點數到十三呢？"
                resultDICT["q8"] = False
            elif "少" in inputSTR:
                resultDICT["response"] = "另一個也是關於數數的問題...在沒有任何的提示或幫忙之下，孩子可不可以從一點數到十三呢？"
                resultDICT["q8"] = True
        else:
            # write your code here
            pass

    if utterance == "沒[錯]":
        if CHATBOT_MODE:
            resultDICT["response"] = "另一個也是關於數數的問題...在沒有任何的提示或幫忙之下，孩子可不可以從一點數到十三呢？"
            resultDICT["q8"] = False
        else:
            # write your code here
            pass

    if utterance == "看跟誰說話":
        if CHATBOT_MODE:
            resultDICT["response"] = "另一個也是關於數數的問題...在沒有任何的提示或幫忙之下，孩子可不可以從一點數到十三呢？"
            resultDICT["q8"] = False
        else:
            # write your code here
            pass

    if utterance == "緊張的[時候][會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "另一個也是關於數數的問題...在沒有任何的提示或幫忙之下，孩子可不可以從一點數到十三呢？"
            resultDICT["q8"] = False
        else:
            # write your code here
            pass

    if utterance == "講得快的[時候]":
        if CHATBOT_MODE:
            resultDICT["response"] = "另一個也是關於數數的問題...在沒有任何的提示或幫忙之下，孩子可不可以從一點數到十三呢？"
            resultDICT["q8"] = False
        else:
            # write your code here
            pass

    return resultDICT