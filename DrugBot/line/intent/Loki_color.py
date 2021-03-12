#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for color

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_color = True
userDefinedDICT = {"粉": ["藥粉", "粉末", "粉狀"], "液體": ["液狀物", "液狀", "液態", "糖漿"], "膜衣錠": ["膜衣錠"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_color:
        print("[color] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[半][透明]的":
        if "透明" == args[-1]:
            resultDICT["color"] = args[-2]+args[-1]

    if utterance == "[白色]":
        resultDICT["color"] = args[0]
        if args[0] == "粉紅":
            resultDICT["color"] = "粉紅"

    if utterance == "[白色][三角形][藥丸]":
        resultDICT["color"] = args[0]

    if utterance == "[粉色][藥丸]":
        if "粉" in args[0]:
            resultDICT["color"] = "粉紅"

    if utterance == "[紅][棕色]":
        resultDICT["color"] = args[0] + args[1]

    if utterance == "[紅][棕色][膠囊]":
        resultDICT["color"] = args[0] + args[1]

    if utterance == "[紅][膠囊]":
        resultDICT["color"] = args[0]

    if utterance == "[紅色]跟[黑色]的":
        resultDICT["color"] = args[0]+'%20'+args[1]

    if utterance == "[透明]的":
        if args[0] =="透明":
            resultDICT["color"] = args[0]

    if utterance == "好像是[紅]的":
        resultDICT["color"] = args[0]

    if utterance == "看起來[紅紅]的":
        dict = set(args[0]) # set()去重複化（會變成dict）
        resultDICT["color"] = dict.pop() # 取出dict裡的東西

    if utterance == "看起來是[紅色]":
        resultDICT["color"] = args[0]

    if utterance == "[白色]的[六][角形][藥丸]":
        resultDICT["color"] = args[0]

    if utterance == "[一邊][白][一邊][紅]的[膠囊]":
        resultDICT["color"] = args[1]+"%20"+args[3]
    return resultDICT
