#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for number
    
    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict
    
    Output:
        resultDICT    dict
"""

DEBUG_number = True
userDefinedDICT = {"液體": ["液狀物", "液狀", "液態"], "網紅": [""], "落紅": [""], "紅不讓": [""]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_number:
        print("[number] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[上面]刻著[1]":
         
        resultDICT["number"] = args[1]
    
    if utterance == "[上面]刻著[一個][1]":
         
        resultDICT["number"] = args[2]

    if utterance == "[上面]印了[1]":
         
        resultDICT["number"] = args[1]

    if utterance == "[上面]印有[1]":
         
        resultDICT["number"] = args[1]

    if utterance == "[上面]印有[一個][1]":
         
        resultDICT["number"] = args[2]

    if utterance == "[上面]印的字是[1]":
         
        resultDICT["number"] = args[1]

    if utterance == "[上面]印著[1]":
         
        resultDICT["number"] = args[1]

    if utterance == "[上面]印著[一個][1]":
         
        resultDICT["number"] = args[2]

    if utterance == "[上面]寫[1]":
         
        resultDICT["number"] = args[1]

    if utterance == "[上面]寫了[一個][1]":
         
        resultDICT["number"] = args[2]

    if utterance == "[上面]寫著[1]":
         
        resultDICT["number"] = args[1]

    if utterance == "[上面]有[1]":
         
        resultDICT["number"] = args[1]

    if utterance == "[上面]有[一個][1]":
         
        resultDICT["number"] = args[2]

    if utterance == "[上面]有刻[一個][1]":
         
        resultDICT["number"] = args[2]

    if utterance == "[上面]的字是[1]":
         
        resultDICT["number"] = args[1]

    if utterance == "他印[1]":
         
        resultDICT["number"] = args[0]

    if utterance == "刻了[1]":
         
        resultDICT["number"] = args[0]

    if utterance == "印有[1]":
         
        resultDICT["number"] = args[0]

    if utterance == "寫著[1]":
         
        resultDICT["number"] = args[0]

    if utterance == "有[個][1]":
         
        resultDICT["number"] = args[1]

    return resultDICT