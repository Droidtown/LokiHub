#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for CheckInSeason

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

DEBUG_CheckInSeason = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_fruit":["火龍果"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_CheckInSeason:
        print("[CheckInSeason] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT, all_utt):
    debugInfo(inputSTR, utterance)
    
    resultDICT["check"] = True
    
    if utterance == "[烏魚子]是[當季]食材嗎":
        resultDICT["ingredient"] = args[0]

    if utterance == "[烏魚子]是不[是][當季]食材？":
        resultDICT["ingredient"] = args[0]

    if utterance == "[葡萄]是[當季]水果嗎":
        resultDICT["ingredient"] = args[0]

    if utterance == "[葡萄]是不[是][當季]的":
        resultDICT["ingredient"] = args[0]

    return resultDICT