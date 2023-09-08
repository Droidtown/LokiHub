#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for point_and_count_to_13

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

DEBUG_point_and_count_to_13 = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_point_and_count_to_13.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_point_and_count_to_13:
        print("[point_and_count_to_13] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[只][會]幾[個]":
        if CHATBOT_MODE:
            resultDICT["response"] = "對了，關於語詞關係的部分...請問您的孩子能不能理解並說出至少三組相對的語詞呢？例如：哥哥是男生，姊姊是…；夏天很熱，冬天…？"
            resultDICT["q9"] = False
        else:
            # write your code here
            pass

    if utterance == "[都]用指的":
        if CHATBOT_MODE:
            resultDICT["response"] = "對了，關於語詞關係的部分...請問您的孩子能不能理解並說出至少三組相對的語詞呢？例如：哥哥是男生，姊姊是…；夏天很熱，冬天…？"
            resultDICT["q9"] = False
        else:
            # write your code here
            pass

    if utterance == "不[完整]":
        if CHATBOT_MODE:
            resultDICT["response"] = "對了，關於語詞關係的部分...請問您的孩子能不能理解並說出至少三組相對的語詞呢？例如：哥哥是男生，姊姊是…；夏天很熱，冬天…？"
            resultDICT["q9"] = False
        else:
            # write your code here
            pass

    if utterance == "不太[會]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "不太行": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "沒[問題]":
        if CHATBOT_MODE:
            if "問題" in inputSTR:
                resultDICT["response"] = "對了，關於語詞關係的部分...請問您的孩子能不能理解並說出至少三組相對的語詞呢？例如：哥哥是男生，姊姊是…；夏天很熱，冬天…？"
                resultDICT["q9"] = True
            elif "辦法" in inputSTR:
                resultDICT["response"] = "對了，關於語詞關係的部分...請問您的孩子能不能理解並說出至少三組相對的語詞呢？例如：哥哥是男生，姊姊是…；夏天很熱，冬天…？"
                resultDICT["q9"] = False
        else:
            # write your code here
            pass

    if utterance == "跳來跳去":
        if CHATBOT_MODE:
            resultDICT["response"] = "對了，關於語詞關係的部分...請問您的孩子能不能理解並說出至少三組相對的語詞呢？例如：哥哥是男生，姊姊是…；夏天很熱，冬天…？"
            resultDICT["q9"] = False
        else:
            # write your code here
            pass

    if utterance == "跳著唸":
        if CHATBOT_MODE:
            resultDICT["response"] = "對了，關於語詞關係的部分...請問您的孩子能不能理解並說出至少三組相對的語詞呢？例如：哥哥是男生，姊姊是…；夏天很熱，冬天…？"
            resultDICT["q9"] = False
        else:
            # write your code here
            pass

    return resultDICT