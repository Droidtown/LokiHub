#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for time

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
from sqlite3 import Time
from ArticutAPI import Articut

with open("./account.info", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())

articut = Articut(username=accountDICT['username'], apikey=accountDICT['articut_key'])

DEBUG_time = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_agreeExp":["YES","Yes","yes","Y","y"],"_disagreeExp":["NO","No","no","N","n"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_time:
        print("[time] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一分]":
        timeDICT = articut.parse(inputSTR)
        if len(timeDICT['result_obj'][0]) == 1 and 'TIME_' in timeDICT['result_obj'][0][0]['pos']:
            timeSTR = args[0]

    if utterance == "[我]學了[一分]":
        timeSTR = args[1]

    if utterance == "[我]學中文學了[一天]":
        timeSTR = args[1]

    if utterance == "[我]學華語學了[一天]":
        timeSTR = args[1]

    if utterance == "學中文學了[一天]":
        timeSTR = args[0]

    if utterance == "學華語學了[一天]":
        timeSTR = args[0]

    resultDICT['time'] = f'哇～你學了{timeSTR}呀！好棒！\n讓我幫你提升華語能力吧！\n請你輸入一個華語句子，如果有錯誤，我將會告訴你建議的說法和錯誤之處。\n我們開始學習華語吧！'

    return resultDICT