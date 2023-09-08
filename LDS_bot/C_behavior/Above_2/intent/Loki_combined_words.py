#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for combined_words

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

DEBUG_combined_words = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_combined_words.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_combined_words:
        print("[combined_words] {} ===> {}".format(inputSTR, utterance))

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
            if "多" in inputSTR: #去reply裡面抓引導用問題
                resultDICT["response"] = getResponse(utterance, args)
            elif "行" in inputSTR:
                resultDICT["response"] = "了解...那孩子他是否可以發出類似「咕、咕、咕」的聲音呀？"
                resultDICT["q1"] = False
        else:
            # write your code here
            pass

    if utterance == "[不太]確定": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[不常][這樣]":
        if CHATBOT_MODE:
            if "不" in inputSTR:
                resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
                resultDICT["q3"] = False
            elif "很" in inputSTR:
                resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
                resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[只]聽過[一兩][次]":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[可以]但不愛說":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[可以]但不愛講":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[好像][可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[好像]不[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "[好像]有":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[好像]沒有":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
                resultDICT["q3"] = False
            elif "常常" in inputSTR:
                resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
                resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但[不多]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[會]但[不常]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[都][可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[都]說很短的":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[都]講很短的":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
            resultDICT["q3"] = True
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
            resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "很多":
        if CHATBOT_MODE:
            if "多" in inputSTR:
                resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
                resultDICT["q3"] = True
            elif "少" in inputSTR: #去reply裡面抓引導用問題
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有說但聽不懂":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "沒有":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "沒聽過":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "沒辦法":
        if CHATBOT_MODE:
            resultDICT["response"] = "好的...那麼在平常的時候，您的孩子都只用手勢或動作來表達自己的需求嗎？"
            resultDICT["q3"] = False
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
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT