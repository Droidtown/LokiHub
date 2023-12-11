#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for combined_sounds

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

DEBUG_combined_sounds = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_combined_sounds.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_combined_sounds:
        print("[combined_sounds] {} ===> {}".format(inputSTR, utterance))

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

    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "這樣子呀...那當您與孩子玩或逗孩子時，孩子會不會發出一些不同聲音來回應您呢？"
                resultDICT["q1"] = False
            else:
                resultDICT["response"] = "這樣子呀...那當您與孩子玩或逗孩子時，孩子會不會發出一些不同聲音來回應您呢？"
                resultDICT["q1"] = True
        else:
            # write your code here
            pass

    if utterance == "[很多]":
        if CHATBOT_MODE:
            if "很少" in inputSTR:
                resultDICT["response"] = "了解...那孩子他是否可以發出類似「咕、咕、咕」的聲音呀？"
                resultDICT["q1"] = False
            else:
                resultDICT["response"] = "了解...那孩子他是否可以發出類似「咕、咕、咕」的聲音呀？"
                resultDICT["q1"] = True
        else:
            # write your code here
            pass
        
    if utterance == "不[一定]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "不太[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那孩子他是否可以發出類似「咕、咕、咕」的聲音呀？"
            resultDICT["q1"] = False
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