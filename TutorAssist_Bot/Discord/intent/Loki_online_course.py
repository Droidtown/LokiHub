#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for online_course

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

DEBUG_online_course = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asNoun":["連假","線上","進班","遠距","面對面","愉快","線下","到班","實體課程"],"_asOkay":["ok","OK","oK","Ok","Okay","okay","OKAY"],"_asTime":["小時半"],"_asVerb":["改一下","討論一下","調整一下"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_online_course:
        print("[online_course] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["online_course"] = {}
    if utterance == "[先]恢復線上":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先]恢復視訊":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先]恢復遠距":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先]改線上":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先]改視訊":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先]改遠距":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先]用線上":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先]用視訊":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先]用遠距":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先]維持線上":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先]維持視訊":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先]維持遠距":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先]線上":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先]視訊":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先]調整為線上":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先]調整為視訊":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先]調整為遠距":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先]遠距":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先都]線上":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先都]視訊":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "[先都]遠距":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "要[先]線上":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "要[先]視訊":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    if utterance == "要[先]遠距":
        if "inform_time" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("inform_time")
            resultDICT["intentLIST"].append("online_course")
        else:
            resultDICT["intentLIST"].append("online_course")

    return resultDICT