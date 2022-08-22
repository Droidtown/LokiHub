#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for which_season

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

DEBUG_which_season = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_veg":["地瓜","地瓜葉","青江菜"],"_food":["水煮蛋","白帶魚","紅棗"],"_fruit":["哈密瓜","火龍果","藍莓"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_which_season:
        print("[which_season] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT, all_utt):
    debugInfo(inputSTR, utterance)

    resultDICT["which_season"] = True

    if utterance == "[幾月]盛產[烏魚子]":
        resultDICT["ingredient"] = args[1]
    
    if utterance == "[烏魚子]是什麼[季節]的":
        resultDICT["ingredient"] = args[0]

    if utterance == "什麼[時候]有[烏魚子]":
        resultDICT["ingredient"] = args[1]

    if utterance == "[你]知道[海膽]什麼[時候]買比較好嗎":
        resultDICT["ingredient"] = args[1]

    if utterance == "[海膽][該]什麼[時候]買":
        resultDICT["ingredient"] = args[0]

    if utterance == "[海膽]什麼[時候]買":
        resultDICT["ingredient"] = args[0]

    if utterance == "[海膽]是[幾月]產的食材":
        resultDICT["ingredient"] = args[0]

    if utterance == "[海膽]是[幾月]的[食材]":
        if "[葡萄]是[當季]水果嗎" in all_utt:
            resultDICT.pop("which_season")
        elif "[烏魚子]是[當季]食材嗎" in all_utt:
            resultDICT.pop("which_season")
        else:
            resultDICT["ingredient"] = args[0]

    if utterance == "[海膽] 盛產季":
        resultDICT["ingredient"] = args[0]

    if utterance == "[海膽]盛產季是什麼[時候]":
        resultDICT["ingredient"] = args[0]

    if utterance == "[葡萄]產季是什麼[時候]":
        resultDICT["ingredient"] = args[0]

    if utterance == "[葡萄]產季什麼[時候]":
        resultDICT["ingredient"] = args[0]

    return resultDICT