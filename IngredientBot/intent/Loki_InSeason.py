#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for InSeason

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

DEBUG_InSeason = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_fruit":["火龍果"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_InSeason:
        print("[InSeason] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):

    resultDICT["inseason"] = True

    debugInfo(inputSTR, utterance)
    if utterance == "[現在][該]吃哪些水果？":
        # write your code here
        pass

    if utterance == "[現在]有什麼":
        # write your code here
        pass

    if utterance == "[現在]有什麼[當季]食材":
        # write your code here
        pass

    if utterance == "[現在]有什麼水果[好吃]":
        # write your code here
        pass

    if utterance == "[現在]有甚麼[好吃]的[當季]水果":
        # write your code here
        pass

    if utterance == "[現在]有甚麼[當季]水果[好吃]":
        # write your code here
        pass

    if utterance == "[現在]有甚麼海鮮":
        # write your code here
        pass

    if utterance == "[現在當季][食材]有哪些":
        # write your code here
        pass

    if utterance == "[現在當季]的水果是什麼":
        # write your code here
        pass

    if utterance == "[目前]盛產甚麼水果":
        # write your code here
        pass

    if utterance == "告訴[我][現在]有什麼[當季]食材":
        # write your code here
        pass

    if utterance == "[今天晚上]吃什麼":
        # write your code here
        pass

    if utterance == "[當季]食材有什麼":
        # write your code here
        pass

    if utterance == "[今天][晚餐]吃什麼":
        # write your code here
        pass

    if utterance == "推薦吃什麼":
        # write your code here
        pass

    if utterance == "有什麼[當季]食材":
        # write your code here
        pass

    if utterance == "有什麼水果":
        # write your code here
        pass

    return resultDICT