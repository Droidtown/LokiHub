#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Adult

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""
from ArticutAPI import ArticutAPI
articut = ArticutAPI.Articut()

DEBUG_Adult = True
userDefinedDICT = {"大": ["大人", "成人"], "小": ["小孩", "孩童"]}

def amountSTRConvert(inputSTR):
    resultDICT={}
    resultDICT = articut.parse(inputSTR, level="lv3")
    return resultDICT['number']

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Adult:
        print("[Adult] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[三]大[一]小":
        # write your code here
        resultDICT['adultAmount'] = amountSTRConvert(args[0])[args[0]]
        pass

    if utterance == "[三]小[一]大":
        # write your code here
        resultDICT['adultAmount'] = amountSTRConvert(args[1])[args[1]]
        pass

    if utterance == "[三個]大人":
        # write your code here
        resultDICT['adultAmount'] = amountSTRConvert(args[0][0])[args[0][0]]
        pass

    if utterance == "[三個]大人[兩個]小孩":
        # write your code here
        resultDICT['adultAmount'] = amountSTRConvert(args[0][0])[args[0][0]]
        pass

    if utterance == "[三個]小孩[一個]大人":
        # write your code here
        resultDICT['adultAmount'] = amountSTRConvert(args[1][0])[args[1][0]]
        pass

    if utterance == "[兩]大":
        # write your code here
        resultDICT['adultAmount'] = amountSTRConvert(args[0])[args[0]]
        pass

    if utterance == "[兩張]全票":
        # write your code here
        resultDICT['adultAmount'] = amountSTRConvert(args[0][0])[args[0][0]]
        pass

    if utterance == "[兩張]成人票":
        # write your code here
        resultDICT['adultAmount'] = amountSTRConvert(args[0][0])[args[0][0]]
        pass

    return resultDICT