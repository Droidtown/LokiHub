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
    userDefinedDICT = {"_soup":["broth","chowder","consomme","consommé","cream","cream of chicken","cream of mushroom","cream of tomato","gazpacho","mulligatawny","puree","veloute","velouté","vichyssoise"],"_tmpFix":["Andrew's","Dean's"],"_MassNounUnit":["block","bottle","box","bucket","case","chunk","cup","glass","handful","mouthful","pair","piece","pile","string"]}

# Debug message
def debugInfo(inputSTR, utterance):
    if DEBUG_divisor:
        print("[divisor] {} ===> {}".format(inputSTR, utterance))

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

    if utterance == "[each] [piece] [of] [equipment] cost [$50]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[0] in ("every", "each", "one", "evenly", "per", "for"):
            # 1. Assign Symbols
            entityX = "money_{}".format(sgForm(args[3]))
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[4])

    if utterance == "[Every] [crayon] [box] can contain [8] [crayons]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[0] in ("every", "each", "one", "evenly", "per", "for"):
            # 1. Assign Symbols
            entityX = sgForm(args[4])
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[3])

    if utterance == "[If] [14 pieces of] [stone] be [in] [each] [bracelet]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[4] in ("every", "each", "one", "evenly", "per", "for"):
            # 1. Assign Symbols
            entityX = sgForm(args[2])
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[1])

    if utterance == "[each] [glass] need [two] [lemons]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[0] in ("every", "each", "one", "evenly", "per", "for"):
            # 1. Assign Symbols
            entityX = sgForm(args[3])
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[2])

    if utterance == "[equal] [number] [of] [paintings] [in] [four] [of] the [rooms]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[0] in ("every", "each", "one", "evenly", "per", "for"):
            # 1. Assign Symbols
            entityX = sgForm(args[7])
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[5])

    if utterance == "[every] [box] can contain [100] [sheets]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[0] in ("every", "each", "one", "evenly", "per", "for"):
            # 1. Assign Symbols
            entityX = sgForm(args[3])
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[2])

    if utterance == "[every] [packet] need [to] contain [7] [seeds]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[0] in ("every", "each", "one", "evenly", "per", "for"):
            # 1. Assign Symbols
            entityX = sgForm(args[4])
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[3])

    if utterance == "[it] take [3] [cutlets] [to] make a [dish]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[2])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1])

    if utterance == "[paper] [envelopes] which can hold [10] [papers] [each]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[4] in ("every", "each", "one", "evenly", "per", "for"):
            # 1. Assign Symbols
            entityX = sgForm(args[3])
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[2])

    if utterance == "[she] give [to] [each] [of] her [two] [grandmothers]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[2] in ("every", "each", "one", "evenly", "per", "for"):
            # 1. Assign Symbols
            entityX = sgForm(args[5])
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[4])

    if utterance == "[they] leave [exactly] [7] [nails] [in] [every] [station]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[5] in ("every", "each", "one", "evenly", "per", "for"):
            # 1. Assign Symbols
            entityX = sgForm(args[3])
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[2])

    return resultDICT