#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Disguise

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Disguise = True
userDefinedDICT = {"聲調": [""], "公安局": ["公安", "官員", "聯合國", "將領", "軍官"], "其友人": ["某某"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Disguise:
        print("[Disguise] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT = {"fake_id":[]}

    if utterance == "偽裝[中年][婦女][聲調]":
        resultDICT["fake_id"].append("".join([i for i in args if i not in userDefinedDICT["聲調"]]))

    if utterance == "偽裝之[該][社團][人員]聯絡":
        resultDICT["fake_id"].append("".join([i for i in args if i not in userDefinedDICT["聲調"]]))

    if utterance == "偽裝成[健保局][官員]":
        resultDICT["fake_id"].append("".join([i for i in args if i not in userDefinedDICT["聲調"]]))

    if utterance == "偽裝成[其友人][葉進興]":
        resultDICT["fake_id"].append("".join([i for i in args if i not in userDefinedDICT["聲調"]]))

    if utterance == "偽裝成[大陸][公安局][人員]":
        resultDICT["fake_id"].append("".join([i for i in args if i not in userDefinedDICT["聲調"]]))

    if utterance == "偽裝成[大陸][地區][衛生局]通訊[管理局]及[公安局][人員]":
        resultDICT["fake_id"].append(args[0] + args[1] + args[-1])

    if utterance == "偽裝成[女性]":
        resultDICT["fake_id"].append(args[0])

    if utterance == "偽裝是[某某][大陸][網路][商城客服][人員]":
        # write your code here
        pass

    if utterance == "偽裝為[CIA][局長]":
        resultDICT["fake_id"].append("".join([i for i in args if i not in userDefinedDICT["聲調"]]))

    if utterance == "偽裝為[保險][客戶][家屬]":
        # write your code here
        pass

    if utterance == "偽裝為[路人]":
        # write your code here
        pass

    if utterance == "偽裝為當地[公安]":
        # write your code here
        pass

    if utterance == "偽裝為退伍[小兵]":
        # write your code here
        pass

    return resultDICT
