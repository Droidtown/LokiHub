#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for destination

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_destination = True
userDefinedDICT = {"大": ["大人", "成人"], "小": ["小孩", "孩童"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_destination:
        print("[destination] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "到[台北]":
        # write your code here
        if "到{}".format(args[0]) in inputSTR:
            resultDICT['destination'] = args[0]
        pass

    if utterance == "去[台北]":
        # write your code here
        if "去{}".format(args[0]) in inputSTR:
            resultDICT['destination'] = args[0]
        pass

    if utterance == "往[台北]":
        # write your code here
        if "往{}".format(args[0]) in inputSTR:
            resultDICT['destination'] = args[0]
        pass

    if utterance == "回[台北]":
        if "回{}".format(args[0]) in inputSTR:
            resultDICT['destination'] = args[0]
        pass
    return resultDICT