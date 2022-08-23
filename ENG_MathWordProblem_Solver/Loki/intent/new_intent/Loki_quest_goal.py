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

import json
import os

DEBUG_quest_goal = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_soup":["broth","chowder","consomme","consommé","cream","cream of chicken","cream of mushroom","cream of tomato","gazpacho","mulligatawny","puree","veloute","velouté","vichyssoise"],"_tmpFix":["Andrew's","Dean's"],"_MassNounUnit":["block","bottle","box","bucket","case","chunk","cup","glass","handful","mouthful","pair","piece","pile","string"]}

# Debug message
def debugInfo(inputSTR, utterance):
    if DEBUG_quest_goal:
        print("[quest_goal] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "How [many] [books] do [Billy] have [now]":
        # write your code here
        pass

    if utterance == "How [many] [books] do [they] have [in] [total]":
        # write your code here
        pass

    if utterance == "How [many] [boxes] [of] [paper] do [Allen] have [now]":
        # write your code here
        pass

    if utterance == "How [many] [boxes] do [she] need ?":
        # write your code here
        pass

    if utterance == "How [many] [candies] do [Andie] have [now]":
        # write your code here
        pass

    if utterance == "How [many] [cats] do [Sarah] have":
        # write your code here
        pass

    if utterance == "How [many] [chairs] do the [restaurant] have [in] [total]":
        # write your code here
        pass

    if utterance == "How [many] [cookies] do [you] sell":
        # write your code here
        pass

    if utterance == "How [many] [crayon] [boxes] do [she] need ?":
        # write your code here
        pass

    if utterance == "How [many] [guitars] be there [in] [total]":
        # write your code here
        pass

    if utterance == "How [many] [headphones] be [in] the [store]":
        # write your code here
        pass

    if utterance == "How [many] [levels] do [Sarah] complete":
        # write your code here
        pass

    if utterance == "How [many] [music] [books] be there [in] [total]":
        # write your code here
        pass

    if utterance == "How [many] [pieces] [of] [candy] be [in] [each] [bag] ?":
        # write your code here
        pass

    if utterance == "How [many] [pieces] [of] [gum] do [Adrianna] have [now]":
        # write your code here
        pass

    if utterance == "How [many] [pieces] can the [school] buy in [total] ?":
        # write your code here
        pass

    if utterance == "How [many] [pots] [of] [soup] be there":
        # write your code here
        pass

    if utterance == "How [many] [rides] can [you] go on ?":
        # write your code here
        pass

    if utterance == "How [many] [staff] be work there":
        # write your code here
        pass

    if utterance == "How [many] [trumpets] do [he] order [in] [total]":
        # write your code here
        pass

    if utterance == "How [many] [words] be on the [spelling] [test]":
        # write your code here
        pass

    if utterance == "How [much] do [1] [tennis] [ball] cost ?":
        # write your code here
        pass

    if utterance == "How [much] do [1] pack [of] [tennis] [balls] cost ?":
        # write your code here
        pass

    if utterance == "find [two] [numbers]":
        # write your code here
        pass

    if utterance == "find the [larger] number":
        # write your code here
        pass

    if utterance == "find the [two] numbers .":
        # write your code here
        pass

    if utterance == "find these [numbers]":
        # write your code here
        pass

    if utterance == "how [many] [bracelets] [of] [blue] [shiny] [round] [stones] will there be ?":
        # write your code here
        pass

    if utterance == "how [many] [colors] do [Sheila] use ?":
        # write your code here
        pass

    if utterance == "how [many] [cutlets] will the [restaurant] have leave over [after] make [as] [many] [dishes] [as] [possible] ?":
        # write your code here
        pass

    if utterance == "how [many] [drawings] will [each] [neighbor] receive ?":
        # write your code here
        pass

    if utterance == "how [many] [glasses] [of] [fresh] [lemonade] can [she] make":
        # write your code here
        pass

    if utterance == "how [many] [marbles] will [each] [of] the [boys] receive ?":
        # write your code here
        pass

    if utterance == "how [many] [paintings] can [she] give [to] [each] [of] her [two] [grandmothers] ?":
        # write your code here
        pass

    if utterance == "how [many] [paintings] will be place [in] [each] [of] the [four] [rooms] ?":
        # write your code here
        pass

    if utterance == "how [many] [pink] [flower] [stones] will [each] [bracelet] have ?":
        # write your code here
        pass

    if utterance == "how [many] [pizzas] be leave":
        # write your code here
        pass

    if utterance == "how [many] [seeds] will be place [in] [each] can [if] [she] places an [equal] [number] [of] [seeds] [in] [each] can ?":
        # write your code here
        pass

    if utterance == "how [many] [star-shape] [stones] will be [in] [each] [bracelet] ?":
        # write your code here
        pass

    if utterance == "how [many] [stations] do [they] visit ?":
        # write your code here
        pass

    if utterance == "how [many] [trading] [cards] do the [hobby] [store] sell":
        # write your code here
        pass

    if utterance == "what be the numbers":
        # write your code here
        pass

    return resultDICT