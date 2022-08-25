import re
import json
import logging
import pandas as pd
import random

 #取得岩館位置或電話
def getGymLocPh(gym, c_a_p):
    lpDict = {}
    if gym == "double8":
        gym = "double 8"
    elif gym == "camp4" or gym == "Camp4" or gym == "camp 4":
        gym = "Camp 4"
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

    for i in range(len(gymsInfo)):
        if gym in gymsInfo.iloc[i, 0]:
            gymPriceList = []
        for j in range(7, 10):
            gymPriceList.append(gymsInfo.iloc[i, j])
        gymPriceDict[gymsInfo.iloc[i, 0]] = gymPriceList
    return gymPriceDict

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

#def intentFilter(inputSTR):   
#if __name__ == "__main__":


