#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for departure

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_departure = True
userDefinedDICT = {"大": ["大人", "成人"], "小": ["小孩", "孩童"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_departure:
        print("[departure] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[台北]出發":
        # write your code here
        resultDICT['departure'] = args[0]
        pass

    if utterance == "[台北]去台南":
        # write your code here
        resultDICT['departure'] = args[0]
        pass

    if utterance == "[新竹]到台北":
        # write your code here
        resultDICT['departure'] = args[0]
        pass

    if utterance == "[新竹]往台北":
        # write your code here
        resultDICT['departure'] = args[0]
        pass

    if utterance == "從[台北]":
        # write your code here
        if "從{}".format(args[0]) in inputSTR:
            resultDICT['departure'] = args[0]
        pass

    return resultDICT