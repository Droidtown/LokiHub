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

import json
import os

DEBUG_divisor = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_soup":["broth","chowder","consomme","consommé","cream","cream of chicken","cream of mushroom","cream of tomato","gazpacho","mulligatawny","puree","veloute","velouté","vichyssoise"],"_tmpFix":["Andrew's","Dean's"],"_MassNounUnit":["block","bottle","box","bucket","case","chunk","cup","glass","handful","mouthful","pair","piece","pile","string"]}

# Debug message
def debugInfo(inputSTR, utterance):
    if DEBUG_divisor:
        print("[divisor] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[Every] [crayon] [box] can contain [8] [crayons]":
        # write your code here
        pass

    if utterance == "[If] [14 pieces of] [stone] be [in] [each] [bracelet]":
        # write your code here
        pass

    if utterance == "[If] brand A be $50 [for] [5 kg]":
        # write your code here
        pass

    if utterance == "[Melissa] buy [2 packs of] [tennis] [balls]":
        # write your code here
        pass

    if utterance == "[each] [glass] need [two] [lemons]":
        # write your code here
        pass

    if utterance == "[each] piece [of] [equipment] cost [$50]":
        # write your code here
        pass

    if utterance == "[equal] number [of] [paintings] [in] [four] [of] the [rooms]":
        # write your code here
        pass

    if utterance == "[every] [box] can contain [100] [sheets]":
        # write your code here
        pass

    if utterance == "[every] [packet] need [to] contain [7] [seeds]":
        # write your code here
        pass

    if utterance == "[it] take [3] [cutlets] [to] make a [dish]":
        # write your code here
        pass

    if utterance == "[paper] [envelopes] which can hold [10] [papers] [each]":
        # write your code here
        pass

    if utterance == "[she] give [to] [each] [of] her [two] [grandmothers]":
        # write your code here
        pass

    if utterance == "[they] leave [exactly] [7] [nails] [in] [every] [station]":
        # write your code here
        pass

    if utterance == "[you] have [4 pieces of] [candy] split [evenly] [into] [2] [bags]":
        # write your code here
        pass

    if utterance == "[you] have [80] [tickets] [for] the [fair] and [each] [ride] costs [5] [tickets]":
        # write your code here
        pass

    if utterance == "brand B be $48 [per] [4 kg]":
        # write your code here
        pass

    if utterance == "there be [6] [tennis] [balls]":
        # write your code here
        pass

    return resultDICT