#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for equipment_list

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
from random import choice

DEBUG_equipment_list = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_rocks":["岩石","岩點","手點","石頭","點"],"_shoes":["岩鞋","抱石鞋","鞋子","攀岩鞋","攀岩鞋子"],"_sides":["中部","北部","南部","東部","西部"],"_whatIs":["星光票"],"_climbing":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石","抱石攀岩","速度攀","速度攀登","攀登","運動攀登"],"_cityAlias":["區域","地區","城市","縣市","都市","地方"],"_gymsShort":["達文西","8a攀岩場","B-plus","Boulder Space","Camp 4","Corner","Dapro","K2","MegaSTONE","POGO","TheDepotCity","Up聯盟","Y17","double 8","double8","久淘","千手抱石","原岩","嗨翻","嘉義攀岩會館","圓石","圓石空間","宜蘭運動中心","小岩館","崩岩","抱石基地","攀吶","新竹紅石","水美iClimb","汐止抱石館","爬森","破舊二廠","破舊工廠","禾匠","紅石","艾思博","蕃薯藤","角岩館","風城"],"_peClothes":["單車褲","瑜珈褲","運動服","運動衣","運動褲","運動鞋","攀岩褲"],"_rockTypes":["crimp","edge","flat","horn","jug","pinch","pocket","sloper","volume"],"_climbingGym":["岩場","岩館","攀岩場","攀岩館","抱石館","上攀館"],"_taiwanAlias":["全台","全台各地","全臺","全臺各地","台灣","臺灣","全台灣"],"_clothesPants":["上衣","服裝","短袖","短袖上衣","短袖衣服","衣服","衣著","衣褲","長袖","長袖上衣","長袖衣服","單車褲","瑜珈褲","短褲","運動褲","長褲"],"_climbingEquip":["岩粉","岩點刷","攀岩刷","攀岩粉","攀岩粉袋","止滑粉","碳酸鎂粉","粉球","粉袋","裝","裝備","鎂粉","鎂粉球"],"_topRopingEquip":["吊帶","垂降手套","安全吊帶","安全扣","安全扣環","快扣","手套","確保器","確保手套","耐磨手套"]}
defaultResponse = json.load(open("data/defaultResponse.json",encoding="utf-8"))
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_equipment_list:
        print("[equipment_list] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[上攀]要準備多少[裝備]":
        if "抱石" in args[0]:
            resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring_b"]
        elif "上攀" in args[0] or "先鋒" in args[0] or "速度" in args[0]:
            resultDICT["reply_equipment_list"] = "{0}{1}".format(args[0],defaultResponse["_equipment_bring_t"])
        else:
            resultDICT["reply_equipment_list"] = choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[抱石]有[服裝][上]的[規定]嗎":
        if args[0] in userDefinedDICT["_climbing"]:
            if args[1] in userDefinedDICT["_clothesPants"]:
                resultDICT["reply_equipment_list"] = defaultResponse["_equipment_wear"]
            else:
                resultDICT["reply_equipment_list"] = choice(defaultResponse["_not_sure"])
        else:
            resultDICT["reply_equipment_list"] = choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[抱石]有什麼是要[先]買好的？":
        if args[0] in userDefinedDICT["_climbing"]:
            resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring"]
        else:
            resultDICT["reply_equipment_list"] = choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[抱石]要[先]買哪些[裝備]":
        if "抱石" in args[0]:
            resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring_b"]
        elif "上攀" in args[0] or "先鋒" in args[0] or "速度" in args[0]:
            resultDICT["reply_equipment_list"] = "{0}{1}".format(args[0],defaultResponse["_equipment_bring_t"])
        else:
            resultDICT["reply_equipment_list"] = choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[抱石]要帶什麼":
        if "抱石" in args[0]:
            resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring_b"]
        elif "上攀" in args[0] or "先鋒" in args[0] or "速度" in args[0]:
            resultDICT["reply_equipment_list"] = "{0}{1}".format(args[0],defaultResponse["_equipment_bring_t"])
        else:
            resultDICT["reply_equipment_list"] = choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[抱石]要準備什麼":
        if "抱石" in args[0]:
            resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring_b"]
        elif "上攀" in args[0] or "先鋒" in args[0] or "速度" in args[0]:
            resultDICT["reply_equipment_list"] = "{0}{1}".format(args[0],defaultResponse["_equipment_bring_t"])
        else:
            resultDICT["reply_equipment_list"] = choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[抱石]要穿什麼":
        if "抱石" in args[0]:
            resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring_b"]
        elif "上攀" in args[0] or "先鋒" in args[0] or "速度" in args[0]:
            resultDICT["reply_equipment_list"] = "{0}{1}".format(args[0],defaultResponse["_equipment_bring_t"])
        else:
            resultDICT["reply_equipment_list"] = choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[抱石]需要[先]買好哪些[裝備]":
        if "抱石" in args[0]:
            resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring_b"]
        elif "上攀" in args[0] or "先鋒" in args[0] or "速度" in args[0]:
            resultDICT["reply_equipment_list"] = "{0}{1}".format(args[0],defaultResponse["_equipment_bring_t"])
        else:
            resultDICT["reply_equipment_list"] = choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[抱石]需要哪些[裝備]":
        if "抱石" in args[0]:
            resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring_b"]
        elif "上攀" in args[0] or "先鋒" in args[0] or "速度" in args[0]:
            resultDICT["reply_equipment_list"] = "{0}{1}".format(args[0],defaultResponse["_equipment_bring_t"])
        else:
            resultDICT["reply_equipment_list"] = choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[抱石]需要買哪些[裝備]":
        if "抱石" in args[0]:
            resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring_b"]
        elif "上攀" in args[0] or "先鋒" in args[0] or "速度" in args[0]:
            resultDICT["reply_equipment_list"] = "{0}{1}".format(args[0],defaultResponse["_equipment_bring_t"])
        else:
            resultDICT["reply_equipment_list"] = choice(defaultResponse["_not_rock_climbing"])

    if utterance == "哪些[裝備][一定]要買":
        resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring"]

    if utterance == "攀岩有[服裝][上]的[規定]嗎":
        resultDICT["reply_equipment_list"] = defaultResponse["_equipment_wear"]

    if utterance == "攀岩有什麼是要[先]買好的？":
        resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring"]

    if utterance == "攀岩要[先]買哪些[裝備]":
        resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring"]

    if utterance == "攀岩要帶什麼":
        resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring"]

    if utterance == "攀岩要準備什麼":
        resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring"]

    if utterance == "攀岩要準備多少[裝備]":
        resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring"]

    if utterance == "攀岩要穿什麼":
        resultDICT["reply_equipment_list"] = defaultResponse["_equipment_wear"]

    if utterance == "攀岩需要[先]買好哪些[裝備]":
        resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring"]

    if utterance == "攀岩需要哪些[裝備]":
        resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring"]

    if utterance == "攀岩需要買哪些[裝備]":
        resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring"]

    if utterance == "要買哪些[裝備]":
        resultDICT["reply_equipment_list"] = defaultResponse["_equipment_bring"]

    return resultDICT