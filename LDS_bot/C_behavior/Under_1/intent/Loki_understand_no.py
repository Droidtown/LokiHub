#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for understand_no

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

DEBUG_understand_no = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_understand_no.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_understand_no:
        print("[understand_no] {} ===> {}".format(inputSTR, utterance))

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
            resultDICT["response"] = "好的，那接下來要問的最後一題是：孩子聽到大人叫自己的名字或小名時，會不會有反應(如：看向大人、轉頭或動動肢體)呀？"
            resultDICT["q12"] = False
        else:
            # write your code here
            pass

    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "常常" in inputSTR:
                resultDICT["response"] = "好的，那接下來要問的最後一題是：孩子聽到大人叫自己的名字或小名時，會不會有反應(如：看向大人、轉頭或動動肢體)呀？"
                resultDICT["q12"] = True
            elif "不常" in inputSTR:
                resultDICT["response"] = "好的，那接下來要問的最後一題是：孩子聽到大人叫自己的名字或小名時，會不會有反應(如：看向大人、轉頭或動動肢體)呀？"
                resultDICT["q12"] = False
        else:
            # write your code here
            pass

    if utterance == "[會]但[不多]":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的，那接下來要問的最後一題是：孩子聽到大人叫自己的名字或小名時，會不會有反應(如：看向大人、轉頭或動動肢體)呀？"
            resultDICT["q12"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但[不常]":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的，那接下來要問的最後一題是：孩子聽到大人叫自己的名字或小名時，會不會有反應(如：看向大人、轉頭或動動肢體)呀？"
            resultDICT["q12"] = True
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

    if utterance == "並不[會]每次":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的，那接下來要問的最後一題是：孩子聽到大人叫自己的名字或小名時，會不會有反應(如：看向大人、轉頭或動動肢體)呀？"
            resultDICT["q12"] = True
        else:
            # write your code here
            pass

    if utterance == "是":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的，那接下來要問的最後一題是：孩子聽到大人叫自己的名字或小名時，會不會有反應(如：看向大人、轉頭或動動肢體)呀？"
            resultDICT["q12"] = True
        else:
            # write your code here
            pass

    if utterance == "沒[什麼]反應": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "玩[自己]的不理[人]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "玩[自己]的沒反應": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
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