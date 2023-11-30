#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for change_person

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

DEBUG_change_person = True
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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_change_person.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_change_person:
        print("[change_person] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, pattern):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*pattern)

    return resultSTR

def getPerson(inputSTR, pattern, resultDICT):
    userDefined = "intent/USER_DEFINED.json"
    posSTR = "".join([pos for pos in articut.parse(inputSTR, userDefinedDictFILE=userDefined)['result_pos'] if len(pos) > 1])
    # 取得比對之後的結果
    checkRes = ""
    for i in re.finditer(pattern, posSTR):
        checkRes = i.group()
        break
    
    # 取資訊加到resultDICT
    if checkRes:
        person = '<ENTITY_pronoun>([^<]+)</ENTITY_pronoun>' 
        r = []
        for i in re.finditer(person, checkRes):
            r.append(i.group(1))
            break
        resultDICT['person'] = "".join(r)

    return resultDICT






def getResult(inputSTR, utterance, pattern, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "可以幫我媽保嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            resultDICT['change'] = True
            getPerson(inputSTR, pattern, resultDICT)
            

    if utterance == "想幫另一個人保":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            resultDICT['change'] = True
            

    if utterance == "想幫我媽媽保":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            resultDICT['change'] = True
            getPerson(inputSTR, pattern, resultDICT)
            

    if utterance == "我想問別的保險":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            resultDICT['change'] = True
            

    if utterance == "不一樣的人要保":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            resultDICT['change'] = True
            

    if utterance == "不同的人要保":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            resultDICT['change'] = True
            

    if utterance == "另一個人要保":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            resultDICT['change'] = True
            

    if utterance == "換另一個人保":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            resultDICT['change'] = True
            

    if utterance == "換成媽媽要問":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            resultDICT['change'] = True
            getPerson(inputSTR, pattern, resultDICT)
            

    if utterance == "想幫別人問問":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            resultDICT['change'] = True
            

    if utterance == "我媽媽是一個家庭主婦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            getPerson(inputSTR, pattern, resultDICT)
            

    if utterance == "我媽媽要保保險":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            getPerson(inputSTR, pattern, resultDICT)
            

    if utterance == "我朋友是一個家庭主婦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            resultDICT['person'] = '朋友'
            

    if utterance == "我朋友要保保險":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            resultDICT['person'] = '朋友'
            

    if utterance == "我妹妹也想保":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, pattern)
        else:
            getPerson(inputSTR, pattern, resultDICT)
            

    return resultDICT