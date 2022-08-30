import re
import json
import logging
import pandas as pd
import random

extendedDICT = {"_taiwanCities":["雲林","嘉義","台南","高雄","屏東","花蓮","台東","基隆","台北","桃園","新竹","宜蘭","新北","苗栗","台中","彰化","南投","蘭嶼","綠島","金門","馬祖","龜山島","離島"],"_midTW":["苗栗","台中","彰化","南投"],"_eastTW":["花蓮","台東"],"_northTW":["基隆","台北","桃園","新竹","宜蘭","新北"],"_southTW":["雲林","嘉義","台南","高雄","屏東"],"_islandsTW":["離島","金門","馬祖","澎湖","龜山島"]}
gymsInfo = pd.read_csv('data/climbingGym.csv', encoding = 'utf-8')


 #取得岩館位置或電話
def getGymLocPh(gym, c_a_p):
    lpDict = {}
    if gym == "double8":
        gym = "double 8"
    elif gym == "camp4" or gym == "Camp4" or gym == "camp 4":
        gym = "Camp 4"
    elif gym == "角岩館":
        gym = "角·攀岩館"
    if c_a_p == "c":
        for i in range(len(gymsInfo)):
            if gym in gymsInfo.iloc[i, 0]:
                lpDict[gymsInfo.iloc[i, 0]] = gymsInfo.iloc[i, 2][:2]
    elif c_a_p == "a":
        for i in range(len(gymsInfo)):
            if gym in gymsInfo.iloc[i, 0]:
                lpDict[gymsInfo.iloc[i, 0]] = gymsInfo.iloc[i, 2]
    elif c_a_p == "p":
        for i in range(len(gymsInfo)):
            if gym in gymsInfo.iloc[i, 0]:
                lpDict[gymsInfo.iloc[i, 0]] = gymsInfo.iloc[i, 1]
    return lpDict

 #取得有岩館的縣市
def gymCountySet():
    countySet = set()
    for i in range(len(gymsInfo)):
        countySet.add(gymsInfo.iloc[i,2][:2])
    return countySet

#取得有指定岩館的縣市
def getBTScity(bts):
    citySet = set()
    if "抱石" in bts:
        for i in range(len(gymsInfo)):
            if gymsInfo.iloc[i, 3] == 1:
                citySet.add(gymsInfo.iloc[i, 2][:2])
    elif "上攀" in bts or "先鋒" in bts:
        for i in range(len(gymsInfo)):
            if gymsInfo.iloc[i, 4] == 1:
                citySet.add(gymsInfo.iloc[i, 2][:2])
    elif "速度" in bts:
        for i in range(len(gymsInfo)):
            if gymsInfo.iloc[i, 5] == 1:
                citySet.add(gymsInfo.iloc[i, 2][:2])  
    return citySet  

#取得岩館票價
def getGymPrice(gym):
    gymPriceDict = {} 
    if gym == "double8":
        gym = "double 8"
    elif gym == "camp4" or gym == "Camp4" or gym == "camp 4":
        gym = "Camp 4"
    elif gym == "角岩館":
        gym = "角·攀岩館"
    for i in range(len(gymsInfo)):
        if gym in gymsInfo.iloc[i, 0]:
            gymPriceList = []
            for j in range(6, 10):
                gymPriceList.append(gymsInfo.iloc[i, j])
            gymPriceDict[gymsInfo.iloc[i, 0]] = gymPriceList
    return gymPriceDict

def priceToString(priceDict):
    string = ""
    print("-----priceDict:",priceDict,"-----")
    for gym, prices in priceDict.items():
        string += gym + ":\n"
        if prices[0] != "n.a.":
            string += "\t平日票價 "+ str(prices[0]) + "\n"
        if prices[1] != "n.a.":
            string += "\t假日票價 "+ str(prices[1]) + "\n"
        if prices[2] != "n.a.":
            string += "\t星光票 "+ str(prices[2]) + "\n"
        if prices[3] != "n.a.":
            string += "\t時票 "+ str(prices[3]) + "\n"
        string += "\n"
    return string

#取得Ｘ縣市的抱石、上攀、速度或一般岩館名稱
def getLocBTSGym(county, bts): 
    locGymSet = set()
    if "抱石" in bts:
        for i in range(len(gymsInfo)):
            if county in gymsInfo.iloc[i,2] and gymsInfo.iloc[i, 3] == 1:
                locGymSet.add(gymsInfo.iloc[i, 0])
    elif "上攀" in bts or "先鋒" in bts:
        for i in range(len(gymsInfo)):
            if county in gymsInfo.iloc[i,2] and gymsInfo.iloc[i, 4] == 1:
                locGymSet.add(gymsInfo.iloc[i, 0])
    elif "速度" in bts:
        for i in range(len(gymsInfo)):
            if county in gymsInfo.iloc[i,2] and gymsInfo.iloc[i, 5] == 1:
                locGymSet.add(gymsInfo.iloc[i, 0])
    else:
        for i in range(len(gymsInfo)):
            if county in gymsInfo.iloc[i,2]:
                locGymSet.add(gymsInfo.iloc[i, 0])
    return locGymSet

