#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for play_with_adults

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

DEBUG_play_with_adults = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_play_with_adults.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_play_with_adults:
        print("[play_with_adults] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[不太]確定": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[不行]":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問一下在日常生活中，孩子會重覆不斷做出固定的動作嗎？例如：重覆玩手、一直轉圈圈、以固定的單一方式玩玩具？"
            resultDICT["q4"] = False
        else:
            # write your code here
            pass

    if utterance == "[只]看過[一兩][次]":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問一下在日常生活中，孩子會重覆不斷做出固定的動作嗎？例如：重覆玩手、一直轉圈圈、以固定的單一方式玩玩具？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "[小孩][很]喜歡跟[人]玩":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問一下在日常生活中，孩子會重覆不斷做出固定的動作嗎？例如：重覆玩手、一直轉圈圈、以固定的單一方式玩玩具？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "另外，想請問一下在日常生活中，孩子會重覆不斷做出固定的動作嗎？例如：重覆玩手、一直轉圈圈、以固定的單一方式玩玩具？"
                resultDICT["q4"] = False
            elif "常常" in inputSTR:
                resultDICT["response"] = "另外，想請問一下在日常生活中，孩子會重覆不斷做出固定的動作嗎？例如：重覆玩手、一直轉圈圈、以固定的單一方式玩玩具？"
                resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但[不多]":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問一下在日常生活中，孩子會重覆不斷做出固定的動作嗎？例如：重覆玩手、一直轉圈圈、以固定的單一方式玩玩具？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但[不常]":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問一下在日常生活中，孩子會重覆不斷做出固定的動作嗎？例如：重覆玩手、一直轉圈圈、以固定的單一方式玩玩具？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "不[一定]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "不喜歡跟[大人]玩":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問一下在日常生活中，孩子會重覆不斷做出固定的動作嗎？例如：重覆玩手、一直轉圈圈、以固定的單一方式玩玩具？"
            resultDICT["q4"] = False
        else:
            # write your code here
            pass

    if utterance == "不太[會]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "不太理人": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "不跟[大人]玩":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問一下在日常生活中，孩子會重覆不斷做出固定的動作嗎？例如：重覆玩手、一直轉圈圈、以固定的單一方式玩玩具？"
            resultDICT["q4"] = False
        else:
            # write your code here
            pass

    if utterance == "並不[會]每次":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問一下在日常生活中，孩子會重覆不斷做出固定的動作嗎？例如：重覆玩手、一直轉圈圈、以固定的單一方式玩玩具？"
            resultDICT["q4"] = True
        else:
            # write your code here
            pass

    if utterance == "小孩不喜歡[別人]碰[他]":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問一下在日常生活中，孩子會重覆不斷做出固定的動作嗎？例如：重覆玩手、一直轉圈圈、以固定的單一方式玩玩具？"
            resultDICT["q4"] = False
        else:
            # write your code here
            pass

    if utterance == "沒[什麼]反應": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "沒辦法":
        if CHATBOT_MODE:
            resultDICT["response"] = "另外，想請問一下在日常生活中，孩子會重覆不斷做出固定的動作嗎？例如：重覆玩手、一直轉圈圈、以固定的單一方式玩玩具？"
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

    if utterance == "看玩什麼": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT