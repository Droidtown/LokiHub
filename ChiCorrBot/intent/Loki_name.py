#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for name

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

from ast import arg
import json
import os
from unicodedata import name
from unittest import result

DEBUG_name = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_agreeExp":["YES","Yes","yes","Y","y"],"_disagreeExp":["NO","No","no","N","n"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_name:
        print("[name] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[小明]":
        nameSTR = args[0]

    if utterance == "[我]叫[小明]":
        nameSTR = args[1]

    if utterance == "[我]叫[早餐店][帥哥]":
        nameSTR = args[1]+args[2]

    if utterance == "[我]叫[陳小明]":
        nameSTR = args[1]

    if utterance == "[我]是[小明]":
        nameSTR = args[1]

    if utterance == "[我]是[早餐店][帥哥]":
        nameSTR = args[0]+args[1]

    if utterance == "[我]是[陳小明]":
        nameSTR = args[1]

    if utterance == "[我]的名字叫[小明]":
        nameSTR = args[1]

    if utterance == "[我]的名字叫[早餐店][帥哥]":
        nameSTR = args[1]+args[2]

    if utterance == "[我]的名字叫[陳小明]":
        nameSTR = args[1]

    if utterance == "[我]的名字是[小明]":
        nameSTR = args[1]

    if utterance == "[我]的名字是[早餐店][帥哥]":
        nameSTR = args[1]+args[2]

    if utterance == "[我]的名字是[陳小明]":
        nameSTR = args[1]

    if utterance == "[早餐店][帥哥]":
        nameSTR = args[0]+args[1]

    if utterance == "[陳小明]":
        nameSTR = args[0]

    resultDICT['greeting'] = f'{nameSTR}，你好！那你學華語多久了？'

    return resultDICT