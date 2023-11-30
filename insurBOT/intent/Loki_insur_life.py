#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for insur_life

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

DEBUG_insur_life = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_insur_life.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_insur_life:
        print("[insur_life] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "一家之主":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            else:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if "life" not in resultDICT['type']:
                resultDICT['type'].append("life")
            

    if utterance == "使家庭生活陷入困境":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "life" not in resultDICT['type']:
                resultDICT['type'].append("life")


    if utterance == "保便宜的壽險":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "life" not in resultDICT['type']:
                resultDICT['type'].append("life")
            

    if utterance == "只有一個人在賺錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['life_con'] = []
            resultDICT['life_con'].append("high")
            if "life" not in resultDICT['type']:
                resultDICT['type'].append("life")
            

    if utterance == "單親家庭":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "life" not in resultDICT['type']:
                resultDICT['type'].append("life")
            

    if utterance == "壽險":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "life" not in resultDICT['type']:
                resultDICT['type'].append("life")
            

    if utterance == "怕留給家人":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['life_con'] = []
            resultDICT['life_con'].append("high")
            if "life" not in resultDICT['type']:
                resultDICT['type'].append("life")
            

    if utterance == "擔心自己的家人":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['life_con'] = []
            resultDICT['life_con'].append("high")
            if "life" not in resultDICT['type']:
                resultDICT['type'].append("life")
            

    if utterance == "是一位單親媽媽":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "life" not in resultDICT['type']:
                resultDICT['type'].append("life")
            

    if utterance == "是一位父親":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
            # if 'life_con' in resultDICT:
            #     resultDICT['life_con'].append("high")
            # else:
            #     resultDICT['life_con'] = []
            #     resultDICT['life_con'].append("high")
            # if "life" not in resultDICT['type']:
            #     resultDICT['type'].append("life")
        
            

    if utterance == "死後想要給家人保障":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['life_con'] = []
            resultDICT['life_con'].append("high")
            if "life" not in resultDICT['type']:
                resultDICT['type'].append("life")
            

    if utterance == "為家裡的經濟支柱":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['life_con'] = []
            resultDICT['life_con'].append("high")
            if "life" not in resultDICT['type']:
                resultDICT['type'].append("life")
            

    if utterance == "給家人多一份保障":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['life_con'] = []
            resultDICT['life_con'].append("high")
            if "life" not in resultDICT['type']:
                resultDICT['type'].append("life")
            

    if utterance == "買新房":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "life" not in resultDICT['type']:
                resultDICT['type'].append("life")
            

    if utterance == "隔代教養家庭":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "life" not in resultDICT['type']:
                resultDICT['type'].append("life")
            

    return resultDICT