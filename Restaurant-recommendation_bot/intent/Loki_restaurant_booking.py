#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for restaurant_booking

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""
from ArticutAPI import Articut
articut = Articut()

DEBUG_restaurant_booking = True
userDefinedDICT = {"房間": ["房"], "旅館": ["青年旅館", "飯店", "休息處", "住宿處", "休息的地方"], "預定": ["預約", "訂位", "預訂"], "餐廳": ["餐館", "店家", "吃飯的地方", "吃飯處", "店"]}

def amountSTRConvert(inputSTR):
    resultDICT={}
    resultDICT = articut.parse(inputSTR=inputSTR, level="lv3")
    return resultDICT['number']
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_restaurant_booking:
        print("[restaurant_booking] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[五]人位子":
        resultDICT["res_person"] = [amountSTRConvert(args[0])[args[0]]]
        pass


    if utterance == "[我]要預約[8]人的":
        resultDICT["res_person"] = [amountSTRConvert(args[1])[args[1]]]
        pass

    if utterance == "[我]要預訂[三]人位子":
        resultDICT["res_person"] = [amountSTRConvert(args[1])[args[1]]]
        pass


    if utterance == "[我們]有[5]人":
        resultDICT["res_person"] = [amountSTRConvert(args[1])[args[1]]]
        pass

    if utterance == "預約[2]人的位子":
        resultDICT["res_person"] = [amountSTRConvert(args[0])[args[0]]]
        pass

    if utterance == "[10位]":
        resultDICT["res_person"] = [amountSTRConvert(args[0])[args[0]]]
        pass

    if utterance == "[全部][共][25位]":
        resultDICT["res_person"] = [amountSTRConvert(args[2])[args[2]]]
        pass

    if utterance == "[我們]有[十位]":
        resultDICT["res_person"] = [amountSTRConvert(args[1])[args[1]]]
        pass

    if utterance == "有[3位]":
        resultDICT["res_person"] = [amountSTRConvert(args[0])[args[0]]]
        pass

    if utterance == "總共[十一位]":
        resultDICT["res_person"] = [amountSTRConvert(args[0])[args[0]]]
        pass

    if utterance == "[我們]有[5位]":
        resultDICT["res_person"] = [amountSTRConvert(args[1])[args[1]]]
        pass

    if utterance == "共[八位]":
        resultDICT["res_person"] = [amountSTRConvert(args[1])[args[1]]]
        pass

    return resultDICT