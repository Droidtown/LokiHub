#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for quest_goal

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
import inflect
sp = inflect.engine()
import json
import os
from pprint import pprint
DEBUG_quest_goal = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_soup":["broth","chowder","consomme","consommé","cream","cream of chicken","cream of mushroom","cream of tomato","gazpacho","mulligatawny","puree","veloute","velouté","vichyssoise"],"_tmpFix":["Andrew's","Dean's"],"_MassNounUnit":["block","bottle","box","bucket","case","chunk","cup","glass","handful","mouthful","pair","piece","pile","string"]}

# Debug message
def debugInfo(inputSTR, utterance):
    if DEBUG_quest_goal:
        print("[quest_goal] {} ===> {}".format(inputSTR, utterance))


def intentChecker(resultDICT):
    if resultDICT["intentLIST"] == []:
        resultDICT["intentLIST"].append("addition")

    #This block takes userDefinedDICT as a KnowledgeGraph source.
    #_key as "KIND_NAME" and elements in the value list as "ENTITY_OF_THE_KIND" are set up in the userDefinedDICT.
    #This block scanns the entity under resultDICT["symbolDICT"] and see if it is in the userDefinedDICT[_KIND_NAME].
    #If it is, copy what's under resultDICT["symbolDICT][entity] into the resultDICT["symbolDICT"][KIND_NAME]
    for enty in resultDICT["symbolDICT"].keys():
        for k in userDefinedDICT.keys():
            if enty in userDefinedDICT[k]:
                resultDICT["symbolDICT"][k.lstrip("_")].extend(resultDICT["symbolDICT"][enty])
    return resultDICT

