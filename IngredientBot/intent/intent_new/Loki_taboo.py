#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for taboo

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

DEBUG_taboo = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_veg":["地瓜","地瓜葉","青江菜"],"_food":["水煮蛋","白帶魚","紅棗","紅蘿蔔","白果","日本馬頭魚"],"_temp":["產季","盛產季"],"_fruit":["哈密瓜","火龍果","藍莓"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_taboo:
        print("[taboo] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[杏仁] 禁忌":
        # write your code here
        pass

    if utterance == "[杏仁][可以]跟什麼[一起]吃":
        # write your code here
        pass

    if utterance == "[杏仁]不[可以]跟什麼[一起]吃":
        # write your code here
        pass

    if utterance == "[杏仁]的食用禁忌有哪些":
        # write your code here
        pass

    if utterance == "[杏仁]與什麼食物相剋？":
        # write your code here
        pass

    if utterance == "[杏仁]跟什麼不[能][一起]吃":
        # write your code here
        pass

    if utterance == "[杏仁]跟什麼相剋":
        # write your code here
        pass

    if utterance == "[芭樂]有什麼禁忌":
        # write your code here
        pass

    if utterance == "[芭樂]有什麼食用禁忌":
        # write your code here
        pass

    if utterance == "[螃蟹]跟[柿子][可以][一起]吃嗎":
        # write your code here
        pass

    if utterance == "和[杏仁]相剋的食物有哪些":
        # write your code here
        pass

    if utterance == "有什麼禁忌":
        # write your code here
        pass

    return resultDICT