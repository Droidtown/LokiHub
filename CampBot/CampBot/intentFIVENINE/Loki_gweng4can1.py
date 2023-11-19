#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for gweng4can1

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

DEBUG_gweng4can1 = True
CHATBOT_MODE = True

try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/replyfivenine/reply_gweng4can1.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_gweng4can1:
        print("[gweng4can1] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[中午][會]吃什麼":
        if args[0] in ["中午", "午餐", "中餐"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
                
        elif args[0] in userDefinedDICT["點心"]:
            resultDICT["response"] = "我們會視情況安排可以期待一下每天的{}時間~".format(args[0])           
        
        else:
            # write your code here
            pass

    if utterance == "[自行]攜帶[午餐]":
        if args[1] in userDefinedDICT["吃的東西"]:
            
            if args[1] not in ["午餐", "點心"]:
                resultDICT["response"] = "我們僅有提供午餐和點心喔!"
                
            elif CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "供應[午餐]":
        if args[0] not in userDefinedDICT["吃的東西"]:
            pass
        elif args[0] != "午餐":
            resultDICT["response"] = "我們僅有提供午餐和點心喔!"
        elif CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "帶[零食]":
        if args[0] in userDefinedDICT["吃的東西"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)            
        else:
            # write your code here
            pass

    if utterance == "帶[零食]進去":
        if args[0] not in userDefinedDICT["吃的東西"]:
            pass
        elif CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "把[零食]帶進去":
        if args[0] in userDefinedDICT["吃的東西"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)            
        else:
            # write your code here
            pass

    if utterance == "有[點心]":
        if args[0] in userDefinedDICT["吃的東西"]:
            if args[0] == "點心":
                if CHATBOT_MODE:
                    resultDICT["response"] = getResponse(utterance, args)
                    
            elif args[0] == "午餐":
                resultDICT["response"] = "我們有提供午餐喔!"
                
            else:
                resultDICT["response"] = "我們僅提供午餐和點心喔!"
                
        else:
            # write your code here
            pass

    if utterance == "有沒[有][點心]":
        if args[1] in userDefinedDICT["吃的東西"]:
            if args[1] not in ["午餐", "點心"]:
                resultDICT["response"] = "我們僅有提供午餐和點心喔!"
                
            elif CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有沒[有][點心]吃？":
        if args[1] in userDefinedDICT["吃的東西"]:
            
            if args[1] not in ["午餐", "點心"]:
                resultDICT["response"] = "我們僅有提供午餐和點心喔!"
                
            elif CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "自備[午餐]":
        if args[0] in userDefinedDICT["吃的東西"]:
            
            if args[0] not in ["午餐", "點心"]:
                resultDICT["response"] = "我們僅有提供午餐和點心喔!"
                
            elif CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "訂[午餐]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[會][餓]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[會][餓]怎麼辦":
        if args[1] != "餓":
            pass
        elif CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "吃[不飽]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "肚子[餓]":
        if args[0] == "餓":
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[早餐]怎麼辦":
        if (args[0] in userDefinedDICT["吃的東西"]) and ("午" not in args[0]):
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[早餐]是[自行]解決":
        if args[0] == "早餐":
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass
        
    if utterance == "那有[午餐]嗎":
        if args[0] in userDefinedDICT["吃的東西"]:
            if args[0] not in ["午餐", "點心"]:
                resultDICT["response"] = "我們僅有提供午餐和點心喔!"
                
            elif CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
    
    if utterance == "不提供[午餐]":
        if args[0] in userDefinedDICT["吃的東西"]:
            if args[0] not in ["午餐", "點心"]:
                resultDICT["response"] = "我們僅有提供午餐和點心喔!"
                
            elif CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
    return resultDICT