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
import inflect
sp = inflect.engine()
import json
import os
from pprint import pprint
DEBUG_quest_goal = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {}

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
        questGoal = "_".join([questGoal, args[argsIndex+2]]) #Let's skip "of" since for mass nouns "of" is always there.
    if questGoal:
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

    if utterance == "How [many] [headphones] be [in] the [store] ?":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [levels] do [Shara] complete ?":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [music] [books] be there [in] [total] ?":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [pieces] [of] [gum] do [Adrianna] have [now]":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [pots] [of] [soup] be there ?":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 3)

    if utterance == "How [many] [shots] be there [in] [total] ?":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [stacks] [of] dessert be there ?":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [staff] be work there ?":
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
        # write your code here
        pass

    if utterance == "How [many] [bags] [of] [chocolate] do [Peter] have [now]":
        resultDICT = intentChecker(resultDICT)
        resultDICT = questGoalChecker(resultDICT, args, 1)

    if utterance == "How [many] [guitars] be there [in] [total] ?":
        if any([x in ("row", "column", "line") for x in resultDICT["symbolDICT"].keys()]):
            resultDICT["intentLIST"].append("multiply")
        else:
            resultDICT["intentLIST"].append("addition")
        resultDICT = questGoalChecker(resultDICT, args, 1)
    return resultDICT