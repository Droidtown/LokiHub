#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for multiplicand

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

DEBUG_multiplicand = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_soup":["broth","chowder","consomme","consommé","cream","cream of chicken","cream of mushroom","cream of tomato","gazpacho","mulligatawny","puree","veloute","velouté","vichyssoise"],"_tmpFix":["Andrew's","Dean's"],"_MassNounUnit":["block","bottle","box","bucket","case","chunk","cup","glass","handful","mouthful","pair","piece","pile","string"]}

# Debug message
def debugInfo(inputSTR, utterance):
    if DEBUG_multiplicand:
        print("[multiplicand] {} ===> {}".format(inputSTR, utterance))

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

    if utterance == "[with] [10] [bricks] [in] [each] [row]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = args[2]
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1])

        #if args[4].lower() in ("every", "each", "one", "1") and args[5] in ("row", "column", "line"):
            #resultDICT["intentLIST"].append("multiply")
        #else:
            #resultDICT["intentLIST"].append("addition")

    if utterance == "A [garden] have [52] [rows] and [15 columns of] [bean] [plants]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "{}_{}".format(sgForm(args[2]), sgForm(args[5]))
        entityY = "{}_{}".format(sgForm(args[3]), sgForm(args[5]))
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1])
        resultDICT = value2variable(resultDICT, entityY, y, args[3])

    if utterance == "A [sandbox] be [312 centimeters] [long] and [146 centimeters] [wide]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[2] != "" and args[4] != "":
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


    if utterance == "[Cayley] earn [$5] an [hour]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "money_{}".format(sgForm(args[2]))
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1])

    if utterance == "[Each] pack [of] [pumpkin] [seeds] cost [$8] and [each] [pack] [of] [tomatoes] [seeds] cost [$5]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "money_{}_{}".format(sgForm(args[2]), sgForm(args[3]))
        entityY = "money_{}_{}".format(sgForm(args[8]), sgForm(args[9]))
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[4])
        resultDICT = value2variable(resultDICT, entityY, y, args[10])

    if utterance == "[He] [planted] [5] [flower] [beds] [with] [roses] and [tulips]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "{}_{}_{}".format(sgForm(args[4]), sgForm(args[3]), sgForm(args[6]))
        entityY = "{}_{}_{}".format(sgForm(args[4]), sgForm(args[3]), sgForm(args[7]))
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[2])
        resultDICT = value2variable(resultDICT, entityY, y, args[2])

    if utterance == "[If] [Dean] be stay [for] [4] [weeks] [there]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "{}_{}".format(args[1], sgForm(args[4]))
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[3])

    if utterance == "[If] [Tom] and [Michael] have [9] [car] [robots] and [Bob] have [9] times [more] [than] that":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "{}_{}".format(sgForm(args[1]), sgForm(args[5]))
        entityY = "{}_{}".format(sgForm(args[2]), sgForm(args[5]))
        entityZ = "{}_{}".format(sgForm(args[6]), sgForm(args[5]))
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        resultDICT = entity2symbol(resultDICT, entityZ)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        z = symbol2variable(resultDICT, entityZ)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[3])
        resultDICT = value2variable(resultDICT, entityY, y, args[3])
        resultDICT = value2variable(resultDICT, entityZ, z, numExtractor(args[3])*numExtractor(args[7]))

    if utterance == "[If] [each] [game] take [5] [minutes] [to] prepare and [he] prepare [a total of] [5] [games]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[1] in ("every", "each", "one", "1"):
            # 1. Assign Symbols
            entityX = "{}_prepare".format(args[2])
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[3])

    if utterance == "[If] [each] [of] [them] bring [4 slices of] [pizza] and [3 bags of] [chips]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[1] in ("every", "each", "one", "1"):
            # 1. Assign Symbols
            entityX = args[5]
            entityY = args[7]
            resultDICT = entity2symbol(resultDICT, entityX)
            resultDICT = entity2symbol(resultDICT, entityY)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            y = symbol2variable(resultDICT, entityY)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[4])
            resultDICT = value2variable(resultDICT, entityY, y, args[6])

    if utterance == "[If] [he] have [4] [friends] coming [over] and [he] make [3] [sandwiches] [for] [each] one [of] [them]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = args[3]
        entityY = args[7]
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[2])
        resultDICT = value2variable(resultDICT, entityY, y, args[6])

    if utterance == "[If] [he] use [2] [oranges] [per] [glass] [of] [juice] and [he] make [6 glasses of] [juice]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = args[3]
        entityX = args[9]
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[2])
        resultDICT = value2variable(resultDICT, entityX, x, args[9])

    if utterance == "[If] an [hour] have [60] [minutes]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = args[3]
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[2])

    if utterance == "[If] the [depth] [of] the [water] be [10] [times] [Dean's] [height]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "{}_{}".format(sgForm(args[3]), sgForm(args[1]))
        entityX = "{}_{}".format(sgForm(args[6]), sgForm(args[7]))
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        #2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        #3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[3]*y)
        resultDICT = value2variable(resultDICT, entityY, y, y)

    if utterance == "[If] the [rare] [robot] have an [original] price [of] [$3]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "money_{}".format(sgForm(args[2]))
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[5])

    if utterance == "[If] there be [5] [roses] and [9] [tulips] [in] [each] [flower] be":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[6] in ("every", "each", "one", "1"):
            # 1. Assign Symbols
            entityX = sgForm(args[2])
            entityY = sgForm(args[4])
            resultDICT = entity2symbol(resultDICT, entityX)
            resultDICT = entity2symbol(resultDICT, entityY)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            y = symbol2variable(resultDICT, entityY)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[1])
            resultDICT = value2variable(resultDICT, entityY, y, args[3])

    if utterance == "[If] there be [seven] [of] [them] including [Dean] and [each] pay [$70] [for] the [rent]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "money_{}".format(sgForm(args[8]))
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, numExtractor(args[6])*numExtractor(args[1]))

    if utterance == "[Lewis] earn [$1,367] [every] [week] [during] the [5 weeks of] [harvest]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "money_{}".format(sgForm(args[6]))
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, numExtractor(args[1])*numExtractor(args[5]))


    if utterance == "[Melissa] buy [2] pack [of] [tennis] [balls]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "pack_{}".format(sgForm(args[4]))
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1])

    if utterance == "[Michael] have [4] times [more] [flying] [robots] [than] [Tom]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "{}_{}".format(sgForm(args[0]), sgForm(args[4]))
        entityY = "{}_{}".format(sgForm(args[6]), sgForm(args[4]))
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1]*x)
        resultDICT = value2variable(resultDICT, entityY, y, x)

    if utterance == "[She] cut [6] [even] [columns] and [3] [even] [rows]":
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

    if utterance == "[She] deliver [newspapers] [3 days] [each] [week] [for 4 hours] [at] a time":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        if args[3] in ("every", "each", "one", "1"):
            # 1. Assign Symbols
            entityX = sgForm(args[5])
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, numExtractor(args[2])*numExtractor(args[5]))

    if utterance == "[Tom] have [twice] [as] [many] [animal] [robots] [than] [Michael]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "_".join((args[0], sgForm(args[5])))
        entityY = "_".join((args[7], sgForm(args[5])))
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        numX = x
        if args[1] == "twice":
            numY = 2*numX
        elif args[1] == "thrice":
            numY = 3*numX
        resultDICT = value2variable(resultDICT, entityX, x, numX)
        resultDICT = value2variable(resultDICT, entityY, y, numY)

    if utterance == "[he] bring [30 dollars] [for] [every] [week] [of] their staying":
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
        number = numExtractor(args[1])
        resultDICT = value2variable(resultDICT, entityX, x, number)

    if utterance == "[she] be [exactly] [3] times [as] [old] [as] [you] be":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "_".join((args[0], args[4]))
        entityY = "_".join((args[6], args[4]))
        resultDICT = entity2symbol(resultDICT, entityX)
        resultDICT = entity2symbol(resultDICT, entityY)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        y = symbol2variable(resultDICT, entityY)
        # 3. Assign value to Symbols
        numX = x
        numY = numExtractor(args[2])*numX
        resultDICT = value2variable(resultDICT, entityX, x, numX)
        resultDICT = value2variable(resultDICT, entityY, y, numY)

    if utterance == "[she] sleep [for 8 hours]":
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

    if utterance == "but [he] say that [Tom] will need [to] pay [3] times the [original] [price]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = args[5]
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, numExtractor(args[3])*x)

    if utterance == "the [company] make [60,000] [of] [each] [kind] [of] [sweatshirt]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = args[6]
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1])

    if utterance == "A [company] have [4] [different] [kinds] [of] [sweatshirts]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "{}_{}".format(sgForm(args[5]), sgForm(args[3]))
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1])

    if utterance == "A [clothing] [company] have [4] [different] [kinds] [of] [sweatshirts]":
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

    if utterance == "The [local] [zoo] [houses] [5 prides of] [lions]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "{}_{}".format(sgForm(args[4]), sgForm(args[3]))
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[3])

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

    if utterance == "[Andrew's] [4] [friends] decide [to] bring [food]":
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

    if utterance == "[Each] [batch] have [5 loaves of] [bread]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "{}_{}".format(sgForm(args[3]), sgForm(args[2]))
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[2])

    if utterance == "[Each] [pride] have [15] [lions]":
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

    if utterance == "[Michael] have [8] [animal] [robots]":
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

    if utterance == "[Tom] have [3] fly [robots]":
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

    if utterance == "[bakery] make [10 batches of] [bread] [every] [day]":
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

    if utterance == "[each] [with] [20] [students]":
        if args[0] in ("each", "every", "everyone"):
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

    if utterance == "[he] bring [30 dollars] [for] [every] [week]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

        # 1. Assign Symbols
        entityX = "money_{}".format(sgForm(args[1]))
        resultDICT = entity2symbol(resultDICT, entityX)
        # 2. Assign variables to Symbols
        x = symbol2variable(resultDICT, entityX)
        # 3. Assign value to Symbols
        resultDICT = value2variable(resultDICT, entityX, x, args[1])

    if utterance == "[school] have [5] [classes]":
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


    if utterance == "One number be [2] times [as] [large] [as] the [other]":
        # write your code here
        pass

    if utterance == "One number be [six] times the [other]":
        # write your code here
        pass

    if utterance == "[If] [each] [game] take [5] [minutes] [to] prepare and [he] prepare a [total of] [5] [games]":
        # write your code here
        pass

    if utterance == "[Twice] the second number be [12] [less] [than] [5] times the first":
        # write your code here
        pass

    if utterance == "a number be [twice] [another] number":
        # write your code here
        pass

    if utterance == "and product [20]":
        # write your code here
        pass

    if utterance == "find the numbers":
        # write your code here
        pass

    if utterance == "find two numbers":
        # write your code here
        pass

    if utterance == "the [larger] number be 4 times the [smaller] number":
        # write your code here
        pass

    if utterance == "their difference be [22]":
        # write your code here
        pass

    if utterance == "whose sum AND product be [11]":
        # write your code here
        pass

    return resultDICT