#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for whatIs

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

DEBUG_whatIs = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_pants":["單車褲","瑜珈褲","短褲","運動褲"],"_rocks":["岩石","岩點","手點","攀岩鞋","攀岩鞋子","石頭","點"],"_shoes":["岩鞋","抱石鞋","鞋子"],"_sides":["中部","北部","南部","東部","西部"],"_tmpFix":["規則"],"_whatIs":["星光票"],"_clothes":["上衣","服裝","短袖","短袖上衣","短袖衣服","衣服","衣著","衣褲","長袖","長袖上衣","長袖衣服"],"_climbing":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石","抱石攀岩","速度攀","速度攀登"],"_cityAlias":["區域","地區","城市","縣市","都市"],"_gymsShort":["8a攀岩場","B-plus","Boulder Space","Camp 4","Corner","Dapro","K2","MegaSTONE","POGO","TheDepotCity","Up聯盟","Y17","double 8","double8","久淘","千手抱石","原岩","嗨翻","嘉義攀岩會館","圓石","圓石空間","宜蘭運動中心","小岩館","崩岩","抱石基地","攀吶","新竹紅石","水美iClimb","汐止抱石館","爬森","破舊二廠","破舊工廠","禾匠","紅石","艾思博","蕃薯藤","角岩館","風城"],"_peClothes":["單車褲","瑜珈褲","運動服","運動衣","運動褲","運動鞋"],"_rockTypes":["crimp","edge","flat","horn","jug","pinch","pocket","sloper","volume"],"_climbingGym":["岩場","岩館","攀岩場","攀岩館"],"_taiwanAlias":["全台","全台各地","全臺","全臺各地","台灣","臺灣"],"_climbingEquip":["岩粉","岩點刷","攀岩刷","攀岩粉","攀岩粉袋","止滑粉","碳酸鎂粉","粉球","粉袋","裝","裝備","鎂粉","鎂粉球"],"_topRopingEquip":["吊帶","垂降手套","安全吊帶","安全扣","安全扣環","快扣","手套","確保器","確保手套","耐磨手套"]}

defaultResponse = json.load(open("data/defaultResponse.json",encoding="utf-8"))
whatIs = json.load(open("data/what_is.json",encoding="utf-8"))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_whatIs:
        print("[whatIs] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[jug]是什麼？":
        resultDICT["_what"] = args[0]
        if args[0] in userDefinedDICT["_rockTypes"]:
            resultDICT["_what_is"] = "{}是一種岩點".format(args[0])
        elif args[0] in userDefinedDICT["_climbingEquip"] and args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["_what_is"] = "{}是一種攀岩用具".format(args[0])
        elif args[0] in whatIs.keys():
            resultDICT["_what_is"] = whatIs[args[0]]
        else:
            resultDICT["_what_is"] = random.choice(defaultResponse["_Not_sure"])

    if utterance == "[星光票]的[意思]是？":
        resultDICT["_what"] = args[0]
        if args[0] in userDefinedDICT["_rockTypes"]:
            resultDICT["_what_is"] = "{}是一種岩點".format(args[0])
        elif args[0] in userDefinedDICT["_climbingEquip"] and args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["_what_is"] = "{}是一種攀岩用具".format(args[0])
        elif args[0] in whatIs.keys():
            resultDICT["_what_is"] = whatIs[args[0]]
        else:
            resultDICT["_what_is"] = random.choice(defaultResponse["_Not_sure"])

    if utterance == "什麼是[星光票]？":
        resultDICT["_what"] = args[0]
        if args[0] in userDefinedDICT["_rockTypes"]:
            resultDICT["_what_is"] = "{}是一種岩點".format(args[0])
        elif args[0] in userDefinedDICT["_climbingEquip"] and args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["_what_is"] = "{}是一種攀岩用具".format(args[0])
        elif args[0] in whatIs.keys():
            resultDICT["_what_is"] = whatIs[args[0]]
        else:
            resultDICT["_what_is"] = random.choice(defaultResponse["_Not_sure"])

    if utterance == "那是什麼？":
        resultDICT["_what"] = None

    if utterance == "什麼是攀岩？":
        resultDICT["_what"] = "攀岩"
        resultDICT["_what_is"] = whatIs["攀岩"]

    if utterance == "攀岩是什麼":
        resultDICT["_what"] = "攀岩"
        resultDICT["_what_is"] = whatIs["攀岩"]

    return resultDICT