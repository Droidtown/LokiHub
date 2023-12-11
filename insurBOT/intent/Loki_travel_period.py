#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for travel_period

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

DEBUG_travel_period = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_travel_period.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_travel_period:
        print("[travel_period] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[國內]玩[10天]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['place'] = args[0]
            resultDICT['period'] = args[1]
            if "travel" not in resultDICT['type']:
                resultDICT['type'].append("travel")
            

    if utterance == "[國外]出差[10天]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['place'] = args[0]
            resultDICT['period'] = args[1]
            if "travel" not in resultDICT['type']:
                resultDICT['type'].append("travel")
            

    if utterance == "[國外]旅遊[10天]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['place'] = args[0]
            resultDICT['period'] = args[1]
            if "travel" not in resultDICT['type']:
                resultDICT['type'].append("travel") 
            

    if utterance == "[國外]玩[10天]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['place'] = args[0]
            resultDICT['period'] = args[1]
            if "travel" not in resultDICT['type']:
                resultDICT['type'].append("travel") 
            

    if utterance == "出國玩[10天]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['place'] = "國外"
            resultDICT['period'] = args[0]
            if "travel" not in resultDICT['type']:
                resultDICT['type'].append("travel")
            

    if utterance == "去[國外][10天]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['place'] = args[0]
            resultDICT['period'] = args[1]
            if "travel" not in resultDICT['type']:
                resultDICT['type'].append("travel")
            

    if utterance == "去[日本][10天]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['place'] = args[0]
            resultDICT['period'] = args[1]
            if "travel" not in resultDICT['type']:
                resultDICT['type'].append("travel")
            

    if utterance == "在[台灣]玩[10天]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['place'] = args[0]
            resultDICT['period'] = args[1]
            if "travel" not in resultDICT['type']:
                resultDICT['type'].append("travel")
            

    if utterance == "打工度假[10天]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['place'] = "國外"
            resultDICT['period'] = args[0]
            if "travel" not in resultDICT['type']:
                resultDICT['type'].append("travel")
            

    if utterance == "留學[10天]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['place'] = "國外"
            resultDICT['period'] = args[0]
            if "travel" not in resultDICT['type']:
                resultDICT['type'].append("travel")
            

    if utterance == "要去[國外][10天]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['place'] = "國外"
            resultDICT['period'] = args[1]
            if "travel" not in resultDICT['type']:
                resultDICT['type'].append("travel") 
            

    if utterance == "赴德[180天]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['place'] = "國外"
            resultDICT['period'] = args[0]
            if "travel" not in resultDICT['type']:
                resultDICT['type'].append("travel")
            

    if utterance == "遊學[10天]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['place'] = "國外"
            resultDICT['period'] = args[0]
            if "travel" not in resultDICT['type']:
                resultDICT['type'].append("travel") 
            

    return resultDICT