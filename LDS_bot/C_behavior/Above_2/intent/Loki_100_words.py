#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for 100_words

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

DEBUG_100_words = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_100_words.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_100_words:
        print("[100_words] {} ===> {}".format(inputSTR, utterance))

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

    if utterance == "[不常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR: #去reply裡面抓引導用問題
                resultDICT["response"] = getResponse(utterance, args)
            elif "常常" in inputSTR:
                resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
                resultDICT["q2"] = True
        else:
            # write your code here
            pass

    if utterance == "[不行]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "[只][會]出個聲音":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "[只]聽過[一兩][次]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[可以]但不愛說":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = True
        else:
            # write your code here
            pass

    if utterance == "[可以]但沒那麼多":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "[好像][可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = True
        else:
            # write your code here
            pass

    if utterance == "[好像]不[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "[好像]有":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = True
        else:
            # write your code here
            pass

    if utterance == "[好像]沒有":
        if CHATBOT_MODE:
            rresultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "[應該]有超過":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但不到[100個]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "[會]但不愛講":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = True
        else:
            # write your code here
            pass

    if utterance == "[都][只]用指的":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "[都]用哭的":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "不太[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "不太行":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "不說話":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "有說但聽不懂":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = True
        else:
            # write your code here
            pass

    if utterance == "沒有":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "沒聽過":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "沒聽過[小孩]說話":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "沒辦法":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    if utterance == "火星語": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "算有哦":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = True
        else:
            # write your code here
            pass

    if utterance == "還不[會]說話":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子能不能在日常生活中，連結兩個語詞來表達需求呀？例如：說出類似「媽媽抱抱」、「媽媽喝」？"
            resultDICT["q2"] = False
        else:
            # write your code here
            pass

    return resultDICT