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

from cgitb import text
from hashlib import new
from inspect import ArgSpec
import json
import os
from sre_constants import AT_END_STRING
from unittest import result

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
        newSTR = inputSTR.replace('對面','面對面')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'faceToface'

    if utterance == "[他們]怕給[家人]新冠肺炎":
        newSTR = inputSTR.replace('給','傳染給')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'contract'

    if utterance == "[你]的話讓[我]返老還童":
        newSTR = inputSTR.replace('返老還童','充滿希望')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'word'

    if utterance == "[大部分]的[美國][學生]的[成績][都]變壞了":
        newSTR = inputSTR.replace('壞','差')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'huai'

    if utterance == "[她]看得很一心一意":
        newSTR = inputSTR.replace('一心一意','專心')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'word'

    if utterance == "[學生][可以]用[網路]參加學習的事情":
        newSTR = inputSTR.replace('的事情','')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'sent2'

    if utterance == "[常常]有很同的[看法]":
        newSTR = inputSTR.replace('同','相同')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'same'

    if utterance == "[應]為記得[我]很簡單的生活":
        newSTR = inputSTR.replace('應','因')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'because'

    if utterance == "[我]對[我]的[家庭][生活]感到尷尬":
        newSTR = inputSTR.replace('尷尬','不好意思')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'embarrassed'

    if utterance == "[我]希望[我們][可以]很快得把新冠肺炎拿走了":
        newSTR = inputSTR.replace('得把','解決').replace('拿走了','的問題')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'sent8'

    if utterance == "[我]希望[春]草[將]來不[會]依靠[何水遠]帶來[快樂]":
        newSTR = inputSTR.replace('會','用')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'need'

    if utterance == "[我]會報告[新館肺炎]對[這三個][部分]怎麼樣":
        if args[1] == '新館肺炎':
            newSTR = inputSTR.replace('新館肺炎','新冠肺炎').replace('怎麼樣','的影響')
        else:
            newSTR = inputSTR.replace('怎麼樣','的影響')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'yingxiang'

    if utterance == "[我]的[家庭]經驗了[很多]":
        newSTR = inputSTR.replace('經驗','經歷')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'experience'

    if utterance == "[我]的[生活]不是很壞":
        newSTR = inputSTR.replace('壞','差')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'huai'

    if utterance == "[我們]的[生活]和[經濟][都]變化了":
        newSTR = inputSTR.replace('變化','改變')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'change'

    if utterance == "[新冠肺炎][確實]對每[一個][人]有真不好的[影響]":
        newSTR = inputSTR.replace('真','很')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'word'

    if utterance == "[春]草的[性格]很強":
        newSTR = inputSTR.replace('性格','個性').replace('強','堅強')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'gexing'

    if utterance == "[當然]不是成心的":
        newSTR = inputSTR.replace('成','真')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'word'

    if utterance == "從[經濟]和[政治]到[人民]的人精和[人際][關係]":
        newSTR = inputSTR.replace('人精','精神')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'word'

    if utterance == "我[兄弟][姐妹]給[我]很深的幸福":
        newSTR = inputSTR.replace('給','讓').replace('很','感到深')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'word'

    if utterance == "把[美國][人]的[生活][都]改變了的一乾二淨":
        newSTR = inputSTR.replace('的一乾二淨','')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'change'

    if utterance == "最[小些]的[孩子]有戴口罩問題":
        newSTR = '最'+args[0][0]+'的'+args[1]+'有戴口罩問題'
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'zui'

    if utterance == "開始[自己]賺和化錢":
        newSTR = '開始'+args[0]+'賺錢和花錢'
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'word'

    if utterance == "防疫[戰術]的[輕重也]在增加":
        newSTR = inputSTR.replace('輕重也','政策')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'word'

    resultDICT['inq'] = None #inq的值為None

    return resultDICT