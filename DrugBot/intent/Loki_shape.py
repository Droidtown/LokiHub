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
userDefinedDICT = {"粉": ["藥粉", "粉末", "粉狀"], "液體": ["液狀物", "液狀", "液態", "糖漿"], "膜衣錠": ["膜衣錠"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_shape:
        print("[shape] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一個][圓圓]的粉紅色藥丸":
        dict = set(args[1]) # set()去重複化（會變成dict）
        resultDICT["shape"] = dict.pop() # 取出dict裡的東西


    if utterance == "[一種][紅色]的[糖漿]":
        if args[2] == "糖漿" or args[2] == "粉末" or args[2] == "藥丸" or args[2] == "藥片" or args[2] == "膠囊"or args[2] == "膜衣錠":
            resultDICT["shape"] = args[2]

    if utterance == "[一種][紫色]的感冒[糖漿]":
        if args[2] == "糖漿" or args[2] == "粉末" or args[2] == "藥丸" or args[2] == "藥片" or args[2] == "膠囊"or args[2] == "膜衣錠":
            resultDICT["shape"] = args[2]

    if utterance == "[三][角形][膜衣錠]":
        if args[2] == "膜衣錠":
            resultDICT["shape"] = args[0]+args[1]+"%20"+args[2]

    if utterance == "[上面]刻A的[藥丸]":
        resultDICT["shape"] = args[1]

    if utterance == "[上面]有[P]的[紅色][膠囊]":
        if args[3] == "糖漿" or args[3] == "粉末" or args[3] == "藥丸" or args[3] == "藥片" or args[3] == "膠囊"or args[3] == "膜衣錠":
            resultDICT["shape"] = args[3]

    if utterance == "[上面]有[P]的[膠囊]":
        if args[2] == "糖漿" or args[2] == "粉末" or args[2] == "藥丸" or args[2] == "藥片" or args[2] == "膠囊"or args[2] == "膜衣錠":
            resultDICT["shape"] = args[2]

    if utterance == "[五][角形]的藥丸":
        resultDICT["shape"] = args[0] + args[1]

    if utterance == "[五][角形]藥片":
        resultDICT["shape"] = args[0] + args[1]

    if utterance == "[白色][三角形][膜衣錠]":
        if args[2] == "膜衣錠":
            resultDICT["shape"] = args[1]+"%20"+args[2]

    if utterance == "[白色][圓][柱形][膜衣錠]":
        if args[3] == "膜衣錠":
            resultDICT["shape"] = args[1]+args[2]+"%20"+args[3]

    if utterance == "[藍色][圓圓]小藥丸":
        dict = set(args[1]) # set()去重複化（會變成dict）
        resultDICT["shape"] = dict.pop() # 取出dict裡的東西

    if utterance == "[藥丸][上面]有EPP":
        resultDICT["shape"] = args[0]

    if utterance == "[裡面]有[橘色]的[粉末]":
        if args[2] == "糖漿" or args[2] == "粉末" or args[2] == "藥丸" or args[2] == "藥片" or args[2] == "膠囊"or args[2] == "膜衣錠":
            resultDICT["shape"] = args[2]

    if utterance == "[黃色][粉末]":
        if args[1] == "糖漿" or args[1] == "粉末" or args[1] == "藥丸" or args[1] == "藥片" or args[1] == "膠囊"or args[1] == "膜衣錠":
            resultDICT["shape"] = args[1]

    if utterance == "應該是[膠囊]":
        if args[0] == "糖漿" or args[1] == "粉末" or args[0] == "藥丸" or args[0] == "藥片" or args[0] == "膠囊"or args[0] == "膜衣錠":
            resultDICT["shape"] = args[0]

    if utterance == "我有[一顆][白色][圓形]的藥丸":
        resultDICT["shape"] = args[2]

    if utterance == "我有[一顆][白色]的[三][角形]藥片":
        resultDICT["shape"] = args[2]+args[3]

    if utterance == "我有[一顆][白色]的藥丸[圓圓]的":
        dict = set(args[2]) # set()去重複化（會變成dict）
        resultDICT["shape"] = dict.pop() # 取出dict裡的東西

    if utterance == "我有[一顆]白色的藥丸他是[圓形]的":
        resultDICT["shape"] = args[1]

    if utterance == "是[一顆][膠囊]":
        if args[1] == "糖漿" or args[1] == "粉末" or args[1] == "藥丸" or args[1] == "藥片" or args[1] == "膠囊"or args[1] == "膜衣錠":
            resultDICT["shape"] = args[1]

    if utterance == "是[圓形]的":
        if "形" in args[0]:
            resultDICT["shape"] = args[0]

    if utterance == "看起來是[方形]的[藥丸]":
        resultDICT["shape"] = args[0]

    if utterance == "看起來是[膠囊]":
        if args[0] == "糖漿" or args[0] == "粉末" or args[0] == "藥丸" or args[0] == "藥片" or args[0] == "膠囊"or args[0] == "膜衣錠":
            resultDICT["shape"] = args[0]
    
    if utterance == "是[圓]的[白色][藥丸]":
        resultDICT["shape"] = args[0]

    if utterance == "是[三][角形]的[紅色][藥丸]":
        resultDICT["shape"] = args[0]+args[1]

    if utterance == "是[方形]的[紅色][藥丸]":
        resultDICT["shape"] = args[0]

    return resultDICT