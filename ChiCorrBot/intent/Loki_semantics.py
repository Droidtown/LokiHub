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

from cgitb import text
import json
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
        # write your code here
        pass

    if utterance == "[可能]記得為什麼[他們]對眼":
        # write your code here
        pass

    if utterance == "[大部][美國]的部分選了人隔離":
        # write your code here
        pass

    if utterance == "[我][最]喜歡[一天][中]的[時間]":
        # write your code here
        pass

    if utterance == "[我]不[誠信]讓[你們]丟了[面子]":
        # write your code here
        pass

    if utterance == "[我]坦白了每個[我]說假的話":
        # write your code here
        pass

    if utterance == "[我]有多[本][書]":
        resDICT = articut.parse(inputSTR)
        textLIST = resDICT['result_segmentation'].split('/')
        print(f"你是想說「很多」{''.join(textLIST[-2:])}是嗎？")
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            resultDICT['suggestion'] = f"{''.join(textLIST[:2])}很{''.join(textLIST[-3:])}"
            resultDICT['error'] = 'duo'
        else:
            pass

    if utterance == "[我]看一看[父母]跟[一起]聊天了":
        # write your code here
        pass

    if utterance == "[我]看的[最近]":
        # write your code here
        pass

    if utterance == "[我]聽[音樂]的[時候]聽說過[一幅][畫]":
        # write your code here
        pass

    if utterance == "[我們][都]不喜歡[個]":
        # write your code here
        pass

    if utterance == "[我們]形成越來越神的[關係]":
        # write your code here
        pass

    if utterance == "[春]草跟[我]的[時候][她]性格[更輕鬆]":
        resDICT = articut.parse(inputSTR)
        textLIST = resDICT['result_suggestation'].split('/')
        print('你是要說你們「在一起」的時候嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            newSTR = re.sub('的時候','在一起的時候', inputSTR)
            newSTR = re.sub('性格', '', newSTR)
            resultDICT['suggestion'] = newSTR
            resultDICT['error'] = 'sent1'


    if utterance == "[這本][書]叫[我人][高興]":
        # write your code here
        pass

    if utterance == "[馬上]變成了[美國][人]的[生活]、[經濟]、[政治]":
        # write your code here
        pass

    if utterance == "有[一個]意思的[結局]":
        # write your code here
        pass

    if utterance == "看起來[這個][男孩子]深思":
        resDICT = articut.parse(inputSTR)
        verbSTR = resDICT['result_segmentation'].split('/')[-1]
        print(f'你的意思是「正在{verbSTR}」嗎？')
        ans = input('請輸入Y或N：')
        if ans == 'Y' or ans == 'y':
            #print(f"那你可以說：{resDICT.split('/')[:-1]}在{verbSTR}")
            #print(explanationDICT['prg'])
            resSTR = ''.join(resDICT['result_segmentation'].split('/')[:-1])
            resultDICT['suggestion'] = f"{resSTR}在{verbSTR}"
            resultDICT['error'] = 'prg'
        else:
            pass

    if utterance == "記得[我]的回憶[很難]的":
        # write your code here
        pass

    return resultDICT