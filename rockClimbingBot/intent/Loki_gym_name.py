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
import pandas as pd

DEBUG_gym_name = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "data/USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_can":["可以","可","適合"],"_pants":["褲子","褲","長褲","短褲","運動褲","瑜珈褲","單車褲"],"_rocks":["岩點","石頭","手點","點","岩石","攀岩鞋","攀岩鞋子"],"_shoes":["岩鞋","鞋子","抱石鞋","鞋"],"_sides":["東部","北部","南部","西部","中部"],"_levels":["難度","等級","階級","級數"],"_whatIs":["星光票"],"_clothes":["衣服","長袖","短袖","衣著","服裝","長袖衣服","上衣","短袖衣服","長袖上衣","短袖上衣","衣褲"],"_climbing":["上攀","速度攀","速度攀登","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石攀岩","抱石"],"_cityAlias":["縣市","縣","市","地區","都市","城市","區","區域"],"_gymsShort":["紅石","小岩館","Camp 4","角岩館","Corner","汐止抱石館","double8","double 8","原岩","Up聯盟","MegaSTONE","POGO","爬森","蕃薯藤","千手抱石","水美iClimb","風城","B-plus","新竹紅石","TheDepotCity","攀吶","Dapro","破舊二廠","破舊工廠","嗨翻","抱石基地","圓石","圓石空間","Boulder Space","K2","艾思博","禾匠","崩岩","久淘","宜蘭運動中心","嘉義攀岩會館","8a攀岩場","Y17"],"_peClothes":["運動衣","運動褲","運動服","瑜珈褲","單車褲"],"_rockTypes":["jug","pinch","sloper","edge","crimp","pocket","flat","horn","volume"],"_climbingGym":["岩館","攀岩館","攀岩場","抱石館","抱石場館","抱石場","岩場","上攀館","上攀場","上攀場館","攀石場","上攀場館","上攀岩館","先鋒攀岩館","速度攀岩館","速度攀登場館","速度攀場館","速度攀登岩館","速度攀場地"],"_taiwanAlias":["全台","全臺","全台各地","台灣","臺灣","全臺各地"],"_climbingEquip":["裝","裝備","岩粉","粉袋","攀岩粉袋","粉球","止滑粉","攀岩粉","攀岩粉袋","岩點刷","攀岩刷","鎂粉球","鎂粉","碳酸鎂粉"],"_normalWearings":["一般運動鞋","牛仔褲"],"_topRopingEquip":["手套","確保手套","垂降手套","耐磨手套","安全吊帶","確保器","安全扣","快扣","安全扣環","吊帶"],"_climbingGeneralGym":["岩館","攀岩館","攀岩場","攀岩場館"]}

gymsInfo = pd.read_csv('data/climbingGym.csv', encoding = 'utf-8')
extendedDICT = {"_taiwanCities":["雲林","嘉義","台南","高雄","屏東","花蓮","台東","基隆","台北","桃園","新竹","宜蘭","新北","苗栗","台中","彰化","南投","蘭嶼","綠島","金門","馬祖","龜山島"],"_midTW":["苗栗","台中","彰化","南投"],"_eastTW":["花蓮","台東"],"_northTW":["基隆","台北","桃園","新竹","宜蘭","新北"],"_southTW":["雲林","嘉義","台南","高雄","屏東"]}
defaultResponse = json.load("data/defaultResponse.json",encoding = "utf-8")
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_gym_name:
        print("[gym_name] {} ===> {}".format(inputSTR, utterance))

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

#取得所有抱石、上攀或速度岩館名稱   
def getBTSGym(bts): #b = 1, t = 2, s = 3
    GymSet = set()
    if bts == 1:
        for i in range(len(gyms)):
            if gymsInfo.iloc[i, 3] == 1:
                GymSet.add(gymsInfo.iloc[i, 0])
    elif bts == 2:
        for i in range(len(gyms)):
            if gymsInfo.iloc[i, 4] == 1:
                GymSet.add(gymsInfo.iloc[i, 0]) 
    else:
        for i in range(len(gyms)):
            if gymsInfo.iloc[i, 5] == 1:
                GymSet.add(gymsInfo.iloc[i, 0]) 
    return str(GymSet)

