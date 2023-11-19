#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for express_needs

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

DEBUG_express_needs = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_express_needs.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_express_needs:
        print("[express_needs] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一直]做[一樣]的[動作]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[不太]確定": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[常常]": 
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "那...在沒有任何提示下，您的孩子能不能聽懂日常生活中常見的指令並完成動作呢？例如：拿去丟掉、鞋鞋收起來、拿給媽媽？"
                resultDICT["q1"] = False
            else:
                resultDICT["response"] = "那...在沒有任何提示下，您的孩子能不能聽懂日常生活中常見的指令並完成動作呢？例如：拿去丟掉、鞋鞋收起來、拿給媽媽？"
                resultDICT["q1"] = True
        else:
            # write your code here
            pass

    if utterance == "[很少]":
        if CHATBOT_MODE:
            if "很少" in inputSTR:
                resultDICT["response"] = "那...在沒有任何提示下，您的孩子能不能聽懂日常生活中常見的指令並完成動作呢？例如：拿去丟掉、鞋鞋收起來、拿給媽媽？"
                resultDICT["q1"] = False
            else:
                resultDICT["response"] = "那...在沒有任何提示下，您的孩子能不能聽懂日常生活中常見的指令並完成動作呢？例如：拿去丟掉、鞋鞋收起來、拿給媽媽？"
                resultDICT["q1"] = True
        else:
            # write your code here
            pass

    if utterance == "[都]用哭的": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
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

    if utterance == "並不[會]每次":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...在沒有任何提示下，您的孩子能不能聽懂日常生活中常見的指令並完成動作呢？例如：拿去丟掉、鞋鞋收起來、拿給媽媽？"
            resultDICT["q1"] = True
        else:
            # write your code here
            pass

    if utterance == "沒[什麼]反應": #去reply裡面抓引導用問題
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