#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for gym_distance

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

#_gym_name, gym_distance, _person_loc, _msg_received

import json
import os
import pandas as pd
import random

DEBUG_gym_distance = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_pants":["單車褲","瑜珈褲","短褲","運動褲"],"_rocks":["岩石","岩點","手點","攀岩鞋","攀岩鞋子","石頭","點"],"_shoes":["岩鞋","抱石鞋","鞋子"],"_sides":["中部","北部","南部","東部","西部"],"_tmpFix":["規則"],"_whatIs":["星光票"],"_clothes":["上衣","服裝","短袖","短袖上衣","短袖衣服","衣服","衣著","衣褲","長袖","長袖上衣","長袖衣服"],"_climbing":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石","抱石攀岩","速度攀","速度攀登"],"_cityAlias":["區域","地區","城市","縣市","都市"],"_gymsShort":["8a攀岩場","B-plus","Boulder Space","Camp 4","Corner","Dapro","K2","MegaSTONE","POGO","TheDepotCity","Up聯盟","Y17","double 8","double8","久淘","千手抱石","原岩","嗨翻","嘉義攀岩會館","圓石","圓石空間","宜蘭運動中心","小岩館","崩岩","抱石基地","攀吶","新竹紅石","水美iClimb","汐止抱石館","爬森","破舊二廠","破舊工廠","禾匠","紅石","艾思博","蕃薯藤","角岩館","風城"],"_peClothes":["單車褲","瑜珈褲","運動服","運動衣","運動褲","運動鞋"],"_rockTypes":["crimp","edge","flat","horn","jug","pinch","pocket","sloper","volume"],"_climbingGym":["岩場","岩館","攀岩場","攀岩館"],"_taiwanAlias":["全台","全台各地","全臺","全臺各地","台灣","臺灣"],"_climbingEquip":["岩粉","岩點刷","攀岩刷","攀岩粉","攀岩粉袋","止滑粉","碳酸鎂粉","粉球","粉袋","裝","裝備","鎂粉","鎂粉球"],"_topRopingEquip":["吊帶","垂降手套","安全吊帶","安全扣","安全扣環","快扣","手套","確保器","確保手套","耐磨手套"]}

gymsInfo = pd.read_csv('data/climbingGym.csv', encoding = 'utf-8')
extendedDICT = {"_taiwanCities":["雲林","嘉義","台南","高雄","屏東","花蓮","台東","基隆","台北","桃園","新竹","宜蘭","新北","苗栗","台中","彰化","南投","蘭嶼","綠島","金門","馬祖","龜山島","離島"],"_midTW":["苗栗","台中","彰化","南投"],"_eastTW":["花蓮","台東"],"_northTW":["基隆","台北","桃園","新竹","宜蘭","新北"],"_southTW":["雲林","嘉義","台南","高雄","屏東"],"_islandsTW":["離島","金門","馬祖","澎湖","龜山島"]}
defaultResponse = json.load(open("data/defaultResponse.json",encoding="utf-8"))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_gym_distance:
        print("[gym_distance] {} ===> {}".format(inputSTR, utterance))

