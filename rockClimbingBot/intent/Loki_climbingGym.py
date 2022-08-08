#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for climbingGym

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

DEBUG_climbingGym = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_can":["可以","可","適合"],"_what":["什麼","哪些","什麼東西","哪些東西","哪種","哪幾間"],"_midTW":["苗栗","台中","彰化","南投"],"_pants":["褲子","褲","長褲","短褲","運動褲","瑜珈褲"],"_rocks":["岩點","石頭","手點","點"],"_rules":["規則","規範","法則","守則","規定"],"_shoes":["岩鞋","鞋子","攀岩鞋","抱石鞋","鞋"],"_sides":["東部","北部","南部","西部","中部"],"_which":["哪幾間","哪間","哪一間","哪些","哪個"],"_eastTW":["花蓮","台東"],"_levels":["難度","等級","階級"],"_clothes":["衣服","長袖","短袖","衣著","服裝","長袖衣服","上衣","短袖衣服","長袖上衣","短袖上衣","衣褲"],"_northTW":["基隆","台北","桃園","新竹","宜蘭","新北"],"_southTW":["雲林","嘉義","台南","高雄","屏東"],"_climbing":["攀岩","抱石","上攀","速度攀","速度攀登","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石攀岩"],"_cityAlias":["縣市","縣","市","地區","都市","城市","區","區域"],"_peClothes":["運動衣","運動褲","運動服","瑜珈褲","單車褲"],"_rockTypes":["jug","pinch","sloper","edge","crimp","pocket","flat","horn","volume"],"_appearance":["樣子","模樣"],"_climbingGym":["岩館","攀岩館","攀岩場","抱石館","抱石場館","抱石場","岩場","上攀館","上攀場","上攀場館"],"_climbingTop":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","上攀館","上攀場館","上攀岩館","先鋒攀岩館"],"_taiwanAlias":["全台","全臺","全台各地","台灣","臺灣","全臺各地"],"_taiwanCities":["雲林","嘉義","台南","高雄","屏東","花蓮","台東","基隆","台北","桃園","新竹","宜蘭","新北","苗栗","台中","彰化","南投"],"_climbingEquip":["裝","裝備","岩粉","粉袋","攀岩粉袋","粉球","止滑粉","攀岩粉","攀岩粉袋","岩點刷","攀岩刷","鎂粉球","鎂粉","碳酸鎂粉"],"_climbingSpeed":["速度攀","速度攀登","速度攀岩館","速度攀登場館"],"_topRopingEquip":["手套","確保手套","垂降手套","耐磨手套","安全吊帶","確保器","安全扣","快扣","安全扣環","吊帶"],"_climbingBoulder":["抱石","抱石攀岩","抱石館","抱石場館","抱石場"],"_climbingGeneralGym":["岩館","攀岩館","攀岩場","攀岩場館"]}

gymsInfo = pd.read_csv('climbingGym.csv', encoding = 'utf-8')
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_climbingGym:
        print("[climbingGym] {} ===> {}".format(inputSTR, utterance))

#取得有岩館的縣市
def gymCountySet():
    countySet = set()
    for i in range(len(gymsInfo)):
        countySet.add(gymsInfo.iloc[i,2][:2])
    return countySet

#取得有「抱石」館的縣市
def gymCountyBloulderSet():
    countySet = set()
    for i in range(len(gymsInfo)):
        if gymsInfo.iloc[i,3] == 1:
            countySet.add(gymsInfo.iloc[i,2][:2])
    return countySet

#取得有「上攀」館的縣市
def gymCountyTopSet():
    countySet = set()
    for i in range(len(gymsInfo)):
        if gymsInfo.iloc[i,4] == 1:
            countySet.add(gymsInfo.iloc[i,2][:2])
    return countySet

#取得有「速度攀」館的縣市
def gymCountySpeedSet():
    countySet = set()
    for i in range(len(gymsInfo)):
        if gymsInfo.iloc[i,5] == 1:
            countySet.add(gymsInfo.iloc[i,2][:2])
    return countySet

#有無岩館
def hasGymCounty(county):
    countySet = gymCountySet()
    return county in countySet

#有無抱石館
def hasBoulderGymCounty(county):
    countySet = gymCountyBoulderSet()
    return county in countySet

#有無上攀館
def hasTopGymCounty(county):
    countySet = gymCountyTopSet()
    return county in countySet

