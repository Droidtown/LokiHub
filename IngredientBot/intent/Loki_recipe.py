#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for recipe

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

DEBUG_recipe = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_fruit":["火龍果"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_recipe:
        print("[recipe] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT, all_utt):
    debugInfo(inputSTR, utterance)

    resultDICT["recipe"] = True

    if utterance == "[我]想知道[蘋果][相關]的料理":
        resultDICT["ingredient"] = args[1]

    if utterance == "[我]想知道[蘋果][能]做什麼料理":
        resultDICT["ingredient"] = args[1]

    if utterance == "[烏魚子][可以]怎麼做":
        resultDICT["ingredient"] = args[0]

    if utterance == "[皮蛋][可以]用烤的嗎":
        resultDICT["ingredient"] = args[0]

    if utterance == "[芭樂] 料理":
        resultDICT["ingredient"] = args[0]

    if utterance == "[芭樂][可以]做成什麼":
        resultDICT["ingredient"] = args[0]

    if utterance == "[芭樂][可以]做成什麼料理":
        resultDICT["ingredient"] = args[0]

    if utterance == "[芭樂][該]怎麼弄":
        resultDICT["ingredient"] = args[0]

    if utterance == "[芭樂]要怎麼弄":
        resultDICT["ingredient"] = args[0]

    if utterance == "[蘋果][相關]的料理":
        resultDICT["ingredient"] = args[0]

    if utterance == "請問[烏魚子][該]怎麼料理":
        resultDICT["ingredient"] = args[0]

    if utterance == "[芭樂]有甚麼做法":
        resultDICT["ingredient"] = args[0]

    if utterance == "[葡萄][該]怎麼料理":
        resultDICT["ingredient"] = args[0]

    if utterance == "[葡萄][該]怎麼處理":
        resultDICT["ingredient"] = args[0]

    if utterance == "[葡萄]有什麼料理方式":
        resultDICT["ingredient"] = args[0]

    if utterance == "[香菇]有甚麼作法":
        resultDICT["ingredient"] = args[0]

    if utterance == "[香蕉]怎麼處理":
        resultDICT["ingredient"] = args[0]

    if utterance == "[芭樂]怎麼吃":
        resultDICT["ingredient"] = args[0]

    if utterance == "[藍莓]的作法":
        resultDICT["ingredient"] = args[0]

    if utterance == "[紅棗][可以]做什麼":
        resultDICT["ingredient"] = args[0]

    if utterance == "[紅棗]有甚麼料理":
        resultDICT["ingredient"] = args[0]

    if utterance == "[紅蘿蔔][可以]幹嘛":
        resultDICT["ingredient"] = args[0]

    if utterance == "[梨子]的做法":
        resultDICT["ingredient"] = args[0]

    if utterance == "[他][能]做什麼":
        # write your code here
        pass

    if utterance == "有什麼[大白菜]的料理":
        resultDICT["ingredient"] = args[0]

    if utterance == "有甚麼[紫甘藍]的作法":
        resultDICT["ingredient"] = args[0]

    if utterance == "有甚麼[紫甘藍]的做法":
        resultDICT["ingredient"] = args[0]

    if utterance == "有甚麼料理":
        # write your code here
        pass

    return resultDICT