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

import json
import os

DEBUG_postve_num = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_soup":["broth","chowder","consomme","consommé","cream","cream of chicken","cream of mushroom","cream of tomato","gazpacho","mulligatawny","puree","veloute","velouté","vichyssoise"],"_tmpFix":["Andrew's","Dean's"],"_MassNounUnit":["block","bottle","box","bucket","case","chunk","cup","glass","handful","mouthful","pair","piece","pile","string"]}

# Debug message
def debugInfo(inputSTR, utterance):
    if DEBUG_postve_num:
        print("[postve_num] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "A [bricklayer] stacks [bricks] [in] [2] [rows]":
        # write your code here
        pass

    if utterance == "The [bag] have [102] [blue] [candies]":
        # write your code here
        pass

    if utterance == "The [restaurant] have [175] [normal] [chairs] and [20] [big] [chairs] [for] [babies]":
        # write your code here
        pass

    if utterance == "The [school] have [$20,000]":
        # write your code here
        pass

    if utterance == "The [tall] [one] be [16 feet]":
        # write your code here
        pass

    if utterance == "The sum [of] the [numbers] be [28]":
        # write your code here
        pass

    if utterance == "There be [4] [classic] [violins] [in] the [store] [room] and [3] [modern] [violins] [on] [display]":
        # write your code here
        pass

    if utterance == "There be [6] [chef] [assistants] and [2] [servers]":
        # write your code here
        pass

    if utterance == "There be [8] [classic] [guitars] and [3] [classic] [flutes] [from] the [order]":
        # write your code here
        pass

    if utterance == "There be [9 pots of] [cream of mushroom] and [8 pots of] [vegetable] [soup]":
        # write your code here
        pass

    if utterance == "[100] [red] [candies] and [94] [green] [candies]":
        # write your code here
        pass

    if utterance == "[1] [of] her [shots] go in the [hoop]":
        # write your code here
        pass

    if utterance == "[7 stacks of] [brownies]":
        # write your code here
        pass

    if utterance == "[Adrianna] have [10 pieces of] [gum]":
        # write your code here
        pass

    if utterance == "[After] deliver [newspapers] [for] [8] [weeks]":
        # write your code here
        pass

    if utterance == "[Ashley] buy a [big] [bag] [of] [candy]":
        # write your code here
        pass

    if utterance == "[Betty] buy [140] [shiny] [blue] [round] [stones]":
        # write your code here
        pass

    if utterance == "[Billy] have [2] [books]":
        # write your code here
        pass

    if utterance == "[Brenda] want [to] have [3] [bracelets] [with] [star-shaped] [stones]":
        # write your code here
        pass

    if utterance == "[Christian] [to] help [him] place [420] [seedlings] [in] [packets]":
        # write your code here
        pass

    if utterance == "[Christian] bring a [bag of] [140] [nails]":
        # write your code here
        pass

    if utterance == "[Dan] be [6 feet] [tall]":
        # write your code here
        pass

    if utterance == "[Dave] have a [ladder] that be [14 feet] [tall]":
        # write your code here
        pass

    if utterance == "[He] [then] buy [1] [book]":
        # write your code here
        pass

    if utterance == "[He] go to the [library] [to] take out [2] [more] [books]":
        # write your code here
        pass

    if utterance == "[If] [Michael] have [8] [animal] [robots]":
        # write your code here
        pass

    if utterance == "[If] [Tom] have [3] fly [robots]":
        # write your code here
        pass

    if utterance == "[In] [one] [box]":
        # write your code here
        pass

    if utterance == "[Lexie] have [32] [watercolor] [paintings]":
        # write your code here
        pass

    if utterance == "[Melissa] buy [2 packs of] [tennis] [balls]":
        # write your code here
        pass

    if utterance == "[Melissa] buy [2 packs of] [tennis] [balls] [for] [$12] [in] [total]":
        # write your code here
        pass

    if utterance == "[Next] [to] the [3] [juice] [fountains]":
        # write your code here
        pass

    if utterance == "[She] buy [36] star-shape [stones]":
        # write your code here
        pass

    if utterance == "[Shiela] have [6] [neighbors]":
        # write your code here
        pass

    if utterance == "[Together] [with] [the] [5] [guitars] that [the] [store] have":
        # write your code here
        pass

    if utterance == "[for] [3] pack [of] [tomato] [seeds] and [4] pack [of] [pumpkin] [seeds]":
        # write your code here
        pass

    if utterance == "[if] the [digits] be [interchanged] the result exceed the [original] [number] [by] [9]":
        # write your code here
        pass

    if utterance == "[it] be [taller] [than] the [Space] [Needle] [by] [369 meters]":
        # write your code here
        pass

    if utterance == "[restaurant] receive a [shipment of] [86] [veal] [cutlets]":
        # write your code here
        pass

    if utterance == "[she] draw [54] [animals]":
        # write your code here
        pass

    if utterance == "[she] go to the [store] [to] get [3] [more] [pieces] [of] [gum]":
        # write your code here
        pass

    if utterance == "[she] go to the [store] and get [70 pieces of] [strawberry] [gum] and [10 pieces of] [bubble] [gum]":
        # write your code here
        pass

    if utterance == "[she] have [18 paintings of] [flowers]":
        # write your code here
        pass

    if utterance == "[she] have [80] [crayons]":
        # write your code here
        pass

    if utterance == "[two] [numbers] whose sum be [62]":
        # write your code here
        pass

    if utterance == "[with] sum [10]":
        # write your code here
        pass

    if utterance == "a [stack of] [700] [sheets] [of] [used] [paper]":
        # write your code here
        pass

    if utterance == "and [5 stacks of] [pasta] [salad]":
        # write your code here
        pass

    if utterance == "the [CN] [Tower] stand [at] [553 meters] [high]":
        # write your code here
        pass

    if utterance == "the [larger] [number] be [five] [more] [than] the [smaller] [number]":
        # write your code here
        pass

    if utterance == "the sum [of] [two] [numbers] be [twenty-three]":
        # write your code here
        pass

    if utterance == "the sum [of] the digits [of] a [two] digit number be [15]":
        # write your code here
        pass

    if utterance == "the sum be [36]":
        # write your code here
        pass

    if utterance == "their sum be [88]":
        # write your code here
        pass

    if utterance == "there be [4 stacks of] [chocolate] [puddings]":
        # write your code here
        pass

    if utterance == "there be [6] [tennis] [balls]":
        # write your code here
        pass

    if utterance == "there be [7] [tables]":
        # write your code here
        pass

    if utterance == "there be a [stack of] [6] [bricks]":
        # write your code here
        pass

    return resultDICT