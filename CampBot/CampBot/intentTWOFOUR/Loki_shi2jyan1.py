#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for shi2jyan1

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

DEBUG_shi2jyan1 = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/replytwofour/reply_shi2jyan1.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_shi2jyan1:
        print("[shi2jyan1] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[可以]在[幾點之後]接":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("家長","孩子")   
        else:
            # write your code here
            pass

    if utterance == "[可以]在哪個[時段]接":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("家長","孩子")  
        else:
            # write your code here
            pass

    if utterance == "[可以]接[他]的時間":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("家長","孩子")
        else:
            # write your code here
            pass

    if utterance == "[幾點][可以]接[他]":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("家長","孩子")
        else:pass


    if utterance == "[幾點]結束":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("家長","孩子")  
        else:
            pass

    if utterance == "[幾點]要送[他]過去":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("家長","孩子")
        else:
            pass


    if utterance == "[幾點]開始":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子")
        else:
            pass

    if utterance == "[幾點]開始接":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("家長","孩子")
        else:
            pass

    if utterance == "[活動]時間是[幾點]到[幾點]":
        if CHATBOT_MODE:
            if args[0] in ("活動", "行程", "營隊"):
                if args[0] in userDefinedDICT.keys():
                    args.append(userDefinedDICT[args[0]][0])
                    tmpReplySTR = getResponse(utterance, args).format(*args)
                    resultDICT["response"] = tmpReplySTR
                else:
                    pass
            else:
                pass
        else:
            # write your code here
            pass

    if utterance == "[活動]進行的[時段]是從[幾點]到[幾點]":
        if CHATBOT_MODE:
            if args[0] in ("活動", "行程", "營隊"):
                if args[0] in userDefinedDICT.keys():
                    args.append(userDefinedDICT[args[0]][0])
                    tmpReplySTR = getResponse(utterance, args).format(*args)
                    resultDICT["response"] = tmpReplySTR
                else:
                    pass
        else:
            # write your code here
            pass

    if utterance == "什麼[時候][可以]接[他]":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("家長","孩子")
        else:
            # write your code here
            pass

    if utterance == "什麼[時候]開始":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子")
        else:
            # write your code here
            pass

    if utterance == "什麼時間[可以]接[他]":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("家長","孩子")
        else:
            # write your code here
            pass

    if utterance == "把[他]送過去的時間":
        if CHATBOT_MODE:
            tmpReplySTR = getResponse(utterance, args).format(*args)
            resultDICT["response"] = tmpReplySTR
        else:
            pass


    if utterance == "接送時間是[幾點]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "營隊[期間]的接送時間":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "甚麼[時候][會]結束":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("家長","孩子")
        else:
            # write your code here
            pass

    if utterance == "甚麼[時候]結束":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("家長","孩子")
        else:
            # write your code here
            pass

    if utterance == "結束時間是[幾點]":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("家長","孩子")
        else:
            # write your code here
            pass

    if utterance == "結束需要到[幾點]":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("家長","孩子")
        else:
            # write your code here
            pass

    if utterance == "開始與結束[時][間]是[幾點]到[幾點]":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("活動")
        else:
            # write your code here
            pass

    if utterance == "需要在[幾點]被送到那裡":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("孩子")
        else:
            # write your code here
            pass
        
    if utterance == "什麼[時候][可以]去接[他]":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("家長","孩子")
        else:
            pass


    if utterance == "接送[時間]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "什麼[時候]回家":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass


    if utterance == "活動時間是[幾點]到[幾點]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "活動進行的時段是從[幾點]到[幾點]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass


    if utterance == "營隊[期間]的接送[時間]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[可以]接[他]的[時間]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[幾點][可以]接[他]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[幾點]帶[他]回家":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[幾點]要送[他]過去":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "什麼[時候][可以]去接[他]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "何時結束":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "何時開始":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "啥時結束":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "啥時開始":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "帶[他]回家":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "帶[他]過去":
        if args[0] == "":
            pass
        elif CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "把[他]送過去":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "把[他]送過去的[時間]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "接送[時間]是[幾點]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "活動[時間]是[幾點]到[幾點]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "活動進行的[時段]是從[幾點]到[幾點]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "結束[時間]是[幾點]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "送[他]過去":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT