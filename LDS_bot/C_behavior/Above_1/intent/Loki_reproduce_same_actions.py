#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for reproduce_same_actions

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

DEBUG_reproduce_same_actions = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_reproduce_same_actions.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_reproduce_same_actions:
        print("[reproduce_same_actions] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一直]做[一樣]的動作":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問一下，您的孩子會不會把自己喜歡的物品與他人分享呢？例如：會拿玩具給大人看？"
            resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "[一直]重複動作":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問一下，您的孩子會不會把自己喜歡的物品與他人分享呢？例如：會拿玩具給大人看？"
            resultDICT["q5"] = False
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
                resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問一下，您的孩子會不會把自己喜歡的物品與他人分享呢？例如：會拿玩具給大人看？"
                resultDICT["q5"] = True
            else:
                resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問一下，您的孩子會不會把自己喜歡的物品與他人分享呢？例如：會拿玩具給大人看？"
                resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "[很少]":
        if CHATBOT_MODE:
            if "很少" in inputSTR:
                resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問一下，您的孩子會不會把自己喜歡的物品與他人分享呢？例如：會拿玩具給大人看？"
                resultDICT["q5"] = True
            else:
                resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問一下，您的孩子會不會把自己喜歡的物品與他人分享呢？例如：會拿玩具給大人看？"
                resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "不[一定]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT