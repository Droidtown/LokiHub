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
    userDefinedDICT = {"_veg":["地瓜","地瓜葉","青江菜"],"_food":["水煮蛋","白帶魚","紅棗","紅蘿蔔","白果","日本馬頭魚"],"_temp":["產季","盛產季"],"_fruit":["哈密瓜","火龍果","藍莓"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_recipe:
        print("[recipe] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我]想知道[蘋果][相關]的料理":
        # write your code here
        pass

    if utterance == "[我]想知道[蘋果][能]做什麼料理":
        # write your code here
        pass

    if utterance == "[梨子]的做法":
        # write your code here
        pass

    if utterance == "[烏魚子][可以]怎麼做":
        # write your code here
        pass

    if utterance == "[皮蛋][可以]用烤的嗎":
        # write your code here
        pass

    if utterance == "[紅棗][可以]做什麼":
        # write your code here
        pass

    if utterance == "[紅棗]有甚麼料理":
        # write your code here
        pass

    if utterance == "[紅蘿蔔][可以]幹嘛":
        # write your code here
        pass

    if utterance == "[芭樂][可以]做成什麼":
        # write your code here
        pass

    if utterance == "[芭樂][可以]做成什麼料理":
        # write your code here
        pass

    if utterance == "[芭樂][該]怎麼弄":
        # write your code here
        pass

    if utterance == "[芭樂]怎麼吃":
        # write your code here
        pass

    if utterance == "[芭樂]有甚麼做法":
        # write your code here
        pass

    if utterance == "[芭樂]要怎麼弄":
        # write your code here
        pass

    if utterance == "[葡萄][該]怎麼料理":
        # write your code here
        pass

    if utterance == "[葡萄][該]怎麼處理":
        # write your code here
        pass

    if utterance == "[葡萄]有什麼料理方式":
        # write your code here
        pass

    if utterance == "[藍莓]的作法":
        # write your code here
        pass

    if utterance == "[蘋果][相關]的料理":
        # write your code here
        pass

    if utterance == "[香菇]有甚麼作法":
        # write your code here
        pass

    if utterance == "[香蕉]怎麼處理":
        # write your code here
        pass

    if utterance == "請問[烏魚子][該]怎麼料理":
        # write your code here
        pass

    return resultDICT