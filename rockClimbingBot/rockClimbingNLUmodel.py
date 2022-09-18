from rockClimbing import runLoki
import json
import logging
import pandas as pd
import re
import random
from random import choice
import rockClimbingFunc
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "intent/USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_rocks":["岩石","岩點","手點","石頭","點"],"_shoes":["岩鞋","抱石鞋","鞋子","攀岩鞋","攀岩鞋子"],"_sides":["中部","北部","南部","東部","西部"],"_whatIs":["星光票"],"_climbing":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石","抱石攀岩","速度攀","速度攀登","攀登","運動攀登"],"_cityAlias":["區域","地區","城市","縣市","都市","地方"],"_gymsShort":["達文西","8a攀岩場","B-plus","Boulder Space","Camp 4","Corner","Dapro","K2","MegaSTONE","POGO","TheDepotCity","Up聯盟","Y17","double 8","double8","久淘","千手抱石","原岩","嗨翻","嘉義攀岩會館","圓石","圓石空間","宜蘭運動中心","小岩館","崩岩","抱石基地","攀吶","新竹紅石","水美","iClimb","汐止抱石館","爬森","破舊二廠","破舊工廠","禾匠","紅石","艾思博","蕃薯藤","角岩館","風城","紅石攀岩館","RedRock","The Little Rock","Camp 4攀岩館","CORNER Bouldering Gym","角·攀岩館","內湖運動中心攀岩館","內湖運動中心","光合作用","Xizhi Bouldering Gym","市民抱石攀岩館","奇岩攀岩館","奇岩","岩究所","原岩攀岩館","T-UP","永和攀岩場","趣攀岩","文山攀岩館","POGO攀岩館","WUSA","WUSA攀岩館","Passion climbing","爬森攀岩館","蕃薯藤攀岩場","水美攀岩館","桃園國民運動中心","桃園國民運動中心攀岩館","iClimb風城","iClimb風城攀岩館","RedRock紅石攀岩","B-plus攀岩館","The depot city","攀吶攀岩館","Dapro indoor climbing","Dapro室內攀岩場","bouldering gym","Shabby Factory","嗨翻綜合體能館","圓石空間","圓石空間攀岩場","K2攀岩休閒館","艾思博攀岩俱樂部","禾匠體驗學習攀岩場","崩岩館站前店","崩岩館民治店","久淘抱石館","宜蘭運動中心攀岩館","8a攀岩場","嘉義市國民運動中心","Mega","RedRock紅石攀岩館-士林店","小岩館The Little Rock-天母店","小岩館The Little Rock-內湖店","Camp 4攀岩館-北投運動中心館","Camp 4攀岩館-萬華運動中心館","CORNER Bouldering Gym角·攀岩館","汐止抱石館Xizhi Bouldering Gym","市民抱石攀岩館","奇岩攀岩館 Kirin Climbing Gym","double 8 岩究所","double 8-Y17岩究所","原岩攀岩館-南港店 T-UP Climbing Gym-n.a.ngang","原岩攀岩館-南港店","原岩攀岩館-萬華店","原岩攀岩館-中和店","永和攀岩場 (趣攀岩)","永和攀岩場 (趣攀岩) TitoRock-Climbing","Up聯盟 文山攀岩館","MegaSTONE Climbing Gym","POGO 攀岩館","WUSA攀岩館-新莊館","WUSA攀岩館-三重館","Passion climbing 爬森攀岩館","原岩攀岩館-楊梅店","原岩攀岩館-A19店","水美攀岩館","pogo","TheDepotCityBoulderingGym","Dapro indoor climbing 室內攀岩場","破舊二廠 bouldering gym","破舊工廠 Shabby Factory","Boulder Space圓石空間攀岩場","崩岩館站前店-本館","崩岩館民治店-教學館","嘉義市國民運動中心8a攀岩場"],"_peClothes":["單車褲","瑜珈褲","運動服","運動衣","運動褲","運動鞋","攀岩褲"],"_rockTypes":["crimp","edge","flat","horn","jug","pinch","pocket","sloper","volume"],"_climbingGym":["岩場","岩館","攀岩場","攀岩館","抱石館","上攀館"],"_taiwanAlias":["全台","全台各地","全臺","全臺各地","台灣","臺灣","全台灣"],"_clothesPants":["上衣","服裝","短袖","短袖上衣","短袖衣服","衣服","衣著","衣褲","長袖","長袖上衣","長袖衣服","單車褲","瑜珈褲","短褲","運動褲","長褲"],"_climbingEquip":["岩粉","岩點刷","攀岩刷","攀岩粉","攀岩粉袋","止滑粉","碳酸鎂粉","粉球","粉袋","裝","裝備","鎂粉","鎂粉球"],"_topRopingEquip":["吊帶","垂降手套","安全吊帶","安全扣","安全扣環","快扣","手套","確保器","確保手套","耐磨手套"]}

