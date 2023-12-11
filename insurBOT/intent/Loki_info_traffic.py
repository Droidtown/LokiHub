#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for info_traffic

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os

DEBUG_info_traffic = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_info_traffic.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_info_traffic:
        print("[info_traffic] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "在假日期間":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_con'] = []
            resultDICT['acc_con'].append("traffic")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "在假日的時候":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_con'] = []
            resultDICT['acc_con'].append("traffic")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "搭乘大眾運輸":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_con'] = []
            resultDICT['acc_con'].append("traffic")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "與交通有關":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_con'] = []
            resultDICT['acc_con'].append("traffic")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "通勤方式":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_con'] = []
            resultDICT['acc_con'].append("traffic")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")

    if utterance == "我是行人":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_con'] = []
            resultDICT['acc_con'].append("traffic")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "我都走路":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_con'] = []
            resultDICT['acc_con'].append("traffic")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "交通上的考量":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_con'] = []
            resultDICT['acc_con'].append("traffic")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")

    return resultDICT