#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for hundreds_word

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

DEBUG_hundreds_word = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_hundreds_word.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_hundreds_word:
        print("[hundreds_word] {} ===> {}".format(inputSTR, utterance))

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
            resultDICT["response"] = "了解...那麼孩子現在是不是可以正確指認至少一個顏色了呢？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "[可以]但不愛講":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那麼孩子現在是不是可以正確指認至少一個顏色了呢？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "[好像][可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那麼孩子現在是不是可以正確指認至少一個顏色了呢？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "[好像]不[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那麼孩子現在是不是可以正確指認至少一個顏色了呢？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "[好像]有":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那麼孩子現在是不是可以正確指認至少一個顏色了呢？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "[好像]沒有":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那麼孩子現在是不是可以正確指認至少一個顏色了呢？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "[會]但不到[一百個]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那麼孩子現在是不是可以正確指認至少一個顏色了呢？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "[會]但不愛說":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那麼孩子現在是不是可以正確指認至少一個顏色了呢？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "[都][可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那麼孩子現在是不是可以正確指認至少一個顏色了呢？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "不太[會]": #去reply裡面抓引導用問題
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

    if utterance == "不說話":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那麼孩子現在是不是可以正確指認至少一個顏色了呢？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "很少":#去reply裡面抓引導用問題
        if CHATBOT_MODE:
            if "多" in inputSTR:
                resultDICT["response"] = "了解...那麼孩子現在是不是可以正確指認至少一個顏色了呢？"
                resultDICT["q6"] = True
            elif "少" in inputSTR: #去reply裡面抓引導用問題
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有而且超過":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那麼孩子現在是不是可以正確指認至少一個顏色了呢？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "有說但聽不懂":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那麼孩子現在是不是可以正確指認至少一個顏色了呢？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "沒辦法":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那麼孩子現在是不是可以正確指認至少一個顏色了呢？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "算有哦":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那麼孩子現在是不是可以正確指認至少一個顏色了呢？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "還不[會]說話":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...那麼孩子現在是不是可以正確指認至少一個顏色了呢？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    return resultDICT