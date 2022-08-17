#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for taboo

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
import os

DEBUG_taboo = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_fruit":["火龍果"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_taboo:
        print("[taboo] {} ===> {}".format(inputSTR, utterance))


def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    resultDICT["taboo"] = True

    if utterance == "[杏仁] 禁忌":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "[杏仁][可以]跟什麼[一起]吃":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "[杏仁]不[可以]跟什麼[一起]吃":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "[杏仁]的食用禁忌有哪些":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "[杏仁]與什麼食物相剋？":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "[杏仁]跟什麼不[能][一起]吃":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "[杏仁]跟什麼相剋":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "[螃蟹]跟[柿子][可以][一起]吃嗎":
        resultDICT["ingredient"] = args[0]
        resultDICT["ingredient_2"] = args[1]
        # write your code here
        pass

    if utterance == "和[杏仁]相剋的食物有哪些":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "[芭樂]有什麼禁忌":
        resultDICT["ingredient"] = args[0]

    if utterance == "[芭樂]有什麼食用禁忌":
        resultDICT["ingredient"] = args[0]

    if utterance == "有什麼禁忌":
        # write your code here
        pass

    return resultDICT
