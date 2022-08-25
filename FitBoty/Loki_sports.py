#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for sports

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

from ArticutAPI import Articut
import json
import os
import re

with open("account.info.json", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())
articut = Articut(username = accountDICT["username"], apikey = accountDICT["api_key"])


DEBUG_sports = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asSports":["丟飛盤","划獨木舟","划船","攀岩","游泳","溜直排輪","滑雪","爬山","登山","走路","跑步","跳繩","跳舞","騎馬"],"_foodName":["便當"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def loadJson(filename):
    with open(filename,"r") as f:
        result = json.load(f)
    return result

sportsDICT  = loadJson("sports_dict.json")

def debugInfo(inputSTR, utterance):
    if DEBUG_sports:
        print("[sports] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[跳繩][30分鐘]":
        if args[0] in sportsDICT.keys():
            sports = sportsDICT[args[0]]
        if re.search("\d+分鐘", args[1]) != None:
            time = int(re.search("(\d+)分鐘", args[1]).group(1))
        elif re.search("\d+小時", args[1]) != None:
            time = int(re.search("(\d+)小時", args[1]).group(1))*60
        resultDICT["sports_cal"] = float(sports)*int(time)

    if utterance == "[跳繩][30分鐘]和[重訓][1小時]":
        if args[0] in sportsDICT.keys():
            sports_1 = sportsDICT[args[0]]
        if re.search("\d+分鐘", args[1]) != None:
            time_1 = int(re.search("(\d+)分鐘", args[1]).group(1))
        elif re.search("\d+小時", args[1]) != None:
            time_1 = int(re.search("(\d+)小時", args[1]).group(1))*60
        
        if args[2] in sportsDICT.keys():
            sports_2 = sportsDICT[args[2]]
        if re.search("\d+分鐘", args[3]) != None:
            time_2 = int(re.search("(\d+)分鐘", args[3]).group(1))
        elif re.search("\d+小時", args[3]) != None:
            time_2 = int(re.search("(\d+)小時", args[3]).group(1))*60
        
        resultDICT["sports_cal"] = float(sports_1)*int(time_1) + float(sports_2)*int(time_2)

    if utterance == "[跳繩]和[重訓]各[30分鐘]":
        if args[0] in sportsDICT.keys():
            sports_1 = sportsDICT[args[0]]
        if args[1] in sportsDICT.keys():
            sports_2 = sportsDICT[args[1]]
        if re.search("\d+分鐘", args[2]) != None:
            time = int(re.search("(\d+)分鐘", args[2]).group(1))
        elif re.search("\d+小時", args[2]) != None:
            time = int(re.search("(\d+)小時", args[2]).group(1))*60
        resultDICT["sports_cal"] = (float(sports_1) + float(sports_2))*int(time)

    if utterance == "做[瑜伽][30分鐘]":
        if args[0] in sportsDICT.keys():
            sports = sportsDICT[args[0]]
        if re.search("\d+分鐘", args[1]) != None:
            time = int(re.search("(\d+)分鐘", args[1]).group(1))
        elif re.search("\d+小時", args[1]) != None:
            time = int(re.search("(\d+)小時", args[1]).group(1))*60
        resultDICT["sports_cal"] = float(sports)*int(time)

    if utterance == "打[排球][30分鐘]":
        if args[0] in sportsDICT.keys():
            sports = sportsDICT[args[0]]
        if re.search("\d+分鐘", args[1]) != None:
            time = int(re.search("(\d+)分鐘", args[1]).group(1))
        elif re.search("\d+小時", args[1]) != None:
            time = int(re.search("(\d+)小時", args[1]).group(1))*60
        resultDICT["sports_cal"] = float(sports)*int(time)

    if utterance == "沒有":
        resultDICT["sports_cal"] == 0

    if utterance == "沒有運動":
        resultDICT["sports_cal"] == 0

    if utterance == "爬[樓梯][30分鐘]":
        if args[0] in sportsDICT.keys():
            sports = sportsDICT[args[0]]
        if re.search("\d+分鐘", args[1]) != None:
            time = int(re.search("(\d+)分鐘", args[1]).group(1))
        elif re.search("\d+小時", args[1]) != None:
            time = int(re.search("(\d+)小時", args[1]).group(1))*60
        resultDICT["sports_cal"] = float(sports)*int(time)
        
    if utterance == "跳[國標舞][30分鐘]":
        if args[0] in sportsDICT.keys():
            sports = sportsDICT[args[0]]
        if re.search("\d+分鐘", args[1]) != None:
            time = int(re.search("(\d+)分鐘", args[1]).group(1))
        elif re.search("\d+小時", args[1]) != None:
            time = int(re.search("(\d+)小時", args[1]).group(1))*60
        resultDICT["sports_cal"] = float(sports)*int(time)
        
    if utterance == "騎[腳踏車][30分鐘]":
        if args[0] in sportsDICT.keys():
            sports = sportsDICT[args[0]]
        if re.search("\d+分鐘", args[1]) != None:
            time = int(re.search("(\d+)分鐘", args[1]).group(1))
        elif re.search("\d+小時", args[1]) != None:
            time = int(re.search("(\d+)小時", args[1]).group(1))*60
        resultDICT["sports_cal"] = float(sports)*int(time)

    return resultDICT