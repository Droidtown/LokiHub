#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for gym_price

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
import random
import pandas as pd

DEBUG_gym_price = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_pants":["單車褲","瑜珈褲","短褲","運動褲"],"_rocks":["岩石","岩點","手點","攀岩鞋","攀岩鞋子","石頭","點"],"_shoes":["岩鞋","抱石鞋","鞋子"],"_sides":["中部","北部","南部","東部","西部"],"_tmpFix":["規則"],"_whatIs":["星光票"],"_clothes":["上衣","服裝","短袖","短袖上衣","短袖衣服","衣服","衣著","衣褲","長袖","長袖上衣","長袖衣服"],"_climbing":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石","抱石攀岩","速度攀","速度攀登"],"_cityAlias":["區域","地區","城市","縣市","都市"],"_gymsShort":["8a攀岩場","B-plus","Boulder Space","Camp 4","Corner","Dapro","K2","MegaSTONE","POGO","TheDepotCity","Up聯盟","Y17","double 8","double8","久淘","千手抱石","原岩","嗨翻","嘉義攀岩會館","圓石","圓石空間","宜蘭運動中心","小岩館","崩岩","抱石基地","攀吶","新竹紅石","水美iClimb","汐止抱石館","爬森","破舊二廠","破舊工廠","禾匠","紅石","艾思博","蕃薯藤","角岩館","風城"],"_peClothes":["單車褲","瑜珈褲","運動服","運動衣","運動褲","運動鞋"],"_rockTypes":["crimp","edge","flat","horn","jug","pinch","pocket","sloper","volume"],"_climbingGym":["岩場","岩館","攀岩場","攀岩館"],"_taiwanAlias":["全台","全台各地","全臺","全臺各地","台灣","臺灣"],"_climbingEquip":["岩粉","岩點刷","攀岩刷","攀岩粉","攀岩粉袋","止滑粉","碳酸鎂粉","粉球","粉袋","裝","裝備","鎂粉","鎂粉球"],"_topRopingEquip":["吊帶","垂降手套","安全吊帶","安全扣","安全扣環","快扣","手套","確保器","確保手套","耐磨手套"]}

gymsInfo = pd.read_csv('data/climbingGym.csv', encoding = 'utf-8')
defaultResponse = json.load(open("data/defaultResponse.json",encoding="utf-8"))
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_gym_price:
        print("[gym_price] {} ===> {}".format(inputSTR, utterance))

def getPriceStr(priceSet):
    output = ""
    for i in priceSet:
        output += i[0]
        if i[1] != "na":
            output += " 平日票" + str(i[1])
        if i[2] != "na":
            output += " 假日票" + str(i[2])
        if i[3] != "na":
            output += " 星光票" + str(i[3])
        if i[4] != "na":
            output += " 時票" + str(i[4]) + "\n"
    return output

def getGymPrice(gym):
    priceSet = set()
    if gym == "double8":
        gym = "double 8"
    elif gym == "camp4" or gym == "Camp4" or gym == "camp 4":
        gym = "Camp 4"

    for i in range(len(gymsInfo)):
        gymPriceList = []  
        if gym in gymsInfo.iloc[i, 0]:
            gymPriceList.append(gymsInfo.iloc[i, 0])
            for j in range(7, 11):
                gymPriceList.append(gymsInfo.iloc[i, j])
            priceSet.add(tuple(gymPriceList)) #list[name, weekdays, weekends, night, hour]
    gymPrice = getPriceStr(priceSet)
    return gymPrice


