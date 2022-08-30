#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for equipment_whereGet

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

DEBUG_equipment_whereGet = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_rocks":["岩石","岩點","手點","石頭","點"],"_shoes":["岩鞋","抱石鞋","鞋子","攀岩鞋","攀岩鞋子"],"_sides":["中部","北部","南部","東部","西部"],"_whatIs":["星光票"],"_climbing":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石","抱石攀岩","速度攀","速度攀登","攀登","運動攀登"],"_cityAlias":["區域","地區","城市","縣市","都市","地方"],"_gymsShort":["達文西","8a攀岩場","B-plus","Boulder Space","Camp 4","Corner","Dapro","K2","MegaSTONE","POGO","TheDepotCity","Up聯盟","Y17","double 8","double8","久淘","千手抱石","原岩","嗨翻","嘉義攀岩會館","圓石","圓石空間","宜蘭運動中心","小岩館","崩岩","抱石基地","攀吶","新竹紅石","水美iClimb","汐止抱石館","爬森","破舊二廠","破舊工廠","禾匠","紅石","艾思博","蕃薯藤","角岩館","風城"],"_peClothes":["單車褲","瑜珈褲","運動服","運動衣","運動褲","運動鞋","攀岩褲"],"_rockTypes":["crimp","edge","flat","horn","jug","pinch","pocket","sloper","volume"],"_climbingGym":["岩場","岩館","攀岩場","攀岩館","抱石館","上攀館"],"_taiwanAlias":["全台","全台各地","全臺","全臺各地","台灣","臺灣","全台灣"],"_clothesPants":["上衣","服裝","短袖","短袖上衣","短袖衣服","衣服","衣著","衣褲","長袖","長袖上衣","長袖衣服","單車褲","瑜珈褲","短褲","運動褲","長褲"],"_climbingEquip":["岩粉","岩點刷","攀岩刷","攀岩粉","攀岩粉袋","止滑粉","碳酸鎂粉","粉球","粉袋","裝","裝備","鎂粉","鎂粉球"],"_topRopingEquip":["吊帶","垂降手套","安全吊帶","安全扣","安全扣環","快扣","手套","確保器","確保手套","耐磨手套"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_equipment_whereGet:
        print("[equipment_whereGet] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[你]知道[可以]去哪買[岩粉]嗎":
        if args[2] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[2] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多可以上攀的岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[2] in userDefinedDICT["_shoes"] or args[2] in userDefinedDICT["_peClothes"]:
            resultDICT["reply_equipment_whereGet"] = '戶外休閒用品店、迪卡儂，或是運動類型網路商店都有賣哦'
        else:
            resultDICT["reply_equipment_whereGet"] = '這超出我能力範圍了'

    if utterance == "[你]知道[岩粉]哪裡租得到嗎":
        if args[1] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '一般岩館都有提供租借哦！'
        elif "手套" in args[1]:
            resultDICT["equipment_whereGet"] = '這應該租不太到'
        elif args[1] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '一般上攀岩館都租借得到哦！'
        else:
            resultDICT["equipment_whereGet"] = '這應該租不太到'

    if utterance == "[你]知道[岩粉]哪裡買得到嗎":
        if args[1] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[1] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多可以上攀的岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[1] in userDefinedDICT["_shoes"] or args[1] in userDefinedDICT["_peClothes"]:
            resultDICT["reply_equipment_whereGet"] = '戶外休閒用品店、迪卡儂，或是運動類型網路商店都有賣哦'
        else:
            resultDICT["reply_equipment_whereGet"] = '這超出我能力範圍了'

    if utterance == "[你]知道[岩粉]要去哪買嗎":
        if args[0] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多可以上攀的岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_peClothes"]:
            resultDICT["reply_equipment_whereGet"] = '戶外休閒用品店、迪卡儂，或是運動類型網路商店都有賣哦'
        else:
            resultDICT["reply_equipment_whereGet"] = '這超出我能力範圍了'

    if utterance == "[岩粉][可以]去哪買？":
        if args[0] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多可以上攀的岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_peClothes"]:
            resultDICT["reply_equipment_whereGet"] = '戶外休閒用品店、迪卡儂，或是運動類型網路商店都有賣哦'
        else:
            resultDICT["reply_equipment_whereGet"] = '這超出我能力範圍了'

    if utterance == "[岩粉]哪裡[可以]租得到？":
        if args[1] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '一般岩館都有提供租借哦！'
        elif "手套" in args[1]:
            resultDICT["equipment_whereGet"] = '這應該租不太到，要自己買'        
        elif args[1] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '一般上攀岩館都租借得到哦！'
        else:
            resultDICT["equipment_whereGet"] = '這應該租不太到'

    if utterance == "[岩粉]哪裡[可以]買得到？":
        if args[0] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多可以上攀的岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_peClothes"]:
            resultDICT["reply_equipment_whereGet"] = '戶外休閒用品店、迪卡儂，或是運動類型網路商店都有賣哦'
        else:
            resultDICT["reply_equipment_whereGet"] = '這超出我能力範圍了'

    if utterance == "[岩粉]哪裡買得到？":
        if args[0] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多可以上攀的岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_peClothes"]:
            resultDICT["reply_equipment_whereGet"] = '戶外休閒用品店、迪卡儂，或是運動類型網路商店都有賣哦'
        else:
            resultDICT["reply_equipment_whereGet"] = '這超出我能力範圍了'

    if utterance == "哪裡[可以]租[岩粉]":
        if args[1] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '大部分岩館都有提供租借哦！'
        elif "手套" in args[1]:
            resultDICT["equipment_whereGet"] = '這應該租不太到，要自己買'        
        elif args[1] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '大部分上攀岩館都租借得到哦！'
        else:
            resultDICT["equipment_whereGet"] = '這應該租不太到'

    if utterance == "哪裡[可以]買[岩粉]":
        if args[1] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[1] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多可以上攀的岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[1] in userDefinedDICT["_shoes"] or args[1] in userDefinedDICT["_peClothes"]:
            resultDICT["reply_equipment_whereGet"] = '戶外休閒用品店、迪卡儂，或是運動類型網路商店都有賣哦'
        else:
            resultDICT["reply_equipment_whereGet"] = '這超出我能力範圍了'

    if utterance == "哪裡[可以]買到[岩粉]":
        if args[1] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[1] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多可以上攀的岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[1] in userDefinedDICT["_shoes"] or args[1] in userDefinedDICT["_peClothes"]:
            resultDICT["reply_equipment_whereGet"] = '戶外休閒用品店、迪卡儂，或是運動類型網路商店都有賣哦'
        else:
            resultDICT["reply_equipment_whereGet"] = '這超出我能力範圍了'

    if utterance == "哪裡租得到[岩粉]":
        if args[0] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '一般岩館都有提供租借哦！'
        elif "手套" in args[1]:
            resultDICT["equipment_whereGet"] = '這應該租不太到，要自己買'
        elif args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '一般上攀岩館都租借得到哦！'
        else:
            resultDICT["equipment_whereGet"] = '這應該租不太到'

    if utterance == "哪裡買得到[岩粉]":
        if args[0] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_whereGet"] = '很多可以上攀的岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'
        elif args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_peClothes"]:
            resultDICT["reply_equipment_whereGet"] = '戶外休閒用品店、迪卡儂，或是運動類型網路商店都有賣哦'
        else:
            resultDICT["reply_equipment_whereGet"] = '這超出我能力範圍了'
    return resultDICT