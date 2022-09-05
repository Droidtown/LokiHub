from rockClimbing import runLoki
import json
import logging
import pandas as pd
import re
import random
from rockClimbingFunc import getLocBTSGym
from rockClimbingFunc import containerToString
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "intent/USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_rocks":["岩石","岩點","手點","石頭","點"],"_shoes":["岩鞋","抱石鞋","鞋子","攀岩鞋","攀岩鞋子"],"_sides":["中部","北部","南部","東部","西部"],"_whatIs":["星光票"],"_climbing":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石","抱石攀岩","速度攀","速度攀登","攀登","運動攀登"],"_cityAlias":["區域","地區","城市","縣市","都市","地方"],"_gymsShort":["達文西","8a攀岩場","B-plus","Boulder Space","Camp 4","Corner","Dapro","K2","MegaSTONE","POGO","TheDepotCity","Up聯盟","Y17","double 8","double8","久淘","千手抱石","原岩","嗨翻","嘉義攀岩會館","圓石","圓石空間","宜蘭運動中心","小岩館","崩岩","抱石基地","攀吶","新竹紅石","水美iClimb","汐止抱石館","爬森","破舊二廠","破舊工廠","禾匠","紅石","艾思博","蕃薯藤","角岩館","風城"],"_peClothes":["單車褲","瑜珈褲","運動服","運動衣","運動褲","運動鞋","攀岩褲"],"_rockTypes":["crimp","edge","flat","horn","jug","pinch","pocket","sloper","volume"],"_climbingGym":["岩場","岩館","攀岩場","攀岩館","抱石館","上攀館"],"_taiwanAlias":["全台","全台各地","全臺","全臺各地","台灣","臺灣","全台灣"],"_clothesPants":["上衣","服裝","短袖","短袖上衣","短袖衣服","衣服","衣著","衣褲","長袖","長袖上衣","長袖衣服","單車褲","瑜珈褲","短褲","運動褲","長褲"],"_climbingEquip":["岩粉","岩點刷","攀岩刷","攀岩粉","攀岩粉袋","止滑粉","碳酸鎂粉","粉球","粉袋","裝","裝備","鎂粉","鎂粉球"],"_topRopingEquip":["吊帶","垂降手套","安全吊帶","安全扣","安全扣環","快扣","手套","確保器","確保手套","耐磨手套"]}