def checkLocation(inputSTR):
    if inputSTR[:2] in extendedDICT["_taiwanCities"]:
        return inputSTR[:2]
    return

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[中部][岩館]有哪些":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_name"] = defaultResponse["_not_rock_climbing"][random.randint(1,4)]
            pass
        areaSet = set()
        if args[0] in userDefinedDICT["_sides"]:
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
                    gyms = getLocBTSGym(county, 1)
                    areaSet.update(gyms)
            elif "上攀" in args[1] or "先鋒" in args[1] :
                for county in counties:
                    gyms = getLocBTSGym(county, 2)
                    areaSet.update(gyms)
            elif "速度" in args[1]:
                for county in counties:
                    gyms = getLocBTSGym(county, 3)
                    areaSet.update(gyms)
            else:
                for county in counties:
                    gyms = getLocGym(county)
                    areaSet.update(gyms)
            if len(areaSet) > 0:
                resultDICT["_gym_howMany"] = "{0}的{1}有{2}".format(args[0], args[1], str(areaSet))
            else:
                resultDICT["_gym_howMany"] = "{}沒有岩館哦！".format(args[0])
        elif len(checkLocation(inputSTR)) > 0:
            county = checkLocation(inputSTR)
            if "抱石" in args[1]:
                areaSet = getLocBTSGym(county, 1)
            elif "上攀" in args[1] or "先鋒" in args[1]:
                areaSet = getLocBTSGym(county, 2)
            elif "速度" in args[1]:
                areaSet = getLocBTSGym(county, 3)
            else:
                areaSet = getLocGym(county)        
            if len(areaSet) > 0:
                resultDICT["_gym_name"] = "{0}的{1}有{2}".format(county, args[1],str(areaSet))
            else:
                resultDICT["_gym_name"] = "{}沒有岩館哦！".format(county)
        else:
           resultDICT["_gym_howMany"] = defaultResponse["_not_taiwan_city"][random.randint(1,4)] 
        pass

    if utterance == "[台中][上攀][可以]去哪裡":
        if args[1] not in userDefinedDICT["_climbing"]:
            resultDICT["_gym_name"] = defaultResponse["_not_rock_climbing"][random.randint(1,4)]
            pass
        if len(checkLocation(arg[0])) > 0:
            areaSet = set()
            if "抱石" in args[1]:
                areaSet = getLocBTSGym(arg[0], 1)
            elif "上攀" in args[1] or "先鋒" in args[1]:
                areaSet = getLocBTSGym(arg[0], 2)
            elif "速度" in args[1]:
                areaSet = getLocBTSGym(arg[0], 3)
            else:
                areaSet = getLocGym(arg[0])        
            if len(areaSet) > 0:
                resultDICT["_gym_name"] = "{0}想{1}可以去{2}".format(arg[0], arg[1],str(areaSet))
            else:
                resultDICT["_gym_name"] = "{}沒有岩館哦！".format(arg[0])
        else:
           resultDICT["_gym_name"] = defaultResponse["_not_taiwan_city"][random.randint(1,4)] 
        pass

    if utterance == "[台中][岩館]有哪些":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_name"] = defaultResponse["_not_rock_climbing"][random.randint(1,4)]
            pass
        if len(checkLocation(arg[0])) > 0:
            areaSet = set()
            if "抱石" in args[1]:
                areaSet = getLocBTSGym(arg[0], 1)
            elif "上攀" in args[1] or "先鋒" in args[1]:
                areaSet = getLocBTSGym(arg[0], 2)
            elif "速度" in args[1]:
                areaSet = getLocBTSGym(arg[0], 3)
            else:
                gyms = getLocGym(arg[0])
                areaSet.add(gyms)           
            if len(areaSet) > 0:
                resultDICT["_gym_name"] = "{0}的{1}有{2}".format(arg[0], arg[1],str(areaSet))
            else:
                resultDICT["_gym_name"] = "{}沒有岩館哦！".format(arg[0])
        else:
           resultDICT["_gym_name"] = defaultResponse["_not_taiwan_city"][random.randint(1,4)] 
        pass

    if utterance == "[台中]攀岩[可以]去哪裡":
        if len(checkLocation(arg[0])) > 0:
            areaSet = getLocGym(arg[0])
            if len(areaSet) > 0:
                resultDICT["_gym_name"] = "{0}想攀岩可以去{2}".format(arg[0], str(areaSet))
            else:
                resultDICT["_gym_name"] = "{}沒有岩館哦！".format(arg[0])
        else:
            resultDICT["_gym_name"] = defaultResponse["_not_taiwan_city"][random.randint(1,4)] 
        pass

    if utterance == "[台中]有哪些[岩館]":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_name"] = defaultResponse["_not_rock_climbing"][random.randint(1,4)]
            pass
        if len(checkLocation(arg[0])) > 0:
            areaSet = set()
            if "抱石" in args[1]:
                areaSet = getLocBTSGym(arg[0], 1)
            elif "上攀" in args[1] or "先鋒" in args[1]:
                areaSet = getLocBTSGym(arg[0], 2)
            elif "速度" in args[1]:
                areaSet = getLocBTSGym(arg[0], 3)
            else:
                gyms = getLocGym(arg[0])
                areaSet.add(gyms)           
            if len(areaSet) > 0:
                resultDICT["_gym_name"] = "{0}的{1}有{2}".format(arg[0], arg[1],str(areaSet))
            else:
                resultDICT["_gym_name"] = "{}沒有岩館哦！".format(arg[0])
        else:
           resultDICT["_gym_name"] = defaultResponse["_not_taiwan_city"][random.randint(1,4)] 
        pass

    if utterance == "[台北]哪些[岩館][可以][抱石]":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_name"] = defaultResponse["_not_rock_climbing"][random.randint(1,4)]
            pass
        if len(checkLocation(arg[3])) > 0:
            areaSet = set()
            if "抱石" in args[3]:
                areaSet = getLocBTSGym(arg[0], 1)
            elif "上攀" in args[3] or "先鋒" in args[3]:
                areaSet = getLocBTSGym(arg[0], 2)
            elif "速度" in args[3]:
                areaSet = getLocBTSGym(arg[0], 3)
            else:
                resultDICT["_gym_name"] = "攀岩沒有{}項目哦！".format(args[3])
                pass        
            if len(areaSet) > 0:
                resultDICT["_gym_name"] = "{0}的{3}{1}有{2}".format(arg[0], arg[1],str(areaSet),args[3])
            else:
                resultDICT["_gym_name"] = "{0}沒有岩館可以{1}哦！".format(arg[0],args[3])
        else:
           resultDICT["_gym_name"] = defaultResponse["_not_taiwan_city"][random.randint(1,4)] 
        pass

    if utterance == "[台北]哪裡[可以][抱石]":
        if args[2] not in userDefinedDICT["_climbing"]:
            resultDICT["_gym_name"] = defaultResponse["_not_rock_climbing"][random.randint(1,4)]
            pass
        if len(checkLocation(arg[0])) > 0:
            areaSet = set()
            if "抱石" in args[2]:
                areaSet = getLocBTSGym(arg[0], 1)
            elif "上攀" in args[2] or "先鋒" in args[2]:
                areaSet = getLocBTSGym(arg[0], 2)
            elif "速度" in args[2]:
                areaSet = getLocBTSGym(arg[0], 3)
            else:
                areaSet = getLocGym(arg[0])        
            if len(areaSet) > 0:
                resultDICT["_gym_name"] = "{0}想{1}可以去{2}".format(arg[0], arg[2],str(areaSet))
            else:
                resultDICT["_gym_name"] = "{0}沒有{1}岩館哦！".format(arg[0],args[2])
        else:
           resultDICT["_gym_name"] = defaultResponse["_not_taiwan_city"][random.randint(1,4)] 
        pass

    if utterance == "[台北]哪裡[可以]攀岩":
        if len(checkLocation(arg[0])) > 0:
            areaSet = getLocGym(arg[0])
            if len(areaSet) > 0:
                resultDICT["_gym_name"] = "{0}想攀岩可以去{2}".format(arg[0], str(areaSet))
            else:
                resultDICT["_gym_name"] = "{}沒有岩館哦！".format(arg[0])
        else:
            resultDICT["_gym_name"] = defaultResponse["_not_taiwan_city"][random.randint(1,4)] 
        pass

    if utterance == "[東部]哪些[岩館][可以][抱石]":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_name"] = defaultResponse["_not_rock_climbing"][random.randint(1,4)]
            pass
        areaSet = set()
        if args[0] in userDefinedDICT["_sides"]:
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
            if "抱石" in args[3]:
                for county in counties:
                    gyms = getLocBTSGym(county, 1)
                    areaSet.update(gyms)
            elif "上攀" in args[3] or "先鋒" in args[3] :
                for county in counties:
                    gyms = getLocBTSGym(county, 2)
                    areaSet.update(gyms)
            elif "速度" in args[3]:
                for county in counties:
                    gyms = getLocBTSGym(county, 3)
                    areaSet.update(gyms)
            else:
                resultDICT["_gym_name"] = "攀岩沒有{}項目哦！".format(args[3])
                pass
            if len(areaSet) > 0:
                resultDICT["_gym_howMany"] = "{0}的{1}岩館有{2}".format(args[0], args[1], str(areaSet))
            else:
                resultDICT["_gym_howMany"] = "{}沒有岩館哦！".format(args[0])   
        if len(checkLocation(inputSTR)) > 0:
            areaSet = set()
            if "抱石" in args[3]:
                areaSet = getLocBTSGym(arg[0], 1)
            elif "上攀" in args[3] or "先鋒" in args[3]:
                areaSet = getLocBTSGym(arg[0], 2)
            elif "速度" in args[3]:
                areaSet = getLocBTSGym(arg[0], 3)
            else:
                resultDICT["_gym_name"] = "攀岩沒有{}項目哦！".format(args[3])
                pass        
            if len(areaSet) > 0:
                resultDICT["_gym_name"] = "{0}的{3}{1}有{2}".format(arg[0], arg[1],str(areaSet),args[3])
            else:
                resultDICT["_gym_name"] = "{0}沒有岩館可以{1}哦！".format(arg[0],args[3])
        else:
           resultDICT["_gym_name"] = defaultResponse["_not_taiwan_city"][random.randint(1,4)] 
        pass

    if utterance == "[東部]有哪些[岩館]":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_name"] = defaultResponse["_not_rock_climbing"][random.randint(1,4)]
            pass
        areaSet = set()
        if args[0] in userDefinedDICT["_sides"]:
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
                    gyms = getLocBTSGym(county, 1)
                    areaSet.update(gyms)
            elif "上攀" in args[1] or "先鋒" in args[1] :
                for county in counties:
                    gyms = getLocBTSGym(county, 2)
                    areaSet.update(gyms)
            elif "速度" in args[1]:
                for county in counties:
                    gyms = getLocBTSGym(county, 3)
                    areaSet.update(gyms)
            else:
                for county in counties:
                    gyms = getLocGym(county)
                    areaSet.update(gyms)
            if len(areaSet) > 0:
                resultDICT["_gym_howMany"] = "{0}的{1}有{2}".format(args[0], args[1], str(areaSet))
            else:
                resultDICT["_gym_howMany"] = "{}沒有岩館哦！".format(args[0])
        elif len(checkLocation(inputSTR[])) > 0:
            county = checkLocation(inputSTR[])
            if "抱石" in args[1]:
                areaSet = getLocBTSGym(county, 1)
            elif "上攀" in args[1] or "先鋒" in args[1]:
                areaSet = getLocBTSGym(county, 2)
            elif "速度" in args[1]:
                areaSet = getLocBTSGym(county, 3)
            else:
                areaSet = getLocGym(county)        
            if len(areaSet) > 0:
                resultDICT["_gym_name"] = "{0}的{1}有{2}".format(county, args[1],str(areaSet))
            else:
                resultDICT["_gym_name"] = "{}沒有岩館哦！".format(county)
        else:
           resultDICT["_gym_howMany"] = defaultResponse["_not_taiwan_city"][random.randint(1,4)] 
        pass

    if utterance == "哪幾[間][岩館]有[速度攀]":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_name"] = defaultResponse["_not_rock_climbing"][random.randint(1,4)]
            pass
        if "抱石" in args[2]:
            areaSet = getBTSGym(1)
        elif "上攀" in args[2] or "先鋒" in args[2]:
            areaSet = getBTSGym(2)
        elif "速度" in args[2]:
            areaSet = getBTSGym(3)
        else:
            resultDICT["_gym_name"] = "攀岩沒有{}項目哦！".format(args[2])
        pass

    if utterance == "那[東部]有哪些[岩館]呢":
        if args[1] not in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_name"] = defaultResponse["_not_rock_climbing"][random.randint(1,4)]
            pass
        areaSet = set()
        if args[0] in userDefinedDICT["_sides"]:
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
                    gyms = getLocBTSGym(county, 1)
                    areaSet.update(gyms)
            elif "上攀" in args[1] or "先鋒" in args[1] :
                for county in counties:
                    gyms = getLocBTSGym(county, 2)
                    areaSet.update(gyms)
            elif "速度" in args[1]:
                for county in counties:
                    gyms = getLocBTSGym(county, 3)
                    areaSet.update(gyms)
            else:
                for county in counties:
                    gyms = getLocGym(county)
                    areaSet.update(gyms)
            if len(areaSet) > 0:
                resultDICT["_gym_howMany"] = "{0}的{1}有{2}".format(args[0], args[1], str(areaSet))
            else:
                resultDICT["_gym_howMany"] = "{}沒有岩館哦！".format(args[0])
        elif len(checkLocation(inputSTR[1:])) > 0:
            county = checkLocation(inputSTR[1:])
            if "抱石" in args[1]:
                areaSet = getLocBTSGym(county, 1)
            elif "上攀" in args[1] or "先鋒" in args[1]:
                areaSet = getLocBTSGym(county, 2)
            elif "速度" in args[1]:
                areaSet = getLocBTSGym(county, 3)
            else:
                areaSet = getLocGym(county)        
            if len(areaSet) > 0:
                resultDICT["_gym_name"] = "{0}的{1}有{2}".format(county, args[1],str(areaSet))
            else:
                resultDICT["_gym_name"] = "{}沒有岩館哦！".format(county)
        else:
           resultDICT["_gym_howMany"] = defaultResponse["_not_taiwan_city"][random.randint(1,4)] 
        pass

    return resultDICT