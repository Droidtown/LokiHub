#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for reserve_trigger

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_reserve_trigger = True
userDefinedDICT = {"房間": ["房"], "旅館": ["青年旅館", "飯店", "休息處", "住宿處", "休息的地方"], "預定": ["預約", "訂位", "預訂"], "餐廳": ["餐館", "店家", "吃飯的地方", "吃飯處", "店"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_reserve_trigger:
        print("[reserve_trigger] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[可以][先][預約]嗎":
        resultDICT["reserve"] = "yes"
        pass

    if utterance == "[可以][預訂][位子]嗎":
        resultDICT["reserve"] = "yes"
        pass

    if utterance == "[我]想[先][預約]":
        resultDICT["reserve"] = "yes"
        pass

    if utterance == "[我]想[預約]":
        resultDICT["reserve"] = "yes"
        pass

    if utterance == "[我]想要[預定][座位]":
        resultDICT["reserve"] = "yes"
        pass

    if utterance == "[我]想要[預約]":
        resultDICT["reserve"] = "yes"
        pass

    if utterance == "[我]要[先][預約][位子]":
        resultDICT["reserve"] = "yes"
        pass

    if utterance == "[我]要[預約]":
        resultDICT["reserve"] = "yes"
        pass

    if utterance == "[方便][預約]嗎":
        resultDICT["reserve"] = "yes"
        pass

    if utterance == "[能][預約]嗎":
        resultDICT["reserve"] = "yes"
        pass

    if utterance == "[我]想要[預定]":
        resultDICT["reserve"] = "yes"
        pass

    if utterance == "那[我]想[預約]":
        resultDICT["reserve"] = "yes"
        pass

    if utterance == "那[能][預約]嗎":
        resultDICT["reserve"] = "yes"
        pass

    return resultDICT