#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for info_indentity

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

DEBUG_info_indentity = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_info_indentity.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_info_indentity:
        print("[info_indentity] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "上班族":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:

            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low_identity")
            else:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low_identity")



            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("job")
                resultDICT['acc_con'].append("low")
            else:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("job")
                resultDICT['acc_con'].append("low")


            

    if utterance == "低收入戶":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("weak")
            else:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("weak")

            resultDICT['life_con'] = []
            resultDICT['life_con'].append("weak")


            

    if utterance == "家庭主婦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("high_identity")
            else:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("high_identity")




    if utterance == "捕魚":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("weak")
            else:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("weak")

            resultDICT['life_con'] = []
            resultDICT['life_con'].append("weak")  



    if utterance == "經濟弱勢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("weak")
            else:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("weak")

            resultDICT['life_con'] = []
            resultDICT['life_con'].append("weak")



    if utterance == "經濟有困難":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("weak")
            else:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("weak")

            resultDICT['life_con'] = []
            resultDICT['life_con'].append("weak")



    if utterance == "剛進入社會":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low_identity")
            else:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low_identity")


            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("job")
                resultDICT['acc_con'].append("low")
            else:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("job")
                resultDICT['acc_con'].append("low")



    if utterance == "剛開始上班":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low_identity")
            else:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low_identity")

            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("job")
                resultDICT['acc_con'].append("low")
            else:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("job")
                resultDICT['acc_con'].append("low")


    if utterance == "平時朝九晚五":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low_identity")
            else:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low_identity")

            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("job")
                resultDICT['acc_con'].append("low")
            else:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("job")
                resultDICT['acc_con'].append("low")
            

    if utterance == "早八要上課":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low_identity")
            else:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low_identity")

            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("job")
                resultDICT['acc_con'].append("low")
            else:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("job")
                resultDICT['acc_con'].append("low")
            

    return resultDICT