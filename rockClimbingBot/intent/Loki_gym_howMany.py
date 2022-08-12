#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for gym_howMany

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

DEBUG_gym_howMany = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "data/USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_can":["可以","可","適合"],"_pants":["褲子","褲","長褲","短褲","運動褲","瑜珈褲","單車褲"],"_rocks":["岩點","石頭","手點","點","岩石","攀岩鞋","攀岩鞋子"],"_shoes":["岩鞋","鞋子","抱石鞋","鞋"],"_sides":["東部","北部","南部","西部","中部"],"_levels":["難度","等級","階級","級數"],"_whatIs":["星光票"],"_clothes":["衣服","長袖","短袖","衣著","服裝","長袖衣服","上衣","短袖衣服","長袖上衣","短袖上衣","衣褲"],"_climbing":["上攀","速度攀","速度攀登","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石攀岩","抱石"],"_cityAlias":["縣市","縣","市","地區","都市","城市","區","區域"],"_gymsShort":["紅石","小岩館","Camp 4","角岩館","Corner","汐止抱石館","double8","double 8","原岩","Up聯盟","MegaSTONE","POGO","爬森","蕃薯藤","千手抱石","水美iClimb","風城","B-plus","新竹紅石","TheDepotCity","攀吶","Dapro","破舊二廠","破舊工廠","嗨翻","抱石基地","圓石","圓石空間","Boulder Space","K2","艾思博","禾匠","崩岩","久淘","宜蘭運動中心","嘉義攀岩會館","8a攀岩場","Y17"],"_peClothes":["運動衣","運動褲","運動服","瑜珈褲","單車褲"],"_rockTypes":["jug","pinch","sloper","edge","crimp","pocket","flat","horn","volume"],"_climbingGym":["岩館","攀岩館","攀岩場","抱石館","抱石場館","抱石場","岩場","上攀館","上攀場","上攀場館","攀石場","上攀場館","上攀岩館","先鋒攀岩館","速度攀岩館","速度攀登場館","速度攀場館","速度攀登岩館","速度攀場地"],"_taiwanAlias":["全台","全臺","全台各地","台灣","臺灣","全臺各地"],"_climbingEquip":["裝","裝備","岩粉","粉袋","攀岩粉袋","粉球","止滑粉","攀岩粉","攀岩粉袋","岩點刷","攀岩刷","鎂粉球","鎂粉","碳酸鎂粉"],"_normalWearings":["一般運動鞋","牛仔褲"],"_topRopingEquip":["手套","確保手套","垂降手套","耐磨手套","安全吊帶","確保器","安全扣","快扣","安全扣環","吊帶"],"_climbingGeneralGym":["岩館","攀岩館","攀岩場","攀岩場館"]}

gymsInfo = pd.read_csv('data/climbingGym.csv', encoding = 'utf-8')
extendedDICT = {"_taiwanCities":["雲林","嘉義","台南","高雄","屏東","花蓮","台東","基隆","台北","桃園","新竹","宜蘭","新北","苗栗","台中","彰化","南投","蘭嶼","綠島","金門","馬祖","龜山島"],"_midTW":["苗栗","台中","彰化","南投"],"_eastTW":["花蓮","台東"],"_northTW":["基隆","台北","桃園","新竹","宜蘭","新北"],"_southTW":["雲林","嘉義","台南","高雄","屏東"]}
defaultResponse = json.load("data/defaultResponse.json",encoding = "utf-8")
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_gym_howMany:
        print("[gym_howMany] {} ===> {}".format(inputSTR, utterance))

#取得Ｘ縣市的岩館數量
def countLocGym(county):
    count = 0
    for i in range(len(gymsInfo)):
        if county in gymsInfo.iloc[i,2]:
            count += 1
    return count

#取得Ｘ縣市的抱石、上攀或速度岩館數量
def countLocBTSGym(county, bts): #b = 1, t = 2, s = 3
    count = 0
    if bts == 1:
        for i in range(len(gymsInfo)):
            if county in gymsInfo.iloc[i,2] and gymsInfo.iloc[i, 3] == 1:
                count += 1
    elif bts == 2:
        for i in range(len(gymsInfo)):
            if county in gymsInfo.iloc[i,2] and gymsInfo.iloc[i, 4] == 1:
                count += 1
    elif bts == 3:
        for i in range(len(gymsInfo)):
            if county in gymsInfo.iloc[i,2] and gymsInfo.iloc[i, 5] == 1:
                count += 1
    return count