#取得Ｘ縣市的抱石、上攀或速度岩館名稱
def getLocBTSGym(county, bts): #b = 1, t = 2, s = 3
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

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[上攀][可以]去哪裡":
        if args[0] in userDefinedDICT["_climbing"]:
            if resultDICT["_person_loc"] != []: #bot 知道人在哪裡
                resultDICT["_gym_name"] = getLocBTSGym(resultDICT["_person_loc"], args[0])
            else:                               #bot 不知道人在哪裡
                resultDICT["_person_loc"] = None
        else:
            resultDICT["_gym_distance"] = random.choice(defaultResponse["_not_rock_climbing"])#defaultResponse["_not_rock_climbing"][random.randint(1,4)]   

    if utterance == "[我]在[台中]":
        if args[0][0] in ("我", "咱"):
            resultDICT["_person_loc"] = args[1]
            resultDICT["_msg_received"] = random.choice(defaultResponse["_msg_received"])

    if utterance == "[我]在[東部]":
        if args[0][0] in ("我", "咱"):
            resultDICT["_person_loc"] = args[1]
            resultDICT["_msg_received"] = random.choice(defaultResponse["_msg_received"])#defaultResponse["_msg_received"][random.choice("_msg_received")]

    if utterance == "[我]在[猩猩縣豬豬市悟淨路141號]":
        if args[0][0] in ("我", "咱"):
            resultDICT["_person_loc"] = args[1]
            resultDICT["_msg_received"] = random.choice(defaultResponse["_msg_received"])

    if utterance == "哪裡[可以][上攀]":
        if args[1] in userDefinedDICT["_climbing"]:
            if resultDICT["_person_loc"] != []: #bot 知道人在哪裡
                resultDICT["_gym_name"] = getLocBTSGym(resultDICT["_person_loc"], args[1])
            else:                               #bot 不知道人在哪裡
                resultDICT["_person_loc"] = None
        else:
            resultDICT["_gym_distance"] = random.choice(defaultResponse["_not_rock_climbing"])        

    if utterance == "哪裡[可以]攀岩":
        if resultDICT["_person_loc"] != []: #bot 知道人在哪裡
            resultDICT["_gym_name"] = getLocBTSGym(resultDICT["_person_loc"], "")
        else:                               #bot 不知道人在哪裡
            resultDICT["_person_loc"] = None

    if utterance == "哪間[岩館]離[我][最近]":
        # write your code here
        pass

    if utterance == "想[抱石][可以]去哪裡":
        if args[0] in userDefinedDICT["_climbing"]:
            if resultDICT["_person_loc"] != []: #bot 知道人在哪裡
                resultDICT["_gym_name"] = getLocBTSGym(resultDICT["_person_loc"], args[0])
            else:                               #bot 不知道人在哪裡
                resultDICT["_person_loc"] = None
        else:
            resultDICT["_gym_distance"] = random.choice(defaultResponse["_not_rock_climbing"]) 

    if utterance == "想攀[先鋒攀][可以]去哪":
        if args[0] in userDefinedDICT["_climbing"]:
            if resultDICT["_person_loc"] != []: #bot 知道人在哪裡
                resultDICT["_gym_name"] = getLocBTSGym(resultDICT["_person_loc"], args[0])
            else:                               #bot 不知道人在哪裡
                resultDICT["_person_loc"] = None
        else:
            resultDICT["_gym_distance"] = random.choice(defaultResponse["_not_rock_climbing"])

    if utterance == "想攀岩[可以]去哪":
        if resultDICT["_person_loc"] != []: #bot 知道人在哪裡
            resultDICT["_gym_name"] = getLocBTSGym(resultDICT["_person_loc"], args[0])
        else:                               #bot 不知道人在哪裡
            resultDICT["_person_loc"] = None

    if utterance == "推薦[一些]距離[近]的[岩館]":
        # write your code here
        pass

    if utterance == "推薦哪些距離[近]的[岩館]":
        # write your code here
        pass

    if utterance == "推薦幾[間]距離[近]的[岩館]":
        # write your code here
        pass

    if utterance == "攀岩[可以]去哪裡":
        if resultDICT["_person_loc"] != []: #bot 知道人在哪裡
            resultDICT["_gym_name"] = getLocBTSGym(resultDICT["_person_loc"], args[0])
        else:                               #bot 不知道人在哪裡
            resultDICT["_person_loc"] = None

    if utterance == "有哪些[岩館]呢":
        if args[0] not in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_distance"] = random.choice(defaultResponse["_not_rock_climbing"]) 
            return resultDICT
        if resultDICT["_person_loc"] != []: #bot 知道人在哪裡
            resultDICT["_gym_name"] = getLocBTSGym(resultDICT["_person_loc"], args[0])
        else:                               #bot 不知道人在哪裡
            resultDICT["_person_loc"] = None

    if utterance == "有推薦的[岩館][麻]":
        if args[0] not in userDefinedDICT["_climbingGym"]:
            resultDICT["_gym_distance"] = random.choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if resultDICT["_person_loc"] != []: #bot 知道人在哪裡
            resultDICT["_gym_name"] = getLocBTSGym(resultDICT["_person_loc"], args[0])
        else:                               #bot 不知道人在哪裡
            resultDICT["_person_loc"] = None

    if utterance == "比較近的[岩館]有哪些":
        # write your code here
        pass

    if utterance == "要[抱石][可以]去哪裡":
        if args[0] in userDefinedDICT["_climbing"]:
            if resultDICT["_person_loc"] != []: #bot 知道人在哪裡
                resultDICT["_gym_name"] = getLocBTSGym(resultDICT["_person_loc"], args[0])
            else:                               #bot 不知道人在哪裡
                resultDICT["_person_loc"] = None
        else:
            resultDICT["_gym_distance"] = random.choice(defaultResponse["_not_rock_climbing"]) 

    if utterance == "離[我][最近]的[岩館]是哪間":
        # write your code here
        pass

    if utterance == "離[我][最近]的[岩館]有哪些":
        # write your code here
        pass

    if utterance == "離[我][近]的[岩館]有[比較]推薦的嗎":
        # write your code here
        pass

    if utterance == "離我[媽][最近]的[岩館]有哪些":
        # write your code here
        pass

    if utterance == "離我[家][最近]的[岩館]是哪間":
        # write your code here
        pass

    if utterance == "哪裡有[速度攀]":
        # write your code here
        pass

    if utterance == "推薦[一些][距離][近]的[岩館]":
        # write your code here
        pass

    if utterance == "推薦哪些[距離][近]的[岩館]":
        # write your code here
        pass

    if utterance == "推薦幾[間][距離][近]的[岩館]":
        # write your code here
        pass

    return resultDICT