def questGoalChecker(resultDICT, args, argsIndex):
    questGoal = sp.singular_noun(args[argsIndex])
    if questGoal in userDefinedDICT["_MassNounUnit"] and args[argsIndex+1] == "of":
        questGoal = "_".join([args[argsIndex+2], questGoal]) #Let's skip "of" since for mass nouns "of" is always there.
    if questGoal in ("row", "column", "line"):
        for i in resultDICT["symbolDICT"].keys():
            if i.endswith("_{}".format(questGoal)):
                resultDICT["questGoalLIST"].append(i)
                break
    elif questGoal:
        resultDICT["questGoalLIST"].append(questGoal)
    else:
        resultDICT["questGoalLIST"].append(args[argsIndex])
    return resultDICT

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "How [many] [books] do [Billy] have [now]":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [candies] do [Andie] have [now] ?":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [chairs] do the [restaurant] have [in] [total]":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [cookies] do [you] sell":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [headphones] be [in] the [store]":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [levels] do [Sarah] complete":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [music] [books] be there [in] [total] ?":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [pieces] [of] [gum] do [Adrianna] have [now]":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [pots] [of] [soup] be there":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 3)

    if utterance == "How [many] [staff] be work there":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [trumpets] do [he] order [in] [total] ?":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [words] be on the [spelling] [test] ?":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "how [many] [trading] [cards] do the [hobby] [store] sell":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [books] do [they] have [in] [total]":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [cats] do [Sarah] have":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "find [two] [numbers]":
        if sgForm(args[1]) in ("number", "integer"):
            resultDICT["intentLIST"].append("simulEq")
        else:
            resultDICT["intentLIST"].append("addition")

    if utterance == "find these [numbers]":
        if sgForm(args[0]) in ("number", "integer"):
            if resultDICT["eqLIST"] == []:
                resultDICT["intentLIST"].append("addition")
            else:
                resultDICT["intentLIST"].append("simulEq")
        else:
            resultDICT["intentLIST"].append("addition")
        resultDICT["questGoalLIST"].append(args[0])

    if utterance == "How [many] [boxes] [of] [paper] do [Allen] have [now]":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [guitars] be there [in] [total]":
        if "{}_row".format(sgForm(args[1])) in resultDICT["symbolDICT"].keys():
            resultDICT["intentLIST"].append("multiply")
        elif "{}_column".format(sgForm(args[1])) in resultDICT["symbolDICT"].keys():
            resultDICT["intentLIST"].append("multiply")
        elif "{}_line".format(sgForm(args[1])) in resultDICT["symbolDICT"].keys():
            resultDICT["intentLIST"].append("multiply")
        elif sgForm(args[1]) in ("row", "column", "line"):
            resultDICT["intentLIST"].append("addition")
        else:
            resultDICT["intentLIST"].append("addition")

        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "how [many] [pizzas] be leave":
        resultDICT["intentLIST"].append("subtraction")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [candies] do [Andie] have [now]":
        resultDICT["intentLIST"].append("addition")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [music] [books] be there [in] [total]":
        resultDICT["intentLIST"].append("addition")
        resultDICT = questGoalChecker(resultDICT, args, 2)

    if utterance == "How [many] [trumpets] do [he] order [in] [total]":
        resultDICT["intentLIST"].append("addition")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [words] be on the [spelling] [test]":
        resultDICT["intentLIST"].append("addition")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "find the [larger] [number]":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "find the [two] numbers .":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT["questGoalLIST"].append("numbers")

    if utterance == "what be the numbers":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT["questGoalLIST"].append("numbers")

    if utterance == "How [tall] be the [Space] [Needle]":
        resultDICT["intentLIST"].append("addition")
        resultDICT["questGoalLIST"].append("{}_{}".format(sgForm(args[1]), sgForm(args[2])))

    if utterance == "How [many] [boxes] do [she] need ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [crayon] [boxes] do [she] need ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 2)

    if utterance == "How [many] [pieces] [of] [candy] be [in] [each] [bag] ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 3)

    if utterance == "How [many] [pieces] can the [school] buy in [total] ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [rides] can [you] go on ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [much] do [1] [tennis] [ball] cost ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 3)

    if utterance == "How [much] do [1] pack [of] [tennis] [balls] cost ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 4)

    if utterance == "find the [larger] [number]":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "how [many] [bracelets] [of] [blue] [shiny] [round] [stones] will there be ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "how [many] [colors] do [Sheila] use ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "how [many] [cutlets] will the [restaurant] have leave over [after] make [as] [many] [dishes] [as] [possible] ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "how [many] [drawings] will [each] [neighbor] receive ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "how [many] [glasses] [of] [fresh] [lemonade] can [she] make":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "how [many] [marbles] will [each] [of] the [boys] receive ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "how [many] [paintings] can [she] give [to] [each] [of] her [two] [grandmothers] ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "how [many] [paintings] will be place [in] [each] [of] the [four] [rooms] ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "how [many] [pink] [flower] [stones] will [each] [bracelet] have ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 3)

    if utterance == "how [many] [seeds] will be place [in] [each] can [if] [she] places an [equal] [number] [of] [seeds] [in] [each] can ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "how [many] [star-shape] [stones] will be [in] [each] [bracelet] ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 2)

    if utterance == "how [many] [stations] do [they] visit ?":
        resultDICT["intentLIST"].append("simulEq")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [ants] do [he] have":
        resultDICT["intentLIST"].append("subtraction")
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [pencil] [crayons] do [Charlene] have leave":
        resultDICT["intentLIST"].append("subtraction")
        resultDICT = questGoalChecker(resultDICT, args, 2)

    if utterance == "How [many] [stickers] be miss":
        resultDICT["intentLIST"].append("subtraction")
        resultDICT = questGoalChecker(resultDICT, args, 1)
        if resultDICT["symbolDICT"][sgForm(args[1])][-1][-1] > 0:
            resultDICT["symbolDICT"][sgForm(args[1])][-1] = (resultDICT["symbolDICT"][sgForm(args[1])][-1][0], resultDICT["symbolDICT"][sgForm(args[1])][-1][-1]*-1)
            resultDICT["symbolLIST"][-1] = (resultDICT["symbolLIST"][-1][0], resultDICT["symbolLIST"][-1][-1]*-1)

    if utterance == "How [many] be score [in] the second [half]":
        resultDICT["intentLIST"].append("subtraction")
        if "score" in resultDICT["symbolDICT"].keys():
            questGoal = "score"
        else:
            questGoal = list(resultDICT["symbolDICT"].keys())[0]
        if resultDICT["symbolDICT"][questGoal][-1][-1] > 0:
            resultDICT["symbolDICT"][questGoal][-1] = (resultDICT["symbolDICT"][questGoal][-1][0], resultDICT["symbolDICT"][questGoal][-1][-1]*-1)
            resultDICT["symbolLIST"][-1] = (resultDICT["symbolLIST"][-1][0], resultDICT["symbolLIST"][-1][-1]*-1)



    return resultDICT