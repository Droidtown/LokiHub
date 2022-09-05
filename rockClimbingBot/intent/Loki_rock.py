#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for rock

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
from rockClimbingFunc import containerToString1

DEBUG_rock = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_rocks":["岩石","岩點","手點","石頭","點"],"_shoes":["岩鞋","抱石鞋","鞋子","攀岩鞋","攀岩鞋子"],"_sides":["中部","北部","南部","東部","西部"],"_whatIs":["星光票"],"_climbing":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石","抱石攀岩","速度攀","速度攀登","攀登","運動攀登"],"_cityAlias":["區域","地區","城市","縣市","都市","地方"],"_gymsShort":["達文西","8a攀岩場","B-plus","Boulder Space","Camp 4","Corner","Dapro","K2","MegaSTONE","POGO","TheDepotCity","Up聯盟","Y17","double 8","double8","久淘","千手抱石","原岩","嗨翻","嘉義攀岩會館","圓石","圓石空間","宜蘭運動中心","小岩館","崩岩","抱石基地","攀吶","新竹紅石","水美iClimb","汐止抱石館","爬森","破舊二廠","破舊工廠","禾匠","紅石","艾思博","蕃薯藤","角岩館","風城"],"_peClothes":["單車褲","瑜珈褲","運動服","運動衣","運動褲","運動鞋","攀岩褲"],"_rockTypes":["crimp","edge","flat","horn","jug","pinch","pocket","sloper","volume"],"_climbingGym":["岩場","岩館","攀岩場","攀岩館","抱石館","上攀館"],"_taiwanAlias":["全台","全台各地","全臺","全臺各地","台灣","臺灣","全台灣"],"_clothesPants":["上衣","服裝","短袖","短袖上衣","短袖衣服","衣服","衣著","衣褲","長袖","長袖上衣","長袖衣服","單車褲","瑜珈褲","短褲","運動褲","長褲"],"_climbingEquip":["岩粉","岩點刷","攀岩刷","攀岩粉","攀岩粉袋","止滑粉","碳酸鎂粉","粉球","粉袋","裝","裝備","鎂粉","鎂粉球"],"_topRopingEquip":["吊帶","垂降手套","安全吊帶","安全扣","安全扣環","快扣","手套","確保器","確保手套","耐磨手套"]}

