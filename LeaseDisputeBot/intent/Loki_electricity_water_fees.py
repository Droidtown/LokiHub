#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for electricity_water_fees

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_electricity_water_fees = True
userDefinedDICT = {"副詞": ["任意", "隨意", "擅自", "隨便"], "動詞": ["過來", "過戶"], "名詞": ["房東", "房客"], "家電": ["抽油煙機", "電風扇", "電冰箱", "飲水機", "除濕機"], "房間配備": ["木地板", "壁紙", "自來水", "Wifi", "單人床墊", "床頭櫃", "單人床"], "法律用語": ["租金", "押租金", "修繕義務", "租賃契約", "出租人", "承租人", "次承租人", "轉租人"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_electricity_water_fees:
        print("[electricity_water_fees] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["confirm_fees_BOOL"] = None
    
    if utterance == "Wifi費用":
        resultDICT["confirm_fees_BOOL"] = True

    if utterance == "[一度]5元":
       resultDICT["confirm_fees_BOOL"] = True

    if utterance == "[一度]6塊錢":
       resultDICT["confirm_fees_BOOL"] = True

    if utterance == "[一度][5.6塊]":
        resultDICT["confirm_fees_BOOL"] = True

    if utterance == "wifi費用":
        resultDICT["confirm_fees_BOOL"] = True

    if utterance == "依台電度數計價":
        resultDICT["confirm_fees_BOOL"] = True

    if utterance == "台電的度數":
        resultDICT["confirm_fees_BOOL"] = True

    if utterance == "天然氣費":
        resultDICT["confirm_fees_BOOL"] = True

    if utterance == "每度5元":
        resultDICT["confirm_fees_BOOL"] = True

    if utterance == "水費":
        resultDICT["confirm_fees_BOOL"] = True

    if utterance == "瓦斯費":
        resultDICT["confirm_fees_BOOL"] = True

    if utterance == "網路費":
        resultDICT["confirm_fees_BOOL"] = True

    if utterance == "自來水費":
        resultDICT["confirm_fees_BOOL"] = True

    if utterance == "電費":
        resultDICT["confirm_fees_BOOL"] = True

    if utterance == "亂記度數":
        resultDICT["confirm_fees_BOOL"] = True

    if utterance == "度數亂記":
        resultDICT["confirm_fees_BOOL"] = True

    if utterance == "自來水公司的度數":
        resultDICT["confirm_fees_BOOL"] = True

    return resultDICT