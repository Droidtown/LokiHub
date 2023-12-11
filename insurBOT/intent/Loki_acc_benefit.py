#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for acc_benefit

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

DEBUG_acc_benefit = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_acc_benefit.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_acc_benefit:
        print("[acc_benefit] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "有保障傷害醫療":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'yiliao_yn'
            

    if utterance == "有保障骨折":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'gs_yn'
            

    if utterance == "有包含實支實付":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'gs_yn'
            
            

    if utterance == "有沒有住院的":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'yiliao_list'
            
            

    if utterance == "哪些保險有實支實付":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'gs_list'
            

    if utterance == "實支實付有給付的有哪些":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'gs_list'
            

    if utterance == "實支實付的保險":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'gs_list'
            

    if utterance == "新iCarry傷害保險有實支實付嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'gs_yn'
            

    if utterance == "有沒有包含實支實付":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'gs_yn'
            

    if utterance == "有沒有包含醫療":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'yiliao_yn'
            

    if utterance == "有沒有包括實支實付":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'gs_yn'
            

    if utterance == "有沒有包括醫療":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'yiliao_yn'
            

    if utterance == "有給付住院":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'yiliao_yn'
            

    if utterance == "看醫生有給付":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'yiliao_yn'
            

    if utterance == "看醫生有給付有哪些":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'yiliao_list'
            

    if utterance == "有包含實支實付的賠償嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'gs_yn'
            

    if utterance == "有包含醫療的賠償嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'yiliao_yn'
            

    if utterance == "有哪些有包含醫療給付":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'yiliao_list'
            

    if utterance == "有哪些有包含骨折給付":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['acc_benefit'] = 'gs_list'
            

    return resultDICT