#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for accept

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

DEBUG_accept = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_veg":["地瓜","地瓜葉","青江菜"],"_food":["水煮蛋","白帶魚","紅棗"],"_fruit":["哈密瓜","火龍果","藍莓"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_accept:
        print("[accept] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    #resultDICT["accept"] = True

    if utterance == "Ok":
        # write your code here
        pass

    if utterance == "了解":
        # write your code here
        pass

    if utterance == "好哦":
        # write your code here
        pass

    if utterance == "沒問題":
        # write your code here
        pass

    if utterance == "[可以]":
        # write your code here
        pass

    if utterance == "喜歡":
        # write your code here
        pass

    return resultDICT