#取得Ｘ縣市有無指定岩館
def hasGymCounty(county, bts):
    if "抱石" in bts:
        for i in range(len(gymsInfo)):
            if county in gymsInfo.iloc[i, 2] and gymsInfo.iloc[i, 3] == 1:
                return True
    elif "上攀" in bts or "先鋒" in bts:
        for i in range(len(gymsInfo)):
            if county in gymsInfo.iloc[i, 2] and gymsInfo.iloc[i, 4] == 1:
                return True
    elif "速度" in bts:
        for i in range(len(gymsInfo)):
            if county in gymsInfo.iloc[i,2] and gymsInfo.iloc[i, 5] == 1:
                return True
    else:
        for i in range(len(gymsInfo)):
            if county in gymsInfo.iloc[i,2]:
                return True
    return False

#取得所有抱石、上攀或速度岩館名稱
def getBTSGym(bts): #b = 1, t = 2, s = 3
    GymSet = set()
    if "抱石" in bts:
        for i in range(len(gymsInfo)):
            if gymsInfo.iloc[i, 3] == 1:
                GymSet.add(gymsInfo.iloc[i, 0])
    elif "上攀" in bts or "先鋒" in bts:
        for i in range(len(gymsInfo)):
            if gymsInfo.iloc[i, 4] == 1:
                GymSet.add(gymsInfo.iloc[i, 0])
    elif "速度" in bts:
        for i in range(len(gymsInfo)):
            if gymsInfo.iloc[i, 5] == 1:
                GymSet.add(gymsInfo.iloc[i, 0])
    else:
        GymSet.update(gymsInfo.iloc[:, 0])
    return GymSet

def getSideCounties(side):
    counties = []
    if side == "中部":
        counties = extendedDICT["_midTW"]
    elif side == "北部":
        counties = extendedDICT["_northTW"]
    elif side == "南部":
        counties = extendedDICT["_southTW"]
    elif side == "東部":
        counties = extendedDICT["_eastTW"]
    else:
        counties = extendedDICT["_taiwanCities"]
        counties.remove("花蓮","台東")
    return counties

def containerToString(container):
    conlen = len(container)
    c = 1
    string = ""
    for i in container:
        if c != conlen:
            string += "「" + i + "」, "
            c += 1
        else:
            string += "「" + i + "」"
    return string

def getGymDistrict(city, bts):
    districtSet = set()
    if "抱石" in bts:
        for i in range(len(gymsInfo)):
            if city in gymsInfo.iloc[2] and gymsInfo.iloc[3] == 1:
                districtSet.add(gymsInfo.iloc[2][3:5])
    elif "上攀" in bts or "先鋒" in bts:
        for i in range(len(gymsInfo)):
            if city in gymsInfo.iloc[2] and gymsInfo.iloc[4] == 1:
                districtSet.add(gymsInfo.iloc[2][3:5])
    elif "速度":
        for i in range(len(gymsInfo)):
            if city in gymsInfo.iloc[2] and gymsInfo.iloc[5] == 1:
                districtSet.add(gymsInfo.iloc[2][3:5])
    else:
        for i in range(len(gymsInfo)):
            if city in gymsInfo.iloc[2]:
                districtSet.add(gymsInfo.iloc[2][3:5])
    return districtSet

def countAllGym(gym):
    count = 0
    if "抱石" in gym:
        for i in range(len(gymsInfo)):
            if gymsInfo.iloc[i,3] == 1:
                count += 1
    elif "上攀" in gym or "先鋒" in gym:
        for i in range(len(gymsInfo)):
            if gymsInfo.iloc[i,4] == 1:
                count += 1
    elif "速度" in gym:
        for i in range(len(gymsInfo)):
            if gymsInfo.iloc[i,5] == 1:
                count += 1
    else:
        count = len(gymsInfo)
    return count

#取得Ｘ縣市的岩館數量
def countLocGym(county, gym):
    count = 0
    if "抱石" in gym:
        for i in range(len(gymsInfo)):
            if county in gymsInfo.iloc[i,2] and gymsInfo.iloc[i,3] == 1:
                count += 1
    elif "上攀" in gym or "先鋒" in gym:
        for i in range(len(gymsInfo)):
            if county in gymsInfo.iloc[i,2] and gymsInfo.iloc[i,4] == 1:
                count += 1
    elif "速度" in gym:
        for i in range(len(gymsInfo)):
            if county in gymsInfo.iloc[i,2] and gymsInfo.iloc[i,5] == 1:
                count += 1
    else:
        for i in range(len(gymsInfo)):
            if county in gymsInfo.iloc[i,2]:
                count += 1
    return count

def checkLocation(inputSTR):
    if inputSTR == "臺中":
        inputSTR = "台中"
    elif inputSTR == "臺北":
        inputSTR = "台北"
    elif inputSTR == "臺南":
        inputSTR = "台南"
    if inputSTR[:2] in extendedDICT["_taiwanCities"]:
        return True
    return False

def checkGymBTS(gym, bts):
    if "抱石" in bts:
        for i in range(len(gymsInfo)):
            if gym in gymsInfo.iloc[i, 0] and gymsInfo.iloc[i, 3] == 1:
                return True
    elif "上攀" in bts or "先鋒" in bts:
        for i in range(len(gymsInfo)):
            if gym in gymsInfo.iloc[i, 0] and gymsInfo.iloc[i, 4] == 1:
                return True
    elif "速度" in bts:
        for i in range(len(gymsInfo)):
            if gym in gymsInfo.iloc[i, 0] and gymsInfo.iloc[i, 5] == 1:
                return True
    return False

def checkGymLoc(gym, loc):
    for i in range(len(gymsInfo)):
        if gym in gymsInfo.iloc[i, 0] and loc in gymsInfo.iloc[i, 2]:
            return True
    return False 



