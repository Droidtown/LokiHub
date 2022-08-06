#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for accounting

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

DEBUG_accounting = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"cost":["支出"],"place":["814","小7","小七"],"people":["Cynthia","Deric"],"earning":["收入"],"gambling":["大樂透"],"medicine":["醫藥費"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_accounting:
        print("[accounting] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[50040][支出]":
        resultDICT["amount"] = args[0]
        resultDICT["account"] = args[1]

    if utterance == "[50040元][支出]":
        resultDICT["amount"] = args[0][:-1]
        resultDICT["account"] = args[1]

    if utterance == "[我]跟[我]朋友去814閒逛了[兩個小時]，[支出][3000元]":
        resultDICT["amount"] = args[4]
        resultDICT["account"] = args[3][:-1]

    if utterance == "[支出][12000]，醫藥費":
        resultDICT["amount"] = args[1]
        resultDICT["account"] = args[0]

    if utterance == "[支出][12000元]，醫藥費":
        resultDICT["amount"] = args[1][:-1]
        resultDICT["account"] = args[0]

    if utterance == "[支出][2000元]":
        resultDICT["amount"] = args[1][:-1]
        resultDICT["account"] = args[0]

    if utterance == "[收入][15000]，[中]大樂透":
        resultDICT["amount"] = args[1]
        resultDICT["account"] = args[0]

    if utterance == "[收入][15000元]，[中]大樂透":
        resultDICT["amount"] = args[1][:-1]
        resultDICT["account"] = args[0]
        
    if utterance == "[收入][3000]":
        resultDICT["amount"] = args[1]
        resultDICT["account"] = args[0]

    if utterance == "去814[支出][300]":
        resultDICT["amount"] = args[1]
        resultDICT["account"] = args[0]

    if utterance == "去814[支出][300元]":
        resultDICT["amount"] = args[1][:-1]
        resultDICT["account"] = args[0]

    if utterance == "去[全聯][支出][3200元]":
        resultDICT["amount"] = args[2][:-1]
        resultDICT["account"] = args[1]

    if utterance == "去小7[收入][1300元]":
        resultDICT["amount"] = args[1][:-1]
        resultDICT["account"] = args[0]

    if utterance == "去小七[支出][3400]":
        resultDICT["amount"] = args[1]
        resultDICT["account"] = args[0]


    # 這次指令的意圖為"accounting"
    resultDICT["intent"] = "accounting"
    return resultDICT