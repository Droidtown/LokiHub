#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for imitate_actions

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

DEBUG_imitate_actions = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_imitate_actions.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_imitate_actions:
        print("[imitate_actions] {} ===> {}".format(inputSTR, utterance))

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
            resultDICT["response"] = "了解...接著想問問在一些簡單的遊戲活動中，如：炒蘿蔔、擊掌，大人示範後孩子是否能參與部分活動呢？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "[只]看過[一兩][次]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...接著想問問在一些簡單的遊戲活動中，如：炒蘿蔔、擊掌，大人示範後孩子是否能參與部分活動呢？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "了解...接著想問問在一些簡單的遊戲活動中，如：炒蘿蔔、擊掌，大人示範後孩子是否能參與部分活動呢？"
                resultDICT["q3"] = False
            elif "常常" in inputSTR:
                resultDICT["response"] = "了解...接著想問問在一些簡單的遊戲活動中，如：炒蘿蔔、擊掌，大人示範後孩子是否能參與部分活動呢？"
                resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但[不多]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...接著想問問在一些簡單的遊戲活動中，如：炒蘿蔔、擊掌，大人示範後孩子是否能參與部分活動呢？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但[不常]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...接著想問問在一些簡單的遊戲活動中，如：炒蘿蔔、擊掌，大人示範後孩子是否能參與部分活動呢？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[都][可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...接著想問問在一些簡單的遊戲活動中，如：炒蘿蔔、擊掌，大人示範後孩子是否能參與部分活動呢？"
            resultDICT["q3"] = True
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

    if utterance == "不太理人": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "好像不[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...接著想問問在一些簡單的遊戲活動中，如：炒蘿蔔、擊掌，大人示範後孩子是否能參與部分活動呢？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "好像沒有":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...接著想問問在一些簡單的遊戲活動中，如：炒蘿蔔、擊掌，大人示範後孩子是否能參與部分活動呢？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "很少":
        if CHATBOT_MODE:
            if "多" in inputSTR:
                resultDICT["response"] = "了解...接著想問問在一些簡單的遊戲活動中，如：炒蘿蔔、擊掌，大人示範後孩子是否能參與部分活動呢？"
                resultDICT["q3"] = True
            elif "少" in inputSTR:
                resultDICT["response"] = "了解...接著想問問在一些簡單的遊戲活動中，如：炒蘿蔔、擊掌，大人示範後孩子是否能參與部分活動呢？"
                resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "沒[什麼]反應":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...接著想問問在一些簡單的遊戲活動中，如：炒蘿蔔、擊掌，大人示範後孩子是否能參與部分活動呢？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "沒辦法":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...接著想問問在一些簡單的遊戲活動中，如：炒蘿蔔、擊掌，大人示範後孩子是否能參與部分活動呢？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "玩[自己]的不理人":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...接著想問問在一些簡單的遊戲活動中，如：炒蘿蔔、擊掌，大人示範後孩子是否能參與部分活動呢？"
            resultDICT["q3"] = False
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