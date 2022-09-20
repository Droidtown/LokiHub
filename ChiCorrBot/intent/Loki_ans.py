#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for ans

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

with open("./account.info", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())

articut = Articut(username=accountDICT['username'], apikey=accountDICT['articut_key'])

DEBUG_ans = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"否":["NO","No","no","N","n","不是","不是的","不對"],"是":["YES","Yes","yes","Y","y","是的","對","對的"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_ans:
        print("[ans] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    
    if utterance == "[resp]":
        resultDICT = articut.parse(inputSTR)
        if resultDICT['result_obj'][0][0]['pos'] == 'ENTITY_oov':
            if args[0] in userDefinedDICT['_agreeExp']:
                resultDICT['inq'] = '是'
            elif args[0] in userDefinedDICT['_disagreeExp']:
                resultDICT['inq'] = '否'

    if utterance == "[對]":
        if len(inputSTR) == 1:
            resultDICT['inq'] = '是' #「對」為是
        elif len(inputSTR) == 2:
            resultDICT['inq'] = '否' #「不對」為否

    if utterance == "不是":
        resultDICT['inq'] = '否'

    if utterance == "否":
        resultDICT['inq'] = '否'

    if utterance == "是":
        resultDICT['inq'] = '是'

    return resultDICT