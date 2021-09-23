#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for 425

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_425 = True
userDefinedDICT = {"副詞": ["任意", "隨意", "擅自", "隨便"], "動詞": ["過來", "過戶", "出租", "承租", "租"], "名詞": ["房東", "房客", "押金", "凶宅"], "家電": ["抽油煙機", "電風扇", "電冰箱", "飲水機", "除濕機"], "房間配備": ["木地板", "壁紙", "自來水", "Wifi", "單人床墊", "床頭櫃", "單人床", "天花板"], "法律用語": ["租金", "押租金", "修繕義務", "租賃契約", "出租人", "承租人", "次承租人", "轉租人"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_425:
        print("[425] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["confirm425_BOOL"] = None
    
    if utterance == "[我][板橋]租的[房子]被房東賣掉了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "[我][現在]住的[地方]被賣了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "[我][現在]住的[地方]被賣掉了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "[我][現在]租的[地方]被賣了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "[我][現在]租的[地方]被賣掉了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "[我][現在]租的[房子]被房東賣了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "[我][現在]租的[房子]被房東賣掉了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "[我]的[租屋處]被莫名其妙賣掉":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "[我]的[租屋處]被賣了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "[我]的[租屋處]被賣掉了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "[我]租的[房子]被賣掉了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "[房子]被賣給[別人]了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "房東把[我][板橋]租的[房子]賣了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "房東把[我][板橋]租的[房子]賣掉了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "房東把[我]租的[房子]賣了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "房東把[我]租的[房子]賣掉了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "房東說[他]要把[我][現在]住的[房子]賣掉":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "房東說要賣屋":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "房東說要賣掉[我][現在]住的[地方]":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "房東說要賣掉[我]的[租屋處]":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "把[我][現在]住的[地方]賣了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "把[我][現在]住的[地方]賣掉了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "把[我][現在]租的[房子]賣了":
        resultDICT["confirm425_BOOL"] = True

    if utterance == "把[我][現在]租的[房子]賣掉了":
        resultDICT["confirm425_BOOL"] = True

    return resultDICT