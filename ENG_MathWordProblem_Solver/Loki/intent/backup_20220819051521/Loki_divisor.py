#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for divisor

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""
from .ArticutToolbox.NumberTools import numExtractor
from .ArticutToolbox.TextTools import sgForm, sympyKey
import json
import os

DEBUG_divisor = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {}

# Debug message
def debugInfo(inputSTR, utterance):
    if DEBUG_divisor:
        print("[divisor] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[Melissa] buy [2] pack [of] [tennis] [balls]":
        # write your code here
        pass

    if utterance == "[each] [piece] [of] [equipment] cost [$50]":
        # write your code here
        pass

    if utterance == "[you] have [4] [pieces of] [candy] split [evenly] [into] [2] [bags]":
        # write your code here
        pass

    if utterance == "[you] have [80] [tickets] [for] the [fair] and [each] ride costs [5] [tickets]":
        # write your code here
        pass

    if utterance == "there be [6] [tennis] [balls]":
        # write your code here
        pass

    return resultDICT