#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for location_words

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

DEBUG_location_words = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_location_words.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_location_words:
        print("[location_words] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[不行]":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問您的孩子在團體中，常常是一個人玩，很少和同學一起互動嗎？"
            resultDICT["q4"] = False
        else:
            # write your code here
            pass

    if utterance == "[偶爾]":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問您的孩子在團體中，常常是一個人玩，很少和同學一起互動嗎？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "[只][會]幾[個]":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問您的孩子在團體中，常常是一個人玩，很少和同學一起互動嗎？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但[不多]":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問您的孩子在團體中，常常是一個人玩，很少和同學一起互動嗎？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但[不常]":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問您的孩子在團體中，常常是一個人玩，很少和同學一起互動嗎？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但不愛講":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問您的孩子在團體中，常常是一個人玩，很少和同學一起互動嗎？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "[有時][會]搞錯":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問您的孩子在團體中，常常是一個人玩，很少和同學一起互動嗎？"
            resultDICT["q4"] = False
        else:
            # write your code here
            pass

    if utterance == "不[一定]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "不太[會]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "不太行": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "好像[可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問您的孩子在團體中，常常是一個人玩，很少和同學一起互動嗎？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "好像不[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問您的孩子在團體中，常常是一個人玩，很少和同學一起互動嗎？"
            resultDICT["q4"] = False
        else:
            # write your code here
            pass

    if utterance == "搞不[清楚]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "沒聽過":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問您的孩子在團體中，常常是一個人玩，很少和同學一起互動嗎？"
            resultDICT["q4"] = False
        else:
            # write your code here
            pass

    if utterance == "沒辦法":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問您的孩子在團體中，常常是一個人玩，很少和同學一起互動嗎？"
            resultDICT["q4"] = False
        else:
            # write your code here
            pass

    if utterance == "看[心情]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT