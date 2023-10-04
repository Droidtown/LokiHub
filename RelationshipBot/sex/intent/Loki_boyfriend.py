#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for boyfriend

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

DEBUG_boyfriend = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_boyfriend.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_boyfriend:
        print("[boyfriend] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[大姨媽]來[對方]還想做":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT["_period"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][硬]不起來":
        if CHATBOT_MODE:
            if args[1] == "硬":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][都][自己]來":
        if CHATBOT_MODE:
            if "自己" in args[2]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass
    
    if utterance == "[對方][每天][都][自己]來":
        if CHATBOT_MODE:
            if "自己" in args[3]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][每天][都][自己]解決":
        if CHATBOT_MODE:
            if "自己" in args[3]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][都]不使用[保險套]":
        if CHATBOT_MODE:
            if args[2] in userDefinedDICT["_condom"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][都]不戴[套]":
        if CHATBOT_MODE:
            if args[2] in userDefinedDICT["_condom"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]不想要戴[套]":
        if CHATBOT_MODE:
            if args[1] in userDefinedDICT["_condom"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]不想要用[保險套]":
        if CHATBOT_MODE:
            if args[1] in userDefinedDICT["_condom"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]不愛戴[套]":
        if CHATBOT_MODE:
            if args[1] in userDefinedDICT["_condom"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]不愛用[保險套]":
        if CHATBOT_MODE:
            if args[1] in userDefinedDICT["_condom"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]包莖":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]太持久":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]寧願[自己]來":
        if CHATBOT_MODE:
            if "自己" in args[2]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]寧願[自己]解決":
        if CHATBOT_MODE:
            if "自己" in args[2]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]寧願看A片":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]早洩":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]有勃起[障礙]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]有包莖[問題]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]有早洩[問題]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]有陽痿[問題]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]的[陰莖][硬]不起來":
        if CHATBOT_MODE:
            if args[1] in userDefinedDICT["_penis"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]的[陰莖]很臭":
        if CHATBOT_MODE:
            if args[1] in userDefinedDICT["_penis"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]的[陰莖]有異味":
        if CHATBOT_MODE:
            if args[1] in userDefinedDICT["_penis"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]的包皮過長":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]陽痿":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[男友]包莖":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT["_noun"] and args[0] != "女友":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
            elif args[0] == "女友":
                resultDICT["response"] = "通常女性不會有包莖的問題，請試著重新輸入，若有冒犯請見諒。"
        else:
            # write your code here
            pass

    if utterance == "[男友]太持久":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT["_noun"] and args[0] != "女友":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
            elif args[0] == "女友":
                resultDICT["response"] = "通常女性不會有太持久的問題，請試著重新輸入，若有冒犯請見諒。"
        else:
            # write your code here
            pass

    if utterance == "[男友]早洩":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT["_noun"] and args[0] != "女友":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
            elif args[0] == "女友":
                resultDICT["response"] = "通常女性不會有早洩的問題，請試著重新輸入，若有冒犯請見諒。"
        else:
            # write your code here
            pass

    if utterance == "[男友]陽痿":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT["_noun"] and args[0] != "女友":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
            elif args[0] == "女友":
                resultDICT["response"] = "通常女性不會有陽痿的問題，請試著重新輸入，若有冒犯請見諒。"
        else:
            # write your code here
            pass

    if utterance == "[對方][做愛]沒有[前]戲":
        if CHATBOT_MODE:
            if args[1] in userDefinedDICT["_mL"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][每天][DIY]":
        if CHATBOT_MODE:
            if args[2] in userDefinedDICT["_masturbation"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass
    if utterance == "[對方]的[陰莖]好臭":
        if CHATBOT_MODE:
            if args[1] in userDefinedDICT["_penis"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    return resultDICT