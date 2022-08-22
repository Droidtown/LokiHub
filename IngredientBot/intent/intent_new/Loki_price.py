#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for price

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

DEBUG_price = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_veg":["地瓜","地瓜葉","青江菜"],"_food":["水煮蛋","白帶魚","紅棗","紅蘿蔔","白果","日本馬頭魚"],"_temp":["產季","盛產季"],"_fruit":["哈密瓜","火龍果","藍莓"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_price:
        print("[price] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一塊][肉]怎麼賣":
        # write your code here
        pass

    if utterance == "[一條][魚]多少錢":
        # write your code here
        pass

    if utterance == "[一盒][蛋]多少":
        # write your code here
        pass

    if utterance == "[我]想買[一盒][蛋]需要帶多少錢":
        # write your code here
        pass

    if utterance == "[我]要買[一盒][皮蛋]":
        # write your code here
        pass

    if utterance == "[現在][一條][白鯧]的價格是多少":
        # write your code here
        pass

    if utterance == "[現在][一盒][皮蛋]要多少錢":
        # write your code here
        pass

    if utterance == "[瘦肉][一斤]多少錢":
        # write your code here
        pass

    if utterance == "[皮蛋]多少錢":
        # write your code here
        pass

    if utterance == "[芭樂]賣多少":
        # write your code here
        pass

    if utterance == "[菠菜][一把]多少錢":
        # write your code here
        pass

    if utterance == "[葡萄][現在]多少錢":
        # write your code here
        pass

    if utterance == "[蘋果]怎麼賣":
        # write your code here
        pass

    if utterance == "[蛤蠣]價錢":
        # write your code here
        pass

    if utterance == "多少錢":
        # write your code here
        pass

    if utterance == "請告訴[我][一盒][蛋]多少錢":
        # write your code here
        pass

    return resultDICT