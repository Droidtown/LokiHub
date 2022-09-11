#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for warm_blessing

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
from datetime import datetime
import re

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["articut_key"])

DEBUG_warm_blessing = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asNoun":["連假","線上","進班","遠距","面對面","愉快","線下","到班","實體課程"],"_asOkay":["ok","OK","oK","Ok","Okay","okay","OKAY"],"_asTime":["小時半"],"_asVerb":["改一下","討論一下","調整一下"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_warm_blessing:
        print("[warm_blessing] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["warm_blessing"] = {}
    if utterance == "[中秋節]快樂":
        if  len(inputSTR) >= 15:
            pass
        elif "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("warm_blessing")
            infoDICT = articut.parse(args[0], userDefinedDictFILE = "./intent/USER_DEFINED.json")
            try:
                resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]*?)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
            except:
                resultDICT["warm_blessing"]["Holiday"] = "unknown"
        else: 
            resultDICT["intentLIST"].append("warm_blessing")
            infoDICT = articut.parse(args[0], userDefinedDictFILE = "./intent/USER_DEFINED.json")
            try:
                resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]*?)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
            except:
                resultDICT["warm_blessing"]["Holiday"] = "unknown"

    if utterance == "[中秋節]愉快":
        if  len(inputSTR) >= 15:
            pass
        elif "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("warm_blessing")
            infoDICT = articut.parse(args[0], userDefinedDictFILE = "./intent/USER_DEFINED.json")
            try:
                resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]*?)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
            except:
                resultDICT["warm_blessing"]["Holiday"] = "unknown"
        else: 
            resultDICT["intentLIST"].append("warm_blessing")
            infoDICT = articut.parse(args[0], userDefinedDictFILE = "./intent/USER_DEFINED.json")
            try:
                resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]*?)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
            except:
                resultDICT["warm_blessing"]["Holiday"] = "unknown"

    if utterance == "[假期]快樂":
        if  len(inputSTR) >= 15:
            pass
        elif "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("warm_blessing")
            infoDICT = articut.parse(args[0], userDefinedDictFILE = "./intent/USER_DEFINED.json")
            try:
                resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]*?)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
            except:
                resultDICT["warm_blessing"]["Holiday"] = "unknown"
        else: 
            resultDICT["intentLIST"].append("warm_blessing")
            infoDICT = articut.parse(args[0], userDefinedDictFILE = "./intent/USER_DEFINED.json")
            try:
                resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]*?)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
            except:
                resultDICT["warm_blessing"]["Holiday"] = "unknown"

    if utterance == "[假期]愉快":
        if  len(inputSTR) >= 15:
            pass
        elif "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("warm_blessing")
            infoDICT = articut.parse(args[0], userDefinedDictFILE = "./intent/USER_DEFINED.json")
            try:
                resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]*?)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
            except:
                resultDICT["warm_blessing"]["Holiday"] = "unknown"
        else: 
            resultDICT["intentLIST"].append("warm_blessing")
            infoDICT = articut.parse(args[0], userDefinedDictFILE = "./intent/USER_DEFINED.json")
            try:
                resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]*?)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
            except:
                resultDICT["warm_blessing"]["Holiday"] = "unknown"

    if utterance == "祝[你]":
        if  len(inputSTR) >= 15:
            pass
        elif "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("warm_blessing")
            infoDICT = articut.parse(args[0], userDefinedDictFILE = "./intent/USER_DEFINED.json")
            try:
                resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]*?)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
            except:
                resultDICT["warm_blessing"]["Holiday"] = "unknown"
        else: 
            resultDICT["intentLIST"].append("warm_blessing")
            infoDICT = articut.parse(args[0], userDefinedDictFILE = "./intent/USER_DEFINED.json")
            try:
                resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]*?)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
            except:
                resultDICT["warm_blessing"]["Holiday"] = "unknown"

    if utterance == "祝[老師]":
        if  len(inputSTR) >= 15:
            pass
        elif "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("warm_blessing")
            infoDICT = articut.parse(args[0], userDefinedDictFILE = "./intent/USER_DEFINED.json")
            try:
                resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]*?)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
            except:
                resultDICT["warm_blessing"]["Holiday"] = "unknown"
        else: 
            resultDICT["intentLIST"].append("warm_blessing")
            infoDICT = articut.parse(args[0], userDefinedDictFILE = "./intent/USER_DEFINED.json")
            try:
                resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]*?)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
            except:
                resultDICT["warm_blessing"]["Holiday"] = "unknown"

    return resultDICT