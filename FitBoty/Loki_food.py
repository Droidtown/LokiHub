#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for food

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

from ArticutAPI import Articut
import cn2num
import json
import os
import re

with open("account.info.json", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())
articut = Articut(username = accountDICT["username"], apikey = accountDICT["api_key"])

DEBUG_food = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asSports":["丟飛盤","划獨木舟","划船","攀岩","游泳","溜直排輪","滑雪","爬山","登山","走路","跑步","跳繩","跳舞","騎馬"],"_foodName":["便當"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def loadJson(filename):
    with open(filename,"r") as f:
        result = json.load(f)
    return result

foodDICT  = loadJson("foodDICT.json")

def debugInfo(inputSTR, utterance):
    if DEBUG_food:
        print("[food] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "吃了[一盤][水果]":
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[0]:
                amount = cn2num.transform(i)
            elif re.search("\d*", args[0]) != None:
                amount = str(list(articut.parse(args[0],level="lv3")["number"].values())[0])
        if args[1] in foodDICT.keys():
            cal = foodDICT[args[1]]
        resultDICT["food_cal"] = int(amount)*int(cal)


    if utterance == "吃了[一盤][炒飯]和[一碗][湯]":
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[0]:
                amount_1 = cn2num.transform(i)
            elif re.search("\d*", args[0]) != None:
                amount_1 = str(list(articut.parse(args[0],level="lv3")["number"].values())[0])
        if args[1] in foodDICT.keys():
            cal_1 = foodDICT[args[1]]

        for i in num:
            if i in args[2]:
                amount_2 = cn2num.transform(i)
            elif re.search("\d*", args[2]) != None:
                amount_2 = str(list(articut.parse(args[2],level="lv3")["number"].values())[0])
        if args[3] in foodDICT.keys():
            cal_2 = foodDICT[args[3]]
        resultDICT["food_cal"] = int(amount_1)*int(cal_1)+int(amount_2)*int(cal_2)

    if utterance == "吃了[一碗][糙米飯]、[一盤][小菜]和[一碗][湯]":
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[0]:
                amount_1 = cn2num.transform(i)
            elif re.search("\d*", args[0]) != None:
                amount_1 = str(list(articut.parse(args[0],level="lv3")["number"].values())[0])
        if args[1] in foodDICT.keys():
            cal_1 = foodDICT[args[1]]
        for i in num:
            if i in args[2]:
                amount_2 = cn2num.transform(i)
            elif re.search("\d*", args[2]) != None:
                amount_2 = str(list(articut.parse(args[2],level="lv3")["number"].values())[0])
        if args[3] in foodDICT.keys():
            cal_2 = foodDICT[args[3]]
        for i in num:
            if i in args[4]:
                amount_3 = cn2num.transform(i)
            elif re.search("\d*", args[4]) != None:
                amount_3 = str(list(articut.parse(args[4],level="lv3")["number"].values())[0])
        if args[5] in foodDICT.keys():
            cal_3 = foodDICT[args[5]]        
        resultDICT["food_cal"] = int(amount_1)*int(cal_1)+int(amount_2)*int(cal_2)+int(amount_3)*int(cal_3)

    return resultDICT