#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for equipment_yesNo

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

DEBUG_equipment_yesNo = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_rocks":["岩石","岩點","手點","石頭","點"],"_shoes":["岩鞋","抱石鞋","鞋子","攀岩鞋","攀岩鞋子"],"_sides":["中部","北部","南部","東部","西部"],"_whatIs":["星光票"],"_climbing":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石","抱石攀岩","速度攀","速度攀登","攀登","運動攀登"],"_cityAlias":["區域","地區","城市","縣市","都市","地方"],"_gymsShort":["達文西","8a攀岩場","B-plus","Boulder Space","Camp 4","Corner","Dapro","K2","MegaSTONE","POGO","TheDepotCity","Up聯盟","Y17","double 8","double8","久淘","千手抱石","原岩","嗨翻","嘉義攀岩會館","圓石","圓石空間","宜蘭運動中心","小岩館","崩岩","抱石基地","攀吶","新竹紅石","水美","iClimb","汐止抱石館","爬森","破舊二廠","破舊工廠","禾匠","紅石","艾思博","蕃薯藤","角岩館","風城","紅石攀岩館","RedRock","The Little Rock","Camp 4攀岩館","CORNER Bouldering Gym","角·攀岩館","內湖運動中心攀岩館","內湖運動中心","光合作用","Xizhi Bouldering Gym","市民抱石攀岩館","奇岩攀岩館","奇岩","岩究所","原岩攀岩館","T-UP","永和攀岩場","趣攀岩","文山攀岩館","POGO攀岩館","WUSA","WUSA攀岩館","Passion climbing","爬森攀岩館","蕃薯藤攀岩場","水美攀岩館","桃園國民運動中心","桃園國民運動中心攀岩館","iClimb風城","iClimb風城攀岩館","RedRock紅石攀岩","B-plus攀岩館","The depot city","攀吶攀岩館","Dapro indoor climbing","Dapro室內攀岩場","bouldering gym","Shabby Factory","嗨翻綜合體能館","圓石空間","圓石空間攀岩場","K2攀岩休閒館","艾思博攀岩俱樂部","禾匠體驗學習攀岩場","崩岩館站前店","崩岩館民治店","久淘抱石館","宜蘭運動中心攀岩館","8a攀岩場","嘉義市國民運動中心","Mega","RedRock紅石攀岩館-士林店","小岩館The Little Rock-天母店","小岩館The Little Rock-內湖店","Camp 4攀岩館-北投運動中心館","Camp 4攀岩館-萬華運動中心館","CORNER Bouldering Gym角·攀岩館","汐止抱石館Xizhi Bouldering Gym","市民抱石攀岩館","奇岩攀岩館 Kirin Climbing Gym","double 8 岩究所","double 8-Y17岩究所","原岩攀岩館-南港店 T-UP Climbing Gym-n.a.ngang","原岩攀岩館-南港店","原岩攀岩館-萬華店","原岩攀岩館-中和店","永和攀岩場 (趣攀岩)","永和攀岩場 (趣攀岩) TitoRock-Climbing","Up聯盟 文山攀岩館","MegaSTONE Climbing Gym","POGO 攀岩館","WUSA攀岩館-新莊館","WUSA攀岩館-三重館","Passion climbing 爬森攀岩館","原岩攀岩館-楊梅店","原岩攀岩館-A19店","水美攀岩館","pogo","TheDepotCityBoulderingGym","Dapro indoor climbing 室內攀岩場","破舊二廠 bouldering gym","破舊工廠 Shabby Factory","Boulder Space圓石空間攀岩場","崩岩館站前店-本館","崩岩館民治店-教學館","嘉義市國民運動中心8a攀岩場"],"_peClothes":["單車褲","瑜珈褲","運動服","運動衣","運動褲","運動鞋","攀岩褲"],"_rockTypes":["crimp","edge","flat","horn","jug","pinch","pocket","sloper","volume"],"_climbingGym":["岩場","岩館","攀岩場","攀岩館","抱石館","上攀館"],"_taiwanAlias":["全台","全台各地","全臺","全臺各地","台灣","臺灣","全台灣"],"_clothesPants":["上衣","服裝","短袖","短袖上衣","短袖衣服","衣服","衣著","衣褲","長袖","長袖上衣","長袖衣服","單車褲","瑜珈褲","短褲","運動褲","長褲"],"_climbingEquip":["岩粉","岩點刷","攀岩刷","攀岩粉","攀岩粉袋","止滑粉","碳酸鎂粉","粉球","粉袋","裝","裝備","鎂粉","鎂粉球"],"_topRopingEquip":["吊帶","垂降手套","安全吊帶","安全扣","安全扣環","快扣","手套","確保器","確保手套","耐磨手套"]}

