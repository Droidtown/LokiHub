#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for congenital_disease

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

DEBUG_congenital_disease = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
# if CHATBOT_MODE:
#     try:
#         responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_congenital_disease.json"), encoding="utf-8"))
#     except Exception as e:
#         print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_congenital_disease:
        print("[congenital_disease] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

disease = ["唐氏症", "小胖威利症", "唇裂", "腭裂", "顎裂", "唇腭裂", "唇顎裂", "小兒症", "聽損", "甲狀腺功能低下", "先天性心臟病", "水腦症", "脊柱裂", "小腦症", "腦出血", "腦部缺氧性病變", "腦部感染", "中樞神經感染", "癩癎", "腦瘤"]

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    
    if utterance == "出生就[腦出血]":
        if CHATBOT_MODE:
            if args[0] in disease:
                resultDICT["congenital_disease"] = True
                resultDICT["response"] = "好的，再來想確認一下孩子的親戚是否有家族遺傳性相關疾病呢？"
            else:
                resultDICT["congenital_disease"] = False
                resultDICT["response"] = "了解，再來想確認一下孩子的親戚是否有家族遺傳性相關疾病呢？"

    if utterance == "[確診][唇顎裂]":
        if CHATBOT_MODE:
            if args[1] in disease:
                resultDICT["congenital_disease"] = True
                resultDICT["response"] = "好的，再來想確認一下孩子的親戚是否有家族遺傳性相關疾病呢？"
            else:
                resultDICT["congenital_disease"] = False
                resultDICT["response"] = "了解，再來想確認一下孩子的親戚是否有家族遺傳性相關疾病呢？"
        else:
            # write your code here
            pass

    if utterance == "是[唇顎裂]":
        if CHATBOT_MODE:
            if args[0] in disease:
                resultDICT["congenital_disease"] = True
                resultDICT["response"] = "好的，再來想確認一下孩子的親戚是否有家族遺傳性相關疾病呢？"
            else:
                resultDICT["congenital_disease"] = False
                resultDICT["response"] = "了解，再來想確認一下孩子的親戚是否有家族遺傳性相關疾病呢？"
        else:
            # write your code here
            pass

    if utterance == "有[唇顎裂]":
        if CHATBOT_MODE:
            if args[0] in disease:
                resultDICT["congenital_disease"] = True
                resultDICT["response"] = "好的，再來想確認一下孩子的親戚是否有家族遺傳性相關疾病呢？"
            else:
                resultDICT["congenital_disease"] = False
                resultDICT["response"] = "了解，再來想確認一下孩子的親戚是否有家族遺傳性相關疾病呢？"
        else:
            # write your code here
            pass

    if utterance == "診斷為[唇顎裂]":
        if CHATBOT_MODE:
            if args[0] in disease:
                resultDICT["congenital_disease"] = True
                resultDICT["response"] = "好的，再來想確認一下孩子的親戚是否有家族遺傳性相關疾病呢？"
            else:
                resultDICT["congenital_disease"] = False
                resultDICT["response"] = "了解，再來想確認一下孩子的親戚是否有家族遺傳性相關疾病呢？"
        else:
            # write your code here
            pass

    return resultDICT
