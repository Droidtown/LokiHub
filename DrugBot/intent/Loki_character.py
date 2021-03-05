#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for character
    
    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict
    
    Output:
        resultDICT    dict
"""

DEBUG_character = True
userDefinedDICT = {"粉": ["藥粉", "粉末", "粉狀"], "液體": ["液狀物", "液狀", "液態", "糖漿"], "膜衣錠": ["膜衣錠"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_character:
        print("[character] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[上面]刻著[P]":
        resultDICT["character"] = args[1]

    if utterance == "[上面]刻著[一個][P]":
        resultDICT["character"] = args[2]

    if utterance == "[上面]印了[P]":
        resultDICT["character"] = args[1]

    if utterance == "[上面]印有[P]":
        resultDICT["character"] = args[1]

    if utterance == "[上面]印有[一個][P]":
        resultDICT["character"] = args[2]

    if utterance == "[上面]印的字是[P]":
        resultDICT["character"] = args[1]

    if utterance == "[上面]印著[P]":
        resultDICT["character"] = args[1]

    if utterance == "[上面]印著[一個][P]":
        resultDICT["character"] = args[2]

    if utterance == "[上面]寫[P]":
        resultDICT["character"] = args[1]

    if utterance == "[上面]寫了[一個][P]":
        resultDICT["character"] = args[2]

    if utterance == "[上面]寫著[P]":
        resultDICT["character"] = args[1]

    if utterance == "[上面]有[P]":
        resultDICT["character"] = args[1]
 
    if utterance == "[上面]有[一個][P]":
        resultDICT["character"] = args[2]

    if utterance == "[上面]有刻[一個][P]":
        resultDICT["character"] = args[2]

    if utterance == "[上面]的字是[P]":
        resultDICT["character"] = args[1]

    if utterance == "他印[P]":
        resultDICT["character"] = args[0]

    if utterance == "刻了[P]":
        resultDICT["character"] = args[0]

    if utterance == "印有[P]":
        resultDICT["character"] = args[0]

    if utterance == "寫著[P]":
        resultDICT["character"] = args[0]

    if utterance == "有[個][P]":
        resultDICT["character"] = args[1]
        
    if utterance == "橢圓形藥丸刻著[ＳＶ]":
        resultDICT["character"] = args[0]
        
    if utterance == "白色的錠狀[上面]有[一條][線]":
        resultDICT["character"] = args[2]

    return resultDICT