gymsInfo = pd.read_csv('data/climbingGym.csv', encoding = 'utf-8')
defaultResponse = json.load(open("data/defaultResponse.json",encoding="utf-8"))
extendedDICT = {"_taiwanCities":["雲林","嘉義","台南","高雄","屏東","花蓮","台東","基隆","台北","桃園","新竹","宜蘭","新北","苗栗","台中","彰化","南投","蘭嶼","綠島","金門","馬祖","龜山島","離島"],"_midTW":["苗栗","台中","彰化","南投"],"_eastTW":["花蓮","台東"],"_northTW":["基隆","台北","桃園","新竹","宜蘭","新北"],"_southTW":["雲林","嘉義","台南","高雄","屏東"],"_islandsTW":["離島","金門","馬祖","澎湖","龜山島"]}


def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    logging.debug("Loki Result => {}".format(resultDICT))
    return resultDICT

def NLUmodel(mscDICT):
    print('mscDICT["msgSTR"]==',mscDICT["msgSTR"])
    resultDICT = getLokiResult(mscDICT["msgSTR"])
    logging.info("\nLoki 處理結果如下: {}\n".format(resultDICT))
    print("\nmscDICT --> {",mscDICT,"}\n")
    print("\nresultDICT --> {",resultDICT,"}\n")
    if len(resultDICT) > 0: #放找得到對應intent
        if "規則" in mscDICT["msgSTR"] or "規定" in mscDICT["msgSTR"]:
            if "reply_equipment_YesNo" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_equipment_YesNo"] 
            if "reply_rules" in resultDICT.keys():    
                mscDICT["replySTR"] = resultDICT["reply_rules"]
            print("\n---rules---\n")
        if "的意思是" in mscDICT["msgSTR"]:
            mscDICT["replySTR"] = resultDICT["reply_whatIs"]
            print("\n---what is---")
    
        elif "幾時" in mscDICT["msgSTR"] or "幾點" in mscDICT["msgSTR"] or "何時" in mscDICT["msgSTR"] or "開" in mscDICT["msgSTR"] or "關" in mscDICT["msgSTR"]:
            if "reply_gym_time" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_gym_time"]
            print("\n---time---\n")
        elif "位置" in mscDICT["msgSTR"] or "地址" in mscDICT["msgSTR"] or "電話" in mscDICT["msgSTR"]  or "資訊" in mscDICT["msgSTR"] or "聯絡" in mscDICT["msgSTR"]:
            if "reply_gym_location" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_gym_location"]
            print("\n---location---\n")
        
        elif "買" in mscDICT["msgSTR"] or "租" in mscDICT["msgSTR"] or "錢" in mscDICT["msgSTR"] or "裝備" in mscDICT["msgSTR"]:
            if "reply_equipment_YesNo" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_equipment_YesNo"] 
            
            if "reply_equipment_whereGet" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_equipment_whereGet"] 
            
            if "reply_gym_price" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_gym_price"]
            
            if "reply_equipment_price" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_equipment_price"]            
            
            if "reply_equipment_list" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_equipment_list"]
                
            if "reply_equipment_price" in resultDICT.keys() and "reply_gym_price" in resultDICT.keys():
                if resultDICT["reply_price"] == "gym":
                    mscDICT["replySTR"] = resultDICT["reply_gym_price"]
                else:
                    mscDICT["replySTR"] = resultDICT["reply_equipment_price"]            
            print("\n---equipment whereGet & list / price---\n")
        elif "有哪些" in mscDICT["msgSTR"]:
            print("---有哪些---")
            if "岩館" in mscDICT["msgSTR"] or "岩場" in mscDICT["msgSTR"]:
                if "reply_gym_location" in resultDICT.keys():
                    if resultDICT["_gym_name"] == "":
                        mscDICT["replySTR"] = "請問想問哪間岩館呢？"
                    else:
                        mscDICT["replySTR"] = resultDICT["reply_gym_location"]                   
                #不知道地點，問岩館名稱
                if "reply_gym_distance" in resultDICT.keys():
                    if resultDICT["reply_gym_distance"] != "":
                        mscDICT["replySTR"] = resultDICT["reply_gym_distance"]
                    else:                        
                        if mscDICT["_person_loc"] != "": #bot 知道人在哪裡
                            building = 0
                            if "館" in resultDICT["_rock_climbing"] or "場" in resultDICT["_rock_climbing"]:
                                building = 1                            
                            selectedGyms = rockClimbingFunc.getLocBTSGym(mscDICT["_person_loc"][:2], resultDICT["_rock_climbing"])
                            gymsNames = rockClimbingFunc.containerToString(selectedGyms)
                            if building == 0:
                                mscDICT["replySTR"] = "{0}的{1}岩館有{2}".format(mscDICT["_person_loc"],resultDICT["_rock_climbing"], gymsNames)
                            else:
                                mscDICT["replySTR"] = "{0}的{1}有{2}".format(mscDICT["_person_loc"],resultDICT["_rock_climbing"], gymsNames)
                        else: #bot 不知道人在哪裡
                            mscDICT["replySTR"] = "請問您在哪裡呢？可以給我一個地址或縣市嗎？"
                            mscDICT["_distance_intent"] = 1
                            mscDICT["_rock_climbing"] = resultDICT["_rock_climbing"]
                #知道地點，問岩館名稱
                if "reply_gym_name" in resultDICT.keys(): 
                    if resultDICT["reply_gym_name"] != "":
                        mscDICT["replySTR"] = resultDICT["reply_gym_name"]
                    else:
                        if resultDICT["_person_loc"] == "": #若有地點資訊，可以回答的問題：附近岩館
                            mscDICT["replySTR"] = "請問您在哪裡呢？可以給我一個地址或縣市嗎？"
                            mscDICT["_distance_intent"] = 1
                        else:
                            building = 0
                            if "館" in resultDICT["_rock_climbing"] or "場" in resultDICT["_rock_climbing"]:
                                building = 1                         
                            if "_gym_loc_large" in resultDICT.keys():
                                if resultDICT["_gym_loc_large"] in userDefinedDICT["_sides"]:
                                    mscDICT["_person_loc"] = resultDICT["_gym_loc_large"]
                                    counties = rockClimbingFunc.getSideCounties(resultDICT["_gym_loc_large"])
                                    selectedGyms = set()
                                    for county in counties:
                                        selectedGyms.update(rockClimbingFunc.getLocBTSGym(county, resultDICT["_rock_climbing"])) 
                                    gymsNames = rockClimbingFunc.containerToString(selectedGyms)
                                    if building == 1:
                                        mscDICT["replySTR"] = "{0}的{1}有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)
                                    else:
                                        mscDICT["replySTR"] = "{0}的{1}岩館有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)
                                elif resultDICT["_gym_loc_large"] in userDefinedDICT["_taiwanAlias"]:
                                    selectedGyms = rockClimbingFunc.getBTSGym(resultDICT["_gym_loc_large"])
                                    gymsNames = rockClimbingFunc.containerToString(selectedGyms)
                                    if building == 1:
                                        mscDICT["replySTR"] = "{0}的{1}有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)
                                    else:                                
                                        mscDICT["replySTR"] = "{0}的{1}岩館有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)                                
                                else:
                                    mscDICT["replySTR"] = choice(defaultResponse["_not_taiwan_city"])                            
                            elif "_gym_loc_small" in resultDICT.keys():
                                if rockClimbingFunc.checkLocation(resultDICT["_person_loc"]):
                                    mscDICT["_person_loc"] = resultDICT["_gym_loc_small"]
                                    selectedGyms = rockClimbingFunc.getLocBTSGym(resultDICT["_person_loc"], resultDICT["_rock_climbing"])
                                    gymsNames = rockClimbingFunc.containerToString(selectedGyms)
                                    if len(selectedGyms) > 0:
                                        if building == 1:
                                            mscDICT["replySTR"] = "{0}的{1}有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)
                                        else:
                                            mscDICT["replySTR"] = "{0}的{1}岩館有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)
                                    else:
                                        if building == 1:
                                            mscDICT["replySTR"] = "{0}的沒有{1}哦".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"])
                                        else:
                                            mscDICT["replySTR"] = "{0}沒有{1}岩館哦".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"])
                                else:
                                    mscDICT["replySTR"] = choice(defaultResponse["_not_taiwan_city"])
                        print(mscDICT["replySTR"])
            elif "岩點" in mscDICT["msgSTR"] or "石" in mscDICT["msgSTR"]:
                mscDICT["replySTR"] = resultDICT["reply_rocks"]
            elif "注意" in mscDICT["msgSTR"] or "小心" in mscDICT["msgSTR"]:
                if "reply_rules" in resultDICT.keys():
                    mscDICT["replySTR"] = resultDICT["reply_rules"]                
            else:
                if "reply_equipment_list" in resultDICT.keys():
                    mscDICT["replySTR"] = resultDICT["reply_equipment_list"]  
        elif "距離" in mscDICT["msgSTR"] and "reply_gym_distance" in resultDICT.keys() and "reply_gym_name" in resultDICT.keys(): 
            if resultDICT["reply_gym_distance"] != "":
                mscDICT["replySTR"] = resultDICT["reply_gym_distance"]
            else:                        
                if mscDICT["_person_loc"] != "": #bot 知道人在哪裡
                    building = 0
                    if "館" in resultDICT["_rock_climbing"] or "場" in resultDICT["_rock_climbing"]:
                        building = 1                            
                    selectedGyms = rockClimbingFunc.getLocBTSGym(mscDICT["_person_loc"][:2], resultDICT["_rock_climbing"])
                    gymsNames = rockClimbingFunc.containerToString(selectedGyms)
                    if len(gymsNames) > 0:
                        if building == 0:
                            mscDICT["replySTR"] = "{0}的{1}岩館有{2}".format(mscDICT["_person_loc"],resultDICT["_rock_climbing"], gymsNames)
                        else:
                            mscDICT["replySTR"] = "{0}的{1}有{2}".format(mscDICT["_person_loc"],resultDICT["_rock_climbing"], gymsNames)
                    else:
                        if building == 0:
                            mscDICT["replySTR"] = "{0}沒有{1}岩館哦！".format(mscDICT["_person_loc"],resultDICT["_rock_climbing"])
                        else:
                            mscDICT["replySTR"] = "{0}沒有{1}哦！".format(mscDICT["_person_loc"],resultDICT["_rock_climbing"])                            
                else: #bot 不知道人在哪裡
                    mscDICT["replySTR"] = "請問您在哪裡呢？可以給我一個地址或縣市嗎？"
                    mscDICT["_distance_intent"] = 1
                    mscDICT["_rock_climbing"] = resultDICT["_rock_climbing"]
        elif "是什麼" in mscDICT["msgSTR"]:
            print("----what is rock------")
            if "有名的" in mscDICT["msgSTR"] or "館" in mscDICT["msgSTR"] or "場" in mscDICT["msgSTR"]:
                #知道地點，問岩館名稱
                if "reply_gym_name" in resultDICT.keys(): 
                    if resultDICT["reply_gym_name"] != "":
                        mscDICT["replySTR"] = resultDICT["reply_gym_name"]
                    else:
                        if resultDICT["_person_loc"] == "": 
                            mscDICT["replySTR"] = "請問您在哪裡呢？可以給我一個地址或縣市嗎？"
                            mscDICT["_rock_climbing"] = resultDICT["_rock_climbing"]
                            mscDICT["_distance_intent"] = 1
                        else: #若有地點資訊，可以回答的問題：附近岩館
                            building = 0
                            if "館" in resultDICT["_rock_climbing"] or "場" in resultDICT["_rock_climbing"]:
                                building = 1                         
                            if "_gym_loc_large" in resultDICT.keys():
                                if resultDICT["_gym_loc_large"] in userDefinedDICT["_sides"]:
                                    mscDICT["_person_loc"] = resultDICT["_gym_loc_large"]
                                    counties = rockClimbingFunc.getSideCounties(resultDICT["_gym_loc_large"])
                                    selectedGyms = set()
                                    for county in counties:
                                        selectedGyms.update(rockClimbingFunc.getLocBTSGym(county, resultDICT["_rock_climbing"])) 
                                    gymsNames = rockClimbingFunc.containerToString(selectedGyms)
                                    if building == 1:
                                        mscDICT["replySTR"] = "{0}的{1}有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)
                                    else:
                                        mscDICT["replySTR"] = "{0}的{1}岩館有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)
                                elif resultDICT["_gym_loc_large"] in userDefinedDICT["_taiwanAlias"]:
                                    selectedGyms = rockClimbingFunc.getBTSGym(args[1])
                                    gymsNames = rockClimbingFunc.containerToString(selectedGyms)
                                    if building == 1:
                                        mscDICT["replySTR"] = "{0}的{1}有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)
                                    else:                                
                                        mscDICT["replySTR"] = "{0}的{1}岩館有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)                                
                                else:
                                    mscDICT["replySTR"] = choice(defaultResponse["_not_taiwan_city"])                            
                            elif "_gym_loc_small" in resultDICT.keys():
                                if rockClimbingFunc.checkLocation(resultDICT["_person_loc"]):
                                    mscDICT["_person_loc"] = resultDICT["_gym_loc_small"]
                                    selectedGyms = rockClimbingFunc.getLocBTSGym(resultDICT["_person_loc"], resultDICT["_rock_climbing"])
                                    gymsNames = rockClimbingFunc.containerToString(selectedGyms)
                                    if len(selectedGyms) > 0:
                                        if building == 1:
                                            mscDICT["replySTR"] = "{0}的{1}有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)
                                        else:
                                            mscDICT["replySTR"] = "{0}的{1}岩館有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)
                                    else:
                                        if building == 1:
                                            mscDICT["replySTR"] = "{0}的沒有{1}哦".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"])
                                        else:
                                            mscDICT["replySTR"] = "{0}沒有{1}岩館哦".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"])
                                else:
                                    mscDICT["replySTR"] = choice(defaultResponse["_not_taiwan_city"]) 
                elif "規則" in mscDICT["msgSTR"] or "規定" in mscDICT["msgSTR"]:
                    mscDICT["replySTR"] = resultDICT["reply_rules"]
                else:
                    mscDICT["replySTR"] = resultDICT["reply_whatIs"]
            elif "地址" in mscDICT["msgSTR"] or "電話" in mscDICT["msgSTR"] or "聯絡" in mscDICT["msgSTR"]:
                if "reply_gym_location" in resultDICT.keys():
                    mscDICT["replySTR"] = resultDICT["reply_gym_location"]
            elif "特" in mscDICT["msgSTR"]:
                if "reply_rocks" in resultDICT.keys():
                    mscDICT["replySTR"] = resultDICT["reply_rocks"]
                    print("----what is rock------")
            else:
                mscDICT["replySTR"] = resultDICT["reply_whatIs"]
        elif "注意" in mscDICT["msgSTR"] or "小心" in mscDICT["msgSTR"]:
            print("----attention----\n")
            if "爬" in mscDICT["msgSTR"] and "reply_rocks" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_rocks"]
            elif "reply_rules" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_rules"]         
        else:
            if "reply_chat" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_chat"]

            if "reply_whatIs" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_whatIs"]
        
            if "reply_gym_price" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_gym_price"]
    
            if "reply_gym_time" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_gym_time"]
            
            if "reply_person_location" in resultDICT.keys():
                if "reply_gym_howMany" in resultDICT.keys():
                    pass
                else:
                    if resultDICT["reply_person_location"] == "addr": #改
                        mscDICT["_person_loc"] = resultDICT["_person_loc"]
                        mscDICT["replySTR"] = choice(defaultResponse["_msg_received"])
                    elif "_gym_loc_small" in resultDICT.keys():
                        if rockClimbingFunc.checkLocation(resultDICT["_person_loc"]):
                            mscDICT["_person_loc"] = resultDICT["_person_loc"]
                            building = 0
                            if "館" in mscDICT["_rock_climbing"] or "場" in mscDICT["_rock_climbing"]:
                                building = 1                            
                            if mscDICT["_distance_intent"] == 1:
                                selectedGyms = rockClimbingFunc.getLocBTSGym(resultDICT["_person_loc"], mscDICT["_rock_climbing"])
                                gymsNames = rockClimbingFunc.containerToString(selectedGyms)  
                                if len(gymsNames) > 0: 
                                    if building == 0:
                                        mscDICT["replySTR"] = "{0}的{1}岩館有{2}".format(resultDICT["_person_loc"], mscDICT["_rock_climbing"], gymsNames)
                                    else:
                                        mscDICT["replySTR"] = "{0}的{1}有{2}".format(resultDICT["_person_loc"], mscDICT["_rock_climbing"], gymsNames)
                                else:
                                    if building == 0:
                                        mscDICT["replySTR"] = "{0}沒有{1}岩館哦".format(resultDICT["_person_loc"], mscDICT["_rock_climbing"])
                                    else:
                                        mscDICT["replySTR"] = "{0}沒有{1}哦".format(resultDICT["_person_loc"], mscDICT["_rock_climbing"])
                                mscDICT["_distance_intent"] = 0
                            else:
                                mscDICT["replySTR"] = choice(defaultResponse["_msg_received"])
                        else:
                            mscDICT["replySTR"] = choice(defaultResponse["_not_taiwan_city"])
                    elif resultDICT["_person_loc"] in userDefinedDICT["_sides"]:
                        if mscDICT["_distance_intent"] == 1:
                            mscDICT["_person_loc"] = resultDICT["_person_loc"]
                            counties = rockClimbingFunc.getSideCounties(resultDICT["_person_loc"])
                            selectedGyms = set()
                            for county in counties:
                                selectedGyms.update(rockClimbingFunc.getLocBTSGym(county, mscDICT["_rock_climbing"]))
                            gymsNames = rockClimbingFunc.containerToString(selectedGyms)
                            mscDICT["replySTR"] = "{0}的{1}有{2}".format(mscDICT["_person_loc"], mscDICT["_rock_climbing"], gymsNames)
                        else:
                            mscDICT["replySTR"] = choice(defaultResponse["_msg_received"])
                    elif "_gym_loc_large" in resultDICT.keys():
                        if resultDICT["_person_loc"] in userDefinedDICT["_taiwanAlias"]:
                            mscDICT["replySTR"] = "可以再明確一點嗎？"
                        else:
                            mscDICT["replySTR"] = choice(defaultResponse["_not_taiwan_city"])    
            
            if "reply_gym_location" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_gym_location"]
        
            #不知道地點，問岩館名稱    
            if "reply_gym_distance" in resultDICT.keys():
                if resultDICT["reply_gym_distance"] != "":
                    mscDICT["replySTR"] = resultDICT["reply_gym_distance"]
                else:                        
                    if mscDICT["_person_loc"] != "": #bot 知道人在哪裡
                        building = 0
                        if "館" in resultDICT["_rock_climbing"] or "場" in resultDICT["_rock_climbing"]:
                            building = 1                            
                        selectedGyms = rockClimbingFunc.getLocBTSGym(mscDICT["_person_loc"][:2], resultDICT["_rock_climbing"])
                        gymsNames = rockClimbingFunc.containerToString(selectedGyms)
                        if len(gymsNames) > 0:
                            if building == 0:
                                mscDICT["replySTR"] = "{0}的{1}岩館有{2}".format(mscDICT["_person_loc"],resultDICT["_rock_climbing"], gymsNames)
                            else:
                                mscDICT["replySTR"] = "{0}的{1}有{2}".format(mscDICT["_person_loc"],resultDICT["_rock_climbing"], gymsNames)
                        else:
                            if building == 0:
                                mscDICT["replySTR"] = "{0}沒有{1}岩館哦！".format(mscDICT["_person_loc"],resultDICT["_rock_climbing"])
                            else:
                                mscDICT["replySTR"] = "{0}沒有{1}哦！".format(mscDICT["_person_loc"],resultDICT["_rock_climbing"])                            
                    else: #bot 不知道人在哪裡
                        mscDICT["replySTR"] = "請問您在哪裡呢？可以給我一個地址或縣市嗎？"
                        mscDICT["_distance_intent"] = 1
                        mscDICT["_rock_climbing"] = resultDICT["_rock_climbing"]
            
            #知道地點，問岩館名稱
            if "reply_gym_name" in resultDICT.keys(): 
                if resultDICT["reply_gym_name"] != "":
                    mscDICT["replySTR"] = resultDICT["reply_gym_name"]
                else:
                    if resultDICT["_person_loc"] == "": 
                        mscDICT["replySTR"] = "請問您在哪裡呢？可以給我一個地址或縣市嗎？"
                        mscDICT["_rock_climbing"] = resultDICT["_rock_climbing"]
                        mscDICT["_distance_intent"] = 1
                    else: #若有地點資訊，可以回答的問題：附近岩館
                        building = 0
                        if "館" in resultDICT["_rock_climbing"] or "場" in resultDICT["_rock_climbing"]:
                            building = 1                         
                        if "_gym_loc_large" in resultDICT.keys():
                            if resultDICT["_gym_loc_large"] in userDefinedDICT["_sides"]:
                                mscDICT["_person_loc"] = resultDICT["_gym_loc_large"]
                                counties = rockClimbingFunc.getSideCounties(resultDICT["_gym_loc_large"])
                                selectedGyms = set()
                                for county in counties:
                                    selectedGyms.update(rockClimbingFunc.getLocBTSGym(county, resultDICT["_rock_climbing"])) 
                                gymsNames = rockClimbingFunc.containerToString(selectedGyms)
                                if building == 1:
                                    mscDICT["replySTR"] = "{0}的{1}有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)
                                else:
                                    mscDICT["replySTR"] = "{0}的{1}岩館有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)
                            elif resultDICT["_gym_loc_large"] in userDefinedDICT["_taiwanAlias"]:
                                selectedGyms = rockClimbingFunc.getBTSGym(args[1])
                                gymsNames = rockClimbingFunc.containerToString(selectedGyms)
                                if building == 1:
                                    mscDICT["replySTR"] = "{0}的{1}有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)
                                else:                                
                                    mscDICT["replySTR"] = "{0}的{1}岩館有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)                                
                            else:
                                mscDICT["replySTR"] = choice(defaultResponse["_not_taiwan_city"])                            
                        elif "_gym_loc_small" in resultDICT.keys():
                            if rockClimbingFunc.checkLocation(resultDICT["_person_loc"]):
                                mscDICT["_person_loc"] = resultDICT["_gym_loc_small"]
                                selectedGyms = rockClimbingFunc.getLocBTSGym(resultDICT["_person_loc"], resultDICT["_rock_climbing"])
                                gymsNames = rockClimbingFunc.containerToString(selectedGyms)
                                if len(selectedGyms) > 0:
                                    if building == 1:
                                        mscDICT["replySTR"] = "{0}的{1}有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)
                                    else:
                                        mscDICT["replySTR"] = "{0}的{1}岩館有{2}".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"], gymsNames)
                                else:
                                    if building == 1:
                                        mscDICT["replySTR"] = "{0}的沒有{1}哦".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"])
                                    else:
                                        mscDICT["replySTR"] = "{0}沒有{1}岩館哦".format(mscDICT["_person_loc"], resultDICT["_rock_climbing"])
                            else:
                                mscDICT["replySTR"] = choice(defaultResponse["_not_taiwan_city"])    
         
            if "reply_gym_howMany" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_gym_howMany"]
        
            if "reply_gym_yesNo" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_gym_yesNo"]
        
            if "reply_equipment_list" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_equipment_list"]
        
            if "reply_equipment_price" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_equipment_price"]
        
            if "reply_equipment_YesNo" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_equipment_YesNo"]
        
            if "reply_rocks" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_rocks"]
        
            if "reply_rules" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_rules"]
                
            if "reply_equipment_whereGet" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_equipment_whereGet"] 
            
            if "reply_gym_name" in resultDICT.keys() and "reply_gym_time" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_gym_time"]
            
            if "reply_gym_name" in resultDICT.keys() and "reply_gym_location" in resultDICT.keys():
                if "有名的" in mscDICT["msgSTR"]:
                    mscDICT["replySTR"] = resultDICT["reply_gym_name"]
                else:
                    mscDICT["replySTR"] = resultDICT["reply_gym_location"]
            
            if "reply_gym_location" in resultDICT.keys() and "reply_gym_district" in resultDICT.keys() :
                mscDICT["replySTR"] = resultDICT["reply_gym_district"]             
            
            if "reply_equipment_price" in resultDICT.keys() and "reply_gym_price" in resultDICT.keys():
                if resultDICT["reply_price"] == "gym":
                    mscDICT["replySTR"] = resultDICT["reply_gym_price"]
                else:
                    mscDICT["replySTR"] = resultDICT["reply_equipment_price"]
            
            if mscDICT["replySTR"] == "":
                mscDICT["replySTR"] = "不太明白你的意思"
    
    else: #沒有對應intent
        mscDICT["replySTR"] = "不太明白你的意思欸"

    return mscDICT