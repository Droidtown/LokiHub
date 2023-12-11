#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for feature

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

DEBUG_feature = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_feature.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_feature:
        print("[feature] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[心e路平安傷害保險][會]有哪些[特色]?":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[心e路平安傷害保險][會]有哪些優點?":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[心e路平安傷害保險][會]有哪些特點?":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[心e路平安傷害保險]是有什麼[特色]?":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[心e路平安傷害保險]是有什麼優點?":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[心e路平安傷害保險]是有什麼特點?":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[心e路平安傷害保險]有何優點":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[心e路平安傷害保險]有何特色":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[心e路平安傷害保險]有哪些好處":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[心e路平安傷害保險]的優點[可以]告訴[我]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[心e路平安傷害保險]的優點有哪些":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[心e路平安傷害保險]的優點為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[心e路平安傷害保險]的好處是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[心e路平安傷害保險]的特色[可以]告訴[我]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[心e路平安傷害保險]的特色是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[心e路平安傷害保險]的特色有哪些":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[心e路平安傷害保險]的特點[可以]告訴[我]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[新iCarry傷害保險]具有哪些特點？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[新iCarry傷害保險]有什麼優點":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[新iCarry傷害保險]有何特點？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[新iCarry傷害保險]有哪些[主要]特點？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[新iCarry傷害保險]有哪些特色和[優勢]？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[新iCarry傷害保險]有哪些特點？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[新iCarry傷害保險]的優點是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[新iCarry傷害保險]的特色為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[新iCarry傷害保險]的特點是什麼？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "何謂[壽險]保障[商品]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "告訴[我][心e路平安傷害保險]的優點":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[1] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[1]
                resultDICT['feature'] = True
            

    if utterance == "告訴[我][心e路平安傷害保險]的特色":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[1] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[1]
                resultDICT['feature'] = True
            

    if utterance == "告訴[我][心e路平安傷害保險]的特點":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[1] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[1]
                resultDICT['feature'] = True
            

    if utterance == "哪些是[心e路平安傷害保險]的優點":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "哪些是[心e路平安傷害保險]的特色":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "哪些是[心e路平安傷害保險]的特點":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "想知道[心e路平安傷害保險]的優點":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "想知道[心e路平安傷害保險]的特色":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "想知道[心e路平安傷害保險]的特點":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "[新iCarry傷害保險]的特點有哪些？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "有什麼是[壽險]保障[商品]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "有哪些是[心e路平安傷害保險]的優點":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "有哪些是[心e路平安傷害保險]的特色":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "有哪些是[心e路平安傷害保險]的特點":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "說說[心e路平安傷害保險]的優點":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "說說[心e路平安傷害保險]的特色":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    if utterance == "說說[心e路平安傷害保險]的特點":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if args[0] in userDefinedDICT['product_term'] or args[0] in userDefinedDICT['insur_term']:
                resultDICT['product'] = args[0]
                resultDICT['feature'] = True
            

    return resultDICT