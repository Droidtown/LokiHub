#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for gym_time

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
from ArticutAPI import Articut
import pandas as pd

DEBUG_gym_time = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_rocks":["岩石","岩點","手點","攀岩鞋","攀岩鞋子","石頭","點"],"_shoes":["岩鞋","抱石鞋","鞋子"],"_sides":["中部","北部","南部","東部","西部"],"_whatIs":["星光票"],"_climbing":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石","抱石攀岩","速度攀","速度攀登"],"_cityAlias":["區域","地區","城市","縣市","都市"],"_gymsShort":["達文西","8a攀岩場","B-plus","Boulder Space","Camp 4","Corner","Dapro","K2","MegaSTONE","POGO","TheDepotCity","Up聯盟","Y17","double 8","double8","久淘","千手抱石","原岩","嗨翻","嘉義攀岩會館","圓石","圓石空間","宜蘭運動中心","小岩館","崩岩","抱石基地","攀吶","新竹紅石","水美iClimb","汐止抱石館","爬森","破舊二廠","破舊工廠","禾匠","紅石","艾思博","蕃薯藤","角岩館","風城"],"_peClothes":["單車褲","瑜珈褲","運動服","運動衣","運動褲","運動鞋"],"_rockTypes":["crimp","edge","flat","horn","jug","pinch","pocket","sloper","volume"],"_climbingGym":["岩場","岩館","攀岩場","攀岩館"],"_taiwanAlias":["全台","全台各地","全臺","全臺各地","台灣","臺灣"],"_clothesPants":["上衣","服裝","短袖","短袖上衣","短袖衣服","衣服","衣著","衣褲","長袖","長袖上衣","長袖衣服","單車褲","瑜珈褲","短褲","運動褲","長褲"],"_climbingEquip":["岩粉","岩點刷","攀岩刷","攀岩粉","攀岩粉袋","止滑粉","碳酸鎂粉","粉球","粉袋","裝","裝備","鎂粉","鎂粉球"],"_topRopingEquip":["吊帶","垂降手套","安全吊帶","安全扣","安全扣環","快扣","手套","確保器","確保手套","耐磨手套"]}

gymsInfo = pd.read_csv('data/climbingGym.csv', encoding = 'utf-8')
accountDICT = json.load(open("account.info", encoding= "utf-8"))
Articut = Articut(username = accountDICT["userName"], apikey = accountDICT["articut_key"])
defaultResponse = json.load(open("data/defaultResponse.json",encoding="utf-8"))
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_gym_time:
        print("[gym_time] {} ===> {}".format(inputSTR, utterance))

def getTimeStr(timeSet):
    timeStr = ""
    for i in timeSet:
        if i[1] != "na" and i[1] != "預約制" and list(timeSet)[0][2] != "na":
            timeStr += "{0}的營業時間為平日{1}，假日{2}".format(i[0],i[1],i[2])
        elif i[1] == "預約制":
            timeStr += "{0}的營業時間採預約制".format(i[0])
        elif i[1] != "na" and i[2] == "na":
            timeStr += "{0}的營業時間為平日{1}".format(i[0],i[1])
        elif i[2] != "na" and i[1] == "na":
            timeStr += "{0}的營業時間為假日{1}".format(i[0],i[2])
        else:
            timeStr += "查無{0}營業時間".format(i[0])
        timeStr += "\n"
    return timeStr

def getGymTime(gym, time):
    timeSet = set()
    if gym == "double8":
        gym = "double 8"
    elif gym == "camp4" or gym == "Camp4" or gym == "camp 4":
        gym = "Camp 4"

    if time == "平日":
        for i in range(len(gymsInfo)): 
            timeList = [] 
            if gym in gymsInfo.iloc[i, 0]:
                timeList.append(gymsInfo.iloc[i, 0])
                timeList.append(gymsInfo[i, 13])
                timeSet.add(timeList)


    elif time == "假日":
        for i in range(len(gymsInfo)): 
            timeList = [] 
            if gym in gymsInfo.iloc[i, 0]:
                timeList.append(gymsInfo.iloc[i, 0])
                timeList.append(gymsInfo[i, 14])
                timeSet.add(timeList)

    else:
        for i in range(len(gymsInfo)): 
            timeList = [] 
            if gym in gymsInfo.iloc[i, 0]:
                timeList.append(gymsInfo.iloc[i, 0])
                timeList.append(gymsInfo[i, 13])
                timeList.append(gymsInfo[i, 14])
                timeSet.add(timeList)
        gymTime = getTimeStr(timeSet)
    return gymTime


def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[啥]時開門":
        # parsedUttr = Articut.parse(utterance)
        # parsed_words = parsedUttr["result_segmentation"]
        # parsed_words = parsed_words.split("/")
        # for word in parsed_words:
        #     if word in userDefinedDICT["_gymsShort"]:
        #         resultDICT["_gym_name"] = word
        #         break
        # for word in parsed_words:
        #     if word in ("平日","假日","平假日"):
        #         resultDICT["_ask_time"] = word
        #         break
        # if resultDICT["_gym_name"] != None:
        #     if resultDICT["_ask_time"] == "平假日" or resultDICT["_ask_time"] == None:

        #         resultDICT["_gym_time"] = "{0}的營業時間為平日{1}，假日{2}".format(resultDICT["_gym_name"], )
        # else:
        #     resultDICT["_gym_time"] = "請問想問哪間岩館呢？"
        pass

    if utterance == "[平常]幾[點]開":
        # write your code here
        pass

    if utterance == "[幾時]營業":
        # write your code here
        pass

    if utterance == "多[早]開":
        # write your code here
        pass

    if utterance == "幾[點]營業":
        # write your code here
        pass

    if utterance == "幾[點]開":
        # write your code here
        pass

    if utterance == "幾[點]開門":
        # write your code here
        pass

    if utterance == "幾[點]關？":
        # write your code here
        pass

    if utterance == "營業[時間]幾[點]到幾[點]？":
        # write your code here
        pass

    if utterance == "營業[時間]是幾[點]？":
        # write your code here
        pass

    if utterance == "營業[時間]是？":
        # write your code here
        pass

    return resultDICT