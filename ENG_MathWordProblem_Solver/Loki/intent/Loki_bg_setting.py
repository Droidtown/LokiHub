#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for bg_setting

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

DEBUG_bg_setting = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_soup":["broth","chowder","consomme","consommé","cream","cream of chicken","cream of mushroom","cream of tomato","gazpacho","mulligatawny","puree","veloute","velouté","vichyssoise"],"_tmpFix":["Andrew's","Dean's"],"_MassNounUnit":["block","bottle","box","bucket","case","chunk","cup","glass","handful","mouthful","pair","piece","pile","string"]}

# Debug message
def debugInfo(inputSTR, utterance):
    if DEBUG_bg_setting:
        print("[bg_setting] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "There wasn’t [enough] [gum]":
        # write your code here
        pass

    if utterance == "[Ariel] be play [basketball]":
        # write your code here
        pass

    if utterance == "[if] [it] take [3] [cutlets] [to] make a [dish]":
        # write your code here
        pass

    if utterance == "find [two] [numbers]":
        # write your code here
        pass

    if utterance == "There be not [enough] [gum]":
        # write your code here
        pass

    if utterance == "[I] have two numbers":
        # write your code here
        pass

    return resultDICT