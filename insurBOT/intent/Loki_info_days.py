#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for info_days

    Input:
        inputSTR      str,
        utterance     str,
        pattern          str[],
        resultDICT    dict,
        refDICT       dict

    Output:
        resultDICT    dict
"""
from ArticutAPI import Articut
from random import sample
import json
import os
import re


DEBUG_info_days = True
CHATBOT_MODE = False


with open("account.info", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())
articut = Articut(accountDICT['username'], accountDICT['api_key'])

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_info_days.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_info_days:
        print("[info_days] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, pattern):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*pattern)

    return resultSTR



def getPeriod(inputSTR, pattern, resultDICT, choice):
    userDefined = "intent/USER_DEFINED.json"
    posSTR = "".join([pos for pos in articut.parse(inputSTR, userDefinedDictFILE=userDefined)['result_pos'] if len(pos) > 1])
    # 取得比對之後的結果
    checkRes = ""
    for i in re.finditer(pattern, posSTR):
        checkRes = i.group()
        break
    
    # 取資訊加到resultDICT
    if checkRes:
        if choice == "year":
            year = '<ENTITY_num>([^<]+)</ENTITY_num><UserDefined>(年)</UserDefined>' 
            lst = []
            for i in re.finditer(year, checkRes):
                lst.append(i.group(1))
                lst.append(i.group(2))
                break
            resultDICT['period'] = "".join(lst)
        else:
            other = "<TIME_(holiday|justtime|day|week|month|season|year|decade)>(.{1,3}天|.{1,3}日|.{1,3}個月|.{1,3}週|.{1,3}個禮拜|.{1,3}個星期|.{1,3}星期|.{1,3}禮拜)</TIME_(holiday|justtime|day|week|month|season|year|decade)>"
            for other_y in re.finditer(other, checkRes):
                resultDICT['period'] = other_y.group(2)
    return resultDICT






def getResult(inputSTR, utterance, pattern, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "一天":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            getPeriod(inputSTR, pattern, resultDICT, "other")
            

    if utterance == "德國一年":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            getPeriod(inputSTR, pattern, resultDICT, "year")
            

    if utterance == "於德國旅行一年":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            getPeriod(inputSTR, pattern, resultDICT, "year")
            

    if utterance == "一學年":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            resultDICT['period'] = "一年"
            

    if utterance == "一學期":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            resultDICT['period'] = "四個月"
            

    if utterance == "暑假都會在國外":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            if "暑假" in inputSTR:
                resultDICT['period'] = "兩個月"
            else:
                resultDICT['period'] = "21天"

    if utterance == "玩一整個暑假":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            if "暑假" in inputSTR:
                resultDICT['period'] = "兩個月"
            else:
                resultDICT['period'] = "21天"

    if utterance == "半個學期":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            resultDICT['period'] = "兩個月"
            pass

    return resultDICT