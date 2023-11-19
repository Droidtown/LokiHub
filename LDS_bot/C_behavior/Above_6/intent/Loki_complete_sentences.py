#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for complete_sentences

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

DEBUG_complete_sentences = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_complete_sentences.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_complete_sentences:
        print("[complete_sentences] {} ===> {}".format(inputSTR, utterance))

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
            resultDICT["response"] = "想請問關於數數字的部分...孩子已可以從一數到三十了嗎？"
            resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "[不常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "想請問關於數數字的部分...孩子已可以從一數到三十了嗎？"
                resultDICT["q5"] = False
            else:
                resultDICT["response"] = "想請問關於數數字的部分...孩子已可以從一數到三十了嗎？"
                resultDICT["q5"] = True
        else:
            # write your code here
            pass

    if utterance == "[很少]":
        if CHATBOT_MODE:
            if "很少" in inputSTR:
                resultDICT["response"] = "想請問關於數數字的部分...孩子已可以從一數到三十了嗎？"
                resultDICT["q5"] = False
            else:
                resultDICT["response"] = "想請問關於數數字的部分...孩子已可以從一數到三十了嗎？"
                resultDICT["q5"] = True
        else:
            # write your code here
            pass

    if utterance == "[都]講很短的":
        if CHATBOT_MODE:
            resultDICT["response"] = "想請問關於數數字的部分...孩子已可以從一數到三十了嗎？"
            resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "不太[會]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "太長的話就不行了":
        if CHATBOT_MODE:
            resultDICT["response"] = "想請問關於數數字的部分...孩子已可以從一數到三十了嗎？"
            resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "有說但聽不懂":
        if CHATBOT_MODE:
            resultDICT["response"] = "想請問關於數數字的部分...孩子已可以從一數到三十了嗎？"
            resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "看[心情]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "要看說什麼": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "講不[完整]":
        if CHATBOT_MODE:
            resultDICT["response"] = "想請問關於數數字的部分...孩子已可以從一數到三十了嗎？"
            resultDICT["q5"] = False
        else:
            # write your code here
            pass

    return resultDICT