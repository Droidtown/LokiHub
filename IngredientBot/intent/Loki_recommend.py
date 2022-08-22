#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for recommend

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

DEBUG_recommend = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_veg":["地瓜","地瓜葉","青江菜"],"_food":["水煮蛋","白帶魚","紅棗"],"_fruit":["哈密瓜","火龍果","藍莓"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_recommend:
        print("[recommend] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT, all_utt):
    debugInfo(inputSTR, utterance)

    resultDICT["recommend"] = True

    if utterance == "[今天][晚餐]吃什麼":
        # write your code here
        pass

    if utterance == "[今天晚上]吃什麼":
        # write your code here
        pass

    if utterance == "推薦吃什麼":
        # write your code here
        pass

    if utterance == "推薦[一道]料理":
        # write your code here
        pass

    if utterance == "推薦[一道]料理給[我]":
        # write your code here
        pass

    return resultDICT