#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for insur_accident

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

DEBUG_insur_accident = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_insur_accident.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_insur_accident:
        print("[insur_accident] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "上學過程":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_con'] = []
            resultDICT['acc_con'].append("traffic")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "保便宜的意外險":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "在外奔走":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "有工作考量":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_con'] = []
            resultDICT['acc_con'].append("job")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "工作遇到一些事故":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_con'] = []
            resultDICT['acc_con'].append("job")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "幫忙負擔醫療費":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "恢復":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "意外險":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "應對突發狀況":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "我的工作較危險":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_con'] = []
            resultDICT['acc_con'].append("job")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "日常生活不便":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "獲得廣泛的意外保障":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "考量工作":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_con'] = []
            resultDICT['acc_con'].append("job")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "覺得意外無處不在":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "讓我在工作的時候有保障":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_con'] = []
            resultDICT['acc_con'].append("job")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "降低經濟壓力":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "高危險性的工作":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_con'] = []
            resultDICT['acc_con'].append("job")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "不是疾病的":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "遇到車禍":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "非疾病的":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "預防突發事故":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            

    if utterance == "有職業上的考量":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            pass

    return resultDICT