#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for info_highBudget

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

DEBUG_info_highBudget = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_info_highBudget.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_info_highBudget:
        print("[info_highBudget] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "加倍保障":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    if utterance == "多一點保障":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    if utterance == "多點保障":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    if utterance == "工作危險性高":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True

    if utterance == "有家庭":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    if utterance == "涵蓋範圍廣":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    if utterance == "理賠比較多":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    if utterance == "不想要省錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    if utterance == "保障多的":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    if utterance == "預算多的":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            pass

    if utterance == "預算頗高":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    if utterance == "比較貴的險":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    if utterance == "不在乎預算":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    if utterance == "不用擔心預算":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    if utterance == "保障可以更全面":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    if utterance == "加強的保障":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    if utterance == "可以有更多支出":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    if utterance == "更好的保障":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    if utterance == "照顧到比較多的需求":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    if utterance == "覆蓋更廣泛的風險":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("high")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("high")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high")
            if not resultDICT['type']:
                resultDICT['high'] = True
            

    return resultDICT