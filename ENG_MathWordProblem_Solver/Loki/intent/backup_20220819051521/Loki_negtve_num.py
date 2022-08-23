#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for negtve_num

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

DEBUG_negtve_num = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {}

# Debug message
def debugInfo(inputSTR, utterance):
    if DEBUG_negtve_num:
        print("[negtve_num] {} ===> {}".format(inputSTR, utterance))

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
    number = -abs(numExtractor(numberSTR))
    resultDICT["symbolDICT"][entitySTR].append((variableX, number))
    resultDICT["symbolLIST"].append((variableX, number))
    return resultDICT

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "A [customer] come in [to] return [2] [pairs of] [headphones]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            # 1. Assign Symbols
            entityX = args[4]
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[2])

    if utterance == "The [hobby] [store] [normally] sell [10,576] [trading] [cards] [per] [month]":
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
            resultDICT = value2variable(resultDICT, entityX, x, args[3])

    if utterance == "[2] [of] her [shots] do not go in the [hoop]":
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
            resultDICT = value2variable(resultDICT, entityX, x, args[0])

    if utterance == "[Shara] share [3] [candies] [with] her [friend]":
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

    if utterance == "[you] sell [320] [chocolate] [cookies] and [270] [vanilla] [cookies]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            # 1. Assign Symbols
            entityX = args[3]
            entityY = args[6]
            resultDICT = entity2symbol(resultDICT, entityX)
            resultDICT = entity2symbol(resultDICT, entityY)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            y = symbol2variable(resultDICT, entityY)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[1])
            resultDICT = value2variable(resultDICT, entityY, y, args[4])

    if utterance == "the [hobby] [store] sell [15,498] [more] [trading] [cards] [than] [normal]":
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
            resultDICT = value2variable(resultDICT, entityX, x, args[2])

    if utterance == "there be [1] [word] misspell":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            # 1. Assign Symbols
            entityX = args[1]
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[0])

    #duplicate
    if utterance == "A [customer] come in [to] return [2 pairs of] [headphones]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            # 1. Assign Symbols
            entityX = "{}_{}".format(sgForm(args[2].rstrip(" of").split(" ")[-1]), sgForm(args[3]))
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[2])

    if utterance == "[Alicia] give [51] [Egyptian] [masks] [from] her [collection] [of] [90]":
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
            resultDICT = value2variable(resultDICT, entityX, x, args[1])

    if utterance == "[Asha] donate [46] [medieval] [art] [pieces] [from] the [70] [she] [originally] have":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            # 1. Assign Symbols
            entityX = args[4]
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[1])

    if utterance == "[She] [also] give the [12] [Egyptian] [weavings]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            # 1. Assign Symbols
            entityX = args[4]
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[2])

    if utterance == "[she] give away [14 pairs of] [shoes] [to] her [friends]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            # 1. Assign Symbols
            entityX = "{}_{}".format(sgForm(args[1].rstrip(" of").split(" ")[-1]), sgForm(args[2]))
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[1])

    if utterance == "[she] give away [49] [miniature] [aircrafts] [to] the [National] [Air] and [Space] [Museum]":
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
            resultDICT = value2variable(resultDICT, entityX, x, args[1])

    if utterance == "[she] send [66] [of] her [gifts]":
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
            resultDICT = value2variable(resultDICT, entityX, x, args[1])

    #duplicate
    if utterance == "the [Bue] [Team] lose [by] [13] [points]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            # 1. Assign Symbols
            args[4] = sgForm(args[4])
            if args[4] in resultDICT["symbolDICT"].keys():
                pass
            else:
                resultDICT["symbolDICT"][args[4]] = []

            # 2. Assign variables to Symbols
            x = sympy.Symbol("{}_{}".format(args[4], len(resultDICT["symbolDICT"][args[4]])))

            # 3. Assign value to Symbols
            args[3] = w2n(args[3])
            resultDICT["symbolDICT"][args[4]].append((x, args[3]))
            resultDICT["symbolLIST"].append((x, args[3]))

    if utterance == "A [customer] buy [1] [pizza]":
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
            resultDICT = value2variable(resultDICT, entityX, x, (args[1]))

    if utterance == "[25 out of] [55] [salmon] [families] go":
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
            resultDICT = value2variable(resultDICT, entityX, x, args[0])

    if utterance == "[32] [bird] [families] fly [away]":
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
            resultDICT = value2variable(resultDICT, entityX, x, args[0])

    if utterance == "[Adrianna] share [another] [10 pieces of] [bubble] [gum]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            # 1. Assign Symbols
            entityX = "{}_{}".format(sgForm(args[2].rstrip(" of").split(" ")[-1]), sgForm(args[4]))
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[2])

    if utterance == "[He] sell [213] [ants]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            # 1. Assign Symbols
            args[2] = sgForm(args[2])
            if args[2] in resultDICT["symbolDICT"].keys():
                pass
            else:
                resultDICT["symbolDICT"][args[2]] = []

            # 2. Assign variables to Symbols
            x = sympy.Symbol("{}_{}".format(args[2], len(resultDICT["symbolDICT"][args[2]])))

            # 3. Assign value to Symbols
            args[1] = w2n(args[1])
            resultDICT["symbolDICT"][args[2]].append((x, args[1]))
            resultDICT["symbolLIST"].append((x, args[1]))


    if utterance == "[If] [21] [chipmunks] be leave [from] the [original] [86]":
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

    if utterance == "[Jasmine] return [$27] worth [of] [change]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            # 1. Assign Symbols
            entityX = "money_{}".format(sgForm(args[3]))
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[1])

    if utterance == "[She] [also] give [86] [candies] [to] [Kayla]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            # write your code here
            args[3] = sgForm(args[3])
            if args[3] in resultDICT["symbolDICT"].keys():
                pass
            else:
                resultDICT["symbolDICT"][args[3]] = []

            # 2. Assign variables to Symbols
            x = sympy.Symbol("{}_{}".format(args[3], len(resultDICT["symbolDICT"][args[3]])))

            # 3. Assign value to Symbols
            args[2] = w2n(args[2])
            resultDICT["symbolDICT"][args[3]].append((x, args[2]))
            resultDICT["symbolLIST"].append((x, args[2]))

    if utterance == "[She] give [105] [candies] [to] [Marissa]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            # write your code here
            args[2] = sgForm(args[2])
            if args[2] in resultDICT["symbolDICT"].keys():
                pass
            else:
                resultDICT["symbolDICT"][args[2]] = []

            # 2. Assign variables to Symbols
            x = sympy.Symbol("{}_{}".format(args[2], len(resultDICT["symbolDICT"][args[2]])))

            # 3. Assign value to Symbols
            args[1] = w2n(args[1])
            resultDICT["symbolDICT"][args[2]].append((x, args[1]))
            resultDICT["symbolLIST"].append((x, args[1]))

    # how to extract subject from context clues?
    if utterance == "[She] give [6] [to] [Theresa]":
        # write your code here
        pass

    if utterance == "[She] share [10 pieces of] [strawberry] [gum]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            # 1. Assign Symbols
            entityX = "{}_{}".format(sgForm(args[1].rstrip(" of").split(" ")[-1]), sgForm(args[3]))
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[1])

    if utterance == "[she] get [for] a [discount of] [$17]":
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
            resultDICT = value2variable(resultDICT, entityX, x, args[3])

    if utterance == "the [Blue] [Team] lose [by] [13] [points]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            # 1. Assign Symbols
            entityX = args[4]
            resultDICT = entity2symbol(resultDICT, entityX)
            # 2. Assign variables to Symbols
            x = symbol2variable(resultDICT, entityX)
            # 3. Assign value to Symbols
            resultDICT = value2variable(resultDICT, entityX, x, args[3])

    if utterance == "the [hobby] [store] sell a [total of] [20,777] [trading] [cards]":
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
            resultDICT = value2variable(resultDICT, entityX, x, args[3])

    if utterance == "A number be [12] [less] [than] [another]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            if args[3] == "another":
                variableLIST = []
                entityX = "number_0"
                entityY = "number_1"
                resultDICT = entity2symbol(resultDICT, entityX)
                resultDICT = entity2symbol(resultDICT, entityY)
                x = sympy.Symbol(entityX)
                y = sympy.Symbol(entityY)
                variableLIST.append(x)
                variableLIST.append(y)

                equation = "{} - {} + {}".format(variableLIST[0].name, variableLIST[1].name, w2n(args[0]))
                resultDICT["eqLIST"].append(sympy.sympify(equation))
                resultDICT["symbolLIST"].extend(variableLIST)

    if utterance == "[One] [positive] [integer] be [3] [less] [than] a [second] [positive] [integer]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            if args[2] == args[8]:
                variableLIST = []
                entityX = "{}_0".format(args[2])
                entityY = "{}_1".format(args[8])
                resultDICT = entity2symbol(resultDICT, entityX)
                resultDICT = entity2symbol(resultDICT, entityY)
                x = sympy.Symbol(entityX)
                y = sympy.Symbol(entityY)
                variableLIST.append(x)
                variableLIST.append(y)

                equation = "{} - {} + {}".format(variableLIST[0].name, variableLIST[1].name, w2n(args[3]))
                resultDICT["eqLIST"].append(sympy.sympify(equation))
                resultDICT["symbolLIST"].extend(variableLIST)

    if utterance == "[One] number be [3] [less] [than] a [second] [number]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            if args[5] == "number":
                variableLIST = []
                entityX = "{}_0".format(args[5])
                entityY = "{}_1".format(args[5])
                resultDICT = entity2symbol(resultDICT, entityX)
                resultDICT = entity2symbol(resultDICT, entityY)
                x = sympy.Symbol(entityX)
                y = sympy.Symbol(entityY)
                variableLIST.append(x)
                variableLIST.append(y)

                equation = "{} - {} + {}".format(variableLIST[0].name, variableLIST[1].name, w2n(args[1]))
                resultDICT["eqLIST"].append(sympy.sympify(equation))
                resultDICT["symbolLIST"].extend(variableLIST)

    if utterance == "The difference [of] [two] [numbers] be [9]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            if w2n(args[3]) == 2:
                variableLIST = []
                for i in range(0, w2n(args[1])):
                    entityV = "{}_{}".format(sgForm(args[2]), i)
                    resultDICT = entity2symbol(resultDICT, entityV)
                    v = sympy.Symbol(entityV)
                    variableLIST.append(v)

                equation = "{} - {} + {}".format(variableLIST[0].name, variableLIST[1].name, w2n(args[3]))
                resultDICT["eqLIST"].append(sympy.sympify(equation))
                resultDICT["symbolLIST"].extend(variableLIST)

    if utterance == "The difference [of] the [same] [2] numbers be [4]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            variableLIST = []
            for i in range(0, w2n(args[2])):
                entityV = "number_{}".format(i)
                resultDICT = entity2symbol(resultDICT, entityV)
                v = sympy.Symbol(entityV)
                variableLIST.append(v)

            if args[1].lower() in ("same", "identical"):
                equation = "{}*{} + {}".format(variableLIST[0].name, w2n(args[2]), w2n(args[3]))
            else:
                equation = "{} - {} + {}".format(variableLIST[0].name, variableLIST[1].name, w2n(args[3]))
            resultDICT["eqLIST"].append(sympy.sympify(equation))
            resultDICT["symbolLIST"].extend(variableLIST)

    if utterance == "[One] number be [seven] [less] [than] [another] number":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            if args[4] == "another":
                variableLIST = []
                for i in range(0, w2n(args[2])):
                    entityV = "number_{}".format(i)
                    resultDICT = entity2symbol(resultDICT, entityV)
                    v = sympy.Symbol(entityV)
                    variableLIST.append(v)

                equation = "{} - {} + {}".format(variableLIST[0].name, variableLIST[1].name, w2n(args[1]))
                resultDICT["eqLIST"].append(sympy.sympify(equation))
                resultDICT["symbolLIST"].extend(variableLIST)

    if utterance == "the difference [of] the [two] numbers be [57]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            variableLIST = []
            for i in range(0, w2n(args[1])):
                entityV = "number_{}".format(i)
                resultDICT = entity2symbol(resultDICT, entityV)
                v = sympy.Symbol(entityV)
                variableLIST.append(v)

            equation = "{} - {} + {}".format(variableLIST[0].name, variableLIST[1].name, w2n(args[1]))
            resultDICT["eqLIST"].append(sympy.sympify(equation))
            resultDICT["symbolLIST"].extend(variableLIST)

    if utterance == "the difference [of] whose [squares] be [207]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            variableLIST = []
            for i in range(0, len(resultDICT["symbolLIST"])):
                entityV = "number_{}".format(i)
                resultDICT = entity2symbol(resultDICT, entityV)
                v = sympy.Symbol(entityV)
                variableLIST.append(v)

            equation = "{}**2 - {}**2 + {}".format(variableLIST[0].name, variableLIST[1].name, w2n(args[2]))
            resultDICT["eqLIST"].append(sympy.sympify(equation))
            resultDICT["symbolLIST"].extend(variableLIST)

    if utterance == "the difference be [9]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            variableLIST = []
            for i in range(0, len(resultDICT["symbolLIST"])):
                entityV = "number_{}".format(i)
                resultDICT = entity2symbol(resultDICT, entityV)
                v = sympy.Symbol(entityV)
                variableLIST.append(v)

            equation = "{} - {} + {}".format(variableLIST[0].name, variableLIST[1].name, w2n(args[0]))
            resultDICT["eqLIST"].append(sympy.sympify(equation))
            resultDICT["symbolLIST"].extend(variableLIST)

    if utterance == "the units [digit] be [5] [more] [than] the ten's [digit]":
        # write your code here
        pass

    if utterance == "their difference be [16]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            variableLIST = []
            for i in range(0, len(resultDICT["symbolLIST"])):
                entityV = "number_{}".format(i)
                resultDICT = entity2symbol(resultDICT, entityV)
                v = sympy.Symbol(entityV)
                variableLIST.append(v)

            equation = "{} - {} + {}".format(variableLIST[0].name, variableLIST[1].name, w2n(args[0]))
            resultDICT["eqLIST"].append(sympy.sympify(equation))
            resultDICT["symbolLIST"].extend(variableLIST)

    if utterance == "whose difference is [6]":
        if inputSTR in resultDICT["inputStrLIST"]:
            return resultDICT
        else:
            resultDICT["inputStrLIST"].append(inputSTR)

            variableLIST = []
            for i in range(0, len(resultDICT["symbolLIST"])):
                entityV = "number_{}".format(i)
                resultDICT = entity2symbol(resultDICT, entityV)
                v = sympy.Symbol(entityV)
                variableLIST.append(v)

            equation = "{} - {} + {}".format(variableLIST[0].name, variableLIST[1].name, w2n(args[0]))
            resultDICT["eqLIST"].append(sympy.sympify(equation))
            resultDICT["symbolLIST"].extend(variableLIST)



    return resultDICT