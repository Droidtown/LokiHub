#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for hwen4lying2

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

DEBUG_hwen4lying2 = True
CHATBOT_MODE = True

try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/replyfivenine/reply_hwen4lying2.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_hwen4lying2:
        print("[hwen4lying2] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[同][年齡]？":
        if args[1] in userDefinedDICT["年紀"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[年紀][小]會不[會]跟不[上]":
        if args[0] in userDefinedDICT["年紀"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[年紀][小]的[孩子][是]否[能]跟得[上]活動的節奏":
        if args[0] in userDefinedDICT["年紀"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[年紀][小]的[孩子]會不[會]玩不起來?":
        if args[0] in userDefinedDICT["年紀"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[年紀][小]的[小孩]能不[能]融入[這個]活動":
        if args[0] in userDefinedDICT["年紀"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[年紀]比較大的[孩子]會不[會][無聊]?":
        if args[0] in userDefinedDICT["年紀"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[年紀]比較大的[孩子]會不[會]覺得[無聊]":
        if args[0] in userDefinedDICT["年紀"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[年紀]比較大的[小孩][可能][會]感到[無趣]":
        if args[0] in userDefinedDICT["年紀"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[年紀]比較大的[小孩]會不[會]感到[無聊]":
        if args[0] in userDefinedDICT["年紀"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[年齡]較大的[孩子][是]否[會]感到[無聊]":
        if args[0] in userDefinedDICT["年紀"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "以[不同][年齡]混合分組":
        if args[1] in userDefinedDICT["年紀"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "分組[都]是混齡":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "包含[不同][年齡]層":
        if args[1] in userDefinedDICT["年紀"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "在分組時[不同][年齡]的人是不[是][都]混合在[一起]":
        if args[1] in userDefinedDICT["年紀"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "是[相同][年紀]":
        if args[1] in userDefinedDICT["年紀"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass


    if utterance == "較大[年紀]的[孩子][是]否[會]感到[無聊]":
        if args[0] in userDefinedDICT["年紀"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "年紀[小]會不[會]跟不[上]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[同][一組]的[小孩][是]否[都]是[同][年齡]？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "同組的[孩子][是]否[都]是[同][年齡]？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "同組的[小孩][都][會]是[同][年紀]嗎?":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "是[同年]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT