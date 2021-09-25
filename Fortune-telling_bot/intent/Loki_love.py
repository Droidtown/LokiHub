#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for love

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_love = True
userDefinedDICT = {"問": ["問", "算", "請問", "問一下"], "想": ["想", "想要", "要"], "事業": ["事業", "工作", "工程", "案子", "標案", "事業運", "募資", "計畫", "企劃", "企劃案", "事業狀況", "投資案", "工作狀況"], "單身": ["單身", "母胎單身"], "屢屢": ["屢屢", "一次次", "不斷", "一直", "一次次的"], "愛情": ["愛情", "感情", "婚姻", "姻緣", "正緣", "桃花", "桃花運", "愛情運", "感情運", "感情狀況", "相處狀況"], "最近": ["最近", "近期", "這陣子"], "求職": ["求職", "求職運", "找工作", "面試", "求職狀況", "求職情況", "換工作"], "考運": ["考試", "升學", "升高中", "升大學", "會考", "考會考", "學測", "考學測", "考研究所", "期中考", "期末考", "月考", "模擬考", "檢定考", "檢定", "上機考", "考運", "考試運", "考試情形", "考試狀況"], "脫單": ["脫單", "脫離單身"], "運勢": ["運勢", "流年", "運氣", "手氣"], "順利": ["順利", "順心", "太順利", "太順心"], "另一半": ["另一半", "女朋友", "男朋友", "男友", "女友", "老公", "老婆", "太太", "先生"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_love:
        print("[love] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[想要][請問][我]的[正緣]何時[才][會]出現":
        if args[3] in userDefinedDICT["愛情"]:
            resultDICT["ask"]="愛情"

    if utterance == "[我][單身]很久":
        resultDICT["ask"]="愛情"

    if utterance == "[我][想][問][感情]":
        if args[3] in userDefinedDICT["愛情"]:
            resultDICT["ask"]="愛情"

    if utterance == "[我][想][問][感情][順]不[順利]":
        if args[3] in userDefinedDICT["愛情"]:
            resultDICT["ask"]="愛情"

    if utterance == "[我][想][問][最近]的[愛情]":
        if args[4] in userDefinedDICT["愛情"]:
            resultDICT["ask"]="愛情"

    if utterance == "[我][想][問]關於[感情]的部分":
        if args[3] in userDefinedDICT["愛情"]:
            resultDICT["ask"]="愛情"

    if utterance == "[我][想][算][我][會]有[姻緣]嗎":
        if args[5] in userDefinedDICT["愛情"]:
            resultDICT["ask"]="愛情"

    if utterance == "[我][想][請問][我]跟另一半兩人[相處狀況]":
        resultDICT["ask"]="愛情"

    if utterance == "[我]何時[可以][脫單]":
        if args[2] in userDefinedDICT["脫單"]:
            resultDICT["ask"]="愛情"

    if utterance == "[我]好[想][脫單]":
        if args[2] in userDefinedDICT["脫單"]:
            resultDICT["ask"]="愛情"

    if utterance == "[我]的[愛情運]何時[才][可以][順利][點]":
        if args[1] in userDefinedDICT["愛情"]:
            resultDICT["ask"]="愛情"

    if utterance == "不知道[自己][下]個[桃花]何時[才][會]出現":
        if args[2] in userDefinedDICT["愛情"]:
            resultDICT["ask"]="愛情"

    if utterance == "[最近]有很多對象選擇":
        resultDICT["ask"]="愛情"

    if utterance == "[另一半]":
       if args[0] in userDefinedDICT["另一半"]:
            resultDICT["ask"]="愛情"

    if utterance == "[另一半]吵架":
        if args[0] in userDefinedDICT["另一半"]:
            resultDICT["ask"]="愛情"

    if utterance == "[另一半]處的不[好]":
        if args[0] in userDefinedDICT["另一半"]:
            resultDICT["ask"]="愛情"

    if utterance == "單戀":
        resultDICT["ask"]="愛情"

    if utterance == "暗戀":
        resultDICT["ask"]="愛情"

    return resultDICT