#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for reject

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

DEBUG_reject = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_fruit":["火龍果"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_reject:
        print("[reject] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    resultDICT["reject"] = True

    if utterance == "[可以]說[點][別]的嗎？":
        # write your code here
        pass

    if utterance == "[我]不喜歡[芭樂]":
        resultDICT["ingredient"] = args[1]

    if utterance == "[我]不想吃[芭樂]":
        resultDICT["ingredient"] = args[1]

    if utterance == "不要讓[我]看到[芭樂]！":
        resultDICT["ingredient"] = args[1]

    if utterance == "再來[點][別]的？":
        # write your code here
        pass

    if utterance == "有沒[有][別]的":
        # write your code here
        pass

    if utterance == "還推薦什麼":
        # write your code here
        pass

    if utterance == "還有什麼？":
        # write your code here
        pass

    if utterance == "還有嗎？":
        # write your code here
        pass

    if utterance == "[也]不喜歡":
        # write your code here
        pass

    if utterance == "[我]討厭[水蜜桃]":
        resultDICT["ingredient"] = args[1]

    return resultDICT