#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for sentence_repetition

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

DEBUG_sentence_repetition = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_sentence_repetition.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_sentence_repetition:
        print("[sentence_repetition] {} ===> {}".format(inputSTR, utterance))

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
                resultDICT["response"] = "接著想了解一下...孩子現在能不能主動地說出至少一種的疑問句呀？例如：是誰？那是什麼？"
                resultDICT["q10"] = True
            else:
                resultDICT["response"] = "接著想了解一下...孩子現在能不能主動地說出至少一種的疑問句呀？例如：是誰？那是什麼？"
                resultDICT["q10"] = False
        else:
            # write your code here
            pass

    if utterance == "[很常][這樣]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "接著想了解一下...孩子現在能不能主動地說出至少一種的疑問句呀？例如：是誰？那是什麼？"
                resultDICT["q10"] = True
            else:
                resultDICT["response"] = "接著想了解一下...孩子現在能不能主動地說出至少一種的疑問句呀？例如：是誰？那是什麼？"
                resultDICT["q10"] = False
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