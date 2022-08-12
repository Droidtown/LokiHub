#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for selection

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

DEBUG_selection = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_fruit":["火龍果"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_selection:
        print("[selection] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    resultDICT["selection"] = True

    if utterance == "[山藥]如何挑選[才][好吃]？":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "[新鮮][肉品]怎麼挑？":
        resultDICT["ingredient"] = args[1]
        # write your code here
        pass

    if utterance == "[火龍果][表皮]有[皺褶][正常]嗎？":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "[肉類]如何挑選？":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "[茄子]挑選[方法]":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "[青椒]怎麼看？":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "[馬鈴薯][軟][一點]好還是[硬][一點][好]？":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "[馬鈴薯]是[軟]的好還是[硬]的[好]？":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "什麼樣的[芭樂][比較好吃]？":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "如何區分[新鮮]與不[新鮮]的[魚]?":
        resultDICT["ingredient"] = args[2]
        # write your code here
        pass

    if utterance == "如何挑選[新鮮][肉品]？":
        resultDICT["ingredient"] = args[1]
        # write your code here
        pass

    if utterance == "怎麼挑[山藥]？":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "要怎麼選[芭樂]？":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "買[茄子]如何挑選？":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "[番茄]怎麼買":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    if utterance == "[西瓜]的選法":
        resultDICT["ingredient"] = args[0]
        # write your code here
        pass

    return resultDICT
