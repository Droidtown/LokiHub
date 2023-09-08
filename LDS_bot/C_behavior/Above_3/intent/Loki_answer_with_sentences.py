#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for answer_with_sentences

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

DEBUG_answer_with_sentences = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_answer_with_sentences.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_answer_with_sentences:
        print("[answer_with_sentences] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[不常][這樣]":
        if CHATBOT_MODE:
            if "不" in inputSTR: #去reply裡面抓引導用問題
                resultDICT["response"] = getResponse(utterance, args)
            elif "很" in inputSTR:
                resultDICT["response"] = "好的...那...孩子說話時會口齒不清，只有主要照顧者或親近的家人才能聽得懂嗎？"
                resultDICT["q1"] = True
        else:
            # write your code here
            pass

    if utterance == "[不行]":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那...孩子說話時會口齒不清，只有主要照顧者或親近的家人才能聽得懂嗎？"
            resultDICT["q1"] = False
        else:
            # write your code here
            pass

    if utterance == "[好像][可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那...孩子說話時會口齒不清，只有主要照顧者或親近的家人才能聽得懂嗎？"
            resultDICT["q1"] = True
        else:
            # write your code here
            pass

    if utterance == "[好像]不[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那...孩子說話時會口齒不清，只有主要照顧者或親近的家人才能聽得懂嗎？"
            resultDICT["q1"] = False
        else:
            # write your code here
            pass

    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR: #去reply裡面抓引導用問題
                resultDICT["response"] = getResponse(utterance, args)
            elif "常常" in inputSTR:
                resultDICT["response"] = "好的...那...孩子說話時會口齒不清，只有主要照顧者或親近的家人才能聽得懂嗎？"
                resultDICT["q1"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但[不常]":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那...孩子說話時會口齒不清，只有主要照顧者或親近的家人才能聽得懂嗎？"
            resultDICT["q1"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但不愛說":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那...孩子說話時會口齒不清，只有主要照顧者或親近的家人才能聽得懂嗎？"
            resultDICT["q1"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但不愛講":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那...孩子說話時會口齒不清，只有主要照顧者或親近的家人才能聽得懂嗎？"
            resultDICT["q1"] = True
        else:
            # write your code here
            pass

    if utterance == "[都][可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那...孩子說話時會口齒不清，只有主要照顧者或親近的家人才能聽得懂嗎？"
            resultDICT["q1"] = True
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

    if utterance == "很少":
        if CHATBOT_MODE:
            if "多" in inputSTR:
                resultDICT["response"] = "好的...那...孩子說話時會口齒不清，只有主要照顧者或親近的家人才能聽得懂嗎？"
                resultDICT["q1"] = True
            elif "少" in inputSTR: #去reply裡面抓引導用問題
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