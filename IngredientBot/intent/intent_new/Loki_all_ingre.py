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
    userDefinedDICT = {"_veg":["地瓜","地瓜葉","青江菜"],"_food":["水煮蛋","白帶魚","紅棗","紅蘿蔔","白果","日本馬頭魚"],"_temp":["產季","盛產季"],"_fruit":["哈密瓜","火龍果","藍莓"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_all_ingre:
        print("[all_ingre] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[你][可以]跟[我]說[所有]的[當季][食材]嗎":
        # write your code here
        pass

    if utterance == "[你][能]列出[所有]的[當季][食材]嗎":
        # write your code here
        pass

    if utterance == "[你]知道[七月]的[當令][食材]有哪些嗎":
        # write your code here
        pass

    if utterance == "[我]想知道[三月]的[當令][食材]有哪些":
        # write your code here
        pass

    if utterance == "[我]想知道[所有]的[當季][食材]":
        # write your code here
        pass

    if utterance == "[所有][當季][食材]":
        # write your code here
        pass

    if utterance == "[現在]的[當季][食材]有哪些":
        # write your code here
        pass

    return resultDICT