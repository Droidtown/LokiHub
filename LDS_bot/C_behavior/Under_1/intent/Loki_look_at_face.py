#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for look_at_face

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

DEBUG_look_at_face = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_look_at_face.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_look_at_face:
        print("[look_at_face] {} ===> {}".format(inputSTR, utterance))

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
            resultDICT["response"] = "那麼...孩子沒事的時候會不會發出一些不同的聲音，好像是在玩自己的聲音的樣子呢？"
            resultDICT["q8"] = False
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
            resultDICT["response"] = "那麼...孩子沒事的時候會不會發出一些不同的聲音，好像是在玩自己的聲音的樣子呢？"
            resultDICT["q8"] = False
        else:
            # write your code here
            pass

    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "那麼...孩子沒事的時候會不會發出一些不同的聲音，好像是在玩自己的聲音的樣子呢？"
                resultDICT["q8"] = False
            else:
                resultDICT["response"] = "那麼...孩子沒事的時候會不會發出一些不同的聲音，好像是在玩自己的聲音的樣子呢？"
                resultDICT["q8"] = True
        else:
            # write your code here
            pass

    if utterance == "[很少]":
        if CHATBOT_MODE:
            if "很少" in inputSTR:
                resultDICT["response"] = "那麼...孩子沒事的時候會不會發出一些不同的聲音，好像是在玩自己的聲音的樣子呢？"
                resultDICT["q8"] = False
            else:
                resultDICT["response"] = "那麼...孩子沒事的時候會不會發出一些不同的聲音，好像是在玩自己的聲音的樣子呢？"
                resultDICT["q8"] = True
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

    if utterance == "看[人]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT