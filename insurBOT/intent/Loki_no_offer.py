#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for no_offer

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

DEBUG_no_offer = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_no_offer.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_no_offer:
        print("[no_offer] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "2000可以買啥":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "yusuan"
            

    if utterance == "保險有幾年期":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "nianqi"
            

    if utterance == "可以賠多少錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "peichang"
            

    if utterance == "合約可以有幾年":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "nianqi"
            

    if utterance == "合約有幾年期":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "nianqi"
            

    if utterance == "壽險以外的保險":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "out"
            

    if utterance == "屬於哪一類職業":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "fenlei"
            

    if utterance == "工人是哪一類的職業":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "fenlei"
            

    if utterance == "幫我算要花多少錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "yusuan"
            

    if utterance == "年齡有什麼限制嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "xianzhi"
            

    if utterance == "想保健康醫療險":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "out"
            

    if utterance == "想保投資型保險":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "out"
            

    if utterance == "我的職業會被分到哪一類":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "fenlei"
            

    if utterance == "有2000元可以買什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "yusuan"
            

    if utterance == "有什麼年齡限制嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "xianzhi"
            

    if utterance == "有什麼職業的限制嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "fenlei"
            

    if utterance == "有哪些限制嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "xianzhi"
            

    if utterance == "有提供保費試算嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if "保費試算" in inputSTR:
                resultDICT['no_offer'] = 'shisuan'
            elif "保額" in inputSTR:
                resultDICT['no_offer'] = 'baoe'
            elif "年期" in inputSTR:
                resultDICT['no_offer'] = 'nianqi'
            elif "職業分類" in inputSTR and "職業類型" in inputSTR:
                resultDICT['no_offer'] = 'fenlei'
            elif "附約" in inputSTR:
                resultDICT['no_offer'] = 'fuyue'
            elif "保險費" in inputSTR or "保費" in inputSTR: 
                resultDICT['no_offer'] = 'shisuan'

    if utterance == "有沒有附加的合約":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "fuyue"
            

    if utterance == "算我可以買哪個":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "yusuan"
            

    if utterance == "職業屬於哪一類":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "fenlei"
            

    if utterance == "職業是哪種類型":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "fenlei"
            

    if utterance == "職業是工人的話可以保意外險嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "fenlei"
            

    if utterance == "職業類型有什麼限制嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "fenlei"
            

    if utterance == "賠償多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "peichang"
            

    if utterance == "賠償金可以拿多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "peichang"
            

    if utterance == "這個險怎麼賣":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "shisuan"
            

    if utterance == "可以幫我算保費嗎?":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = 'shisuan'
            

    if utterance == "錢怎麼算":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = 'shisuan'
            

    if utterance == "保費有多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = 'shisuan'
            

    if utterance == "可以分期付款嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = 'fenqi'
            

    if utterance == "有什麼附約嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = 'fuyue'
            

    if utterance == "有提供分期付款嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = 'fenqi'
            

    if utterance == "賠償金多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "peichang"
            

    if utterance == "賠償金有多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['no_offer'] = "peichang"
            

    return resultDICT