rocksInfo = json.load(open('data/rocks.json', encoding = 'utf-8'))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_rock:
        print("[rock] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[jug]有什麼[特色]":
        if args[0] in userDefinedDICT["_rockTypes"]:
            resultDICT["reply_rocks"] = "{0}{1}".format(args[0], rocksInfo[args[0]][0])
        else:
            resultDICT["reply_rocks"] = "我不認識這種岩點耶！"

    if utterance == "[jug]的[特色]是什麼":
        if args[0] in userDefinedDICT["_rockTypes"]:
            resultDICT["reply_rocks"] = "{0}{1}".format(args[0], rocksInfo[args[0]][0])
        else:
            resultDICT["reply_rocks"] = "我不認識這種岩點耶！"

    if utterance == "[jug]長什麼樣子":
        if args[0] in userDefinedDICT["_rockTypes"]:
            if args[0] == "jug":
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/idnc3ekvnuid6bm/jug.png?dl=0"#args[0]
            elif args[0] == "crimp":
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/f8pby7052vzfg0m/crimp.png?dl=0"
            elif args[0] == "edge":
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/fzs4ae0jjiapgzm/edge.png?dl=0"
            elif args[0] == "flat":
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/vntlf9bmw795ww4/flat.png?dl=0"
            elif args[0] == "horn":
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/dfxxayjbgq8grzv/horn.png?dl=0"
            elif args[0] == "pinch":
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/z4vvzvppl6imgax/pinch.png?dl=0"
            elif args[0] == "pocket":
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/5azmi5pjrf4048s/pocket.png?dl=0"
            elif args[0] == "sloper":
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/8vaeh37qypa69b7/sloper.png?dl=0"
            else:#volume
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/oz76sdzv57rbb5x/volume.png?dl=0"
        else:
            resultDICT["reply_rocks"] = "我不認識這種岩點耶！"

    if utterance == "[jug]長怎樣":
        if args[0] in userDefinedDICT["_rockTypes"]:
            if args[0] == "jug":
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/idnc3ekvnuid6bm/jug.png?dl=0"#args[0]
            elif args[0] == "crimp":
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/f8pby7052vzfg0m/crimp.png?dl=0"
            elif args[0] == "edge":
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/fzs4ae0jjiapgzm/edge.png?dl=0"
            elif args[0] == "flat":
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/vntlf9bmw795ww4/flat.png?dl=0"
            elif args[0] == "horn":
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/dfxxayjbgq8grzv/horn.png?dl=0"
            elif args[0] == "pinch":
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/z4vvzvppl6imgax/pinch.png?dl=0"
            elif args[0] == "pocket":
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/5azmi5pjrf4048s/pocket.png?dl=0"
            elif args[0] == "sloper":
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/8vaeh37qypa69b7/sloper.png?dl=0"
            else:#volume
                resultDICT["reply_rocks"] = "https://www.dropbox.com/s/oz76sdzv57rbb5x/volume.png?dl=0"
        else:
            resultDICT["reply_rocks"] = "我不認識這種岩點耶！"

    if utterance == "[pinch]怎麼抓":
        if args[0] in userDefinedDICT["_rockTypes"]:
            resultDICT["reply_rocks"] = "{0}{1}".format(args[0], rocksInfo[args[0]][1])
        else:
            resultDICT["reply_rocks"] = "我不認識這種岩點耶！"

    if utterance == "[sloper][可以]怎麼爬":
        if args[0] in userDefinedDICT["_rockTypes"]:
            resultDICT["reply_rocks"] = "{0}{1}".format(args[0], rocksInfo[args[0]][1])
        else:
            resultDICT["reply_rocks"] = "我不認識這種岩點耶！"

    if utterance == "[岩點]有哪些":
        if args[0] in userDefinedDICT["_rocks"]:
            rocksStr = containerToString1(userDefinedDICT["_rockTypes"])
            resultDICT["reply_rocks"] = "{0}較常見的有{1}".format(args[0], rocksStr)
            return resultDICT
        elif args[0] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_list"] = args[0]+"有岩粉、岩鞋、粉袋、確保器、安全吊帶、手套等"
        else:
            resultDICT["reply_rocks"] = "不確定你的問題，可否再問明確點"

    if utterance == "[岩點]有哪幾[種]":
        if args[0] in userDefinedDICT["_rocks"]:
            rocksStr = containerToString1(userDefinedDICT["_rockTypes"])
            resultDICT["reply_rocks"] = "{0}較常見的有{1}".format(args[0], rocksStr)
        elif args[0] in userDefinedDICT["_climbingEquip"]:
            resultDICT["reply_equipment_list"] = args[0]+"有岩粉、岩鞋、粉袋、確保器、安全吊帶、手套等"
        else:
            resultDICT["reply_rocks"] = "不確定你的問題，可否再問明確點"

    if utterance == "[最好爬]的是哪種":
        resultDICT["reply_rocks"] = "jug是新手會遇到的最初階岩點類型"

    if utterance == "最不好抓的[點]是":
        resultDICT["reply_rocks"] = "我覺得是flat"

    if utterance == "最不好抓的[點]是哪個":
        resultDICT["reply_rocks"] = "我覺得是flat"

    if utterance == "最好抓的是哪種[點]":
        resultDICT["reply_rocks"] = "jug是新手會遇到的最初階岩點類型"

    if utterance == "最難抓的[點]是哪個":
        resultDICT["reply_rocks"] = "我覺得是flat"

    if utterance == "爬[jug]要注意什麼":
        if args[0] in userDefinedDICT["_rockTypes"]:
            resultDICT["reply_rocks"] = "{0}{1}".format(args[0], rocksInfo[args[0]][1])
        else:
            resultDICT["reply_rocks"] = "我不認識這種岩點耶！"

    return resultDICT