#有無速度攀館
def hasSpeedGymCounty(county):
    countySet = gymCountySpeedSet()
    return county in countySet

#取得Ｘ縣市的所有岩館名稱    
def getLocGym(county):
    locGymSet = set()
    for i in range(len(gymsInfo)):
        if county in gymsInfo.iloc[i,2]:
            locGymSet.add(gymsInfo.iloc[i, 0])
    return str(locGymSet)

#取得Ｘ縣市的抱石、上攀或速度岩館名稱   
def getLocBTSGym(county, bts): #b = 1, t = 2, s = 3
    locGymSet = set()
    if bts == 1:
        for i in range(len(gyms)):
            if county in gymsInfo.iloc[i,2] and gymsInfo.iloc[i, 3] == 1:
                locGymSet.add(gymsInfo.iloc[i, 0])
    elif bts == 2:
        for i in range(len(gyms)):
            if county in gymsInfo.iloc[i,2] and gymsInfo.iloc[i, 4] == 1:
                locGymSet.add(gymsInfo.iloc[i, 0]) 
    else:
        for i in range(len(gyms)):
            if county in gymsInfo.iloc[i,2] and gymsInfo.iloc[i, 5] == 1:
                locGymSet.add(gymsInfo.iloc[i, 0]) 
    return str(locGymSet)

