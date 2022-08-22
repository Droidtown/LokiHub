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
    userDefinedDICT = {"_veg":["地瓜","地瓜葉","青江菜"],"_food":["水煮蛋","白帶魚","紅棗","紅蘿蔔","白果","日本馬頭魚"],"_temp":["產季","盛產季"],"_fruit":["哈密瓜","火龍果","藍莓"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_selection:
        print("[selection] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[山藥]如何挑選[才][好吃]？":
        # write your code here
        pass

    if utterance == "[新鮮][肉品]怎麼挑？":
        # write your code here
        pass

    if utterance == "[李子]挑法":
        # write your code here
        pass

    if utterance == "[火龍果][表皮]有[皺褶][正常]嗎？":
        # write your code here
        pass

    if utterance == "[番茄]怎麼買":
        # write your code here
        pass

    if utterance == "[肉類]如何挑選？":
        # write your code here
        pass

    if utterance == "[茄子]挑選[方法]":
        # write your code here
        pass

    if utterance == "[西瓜]的選法":
        # write your code here
        pass

    if utterance == "[青椒]怎麼看？":
        # write your code here
        pass

    if utterance == "[馬鈴薯][軟][一點]好還是[硬][一點][好]？":
        # write your code here
        pass

    if utterance == "[馬鈴薯]是[軟]的好還是[硬]的[好]？":
        # write your code here
        pass

    if utterance == "什麼樣的[芭樂][比較好吃]？":
        # write your code here
        pass

    if utterance == "如何區分[新鮮]與不[新鮮]的[魚]?":
        # write your code here
        pass

    if utterance == "如何挑選[新鮮][肉品]？":
        # write your code here
        pass

    if utterance == "怎麼挑":
        # write your code here
        pass

    if utterance == "怎麼挑[山藥]？":
        # write your code here
        pass

    if utterance == "要怎麼選[芭樂]？":
        # write your code here
        pass

    if utterance == "買[茄子]如何挑選？":
        # write your code here
        pass

    return resultDICT