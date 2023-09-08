#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for function_of_4_objects

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

DEBUG_function_of_4_objects = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_function_of_4_objects.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_function_of_4_objects:
        print("[function_of_4_objects] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[不常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR: #去reply裡面抓引導用問題
                resultDICT["response"] = getResponse(utterance, args)
            elif "常常" in inputSTR:
                resultDICT["response"] = "哦...是哦...那您的孩子可以理解並正確回應含有方位詞的句子嗎？例如：指出在樹下的小鳥？"
                resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[不行]":
        if CHATBOT_MODE:
            resultDICT["response"] = "哦...是哦...那您的孩子可以理解並正確回應含有方位詞的句子嗎？例如：指出在樹下的小鳥？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "[只]聽過[一兩][次]":
        if CHATBOT_MODE:
            resultDICT["response"] = "哦...是哦...那您的孩子可以理解並正確回應含有方位詞的句子嗎？例如：指出在樹下的小鳥？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "[可以]但[不多]":
        if CHATBOT_MODE:
            resultDICT["response"] = "哦...是哦...那您的孩子可以理解並正確回應含有方位詞的句子嗎？例如：指出在樹下的小鳥？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "[可以]但沒那麼多[種]":
        if CHATBOT_MODE:
            resultDICT["response"] = "哦...是哦...那您的孩子可以理解並正確回應含有方位詞的句子嗎？例如：指出在樹下的小鳥？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "[會]但不到[4個]":
        if CHATBOT_MODE:
            resultDICT["response"] = "哦...是哦...那您的孩子可以理解並正確回應含有方位詞的句子嗎？例如：指出在樹下的小鳥？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "[會]但不愛說":
        if CHATBOT_MODE:
            resultDICT["response"] = "哦...是哦...那您的孩子可以理解並正確回應含有方位詞的句子嗎？例如：指出在樹下的小鳥？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但不愛講":
        if CHATBOT_MODE:
            resultDICT["response"] = "哦...是哦...那您的孩子可以理解並正確回應含有方位詞的句子嗎？例如：指出在樹下的小鳥？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "[都][可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "哦...是哦...那您的孩子可以理解並正確回應含有方位詞的句子嗎？例如：指出在樹下的小鳥？"
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

    if utterance == "好像[可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "哦...是哦...那您的孩子可以理解並正確回應含有方位詞的句子嗎？例如：指出在樹下的小鳥？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "好像不[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "哦...是哦...那您的孩子可以理解並正確回應含有方位詞的句子嗎？例如：指出在樹下的小鳥？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "很少":
        if CHATBOT_MODE:
            if "多" in inputSTR:
                resultDICT["response"] = "哦...是哦...那您的孩子可以理解並正確回應含有方位詞的句子嗎？例如：指出在樹下的小鳥？"
                resultDICT["q3"] = True
            elif "少" in inputSTR:  #去reply裡面抓引導用問題
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有而且超過[四個]":
        if CHATBOT_MODE:
            resultDICT["response"] = "哦...是哦...那您的孩子可以理解並正確回應含有方位詞的句子嗎？例如：指出在樹下的小鳥？"
            resultDICT["q3"] = True
        else:
            # write your code here
            pass

    if utterance == "沒聽過":
        if CHATBOT_MODE:
            resultDICT["response"] = "哦...是哦...那您的孩子可以理解並正確回應含有方位詞的句子嗎？例如：指出在樹下的小鳥？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "沒辦法":
        if CHATBOT_MODE:
            resultDICT["response"] = "哦...是哦...那您的孩子可以理解並正確回應含有方位詞的句子嗎？例如：指出在樹下的小鳥？"
            resultDICT["q3"] = False
        else:
            # write your code here
            pass

    if utterance == "要看是什麼樣的[東西]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT