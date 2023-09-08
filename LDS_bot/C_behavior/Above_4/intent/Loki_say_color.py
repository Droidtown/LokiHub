#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for say_color

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

DEBUG_say_color = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_say_color.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_say_color:
        print("[say_color] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[不行]":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...平常的時候，孩子會像錄音機一樣一直重覆同樣的話嗎？"
            resultDICT["q8"] = False
        else:
            # write your code here
            pass

    if utterance == "[偶爾]":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...平常的時候，孩子會像錄音機一樣一直重覆同樣的話嗎？"
            resultDICT["q8"] = True            
        else:
            # write your code here
            pass

    if utterance == "[可以]但不愛講":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...平常的時候，孩子會像錄音機一樣一直重覆同樣的話嗎？"
            resultDICT["q8"] = True
        else:
            # write your code here
            pass

    if utterance == "[應該]有超過":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...平常的時候，孩子會像錄音機一樣一直重覆同樣的話嗎？"
            resultDICT["q8"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但[不常]":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...平常的時候，孩子會像錄音機一樣一直重覆同樣的話嗎？"
            resultDICT["q8"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但不愛說":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...平常的時候，孩子會像錄音機一樣一直重覆同樣的話嗎？"
            resultDICT["q8"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]搞錯[顏色]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[會]說但發音不[清楚]":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...平常的時候，孩子會像錄音機一樣一直重覆同樣的話嗎？"
            resultDICT["q8"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]說錯":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...平常的時候，孩子會像錄音機一樣一直重覆同樣的話嗎？"
            resultDICT["q8"] = False
        else:
            # write your code here
            pass

    if utterance == "[都][可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...平常的時候，孩子會像錄音機一樣一直重覆同樣的話嗎？"
            resultDICT["q8"] = True
        else:
            # write your code here
            pass

    if utterance == "[顏色][都]錯亂": #去reply裡面抓引導用問題
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

    if utterance == "好像[可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...平常的時候，孩子會像錄音機一樣一直重覆同樣的話嗎？"
            resultDICT["q8"] = True
        else:
            # write your code here
            pass

    if utterance == "好像不[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...平常的時候，孩子會像錄音機一樣一直重覆同樣的話嗎？"
            resultDICT["q8"] = False
        else:
            # write your code here
            pass

    if utterance == "沒聽過":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...平常的時候，孩子會像錄音機一樣一直重覆同樣的話嗎？"
            resultDICT["q8"] = False
        else:
            # write your code here
            pass

    if utterance == "沒辦法":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...平常的時候，孩子會像錄音機一樣一直重覆同樣的話嗎？"
            resultDICT["q8"] = False
        else:
            # write your code here
            pass

    if utterance == "還不太[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "最後一個想問的問題是...平常的時候，孩子會像錄音機一樣一直重覆同樣的話嗎？"
            resultDICT["q8"] = False
        else:
            # write your code here
            pass

    if utterance == "錯亂": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT