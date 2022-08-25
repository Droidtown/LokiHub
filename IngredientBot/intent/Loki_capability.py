#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for capability

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

DEBUG_capability = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_veg":["青江菜","地瓜葉","地瓜"],"_food":["水煮蛋","紅棗","白帶魚"],"_fruit":["火龍果","哈密瓜","藍莓"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_capability:
        print("[capability] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT, all_utt):
    debugInfo(inputSTR, utterance)

    resultDICT["capability"] = True

    if utterance == "[你][可以]幫[我]做什麼":
        # write your code here
        pass

    if utterance == "[你][可以]幫[我]解決什麼問題":
        # write your code here
        pass

    if utterance == "[你]知道什麼":
        # write your code here
        pass

    if utterance == "那[可以]問什麼":
        # write your code here
        pass

    if utterance == "[你][可以]回答什麼問題":
        # write your code here
        pass

    if utterance == "[我][可以]問[你]什麼":
        # write your code here
        pass

    if utterance == "那[我]還[可以]問什麼":
        # write your code here
        pass

    if utterance == "那[你]還[會]什麼":
        # write your code here
        pass

    return resultDICT