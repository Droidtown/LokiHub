#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for all_ingre

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

DEBUG_all_ingre = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_veg":["地瓜","地瓜葉","青江菜"],"_food":["水煮蛋","白帶魚","紅棗"],"_fruit":["哈密瓜","火龍果","藍莓"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_all_ingre:
        print("[all_ingre] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT, all_utt):
    debugInfo(inputSTR, utterance)

    resultDICT["all_ingr"] = True

    if utterance == "[你][能]列出[所有]的[當季][食材]嗎":
        resultDICT["type"] = args[4]
        resultDICT["time"] = args[3]

    if utterance == "[我]想知道[所有]的[當季][食材]":
        resultDICT["type"] = args[3]
        resultDICT["time"] = args[1]        

    if utterance == "[現在]的[當季][食材]有哪些":
        resultDICT["time"] = args[0]
        resultDICT["type"] = args[1]

    if utterance == "[你]知道[七月]的[當令][食材]有哪些嗎":
        resultDICT["time"] = args[1]
        resultDICT["type"] = args[2]

    if utterance == "[我]想知道[三月]的[當令][食材]有哪些":
        resultDICT["time"] = args[1]
        resultDICT["type"] = args[2]

    if utterance == "[你][可以]跟[我]說[所有]的[當季][食材]嗎":
        resultDICT["type"] = args[5]

    if utterance == "告訴[我][所有]的[當季][食材]":
        resultDICT["type"] = args[3]

    return resultDICT