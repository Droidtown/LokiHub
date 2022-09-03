#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for gym_city

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
from rockClimbingFunc import gymCountySet
from rockClimbingFunc import hasGymCounty
from rockClimbingFunc import getSideCounties
from rockClimbingFunc import getGymLocPh
from rockClimbingFunc import getBTScity
from rockClimbingFunc import getGymPrice
from rockClimbingFunc import containerToString
from rockClimbingFunc import priceToString
from rockClimbingFunc import getGymDistrict

DEBUG_gym_city = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_rocks":["岩石","岩點","手點","石頭","點"],"_shoes":["岩鞋","抱石鞋","鞋子","攀岩鞋","攀岩鞋子"],"_sides":["中部","北部","南部","東部","西部"],"_whatIs":["星光票"],"_climbing":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石","抱石攀岩","速度攀","速度攀登","攀登","運動攀登"],"_cityAlias":["區域","地區","城市","縣市","都市","地方"],"_gymsShort":["達文西","8a攀岩場","B-plus","Boulder Space","Camp 4","Corner","Dapro","K2","MegaSTONE","POGO","TheDepotCity","Up聯盟","Y17","double 8","double8","久淘","千手抱石","原岩","嗨翻","嘉義攀岩會館","圓石","圓石空間","宜蘭運動中心","小岩館","崩岩","抱石基地","攀吶","新竹紅石","水美iClimb","汐止抱石館","爬森","破舊二廠","破舊工廠","禾匠","紅石","艾思博","蕃薯藤","角岩館","風城"],"_peClothes":["單車褲","瑜珈褲","運動服","運動衣","運動褲","運動鞋","攀岩褲"],"_rockTypes":["crimp","edge","flat","horn","jug","pinch","pocket","sloper","volume"],"_climbingGym":["岩場","岩館","攀岩場","攀岩館","抱石館","上攀館"],"_taiwanAlias":["全台","全台各地","全臺","全臺各地","台灣","臺灣","全台灣"],"_clothesPants":["上衣","服裝","短袖","短袖上衣","短袖衣服","衣服","衣著","衣褲","長袖","長袖上衣","長袖衣服","單車褲","瑜珈褲","短褲","運動褲","長褲"],"_climbingEquip":["岩粉","岩點刷","攀岩刷","攀岩粉","攀岩粉袋","止滑粉","碳酸鎂粉","粉球","粉袋","裝","裝備","鎂粉","鎂粉球"],"_topRopingEquip":["吊帶","垂降手套","安全吊帶","安全扣","安全扣環","快扣","手套","確保器","確保手套","耐磨手套"]}

