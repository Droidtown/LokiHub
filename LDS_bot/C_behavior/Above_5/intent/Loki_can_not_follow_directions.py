#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for can_not_follow_directions

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

DEBUG_can_not_follow_directions = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_can_not_follow_directions.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_can_not_follow_directions:
        print("[can_not_follow_directions] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "對了...您的孩子可以向他人描述發生在自己身上的事情嗎？例如：分享在學校發生的事？"
                resultDICT["q3"] = True
            else:
                resultDICT["response"] = "對了...您的孩子可以向他人描述發生在自己身上的事情嗎？例如：分享在學校發生的事？"
                resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "[很少]":
        if CHATBOT_MODE:
            if "很少" in inputSTR:
                resultDICT["response"] = "對了...您的孩子可以向他人描述發生在自己身上的事情嗎？例如：分享在學校發生的事？"
                resultDICT["q3"] = True
            else:
                resultDICT["response"] = "對了...您的孩子可以向他人描述發生在自己身上的事情嗎？例如：分享在學校發生的事？"
                resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "不太[會]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT