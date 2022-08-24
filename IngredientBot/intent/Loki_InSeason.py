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

def getResult(inputSTR, utterance, args, resultDICT, all_utt):
    debugInfo(inputSTR, utterance)
    
    resultDICT["inseason"] = True

    if utterance == "[現在][該]吃哪些[水果]？":
        resultDICT["time"] = args[0]
        resultDICT["type"] = args[2]

    if utterance == "[現在]有什麼":
        resultDICT["time"] = args[0]

    if utterance == "[現在]有什麼[水果][好吃]":
        resultDICT["time"] = args[0]
        resultDICT["type"] = args[1]

    if utterance == "[現在]有什麼[當季][食材]":
        resultDICT["time"] = args[0]
        resultDICT["type"] = args[2]

    if utterance == "[現在]有甚麼[好吃]的[當季][水果]":
        resultDICT["time"] = args[0]
        resultDICT["type"] = args[3]

    if utterance == "[現在]有甚麼[海鮮]":
        resultDICT["time"] = args[0]
        resultDICT["type"] = args[1]

    if utterance == "[現在]有甚麼[當季][水果][好吃]":
        resultDICT["time"] = args[0]
        resultDICT["type"] = args[2]

    if utterance == "[現在當季]的[水果]是什麼":
        resultDICT["time"] = args[0]
        resultDICT["type"] = args[1]

    if utterance == "[目前]盛產甚麼[水果]":
        resultDICT["time"] = args[0]
        resultDICT["type"] = args[1]

    if utterance == "告訴[我][現在]有什麼[當季][食材]":
        resultDICT["time"] = args[1]
        resultDICT["type"] = args[3]

    if utterance == "有什麼[水果]":
        if '有什麼禁忌' in all_utt:
            resultDICT.pop("inseason")
        elif "[芭樂]有什麼禁忌" in all_utt:
            resultDICT.pop("inseason")
        elif "[紅棗]有甚麼料理" in all_utt:
            resultDICT.pop("inseason")
        elif "[葡萄]有什麼料理方式" in all_utt:
            resultDICT.pop("inseason")
        elif "有甚麼[紫甘藍]的作法" in all_utt:
            resultDICT.pop("inseason")
        elif "有甚麼料理" in all_utt:
            resultDICT.pop("inseason")
        else:
            resultDICT["type"] = args[0]

    if utterance == "有什麼[當季][食材]":
        resultDICT["type"] = args[1]

    if utterance == "[現在]盛產什麼":
        resultDICT["time"] = args[0]

    if utterance == "[當季][食材]有啥":

        if "[現在]的[當季][食材]有哪些" in all_utt:
            resultDICT.pop("inseason")
        elif "[你]知道[七月]的[當令][食材]有哪些嗎" in all_utt:
            resultDICT.pop("inseason")
        elif "[我]想知道[三月]的[當令][食材]有哪些" in all_utt:
            resultDICT.pop("inseason")
        else:
            resultDICT["time"] = args[0]
            resultDICT["type"] = args[1]

    return resultDICT