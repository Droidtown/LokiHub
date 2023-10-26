#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for ying2dwei4shou1hwo4

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

DEBUG_ying2dwei4shou1hwo4 = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/replytwofour/reply_ying2dwei4shou1hwo4.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_ying2dwei4shou1hwo4:
        print("[ying2dwei4shou1hwo4] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[能]學到什麼":
        if CHATBOT_MODE:
            tmpSTR = "關於{}呢...".format("學到什麼") + getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子")   
        else:
            # write your code here
            pass

    if utterance == "[能]獲得哪些[知識]":
        if CHATBOT_MODE:
            tmpSTR = "關於{}呢...".format("獲得什麼") + getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子")   
        else:
            # write your code here
            pass

    if utterance == "[能夠]學到[些]什麼":
        if CHATBOT_MODE:
            tmpSTR = "關於{}呢...".format("學到什麼") + getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子")   
        else:
            # write your code here
            pass

    if utterance == "培養什麼[實力]":
        if CHATBOT_MODE:
            tmpSTR = "關於{}呢...".format("培養什麼") + getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子")   
        else:
            # write your code here
            pass

    if utterance == "學到什麼":
        if CHATBOT_MODE:
            tmpSTR = "關於{}呢...".format("學到什麼") + getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子")   
        else:
            # write your code here
            pass

    if utterance == "學到哪些[東西]":
        if CHATBOT_MODE:
            tmpSTR = "關於{}呢...".format("學到什麼") + getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子")   
        else:
            # write your code here
            pass

    if utterance == "得到什麼":
        if CHATBOT_MODE:
            tmpSTR = "關於{}呢...".format("得到什麼") + getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子")   
        else:
            # write your code here
            pass

    if utterance == "有什麼收穫":
        if CHATBOT_MODE:
            tmpSTR = "關於{}呢...".format("收穫") + getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子")   
        else:
            # write your code here
            pass

    if utterance == "有收穫":
        if CHATBOT_MODE:
            tmpSTR = "關於{}呢...".format("收穫") + getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子") 
        else:
            # write your code here
            pass

    if utterance == "有沒[有]收穫":
        if CHATBOT_MODE:
            tmpSTR = "關於{}呢...".format("收穫") + getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子") 
        else:
            # write your code here
            pass

    if utterance == "獲得什麼[經驗]":
        if CHATBOT_MODE:
            tmpSTR = "關於{}呢...".format("獲得的經驗") + getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子") 
        else:
            # write your code here
            pass

    if utterance == "獲得哪些收穫":
        if CHATBOT_MODE:
            tmpSTR = "關於{}呢...".format("收穫") + getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子") 
        else:
            # write your code here
            pass

    if utterance == "[可以]獲得怎樣的[知識]":
        if CHATBOT_MODE:
            tmpSTR = "關於{}呢...".format("獲得什麼") + getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子") 
        else:
            # write your code here
            pass

    if utterance == "獲得的[東西]":
        if (args[0] not in userDefinedDICT["小孩"]) and ("獲" in inputSTR): 
            if CHATBOT_MODE:
           
                tmpSTR = "關於{}呢...".format("獲得什麼") + getResponse(utterance, args)
                resultDICT["response"] = tmpSTR.format("孩子")
            else:pass
        else:
            # write your code here
            pass

    if utterance == "累積什麼[經驗]":
        if CHATBOT_MODE:
            tmpSTR = "關於{}呢...".format("獲得的經驗") + getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子") 
        else:
            # write your code here
            pass

   
    

   

    

    
   

    if utterance == "學到那些[東西]":
        if CHATBOT_MODE:
            tmpSTR = "關於{}呢...".format("學到什麼") + getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子")   
        else:
            # write your code here
            pass

    if utterance == "[能]獲得哪些知識":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "獲得怎樣的知識":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass


    return resultDICT