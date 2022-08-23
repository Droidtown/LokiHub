#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for dividend

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

DEBUG_dividend = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_soup":["broth","chowder","consomme","consommé","cream","cream of chicken","cream of mushroom","cream of tomato","gazpacho","mulligatawny","puree","veloute","velouté","vichyssoise"],"_tmpFix":["Andrew's","Dean's"],"_MassNounUnit":["block","bottle","box","bucket","case","chunk","cup","glass","handful","mouthful","pair","piece","pile","string"]}

# Debug message
def debugInfo(inputSTR, utterance):
    if DEBUG_dividend:
        print("[dividend] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "The [school] have [$20,000]":
        # write your code here
        pass

    if utterance == "[Allan] have [49] [blocks] and there be [7] [blocks] [for] [every] [color]":
        # write your code here
        pass

    if utterance == "[If] [brand] A be [$50] [for] [5 kg]":
        # write your code here
        pass

    if utterance == "[Melissa] buy [2 packs of] [tennis] [balls] [for] [$12] [in] [total]":
        # write your code here
        pass

    if utterance == "[She] buy [88] [pink] [flower] [stones] and want [to] make [8] [bracelets]":
        # write your code here
        pass

    if utterance == "[brand] [B] be [$48] [per] [4 kg]":
        # write your code here
        pass

    if utterance == "[she] have [54] [sunflower] [seeds] and there be [9] [cans]":
        # write your code here
        pass

    if utterance == "[you] have [4 pieces of] [candy] split [evenly] [into] [2] [bags]":
        # write your code here
        pass

    if utterance == "[you] have [80] [tickets] [for] the [fair] and [each] [ride] costs [5] [tickets]":
        # write your code here
        pass

    return resultDICT