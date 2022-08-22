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
    userDefinedDICT = {"_veg":["地瓜","地瓜葉","青江菜"],"_food":["水煮蛋","白帶魚","紅棗","紅蘿蔔","白果","日本馬頭魚"],"_temp":["產季","盛產季"],"_fruit":["哈密瓜","火龍果","藍莓"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_InSeason:
        print("[InSeason] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[現在][該]吃哪些[水果]？":
        # write your code here
        pass

    if utterance == "[現在]有什麼":
        # write your code here
        pass

    if utterance == "[現在]有什麼[水果][好吃]":
        # write your code here
        pass

    if utterance == "[現在]有什麼[當季][食材]":
        # write your code here
        pass

    if utterance == "[現在]有甚麼[好吃]的[當季][水果]":
        # write your code here
        pass

    if utterance == "[現在]有甚麼[海鮮]":
        # write your code here
        pass

    if utterance == "[現在]有甚麼[當季][水果][好吃]":
        # write your code here
        pass

    if utterance == "[現在]盛產什麼":
        # write your code here
        pass

    if utterance == "[現在當季]的[水果]是什麼":
        # write your code here
        pass

    if utterance == "[當季][食材]有啥":
        # write your code here
        pass

    if utterance == "[目前]盛產甚麼[水果]":
        # write your code here
        pass

    if utterance == "告訴[我][現在]有什麼[當季][食材]":
        # write your code here
        pass

    if utterance == "有什麼[水果]":
        # write your code here
        pass

    if utterance == "有什麼[當季][食材]":
        # write your code here
        pass

    return resultDICT