#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Inquiry

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Inquiry = True
userDefinedDICT = {"找": ["尋找", "找尋", "列出", "知道"], "泛稱": ["全台首富", "晶片大亨"], "類型": ["公立大學", "私立大學", "公立科技大學", "私立科技大學", "軍警院校"], "外文系": ["外國語文學系"], "資訊系": ["資訊工程學系"], "公司名稱": ["皮克斯", "聯發科", "微軟"], "台灣大學": ["台大", "國立台灣大學"], "工作動詞": ["煮飯", "攝影", "教學"], "成功大學": ["成大", "國立成功大學", "成功大學"], "人名的職業": ["郭台銘", "川普"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Inquiry:
        print("[Inquiry] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == " [成大][外文系]":
        # write your code here
        pass

    if utterance == "[外文系]":
        # write your code here
        pass

    if utterance == "[成大][外文系][可以]做什麼":
        # write your code here
        pass

    if utterance == "[成大][外文系]出路":
        # write your code here
        pass

    if utterance == "[成大][外文系]分享":
        # write your code here
        pass

    if utterance == "[成大][外文系]好不[好]":
        # write your code here
        pass

    if utterance == "[成大][外文系]畢業出路":
        # write your code here
        pass

    if utterance == "[成大][外文系]畢業工作":
        # write your code here
        pass

    if utterance == "[成大][外文系]當老師":
        # write your code here
        pass

    if utterance == "[我]想找[成大][外文系]":
        # write your code here
        pass

    if utterance == "[我]想要找[成大][外文系]":
        # write your code here
        pass

    if utterance == "[我]要找[台大][外文系]和[資訊系]":
        # write your code here
        pass

    if utterance == "[我]要找[成大][外文系]":
        # write your code here
        pass

    if utterance == "[我]要找[成大][外文系]和[台大][資訊系]":
        # write your code here
        pass

    if utterance == "[我]要找[成大]和[台大][外文系]":
        # write your code here
        pass

    if utterance == "有沒[有][成大][外文系]":
        # write your code here
        pass

    if utterance == "請問有沒[有][成大][外文系]":
        # write your code here
        pass

    return resultDICT