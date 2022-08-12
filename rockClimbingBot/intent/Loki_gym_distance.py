#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for gym_distance

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

DEBUG_gym_distance = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_can":["可以","可","適合"],"_pants":["褲子","褲","長褲","短褲","運動褲","瑜珈褲","單車褲"],"_rocks":["岩點","石頭","手點","點","岩石","攀岩鞋","攀岩鞋子"],"_shoes":["岩鞋","鞋子","抱石鞋","鞋"],"_sides":["東部","北部","南部","西部","中部"],"_levels":["難度","等級","階級","級數"],"_whatIs":["星光票"],"_clothes":["衣服","長袖","短袖","衣著","服裝","長袖衣服","上衣","短袖衣服","長袖上衣","短袖上衣","衣褲"],"_climbing":["上攀","速度攀","速度攀登","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石攀岩","抱石"],"_cityAlias":["縣市","縣","市","地區","都市","城市","區","區域"],"_gymsShort":["紅石","小岩館","Camp 4","角岩館","Corner","汐止抱石館","double8","double 8","原岩","Up聯盟","MegaSTONE","POGO","爬森","蕃薯藤","千手抱石","水美iClimb","風城","B-plus","新竹紅石","TheDepotCity","攀吶","Dapro","破舊二廠","破舊工廠","嗨翻","抱石基地","圓石","圓石空間","Boulder Space","K2","艾思博","禾匠","崩岩","久淘","宜蘭運動中心","嘉義攀岩會館","8a攀岩場","Y17"],"_peClothes":["運動衣","運動褲","運動服","瑜珈褲","單車褲"],"_rockTypes":["jug","pinch","sloper","edge","crimp","pocket","flat","horn","volume"],"_climbingGym":["岩館","攀岩館","攀岩場","抱石館","抱石場館","抱石場","岩場","上攀館","上攀場","上攀場館","攀石場","上攀場館","上攀岩館","先鋒攀岩館","速度攀岩館","速度攀登場館","速度攀場館","速度攀登岩館","速度攀場地"],"_taiwanAlias":["全台","全臺","全台各地","台灣","臺灣","全臺各地"],"_climbingEquip":["裝","裝備","岩粉","粉袋","攀岩粉袋","粉球","止滑粉","攀岩粉","攀岩粉袋","岩點刷","攀岩刷","鎂粉球","鎂粉","碳酸鎂粉"],"_normalWearings":["一般運動鞋","牛仔褲"],"_topRopingEquip":["手套","確保手套","垂降手套","耐磨手套","安全吊帶","確保器","安全扣","快扣","安全扣環","吊帶"],"_climbingGeneralGym":["岩館","攀岩館","攀岩場","攀岩場館"]}

defaultResponse = json.load('data/defaultResponse.json', 'r', encoding = 'utf-8')
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_gym_distance:
        print("[gym_distance] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[上攀][可以]去哪裡":
        if args[0] in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_distance"] = defaultResponse["gym_distance"]
        else:
            resultDICT["_gym_distance"] = defaultResponse["_not_rock_climbing"][random.randint(1,3)]

    if utterance == "[我]在[台中]":
        

    if utterance == "[我]在[東部]":
        

    if utterance == "哪裡[可以][上攀]":
        if args[1] in userDefinedDICT["_climbing"]:
            resultDICT["_gym_distance"] = defaultResponse["gym_distance"]
        else:
            resultDICT["_gym_distance"] = defaultResponse["_not_rock_climbing"][random.randint(1,3)]

    if utterance == "哪裡[可以]攀岩":
        resultDICT["_gym_distance"] = defaultResponse["gym_distance"]

    if utterance == "哪間[岩館]離[我][最近]":
        if args[0] in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_distance"] = defaultResponse["gym_distance"]
        else:
            resultDICT["_gym_distance"] = defaultResponse["_not_rock_climbing"][random.randint(1,3)]

    if utterance == "想[抱石][可以]去哪裡":
        if args[0] in userDefinedDICT["_climbing"]:
            resultDICT["_gym_distance"] = defaultResponse["gym_distance"]
        else:
            resultDICT["_gym_distance"] = defaultResponse["_not_rock_climbing"][random.randint(1,3)]

    if utterance == "想攀[先鋒攀][可以]去哪":
        if args[0] in userDefinedDICT["_climbing"]:
            resultDICT["_gym_distance"] = defaultResponse["gym_distance"]
        else:
            resultDICT["_gym_distance"] = defaultResponse["_not_rock_climbing"][random.randint(1,3)]

    if utterance == "想攀岩[可以]去哪":
        resultDICT["_gym_distance"] = defaultResponse["gym_distance"]

    if utterance == "推薦哪些距離[近]的[岩館]":
        if args[1] in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_distance"] = defaultResponse["gym_distance"]
        else:
            resultDICT["_gym_distance"] = defaultResponse["_not_rock_climbing"][random.randint(1,3)]

    if utterance == "攀岩[可以]去哪裡":
        resultDICT["_gym_distance"] = defaultResponse["gym_distance"]

    if utterance == "有哪些[岩館]呢":
        if args[0] in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_distance"] = defaultResponse["gym_distance"]
        else:
            resultDICT["_gym_distance"] = defaultResponse["_not_rock_climbing"][random.randint(1,3)]

    if utterance == "有推薦的[岩館][麻]":
        if args[0] in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_distance"] = defaultResponse["gym_distance"]
        else:
            resultDICT["_gym_distance"] = defaultResponse["_not_rock_climbing"][random.randint(1,3)]

    if utterance == "比較近的[岩館]有哪些":
        if args[0] in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_distance"] = defaultResponse["gym_distance"]
        else:
            resultDICT["_gym_distance"] = defaultResponse["_not_rock_climbing"][random.randint(1,3)]

    if utterance == "要[抱石][可以]去哪裡":
        if args[0] in userDefinedDICT["_climbing"]:
            resultDICT["_gym_distance"] = defaultResponse["gym_distance"]
        else:
            resultDICT["_gym_distance"] = defaultResponse["_not_rock_climbing"][random.randint(1,3)]

    if utterance == "離[我][最近]的[岩館]是哪間": ###
        if args[2] in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_distance"] = defaultResponse["gym_distance"]
        else:
            resultDICT["_gym_distance"] = defaultResponse["_not_rock_climbing"][random.randint(1,3)]

    if utterance == "離[我][最近]的[岩館]有哪些":
        if args[2] in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_distance"] = defaultResponse["gym_distance"]
        else:
            resultDICT["_gym_distance"] = defaultResponse["_not_rock_climbing"][random.randint(1,3)]

    if utterance == "離[我][近]的[岩館]有[比較]推薦的嗎":
        if args[2] in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_distance"] = defaultResponse["gym_distance"]
        else:
            resultDICT["_gym_distance"] = defaultResponse["_not_rock_climbing"][random.randint(1,3)]

    if utterance == "離我[媽][最近]的[岩館]有哪些":
        if args[2] in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_distance"] = defaultResponse["gym_distance"]
        else:
            resultDICT["_gym_distance"] = defaultResponse["_not_rock_climbing"][random.randint(1,3)]

    if utterance == "離我[家][最近]的[岩館]是哪間":
        if args[2] in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_distance"] = defaultResponse["gym_distance"]
        else:
            resultDICT["_gym_distance"] = defaultResponse["_not_rock_climbing"][random.randint(1,3)]
            
    return resultDICT