#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for sharing

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

DEBUG_sharing = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_sharing.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_sharing:
        print("[sharing] {} ===> {}".format(inputSTR, utterance))

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
            resultDICT["response"] = "是這樣子呀...那在沒有大人的任何手勢或動作下，孩子是否可以聽懂日常生活中常用的簡單短句呢？例如：媽媽抱抱、喝ㄋㄟㄋㄟ、給我、洗澡了？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "[不太]確定": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[只]看過[一兩][次]":
        if CHATBOT_MODE:
            resultDICT["response"] = "是這樣子呀...那在沒有大人的任何手勢或動作下，孩子是否可以聽懂日常生活中常用的簡單短句呢？例如：媽媽抱抱、喝ㄋㄟㄋㄟ、給我、洗澡了？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = getResponse(utterance, args) #去reply裡面抓引導用問題
            elif "常常" in inputSTR:
                resultDICT["response"] = "是這樣子呀...那在沒有大人的任何手勢或動作下，孩子是否可以聽懂日常生活中常用的簡單短句呢？例如：媽媽抱抱、喝ㄋㄟㄋㄟ、給我、洗澡了？"
                resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但[不常]":
        if CHATBOT_MODE:
            resultDICT["response"] = "是這樣子呀...那在沒有大人的任何手勢或動作下，孩子是否可以聽懂日常生活中常用的簡單短句呢？例如：媽媽抱抱、喝ㄋㄟㄋㄟ、給我、洗澡了？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "[都][只是]拿著": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[都]拿在手[裡]": #去reply裡面抓引導用問題
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

    if utterance == "不太理人": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "好像不[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "是這樣子呀...那在沒有大人的任何手勢或動作下，孩子是否可以聽懂日常生活中常用的簡單短句呢？例如：媽媽抱抱、喝ㄋㄟㄋㄟ、給我、洗澡了？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "好像沒有":
        if CHATBOT_MODE:
            resultDICT["response"] = "是這樣子呀...那在沒有大人的任何手勢或動作下，孩子是否可以聽懂日常生活中常用的簡單短句呢？例如：媽媽抱抱、喝ㄋㄟㄋㄟ、給我、洗澡了？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "很少":
        if CHATBOT_MODE:
            if "多" in inputSTR:
                resultDICT["response"] = "是這樣子呀...那在沒有大人的任何手勢或動作下，孩子是否可以聽懂日常生活中常用的簡單短句呢？例如：媽媽抱抱、喝ㄋㄟㄋㄟ、給我、洗澡了？"
                resultDICT["q6"] = True
            elif "少" in inputSTR:
                resultDICT["response"] = "是這樣子呀...那在沒有大人的任何手勢或動作下，孩子是否可以聽懂日常生活中常用的簡單短句呢？例如：媽媽抱抱、喝ㄋㄟㄋㄟ、給我、洗澡了？"
                resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "很少見":
        if CHATBOT_MODE:
            resultDICT["response"] = "是這樣子呀...那在沒有大人的任何手勢或動作下，孩子是否可以聽懂日常生活中常用的簡單短句呢？例如：媽媽抱抱、喝ㄋㄟㄋㄟ、給我、洗澡了？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "拿著不放": #去reply裡面抓引導用問題
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