#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Probe

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Probe = True
userDefinedDICT = {"D": ["設計", "d"], "I": ["發明", "i"], "M": ["新型", "m"], "G06Q_020_24": ["信用方案", "信用", "後付", "pay after", "24"], "G06Q_020_26": ["轉帳方案", "轉帳", "現付", "pay now", "26"], "G06Q_020_28": ["預付方案", "預付", "pay before", "28"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Probe:
        print("[Probe] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "不是":
        if len(inputSTR) < 3:
            resultDICT["confirm"] = False
        pass

    if utterance == "對":
        if len(inputSTR) < 3:
            if "不" in inputSTR:
                resultDICT["confirm"] = False
            else:
                resultDICT["confirm"] = True        
            pass

    if utterance == "是":
        if len(inputSTR) < 2:
            resultDICT["confirm"] = True        
        pass

    if utterance == "沒錯":
        if len(inputSTR) < 3:
            resultDICT["confirm"] = True
        pass

    return resultDICT