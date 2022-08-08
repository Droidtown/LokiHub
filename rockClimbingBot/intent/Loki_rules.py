#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for rules

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

DEBUG_rules = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_can":["可以","可","適合"],"_what":["什麼","哪些","什麼東西","哪些東西","哪種","哪幾間"],"_midTW":["苗栗","台中","彰化","南投"],"_pants":["褲子","褲","長褲","短褲","運動褲","瑜珈褲"],"_rocks":["岩點","石頭","手點","點"],"_rules":["規則","規範","法則","守則","規定"],"_shoes":["岩鞋","鞋子","攀岩鞋","抱石鞋","鞋"],"_sides":["東部","北部","南部","西部","中部"],"_which":["哪幾間","哪間","哪一間","哪些","哪個"],"_eastTW":["花蓮","台東"],"_levels":["難度","等級","階級"],"_clothes":["衣服","長袖","短袖","衣著","服裝","長袖衣服","上衣","短袖衣服","長袖上衣","短袖上衣","衣褲"],"_northTW":["基隆","台北","桃園","新竹","宜蘭","新北"],"_southTW":["雲林","嘉義","台南","高雄","屏東"],"_climbing":["攀岩","抱石","上攀","速度攀","速度攀登","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石攀岩"],"_cityAlias":["縣市","縣","市","地區","都市","城市","區","區域"],"_peClothes":["運動衣","運動褲","運動服","瑜珈褲","單車褲"],"_rockTypes":["jug","pinch","sloper","edge","crimp","pocket","flat","horn","volume"],"_appearance":["樣子","模樣"],"_climbingGym":["岩館","攀岩館","攀岩場","抱石館","抱石場館","抱石場","岩場","上攀館","上攀場","上攀場館"],"_climbingTop":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","上攀館","上攀場館","上攀岩館","先鋒攀岩館"],"_taiwanAlias":["全台","全臺","全台各地","台灣","臺灣","全臺各地"],"_taiwanCities":["雲林","嘉義","台南","高雄","屏東","花蓮","台東","基隆","台北","桃園","新竹","宜蘭","新北","苗栗","台中","彰化","南投"],"_climbingEquip":["裝","裝備","岩粉","粉袋","攀岩粉袋","粉球","止滑粉","攀岩粉","攀岩粉袋","岩點刷","攀岩刷","鎂粉球","鎂粉","碳酸鎂粉"],"_climbingSpeed":["速度攀","速度攀登","速度攀岩館","速度攀登場館"],"_topRopingEquip":["手套","確保手套","垂降手套","耐磨手套","安全吊帶","確保器","安全扣","快扣","安全扣環","吊帶"],"_climbingBoulder":["抱石","抱石攀岩","抱石館","抱石場館","抱石場"],"_climbingGeneralGym":["岩館","攀岩館","攀岩場","攀岩場館"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_rules:
        print("[rules] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[上攀]有[什麼]要注意的？":
        if args[0] not in userDefinedDICT["climbing"]:
            resultDICT["func_rule"] = "這跟攀岩無關，我不清楚耶"
        else:
            resultDICT["func_rule"] = "小心不要受傷！"
        pass

    if utterance == "[上攀]有[哪些]要[小心]的？":
        if args[0] not in userDefinedDICT["climbing"]:
            resultDICT["func_rule"] = "這跟攀岩無關，我不清楚耶"
        else:
            resultDICT["func_rule"] = "小心不要受傷！"
        pass

    if utterance == "[上攀]要[小心][什麼]？":
        if args[0] not in userDefinedDICT["climbing"]:
            resultDICT["func_rule"] = "這跟攀岩無關，我不清楚耶"
        else:
            resultDICT["func_rule"] = "小心不要受傷！"
        pass

    if utterance == "[抱石]要注意[什麼]":
        if args[0] not in userDefinedDICT["climbing"]:
            resultDICT["func_rule"] = "這跟攀岩無關，我不清楚耶"
        else:
            resultDICT["func_rule"] = "小心不要受傷！"
        pass

    if utterance == "[攀岩]有[哪些]規則":
        if args[0] not in userDefinedDICT["climbing"]:
            resultDICT["func_rule"] = "這跟攀岩無關，我不清楚耶"
        else:
            resultDICT["func_rule"] = "1.每條路線都有「起攀點」和一個「完攀點」。 2.雙手雙腳離地才算正式起攀。 3.沿著同一個顏色的石頭往上爬，其中不可以碰到其他路線的石頭。 4. 牆壁可以運用。 5.在其他石頭上若有同色岩點，則該石頭屬於可攀爬岩點。"
        pass

    if utterance == "[攀岩]有[規則]嗎": #[攀岩]有分[難度]嗎？"
        if args[0] not in userDefinedDICT["climbing"]:
            resultDICT["func_rule"] = "這跟攀岩無關，我不清楚耶"
        elif args[1] in userDefinedDICT["_rules"]:
            resultDICT["func_rule"] = "有的。請問是想了解基礎規則還是奧運比賽規則呢？"
        elif args[1] in userDefinedDICT["_levels"]:
            resultDICT["func_rule"] = "有的。市面上比較常看到抱石的等級劃分，分為V0-V16，級數越高，難度越高。一般岩館通常最高到V8，V9以上戶外場地居多。"
        else:
            resultDICT["func_rule"] = "我不知道耶"
        pass

    if utterance == "[攀岩]有[難度]之分嗎":
        if args[0] not in userDefinedDICT["climbing"]:
            resultDICT["func_rule"] = "這跟攀岩無關，我不清楚耶"
        else:
            resultDICT["func_rule"] = "有的。市面上比較常看到抱石的等級劃分，分為V0-V16，級數越高，難度越高。一般岩館通常最高到V8，V9以上戶外場地居多。"
        pass

    if utterance == "[攀岩]的[規則]是什麼":
        if args[0] not in userDefinedDICT["climbing"]:
            resultDICT["func_rule"] = "這跟攀岩無關，我不清楚耶"
        else:
            resultDICT["func_rule"] = "1.每條路線都有「起攀點」和一個「完攀點」。 2.雙手雙腳離地才算正式起攀。 3.沿著同一個顏色的石頭往上爬，其中不可以碰到其他路線的石頭。 4. 牆壁可以運用。 5.在其他石頭上若有同色岩點，則該石頭屬於可攀爬岩點。"
        pass

    if utterance == "怎麼知道[我]是哪個[等級]":
        resultDICT["func_rule"] = "爬過就知道了！"
        pass

    if utterance == "要怎麼知道[自己]的[等級]":
        resultDICT["func_rule"] = "爬過就知道了！"
        pass

    return resultDICT