defaultResponse = json.load(open("data/defaultResponse.json",encoding="utf-8"))
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_gym_city:
        print("[gym_city] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[double 8]在哪個[縣市]":
        if args[0] in userDefinedDICT["_gymsShort"]:
            resultDICT["_gym_name"] = args[0]
            if args[1] in userDefinedDICT["_cityAlias"]: #get city
                cityDict = getGymLocPh(args[0], "c")
                tmp = ""
                for gym, loc in cityDict.items():
                    tmp += "{0}在{1}\n".format(gym, loc)
                resultDICT["reply_gym_location"] = tmp
            elif args[1] == "位置": #get address
                cityDict = getGymLocPh(args[0], "a")
                tmp = ""
                for gym, loc in cityDict.items():
                    tmp += "{0}在{1}\n".format(gym, loc)
                resultDICT["reply_gym_location"] = tmp
            else:
                resultDICT["reply_gym_location"] = choice(defaultResponse["_question_not_know"])
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_gym_unknown"])

    if utterance == "[double 8]在哪裡":
        if args[0] in userDefinedDICT["_gymsShort"]:
            resultDICT["_gym_name"] = args[0]
            cityDict = getGymLocPh(args[0], "a")
            tmp = ""
            for gym, loc in cityDict.items():
                tmp += "{0}在{1}\n".format(gym, loc)
            resultDICT["reply_gym_location"] = tmp
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_gym_unknown"])

    if utterance == "[中部]哪裡有[上攀][岩館]":
        if args[2] not in userDefinedDICT["_climbingGym"]:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if args[0] in userDefinedDICT["_taiwanAlias"]:
            countySet1 = gymCountySet()
            countySet2 = set()
            for county in countySet1:
                if hasGymCounty(county, args[1]):
                    countySet2.add(county)
            counties = containerToString(countySet2)
            resultDICT["reply_gym_location"] = "{0}的{1}{2}有{3}".format(args[0], args[1], args[2], counties)
        elif args[0] in userDefinedDICT["_sides"]:
            counties = getSideCounties(args[0])
            countySet2 = set()
            for county in counties:
                if hasGymCounty(county, args[1]):
                    countySet2.add(county)
            counties = containerToString(countySet2)
            resultDICT["reply_gym_location"] = "{0}的{1}{2}有{3}".format(args[0], args[1], args[2], counties)                        
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[可以]告訴[我][double 8][岩館]的[地址]嗎":
        if args[2] in userDefinedDICT["_gymsShort"]:
            resultDICT["_gym_name"] = args[2]
            if args[4] in ("地址","位置"): #address
                cityDict = getGymLocPh(args[2], "a")
                gymLoc = ""
                for gym, loc in cityDict.items():
                    gymLoc += "{0}地址:{1}\n".format(gym, loc)
                resultDICT["reply_gym_location"] = gymLoc
            elif "價" in args[4]: #price
                gymPriceDict = getGymPrice(args[2])
                gymPrice = priceToString(gymPriceDict)
                resultDICT["reply_gym_price"] = gymPrice
            elif "電話" in args[4]: #phone
                phoneDict = getGymLocPh(args[2], "p")
                gymPh = ""
                for gym, phone in phoneDict.items():
                    gymPh += "{0}電話:{1}\n".format(gym, phone)
                resultDICT["reply_gym_location"] = gymPh
            else:
                esultDICT["reply_gym_location"] = choice(defaultResponse["_question_not_know"])
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_gym_unknown"])
            
    if utterance == "[可以]告訴[我][double 8]的[地址]嗎":
        if args[2] in userDefinedDICT["_gymsShort"]:
            resultDICT["_gym_name"] = args[2]
            if args[3] in ("地址","位置"): #address
                cityDict = getGymLocPh(args[2], "a")
                gymLoc = ""
                for gym, loc in cityDict.items():
                    gymLoc += "{0}地址:{1}\n".format(gym, loc)
                resultDICT["reply_gym_location"] = gymLoc
            elif "價" in args[3]: #price
                gymPriceDict = getGymPrice(args[2])
                gymPrice = priceToString(gymPriceDict)
                resultDICT["reply_gym_price"] = gymPrice
            elif "電話" in args[3]: #phone
                phoneDict = getGymLocPh(args[2], "p")
                gymPh = ""
                for gym, phone in phoneDict.items():
                    gymPh += "{0}電話:{1}\n".format(gym, phone)
                resultDICT["reply_gym_location"] = gymPh
            else:
                esultDICT["reply_gym_location"] = choice(defaultResponse["_question_not_know"])
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_gym_unknown"])

    if utterance == "[可以]給[我][double 8][岩館]的[地址]嗎":
        if args[2] in userDefinedDICT["_gymsShort"]:
            resultDICT["_gym_name"] = args[2]
            if args[4] in ("地址","位置"): #address
                cityDict = getGymLocPh(args[2], "a")
                gymLoc = ""
                for gym, loc in cityDict.items():
                    gymLoc += "{0}地址:{1}\n".format(gym, loc)
                resultDICT["reply_gym_location"] = gymLoc
            elif "價" in args[4]: #price
                gymPriceDict = getGymPrice(args[2])
                gymPrice = priceToString(gymPriceDict)
                resultDICT["reply_gym_price"] = gymPrice
            elif "電話" in args[4]: #phone
                phoneDict = getGymLocPh(args[2], "p")
                gymPh = ""
                for gym, phone in phoneDict.items():
                    gymPh += "{0}電話:{1}\n".format(gym, phone)
                resultDICT["reply_gym_location"] = gymPh
            else:
                esultDICT["reply_gym_location"] = choice(defaultResponse["_question_not_know"])
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_gym_unknown"])

    if utterance == "[可以]給[我][double 8]的[地址]嗎":
        if args[2] in userDefinedDICT["_gymsShort"]:
            resultDICT["_gym_name"] = args[2]
            if args[3] in ("地址","位置"): #address
                cityDict = getGymLocPh(args[2], "a")
                gymLoc = ""
                for gym, loc in cityDict.items():
                    gymLoc += "{0}地址:{1}\n".format(gym, loc)
                resultDICT["reply_gym_location"] = gymLoc
            elif "價" in args[3]: #price
                gymPriceDict = getGymPrice(args[2])
                gymPrice = priceToString(gymPriceDict)
                resultDICT["reply_gym_price"] = gymPrice
            elif "電話" in args[3]: #phone
                phoneDict = getGymLocPh(args[2], "p")
                gymPh = ""
                for gym, phone in phoneDict.items():
                    gymPh += "{0}電話:{1}\n".format(gym, phone)
                resultDICT["reply_gym_location"] = gymPh
            else:
                esultDICT["reply_gym_location"] = choice(defaultResponse["_question_not_know"])
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_gym_unknown"])

    if utterance == "[台北]哪裡有[速度攀]": #區、市
        if args[1] not in userDefinedDICT["_climbing"] and args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        districtSet = getGymDistrict(args[0])
        if len(districtSet) > 0:
            district = containerToString(districtSet, args[1])
            resultDICT["reply_gym_location"] = "{0}有{1}的地區有{2}".format(args[0], args[1], district)
        else:
            resultDICT["reply_gym_location"] = "{0}沒有{1}".format(args[0], args[1])

    if utterance == "[台灣]哪些[縣市]有[岩館]呢":
        if args[2] not in userDefinedDICT["_climbingGym"]:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if args[0] in userDefinedDICT["_taiwanAlias"]:
            countySet1 = gymCountySet()
            countySet2 = set()
            for county in countySet1:
                if hasGymCounty(county, args[2]):
                    countySet2.add(county)
            counties = containerToString(countySet2)
            resultDICT["reply_gym_location"] = "{0}有{3}的{1}有{2}".format(args[0], args[1], counties, args[2])
        elif args[0] in userDefinedDICT["_sides"]:
            counties = getSideCounties(args[0])
            countySet2 = set()
            for county in counties:
                if hasGymCounty(county, args[2]):
                    countySet2.add(county)
            counties = containerToString(countySet2)
            resultDICT["reply_gym_location"] = "{0}有{3}的{1}有{2}".format(args[0], args[1], counties, args[2])
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[我]需要[新竹紅石]的[電話]":
        if args[1] in userDefinedDICT["_gymsShort"]:
            resultDICT["_gym_name"] = args[1]
            if args[2] in ("地址","位置"): #address
                cityDict = getGymLocPh(args[1], "a")
                gymLoc = ""
                for gym, loc in cityDict.items():
                    gymLoc += "{0}地址:{1}\n".format(gym, loc)
                resultDICT["reply_gym_location"] = gymLoc
            elif "價" in args[2]: #price
                gymPriceDict = getGymPrice(args[1])
                gymPrice = priceToString(gymPriceDict)
                resultDICT["reply_gym_price"] = gymPrice
            elif "電話" in args[2]: #phone
                phoneDict = getGymLocPh(args[1], "p")
                gymPh = ""
                for gym, phone in phoneDict.items():
                    gymPh += "{0}電話:{1}\n".format(gym, phone)
                resultDICT["reply_gym_location"] = gymPh
            else:
                esultDICT["reply_gym_location"] = choice(defaultResponse["_question_not_know"])
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_gym_unknown"])

    if utterance == "[可以]給[我][double 8]的[地址]嗎":
        if args[2] in userDefinedDICT["_gymsShort"]:
            resultDICT["_gym_name"] = args[2]
            if args[3] in ("地址","位置"): #address
                cityDict = getGymLocPh(args[2], "a")
                gymLoc = ""
                for gym, loc in cityDict.items():
                    gymLoc += "{0}地址:{1}\n".format(gym, loc)
                resultDICT["reply_gym_location"] = gymLoc
            elif "價" in args[3]: #price
                gymPriceDict = getGymPrice(args[2])
                gymPrice = priceToString(gymPriceDict)
                resultDICT["reply_gym_price"] = gymPrice
            elif "電話" in args[3]: #phone
                phoneDict = getGymLocPh(args[2], "p")
                gymPh = ""
                for gym, phone in phoneDict.items():
                    gymPh += "{0}電話:{1}\n".format(gym, phone)
                resultDICT["reply_gym_location"] = gymPh
            else:
                esultDICT["reply_gym_location"] = choice(defaultResponse["_question_not_know"])
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_gym_unknown"])

    if utterance == "[新竹紅石]的[地址]是？":
        if args[0] in userDefinedDICT["_gymsShort"]:
            resultDICT["_gym_name"] = args[0]
            if args[1] in ("地址","位置"): #address
                cityDict = getGymLocPh(args[0], "a")
                gymLoc = ""
                for gym, loc in cityDict.items():
                    gymLoc += "{0}地址:{1}\n".format(gym, loc)
                resultDICT["reply_gym_location"] = gymLoc
            elif "價" in args[1]: #price
                gymPriceDict = getGymPrice(args[0])
                gymPrice = priceToString(gymPriceDict)
                resultDICT["reply_gym_price"] = gymPrice
            elif "電話" in args[1]: #phone
                phoneDict = getGymLocPh(args[0], "p")
                gymPh = ""
                for gym, phone in phoneDict.items():
                    gymPh += "{0}電話:{1}\n".format(gym, phone)
                resultDICT["reply_gym_location"] = gymPh
            else:
                esultDICT["reply_gym_location"] = choice(defaultResponse["_question_not_know"])
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_gym_unknown"])

    if utterance == "[新竹紅石]的電話多少":
        if args[0] in userDefinedDICT["_gymsShort"]:
            resultDICT["_gym_name"] = args[0]
            phoneDict = getGymLocPh(args[0], "p")
            gymPh = ""
            for gym, phone in phoneDict.items():
                gymPh += "{0}電話:{1}\n".format(gym, phone)
            resultDICT["reply_gym_location"] = gymPh
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_gym_unknown"])

    if utterance == "[新竹紅石]的電話是幾號":
        if args[0] in userDefinedDICT["_gymsShort"]:
            resultDICT["_gym_name"] = args[0]
            phoneDict = getGymLocPh(args[0], "p")
            gymPh = ""
            for gym, phone in phoneDict.items():
                gymPh += "{0}電話:{1}\n".format(gym, phone)
            resultDICT["reply_gym_location"] = gymPh
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_gym_unknown"])

    if utterance == "[東部]哪裡有[速度攀]":
        if args[1] not in userDefinedDICT["_climbingGym"] and args[1] not in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if args[0] in userDefinedDICT["_taiwanAlias"]:
            countySet1 = gymCountySet()
            countySet2 = set()
            for county in countySet1:
                if hasGymCounty(county, args[1]):
                    countySet2.add(county)
            counties = containerToString(countySet2)
            resultDICT["_gym_name"] = "no_need"
            resultDICT["reply_gym_location"] = "{0}有{1}的縣市有{2}".format(args[0], args[1], counties)
        elif args[0] in userDefinedDICT["_sides"]:
            counties = getSideCounties(args[0])
            countySet2 = set()
            for county in counties:
                if hasGymCounty(county, args[1]):
                    countySet2.add(county)
            counties = containerToString(countySet2)
            resultDICT["_gym_name"] = "no_need"
            resultDICT["reply_gym_location"] = "{0}有{1}的縣市有{2}".format(args[0], args[1], counties)                        
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_not_taiwan_city"])        

    if utterance == "[紅石]聯絡[方式]":
        if args[0] in userDefinedDICT["_gymsShort"]:
            resultDICT["_gym_name"] = args[0]
            phoneDict = getGymLocPh(args[0], "p")
            gymPh = ""
            for gym, phone in phoneDict.items():
                gymPh += "{0}電話:{1}\n".format(gym, phone)
            resultDICT["reply_gym_location"] = gymPh
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_gym_unknown"])

    if utterance == "哪個[縣市]有[速度攀][場館]":
        if args[1] not in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if args[0] in userDefinedDICT["_cityAlias"]:
            citySet = getBTScity(args[1])
            cities = containerToString(citySet)
            resultDICT["reply_gym_location"] = "有{0}的{1}有{2}".format(args[1], args[0], cities)
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_no_meaning"])

    if utterance == "哪裡有[速度攀][場館]":
        if args[0] not in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        citySet = getBTScity(args[0])
        cities = containerToString(citySet)
        resultDICT["reply_gym_location"] = "有{0}的地區有{1}".format(args[0], cities)

    if utterance == "[紅石]資訊":
        if args[0] in userDefinedDICT["_gymsShort"]:
            resultDICT["_gym_name"] = args[0]
            phoneDict = getGymLocPh(args[0], "pa")
            gymInfo = ""
            for gym, info in phoneDict.items():
                gymInfo += "{0}\n電話:{1}\n地址:{2}\n".format(gym, info[0], info[1])
            resultDICT["reply_gym_location"] = gymInfo
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_gym_unknown"])

    if utterance == "[紅石]電話":
        if args[0] in userDefinedDICT["_gymsShort"]:
            resultDICT["_gym_name"] = args[0]
            phoneDict = getGymLocPh(args[0], "p")
            gymPh = ""
            for gym, phone in phoneDict.items():
                gymPh += "{0}電話:{1}\n".format(gym, phone)
            resultDICT["reply_gym_location"] = gymPh
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_gym_unknown"])

    if utterance == "[紅石]電話號碼":
        if args[0] in userDefinedDICT["_gymsShort"]:
            resultDICT["_gym_name"] = args[0]
            phoneDict = getGymLocPh(args[0], "p")
            gymPh = ""
            for gym, phone in phoneDict.items():
                gymPh += "{0}電話:{1}\n".format(gym, phone)
            resultDICT["reply_gym_location"] = gymPh
        else:
            resultDICT["reply_gym_location"] = choice(defaultResponse["_gym_unknown"])

    return resultDICT