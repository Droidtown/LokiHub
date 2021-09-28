#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for study

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_study = True
userDefinedDICT = {"問": ["問", "算", "請問", "問一下"], "想": ["想", "想要", "要"], "事業": ["事業", "工作", "工程", "案子", "標案", "事業運", "募資", "計畫", "企劃", "企劃案", "事業狀況", "投資案", "工作狀況", "業績"], "單身": ["單身", "母胎單身"], "屢屢": ["屢屢", "一次次", "不斷", "一直", "一次次的"], "愛情": ["愛情", "感情", "婚姻", "姻緣", "正緣", "桃花", "桃花運", "愛情運", "感情運", "感情狀況", "相處狀況"], "最近": ["最近", "近期", "這陣子"], "求職": ["求職", "求職運", "找工作", "面試", "求職狀況", "求職情況", "換工作"], "考運": ["考試", "升學", "升高中", "升大學", "會考", "考會考", "學測", "考學測", "考研究所", "期中考", "期末考", "月考", "模擬考", "檢定考", "檢定", "上機考", "考運", "考試運", "考試情形", "考試狀況"], "脫單": ["脫單", "脫離單身"], "運勢": ["運勢", "流年", "運氣", "手氣"], "順利": ["順利", "順心", "太順利", "太順心"], "另一半": ["另一半", "男友", "女友", "老公", "老婆", "太太", "先生"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_study:
        print("[study] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[下禮拜]有[考試]":
        if args[1] in userDefinedDICT["考運"]:
            resultDICT["ask"]="考試"

    if utterance == "[我][今年]有[一場][考試]":
        if args[3] in userDefinedDICT["考運"]:
            resultDICT["ask"]="考試"

    if utterance == "[我][今年]有[考試]":
        if args[2] in userDefinedDICT["考運"]:
            resultDICT["ask"]="考試"

    if utterance == "[我][想][問][最近]的[考試]":
        if args[4] in userDefinedDICT["考運"]:
            resultDICT["ask"]="考試"

    if utterance == "[我][想][問][最近]的[考試]如何":
        if args[4] in userDefinedDICT["考運"]:
            resultDICT["ask"]="考試"

    if utterance == "[我][想][問][考試]":
        if args[3] in userDefinedDICT["考運"]:
            resultDICT["ask"]="考試"

    if utterance == "[我][想][問][考試][順]不[順利]":
        if args[3] in userDefinedDICT["考運"]:
            resultDICT["ask"]="考試"

    if utterance == "[我][想][問]關於[考試]的部分":
        if args[3] in userDefinedDICT["考運"]:
            resultDICT["ask"]="考試"

    if utterance == "[我][想]知道[考試]結果如何":
        if args[2] in userDefinedDICT["考運"]:
            resultDICT["ask"]="考試"

    if utterance == "[我]會考[上]嗎?":
        resultDICT["ask"]="考試"

    if utterance == "[最近][考試]不太好":
        if args[1] in userDefinedDICT["考運"]:
            resultDICT["ask"]="考試"
            
    if utterance == "不知道[考試][順]不[順利]":
        if args[0] in userDefinedDICT["考運"]:
            resultDICT["ask"]="考試"

    if utterance == "[想][問][下]個月考試結果":
        resultDICT["ask"]="考試"

    if utterance == "[想][問][考試][成績]":
        if args[2] in userDefinedDICT["考運"]:
            resultDICT["ask"]="考試"

    if utterance == "[想][問][考試][成績]方面":
        if args[2] in userDefinedDICT["考運"]:
            resultDICT["ask"]="考試"

    return resultDICT