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
from .ArticutToolbox.NumberTools import numExtractor
from .ArticutToolbox.TextTools import sgForm, sympyKey
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

def entity2symbol(resultDICT, entitySTR):
    '''
    Assign Symbols to resultDICT["symbolDICT"]
    '''
    entitySTR = sgForm(entitySTR)
    if entitySTR in resultDICT["symbolDICT"].keys():
        pass
    else:
        resultDICT["symbolDICT"][entitySTR] = []
    return resultDICT

def symbol2variable(resultDICT, entitySTR):
    '''
    Assign variables to Symbols in resultDICT["symbolDICT"]
    '''
    entitySTR = sgForm(entitySTR)
    if "{}_{}".format(sympyKey(entitySTR), len(resultDICT["symbolDICT"][entitySTR])) in resultDICT["symbolDICT"][entitySTR]:
        variableX = sympy.Symbol("{}_{}".format(sympyKey(entitySTR), len(resultDICT["symbolDICT"][entitySTR])+1))
    else:
        variableX = sympy.Symbol("{}_{}".format(sympyKey(entitySTR), len(resultDICT["symbolDICT"][entitySTR])))
    return variableX

def value2variable(resultDICT, entitySTR, variableX, numberSTR):
    '''
    Assign value to the variable
    '''
    entitySTR = sgForm(entitySTR)
    number = numExtractor(numberSTR)
    resultDICT["symbolDICT"][entitySTR].append((variableX, number))
    resultDICT["symbolLIST"].append((variableX, number))
    return resultDICT

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "The [school] have [$20,000]":
        # write your code here
        pass

    if utterance == "[Melissa] buy [2] pack [of] [tennis] [balls] [for] [$12] [in] [total]":
        # write your code here
        pass

    if utterance == "[you] have [4] [pieces of] [candy] split [evenly] [into] [2] [bags]":
        # write your code here
        pass

    if utterance == "[you] have [80] [tickets] [for] the [fair] and [each] ride costs [5] [tickets]":
        # write your code here
        pass

    if utterance == "[Allan] have [49] [blocks] and there be [7] [blocks] [for] [every] [color]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[6] in ("every", "each", "one", "1"):
            # 1. Assign Symbols
            entityX = args[2]
            entityY = args[4]
            resultDICT = entity2symbol(resultDICT, entityX)
            resultDICT = entity2symbol(resultDICT, entityY)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            y = symbol2variable(resultDICT, entityY)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[1])
            resultDICT = value2variable(resultDICT, entityY, y, args[3])

    if utterance == "[If] [brand] A be [$50] [for] [5 kg]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[3] in ("every", "each", "one", "evenly", "per", "for"):
            # 1. Assign Symbols
            entityX = "money_{}".format(sgForm(args[4]))
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[2])

    if utterance == "[Melissa] buy [2 packs of] [tennis] [balls] [for] [$12] [in] [total]":
        # write your code here
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[4] in ("every", "each", "one", "evenly", "per", "for"):
            # 1. Assign Symbols
            entityX = "money_{}".format(sgForm(args[1]))
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[5])

    if utterance == "[She] buy [88] [pink] [flower] [stones] and want [to] make [8] [bracelets]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[1] in ("every", "each", "one", "1"):
            # 1. Assign Symbols
            entityX = args[4]
            entityY = args[7]
            resultDICT = entity2symbol(resultDICT, entityX)
            resultDICT = entity2symbol(resultDICT, entityY)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            y = symbol2variable(resultDICT, entityY)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[1])
            resultDICT = value2variable(resultDICT, entityY, y, args[6])

    if utterance == "[brand] [B] be [$48] [per] [4 kg]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[3] in ("every", "each", "one", "evenly", "per"):
            # 1. Assign Symbols
            entityX = "money_{}".format(sgForm(args[4]))
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[2])

    if utterance == "[she] have [54] [sunflower] [seeds] and there be [9] [cans]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = args[2]
        entityY = args[4]
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1])
        resultDICT = value2variable(resultDICT, entityY, y, args[3])

    if utterance == "[you] have [4 pieces of] [candy] split [evenly] [into] [2] [bags]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[1] in ("every", "each", "one", "evenly"):
            # 1. Assign Symbols
            entityX = args[2]
            entityY = args[5]
            resultDICT = entity2symbol(resultDICT, entityX)
            resultDICT = entity2symbol(resultDICT, entityY)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            y = symbol2variable(resultDICT, entityY)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[1])
            resultDICT = value2variable(resultDICT, entityY, y, args[4])

    if utterance == "[you] have [80] [tickets] [for] the [fair] and [each] [ride] costs [5] [tickets]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[1] in ("every", "each", "one", "1"):
            # 1. Assign Symbols
            entityX = args[2]
            entityY = args[8]
            resultDICT = entity2symbol(resultDICT, entityX)
            resultDICT = entity2symbol(resultDICT, entityY)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            y = symbol2variable(resultDICT, entityY)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[1])
            resultDICT = value2variable(resultDICT, entityY, y, args[7])

    return resultDICT