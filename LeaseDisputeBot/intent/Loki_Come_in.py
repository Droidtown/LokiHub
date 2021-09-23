#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Come_in

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Come_in = True
userDefinedDICT = {"副詞": ["任意", "隨意", "擅自", "隨便"], "動詞": ["過來", "過戶"], "名詞": ["房東", "房客"], "家電": ["抽油煙機", "電風扇", "電冰箱", "飲水機", "除濕機"], "房間配備": ["木地板", "壁紙", "自來水", "Wifi", "單人床墊", "床頭櫃", "單人床"], "法律用語": ["租金", "押租金", "修繕義務", "租賃契約", "出租人", "承租人", "次承租人", "轉租人"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Come_in:
        print("[Come_in] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["confirm_comein_BOOL"] = None
    
    if utterance == "[房東][任意]進出[我][租屋處]":
        resultDICT["confirm_comein_BOOL"] = True

    if utterance == "[房東][擅自]帶[人]進來[我][房間]":
        resultDICT["confirm_comein_BOOL"] = True

    if utterance == "[房東][隨便]進來[我][房間]":
        resultDICT["confirm_comein_BOOL"] = True

    if utterance == "[房東][隨意]進入[我][房間]":
        resultDICT["confirm_comein_BOOL"] = True

    if utterance == "[房東]未經[我]同意就帶[人]進來":
        resultDICT["confirm_comein_BOOL"] = True

    if utterance == "[房東]未經同意就[任意]進入[我][房間]":
        resultDICT["confirm_comein_BOOL"] = True

    if utterance == "[房東]趁[我]不在帶[人]來看屋":
        resultDICT["confirm_comein_BOOL"] = True

    if utterance == "[房東][任意]帶[人]進來[我][房間]":
        resultDICT["confirm_comein_BOOL"] = True

    if utterance == "[房東][擅自]帶[人]進入[我][房間]":
        resultDICT["confirm_comein_BOOL"] = True

    if utterance == "[房東][會]亂開[我][房間]的門":
        resultDICT["confirm_comein_BOOL"] = True

    if utterance == "[房東][會]跑到[我][房間][裡]":
        resultDICT["confirm_comein_BOOL"] = True

    if utterance == "[房東]亂跑進來[我][房間][裡面]":
        resultDICT["confirm_comein_BOOL"] = True

    if utterance == "[房東]進[我][房間]":
        resultDICT["confirm_comein_BOOL"] = True

    return resultDICT