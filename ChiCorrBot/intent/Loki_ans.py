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
from msilib.schema import InstallUISequence
import os

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
    if utterance == "[是]":
        if args[0] in userDefinedDICT:
            resultDICT['inq'] = args[0]
        elif args[0] in userDefinedDICT['是']:
            resultDICT['inq'] = '是'
        elif args[0] in userDefinedDICT['否']:
            resultDICT['inq'] = '否'
        
    return resultDICT