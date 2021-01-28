#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for shape
    
    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict
    
    Output:
        resultDICT    dict
"""

DEBUG_shape = True
userDefinedDICT = {"粉": ["粉末", "粉狀"], "液體": ["液狀物", "液狀", "液態"], "網紅": [""], "落紅": [""], "紅不讓": [""], "膜衣錠": ["膜衣錠"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_shape:
        print("[shape] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    if utterance == "[三][角形][膜衣錠]":
        if args[2] == "膜衣錠":
            resultDICT["shape"] = args[0]+args[1]+"%20"+args[2]
        else:
            resultDICT["shape"] = args[0]+args[1]

    if utterance == "[五][角形]的藥丸":
        if args[1] == "角形":
            resultDICT["shape"].append(args[0]+args[1])

    if utterance == "[五][角形]藥片":
        if args[1] == "角形":
            resultDICT["shape"] = args[0]+args[1]

    if utterance == "[圓形]":
        if "形" in args[0]:
            resultDICT["shape"] = args[0]

    if utterance == "[裡面]有橘色的[粉末]":
        resultDICT["shape"] = args[1]

    if utterance == "應該是[膠囊]":
        resultDICT["shape"] = args[0]

    if utterance == "我有[一顆]白色[圓形]的藥丸":
        if "形" in args[1]:
            resultDICT["shape"] = args[1]

    if utterance == "我有[一顆]白色的[三][角形]藥片":
        if args[2] == "角形":
            resultDICT["shape"] = args[1]+args[2]

    if utterance == "我有[一顆]白色的圓形藥丸":
        resultDICT["shape"] = ""

    if utterance == "我有[一顆]白色的藥丸[圓圓]的":
        resultDICT["shape"] = args[1]

    if utterance == "我有[一顆]白色的藥丸他是[圓形]的":
        if "形" in args[1]:
            resultDICT["shape"] = args[1]

    if utterance == "是[一顆][膠囊]":
        resultDICT["shape"] = args[1]

    if utterance == "白色[三角形][膜衣錠]":
        if args[1] == "膜衣錠":
            resultDICT["shape"] = args[0]+"%20"+args[1]
        else:
            resultDICT["shape"] = args[0]

    if utterance == "白色[圓][柱形][膜衣錠]":
        if args[2] == "膜衣錠":
            resultDICT["shape"] = args[0]+args[1]+"%20"+args[2]
        else:
            resultDICT["shape"] = args[0]+args[1]

    if utterance == "看起來是[方形]的[藥丸]":
        if "形" in args[0]:
            resultDICT["shape"] = args[0]

    if utterance == "看起來是[膠囊]":
        resultDICT["shape"] = args[0]

    if utterance == "粉末":
        resultDICT["shape"] = "粉末"

    if utterance == "黃色的[粉]":
        resultDICT["shape"] = "粉"
    
    if utterance == "[一個][圓圓]的粉紅色藥丸":
        dict = set(args[1]) # set()去重複化（會變成dict）
        resultDICT["shape"] = dict.pop() # 取出dict裡的東西
    
    if utterance == "藍色[圓圓]小藥丸":
        dict = set(args[0]) # set()去重複化（會變成dict）
        resultDICT["shape"] = dict.pop() # 取出dict裡的東西

    return resultDICT
