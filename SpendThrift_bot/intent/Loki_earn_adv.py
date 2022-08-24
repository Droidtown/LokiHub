#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for earn_adv

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

DEBUG_earn_adv = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_key":["收入","支出","記帳狀況"],"_park":["六福村","九族文化村","義大","義大世界"],"money":["支出總額","支出費用","總金額","總額","費用","金錢","錢"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_earn_adv:
        print("[earn_adv] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "去全聯收入3000":
        # write your code here
        pass

    if utterance == "去全聯賺了3000":
        # write your code here
        pass

    if utterance == "去六福村收入3000":
        # write your code here
        pass

    if utterance == "去六福村賺了3000":
        # write your code here
        pass

    if utterance == "去台北收入3000":
        # write your code here
        pass

    if utterance == "去台北賺了3000":
        # write your code here
        pass

    if utterance == "收入3000":
        # write your code here
        pass

    if utterance == "昨天去全聯收入3000":
        # write your code here
        pass

    if utterance == "昨天去全聯賺了3000":
        # write your code here
        pass

    if utterance == "昨天在六福村收入3000":
        # write your code here
        pass

    if utterance == "昨天在六福村賺了3000":
        # write your code here
        pass

    if utterance == "昨天在台北收入3000":
        # write your code here
        pass

    if utterance == "昨天在台北賺了3000":
        # write your code here
        pass

    if utterance == "昨天收入3000":
        # write your code here
        pass

    if utterance == "昨天賺了3000":
        # write your code here
        pass

    if utterance == "賺了3000":
        # write your code here
        pass

    return resultDICT