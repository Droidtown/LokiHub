#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for class_arrangement

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
from ArticutAPI import Articut
import os
import re
from datetime import datetime

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["articut_key"])

DEBUG_class_arrangement = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asNoun":["連假","線上","進班","遠距","面對面","愉快","線下","到班","實體課程"],"_asOkay":["ok","OK","oK","Ok","Okay","okay","OKAY"],"_asTime":["小時半"],"_asVerb":["改一下","討論一下","調整一下"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_class_arrangement:
        print("[class_arrangement] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["class_arrangement"] = {}
    if utterance == "[8].OK嗎":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "[8].[你]OK嗎":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "[8].[你][可以]嗎":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "[8].[你][方便]嗎":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "[8].[可以]幫[XX]上課嗎":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[2]

    if utterance == "[8].[可以]幫[弟弟]上課嗎":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[2]

    if utterance == "[8].[老師]OK嗎":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "[8].[老師][可以]嗎":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "[8].[老師][方便]嗎":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "[XX][先]延[後][一]小時半":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[3]+"小時半"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]延[後][一個]小時半":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[3]+"小時半"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]延[後][半個][小時]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[3]+args[4]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]延[後][半小時]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[3]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]延[後]到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]延[後]到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]提早[一]小時半":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[2]+"小時半"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]提早[半個][小時]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[2]+args[3]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]提早[半小時]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[2]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]提早到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]提早到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]換到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]換到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]換成[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]換成[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]換至[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]換至[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]改[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]改[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]改到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]改到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]改至[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]改至[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]調到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]調到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]調成[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]調成[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]調整到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]調整到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]調整成[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]調整成[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]調整至[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]調整至[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]調至[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][先]調至[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]延[後][一]小時半":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[4]+"小時半"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]延[後][一個]小時半":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[4]+"小時半"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]延[後][半個][小時]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[4]+args[5]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]延[後][半小時]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[4]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]延[後]到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[4]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]延[後]到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[4]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]提早[一]小時半":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[3]+"小時半"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]提早[半個][小時]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[3]+args[4]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]提早[半小時]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[3]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]提早到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[3]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]提早到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[3]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]換到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]換到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]換成[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]換成[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]換至[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]換至[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]改[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]改[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]改到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]改到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]改至[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]改至[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]調到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]調到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]調成[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]調成[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]調整到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]調整到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]調整成[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]調整成[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]調整至[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]調整至[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]調至[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[XX][可能]要[先]調至[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[八點][你]OK嗎":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "[八點][你][方便]嗎":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "[八點][老師]OK嗎":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "[八點][老師][可以]嗎":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "[八點][老師][方便]嗎":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "[弟弟][先]延[後][一]小時半":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[3]+"小時半"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]延[後][一個]小時半":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[3]+"小時半"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]延[後][半個][小時]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[3]+args[4]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]延[後][半小時]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[3]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]延[後]到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]延[後]到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]提早[一]小時半":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[2]+小時半
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]提早[半個][小時]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[2]+args[3]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]提早[半小時]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[2]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]提早到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]提早到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]換到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]換到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]換成[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]換成[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]換至[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]換至[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]改[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]改[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]改到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]改到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]改至[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]改至[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]調到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]調到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]調成[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]調成[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]調整到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]調整到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]調整成[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]調整成[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]調整至[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]調整至[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]調至[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][先]調至[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[2]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]延[後][一]小時半":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[4]+"小時半"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]延[後][一個]小時半":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[4]+"小時半"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]延[後][半個][小時]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[4]+args[5]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]延[後][半小時]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[4]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]延[後]到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[4]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]延[後]到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[4]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]提早[一]小時半":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[3]+"小時半"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]提早[半個][小時]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[3]+args[4]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]提早[半小時]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[3]
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]提早到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]提早到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]換到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]換到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]換成[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]換成[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]換至[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]換至[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]改[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]改[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]改到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]改到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]改至[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]改至[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]調到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]調到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]調成[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]調成[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]調整到[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]調整到[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]調整成[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]調整成[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]調整至[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]調整至[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]調至[8].":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[弟弟][可能]要[先]調至[八點]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[3]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "[禮拜天][可以]幫[XX]上課嗎":
        # write your code here
        pass

    if utterance == "[禮拜天][可以]幫[弟弟]上課嗎":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[2]

    if utterance == "改[XX]的[時間]":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[2]

    if utterance == "改[弟弟]的時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "改[週四]的時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "改一下[XX]的時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "改一下[弟弟]的時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "改一下[週四]的時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "改一下上課時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "改一下時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "改上課時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "改時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "討論[XX]的時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "討論[弟弟]的時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "討論[週四]的時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "討論一下[XX]的時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "討論一下[弟弟]的時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "討論一下[週四]的時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "討論一下上課時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "討論一下時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "討論上課時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "討論時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "調整[XX]的時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "調整[弟弟]的時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "調整[週四]的時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "調整一下[XX]的時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "調整一下[弟弟]的時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "調整一下[週四]的時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]

    if utterance == "調整一下上課時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "調整一下時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "調整上課時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    if utterance == "調整時間":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("class_arrangement")
        else: 
            resultDICT["intentLIST"].append("class_arrangement") 
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"

    return resultDICT