#取得所有的抱石、上攀或速度岩館數量
def countBTSGym(bts): #b = 1, t = 2, s = 3
    count = 0
    if bts == 1:
        for i in range(len(gymsInfo)):
            if gymsInfo.iloc[i, 3] == 1:
                count += 1
    elif bts == 2:
        for i in range(len(gymsInfo)):
            if gymsInfo.iloc[i, 4] == 1:
                count += 1
    elif bts == 3:
        for i in range(len(gymsInfo)):
            if gymsInfo.iloc[i, 5] == 1:
                count += 1
    return count

def checkLocation(inputSTR):
    if inputSTR[:2] in extendedDICT["_taiwanCities"]:
        return inputSTR[:2]
    return

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[新竹]有多少[岩館]":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_howMany"] = defaultResponse["_not_rock_climbing"][random.randint(1,4)]
            pass
        if len(checkLocation(inputSTR)) > 0:
            gymCount = 0
            if "抱石" in args[1]:
                gymCount = countLocBTSGym(args[0], 1)
            elif "上攀" in args[1] or "先鋒" in args[1]:
                gymCount = countLocBTSGym(args[0], 2)
            elif "速度" in args[1]:
                gymCount = countLocBTSGym(args[0], 3)
            else:
                gymCount = countLocGym(args[0])            
            if gymCount > 0:
                resultDICT["_gym_howMany"] =  "{0}的{1}有{2}間".format(args[0],args[1], gymCount)
            else:
                resultDICT["_gym_howMany"] = "{}沒有岩館哦！".format(args[0])
        else:
           resultDICT["_gym_howMany"] = defaultResponse["_not_taiwan_city"][random.randint(1,4)] 
        pass
    if utterance == "[新竹]有幾[間][岩館]":
        if args[2] not in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_howMany"] = defaultResponse["_not_rock_climbing"][random.randint(1,4)]
            pass
        if len(checkLocation(inputSTR)) > 0:
            gymCount = 0
            if "抱石" in args[2]:
                gymCount = countLocBTSGym(args[0], 1)
            elif "上攀" in args[2] or "先鋒" in args[1]:
                gymCount = countLocBTSGym(args[0], 2)
            elif "速度" in args[2]:
                gymCount = countLocBTSGym(args[0], 3)
            else:
                gymCount = countLocGym(args[0])            
            if gymCount > 0:
                resultDICT["_gym_howMany"] = "{0}的{1}有{2}間".format(args[0],args[2], gymCount)
            else:
                resultDICT["_gym_howMany"] = "{}沒有岩館哦！".format(args[0])
        else:
           resultDICT["_gym_howMany"] = defaultResponse["_not_taiwan_city"][random.randint(1,4)] 
        pass
    if utterance == "[東部]有多少[岩館]":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_howMany"] = defaultResponse["_not_rock_climbing"][random.randint(1,4)]
            pass
        if args[0] in userDefinedDICT["_sides"]:
            gymCount = 0
            counties = []
            if args[0] == "中部":
                counties = extendedDICT["_midTW"]
            elif args[0] == "北部"：
                counties = extendedDICT["_northTW"]
            elif args[0] == "南部"：
                counties = extendedDICT["_southTW"]
            elif args[0] == "東部":
                counties = extendedDICT["_eastTW"]
            else: 
                counties = list(gymCountySet())
                counties.remove("花蓮","台東")
            if "抱石" in args[1]:
                for county in counties:
                    gymCount += countLocBTSGym(county, 1)
            elif "上攀" in args[1] or "先鋒" in args[1] :
                for county in counties:
                    gymCount += countLocBTSGym(county, 2)
            elif "速度" in args[1]:
                for county in counties:
                    gymCount += countLocBTSGym(county, 3)
            else:
                for county in counties:
                    gymCount += countLocGym(county)
            if gymCount > 0:
                resultDICT["_gym_howMany"] = "{0}的{1}有{2}間".format(args[0],args[1], gymCount)
            else:
                resultDICT["_gym_howMany"] = "{}沒有岩館哦！".format(args[0])
        elif len(checkLocation(inputSTR)) > 0:
            loc = checkLocation(inputSTR)
            gymCount = 0
            if "抱石" in args[1]:
                gymCount = countLocBTSGym(loc, 1)
            elif "上攀" in args[1] or "先鋒" in args[1]:
                gymCount = countLocBTSGym(loc, 2)
            elif "速度" in args[1]:
                gymCount = countLocBTSGym(loc, 3)
            else:
                gymCount = countLocGym(loc)            
            if gymCount > 0:
                resultDICT["_gym_howMany"] =  "{0}的{1}有{2}間".format(args[0],args[1], gymCount)
            else:
                resultDICT["_gym_howMany"] = "{}沒有岩館哦！".format(loc)
        elif args[0] in userDefinedDICT["_taiwanAlias"]:
            gymCount = 0
            if "抱石" in args[1]:
                gymCount = countBTSGym(1)
            elif "上攀" in args[1] or "先鋒" in args[1]:
                gymCount = countBTSGym(2)
            elif "速度" in args[1]:
                gymCount = countBTSGym(3)
            else:
                resultDICT["_gym_howMany"] = "{0}的岩館共有{1}間".format(args[0],len(gymsInfo)+1)
            resultDICT["_gym_howMany"] = "{0}的{1}共有{2}間".format(args[0],args[1],gymCount)
        else:
           resultDICT["_gym_howMany"] = defaultResponse["_not_taiwan_city"][random.randint(1,4)] 
        pass
    if utterance == "[東部]有幾[間][岩館]":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_howMany"] = defaultResponse["_not_rock_climbing"][random.randint(1,4)]
            pass
        if args[0] in userDefinedDICT["_sides"]:
            gymCount = 0
            counties = []
            if args[0] == "中部":
                counties = extendedDICT["_midTW"]
            elif args[0] == "北部"：
                counties = extendedDICT["_northTW"]
            elif args[0] == "南部"：
                counties = extendedDICT["_southTW"]
            elif args[0] == "東部":
                counties = extendedDICT["_eastTW"]
            else: 
                counties = list(gymCountySet())
                counties.remove("花蓮","台東")
            if "抱石" in args[1]:
                for county in counties:
                    gymCount += countLocBTSGym(county, 1)
            elif "上攀" in args[1] or "先鋒" in args[1] :
                for county in counties:
                    gymCount += countLocBTSGym(county, 2)
            elif "速度" in args[1]:
                for county in counties:
                    gymCount += countLocBTSGym(county, 3)
            else:
                for county in counties:
                    gymCount += countLocGym(county)
            if gymCount > 0:
                resultDICT["_gym_howMany"] =  "{0}的{1}有{2}間".format(args[0],args[2], gymCount)
            else:
                resultDICT["_gym_howMany"] = "{}沒有岩館哦！".format(args[0])
        elif len(checkLocation(inputSTR)) > 0:
            loc = checkLocation(inputSTR)
            gymCount = 0
            if "抱石" in args[1]:
                gymCount = countLocBTSGym(loc, 1)
            elif "上攀" in args[1] or "先鋒" in args[1]:
                gymCount = countLocBTSGym(loc, 2)
            elif "速度" in args[1]:
                gymCount = countLocBTSGym(loc, 3)
            else:
                gymCount = countLocGym(loc)            
            if gymCount > 0:
                resultDICT["_gym_howMany"] =  "{0}的{1}有{2}間".format(args[0],args[2], gymCount)
            else:
                resultDICT["_gym_howMany"] = "{}沒有岩館哦！".format(loc)
        elif args[0] in userDefinedDICT["_taiwanAlias"]:
            gymCount = 0
            if "抱石" in args[2]:
                gymCount = countBTSGym(1)
            elif "上攀" in args[2] or "先鋒" in args[1]:
                gymCount = countBTSGym(2)
            elif "速度" in args[2]:
                gymCount = countBTSGym(3)
            else:
                resultDICT["_gym_howMany"] = "{0}的岩館共有{1}間".format(args[0],len(gymsInfo)+1)
            resultDICT["_gym_howMany"] = "{0}的{1}共有{2}間".format(args[0],args[2],gymCount)
        else:
           resultDICT["_gym_howMany"] = defaultResponse["_not_taiwan_city"][random.randint(1,4)] 

    return resultDICT