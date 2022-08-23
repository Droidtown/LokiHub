#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for multiplier

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
import sympy

DEBUG_multiplier = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_soup":["broth","chowder","consomme","consommé","cream","cream of chicken","cream of mushroom","cream of tomato","gazpacho","mulligatawny","puree","veloute","velouté","vichyssoise"],"_tmpFix":["Andrew's","Dean's"],"_MassNounUnit":["block","bottle","box","bucket","case","chunk","cup","glass","handful","mouthful","pair","piece","pile","string"]}

# Debug message
def debugInfo(inputSTR, utterance):
    if DEBUG_multiplier:
        print("[multiplier] {} ===> {}".format(inputSTR, utterance))


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

    if utterance == "A [bricklayer] stacks [bricks] [in] [2] [rows]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)
        # 1. Assign Symbols
        entityX = sgForm(args[0])
        entityY = "{}_{}".format(sgForm(args[1]), sgForm(args[4]))
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, 1)
        resultDICT = value2variable(resultDICT, entityY, y, args[3])

            ## 1. Assign Symbols
            #args[4] = sgForm(args[4])
            #if args[4] in resultDICT["symbolDICT"].keys():
                #pass
            #else:
                #resultDICT["symbolDICT"][args[4]] = []

            ## 2. Assign variables to Symbols
            #x = sympy.Symbol("{}_{}".format(sympyKey(args[4]), len(resultDICT["symbolDICT"][args[4]])))

            ## 3. Assign value to Symbols
            #args[3] = numExtractor(args[3])
            #resultDICT["symbolDICT"][args[4]].append((x, args[3]))
            #resultDICT["symbolLIST"].append((x, args[3]))



    if utterance == "[On] [top] [of] [each] [row]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)
        resultDICT["intentLIST"].append("multiply")

    return resultDICT