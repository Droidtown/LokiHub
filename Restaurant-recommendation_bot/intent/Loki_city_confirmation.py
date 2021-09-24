#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for city_confirmation

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_city_confirmation = True
userDefinedDICT = {"房間": ["房"], "旅館": ["青年旅館", "飯店", "休息處", "住宿處", "休息的地方"], "預定": ["預約", "訂位", "預訂"], "餐廳": ["餐館", "店家", "吃飯的地方", "吃飯處", "店"]}
cityDefinedDICT = {"臺中": ["台中市", "臺中市", "台中"], "臺南": ["台南市", "臺南市", "台南"], "臺北": ["台北市", "台北", "臺北市"]}
areaDefinedDICT = {"地區": ["忠孝復興站", "忠孝敦化站", "國父紀念館站", "沙鹿區", "北屯區", "西屯區", "中西區", "東區", "南區"]}

def confirm_city(cityDefinedDICT, args):
    result = "Nothing"
    for k, v in cityDefinedDICT.items():
        if args in v:
            result = k
        elif args == k:
            result = k
        else:
            pass
    return result

def confirm_area(areaDefinedDICT, args):
    result = "Nothing"
    for k, v in areaDefinedDICT.items():
        if args in v:
            result = args
        else:
            pass
    return result
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_city_confirmation:
        print("[city_confirmation] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我][現在]在[台南]":
        if "在{}".format(args[2]) in inputSTR:
            if args[2] not in areaDefinedDICT["地區"]:
                resultDICT["city"] = confirm_city(cityDefinedDICT, args=args[2])
            else:
                resultDICT["area"] = confirm_area(areaDefinedDICT, args=args[2])


    if utterance == "[我]在的縣市是[台中]":
        if args[1] not in areaDefinedDICT["地區"]:
            resultDICT["city"] = confirm_city(cityDefinedDICT, args=args[1])
        else:
            resultDICT["area"] = confirm_area(areaDefinedDICT, args=args[1])


    if utterance == "在[臺中]":
        if "在{}".format(args[0]) in inputSTR:
            if args[0] not in areaDefinedDICT["地區"]:
                resultDICT["city"] = confirm_city(cityDefinedDICT, args=args[0])
            else:
                resultDICT["area"] = confirm_area(areaDefinedDICT, args=args[0])


    if utterance == "我人在[台南]":
        if args[0] not in areaDefinedDICT["地區"]:
            resultDICT["city"] = confirm_city(cityDefinedDICT, args=args[0])
        else:
            resultDICT["area"] = confirm_area(areaDefinedDICT, args=args[0])


    if utterance == "[我][現在]的地區是[北屯區]":
        if args[2] not in areaDefinedDICT["地區"]:
            resultDICT["city"] = confirm_city(cityDefinedDICT, args=args[2])
        else:
            resultDICT["area"] = confirm_area(areaDefinedDICT, args=args[2])


    return resultDICT