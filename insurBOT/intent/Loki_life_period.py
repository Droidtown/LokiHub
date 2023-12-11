#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for life_perioderiod

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

DEBUG_life_perioderiod = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_life_perioderiod.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_life_perioderiod:
        print("[life_perioderiod] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "哪一個壽險是定期":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "life_con" in resultDICT and resultDICT['life_con']:
                if "low" in resultDICT['life_con'] or "low_identity" in resultDICT['life_con']:
                    if '定期' in inputSTR:
                        resultDICT['life_period'] = 'regular_combine'
                    else:
                        resultDICT['life_period'] = 'life_combine'  
                elif "high" in resultDICT['life_con'] or "high_identity" in resultDICT['life_con']:
                    if '定期' in inputSTR:
                        resultDICT['life_period'] = 'regular_combine'
                    else:
                        resultDICT['life_period'] = 'life_combine'
                elif "weak" in resultDICT['life_con']:
                    if '定期' in inputSTR:
                        resultDICT['life_period'] = 'regular_combine'
                    else:
                        resultDICT['life_period'] = 'life_combine'
            else:
                if '定期' in inputSTR:
                    resultDICT['life_period'] = 'regular_list'
                else:
                    resultDICT['life_period'] = 'life_list'
            

    if utterance == "終生或定期":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['life_period'] = 'or_'
            

    if utterance == "終身還是定期":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['life_period'] = 'or_'
            

    if utterance == "是定期的嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if '定期' in inputSTR:
                resultDICT['life_period'] = 'regular_yn'
            else:
                resultDICT['life_period'] = 'life_yn'
            

    if utterance == "保定期的方案":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['life_period'] = 'regular_list'
            

    if utterance == "想保終身的壽險":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['life_period'] = 'life_list'
            

    if utterance == "想保終身的方案":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['life_period'] = 'life_list'
            

    if utterance == "這個是終身的壽險嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if '定期' in inputSTR:
                resultDICT['life_period'] = 'regular_yn'
            else:
                resultDICT['life_period'] = 'life_yn'
            

    return resultDICT