defaultResponse = json.load(open("data/defaultResponse.json",encoding="utf-8"))
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_equipment_yesNo:
        print("[equipment_yesNo] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[上攀][裝備]會不[會]很難買？":
        if args[0] in userDefinedDICT["_climbing"]:
            resultDICT["reply_equipment_YesNo"] = "不會"
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[可以]不買[裝備]嗎":
        resultDICT["reply_equipment_YesNo"] = defaultResponse["_equipment_bring"]

    if utterance == "[可以]穿[一般][運動鞋]去[抱石]嗎":
        if args[3] in userDefinedDICT["_climbing"]:
            if args[2] not in userDefinedDICT['_clothesPants'] and args[2] not in userDefinedDICT['_shoes'] and args[2] not in userDefinedDICT['_peClothes']:
                resultDICT["reply_equipment_YesNo"] = '最好不要，這樣會提高受傷機率'
            elif args[2] == "運動鞋":
                resultDICT["reply_equipment_YesNo"] = "最好是穿岩鞋攀岩比較安全哦！"
            else:
                resultDICT["reply_equipment_YesNo"] = '可以！穿{0}{1}當然沒問題'.format(args[2], args[3])
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[可以]穿[一般][運動鞋]去攀岩嗎":
        if args[2] not in userDefinedDICT['_clothesPants'] and args[2] not in userDefinedDICT['_shoes'] and args[2] not in userDefinedDICT['_peClothes']:
            resultDICT["reply_equipment_YesNo"] = '最好不要，這樣會提高受傷機率'
        elif args[2] == "運動鞋":
            resultDICT["reply_equipment_YesNo"] = "最好是穿岩鞋攀岩比較安全哦！"        
        else:
            resultDICT["reply_equipment_YesNo"] = '可以！穿{0}攀岩當然沒問題'.format(args[2])

    if utterance == "[可以]穿[牛仔褲][抱石]嗎？":
        if args[2] in userDefinedDICT["_climbing"]:
            if args[1] not in userDefinedDICT['_clothesPants'] and args[1] not in userDefinedDICT['_shoes'] and args[1] not in userDefinedDICT['_peClothes']:
                resultDICT["reply_equipment_YesNo"] = '最好不要，這樣會提高受傷機率'
            else:
                resultDICT["reply_equipment_YesNo"] = '可以！穿{0}{1}當然沒問題'.format(args[1], args[2])
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[可以]穿[牛仔褲]攀岩嗎？":
        if args[1] not in userDefinedDICT['_clothesPants'] and args[1] not in userDefinedDICT['_shoes'] and args[1] not in userDefinedDICT['_peClothes']:
            resultDICT["reply_equipment_YesNo"] = '最好不要，這樣會提高受傷機率'
        else:
            resultDICT["reply_equipment_YesNo"] = '可以！穿{0}{1}當然沒問題'.format(args[1], args[2])

    if utterance == "[可以]穿[運動鞋]嗎":
        if args[1] == "運動鞋":
            resultDICT["reply_equipment_YesNo"] = "最好是穿岩鞋攀岩比較安全哦！"
        elif args[1] in userDefinedDICT['_clothesPants'] and args[1] in userDefinedDICT['_shoes'] and args[1] in userDefinedDICT['_peClothes']:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
        else:
            resultDICT["reply_equipment_YesNo"] = '最好不要，這樣會提高受傷機率'

    if utterance == "[安全吊帶]租得到嘛":
        if "手套" in args[0]:
            resultDICT["reply_equipment_YesNo"] = "不行欸"
        elif args[0] in userDefinedDICT["_shoes"] or "岩粉" in args[0] or args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_YesNo"] = "通常可以"
        else:
            resultDICT["reply_equipment_YesNo"] = "通常不行"

    if utterance == "[安全吊帶]買得到嘛":
        if args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_climbingEquip"] or args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Not_sure"])

    if utterance == "[岩粉][必須]買嗎":
        if args[0] in userDefinedDICT["_climbingEquip"] or args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_YesNo"] = defaultResponse["_equipment_bring"]
        elif args[0] in userDefinedDICT["_shoes"]:
            resultDICT["reply_equipment_YesNo"] = defaultResponse["_equipment_wear"]
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_No_need"])

    if utterance == "[岩粉]有需要買嗎":
        if args[0] in userDefinedDICT["_climbingEquip"] or args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_YesNo"] = defaultResponse["_equipment_bring"]
        elif args[0] in userDefinedDICT["_shoes"]:
            resultDICT["reply_equipment_YesNo"] = defaultResponse["_equipment_wear"]
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_No_need"])

    if utterance == "[岩鞋][岩館]租得到嗎":
        if args[1] in userDefinedDICT["_climbingGym"]:
            if args[0] in userDefinedDICT["_shoes"] or "岩粉" in args[0] or args[0] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["reply_equipment_YesNo"] = "通常可以"
            else:
                resultDICT["reply_equipment_YesNo"] = "通常不行"
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Not_sure"])

    if utterance == "[岩鞋]在[岩館]買得到嗎":
        if args[1] in userDefinedDICT["_climbingGym"]:
            if args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_climbingEquip"] or args[0] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["reply_equipment_YesNo"] = "有些會賣{}，有些不會，這我不太確定耶".format(args[0])
            else:
                resultDICT["reply_equipment_YesNo"] = "通常不會"
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Not_sure"])

    if utterance == "[岩館][可以]買[鞋子]嗎":
        if args[0] in userDefinedDICT["_climbingGym"]:
            if args[2] in userDefinedDICT["_shoes"] or args[2] in userDefinedDICT["_climbingEquip"] or args[2] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["reply_equipment_YesNo"] = "有些會賣{}，有些不會，這我不太確定耶".format(args[2])
            else:
                resultDICT["reply_equipment_YesNo"] = "應該不太行"
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Not_sure"])

    if utterance == "[岩館]買得到[鞋子]嗎":
        if args[0] in userDefinedDICT["_climbingGym"]:
            if args[1] in userDefinedDICT["_shoes"] or args[1] in userDefinedDICT["_climbingEquip"] or args[1] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["reply_equipment_YesNo"] = "有些會賣{}，有些不會，這我不太確定耶".format(args[1])
            else:
                resultDICT["reply_equipment_YesNo"] = "應該不太行"
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Not_sure"])

    if utterance == "[必須]買[岩粉]嗎":
        resultDICT["reply_equipment_YesNo"] = defaultResponse["_equipment_bring"]

    if utterance == "[抱石][一定]要穿[運動服]嗎":
        if args[0] in userDefinedDICT["_climbing"]:
            if args[2] in userDefinedDICT["_clothesPants"] or args[2] in userDefinedDICT["_shoes"] or args[2] in userDefinedDICT["_peClothes"]:
                resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Yes_yes"])
            else:
                resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_No_need"])
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[抱石][可以]穿[短袖]嗎？":
        if args[0] in userDefinedDICT["_climbing"]:
            if args[2] in userDefinedDICT["_clothesPants"] or args[2] in userDefinedDICT["_shoes"] or args[2] in userDefinedDICT["_peClothes"]:
                resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
            else:
                resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_No_not"])
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[抱石]租得到[鞋子]嗎":
        if args[0] in userDefinedDICT["_climbing"] or args[0] in userDefinedDICT["_climbingGym"]:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[抱石]要買[鞋子]嗎":
        if args[0] in userDefinedDICT["_climbing"]:
            resultDICT["reply_equipment_YesNo"] = defaultResponse["_equipment_bring"]
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[抱石]需要穿[運動褲]嗎":
        if args[0] not in userDefinedDICT["_climbing"] or args[0] not in userDefinedDICT["_climbingGym"]:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if args[1] in userDefinedDICT["_clothesPants"] or args[1] in userDefinedDICT["_shoes"] or args[1] in userDefinedDICT["_peClothes"]:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Yes_need"])
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_No_need"])

    if utterance == "[新手]有需要買[裝備]嗎":
        resultDICT["reply_equipment_YesNo"] = defaultResponse["_equipment_bring"]

    if utterance == "[衣著]有限制嗎？":
        if args[0] in userDefinedDICT["_clothesPants"]:
            resultDICT["reply_equipment_YesNo"] = defaultResponse["_equipment_wear"]
        else:
            resultDICT["reply_equipment_YesNo"] = "應該沒有"

    if utterance == "去[岩館]要帶[岩粉]嗎":
        if args[0] in userDefinedDICT["_climbingGym"] or args[0] in userDefinedDICT["_climbing"]:
            if args[1] in userDefinedDICT["_climbingEquip"] or args[1] in userDefinedDICT["_shoes"] or args[1] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Yes_need"])
            else:
                resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_No_need"])
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])

    if utterance == "攀岩[一定]要穿[運動服]嗎":
        resultDICT["reply_equipment_YesNo"] = "攀岩{}".format(defaultResponse["_equipment_wear"])

    if utterance == "攀岩[可以]穿[短袖]嗎？":
        if args[1] in userDefinedDICT["_clothesPants"] or args[1] in userDefinedDICT["_shoes"]:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_No_not"])

    if utterance == "攀岩[裝備]會不[會]很難買？":
        resultDICT["reply_equipment_YesNo"] = '不會。很多岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'

    if utterance == "攀岩租得到[鞋子]嗎":
        if args[0] in userDefinedDICT["_peClothes"] or args[0] in userDefinedDICT["_shoes"] or args[0] == "裝備":
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_No_not"])        

    if utterance == "攀岩要買[鞋子]嗎":
        resultDICT["reply_equipment_YesNo"] = defaultResponse["_equipment_bring"]

    if utterance == "攀岩需要穿[運動褲]嗎":
        if args[0] in userDefinedDICT["_peClothes"] or args[0] == "岩鞋" or args[0] == "裝備":
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Yes_need"])
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_No_need"])

    if utterance == "有dress code嗎？":
        resultDICT["reply_equipment_YesNo"] = defaultResponse["_equipment_wear"]

    if utterance == "有規定要穿什麼嗎":
        resultDICT["reply_equipment_YesNo"] = defaultResponse["_equipment_wear"]

    if utterance == "穿[短袖][可以][抱石]嗎":
        if args[2] in userDefinedDICT["_climbing"]:
            if args[0] in userDefinedDICT["_clothesPants"] or args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_peClothes"]:
                resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
            else:
                resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_No_not"])
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])

    if utterance == "穿[短袖][可以]去攀岩嗎":
        if args[0] in userDefinedDICT["_clothesPants"] or args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_peClothes"]:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_No_not"])

    if utterance == "穿[短袖][可以]攀岩嗎":
        if args[0] in userDefinedDICT["_clothesPants"] or args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_peClothes"]:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_No_not"])

    if utterance == "要帶[岩粉]嗎":
        if args[0] in userDefinedDICT["_clothesPants"] or args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_peClothes"] or args[0] in userDefinedDICT["_climbingEquip"] or args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["reply_equipment_YesNo"] = "{} 帶著比較好".format(random.choice(defaultResponse["_Yes_can"]))
        else:
            resultDICT["reply_equipment_YesNo"] = random.choice(defaultResponse["_No_need"])

    return resultDICT