#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for restaurant_eva

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_restaurant_eva = True
userDefinedDICT = {"房間": ["房"], "旅館": ["青年旅館", "飯店", "休息處", "住宿處", "休息的地方"], "預定": ["預約", "訂位", "預訂"], "餐廳": ["餐館", "店家", "吃飯的地方", "吃飯處", "店"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_restaurant_eva:
        print("[restaurant_eva] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    resultDICT["res_eva"] = None    #初始狀態
    debugInfo(inputSTR, utterance)
    if utterance == "這[店家]好嗎":
        if "好嗎" in inputSTR:
            resultDICT["res_eva"] = "request"
        pass

    if utterance == "這家好吃嗎":
        if "好吃嗎" in inputSTR:
            resultDICT["res_eva"] = "request"
        pass

    if utterance == "這間[食物][好吃]嗎":
        if "好吃嗎" in inputSTR:
            resultDICT["res_eva"] = "request"
        pass

    if utterance == "這間[餐廳]評價如何":
        if "評價" in inputSTR:
            resultDICT["res_eva"] = "request"
        pass

    if utterance == "那這家[餐廳]評價如何啊":
        if "評價" in inputSTR:
            resultDICT["res_eva"] = "request"
        pass

    if utterance == "這家[店][好吃]嗎":
        if "好吃嗎" in inputSTR:
            resultDICT["res_eva"] = "request"
        pass

    if utterance == "這間評價如何":
        if "評價" in inputSTR:
            resultDICT["res_eva"] = "request"
        pass

    if utterance == "那這間評價好嗎":
        if "評價" in inputSTR:
            resultDICT["res_eva"] = "request"
        pass

    if utterance == "那這間評價怎麼樣":
        if "評價" in inputSTR:
            resultDICT["res_eva"] = "request"
        pass

    return resultDICT