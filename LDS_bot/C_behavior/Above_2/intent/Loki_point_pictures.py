#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for point_pictures

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

DEBUG_point_pictures = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_point_pictures.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_point_pictures:
        print("[point_pictures] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[不太]確定": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[不行]":
        if CHATBOT_MODE:
            resultDICT["response"] = "這樣呀...當您與孩子一起看書時，他是否已經懂得一些看書的規則呀？例如：他會一頁頁翻書或會用手去指圖片？"
            resultDICT["q8"] = False
        else:
            # write your code here
            pass

    if utterance == "[好像][可以]":
        if CHATBOT_MODE:
            resultDICT["response"] = "這樣呀...當您與孩子一起看書時，他是否已經懂得一些看書的規則呀？例如：他會一頁頁翻書或會用手去指圖片？"
            resultDICT["q8"] = True
        else:
            # write your code here
            pass

    if utterance == "[好像]不[會]":
        if CHATBOT_MODE:
            resultDICT["response"] = "這樣呀...當您與孩子一起看書時，他是否已經懂得一些看書的規則呀？例如：他會一頁頁翻書或會用手去指圖片？"
            resultDICT["q8"] = False
        else:
            # write your code here
            pass

    if utterance == "[好像]有":
        if CHATBOT_MODE:
            resultDICT["response"] = "這樣呀...當您與孩子一起看書時，他是否已經懂得一些看書的規則呀？例如：他會一頁頁翻書或會用手去指圖片？"
            resultDICT["q8"] = True
        else:
            # write your code here
            pass

    if utterance == "[小孩]沒興趣": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "這樣呀...當您與孩子一起看書時，他是否已經懂得一些看書的規則呀？例如：他會一頁頁翻書或會用手去指圖片？"
                resultDICT["q8"] = False
            elif "常常" in inputSTR:
                resultDICT["response"] = "這樣呀...當您與孩子一起看書時，他是否已經懂得一些看書的規則呀？例如：他會一頁頁翻書或會用手去指圖片？"
                resultDICT["q8"] = True
        else:
            # write your code here
            pass

    if utterance == "[會]但[不常]":
        if CHATBOT_MODE:
            resultDICT["response"] = "這樣呀...當您與孩子一起看書時，他是否已經懂得一些看書的規則呀？例如：他會一頁頁翻書或會用手去指圖片？"
            resultDICT["q8"] = True
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

    if utterance == "沒辦法":
        if CHATBOT_MODE:
            resultDICT["response"] = "這樣呀...當您與孩子一起看書時，他是否已經懂得一些看書的規則呀？例如：他會一頁頁翻書或會用手去指圖片？"
            resultDICT["q8"] = False
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