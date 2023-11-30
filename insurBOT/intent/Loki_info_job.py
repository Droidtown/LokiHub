#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for info_job

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

DEBUG_info_job = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__), "reply/reply_info_job.json"), encoding="utf-8")))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_info_job:
        print("[info_job] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "以種植蔬果為生":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "acc_con" in resultDICT:
                resultDICT['acc_con'].append("job")
            else:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("job")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")

    if utterance == "內勤":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "acc_con" in resultDICT:
                resultDICT['acc_con'].append("job")
            else:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("job")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")

    if utterance == "在外商公司上班":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "acc_con" in resultDICT:
                resultDICT['acc_con'].append("job")
            else:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("job")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")

    if utterance == "從事服務業":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "acc_con" in resultDICT:
                resultDICT['acc_con'].append("job")
            else:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("job")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")
            



    if utterance == "是一位服務員":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "life_con" not in resultDICT: 
                if "acc_con" in resultDICT:
                    resultDICT['acc_con'].append("job")
                else:
                    resultDICT['acc_con'] = []
                    resultDICT['acc_con'].append("job")
            
            # if "accident" not in resultDICT['type']:
            #     resultDICT['type'].append("accident")


    if utterance == "是捕魚的":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "life_con" not in resultDICT:
                if "保障" not in inputSTR:
                    if "acc_con" in resultDICT:
                        resultDICT['acc_con'].append("job")
                    else:
                        resultDICT['acc_con'] = []
                        resultDICT['acc_con'].append("job")
                # if "accident" not in resultDICT['type']:
                #     resultDICT['type'].append("accident")



    if utterance == "為一工人":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "life_con" not in resultDICT:
                if "acc_con" in resultDICT:
                    resultDICT['acc_con'].append("job")
                else:
                    resultDICT['acc_con'] = []
                    resultDICT['acc_con'].append("job")
            # if "accident" not in resultDICT['type']:
            #     resultDICT['type'].append("accident")


    if utterance == "職業是漁夫":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "acc_con" in resultDICT:
                resultDICT['acc_con'].append("job")
            else:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("job")
            if "accident" not in resultDICT['type']:
                resultDICT['type'].append("accident")

    return resultDICT