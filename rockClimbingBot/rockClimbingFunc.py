import re
import json
import logging
import pandas as pd
import random

extendedDICT = {"_taiwanCities":["雲林","嘉義","台南","高雄","屏東","花蓮","台東","基隆","台北","桃園","新竹","宜蘭","新北","苗栗","台中","彰化","南投","蘭嶼","綠島","金門","馬祖","龜山島","離島"],"_midTW":["苗栗","台中","彰化","南投"],"_eastTW":["花蓮","台東"],"_northTW":["基隆","台北","桃園","新竹","宜蘭","新北"],"_southTW":["雲林","嘉義","台南","高雄","屏東"],"_islandsTW":["離島","金門","馬祖","澎湖","龜山島"]}
gymsInfo = pd.read_csv('data/climbingGym.csv', encoding = 'utf-8')
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_rocks":["岩石","岩點","手點","石頭","點"],"_shoes":["岩鞋","抱石鞋","鞋子","攀岩鞋","攀岩鞋子"],"_sides":["中部","北部","南部","東部","西部"],"_whatIs":["星光票"],"_climbing":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石","抱石攀岩","速度攀","速度攀登","攀登","運動攀登"],"_cityAlias":["區域","地區","城市","縣市","都市","地方"],"_gymsShort":["達文西","8a攀岩場","B-plus","Boulder Space","Camp 4","Corner","Dapro","K2","MegaSTONE","POGO","TheDepotCity","Up聯盟","Y17","double 8","double8","久淘","千手抱石","原岩","嗨翻","嘉義攀岩會館","圓石","圓石空間","宜蘭運動中心","小岩館","崩岩","抱石基地","攀吶","新竹紅石","水美iClimb","汐止抱石館","爬森","破舊二廠","破舊工廠","禾匠","紅石","艾思博","蕃薯藤","角岩館","風城"],"_peClothes":["單車褲","瑜珈褲","運動服","運動衣","運動褲","運動鞋","攀岩褲"],"_rockTypes":["crimp","edge","flat","horn","jug","pinch","pocket","sloper","volume"],"_climbingGym":["岩場","岩館","攀岩場","攀岩館","抱石館","上攀館"],"_taiwanAlias":["全台","全台各地","全臺","全臺各地","台灣","臺灣","全台灣"],"_clothesPants":["上衣","服裝","短袖","短袖上衣","短袖衣服","衣服","衣著","衣褲","長袖","長袖上衣","長袖衣服","單車褲","瑜珈褲","短褲","運動褲","長褲"],"_climbingEquip":["岩粉","岩點刷","攀岩刷","攀岩粉","攀岩粉袋","止滑粉","碳酸鎂粉","粉球","粉袋","裝","裝備","鎂粉","鎂粉球"],"_topRopingEquip":["吊帶","垂降手套","安全吊帶","安全扣","安全扣環","快扣","手套","確保器","確保手套","耐磨手套"]}

#取得岩館位置或電話
def getGymLocPh(gym, c_a_p):
    lpDict = {}
    if gym == "double8":
        gym = "double 8"
    elif gym == "camp4" or gym == "Camp4" or gym == "camp 4":
        gym = "Camp 4"
    elif gym == "角岩館":
        gym = "角·攀岩館"
    elif gym == "pogo":
        gym = "POGO"    
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
    elif c_a_p == "pa":
        for i in range(len(gymsInfo)):
            paList = []
            if gym in gymsInfo.iloc[i, 0]:
                paList.append(gymsInfo.iloc[i, 1])
                paList.append(gymsInfo.iloc[i, 2])
                lpDict[gymsInfo.iloc[i, 0]] = paList   
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

def getGymTime(gym):
    gymTimeDict = {} 
    if gym == "double8":
        gym = "double 8"
    elif gym == "camp4" or gym == "Camp4" or gym == "camp 4":
        gym = "Camp 4"
    elif gym == "角岩館":
        gym = "角·攀岩館"
    elif gym == "pogo":
        gym = "POGO"      
    for i in range(len(gymsInfo)):
        if gym in gymsInfo.iloc[i, 0]:
            gymTimeList = []
            for j in range(13, 15):
                gymTimeList.append(gymsInfo.iloc[i, j])
            gymTimeDict[gymsInfo.iloc[i, 0]] = gymTimeList
    return gymTimeDict

def timeToString(timeDict, daySTR):
    string = ""
    if "平日" in daySTR:
        for gym, time in timeDict.items():
            if time[0] != "n.a.":
                string += gym + "平日營業時間是" +time[0] + "\n"
            else:
                string += gym + "平日不營業哦"
    elif "假日" in daySTR:
        for gym, time in timeDict.items():
            if time[0] != "n.a.":
                string += gym + "假日營業時間是" +time[0] + "\n"
            else:
                string += gym + "假日不營業哦"
    #elif "今天" in daySTR or "今日" in daySTR:
    else:
        for gym, time in timeDict.items():
            if time[0] == "預約制":
                string += gym + "採預約制，如想至"+gym+"攀岩請先預約"
            else:
                string += gym + ":\n"
                if time[0] != "n.a.":
                    string += "\t平日營業時間 " +time[0] + "\n"
                else:
                    string += "\t平日不營業"
                if time[1] != "n.a.":
                    string += "\t假日營業時間 " +time[1] + "\n"
                else:
                    string += "\t假日不營業"
    return string

#取得岩館票價
def getGymPrice(gym):
    gymPriceDict = {} 
    if gym == "double8":
        gym = "double 8"
    elif gym == "camp4" or gym == "Camp4" or gym == "camp 4":
        gym = "Camp 4"
    elif gym == "角岩館":
        gym = "角·攀岩館"
    elif gym == "pogo":
        gym = "POGO"      
    for i in range(len(gymsInfo)):
        if gym in gymsInfo.iloc[i, 0]:
            gymPriceList = []
            for j in range(6, 10):
                gymPriceList.append(gymsInfo.iloc[i, j])
            gymPriceDict[gymsInfo.iloc[i, 0]] = gymPriceList
    return gymPriceDict

def priceToString(priceDict):
    string = ""
    #print("-----priceDict:",priceDict,"-----")
    for gym, prices in priceDict.items():
        string += gym + "：\n"
        if prices[0] != "n.a.":
            string += "\t平日單日票價 "+ str(prices[0]) + "\n"
        if prices[1] != "n.a.":
            string += "\t假日單日票價 "+ str(prices[1]) + "\n"
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

def containerToString1(container):
    conlen = len(container)
    c = 1
    string = ""
    for i in container:
        if c != conlen:
            string += i + ", "
            c += 1
        else:
            string += i 
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

def checkGymInString(inputSTR):
    theGym = ""
    for i in userDefinedDICT["_gymsShort"]:
        if i in inputSTR:
            theGym = i
            return theGym
    return ""

def checkGymCity(gym, city):
    for i in range(len(gymsInfo)):
        if gym in gymsInfo.iloc[i, 0]:
            if city in gymsInfo.iloc[i, 2]:
                return True
    return False

