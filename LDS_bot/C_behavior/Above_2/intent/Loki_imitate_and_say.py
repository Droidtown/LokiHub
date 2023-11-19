#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for imitate_and_say

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

DEBUG_imitate_and_say = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_imitate_and_say.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_imitate_and_say:
        print("[imitate_and_say] {} ===> {}".format(inputSTR, utterance))

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

    if utterance == "[只][會]出個聲音":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...對了，當您和孩子互動時，孩子一般都不看您的示範或不聽大人的說明嗎？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "[只][會]動一下嘴巴":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...對了，當您和孩子互動時，孩子一般都不看您的示範或不聽大人的說明嗎？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "[只]聽過[一兩][次]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...對了，當您和孩子互動時，孩子一般都不看您的示範或不聽大人的說明嗎？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "了解...對了，當您和孩子互動時，孩子一般都不看您的示範或不聽大人的說明嗎？"
                resultDICT["q6"] = False
            else:
                resultDICT["response"] = "了解...對了，當您和孩子互動時，孩子一般都不看您的示範或不聽大人的說明嗎？"
                resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "[很少]":
        if CHATBOT_MODE:
            if "很少" in inputSTR:
                resultDICT["response"] = "了解...對了，當您和孩子互動時，孩子一般都不看您的示範或不聽大人的說明嗎？"
                resultDICT["q6"] = False
            else:
                resultDICT["response"] = "了解...對了，當您和孩子互動時，孩子一般都不看您的示範或不聽大人的說明嗎？"
                resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "[都]說很短的":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...對了，當您和孩子互動時，孩子一般都不看您的示範或不聽大人的說明嗎？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "[都]講很短的":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...對了，當您和孩子互動時，孩子一般都不看您的示範或不聽大人的說明嗎？"
            resultDICT["q6"] = True
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

    if utterance == "並不[會]每次":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...對了，當您和孩子互動時，孩子一般都不看您的示範或不聽大人的說明嗎？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "太長的[話]就不行了":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...對了，當您和孩子互動時，孩子一般都不看您的示範或不聽大人的說明嗎？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "有說但聽不懂":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...對了，當您和孩子互動時，孩子一般都不看您的示範或不聽大人的說明嗎？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "沒[什麼]反應": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "沒聽過":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...對了，當您和孩子互動時，孩子一般都不看您的示範或不聽大人的說明嗎？"
            resultDICT["q6"] = False
        else:
            # write your code here
            pass

    if utterance == "沒那麼多[種]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...對了，當您和孩子互動時，孩子一般都不看您的示範或不聽大人的說明嗎？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "看[心情]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "短的[才]有辦法說":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...對了，當您和孩子互動時，孩子一般都不看您的示範或不聽大人的說明嗎？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "講不[完整]":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...對了，當您和孩子互動時，孩子一般都不看您的示範或不聽大人的說明嗎？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    if utterance == "長[一點]就不[會]講":
        if CHATBOT_MODE:
            resultDICT["response"] = "了解...對了，當您和孩子互動時，孩子一般都不看您的示範或不聽大人的說明嗎？"
            resultDICT["q6"] = True
        else:
            # write your code here
            pass

    return resultDICT