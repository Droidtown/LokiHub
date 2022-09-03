#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for gym_name

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
import pandas as pd
from rockClimbingFunc import getBTSGym
from rockClimbingFunc import getLocBTSGym
from rockClimbingFunc import gymCountySet
from rockClimbingFunc import getSideCounties
from rockClimbingFunc import containerToString
from rockClimbingFunc import checkLocation
from rockClimbingFunc import getBTSGym

DEBUG_gym_name = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_rocks":["岩石","岩點","手點","石頭","點"],"_shoes":["岩鞋","抱石鞋","鞋子","攀岩鞋","攀岩鞋子"],"_sides":["中部","北部","南部","東部","西部"],"_whatIs":["星光票"],"_climbing":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石","抱石攀岩","速度攀","速度攀登","攀登","運動攀登"],"_cityAlias":["區域","地區","城市","縣市","都市","地方"],"_gymsShort":["達文西","8a攀岩場","B-plus","Boulder Space","Camp 4","Corner","Dapro","K2","MegaSTONE","POGO","TheDepotCity","Up聯盟","Y17","double 8","double8","久淘","千手抱石","原岩","嗨翻","嘉義攀岩會館","圓石","圓石空間","宜蘭運動中心","小岩館","崩岩","抱石基地","攀吶","新竹紅石","水美iClimb","汐止抱石館","爬森","破舊二廠","破舊工廠","禾匠","紅石","艾思博","蕃薯藤","角岩館","風城"],"_peClothes":["單車褲","瑜珈褲","運動服","運動衣","運動褲","運動鞋","攀岩褲"],"_rockTypes":["crimp","edge","flat","horn","jug","pinch","pocket","sloper","volume"],"_climbingGym":["岩場","岩館","攀岩場","攀岩館","抱石館","上攀館"],"_taiwanAlias":["全台","全台各地","全臺","全臺各地","台灣","臺灣","全台灣"],"_clothesPants":["上衣","服裝","短袖","短袖上衣","短袖衣服","衣服","衣著","衣褲","長袖","長袖上衣","長袖衣服","單車褲","瑜珈褲","短褲","運動褲","長褲"],"_climbingEquip":["岩粉","岩點刷","攀岩刷","攀岩粉","攀岩粉袋","止滑粉","碳酸鎂粉","粉球","粉袋","裝","裝備","鎂粉","鎂粉球"],"_topRopingEquip":["吊帶","垂降手套","安全吊帶","安全扣","安全扣環","快扣","手套","確保器","確保手套","耐磨手套"]}

