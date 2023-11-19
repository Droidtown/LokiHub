#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for play_alone

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

DEBUG_play_alone = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_play_alone.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_play_alone:
        print("[play_alone] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一直][都]是[這樣]":
        if CHATBOT_MODE:
            resultDICT["response"] = "接下來是關於數數的部分...您的孩子可以依序點數五個物品嗎？例如：用手指從第一個點點數到第五個點點？"
            resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "[小孩][很]怕生":
        if CHATBOT_MODE:
            resultDICT["response"] = "接下來是關於數數的部分...您的孩子可以依序點數五個物品嗎？例如：用手指從第一個點點數到第五個點點？"
            resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "[小孩]沒[興趣]":
        if CHATBOT_MODE:
            resultDICT["response"] = "接下來是關於數數的部分...您的孩子可以依序點數五個物品嗎？例如：用手指從第一個點點數到第五個點點？"
            resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "接下來是關於數數的部分...您的孩子可以依序點數五個物品嗎？例如：用手指從第一個點點數到第五個點點？"
                resultDICT["q5"] = True
            else:
                resultDICT["response"] = "接下來是關於數數的部分...您的孩子可以依序點數五個物品嗎？例如：用手指從第一個點點數到第五個點點？"
                resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "[很常][這樣]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "接下來是關於數數的部分...您的孩子可以依序點數五個物品嗎？例如：用手指從第一個點點數到第五個點點？"
                resultDICT["q5"] = True
            else:
                resultDICT["response"] = "接下來是關於數數的部分...您的孩子可以依序點數五個物品嗎？例如：用手指從第一個點點數到第五個點點？"
                resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "不喜歡跟[大人]玩": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "不太[會]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "不跟[大人]玩": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "對[都]玩[自己]的不理人":
        if CHATBOT_MODE:
            resultDICT["response"] = "接下來是關於數數的部分...您的孩子可以依序點數五個物品嗎？例如：用手指從第一個點點數到第五個點點？"
            resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "從[以前]就不喜歡跟[別人]玩":
        if CHATBOT_MODE:
            resultDICT["response"] = "接下來是關於數數的部分...您的孩子可以依序點數五個物品嗎？例如：用手指從第一個點點數到第五個點點？"
            resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "有聽[學校][老師]說過": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "看[心情]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT