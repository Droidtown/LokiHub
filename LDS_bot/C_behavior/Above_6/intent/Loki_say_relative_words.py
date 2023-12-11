#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for say_relative_words

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

DEBUG_say_relative_words = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_say_relative_words.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_say_relative_words:
        print("[say_relative_words] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[不多]":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...平時孩子會常常出現自言自語的表現，只說自己感興趣的話題嗎？"
            resultDICT["q10"] = False
        else:
            # write your code here
            pass

    if utterance == "[不常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "最後一個想問的問題是...平時孩子會常常出現自言自語的表現，只說自己感興趣的話題嗎？"
                resultDICT["q10"] = False
            else:
                resultDICT["response"] = "最後一個想問的問題是...平時孩子會常常出現自言自語的表現，只說自己感興趣的話題嗎？"
                resultDICT["q10"] = True
        else:
            # write your code here
            pass

    if utterance == "[很少]":
        if CHATBOT_MODE:
            if "很少" in inputSTR:
                resultDICT["response"] = "最後一個想問的問題是...平時孩子會常常出現自言自語的表現，只說自己感興趣的話題嗎？"
                resultDICT["q10"] = False
            else:
                resultDICT["response"] = "最後一個想問的問題是...平時孩子會常常出現自言自語的表現，只說自己感興趣的話題嗎？"
                resultDICT["q10"] = True
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

    return resultDICT