gymsInfo = pd.read_csv('data/climbingGym.csv', encoding = 'utf-8')
extendedDICT = {"_taiwanCities":["雲林","嘉義","台南","高雄","屏東","花蓮","台東","基隆","台北","桃園","新竹","宜蘭","新北","苗栗","台中","彰化","南投","蘭嶼","綠島","金門","馬祖","龜山島","離島"],"_midTW":["苗栗","台中","彰化","南投"],"_eastTW":["花蓮","台東"],"_northTW":["基隆","台北","桃園","新竹","宜蘭","新北"],"_southTW":["雲林","嘉義","台南","高雄","屏東"],"_islandsTW":["離島","金門","馬祖","澎湖","龜山島"]}
defaultResponse = json.load(open("data/defaultResponse.json",encoding="utf-8"))
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_gym_name:
        print("[gym_name] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[中部][上攀][可以]去哪":
        if args[1] not in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if args[0] in userDefinedDICT["_sides"]:
            resultDICT["_person_loc"] = args[0]
            counties = getSideCounties(args[0])
            selectedGyms = set()
            for county in counties:
                selectedGyms.update(getLocBTSGym(county, args[1]))
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}岩館有{2}".format(args[0], args[1], gymsNames)
        elif args[0] in userDefinedDICT["_taiwanAlias"]:
            selectedGyms = getBTSGym(args[1])
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}岩館有{2}".format(args[0], args[1], gymsNames)
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[中部][上攀][可以]去哪裡":
        if args[1] not in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if args[0] in userDefinedDICT["_sides"]:
            resultDICT["_person_loc"] = args[0]
            counties = getSideCounties(args[0])
            selectedGyms = set()
            for county in counties:
                selectedGyms.update(getLocBTSGym(county, args[1]))
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}岩館有{2}".format(args[0], args[1], gymsNames)
        elif args[0] in userDefinedDICT["_taiwanAlias"]:
            selectedGyms = getBTSGym(args[1])
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}岩館有{2}".format(args[0], args[1], gymsNames)
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[中部][岩館]有哪些":
        if args[1] not in userDefinedDICT["_climbingGym"] or args[1] not in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if args[0] in userDefinedDICT["_sides"]:
            resultDICT["_person_loc"] = args[0]
            counties = getSideCounties(args[0])
            selectedGyms = set()
            for county in counties:
                selectedGyms.update(getLocBTSGym(county, args[1]))
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}有{2}".format(args[0], args[1], gymsNames)
        elif args[0] in userDefinedDICT["_taiwanAlias"]:
            selectedGyms = getBTSGym(args[1])
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}有{2}".format(args[0], args[1], gymsNames)
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[台中][上攀][可以]去哪裡":
        if args[1] not in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if checkLocation(args[0]):
            resultDICT["_person_loc"] = args[0]
            selectedGyms = getLocBTSGym(resultDICT["_person_loc"], args[1])
            gymsNames = containerToString(selectedGyms)
            if len(selectedGyms) != 0:
                resultDICT["reply_gym_name"] = "{0}的{1}岩館有{2}".format(args[0], args[1], gymsNames)
            else:
                resultDICT["reply_gym_name"] = "{0}沒有{1}岩館哦！".format(arg[0],args[1])
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[台中][岩館]有哪些":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if checkLocation(args[0]):
            resultDICT["_person_loc"] = args[0]
            selectedGyms = getLocBTSGym(resultDICT["_person_loc"], args[1])
            gymsNames = containerToString(selectedGyms)
            if len(selectedGyms) != 0:
                resultDICT["reply_gym_name"] = "{0}的{1}岩館有{2}".format(args[0], args[1], gymsNames)
            else:
                resultDICT["reply_gym_name"] = "{0}沒有{1}岩館哦！".format(arg[0],args[1])
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[台中]攀岩[可以]去哪裡":
        if checkLocation(args[0]):
            resultDICT["_person_loc"] = args[0]
            selectedGyms = getLocBTSGym(resultDICT["_person_loc"], "")
            gymsNames = containerToString(selectedGyms)
            if len(selectedGyms) != 0:
                resultDICT["reply_gym_name"] = "{0}的岩館有{1}".format(args[0], gymsNames)
            else:
                resultDICT["reply_gym_name"] = "{0}沒有岩館哦！".format(arg[0])
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])
        
    if utterance == "[台中]有哪些[上攀][岩館]":
        if args[2] not in userDefinedDICT["_climbingGym"] or args[1] not in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if checkLocation(args[0]):
            resultDICT["_person_loc"] = args[0]
            selectedGyms = getLocBTSGym(resultDICT["_person_loc"], args[1])
            gymsNames = containerToString(selectedGyms)
            if len(selectedGyms) != 0:
                resultDICT["reply_gym_name"] = "{0}的{1}岩館有{2}".format(args[0], args[1], gymsNames)
            else:
                resultDICT["reply_gym_name"] = "{0}沒有{1}岩館哦！".format(arg[0],args[1])
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[台中]有哪些[岩館]":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if checkLocation(args[0]):
            resultDICT["_person_loc"] = args[0]
            selectedGyms = getLocBTSGym(resultDICT["_person_loc"], args[1])
            gymsNames = containerToString(selectedGyms)
            if len(selectedGyms) != 0:
                resultDICT["reply_gym_name"] = "{0}的{1}岩館有{2}".format(args[0], args[1], gymsNames)
            else:
                resultDICT["reply_gym_name"] = "{0}沒有{1}岩館哦！".format(arg[0],args[1])
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[台北][有名]的[岩館]":
        if args[2] not in userDefinedDICT["_climbingGym"]:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if checkLocation(args[0]):
            resultDICT["_person_loc"] = args[0]
            selectedGyms = getLocBTSGym(resultDICT["_person_loc"], args[2])
            gymsNames = containerToString(selectedGyms)
            if len(selectedGyms) != 0:
                resultDICT["reply_gym_name"] = "{0}的{1}有{2}".format(args[0], args[2], gymsNames)
            else:
                resultDICT["reply_gym_name"] = "{0}沒有{1}哦！".format(arg[0],args[2])
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[台北]哪些[岩館][可以][抱石]":
        if args[3] not in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if checkLocation(args[0]):
            resultDICT["_person_loc"] = args[0]
            selectedGyms = getLocBTSGym(resultDICT["_person_loc"], args[3])
            gymsNames = containerToString(selectedGyms)
            if len(selectedGyms) != 0:
                resultDICT["reply_gym_name"] = "{0}的{1}岩館有{2}".format(args[0], args[3], gymsNames)
            else:
                resultDICT["reply_gym_name"] = "{0}沒有可以{1}的岩館哦！".format(arg[0],args[3])
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[台北]哪裡[可以][抱石]":
        if args[2] not in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if checkLocation(args[0]):
            resultDICT["_person_loc"] = args[0]
            selectedGyms = getLocBTSGym(resultDICT["_person_loc"], args[2])
            gymsNames = containerToString(selectedGyms)
            if len(selectedGyms) != 0:
                resultDICT["reply_gym_name"] = "{0}的{1}岩館有{2}".format(args[0], args[2], gymsNames)
            else:
                resultDICT["reply_gym_name"] = "{0}沒有可以{1}的岩館哦！".format(arg[0],args[2])
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[台北]哪裡[可以]攀岩":
        if checkLocation(args[0]):
            resultDICT["_person_loc"] = args[0]
            selectedGyms = getLocBTSGym(resultDICT["_person_loc"], "")
            gymsNames = containerToString(selectedGyms)
            if len(selectedGyms) != 0:
                resultDICT["reply_gym_name"] = "{0}的岩館有{1}".format(args[0], gymsNames)
            else:
                resultDICT["reply_gym_name"] = "{0}沒有岩館哦！".format(arg[0])
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[東部][有名]的[岩館]":
        if args[2] not in userDefinedDICT["_climbingGym"] or args[2] not in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if args[0] in userDefinedDICT["_sides"]:
            resultDICT["_person_loc"] = args[0]
            counties = getSideCounties(args[0])
            selectedGyms = set()
            for county in counties:
                selectedGyms.update(getLocBTSGym(county, args[2]))
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}有{2}".format(args[0], args[2], gymsNames)
        elif args[0] in userDefinedDICT["_taiwanAlias"]:
            selectedGyms = getBTSGym(args[2])
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}有{2}".format(args[0], args[2], gymsNames)
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[東部]哪些[岩館][可以][抱石]":
        if args[3] not in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if args[0] in userDefinedDICT["_sides"]:
            resultDICT["_person_loc"] = args[0]
            counties = getSideCounties(args[0])
            selectedGyms = set()
            for county in counties:
                selectedGyms.update(getLocBTSGym(county, args[3]))
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}岩館有{2}".format(args[0], args[3], gymsNames)
        elif args[0] in userDefinedDICT["_taiwanAlias"]:
            selectedGyms = getBTSGym(args[3])
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}岩館有{2}".format(args[0], args[3], gymsNames)
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[東部]有哪些[上攀][岩館]":
        if args[2] not in userDefinedDICT["_climbingGym"] or args[1] not in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if args[0] in userDefinedDICT["_sides"]:
            resultDICT["_person_loc"] = args[0]
            counties = getSideCounties(args[0])
            selectedGyms = set()
            for county in counties:
                selectedGyms.update(getLocBTSGym(county, args[1]))
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}岩館有{2}".format(args[0], args[1], gymsNames)
        elif args[0] in userDefinedDICT["_taiwanAlias"]:
            selectedGyms = getBTSGym(args[1])
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}岩館有{2}".format(args[0], args[1], gymsNames)
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[東部]有哪些[岩館]":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if args[0] in userDefinedDICT["_sides"]:
            resultDICT["_person_loc"] = args[0]
            counties = getSideCounties(args[0])
            selectedGyms = set()
            for county in counties:
                selectedGyms.update(getLocBTSGym(county, args[1]))
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}有{2}".format(args[0], args[1], gymsNames)
        elif args[0] in userDefinedDICT["_taiwanAlias"]:
            selectedGyms = getBTSGym(args[1])
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}有{2}".format(args[0], args[1], gymsNames)
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[臺中][上攀][可以]去哪":
        if args[1] not in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if checkLocation(args[0]):
            resultDICT["_person_loc"] = args[0]
            selectedGyms = getLocBTSGym(resultDICT["_person_loc"], args[1])
            gymsNames = containerToString(selectedGyms)
            if len(selectedGyms) > 0:
                resultDICT["reply_gym_name"] = "{0}的{1}岩館有{2}".format(args[0], args[1], gymsNames)
            else:
                resultDICT["reply_gym_name"] = "{0}沒有可以{1}的岩館哦！".format(args[0],args[1])
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "哪幾[間][岩館]有[速度攀]":
        if args[2] not in userDefinedDICT["_climbing"]:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        selectedGyms = getBTSGym(args[2])
        gymsNames = containerToString(selectedGyms)
        resultDICT["reply_gym_name"] = "有{0}的岩館有{1}".format(args[2], gymsNames)

    if utterance == "那[東部]有哪些[岩館]呢":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if args[0] in userDefinedDICT["_sides"]:
            resultDICT["_person_loc"] = args[0]
            counties = getSideCounties(args[0])
            selectedGyms = set()
            for county in counties:
                selectedGyms.update(getLocBTSGym(county, args[1]))
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}有{2}".format(args[0], args[1], gymsNames)
        elif args[0] in userDefinedDICT["_taiwanAlias"]:
            selectedGyms = getBTSGym(args[1])
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}有{2}".format(args[0], args[1], gymsNames)
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[台北]哪些[地方][可以]攀岩":
        if checkLocation(args[0]):
            resultDICT["_person_loc"] = args[0]
            selectedGyms = getLocBTSGym(resultDICT["_person_loc"], "")
            gymsNames = containerToString(selectedGyms)
            if len(selectedGyms) != 0:
                resultDICT["reply_gym_name"] = "{0}的岩館有{1}".format(args[0], gymsNames)
            else:
                resultDICT["reply_gym_name"] = "{0}沒有岩館哦！".format(arg[0])
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    if utterance == "[東部]攀岩[可以]去哪裡":
        if args[0] in userDefinedDICT["_sides"]:
            resultDICT["_person_loc"] = args[0]
            counties = getSideCounties(args[0])
            selectedGyms = set()
            for county in counties:
                selectedGyms.update(getLocBTSGym(county, args[1]))
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}有{2}".format(args[0], args[1], gymsNames)
        elif args[0] in userDefinedDICT["_taiwanAlias"]:
            selectedGyms = getBTSGym(args[1])
            gymsNames = containerToString(selectedGyms)
            resultDICT["reply_gym_name"] = "{0}的{1}有{2}".format(args[0], args[1], gymsNames)
        else:
            resultDICT["reply_gym_name"] = choice(defaultResponse["_not_taiwan_city"])

    return resultDICT