def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[double 8][一個][人]多少[錢]":
        if args[0] in userDefinedDICT["_gymsShort"]:
            resultDICT["reply_gym_name"] = args[0]
            gymPrice = getGymPrice(args[0])
            resultDICT["reply_gym_price"] = gymPrice
        elif args[0] in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_price"] = defaultResponse["_climbing_price"]
        else:
            resultDICT["reply_gym_price"] = "台灣沒有這間岩館哦"

    if utterance == "[抱石][一次]多少[錢]":
        if args[0] in userDefinedDICT["_gymsShort"]:
            resultDICT["reply_gym_name"] = args[0]
            gymPrice = getGymPrice(args[0])
            resultDICT["reply_gym_price"] = gymPrice
        elif args[0] in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_price"] = defaultResponse["_climbing_price"]
        else:
            resultDICT["reply_gym_price"] = "台灣沒有這間岩館哦"

    if utterance == "[抱石][通常]要花多少":
        if args[0] in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_price"] = defaultResponse["_climbing_price"]
        else:
            resultDICT["reply_gym_price"] = "台灣沒有這間岩館哦"

    if utterance == "[紅石][一次]多少":
        if args[0] in userDefinedDICT["_gymsShort"]:
            resultDICT["reply_gym_name"] = args[0]
            gymPrice = getGymPrice(args[0])
            resultDICT["reply_gym_price"] = gymPrice
        elif args[0] in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_price"] = defaultResponse["_climbing_price"]
        else:
            resultDICT["reply_gym_price"] = "台灣沒有這間岩館哦"

    if utterance == "[紅石][票價]多少":
        if args[0] in userDefinedDICT["_gymsShort"]:
            resultDICT["reply_gym_name"] = args[0]
            gymPrice = getGymPrice(args[0])
            resultDICT["reply_gym_price"] = gymPrice
        elif args[0] in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_price"] = defaultResponse["_climbing_price"]
        else:
            resultDICT["reply_gym_price"] = "台灣沒有這間岩館哦"

    if utterance == "[紅石]攀岩[一天]多少[錢]":
        if args[0] in userDefinedDICT["_gymsShort"]:
            resultDICT["reply_gym_name"] = args[0]
            gymPrice = getGymPrice(args[0])
            resultDICT["reply_gym_price"] = gymPrice
        elif args[0] in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_price"] = defaultResponse["_climbing_price"]
        else:
            resultDICT["reply_gym_price"] = "台灣沒有這間岩館哦"

    if utterance == "[紅石]攀岩[一次]多少":
        if args[0] in userDefinedDICT["_gymsShort"]:
            resultDICT["reply_gym_name"] = args[0]
            gymPrice = getGymPrice(args[0])
            resultDICT["reply_gym_price"] = gymPrice
        elif args[0] in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_price"] = defaultResponse["_climbing_price"]
        else:
            resultDICT["reply_gym_price"] = "台灣沒有這間岩館哦"

    if utterance == "去[double8]攀岩[一次]多少":
        if args[0] in userDefinedDICT["_gymsShort"]:
            resultDICT["reply_gym_name"] = args[0]
            gymPrice = getGymPrice(args[0])
            resultDICT["reply_gym_price"] = gymPrice
        elif args[0] in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_price"] = defaultResponse["_climbing_price"]
        else:
            resultDICT["reply_gym_price"] = "台灣沒有這間岩館哦"

    if utterance == "去[一次][岩館]多少[錢]":
        if args[1] in userDefinedDICT["_gymsShort"]:
            resultDICT["reply_gym_name"] = args[1]
            gymPrice = getGymPrice(args[1])
            resultDICT["reply_gym_price"] = gymPrice
        elif args[1] in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_price"] = defaultResponse["_climbing_price"]
        else:
            resultDICT["reply_gym_price"] = "台灣沒有這間岩館哦"

    if utterance == "去[抱石][一次]多少":
        if args[0] in userDefinedDICT["_gymsShort"]:
            resultDICT["reply_gym_name"] = args[0]
            gymPrice = getGymPrice(args[0])
            resultDICT["reply_gym_price"] = gymPrice
        elif args[0] in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_price"] = defaultResponse["_climbing_price"]
        else:
            resultDICT["reply_gym_price"] = "台灣沒有這間岩館哦"

    if utterance == "去攀[一次]岩多少[錢]":
        resultDICT["reply_gym_price"] = defaultResponse["_climbing_price"]

    if utterance == "去攀岩[一次]多少":
        resultDICT["reply_gym_price"] = defaultResponse["_climbing_price"]

    if utterance == "去攀岩[一次]多少[錢]":
        resultDICT["reply_gym_price"] = defaultResponse["_climbing_price"]

    if utterance == "攀岩[一次]多少[錢]":
        resultDICT["reply_gym_price"] = defaultResponse["_climbing_price"]

    if utterance == "攀岩[通常]要花多少":
        resultDICT["reply_gym_price"] = defaultResponse["_climbing_price"]

    if utterance == "去攀[一次][岩]多少[錢]":
        resultDICT["reply_gym_price"] = defaultResponse["_climbing_price"]

    return resultDICT