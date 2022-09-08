#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for agree_adv

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
import os

DEBUG_agree_adv = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asNoun":["連假","線上","進班","遠距","面對面","愉快","線下","到班","實體課程"],"_asOkay":["ok","OK","oK","Ok","Okay","okay","OKAY"],"_asTime":["小時半"],"_asVerb":["改一下","討論一下","調整一下"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_agree_adv:
        print("[agree_adv] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "ok":
        if len(inputSTR) >= 4 or resultDICT["intentLIST"] != []:
            pass
        else:
            resultDICT["intentLIST"].append("agree")

    if utterance == "okay":
        if len(inputSTR) >= 4 or resultDICT["intentLIST"] != []:
            pass
        else:
            resultDICT["intentLIST"].append("agree")

    if utterance == "yes":
        if len(inputSTR) >= 5 or resultDICT["intentLIST"] != []:
            pass
        else:
            resultDICT["intentLIST"].append("agree")

    if utterance == "好":
        if len(inputSTR) >= 4 or resultDICT["intentLIST"] != []:
            pass
        else:
            resultDICT["intentLIST"].append("agree")

    if utterance == "好的":
        if len(inputSTR) >= 4 or resultDICT["intentLIST"] != []:
            pass
        else:
            resultDICT["intentLIST"].append("agree")

    if utterance == "對":
        if len(inputSTR) >= 4 or resultDICT["intentLIST"] != []:
            pass
        else:
            resultDICT["intentLIST"].append("agree")

    if utterance == "是":
        if len(inputSTR) >= 4 or resultDICT["intentLIST"] != []:
            pass
        else:
            resultDICT["intentLIST"].append("agree")

    if utterance == "正確":
        if len(inputSTR) >= 4 or resultDICT["intentLIST"] != []:
            pass
        else:
            resultDICT["intentLIST"].append("agree")

    if utterance == "沒問題":
        if len(inputSTR) >= 5 or resultDICT["intentLIST"] != []:
            pass
        else:
            resultDICT["intentLIST"].append("agree")

    if utterance == "沒錯":
        if len(inputSTR) >= 4 or resultDICT["intentLIST"] != []:
            pass
        else:
            resultDICT["intentLIST"].append("agree")

    return resultDICT