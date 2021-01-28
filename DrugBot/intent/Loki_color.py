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
userDefinedDICT = {"液體": ["液狀物", "液狀", "液態"], "網紅": [""], "落紅": [""], "紅不讓": [""]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_color:
        print("[color] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[半][透明]的":
        # write your code here
        if "透明" == args[-1]:
            resultDICT["color"] = args[-2]+args[-1]


    if utterance == "[粉色]藥丸":
        if "色" in args[0]:
            resultDICT["color"] = args[0]
        # write your code here

    if utterance == "[白色]圓形的藥丸":
        if "色" in args[0]:
            resultDICT["color"] = args[0]

    if utterance == "[紅][棕色]":
        if "棕色" == args[1]:
            resultDICT["color"] = args[0]+args[1]


    if utterance == "[紅][棕色]膠囊":
        if "棕色" == args[1]:
            resultDICT["color"] = args[0]+args[1]
        # write your code here


    if utterance == "[紅]膠囊":
        resultDICT["color"] = args[0]
        # write your code here


    if utterance == "[紅]藥丸":
        resultDICT["color"] = args[0]
        # write your code here


    if utterance == "[紅]藥片":
        # write your code here
        resultDICT["color"] = args[0]


    if utterance == "[紅紅]的":
        # write your code here
        resultDICT["color"] = args[0]


    if utterance == "[透明]的":
        # write your code here
        resultDICT["color"] = args[0]


    if utterance == "好像是[紅]的":
        # write your code here
        resultDICT["color"] = args[0]


    if utterance == "看起來[紅紅]的":
        # write your code here
        resultDICT["color"] = args[0]


    if utterance == "看起來是[紅色]":
        # write your code here
        resultDICT["color"] = args[0]

    if utterance == "[紅色]跟[黑色]的":
        resultDICT["color"] = args[0]+'%20'+args[1]
    
    if utterance == "[白色]":
        resultDICT["color"] = args[0]

    if utterance == "[白色]三角形藥丸":
        resultDICT["color"] = args[0]



    return resultDICT