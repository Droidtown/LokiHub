#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for articulation

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

DEBUG_articulation = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_articulation.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_articulation:
        print("[articulation] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一直][都]是":
        if CHATBOT_MODE:
            resultDICT["response"] = "這樣呀...那您的孩子可以使用四至五個語詞組成的句子來跟大人一問一答嗎？"
            resultDICT["q1"] = False
        else:
            # write your code here
            pass

    if utterance == "[不常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR: #去reply裡面抓引導用問題
                resultDICT["response"] = getResponse(utterance, args)
            elif "常常" in inputSTR:
                resultDICT["response"] = "這樣呀...那您的孩子可以使用四至五個語詞組成的句子來跟大人一問一答嗎？"
                resultDICT["q1"] = False
        else:
            # write your code here
            pass

    if utterance == "[大家][都]聽不懂":
        if CHATBOT_MODE:
            resultDICT["response"] = "這樣呀...那您的孩子可以使用四至五個語詞組成的句子來跟大人一問一答嗎？"
            resultDICT["q1"] = False
        else:
            # write your code here
            pass

    if utterance == "[大家][都]聽得懂":
        if CHATBOT_MODE:
            resultDICT["response"] = "這樣呀...那您的孩子可以使用四至五個語詞組成的句子來跟大人一問一答嗎？"
            resultDICT["q1"] = True
        else:
            # write your code here
            pass

    if utterance == "[對]":
        if CHATBOT_MODE:
            resultDICT["response"] = "這樣呀...那您的孩子可以使用四至五個語詞組成的句子來跟大人一問一答嗎？"
            resultDICT["q1"] = False
        else:
            # write your code here
            pass

    if utterance == "[很常][這樣]":
        if CHATBOT_MODE:
            if "很" in inputSTR:
                resultDICT["response"] = "這樣呀...那您的孩子可以使用四至五個語詞組成的句子來跟大人一問一答嗎？"
                resultDICT["q1"] = False
            elif "不" in inputSTR:
                resultDICT["response"] = "這樣呀...那您的孩子可以使用四至五個語詞組成的句子來跟大人一問一答嗎？"
                resultDICT["q1"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但[不多]":
        if CHATBOT_MODE:
            resultDICT["response"] = "這樣呀...那您的孩子可以使用四至五個語詞組成的句子來跟大人一問一答嗎？"
            resultDICT["q1"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但[不常]":
        if CHATBOT_MODE:
            resultDICT["response"] = "這樣呀...那您的孩子可以使用四至五個語詞組成的句子來跟大人一問一答嗎？"
            resultDICT["q1"] = True
        else:
            # write your code here
            pass

    if utterance == "不太[會]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "好像不[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "這樣呀...那您的孩子可以使用四至五個語詞組成的句子來跟大人一問一答嗎？"
            resultDICT["q1"] = True
        else:
            # write your code here
            pass

    if utterance == "很少": 
        if CHATBOT_MODE:
            if "多" in inputSTR:
                resultDICT["response"] = "這樣呀...那您的孩子可以使用四至五個語詞組成的句子來跟大人一問一答嗎？"
                resultDICT["q1"] = False
            elif "少" in inputSTR: #去reply裡面抓引導用問題
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有幾[個][字][會]說不[清楚]":
        if CHATBOT_MODE:
            resultDICT["response"] = "這樣呀...那您的孩子可以使用四至五個語詞組成的句子來跟大人一問一答嗎？"
            resultDICT["q1"] = False
        else:
            # write your code here
            pass

    if utterance == "沒[錯]":
        if CHATBOT_MODE:
            resultDICT["response"] = "這樣呀...那您的孩子可以使用四至五個語詞組成的句子來跟大人一問一答嗎？"
            resultDICT["q1"] = False
        else:
            # write your code here
            pass

    return resultDICT