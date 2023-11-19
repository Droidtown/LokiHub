#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for not_listen

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

DEBUG_not_listen = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_not_listen.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_not_listen:
        print("[not_listen] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[常常][這樣]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問，在沒有任何的提示或示範下，孩子能不能正確指出圖片中的一項物品或照片中的一位人物呢？"
                resultDICT["q7"] = True
            else:
                resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問，在沒有任何的提示或示範下，孩子能不能正確指出圖片中的一項物品或照片中的一位人物呢？"
                resultDICT["q7"] = False
        else:
            # write your code here
            pass

    if utterance == "[有時候]不聽":
        if CHATBOT_MODE:
            resultDICT["response"] = "目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問，在沒有任何的提示或示範下，孩子能不能正確指出圖片中的一項物品或照片中的一位人物呢？"
            resultDICT["q7"] = True
        else:
            # write your code here
            pass

    if utterance == "不[一定]": #去reply裡面抓引導用問題
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