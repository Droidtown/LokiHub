#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for searching

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

DEBUG_searching = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"cost":["支出"],"money":["總額","費用","總金額","金錢","錢"],"place":["814","小7","小七"],"people":["Cynthia","Deric"],"search":["查","查詢"],"earning":["收入"],"gambling":["大樂透"],"medicine":["醫藥費"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_searching:
        print("[searching] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    # debugInfo(inputSTR, utterance)
    if utterance == "查詢[總金額]":
        pass

    if utterance == "查詢支出[總額]":
        # write your code here
        pass

    return resultDICT