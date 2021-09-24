#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for restaurant_price

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_restaurant_price = True
userDefinedDICT = {"房間": ["房"], "旅館": ["青年旅館", "飯店", "休息處", "住宿處", "休息的地方"], "預定": ["預約", "訂位", "預訂"], "餐廳": ["餐館", "店家", "吃飯的地方", "吃飯處", "店"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_restaurant_price:
        print("[restaurant_price] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    resultDICT["res_price"] = None   #初始狀態
    debugInfo(inputSTR, utterance)
    if utterance == "吃這家[店][大概]要花多少":
        if "花多少" in inputSTR:
            resultDICT["res_price"] = "request"
        pass

    if utterance == "這家[店][會]貴嗎":
        resultDICT["res_price"] = "request"
        pass

    if utterance == "這間[餐廳]價位多少":
        if "{}價位".format(args[0]) in inputSTR:
            resultDICT["res_price"] = "request"
        pass

    if utterance == "這間[餐廳]的低銷是多少":
        if "低銷" in inputSTR:
            resultDICT["res_price"] = "request"
        pass

    if utterance == "這間[餐廳][大概]要花多少":
        if "花多少" in inputSTR:
            resultDICT["res_price"] = "request"
        pass

    if utterance == "吃這間要花多少錢":
        if "花多少" in inputSTR:
            resultDICT["res_price"] = "request"
        pass

    if utterance == "這家[店]平均花費多少":
        if "花費" in inputSTR:
            resultDICT["res_price"] = "request"
        pass

    if utterance == "這間[大概]要花多少":
        if "花多少" in inputSTR:
            resultDICT["res_price"] = "request"
        pass

    return resultDICT