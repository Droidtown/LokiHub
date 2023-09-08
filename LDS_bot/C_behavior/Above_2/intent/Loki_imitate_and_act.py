#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for imitate_and_act

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

DEBUG_imitate_and_act = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_imitate_and_act.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_imitate_and_act:
        print("[imitate_and_act] {} ===> {}".format(inputSTR, utterance))

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

    if utterance == "[不常][這樣]":
        if CHATBOT_MODE:
            if "不" in inputSTR:
                resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
                resultDICT["q5"] = False
            elif "很" in inputSTR:
                resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
                resultDICT["q5"] = True
        else:
            # write your code here
            pass

    if utterance == "[不行]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
            resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "[只]看過[一兩][次]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
            resultDICT["q5"] = True
        else:
            # write your code here
            pass

    if utterance == "[可以]但[不多]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
            resultDICT["q5"] = True
        else:
            # write your code here
            pass

    if utterance == "[可以]但沒那麼多[種]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
            resultDICT["q5"] = True
        else:
            # write your code here
            pass

    if utterance == "[好像][可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
            resultDICT["q5"] = True
        else:
            # write your code here
            pass

    if utterance == "[好像]不[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
            resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "[好像]沒有":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
            resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "[小孩]沒興趣": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
                resultDICT["q5"] = False
            elif "常常" in inputSTR:
                resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
                resultDICT["q5"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但[不常]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
            resultDICT["q5"] = True
        else:
            # write your code here
            pass

    if utterance == "[都][可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
            resultDICT["q5"] = True
        else:
            # write your code here
            pass

    if utterance == "不太[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
            resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "不太行":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
            resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "很少":
        if CHATBOT_MODE:
            if "多" in inputSTR:
                resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
                resultDICT["q5"] = True
            elif "少" in inputSTR: #去reply裡面抓引導用問題
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "沒辦法":
        if CHATBOT_MODE:
            resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
            resultDICT["q5"] = False
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
            resultDICT["response"] = "那...孩子在聽到大人說話後，會不會模仿並說出大人說的語詞呢？"
            resultDICT["q5"] = True
        else:
            # write your code here
            pass

    return resultDICT