#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Career

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Career = True
userDefinedDICT = {"找": ["尋找", "找尋", "列出", "知道"], "泛稱": ["全台首富", "晶片大亨"], "類型": ["公立大學", "私立大學", "公立科技大學", "私立科技大學", "軍警院校"], "外文系": ["外國語文學系"], "資訊系": ["資訊工程學系"], "公司名稱": ["皮克斯", "聯發科", "微軟"], "台灣大學": ["台大", "國立台灣大學"], "工作動詞": ["煮飯", "攝影", "教學"], "成功大學": ["成大", "國立成功大學", "成功大學"], "人名的職業": ["郭台銘", "川普"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Career:
        print("[Career] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    
    resultDICT["career"] = []
    
    if utterance == "[我]想要當[廚師]":
        # write your code here
        resultDICT["career"].append(args[1])
        

    if utterance == "[我]要做[煮飯]的工作":
        # write your code here
        resultDICT["career"].append(args[1])


    if utterance == "[我]要去拍攝[電影]":
        # write your code here
        resultDICT["career"].append(args[1])

    
    if utterance == "怎麼當[老師]":
        resultDICT["career"].append(args[0])


    if utterance == "要當[老師]要讀什麼":
        resultDICT["career"].append(args[0])


    if utterance == "讀什麼[可以]當[老師]":
        resultDICT["career"].append(args[1])

    return resultDICT

