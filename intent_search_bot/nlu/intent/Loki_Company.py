#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Company

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Company = True
userDefinedDICT = {"找": ["尋找", "找尋", "列出", "知道"], "泛稱": ["全台首富", "晶片大亨"], "類型": ["公立大學", "私立大學", "公立科技大學", "私立科技大學", "軍警院校"], "外文系": ["外國語文學系"], "資訊系": ["資訊工程學系"], "公司名稱": ["皮克斯", "聯發科", "微軟"], "台灣大學": ["台大", "國立台灣大學"], "工作動詞": ["煮飯", "攝影", "教學"], "成功大學": ["成大", "國立成功大學", "成功大學"], "人名的職業": ["郭台銘", "川普"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Company:
        print("[Company] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    
    resultDICT["company"] = []
    
    if utterance == "[我]要去[微軟]上班":
        # write your code here
        resultDICT["company"].append(args[1])


    if utterance == "[我]要去[聯發科]工作":
        # write your code here
        resultDICT["company"].append(args[1])


    if utterance == "[微軟]工作":
        resultDICT["company"].append(args[0])
 
 
    if utterance == "怎麼去[微軟]上班":
        resultDICT["company"].append(args[0])


    if utterance == "怎麼去[微軟]工作":
        resultDICT["company"].append(args[0])


    if utterance == "怎麼進[微軟]":
        resultDICT["company"].append(args[0])
        
        
    if utterance == "讀什麼[可以]去[微軟]":
        resultDICT["company"].append(args[1])
        

    if utterance == "讀什麼[可以]進[微軟]":
        resultDICT["company"].append(args[1])


    if utterance == "讀什麼系[可以]去[微軟]":
        resultDICT["company"].append(args[1])


    return resultDICT