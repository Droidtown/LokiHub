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
    userDefinedDICT = {"_fruit":["火龍果"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_price:
        print("[price] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT, all_utt):
    debugInfo(inputSTR, utterance)

    resultDICT["price"] = True

    if utterance == "[一塊][肉]怎麼賣":
        resultDICT["ingredient"] = args[1]
    
    if utterance == "[一條][魚]多少錢":
        resultDICT["ingredient"] = args[1]
        
    if utterance == "[一盒][蛋]多少":
        resultDICT["ingredient"] = args[1]
        
    if utterance == "[我]想買[一盒][蛋]需要帶多少錢":
        resultDICT["ingredient"] = args[2]
        
    if utterance == "[我]要買[一盒][皮蛋]":
        resultDICT["ingredient"] = args[2]
        
    if utterance == "[現在][一條][白鯧]的價格是多少":
        resultDICT["ingredient"] = args[2]
        
    if utterance == "[現在][一盒][皮蛋]要多少錢":
        resultDICT["ingredient"] = args[2]
        
    if utterance == "[瘦肉][一斤]多少錢":
        resultDICT["ingredient"] = args[0]
        
    if utterance == "[皮蛋]多少錢":
        resultDICT["ingredient"] = args[0]

    if utterance == "[蘋果]怎麼賣":
        resultDICT["ingredient"] = args[0]

    if utterance == "請告訴[我][一盒][蛋]多少錢":
        resultDICT["ingredient"] = args[2]
        
    if utterance == "[芭樂]賣多少":
        resultDICT["ingredient"] = args[0]

    if utterance == "[菠菜][一把]多少錢":
        resultDICT["ingredient"] = args[0]

    if utterance == "[葡萄][現在]多少錢":
        resultDICT["ingredient"] = args[0]

    if utterance == "多少錢":
        # write your code here
        pass

    if utterance == "[蛤蠣]價錢":
        resultDICT["ingredient"] = args[0]

    if utterance == "[螃蟹]價格高嗎":
        resultDICT["ingredient"] = args[0]

    if utterance == "[高麗菜]的價格":
        resultDICT["ingredient"] = args[0]

    return resultDICT