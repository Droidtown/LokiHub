#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for genetic_disease

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

DEBUG_genetic_disease = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
# if CHATBOT_MODE:
#     try:
#         responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_genetic_disease.json"), encoding="utf-8"))
#     except Exception as e:
#         print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_genetic_disease:
        print("[genetic_disease] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

disease = ["聽損", "視障", "視覺障礙", "自閉", "自閉症", "智能不足", "精神疾病"]
relative = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "third_degree_relative.txt"), encoding="utf-8").read().split("\n")

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[自閉]":
        if CHATBOT_MODE:
            if args[0] in disease :
                resultDICT["genetic_disease"] = args[0]
                resultDICT["response"] = "有{}的是哪位親戚呢？".format(args[0])
            else:
                resultDICT["genetic_disease"] = False
        else:
            # write your code here
            pass

    if utterance == "[爸爸][自閉]":
        if CHATBOT_MODE:
            if args[1] in disease and args[0] != "":
                if args[0] in relative:
                    resultDICT["genetic_disease"] = True
                    resultDICT["response"] = "好的，接下來想針對孩子的生活環境跟您做一些確認。\n不知道孩子是不是已經上托嬰中心或幼兒園了呢?"
                else:
                    resultDICT["genetic_disease"] = False
                    resultDICT["response"] = "好的，接下來想針對孩子的生活環境跟您做一些確認。\n不知道孩子是不是已經上托嬰中心或幼兒園了呢?"
            elif args[1] in disease and args[0] == "":
                resultDICT["genetic_disease"] = args[1]
                resultDICT["response"] = "有{}的是孩子的哪位親戚呢？".format(args[1])
            else:
                resultDICT["genetic_disease"] = False
                resultDICT["response"] = "好的，接下來想針對孩子的生活環境跟您做一些確認。\n不知道孩子是不是已經上托嬰中心或幼兒園了呢?"
        else:
            # write your code here
            pass

    if utterance == "[爸爸]有[自閉]":
        if CHATBOT_MODE:
            if args[1] in disease and args[0] != "":
                if args[0] in relative:
                    resultDICT["genetic_disease"] = True
                    resultDICT["response"] = "好的，接下來想針對孩子的生活環境跟您做一些確認。\n不知道孩子是不是已經上托嬰中心或幼兒園了呢?"
                else:
                    resultDICT["genetic_disease"] = False
                    resultDICT["response"] = "好的，接下來想針對孩子的生活環境跟您做一些確認。\n不知道孩子是不是已經上托嬰中心或幼兒園了呢?"
            elif args[1] in disease and args[0] == "":
                resultDICT["genetic_disease"] = args[1]
                resultDICT["response"] = "有{}的是孩子的哪位親戚呢？".format(args[1])
            else:
                resultDICT["genetic_disease"] = False
                resultDICT["response"] = "好的，接下來想針對孩子的生活環境跟您做一些確認。\n不知道孩子是不是已經上托嬰中心或幼兒園了呢?"
        else:
            # write your code here
            pass

    if utterance == "[爸爸]是[自閉]":
        if CHATBOT_MODE:
            if args[1] in disease and args[0] != "":
                if args[0] in relative:
                    resultDICT["genetic_disease"] = True
                    resultDICT["response"] = "好的，接下來想針對孩子的生活環境跟您做一些確認。\n不知道孩子是不是已經上托嬰中心或幼兒園了呢?"
                else:
                    resultDICT["genetic_disease"] = False
                    resultDICT["response"] = "好的，接下來想針對孩子的生活環境跟您做一些確認。\n不知道孩子是不是已經上托嬰中心或幼兒園了呢?"
            elif args[1] in disease and args[0] == "":
                resultDICT["genetic_disease"] = args[1]
                resultDICT["response"] = "有{}的是孩子的哪位親戚呢？".format(args[1])
            else:
                resultDICT["genetic_disease"] = False
                resultDICT["response"] = "好的，接下來想針對孩子的生活環境跟您做一些確認。\n不知道孩子是不是已經上托嬰中心或幼兒園了呢?"
        else:
            # write your code here
            pass

    if utterance == "[爸爸]有":
        if CHATBOT_MODE:
            if args[0] in relative:
                resultDICT["genetic_disease"] = 1/2
                resultDICT["response"] = "那{}是有什麼樣的遺傳性疾病呢?"
            else:
                resultDICT["genetic_disease"] = False
                resultDICT["response"] = "好的，接下來想針對孩子的生活環境跟您做一些確認。\n不知道孩子是不是已經上托嬰中心或幼兒園了呢?"
        else:
            # write your code here
            pass

    if utterance == "是自閉":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT
