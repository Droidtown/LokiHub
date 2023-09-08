#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for ten_words

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

DEBUG_ten_words = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_ten_words.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_ten_words:
        print("[ten_words] {} ===> {}".format(inputSTR, utterance))

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
            resultDICT["response"] = "最後一個想問的問題是...在沒有任何幫忙下，您的孩子可以聽懂連續兩個動作的指令嗎？例如：撿起來拿給爸爸？"
            resultDICT["q11"] = False
        else:
            # write your code here
            pass

    if utterance == "[只]聽過[一兩][次]":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...在沒有任何幫忙下，您的孩子可以聽懂連續兩個動作的指令嗎？例如：撿起來拿給爸爸？"
            resultDICT["q11"] = False
        else:
            # write your code here
            pass

    if utterance == "[可以]但[不多]":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...在沒有任何幫忙下，您的孩子可以聽懂連續兩個動作的指令嗎？例如：撿起來拿給爸爸？"
            resultDICT["q11"] = False
        else:
            # write your code here
            pass

    if utterance == "[可以]但沒那麼多":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...在沒有任何幫忙下，您的孩子可以聽懂連續兩個動作的指令嗎？例如：撿起來拿給爸爸？"
            resultDICT["q11"] = False
            # write your code here
            pass

    if utterance == "[會]但不到[10個]":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...在沒有任何幫忙下，您的孩子可以聽懂連續兩個動作的指令嗎？例如：撿起來拿給爸爸？"
            resultDICT["q11"] = False
        else:
            # write your code here
            pass

    if utterance == "[有時候]":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...在沒有任何幫忙下，您的孩子可以聽懂連續兩個動作的指令嗎？例如：撿起來拿給爸爸？"
            resultDICT["q11"] = True
        else:
            # write your code here
            pass

    if utterance == "[都][可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...在沒有任何幫忙下，您的孩子可以聽懂連續兩個動作的指令嗎？例如：撿起來拿給爸爸？"
            resultDICT["q11"] = True
        else:
            # write your code here
            pass

    if utterance == "[都]用叫的": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[都]用哭的": #去reply裡面抓引導用問題
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

    if utterance == "不說話[都]用指的":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...在沒有任何幫忙下，您的孩子可以聽懂連續兩個動作的指令嗎？例如：撿起來拿給爸爸？"
            resultDICT["q11"] = False
        else:
            # write your code here
            pass

    if utterance == "好像沒有":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...在沒有任何幫忙下，您的孩子可以聽懂連續兩個動作的指令嗎？例如：撿起來拿給爸爸？"
            resultDICT["q11"] = False
        else:
            # write your code here
            pass

    if utterance == "很少": 
        if CHATBOT_MODE:
            if "多" in inputSTR:
                resultDICT["response"] = "最後一個想問的問題是...在沒有任何幫忙下，您的孩子可以聽懂連續兩個動作的指令嗎？例如：撿起來拿給爸爸？"
                resultDICT["q11"] = True
            elif "少" in inputSTR: #去reply裡面抓引導用問題
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "拉[大人]去拿":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...在沒有任何幫忙下，您的孩子可以聽懂連續兩個動作的指令嗎？例如：撿起來拿給爸爸？"
            resultDICT["q11"] = False
        else:
            # write your code here
            pass

    if utterance == "有而且超過[十個]":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...在沒有任何幫忙下，您的孩子可以聽懂連續兩個動作的指令嗎？例如：撿起來拿給爸爸？"
            resultDICT["q11"] = True
        else:
            # write your code here
            pass

    if utterance == "有說但聽不懂":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...在沒有任何幫忙下，您的孩子可以聽懂連續兩個動作的指令嗎？例如：撿起來拿給爸爸？"
            resultDICT["q11"] = True
        else:
            # write your code here
            pass

    if utterance == "沒聽過[小孩]說話":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...在沒有任何幫忙下，您的孩子可以聽懂連續兩個動作的指令嗎？例如：撿起來拿給爸爸？"
            resultDICT["q11"] = False
        else:
            # write your code here
            pass

    if utterance == "沒辦法":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...在沒有任何幫忙下，您的孩子可以聽懂連續兩個動作的指令嗎？例如：撿起來拿給爸爸？"
            resultDICT["q11"] = False
        else:
            # write your code here
            pass

    if utterance == "看[心情]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "算有哦":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...在沒有任何幫忙下，您的孩子可以聽懂連續兩個動作的指令嗎？例如：撿起來拿給爸爸？"
            resultDICT["q11"] = True
        else:
            # write your code here
            pass

    if utterance == "還不[會]說話":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...在沒有任何幫忙下，您的孩子可以聽懂連續兩個動作的指令嗎？例如：撿起來拿給爸爸？"
            resultDICT["q11"] = False
        else:
            # write your code here
            pass

    return resultDICT