gymsInfo = pd.read_csv('data/climbingGym.csv', encoding = 'utf-8')
defaultResponse = json.load(open("data/defaultResponse.json",encoding="utf-8"))

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
    print("\nmscDICT --> {",mscDICT.keys(),"}\n")
    if len(resultDICT) > 0: #放找得到對應intent
        if "規則" in mscDICT["msgSTR"] or "規定" in mscDICT["msgSTR"]:
            if "reply_rules" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_rules"]
            print("\n---rules---\n")
        elif "錢" in mscDICT["msgSTR"] or "多少" in mscDICT["msgSTR"]:
            if "reply_gym_price" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_gym_price"]
            print("\n---price---\n")
        elif "幾時" in mscDICT["msgSTR"] or "幾點" in mscDICT["msgSTR"] or "何時" in mscDICT["msgSTR"] or "開" in mscDICT["msgSTR"] or "關" in mscDICT["msgSTR"]:
            if "reply_gym_time" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_gym_time"]
            print("\n---time---\n")
        elif "位置" in mscDICT["msgSTR"] or "地址" in mscDICT["msgSTR"] or "電話" in mscDICT["msgSTR"]  or "資訊" in mscDICT["msgSTR"] or "聯絡" in mscDICT["msgSTR"]:
            if "reply_gym_location" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_gym_location"]
            print("\n---location---\n")
        elif "買" in mscDICT["msgSTR"] or "租" in mscDICT["msgSTR"]:
            if "reply_equipment_whereGet" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_equipment_whereGet"] 
            print("\n---equipment where get---\n")
        elif "有哪些" in mscDICT["msgSTR"]:
            if "岩館" in mscDICT["msgSTR"]:
                if "reply_gym_location" in resultDICT.keys():
                    if resultDICT["_gym_name"] == "":
                        mscDICT["replySTR"] = "請問想問哪間岩館呢？"
                    else:
                        mscDICT["replySTR"] = resultDICT["reply_gym_location"]                   
                if "reply_gym_distance" in resultDICT.keys():
                    mscDICT["replySTR"] = resultDICT["reply_gym_distance"] 
                if "reply_gym_name" in resultDICT.keys():
                    if resultDICT["_person_loc"] == "": 
                        mscDICT["replySTR"] = "請問您在哪裡呢？可以給我一個地址或縣市嗎？"
                        mscDICT["_distance_intent"] = 1
                    else:
                        mscDICT["replySTR"] = resultDICT["reply_gym_name"]    
            elif "岩點" in mscDICT["msgSTR"] or "石" in mscDICT["msgSTR"]:
                mscDICT["replySTR"] = resultDICT["reply_rocks"]
            elif "注意" in mscDICT["msgSTR"] or "小心" in mscDICT["msgSTR"]:
                if "reply_rules" in resultDICT.keys():
                    mscDICT["replySTR"] = resultDICT["reply_rules"]                
            else:
                if "reply_equipment_list" in resultDICT.keys():
                    mscDICT["replySTR"] = resultDICT["reply_equipment_list"]                
        else:
            if "reply_chat" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_chat"]
            
            if "reply_gym_distance" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_gym_distance"] 

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
                    if resultDICT["reply_person_location"] == "addr":
                        mscDICT["replySTR"] = "我知道了"
                    elif resultDICT["_person_loc"] != "" and resultDICT["_person_loc"] not in userDefinedDICT["_sides"]:
                        if mscDICT["_distance_intent"] == 1:
                            selectedGyms = getLocBTSGym(resultDICT["_person_loc"] ,"")
                            gymsNames = containerToString(selectedGyms)  
                            if len(gymsNames) > 0: 
                                mscDICT["replySTR"] = "{0}的岩館有{1}".format(resultDICT["_person_loc"] , gymsNames)
                            else:
                                mscDICT["replySTR"] = "{}沒有岩館哦".format(resultDICT["_person_loc"])
                            mscDICT["_distance_intent"] = 0
                        else:
                            mscDICT["replySTR"] = random.choice(defaultResponse["_msg_received"])
                    elif resultDICT["_person_loc"] in userDefinedDICT["_sides"]:
                        counties = getSideCounties(args[0])
                        selectedGyms = set()
                        for county in counties:
                            selectedGyms.update(getLocBTSGym(county, args[1]))
                        gymsNames = containerToString(selectedGyms)
                        mscDICT["replySTR"] = "{0}的{1}有{2}".format(args[0], args[1], gymsNames)
                    else:
                        mscDICT["replySTR"] = "你怎麼知道"
        
            if "reply_gym_name" in resultDICT.keys():
                if resultDICT["_person_loc"] == "": #若有地點資訊，可以回答的問題：附近岩館
                    mscDICT["replySTR"] = "請問您在哪裡呢？可以給我一個地址或縣市嗎？"
                    mscDICT["_distance_intent"] = 1
                else:
                    mscDICT["replySTR"] = resultDICT["reply_gym_name"]
                    
            if "reply_gym_location" in resultDICT.keys():
                if resultDICT["_gym_name"] == "":
                    mscDICT["replySTR"] = "請問想問哪間岩館呢？"
                else:
                    mscDICT["replySTR"] = resultDICT["reply_gym_location"]            
        
            if "reply_gym_howMany" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_gym_howMany"]
        
            if "reply_gym_yesNo" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_gym_yesNo"]
        
            if "reply_equipment_list" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_equipment_list"]
        
            if "reply_equipment_price" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_equipment_price"]
        
            if "reply_equipment_YesNo" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_equipment_yesNo"]
        
            if "reply_rocks" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_rocks"]
        
            if "reply_rules" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_rules"]
                
            if "reply_equipment_whereGet" in resultDICT.keys():
                mscDICT["replySTR"] = resultDICT["reply_equipment_whereGet"] 
            
            if mscDICT["replySTR"] == "":
                mscDICT["replySTR"] = "不太明白你的意思"
    
    else: #沒有對應intent
        mscDICT["replySTR"] = "不太明白你的意思欸"

    return mscDICT