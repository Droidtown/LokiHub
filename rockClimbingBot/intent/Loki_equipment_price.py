#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for equipment_price

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

DEBUG_equipment_price = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_rocks":["岩石","岩點","手點","石頭","點"],"_shoes":["岩鞋","抱石鞋","鞋子","攀岩鞋","攀岩鞋子"],"_sides":["中部","北部","南部","東部","西部"],"_whatIs":["星光票"],"_climbing":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石","抱石攀岩","速度攀","速度攀登","攀登","運動攀登"],"_cityAlias":["區域","地區","城市","縣市","都市","地方"],"_gymsShort":["達文西","8a攀岩場","B-plus","Boulder Space","Camp 4","Corner","Dapro","K2","MegaSTONE","POGO","TheDepotCity","Up聯盟","Y17","double 8","double8","久淘","千手抱石","原岩","嗨翻","嘉義攀岩會館","圓石","圓石空間","宜蘭運動中心","小岩館","崩岩","抱石基地","攀吶","新竹紅石","水美iClimb","汐止抱石館","爬森","破舊二廠","破舊工廠","禾匠","紅石","艾思博","蕃薯藤","角岩館","風城"],"_peClothes":["單車褲","瑜珈褲","運動服","運動衣","運動褲","運動鞋","攀岩褲"],"_rockTypes":["crimp","edge","flat","horn","jug","pinch","pocket","sloper","volume"],"_climbingGym":["岩場","岩館","攀岩場","攀岩館","抱石館","上攀館"],"_taiwanAlias":["全台","全台各地","全臺","全臺各地","台灣","臺灣","全台灣"],"_clothesPants":["上衣","服裝","短袖","短袖上衣","短袖衣服","衣服","衣著","衣褲","長袖","長袖上衣","長袖衣服","單車褲","瑜珈褲","短褲","運動褲","長褲"],"_climbingEquip":["岩粉","岩點刷","攀岩刷","攀岩粉","攀岩粉袋","止滑粉","碳酸鎂粉","粉球","粉袋","裝","裝備","鎂粉","鎂粉球"],"_topRopingEquip":["吊帶","垂降手套","安全吊帶","安全扣","安全扣環","快扣","手套","確保器","確保手套","耐磨手套"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_equipment_price:
        print("[equipment_price] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[岩鞋][大概]多少[錢]？":
        if "租" not in utterance:
            if args[0] in userDefinedDICT["_shoes"]:
                resultDICT["reply_price"] = "equipment"
                resultDICT["reply_equipment_price"] = args[0]+'價錢介於1000~5000不等，可依預算和偏好考量入手鞋款'
            elif args[0] in userDefinedDICT["_climbingEquip"]:
                resultDICT["reply_price"] = "equipment"
                resultDICT["reply_equipment_price"] = args[0]+'價錢大多低於1000，喜歡抱石可考慮入手哦'
            elif args[0] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["reply_price"] = "equipment"
                resultDICT["reply_equipment_price"] = args[0]+'的價位大約是800~2000左右，建議對上攀真的很有興趣再入手'
            else:
                resultDICT["reply_equipment_price"] = '這我不知道噎'
        else:
            if args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_climbingEquip"] or args[0] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["reply_price"] = "equipment"
                resultDICT["reply_equipment_price"] = "場館租借{}大多介於50-100之間哦".format(args[0])
            else:
                resultDICT["reply_equipment_price"] = "應該是沒有場館在租借{}哦".format(args[0])

    if utterance == "[岩鞋][很貴]嗎？":
        if "租" not in utterance:
            if args[0] in userDefinedDICT["_shoes"]:
                resultDICT["reply_price"] = "equipment"
                resultDICT["reply_equipment_price"] = args[0]+'價錢介於1000~5000不等，可依預算和偏好考量入手鞋款'
            elif args[0] in userDefinedDICT["_climbingEquip"]:
                resultDICT["reply_price"] = "equipment"
                resultDICT["reply_equipment_price"] = args[0]+'價錢大多低於1000，喜歡抱石可考慮入手哦'
            elif args[0] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["reply_price"] = "equipment"
                resultDICT["reply_equipment_price"] = args[0]+'的價位大約是800~2000左右，建議對上攀真的很有興趣再入手'
            else:
                resultDICT["reply_equipment_price"] = '這我不知道噎'
        else:
            if args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_climbingEquip"] or args[0] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["reply_equipment_price"] = "場館租借{}大多介於50-100之間哦".format(args[0])
            else:
                resultDICT["reply_equipment_price"] = "應該是沒有場館在租借{}哦".format(args[0])

    if utterance == "[岩鞋]多貴？":
        if "租" not in utterance:
            if args[0] in userDefinedDICT["_shoes"]:
                resultDICT["reply_equipment_price"] = args[0]+'價錢介於1000~5000不等，可依預算和偏好考量入手鞋款'
            elif args[0] in userDefinedDICT["_climbingEquip"]:
                resultDICT["reply_equipment_price"] = args[0]+'價錢大多低於1000，喜歡抱石可考慮入手哦'
            elif args[0] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["reply_equipment_price"] = args[0]+'的價位大約是800~2000左右，建議對上攀真的很有興趣再入手'
            else:
                resultDICT["reply_equipment_price"] = '這我不知道噎'
        else:
            if args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_climbingEquip"] or args[0] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["reply_equipment_price"] = "場館租借{}大多介於50-100之間哦".format(args[0])
            else:
                resultDICT["reply_equipment_price"] = "應該是沒有場館在租借{}哦".format(args[0])

    if utterance == "[岩鞋]要價多少？":
        if "租" not in utterance:
            if args[0] in userDefinedDICT["_shoes"]:
                resultDICT["reply_equipment_price"] = args[0]+'價錢介於1000~5000不等，可依預算和偏好考量入手鞋款'
            elif args[0] in userDefinedDICT["_climbingEquip"]:
                resultDICT["reply_equipment_price"] = args[0]+'價錢大多低於1000，喜歡抱石可考慮入手哦'
            elif args[0] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["reply_equipment_price"] = args[0]+'的價位大約是800~2000左右，建議對上攀真的很有興趣再入手'
            else:
                resultDICT["reply_equipment_price"] = '這我不知道噎'
        else:
            if args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_climbingEquip"] or args[0] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["reply_equipment_price"] = "場館租借{}大多介於50-100之間哦".format(args[0])
            else:
                resultDICT["reply_equipment_price"] = "應該是沒有場館在租借{}哦".format(args[0])

    if utterance == "[岩鞋]要多少[錢]？":
        if "租" not in utterance:
            if args[0] in userDefinedDICT["_shoes"]:
                resultDICT["reply_equipment_price"] = args[0]+'價錢介於1000~5000不等，可依預算和偏好考量入手鞋款'
            elif args[0] in userDefinedDICT["_climbingEquip"]:
                resultDICT["reply_equipment_price"] = args[0]+'價錢大多低於1000，喜歡抱石可考慮入手哦'
            elif args[0] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["reply_equipment_price"] = args[0]+'的價位大約是800~2000左右，建議對上攀真的很有興趣再入手'
            else:
                resultDICT["reply_equipment_price"] = '這我不知道噎'
        else:
            if args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_climbingEquip"] or args[0] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["reply_equipment_price"] = "場館租借{}大多介於50-100之間哦".format(args[0])
            else:
                resultDICT["reply_equipment_price"] = "應該是沒有場館在租借{}哦".format(args[0])

    if utterance == "多少[錢][可以]租到[岩鞋]":
        if args[2] in userDefinedDICT["_shoes"] or args[2] in userDefinedDICT["_climbingEquip"] or args[2] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_price"] = "場館租借{}大多介於50-100之間哦".format(args[2])
        else:
            resultDICT["reply_equipment_price"] = "應該是沒有場館在租借{}哦".format(args[2])

    if utterance == "多少[錢][能]買得到[岩鞋]？":
        if args[2] in userDefinedDICT["_shoes"]:
            resultDICT["reply_equipment_price"] = args[2]+'價錢介於1000~5000不等，可依預算和偏好考量入手鞋款'
        elif args[2] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_price"] = args[2]+'價錢大多低於1000，喜歡抱石可考慮入手哦'
        elif args[2] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_price"] = args[2]+'的價位大約是800~2000左右，建議對上攀真的很有興趣再入手'
        else:
            resultDICT["reply_equipment_price"] = '這我不知道噎'

    if utterance == "多少[錢]租得到[岩鞋]":
        if args[1] in userDefinedDICT["_shoes"] or args[1] in userDefinedDICT["_climbingEquip"] or args[2] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_price"] = "場館租借{}大多介於50-100之間哦".format(args[1])
        else:
            resultDICT["reply_equipment_price"] = "應該是沒有場館在租借{}哦".format(args[1])

    if utterance == "多少[錢]買得到[岩鞋]？":
        if args[1] in userDefinedDICT["_shoes"]:
            resultDICT["reply_equipment_price"] = args[1]+'價錢介於1000~5000不等，可依預算和偏好考量入手鞋款'
        elif args[1] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_price"] = args[1]+'價錢大多低於1000，喜歡抱石可考慮入手哦'
        elif args[1] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_price"] = args[1]+'的價位大約是800~2000左右，建議對上攀真的很有興趣再入手'
        else:
            resultDICT["reply_equipment_price"] = '這我不知道噎'

    if utterance == "租[岩鞋]要花多少":
        if args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_climbingEquip"] or args[2] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_price"] = "場館租借{}大多介於50-100之間哦".format(args[0])
        else:
            resultDICT["reply_equipment_price"] = "應該是沒有場館在租借{}哦".format(args[0])

    if utterance == "花多少[才]租得到[岩鞋]？":
        if args[1] in userDefinedDICT["_shoes"] or args[1] in userDefinedDICT["_climbingEquip"] or args[2] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_price"] = "場館租借{}大多介於50-100之間哦".format(args[1])
        else:
            resultDICT["reply_equipment_price"] = "應該是沒有場館在租借{}哦".format(args[1])

    if utterance == "花多少[才]買得到[岩鞋]？":
        if args[1] in userDefinedDICT["_shoes"]:
            resultDICT["reply_equipment_price"] = args[1]+'價錢介於1000~5000不等，可依預算和偏好考量入手鞋款'
        elif args[1] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_price"] = args[1]+'價錢大多低於1000，喜歡抱石可考慮入手哦'
        elif args[1] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_price"] = args[1]+'的價位大約是800~2000左右，建議對上攀真的很有興趣再入手'
        else:
            resultDICT["reply_equipment_price"] = '這我不知道噎'

    if utterance == "買[岩鞋]要花多少？":
        if args[0] in userDefinedDICT["_shoes"]:
            resultDICT["reply_equipment_price"] = args[0]+'價錢介於1000~5000不等，可依預算和偏好考量入手鞋款'
        elif args[0] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_price"] = args[0]+'價錢大多低於1000，喜歡抱石可考慮入手哦'
        elif args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_price"] = args[0]+'的價位大約是800~2000左右，建議對上攀真的很有興趣再入手'
        else:
            resultDICT["reply_equipment_price"] = '這我不知道噎'

    if utterance == "買[岩鞋]需要[花]到[四個]小朋友嗎？":
        # write your code here
        pass

    return resultDICT