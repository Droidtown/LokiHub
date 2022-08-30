#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for semantics

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

from ast import arg
from cgitb import text
from hashlib import new
import json
from ntpath import join
import os
from unittest import result

DEBUG_semantics = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_semantics:
        print("[semantics] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[人們][應該]合作來更好的[生活]":
        inq = f'你是說「讓{args[2]}更好」嗎？'
        newSTR = inputSTR.replace('更好的','改善')
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'better'

    if utterance == "[可能]記得為什麼[他們]對眼":
        inq = '你說的「對眼」是「喜歡」的意思嗎？'
        newSTR = inputSTR.replace('記得','想起').replace('對眼','喜歡彼此')
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'sent3'

    if utterance == "[大部][美國]的部分選了人隔離":
        inq = f'你是說「很多{args[1]}的地方選擇了{utterance[-1]}」嗎？'
        if args[0].endswith('部') and args[0][0] in ('一','大'):
            newSTR = args[0]+'分'+args[1]+'的地方都'+'選了'+utterance[-2:]
        else:
            newSTR = '大部分'+args[1]+'的地方都'+'選了'+utterance[-2:]
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'part'

    if utterance == "[我][最]喜歡[一天][中]的[時間]":
        inq = f'你是說「{args[0]}{args[1]}喜歡的{args[4]}」嗎？'
        newSTR = args[0]+args[1]+'喜歡'+'的'+args[4]+'是+(某事物)'
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'favorite'

    if utterance == "[我]不[誠信]讓[你們]丟了[面子]":
        inq = f'你是說「{args[0]}不{args[1]}是一件丟臉的事情」嗎？'
        newSTR = args[0]+'的'+inputSTR[1:]
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'sent4'

    if utterance == "[我]坦白了每個[我]說假的話":
        inq = '你的意思是「說謊」嗎？'
        newSTR = inputSTR.replace('假的話','的謊話')
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'lie'

    if utterance == "[我]有多[本][書]":
        inq = f'你是想說「很多{args[1]}{args[2]}」是嗎？'
        newSTR = inputSTR[:2]+'很多'+args[1]+args[2]
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'duo'

    if utterance == "[我]看一看[父母]跟[一起]聊天了":
        inq = f'你是說「{args[0]}和{args[1]}聊天」嗎？'
        newSTR = inputSTR[:7]+'他們一起聊天'
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'gen'

    if utterance == "[我]看的[最近]":
        inq = f'你是說「近期有看的書籍或影集」嗎？'
        newSTR = args[0]+'最近'+inputSTR[1:3]+'(名詞)'
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'recently'

    if utterance == "[我]聽[音樂]的[時候]聽說過[一幅][畫]":
        inq = f'你的意思是「{args[1]}裡提到{args[3]}{args[4]}」嗎？'
        newSTR = inputSTR.replace('聽說過', '有提到')
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'content'

    if utterance == "[我們][都]不喜歡[個]":
        inq = f'你的意思是「不喜歡前文提到的某事物」嗎？'
        newSTR = inputSTR.replace('個','這個')
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'det'
            
    if utterance == "[我們]形成越來越神的[關係]":
        inq = f'你是說「{args[1]}變好」嗎？'
        newSTR = inputSTR.replace('越神','越好')
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'shen'

    if utterance == "[春]草跟[我]的[時候][她]性格[更輕鬆]":
        inq = '你是說你們「在一起」的時候嗎？'
        newSTR = inputSTR[:4]+'在一起的時候'+args[3]+args[4]
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'sent1'

    if utterance == "[這本][書]叫[我人][高興]":
        inq = f'你是說「你讀{args[0]}{args[1]}覺得高興」嗎？'
        newSTR = args[0]+args[1]+'讓'+args[2][0]+args[3]
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'sentiment'

    if utterance == "[馬上]變成了[美國][人]的[生活]、[經濟]、[政治]":
        inq = f'你是說「{args[1]}{args[2]}的{args[3]}、{args[4]}、{args[5]}受到影響」嗎？'
        newSTR = inputSTR.replace('變成','改變')
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'change'

    if utterance == "有[一個]意思的[結局]":
        inq = f'你是說「{args[1]}很有趣」嗎？'
        newSTR = '有一個有意思的'+args[1]
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'youYiSi'

    if utterance == "看起來[這個][男孩子]深思":
        inq = f'你的意思是「正在{inputSTR[-2:]}」嗎？'
        newSTR = utterance[0]+args[0]+args[1]+'在'+inputSTR[-2:]
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'prg'

    if utterance == "記得[我]的回憶[很難]的":
        inq = '你是說「記得事情很困難」嗎？'
        newSTR = args[0]+'的記憶不好'
        resultDICT['inq'] = inq
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'memory'

    return resultDICT