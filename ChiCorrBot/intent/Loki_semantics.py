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
import re
from unittest import result
from ArticutAPI import Articut

with open('./intent/account.info', 'r', encoding='utf-8') as f:
    accountDICT = json.load(f)

articut = Articut(username=accountDICT['username'], apikey=accountDICT['articut_key'])


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
        print(f'你是說「讓{args[2]}更好」嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = inputSTR.replace('更好的','改善')
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'better'
        else:
            pass

    if utterance == "[可能]記得為什麼[他們]對眼":
        print('你說的「對眼」是「喜歡」的意思嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = inputSTR.replace('記得','想起').replace('對眼','喜歡彼此')
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'sent3'
        else:
            pass

    if utterance == "[大部][美國]的部分選了人隔離":
        print(f'你是說「很多{args[1]}的地方選擇了{utterance[-1]}」嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            if args[0].endswith('部') and args[0][0] in ('一','大'):
                newSTR = args[0]+'分'+args[1]+'的地方都'+'選了'+utterance[-2:]
            else:
                newSTR = '大部分'+args[1]+'的地方都'+'選了'+utterance[-2:]
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'part'
        else:
            pass

    if utterance == "[我][最]喜歡[一天][中]的[時間]":
        print(f'你是說「{args[0]}{args[1]}喜歡的{args[4]}」嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = args[0]+args[1]+'喜歡'+'的'+args[4]+'是+(某事物)'
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'favorite'
        else:
            pass

    if utterance == "[我]不[誠信]讓[你們]丟了[面子]":
        print(f'你是說「{args[0]}不{args[1]}是一件丟臉的事情」嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = args[0]+'的'+inputSTR[1:]
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'sent4'
        else:
            pass

    if utterance == "[我]坦白了每個[我]說假的話":
        print('你的意思是「說謊」嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = inputSTR.replace('假的話','的謊話')
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'lie'
        else:
            pass

    if utterance == "[我]有多[本][書]":
        print(f"你是想說「很多{args[1]}{args[2]}」是嗎？")
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = inputSTR[:2]+'很多'+args[1]+args[2]
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'duo'
        else:
            pass

    if utterance == "[我]看一看[父母]跟[一起]聊天了":
        print(f'你是說「{args[0]}和{args[1]}聊天」嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = inputSTR[:7]+'他們一起聊天'
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'gen'
        else:
            pass

    if utterance == "[我]看的[最近]":
        print(f'你是說「近期有看的書籍或影集」嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = args[0]+'最近'+inputSTR[1:3]+'(名詞)'
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'recently'
        else:
            pass

    if utterance == "[我]聽[音樂]的[時候]聽說過[一幅][畫]":
        print(f'你的意思是「{args[1]}裡提到{args[3]}{args[4]}」嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = inputSTR.replace('聽說過', '有提到')
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'content'
        else:
            pass

    if utterance == "[我們][都]不喜歡[個]":
        print(f'你的意思是「不喜歡前文提到的某事物」嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = inputSTR.replace('個','這個')
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'det'
        else:
            pass
            
    if utterance == "[我們]形成越來越神的[關係]":
        print(f'你是說「{args[1]}變好」嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = inputSTR.replace('越神','越好')
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'shen'
        else:
            pass

    if utterance == "[春]草跟[我]的[時候][她]性格[更輕鬆]":
        print('你是說你們「在一起」的時候嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = inputSTR[:4]+'在一起的時候'+args[3]+args[4]
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'sent1'
        else:
            pass

    if utterance == "[這本][書]叫[我人][高興]":
        print(f'你是說「你讀{args[0]}{args[1]}覺得高興」嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = args[0]+args[1]+'讓'+args[2][0]+args[3]
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'sentiment'
        else:
            pass

    if utterance == "[馬上]變成了[美國][人]的[生活]、[經濟]、[政治]":
        print(f'你是說「{args[1]}{args[2]}的{args[3]}、{args[4]}、{args[5]}受到影響」嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = inputSTR.replace('變成','改變')
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'change'
        else:
            pass

    if utterance == "有[一個]意思的[結局]":
        print(f'你是說「{args[1]}很有趣」嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = '有一個有意思的'+args[1]
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'youYiSi'
        else:
            pass

    if utterance == "看起來[這個][男孩子]深思":
        print(f'你的意思是「正在{inputSTR[-2:]}」嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = utterance[0]+args[0]+args[1]+'在'+inputSTR[-2:]
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'prg'
        else:
            pass

    if utterance == "記得[我]的回憶[很難]的":
        print('你是說「記得事情很困難」嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = args[0]+'的記憶不好'
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'memory'
        else:
            pass

    return resultDICT