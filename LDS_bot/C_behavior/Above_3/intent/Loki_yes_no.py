#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for yes_no

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

DEBUG_yes_no = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
#if CHATBOT_MODE:
#    try:
#        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_yes_no.json"), encoding="utf-8"))
#    except Exception as e:
#        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_yes_no:
        print("[yes_no] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "不可以":
        if CHATBOT_MODE:
            resultDICT["yes_no"] = False
        else:
            # write your code here
            pass

    if utterance == "不對":
        if CHATBOT_MODE:
            resultDICT["yes_no"] = False
        else:
            # write your code here
            pass

    if utterance == "可以":
        if CHATBOT_MODE:
            resultDICT["yes_no"] = True
        else:
            # write your code here
            pass

    if utterance == "否":
        if CHATBOT_MODE:
            resultDICT["yes_no"] = False
        else:
            # write your code here
            pass

    if utterance == "對":
        if CHATBOT_MODE:
            resultDICT["yes_no"] = True
        else:
            # write your code here
            pass

    if utterance == "對啊":
        if CHATBOT_MODE:
            resultDICT["yes_no"] = True
        else:
            # write your code here
            pass

    if utterance == "有":
        if CHATBOT_MODE:
            resultDICT["yes_no"] = True
        else:
            # write your code here
            pass

    if utterance == "沒有":
        if CHATBOT_MODE:
            resultDICT["yes_no"] = False
        else:
            # write your code here
            pass

    return resultDICT