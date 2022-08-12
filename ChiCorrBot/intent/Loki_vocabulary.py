#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for vocabulary

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
import os
from ArticutAPI import Articut

with open('./intent/account.info', 'r', encoding='utf-8') as f:
    accountDICT = json.load(f)

articut = Articut(username=accountDICT['username'], apikey=accountDICT['articut_key'])


DEBUG_vocabulary = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_vocabulary:
        print("[vocabulary] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一]年級[我]沒有[對面]的課":
        # write your code here
        pass

    if utterance == "[他們]怕給[家人]新冠肺炎":
        # write your code here
        pass

    if utterance == "[你]的話讓[我]返老還童":
        # write your code here
        pass

    if utterance == "[大部分]的[美國][學生]的[成績][都]變壞了":
        # write your code here
        pass

    if utterance == "[她]看得很一心一意":
        # write your code here
        pass

    if utterance == "[學生][可以]用[網路]參加學習的事情":
        # write your code here
        pass

    if utterance == "[常常]有很同的[看法]":
        # write your code here
        pass

    if utterance == "[應]為記得[我]很簡單的生活":
        # write your code here
        pass

    if utterance == "[我]對[我]的[家庭][生活]感到尷尬":
        # write your code here
        pass

    if utterance == "[我]希望[我們][可以]很快得把新冠肺炎拿走了":
        # write your code here
        pass

    if utterance == "[我]希望[春]草[將]來不[會]依靠[何水遠]帶來[快樂]":
        # write your code here
        pass

    if utterance == "[我]會報告[新館肺炎]對[這三個][部分]怎麼樣":
        resDICT = articut.parse(inputSTR)
        textLIST = resDICT['result_segmentation'].split('/')
        if textLIST[3] == '新館肺炎':
            textSTR = ''.join(textLIST[:3])+'新冠肺炎'+''.join(textLIST[4:7])+'的影響'
        else:
            textSTR = ''.join(textLIST[:-1])+'的影響'
        resultDICT['suggestion'] = textSTR
        resultDICT['error'] = 'yingxiang'

    if utterance == "[我]的[家庭]經驗了[很多]":
        # write your code here
        pass

    if utterance == "[我]的[生活]不是很壞":
        resDICT = articut.parse(inputSTR)
        textLIST = resDICT['result_segmentation'].split('/')
        textSTR = ''.join(textLIST[:-1])+'很差'
        resultDICT['suggestion'] = textSTR
        resultDICT['error'] = 'huai'

    if utterance == "[我們]的[生活]和[經濟][都]變化了":
        # write your code here
        pass

    if utterance == "[新冠肺炎][確實]對每[一個][人]有真不好的[影響]":
        # write your code here
        pass

    if utterance == "[春]草的[性格]很強":
        # write your code here
        pass

    if utterance == "[當然]不是成心的":
        # write your code here
        pass

    if utterance == "從[經濟]和[政治]到[人民]的人精和[人際][關係]":
        # write your code here
        pass

    if utterance == "我[兄弟][姐妹]給[我]很深的幸福":
        # write your code here
        pass

    if utterance == "把[美國][人]的[生活][都]改變了的一乾二淨":
        # write your code here
        pass

    if utterance == "最[小些]的[孩子]有戴口罩問題":
        # write your code here
        pass

    if utterance == "開始[自己]賺和化錢":
        # write your code here
        pass

    if utterance == "防疫[戰術]的[輕重也]在增加":
        # write your code here
        pass

    return resultDICT