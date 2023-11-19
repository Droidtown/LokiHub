#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for point_and_count_to_5

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

DEBUG_point_and_count_to_5 = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_point_and_count_to_5.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_point_and_count_to_5:
        print("[point_and_count_to_5] {} ===> {}".format(inputSTR, utterance))

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
                resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問在您或其他大人的示範下，孩子可以正確仿說至少三個語詞組成的句子(如：弟弟背起書包)嗎？"
                resultDICT["q6"] = False
            else:
                resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問在您或其他大人的示範下，孩子可以正確仿說至少三個語詞組成的句子(如：弟弟背起書包)嗎？"
                resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "[很少]":
        if CHATBOT_MODE:
            if "很少" in inputSTR:
                resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問在您或其他大人的示範下，孩子可以正確仿說至少三個語詞組成的句子(如：弟弟背起書包)嗎？"
                resultDICT["q6"] = False
            else:
                resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問在您或其他大人的示範下，孩子可以正確仿說至少三個語詞組成的句子(如：弟弟背起書包)嗎？"
                resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "[都][只]用指的":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問在您或其他大人的示範下，孩子可以正確仿說至少三個語詞組成的句子(如：弟弟背起書包)嗎？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "不到[5個]":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問在您或其他大人的示範下，孩子可以正確仿說至少三個語詞組成的句子(如：弟弟背起書包)嗎？"
            resultDICT["q6"] = False
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