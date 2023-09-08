#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for other

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

DEBUG_other = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_other.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_other:
        print("[other] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[對方][偷偷]下載交友[軟體]":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][偷偷]下載約炮軟體":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]不[能]接受[開放性]關係":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]不讓[我]看[他]手機":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]出軌":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]劈腿":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]和[他][前][女友]還有在連絡":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]和[前][女友]藕斷絲連":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]和[前]任藕斷絲連":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]外遇":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]好像出軌":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]好像劈腿":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]好像戴[我]綠帽":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]好像腳踏[兩條]船":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]已經出軌好幾[次]":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]已經劈腿好幾[次]":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]很多[女生]朋友":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]戴[我]綠帽":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]曾經約過炮":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]有[兩支]手機":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]有炮友":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]無法讓[我]信任":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]瞞著[我]開小帳":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]腳踏[兩條]船":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]被[我]捉姦在床":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]讓[我]沒有安全感":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]還留著[他][前][女友]的[東西]":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]還留著[前]任的[東西]":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[男友]出軌":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[男友]劈腿":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[男友]外遇":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT["_noun"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[男友]腳踏[兩條]船":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT["_noun"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][會]和[別][人]傳曖昧[訊息]":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][會]和[別][人]搞曖昧":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][會]讓[別][人]坐[前]座":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][會]載[別][人]回家":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]不知道和[別][人]保持距離":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]不知道和[別][人]劃清界線":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]不知道要和[別][人]保持距離":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]不知道要和[別][人]劃清界線":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]和[前][女友]沒分[乾淨]":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]和[前]任沒分[乾淨]":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]已經出軌很多次了":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]已經劈腿很多次了":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]愛和[別][人]搞曖昧":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]是[渣男]":
        if CHATBOT_MODE:
            if args[0] != "我" and args[1] in ("渣男","臭渣男","甘蔗男","婊子","臭婊","臭婊子","渣渣"):
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass


    if utterance == "[對方][會]讓[別]的[女生][朋友]坐[前]座":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][會]載[別]的[女生][朋友]回家":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass
        
    if utterance == "[對方]騙[我][他]沒出軌":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]騙[我][他]沒劈腿":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]騙[我]說[他]沒出軌":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]騙[我]說[他]沒劈腿":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]不讓[我]看[他][LINE]":
        if CHATBOT_MODE:
            if args[0] != "我" and args[3] in userDefinedDICT["_sm"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]跟[別][人]去[旅館]":
        if CHATBOT_MODE:
            if args[0] != "我" and args[3] in userDefinedDICT["_hotel"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]追蹤很多[正妹]":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]約[別][人]去[旅館]":
        if CHATBOT_MODE:
            if args[0] != "我" and args[3] in userDefinedDICT["_hotel"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][會]偷看[我]的[兄弟]":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][會]偷看我[兄弟]":
        if CHATBOT_MODE:
            if args[0] != "我":
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][會]和[別][人][幽會]":
        if CHATBOT_MODE:
            if args[0] != "我" and args[4] in userDefinedDICT["_loyalty"]:
                if args[2]:
                    args[2] = args[2] + "的"
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]帶[別][人]去[旅館]":
        if CHATBOT_MODE:
            if args[0] != "我" and args[3] in userDefinedDICT["_hotel"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][會]和[他][妹][上床]":
        if CHATBOT_MODE:
            if args[0] != "我" and args[4] in userDefinedDICT["_loyalty"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][會]和她[妹妹][上床]":
        if CHATBOT_MODE:
            if args[0] != "我" and args[3] in userDefinedDICT["_loyalty"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[男人]的嘴騙人的鬼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    return resultDICT