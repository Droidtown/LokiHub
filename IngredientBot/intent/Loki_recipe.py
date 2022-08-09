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

def getResult(inputSTR, utterance, args, resultDICT):
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

    return resultDICT