#取得Ｘ縣市的岩館數量
def countLocGym(county):
    count = 0
    for i in range(len(gymsInfo)):
        if county in gymsInfo.iloc[i,2]:
            count += 1
    return count

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[台中]有哪些[岩館]":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["func_loc"] = "攀岩以外都不在我的能力範圍內哦！"
            pass
        if arg[0] not in userDefinedDICT["_taiwanCities"] or arg[0] not in userDefinedDICT["_sides"]:
            resultDICT["func_loc"] = "台灣以外的岩館我不熟耶！"
            pass        
        if args[0] in userDefinedDICT["_sides"]:
            areaSet = set()
            counties = []
            if args[0] == "中部":
                counties = userDefinedDICT["_midTW"]
            elif args[0] == "北部"：
                counties = userDefinedDICT["_northTW"]
            elif args[0] == "南部"：
                counties = userDefinedDICT["_southTW"]
            elif args[0] == "東部":
                counties = userDefinedDICT["_eastTW"]
            else: 
                counties = list(gymCountySet())
                counties.remove("花蓮","台東")

            if "抱石" in arg[1]:
                for county in counties:
                    if hasBoulderGymCounty(county):
                        countyGym = getLocBTSGym(county, 1)
                        areaSet.add(countyGym)
            elif arg[1] in userDefinedDICT["_climbingTop"]:
                for county in counties:
                    if hasTopGymCounty(county):
                        countyGym = getLocBTSGym(county, 2)
                        areaSet.add(countyGym)
            elif arg[1] in userDefinedDICT["_climbingSpeed"]:
                for county in counties:
                    if hasSpeedGymCounty(county):
                        countyGym = getLocBTSGym(county, 3)
                        areaSet.add(countyGym)
            else: 
                for county in counties:
                    if hasGymCounty(county):
                        countyGym = getLocGym(county)
                        areaSet.add(countyGym)
            if len(areaSet) != 0:
                resultDICT["func_loc"] = args[0]+"的"+args[1]+"有"+ str(areaSet)
            else: 
                resultDICT["func_loc"] = args[0]+"沒有"+args[1]+"哦！"
        elif args[0] in userDefinedDICT["_taiwanAlias"]:
            counties = list(gymCountySet())
            if "抱石" in arg[1]:
                for county in counties:
                    if hasBoulderGymCounty(county):
                        countyGym = getLocBTSGym(county, 1)
                        areaSet.add(countyGym)
            elif arg[1] in userDefinedDICT["_climbingTop"]:
                for county in counties:
                    if hasTopGymCounty(county):
                        countyGym = getLocBTSGym(county, 2)
                        areaSet.add(countyGym)
            elif arg[1] in userDefinedDICT["_climbingSpeed"]:
                for county in counties:
                    if hasSpeedGymCounty(county):
                        countyGym = getLocBTSGym(county, 3)
                        areaSet.add(countyGym)
            else: 
                for county in counties:
                    if hasGymCounty(county):
                        countyGym = getLocGym(county)
                        areaSet.add(countyGym)
            resultDICT["func_loc"] = "台灣的"+args[0]+"有"+ str(areaSet)
        elif "抱石" in arg[1]:
            if hasBoulderGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[1]+"有"+getLocBTSGym(args[0],1)
            else:
                resultDICT["func_loc"] = args[0]+"沒有"+args[1]+"哦！"
        elif arg[1] in userDefinedDICT["_climbingTop"]:
            if hasTopGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[1]+"有"+getLocBTSGym(args[0],2)
            else:
                resultDICT["func_loc"] = args[0]+"沒有"+args[1]+"哦！"
        elif arg[1] in userDefinedDICT["_climbingSpeed"]:
            if hasTopGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[1]+"有"+getLocBTSGym(args[0],3)
            else:
                resultDICT["func_loc"] = args[0]+"沒有"+args[1]+"哦！"
        elif arg[1] in userDefinedDICT["_climbingGym"]:
            if hasGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[1]+"有"+getLocGym(args[0])
        else:
            resultDICT["func_loc"] = args[0]+'沒有岩館哦！'
        pass

    if utterance == "[台北]哪裡[可以][抱石]":
        if args[2] not in userDefinedDICT["_climbing"]:
            resultDICT["func_loc"] = "攀岩以外都不在我的能力範圍內哦！"
            pass
        if arg[0] not in userDefinedDICT["_taiwanCities"] or arg[0] not in userDefinedDICT["_sides"]:
            resultDICT["func_loc"] = "台灣以外的岩館我不熟耶！"
            pass        
        if args[0] in userDefinedDICT["_sides"]:
            areaSet = set()
            counties = []
            if args[0] == "中部":
                counties = userDefinedDICT["_midTW"]
            elif args[0] == "北部"：
                counties = userDefinedDICT["_northTW"]
            elif args[0] == "南部"：
                counties = userDefinedDICT["_southTW"]
            elif args[0] == "東部":
                counties = userDefinedDICT["_eastTW"]
            else: 
                counties = list(gymCountySet())
                counties.remove("花蓮","台東")

            if "抱石" in arg[2]:
                for county in counties:
                    if hasBoulderGymCounty(county):
                        countyGym = getLocBTSGym(county, 1)
                        areaSet.add(countyGym)
            elif arg[2] in userDefinedDICT["_climbingTop"]:
                for county in counties:
                    if hasTopGymCounty(county):
                        countyGym = getLocBTSGym(county, 2)
                        areaSet.add(countyGym)
            elif arg[2] in userDefinedDICT["_climbingSpeed"]:
                for county in counties:
                    if hasSpeedGymCounty(county):
                        countyGym = getLocBTSGym(county, 3)
                        areaSet.add(countyGym)
            else: 
                for county in counties:
                    if hasGymCounty(county):
                        countyGym = getLocGym(county)
                        areaSet.add(countyGym)
            if len(areaSet) != 0:
                resultDICT["func_loc"] = args[0]+"的"+args[2]+"有"+ str(areaSet)
            else: 
                resultDICT["func_loc"] = args[0]+"沒有"+args[2]+"哦！"
        elif args[0] in userDefinedDICT["_taiwanAlias"]:
            counties = list(gymCountySet())
            if "抱石" in arg[2]:
                for county in counties:
                    if hasBoulderGymCounty(county):
                        countyGym = getLocGym(county)
                        areaSet.add(countyGym)
            elif arg[2] in userDefinedDICT["_climbingTop"]:
                for county in counties:
                    if hasTopGymCounty(county):
                        countyGym = getLocGym(county)
                        areaSet.add(countyGym)
            elif arg[2] in userDefinedDICT["_climbingSpeed"]:
                for county in counties:
                    if hasSpeedGymCounty(county):
                        countyGym = getLocGym(county)
                        areaSet.add(countyGym)
            else: 
                for county in counties:
                    if hasGymCounty(county):
                        countyGym = getLocGym(county)
                        areaSet.add(countyGym)
            resultDICT["func_loc"] = "台灣的"+args[2]+"有"+ str(areaSet)
        elif "抱石" in arg[2]:
            if hasBoulderGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[2]+"有"+getLocGym(args[0])
            else:
                resultDICT["func_loc"] = args[0]+"沒有"+args[2]+"哦！"
        elif arg[2] in userDefinedDICT["_climbingTop"]:
            if hasTopGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[2]+"有"+getLocGym(args[0])
            else:
                resultDICT["func_loc"] = args[0]+"沒有"+args[2]+"哦！"
        elif arg[2] in userDefinedDICT["_climbingSpeed"]:
            if hasSpeedGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[2]+"有"+getLocGym(args[0])
            else:
                resultDICT["func_loc"] = args[0]+"沒有"+args[2]+"哦！"
        elif arg[2] in userDefinedDICT["_climbingGym"]:
            if hasGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[2]+"有"+getLocGym(args[0])
        else:
            resultDICT["func_loc"] = args[0]+'沒有岩館哦！'
        pass

    if utterance == "[台灣][哪些][縣市]有[岩館]呢":
        if args[3] not in userDefinedDICT["climbingGym"]:
            result["func_loc"] = "攀岩以外都不在我的能力範圍哦！"
            pass
        if args[0] not in userDefinedDICT["_taiwanAlias"]:
            resultDICT["func_loc"] = "台灣以外的岩館我不熟耶！"
            pass
        if args[2] in userDefinedDICT["_cityAlias"]:
            if "抱石" in args[3]:
                result["func_loc"] = str(gymCountyBloulderSet())
            elif args[3] in userDefinedDICT["_climbingTop"]:
                result["func_loc"] = str(gymCountyTopSet())
            elif args[3] in userDefinedDICT["_climbingSpeed"]:
                result["func_loc"] = str(gymCountySpeedSet())
            else:
                result["func_loc"] = str(gymCountySet())
        pass

    if utterance == "[哪幾間]岩館有[速度攀]":
        if "抱石" in args[1]:
            resultDICT["func_loc"] = "大部分岩館都可以抱石耶！請問有特別想查哪個縣市嗎？"
        elif arg[1] in userDefinedDICT["_climbingTop"]:
            gymSet = set()
            for i in range(len(gymsInfo)):
                if gymsInfo.iloc[i, 4] == 1:
                    gymSet.add(gymsInfo.iloc[i, 0])
            resultDICT["func_loc"] = str(gymSet)
        else:
            gymSet = set()
            for i in range(len(gymsInfo)):
                if gymsInfo.iloc[i, 5] == 1:
                    gymSet.add(gymsInfo.iloc[i, 0])
            resultDICT["func_loc"] = str(gymSet)
        pass

    if utterance == "[攀岩][一次]多少[錢]":
        resultDICT["func_money"] = '據岩館地區的不同，入館價格約落在150-450左右，租借岩鞋岩粉各別會再加50-100左右'
        pass

    if utterance == "[新手][可以]去哪[攀岩]":
        if args[2] not in userDefinedDICT["_climbing"]:
            resultDICT["func_loc"] = "攀岩以外都不屬於我的能力範圍哦！"
            pass
        resultDICT["loc"] = "大多數岩館都有適合各種程度的路線哦！請問你在哪裡呢？"
        pass

    if utterance == "[新竹]有幾[間][岩館]":
        if args[2] not in userDefinedDICT["_climbingGym"]:
            resultDICT["func_loc"] = "攀岩以外都不屬於我的能力範圍哦！"
            pass
        if arg[0] not in userDefinedDICT["_taiwanCities"] or arg[0] not in userDefinedDICT["_sides"]:
            resultDICT["func_loc"] = "台灣以外的岩館我不熟耶！"
            pass        
        if args[0] in userDefinedDICT["_sides"]:
            gymCount = 0
            counties = []
            if args[0] == "中部":
                counties = userDefinedDICT["_midTW"]
            elif args[0] == "北部"：
                counties = userDefinedDICT["_northTW"]
            elif args[0] == "南部"：
                counties = userDefinedDICT["_southTW"]
            elif args[0] == "東部":
                counties = userDefinedDICT["_eastTW"]
            else: 
                counties = list(gymCountySet())
                counties.remove("花蓮","台東")

            if "抱石" in arg[2]:
                for county in counties:
                    if hasBoulderGymCounty(county):
                        gymCount += len(gymCountyBoulderSet(county))
            elif arg[2] in userDefinedDICT["_climbingTop"]:
                for county in counties:
                    if hasTopGymCounty(county):
                        gymCount += len(gymCountyTopSet(county))
            elif arg[2] in userDefinedDICT["_climbingSpeed"]:
                for county in counties:
                    if hasSpeedGymCounty(county):
                        gymCount += len(gymCountySpeedSet(county))       
            else: 
                for county in counties:
                    if hasGymCounty(county):
                        gymCount += len(gymCountySet(county))
            if gymCount != 0:
                resultDICT["func_loc"] = args[0]+"的"+args[1]+"有"+ str(gymCount) + "間。"
            else: 
                resultDICT["func_loc"] = args[0]+"沒有"+args[1]+"哦！"
        elif args[0] in userDefinedDICT["_taiwanAlias"]:
            counties = list(gymCountySet())
            if "抱石" in arg[2]:
                for county in counties:
                    if hasBoulderGymCounty(county):
                        gymCount += len(gymCountyBoulderSet(county))
            elif arg[2] in userDefinedDICT["_climbingTop"]:
                for county in counties:
                    if hasTopGymCounty(county):
                        gymCount += len(gymCountyTopSet(county))
            elif arg[2] in userDefinedDICT["_climbingSpeed"]:
                for county in counties:
                    if hasSpeedGymCounty(county):
                        gymCount += len(gymCountySpeedSet(county))
            else: 
                for county in counties:
                    if hasGymCounty(county):
                        gymCount += len(gymCountySet(county))
            resultDICT["func_loc"] = "台灣的"+args[1]+"有"+ str(gymCount)+"間。"
        elif "抱石" in arg[2]:
            if hasBoulderGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[2]+"有"+ str(gymCount) + "間。"
            else:
                resultDICT["func_loc"] = args[0]+"沒有"+args[2]+"哦！"
        elif arg[2] in userDefinedDICT["_climbingTop"]:
            if hasTopGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[2]+"有"+ str(gymCount) + "間。"
            else:
                resultDICT["func_loc"] = args[0]+"沒有"+args[2]+"哦！"
        elif arg[2] in userDefinedDICT["_climbingSpeed"]:
            if hasSpeedGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[2]+"有"+ str(gymCount) + "間。"
            else:
                resultDICT["func_loc"] = args[0]+"沒有"+args[2]+"哦！"
        elif arg[2] in userDefinedDICT["_climbingGym"]:
            if hasGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[2]+"有"+ str(gymCount) + "間。"
        else:
            resultDICT["func_loc"] = args[0]+'沒有岩館哦！'
        pass

    if utterance == "[東部]有[岩館]嗎":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["func_loc"] = "攀岩以外都不屬於我的能力範圍哦！"
            pass
        if args[0] in userDefinedDICT["_sides"]:
            if args[1] in userDefinedDICT["_climbingGym"]:
                resultDICT["func_loc"] = "有哦！"
            elif args[1] in userDefinedDICT["_climbingSpeed"]:
                gymCount = 0
                counties = []
                if args[0] == "中部":
                    counties = userDefinedDICT["_midTW"]
                elif args[0] == "北部"：
                    counties = userDefinedDICT["_northTW"]
                elif args[0] == "南部"：
                    counties = userDefinedDICT["_southTW"]
                elif args[0] == "東部":
                    counties = userDefinedDICT["_eastTW"]
                else: 
                    counties = list(gymCountySet())
                    counties.remove("花蓮","台東")
                for county in counties:
                    if hasSpeedGymCounty(county):
                        gymCount += len(gymCountySpeedSet(county))
                if gymCount != 0:
                    resultDICT["func_loc"] = "有哦！"
                else:
                    resultDICT["func_loc"] = "沒有耶！"
        elif args[0] in userDefinedDICT["_taiwanCities"]:
            if "抱石" in arg[1]:
                if hasBoulderGymCounty(args[1]):
                    resultDICT["func_loc"] = "有哦！"
                else:
                    resultDICT["func_loc"] = "沒有耶！"
            elif arg[1] in userDefinedDICT["_climbingTop"]:
                if hasTopGymCounty(args[1]):
                    resultDICT["func_loc"] = "有哦！"
                else:
                    resultDICT["func_loc"] = "沒有耶！"
            elif arg[1] in userDefinedDICT["_climbingSpeed"]:
                if hasSpeedGymCounty(args[1]):
                    resultDICT["func_loc"] = "有哦！"
                else:
                    resultDICT["func_loc"] = "沒有耶！"
            else:
                if hasGymCounty(args[1]):
                    resultDICT["func_loc"] = "有哦！"
                else:
                    resultDICT["func_loc"] = "沒有耶！"
            pass

    if utterance == "[苗栗][能][攀岩]嗎":
        if args[2] not in userDefinedDICT["_climbing"]:
            resultDICT["func_loc"] = "攀岩以外都不屬於我的能力範圍哦！"
            pass
        if args[0] in userDefinedDICT["_sides"]:
            resultDICT["func_loc"] = "可以哦！"
        elif args[0] in userDefinedDICT["_taiwanCities"]:
            if "抱石" in arg[2]:
                if hasBoulderGymCounty(args[2]):
                    resultDICT["func_loc"] = "可以哦！"+args[0]+"有抱石館"
                else:
                    resultDICT["func_loc"] = args[0]+"沒有抱石館耶！要不要考慮其他縣市？"
            elif arg[1] in userDefinedDICT["_climbingTop"]:
                if hasTopGymCounty(args[1]):
                    resultDICT["func_loc"] = "可以哦！"+args[0]+"有上攀岩館"
                else:
                    resultDICT["func_loc"] = args[0]+"沒有上攀岩館耶！要不要考慮其他縣市？"
            elif arg[1] in userDefinedDICT["_climbingSpeed"]:
                if hasSpeedGymCounty(args[1]):
                    resultDICT["func_loc"] = "可以哦！"+args[0]+"有速度攀的岩館"
                else:
                    resultDICT["func_loc"] = args[0]+"沒有有速度牆的岩館耶！要不要考慮其他縣市？"
            else:
                if hasGymCounty(args[1]):
                    resultDICT["func_loc"] = "可以哦！"+args[0]+"有岩館"
                else:
                    resultDICT["func_loc"] = args[0]+"沒有岩館耶！要不要考慮其他縣市？"
        pass

    if utterance == "[紅石][攀岩][一天]多少錢":
        # write your code here
        pass

    if utterance == "[紅石][攀岩][一次]多少":
        # write your code here
        pass

    if utterance == "[苗栗][能][攀岩]嗎":
        if args[2] not in userDefinedDICT["_climbing"]:
            resultDICT["func_loc"] = "攀岩以外都不在我的能力範圍內哦！"
            pass
        if arg[0] not in userDefinedDICT["_taiwanCities"] or arg[0] not in userDefinedDICT["_sides"]:
            resultDICT["func_loc"] = "台灣以外的岩館我不熟耶！"
            pass        
        if args[0] in userDefinedDICT["_sides"]:
            areaSet = set()
            counties = []
            if args[0] == "中部":
                counties = userDefinedDICT["_midTW"]
            elif args[0] == "北部"：
                counties = userDefinedDICT["_northTW"]
            elif args[0] == "南部"：
                counties = userDefinedDICT["_southTW"]
            elif args[0] == "東部":
                counties = userDefinedDICT["_eastTW"]
            else: 
                counties = list(gymCountySet())
                counties.remove("花蓮","台東")

            if "抱石" in arg[2]:
                for county in counties:
                    if hasBoulderGymCounty(county):
                        countyGym = getLocBTSGym(county, 1)
                        areaSet.add(countyGym)
            elif arg[2] in userDefinedDICT["_climbingTop"]:
                for county in counties:
                    if hasTopGymCounty(county):
                        countyGym = getLocBTSGym(county, 2)
                        areaSet.add(countyGym)
            elif arg[2] in userDefinedDICT["_climbingSpeed"]:
                for county in counties:
                    if hasSpeedGymCounty(county):
                        countyGym = getLocBTSGym(county, 3)
                        areaSet.add(countyGym)
            else: 
                for county in counties:
                    if hasGymCounty(county):
                        countyGym = getLocGym(county)
                        areaSet.add(countyGym)
            if len(areaSet) != 0:
                resultDICT["func_loc"] = args[0]+"的"+args[2]+"館有"+ str(areaSet)
            else: 
                resultDICT["func_loc"] = args[0]+"沒有"+args[2]+"館哦！"
        elif args[0] in userDefinedDICT["_taiwanAlias"]:
            counties = list(gymCountySet())
            if "抱石" in arg[2]:
                for county in counties:
                    if hasBoulderGymCounty(county):
                        countyGym = getLocGym(county)
                        areaSet.add(countyGym)
            elif arg[2] in userDefinedDICT["_climbingTop"]:
                for county in counties:
                    if hasTopGymCounty(county):
                        countyGym = getLocGym(county)
                        areaSet.add(countyGym)
            elif arg[2] in userDefinedDICT["_climbingSpeed"]:
                for county in counties:
                    if hasSpeedGymCounty(county):
                        countyGym = getLocGym(county)
                        areaSet.add(countyGym)
            else: 
                for county in counties:
                    if hasGymCounty(county):
                        countyGym = getLocGym(county)
                        areaSet.add(countyGym)
            resultDICT["func_loc"] = "台灣的"+args[2]+"館有"+ str(areaSet)
        elif "抱石" in arg[2]:
            if hasBoulderGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[2]+"館有"+getLocGym(args[0])
            else:
                resultDICT["func_loc"] = args[0]+"沒有"+args[2]+"館哦！"
        elif arg[2] in userDefinedDICT["_climbingTop"]:
            if hasTopGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[2]+"館有"+getLocGym(args[0])
            else:
                resultDICT["func_loc"] = args[0]+"沒有"+args[2]+"館哦！"
        elif arg[2] in userDefinedDICT["_climbingSpeed"]:
            if hasSpeedGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[2]+"館有"+getLocGym(args[0])
            else:
                resultDICT["func_loc"] = args[0]+"沒有"+args[2]+"館哦！"
        elif arg[2] in userDefinedDICT["_climbingGym"]:
            if hasGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[2]+"館有"+getLocGym(args[0])
        else:
            resultDICT["func_loc"] = args[0]+'沒有岩館哦！'
        pass

    if utterance == "去[一次][岩館]多少錢":
        if args[2] not in userDefinedDICT["_climbingGym"] or args[2] not in userDefinedDICT["_climbing"]:
            resultDICT["func_loc"] = "攀岩以外都不屬於我的能力範圍哦！"
            pass
        else:
            resultDICT["func_money"] = '據岩館地區的不同，入館價格約落在150-450左右，租借岩鞋岩粉各別會再加50-100左右'
        pass

    if utterance == "去攀[一次]岩多少[錢]":
        resultDICT["func_money"] = '據岩館地區的不同，入館價格約落在150-450左右，租借岩鞋岩粉等裝備各別會再加50-100左右'
        pass

    if utterance == "哪些[縣市]有[岩館]呢": #e.g.2 哪些岩館有速度攀
        if args[1] not in userDefinedDICT["climbingGym"]:
            result["func_loc"] = "攀岩以外都不在我的能力範圍哦！"
            pass
        if args[0] in userDefinedDICT["_cityAlias"] or args[0] in userDefinedDICT["_climbingGym"]:
            if "抱石" in args[1]:
                result["func_loc"] = str(gymCountyBloulderSet())
            elif args[1] in userDefinedDICT["_climbingTop"]:
                result["func_loc"] = str(gymCountyTopSet())
            elif args[1] in userDefinedDICT["_climbingSpeed"]:
                result["func_loc"] = str(gymCountySpeedSet())
            else:
                result["func_loc"] = str(gymCountySet())
        pass

    if utterance == "哪裡可以攀岩":
        resultDICT["func_loc"] = "想找哪個地區的呢？"
        pass

    if utterance == "哪間[岩館]離[我][最近]":
        if args[0] not in userDefinedDICT["climbingGym"]:
            resultDICT["func_loc"] = "攀岩以外都不屬於我的能力範圍，麻煩重新查詢~"
        else:
            resultDICT["func_loc"] = "請問你在哪裡呢？可以給我大概地理位置嗎？"
        pass

    if utterance == "想[抱石][可以]去哪裡":
        if args[0] not in userDefinedDICT["climbing"]:
            resultDICT["func_loc"] = "攀岩以外都不屬於我的能力範圍，麻煩重新查詢~"
        else:
            resultDICT["func_loc"] = "請問你在哪裡呢？可以給我大概地理位置嗎？"
        pass

    if utterance == "推薦哪些[距離][近]的[岩館]":
        if args[2] not in userDefinedDICT["climbingGym"]:
            resultDICT["func_loc"] = "攀岩以外不在我的能力範圍內，麻煩重新查詢~"
        else:
            resultDICT["func_loc"] = "請問你在哪裡呢？可以給我大概地理位置嗎？"
        pass

    if utterance == "有哪些[岩館]呢":
        resultDICT["func_loc"] = "想找哪個地區的呢？"
        pass

    if utterance == "有推薦的[岩館][麻]":
        if args[0] not in userDefinedDICT["climbingGym"]:
            resultDICT["func_loc"] = "攀岩以外不在我的能力範圍內，麻煩重新查詢~"
        else:
            resultDICT["func_loc"] = "請問你在哪裡呢？可以給我大概地理位置嗎？"
        pass

    if utterance == "那[東部]有哪些[岩館]呢":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["func_loc"] = "攀岩以外都不在我的能力範圍內哦！"
            pass
        if arg[0] not in userDefinedDICT["_taiwanCities"] or arg[0] not in userDefinedDICT["_sides"]:
            resultDICT["func_loc"] = "台灣以外的岩館我不熟耶！"
            pass        
        if args[0] in userDefinedDICT["_sides"]:
            areaSet = set()
            counties = []
            if args[0] == "中部":
                counties = userDefinedDICT["_midTW"]
            elif args[0] == "北部"：
                counties = userDefinedDICT["_northTW"]
            elif args[0] == "南部"：
                counties = userDefinedDICT["_southTW"]
            elif args[0] == "東部":
                counties = userDefinedDICT["_eastTW"]
            else: 
                counties = list(gymCountySet())
                counties.remove("花蓮","台東")

            if "抱石" in arg[1]:
                for county in counties:
                    if hasBoulderGymCounty(county):
                        countyGym = getLocBTSGym(county, 1)
                        areaSet.add(countyGym)
            elif arg[1] in userDefinedDICT["_climbingTop"]:
                for county in counties:
                    if hasTopGymCounty(county):
                        countyGym = getLocBTSGym(county, 2)
                        areaSet.add(countyGym)
            elif arg[1] in userDefinedDICT["_climbingSpeed"]:
                for county in counties:
                    if hasSpeedGymCounty(county):
                        countyGym = getLocBTSGym(county, 3)
                        areaSet.add(countyGym)
            else: 
                for county in counties:
                    if hasGymCounty(county):
                        countyGym = getLocGym(county)
                        areaSet.add(countyGym)
            if len(areaSet) != 0:
                resultDICT["func_loc"] = args[0]+"的"+args[1]+"有"+ str(areaSet)
            else: 
                resultDICT["func_loc"] = args[0]+"沒有"+args[1]+"哦！"
        elif args[0] in userDefinedDICT["_taiwanAlias"]:
            counties = list(gymCountySet())
            if "抱石" in arg[1]:
                for county in counties:
                    if hasBoulderGymCounty(county):
                        countyGym = getLocBTSGym(county, 1)
                        areaSet.add(countyGym)
            elif arg[1] in userDefinedDICT["_climbingTop"]:
                for county in counties:
                    if hasTopGymCounty(county):
                        countyGym = getLocBTSGym(county, 2)
                        areaSet.add(countyGym)
            elif arg[1] in userDefinedDICT["_climbingSpeed"]:
                for county in counties:
                    if hasSpeedGymCounty(county):
                        countyGym = getLocBTSGym(county, 3)
                        areaSet.add(countyGym)
            else: 
                for county in counties:
                    if hasGymCounty(county):
                        countyGym = getLocGym(county)
                        areaSet.add(countyGym)
            resultDICT["func_loc"] = "台灣的"+args[0]+"有"+ str(areaSet)
        elif "抱石" in arg[1]:
            if hasBoulderGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[1]+"有"+getLocBTSGym(args[0],1)
            else:
                resultDICT["func_loc"] = args[0]+"沒有"+args[1]+"哦！"
        elif arg[1] in userDefinedDICT["_climbingTop"]:
            if hasTopGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[1]+"有"+getLocBTSGym(args[0],2)
            else:
                resultDICT["func_loc"] = args[0]+"沒有"+args[1]+"哦！"
        elif arg[1] in userDefinedDICT["_climbingSpeed"]:
            if hasTopGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[1]+"有"+getLocBTSGym(args[0],3)
            else:
                resultDICT["func_loc"] = args[0]+"沒有"+args[1]+"哦！"
        elif arg[1] in userDefinedDICT["_climbingGym"]:
            if hasGymCounty(args[0]):
                resultDICT["func_loc"] = args[0]+"的"+args[1]+"有"+getLocGym(args[0])
        else:
            resultDICT["func_loc"] = args[0]+'沒有岩館哦！'
        pass

    if utterance == "離[我][近]的[岩館]有[比較]推薦的嗎":
        if args[2] not in userDefinedDICT["climbingGym"]:
            resultDICT["func_loc"] = "攀岩以外不在我的能力範圍內，麻煩重新查詢~"
        else:
            resultDICT["func_loc"] = "請問你在哪裡呢？可以給我大概地理位置嗎？"
        pass

    return resultDICT