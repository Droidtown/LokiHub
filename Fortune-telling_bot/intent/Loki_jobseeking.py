#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for jobseeking

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_jobseeking = True
userDefinedDICT = {"問": ["問", "算", "請問", "問一下"], "想": ["想", "想要", "要"], "事業": ["事業", "工作", "工程", "案子", "標案", "事業運", "募資", "計畫", "企劃", "企劃案", "事業狀況", "投資案", "工作狀況", "業績"], "單身": ["單身", "母胎單身"], "屢屢": ["屢屢", "一次次", "不斷", "一直", "一次次的"], "愛情": ["愛情", "感情", "婚姻", "姻緣", "正緣", "桃花", "桃花運", "愛情運", "感情運", "感情狀況", "相處狀況"], "最近": ["最近", "近期", "這陣子"], "求職": ["求職", "求職運", "找工作", "面試", "求職狀況", "求職情況", "換工作"], "考運": ["考試", "升學", "升高中", "升大學", "會考", "考會考", "學測", "考學測", "考研究所", "期中考", "期末考", "月考", "模擬考", "檢定考", "檢定", "上機考", "考運", "考試運", "考試情形", "考試狀況"], "脫單": ["脫單", "脫離單身"], "運勢": ["運勢", "流年", "運氣", "手氣"], "順利": ["順利", "順心", "太順利", "太順心"], "另一半": ["另一半", "男友", "女友", "老公", "老婆", "太太", "先生"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_jobseeking:
        print("[jobseeking] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我][之後]有[一場]面試":
        resultDICT["ask"]="求職"

    if utterance == "[我][想][問][最近]的[求職狀況]":
        if args[4] in userDefinedDICT["求職"]:
            resultDICT["ask"]="求職"

    if utterance == "[我][想][問][求職]":
        if args[3] in userDefinedDICT["求職"]:
            resultDICT["ask"]="求職"

    if utterance == "[我][想][問][求職][順]不[順利]":
        if args[3] in userDefinedDICT["求職"]:
            resultDICT["ask"]="求職"

    if utterance == "[我][想][算]關於[求職]的部分":
        if args[3] in userDefinedDICT["求職"]:
            resultDICT["ask"]="求職"

    if utterance == "[我][想][請問][最近]的[求職狀況]如何":
        if args[4] in userDefinedDICT["求職"]:
            resultDICT["ask"]="求職"

    if utterance == "[我]有[個]面試":
        resultDICT["ask"]="求職"

    if utterance == "[最近][找工作][屢屢]撲空":
        resultDICT["ask"]="求職"

    if utterance == "[最近][求職]不太好":
        if args[1] in userDefinedDICT["求職"]:
            resultDICT["ask"]="求職"

    if utterance == "[最近]的[求職運]不是很好":
        if args[1] in userDefinedDICT["求職"]:
            resultDICT["ask"]="求職"

    if utterance == "[下周]有[個]工作面試":
        resultDICT["ask"]="求職"

    if utterance == "[我][想要][找工作]":
        if args[2] in userDefinedDICT["求職"]:
            resultDICT["ask"]="求職"

    if utterance == "[最近][要][換工作]":
        if args[2] in userDefinedDICT["求職"]:
            resultDICT["ask"]="求職"

    return resultDICT