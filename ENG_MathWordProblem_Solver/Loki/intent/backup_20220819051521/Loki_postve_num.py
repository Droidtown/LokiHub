#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for postve_num

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
from word2number.w2n import word_to_num as w2n

DEBUG_postve_num = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {}

# Debug message
def debugInfo(inputSTR, utterance):
    if DEBUG_postve_num:
        print("[postve_num] {} ===> {}".format(inputSTR, utterance))

def inputSTRChecker(resultDICT, inputSTR):
    if inputSTR in resultDICT["inputStrLIST"]:
        pass
    else:
        resultDICT["inputStrLIST"].append(inputSTR)
    return resultDICT

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
    try:
        number = numExtractor(numberSTR)
    except:
        number = None
    resultDICT["symbolDICT"][entitySTR].append((variableX, number))
    resultDICT["symbolLIST"].append((variableX, number))
    return resultDICT

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    #5th problem
    if utterance == "The [restaurant] have [175] [normal] [chairs] and [20] [big] [chairs] [for] [babies]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[3])
        entityY = sgForm(args[6])
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1])
        resultDICT = value2variable(resultDICT, entityY, y, args[4])
        #resultDICT["intentLIST"].append("addition")

    #quest_goal: people
    if utterance == "There be [6] [chef] [assistants] and [2] [servers]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[2])
        entityY = sgForm(args[4])
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[0])
        resultDICT = value2variable(resultDICT, entityY, y, args[3])
        #resultDICT["intentLIST"].append("addition")

    #7th problem
    if utterance == "There be [4] [classic] [violins] [in] the [store] [room] and [3] [modern] [violins] [on] [display]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[2])
        entityY = sgForm(args[8])
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[0])
        resultDICT = value2variable(resultDICT, entityY, y, args[6])

    #1st problem
    if utterance == "There be [8] [classic] [guitars] and [3] [classic] [flutes] [from] the [order]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[2])
        entityY = sgForm(args[5])
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[0])
        resultDICT = value2variable(resultDICT, entityY, y, args[3])

    #1st problem
    if utterance == "[Together] [with] [the] [5] [guitars] that [the] [store] have":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[4])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[3])

    if utterance == "[1] [of] her [shots] go in the [hoop]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[2])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[0])

    if utterance == "[Ashley] buy a [big] [bag] [of] [candy]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[2])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        if inputSTR.split(" ")[2] in ("a", "an"):
            resultDICT = value2variable(resultDICT, entityX, x, "1")

    #4th problem
    if utterance == "[Billy] have [2] [books]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[2])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1])

    #4th problem
    if utterance == "[He] [then] buy [1] [book]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[3])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[2])

    #4th problem
    if utterance == "[He] go to the [library] [to] take out [2] [more] [books]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[5])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[3])

    if utterance == "[restaurant] receive a [shipment of] [86] [veal] [cutlets]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[4])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[2])

    #3rd problem : WIP
    if utterance == "[she] go to the [store] [to] get [3] [more] [pieces] [of] [gum]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "{}_{}".format(sgForm(args[7]), sgForm(args[5]))

        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[3])

    #8th problem
    if utterance == "[she] go to the [store] and get [70 pieces of] [strawberry] [gum] and [10 pieces of] [bubble] [gum]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "{}_{}".format(sgForm(args[2].rstrip(" of").split(" ")[-1]), sgForm(args[4]))
        entityY = "{}_{}".format(sgForm(args[5].rstrip(" of").split(" ")[-1]), sgForm(args[7]))
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[2])
        resultDICT = value2variable(resultDICT, entityY, y, args[5])

    if utterance == "there be [6] [tennis] [balls]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[2])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[0])

    if utterance == "A [bricklayer] stacks [bricks] [in] [2] [rows]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[0])
        entityY = sgForm(args[4])
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, 1)
        resultDICT = value2variable(resultDICT, entityY, y, args[3])

            #resultDICT["inputStrLIST"].append(inputSTR)
            #resultDICT["intentLIST"].append("addition")

    if utterance == "The [bag] have [102] [blue] [candies]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if sgForm(args[3]) in ("row", "column"):
            pass
        else:
            # 1. Assign Symbols
            entityX = sgForm(args[3])
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[1])
            #resultDICT["intentLIST"].append("addition")

    if utterance == "[100] [red] [candies] and [94] [green] [candies]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[2])
        entityY = sgForm(args[5])
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[0])
        resultDICT = value2variable(resultDICT, entityY, y, args[3])

    if utterance == "and [5 stacks of] [pasta] [salad]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[2])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[0])

    if utterance == "there be [4 stacks of] [chocolate] [puddings]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[2])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[0])

    if utterance == "there be a [stack of] [6] [bricks]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[2])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1])

    if utterance == "[In] [one] [box]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[2])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1])

    #2nd problem : working
    if utterance == "[Next] [to] the [3] [juice] [fountains]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[4])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[2])

    #there is a problem with this utterance
    #args list index out of range
    if utterance == "there be [7] [tables]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[1])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[0])

    if utterance == "[Dave] have a [ladder] that be [14 feet] [tall]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[2])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[2])

    if utterance == "The [tall] [one] be [16 feet]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[1] == "one":
            # 1. Assign Symbols
            entityX = sgForm(args[2])
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[2])
        else:
            pass

    if utterance == "[After] deliver [newspapers] [for] [8] [weeks]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[4])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[3])

    if utterance == "[Dan] be [6 feet] [tall]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[1])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1])

    if utterance == "[If] [Michael] have [8] [animal] [robots]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[4])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[2])

    if utterance == "[If] [Tom] have [3] fly [robots]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[3])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[2])

    if utterance == "the [larger] [number] be [five] [more] [than] the [smaller] [number]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if set([args[1], args[6]]).intersection(set(["number", "integer"])):
            # 1. Assign Symbols
            if sgForm(args[1]) in resultDICT["symbolDICT"].keys():
                pass
            else:
                resultDICT["symbolDICT"][sgForm(args[1])] = []

            variableLIST = []
            # 2. Assign variables to Symbols
            entityX = "{}_{}".format(sgForm(args[1]), len(resultDICT["symbolDICT"][sgForm(args[1])]))
            variableLIST.append(sympy.Symbol(entityX))
            resultDICT = entity2symbol(resultDICT, entityX)
            if args[1] == args[6]:
                entityY = "{}_{}".format(sgForm(args[6]), len(resultDICT["symbolDICT"][sgForm(args[6])])+1)
            else:
                entityY = "{}_{}".format(sgForm(args[6]), len(resultDICT["symbolDICT"][sgForm(args[6])]))
            variableLIST.append(sympy.Symbol(entityY))
            resultDICT = entity2symbol(resultDICT, entityY)

            # 3. Add equation to eqLIST
            equation = "{} - {} - {}".format(variableLIST[0].name, w2n(args[2]), variableLIST[-1].name)
            resultDICT["eqLIST"].append(sympy.sympify(equation))
            resultDICT["symbolLIST"].extend(variableLIST)

    if utterance == "[for] [3] pack [of] [tomato] [seeds] and [4] pack [of] [pumpkin] [seeds]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "{}_{}".format(args[3], args[4])
        entityY = "{}_{}".format(args[7], args[8])
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1])
        resultDICT = value2variable(resultDICT, entityY, y, args[5])

    if utterance == "[Melissa] buy [2 packs of] [tennis] [balls]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[3])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1])

    if utterance == "[7] [stray] [dogs] living [around] his [neighborhood]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[2])
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[0])

    #quest_goal: soup
    if utterance == "There be [9 pots of] [cream of mushroom] and [8 pots of] [vegetable] [soup]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = sgForm(args[1])
        entityY = sgForm(args[4])
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[0])
        resultDICT = value2variable(resultDICT, entityY, y, args[2])

    if utterance == "[7 stacks of] [brownies]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "{}_{}".format(sgForm(args[1]), sgForm(args[0]))
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[0])

    #3rd problem : WIP
    if utterance == "[Adrianna] have [10 pieces of] [gum]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "{}_{}".format(sgForm(args[2]), sgForm(args[1]))
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1])

    if utterance == "the sum [of] [two] [numbers] be [twenty-three]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        for i in range(0, w2n(args[1])):
            if "{}_{}".format(sgForm(args[1]), i) in resultDICT["symbolDICT"].keys():
                pass
            else:
                resultDICT["symbolDICT"]["{}_{}".format(sgForm(args[1]), i)] = []

        variableLIST = []
        # 2. Assign variables to Symbols
        for n in range(0, w2n(args[1])):
            variableLIST.append(sympy.Symbol("number_{}".format(n)))

        # 3. Add equation to eqLIST and symbols to symbolLIST
        equation = str(w2n(args[3])*-1)+"+"
        for v in variableLIST:
            equation = equation + v.name + " + "
        resultDICT["eqLIST"].append(sympy.sympify(equation.rstrip(" + ")))
        for v in variableLIST:
            if v in resultDICT["symbolLIST"]:
                pass
            else:
                resultDICT["symbolLIST"].append(v)

    if utterance == "The sum [of] the [numbers] be [28]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        for i in range(0, len(resultDICT["symbolLIST"])):
            if "{}_{}".format(sgForm(args[1]), i) in resultDICT["symbolDICT"].keys():
                pass
            else:
                resultDICT["symbolDICT"]["{}_{}".format(sgForm(args[1]), i)] = []

        variableLIST = []
        # 2. Assign variables to Symbols
        for n in range(0, len(resultDICT["symbolDICT"].keys())):
            variableLIST.append(sympy.Symbol("number_{}".format(n)))

        # 3. Add equation to eqLIST and symbols to symbolLIST
        equation = str(w2n(args[2])*-1)+"+"
        for v in variableLIST:
            equation = equation + v.name + " + "
        resultDICT["eqLIST"].append(sympy.sympify(equation.rstrip(" + ")))
        for v in variableLIST:
            if v in resultDICT["symbolLIST"]:
                pass
            else:
                resultDICT["symbolLIST"].append(v)

    if utterance == "[two] [numbers] whose sum be [62]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        for i in range(0, w2n(args[0])):
            if "{}_{}".format(sgForm(args[1]), i) in resultDICT["symbolDICT"].keys():
                pass
            else:
                resultDICT["symbolDICT"]["{}_{}".format(sgForm(args[1]), i)] = []

        variableLIST = []
        # 2. Assign variables to Symbols
        for n in range(0, len(resultDICT["symbolDICT"].keys())):
            variableLIST.append(sympy.Symbol("number_{}".format(n)))

        # 3. Add equation to eqLIST and symbols to symbolLIST
        equation = str(w2n(args[2])*-1)+"+"
        for v in variableLIST:
            equation = equation + v.name + " + "
        resultDICT["eqLIST"].append(sympy.sympify(equation.rstrip(" + ")))
        for v in variableLIST:
            if v in resultDICT["symbolLIST"]:
                pass
            else:
                resultDICT["symbolLIST"].append(v)

    if utterance == "[with] sum [10]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        for i in range(0, len(resultDICT["symbolLIST"])):
            if resultDICT["symbolLIST"][i] in resultDICT["symbolDICT"].keys():
                pass
            else:
                resultDICT["symbolDICT"][resultDICT["symbolLIST"][i]] = []

        variableLIST = []
        # 2. Assign variables to Symbols
        for n in range(0, len(resultDICT["symbolDICT"].keys())):
            variableLIST.append(sympy.Symbol("number_{}".format(n)))

        # 3. Add equation to eqLIST and symbols to symbolLIST
        equation = str(w2n(args[1])*-1)+"+"
        for v in variableLIST:
            equation = equation + v.name + " + "
        resultDICT["eqLIST"].append(sympy.sympify(equation.rstrip(" + ")))
        for v in variableLIST:
            if v in resultDICT["symbolLIST"]:
                pass
            else:
                resultDICT["symbolLIST"].append(v)

    if utterance == "the sum [of] the digits [of] a [two] digit number be [15]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        for i in range(0, w2n(args[2])):
            if "number_{}".format(i) in resultDICT["symbolDICT"].keys():
                pass
            else:
                resultDICT["symbolDICT"]["number_{}".format(i)] = []

        variableLIST = []
        # 2. Assign variables to Symbols
        for n in range(0, len(resultDICT["symbolDICT"].keys())):
            variableLIST.append(sympy.Symbol("number_{}".format(n)))

        # 3. Add equation to eqLIST and symbols to symbolLIST
        equation = str(w2n(args[3])*-1)+"+"
        for v in variableLIST:
            equation = equation + v.name + " + "
        resultDICT["eqLIST"].append(sympy.sympify(equation.rstrip(" + ")))
        for v in variableLIST:
            if v in resultDICT["symbolLIST"]:
                pass
            else:
                resultDICT["symbolLIST"].append(v)

    if utterance == "[if] the [digits] be [interchanged] the result exceed the [original] [number] [by] [9]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        for i in range(0, len(resultDICT["symbolLIST"])):
            if "number_{}".format(i) in resultDICT["symbolDICT"].keys():
                pass
            else:
                resultDICT["symbolDICT"]["number_{}".format(i)] = []

        variableLIST = []
        # 2. Assign variables to Symbols
        for n in range(0, len(resultDICT["symbolDICT"].keys())):
            variableLIST.append(sympy.Symbol("number_{}".format(n)))

        # 3. Add equation to eqLIST and symbols to symbolLIST
        equation = str(w2n(args[6])*-1) + "+ 10*{1} + {0} - 10*{0} + {1}".format(variableLIST[0].name, variableLIST[1].name)
        resultDICT["eqLIST"].append(sympy.sympify(equation.rstrip(" + ")))
        for v in variableLIST:
            if v in resultDICT["symbolLIST"]:
                pass
            else:
                resultDICT["symbolLIST"].append(v)

    if utterance == "the sum be [36]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        for i in range(0, len(resultDICT["symbolLIST"])):
            if resultDICT["symbolLIST"][i] in resultDICT["symbolDICT"].keys():
                pass
            else:
                resultDICT["symbolDICT"][resultDICT["symbolLIST"][i]] = []

        variableLIST = []
        # 2. Assign variables to Symbols
        for n in range(0, len(resultDICT["symbolDICT"].keys())):
            variableLIST.append(sympy.Symbol("number_{}".format(n)))

        # 3. Add equation to eqLIST and symbols to symbolLIST
        equation = str(w2n(args[0])*-1)+"+"
        for v in variableLIST:
            equation = equation + v.name + " + "
        resultDICT["eqLIST"].append(sympy.sympify(equation.rstrip(" + ")))
        for v in variableLIST:
            if v in resultDICT["symbolLIST"]:
                pass
            else:
                resultDICT["symbolLIST"].append(v)

    if utterance == "their sum be [88]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        for i in range(0, len(resultDICT["symbolLIST"])):
            if resultDICT["symbolLIST"][i] in resultDICT["symbolDICT"].keys():
                pass
            else:
                resultDICT["symbolDICT"][resultDICT["symbolLIST"][i]] = []

        variableLIST = []
        # 2. Assign variables to Symbols
        for n in range(0, len(resultDICT["symbolDICT"].keys())):
            variableLIST.append(sympy.Symbol("number_{}".format(n)))

        # 3. Add equation to eqLIST and symbols to symbolLIST
        equation = str(w2n(args[0])*-1)+"+"
        for v in variableLIST:
            equation = equation + v.name + " + "
        resultDICT["eqLIST"].append(sympy.sympify(equation.rstrip(" + ")))
        for v in variableLIST:
            if v in resultDICT["symbolLIST"]:
                pass
            else:
                resultDICT["symbolLIST"].append(v)

    if utterance == "the [CN] [Tower] stand [at] [553 meters] [high]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "{}_{}".format(sgForm(args[0]), sgForm(args[1]))
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[3].split(" ")[0])

    if utterance == "[it] be [taller] [than] the [Space] [Needle] [by] [369 meters]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            # 1. Assign Symbols
            entityX = "{}_{}".format(sgForm(args[3]), sgForm(args[4]))
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, resultDICT["symbolLIST"][0][1]-w2n(args[6].split(" ")[0]))

    return resultDICT