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
    userDefinedDICT = {"_veg":["地瓜","地瓜葉","青江菜"],"_food":["水煮蛋","白帶魚","紅棗","紅蘿蔔","白果","日本馬頭魚"],"_temp":["產季","盛產季"],"_fruit":["哈密瓜","火龍果","藍莓"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_CheckInSeason:
        print("[CheckInSeason] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[烏魚子]是[當季]食材嗎":
        # write your code here
        pass

    if utterance == "[烏魚子]是不[是][當季]食材？":
        # write your code here
        pass

    if utterance == "[葡萄]是[當季]水果嗎":
        # write your code here
        pass

    if utterance == "[葡萄]是不[是][當季]的":
        # write your code here
        pass

    return resultDICT