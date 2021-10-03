#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for hotel_eva

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_hotel_eva = True
userDefinedDICT = {"房間": ["房"], "旅館": ["青年旅館", "飯店", "休息處", "住宿處", "休息的地方"], "預定": ["預約", "訂位", "預訂"], "餐廳": ["餐館", "店家", "吃飯的地方", "吃飯處", "店"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_hotel_eva:
        print("[hotel_eva] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "這家[旅館]好嗎?":
        # write your code here
        pass

    if utterance == "這間[旅館]好嗎?":
        # write your code here
        pass

    if utterance == "這間[旅館]評價如何?":
        # write your code here
        pass

    if utterance == "那這間[旅館][大家]推薦嗎":
        # write your code here
        pass

    return resultDICT