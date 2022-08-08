#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for chat

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

DEBUG_chat = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_can":["可以","可","適合"],"_what":["什麼","哪些","什麼東西","哪些東西","哪種","哪幾間"],"_midTW":["苗栗","台中","彰化","南投"],"_pants":["褲子","褲","長褲","短褲","運動褲","瑜珈褲"],"_rocks":["岩點","石頭","手點","點"],"_rules":["規則","規範","法則","守則","規定"],"_shoes":["岩鞋","鞋子","攀岩鞋","抱石鞋","鞋"],"_sides":["東部","北部","南部","西部","中部"],"_which":["哪幾間","哪間","哪一間","哪些","哪個"],"_eastTW":["花蓮","台東"],"_levels":["難度","等級","階級"],"_clothes":["衣服","長袖","短袖","衣著","服裝","長袖衣服","上衣","短袖衣服","長袖上衣","短袖上衣","衣褲"],"_northTW":["基隆","台北","桃園","新竹","宜蘭","新北"],"_southTW":["雲林","嘉義","台南","高雄","屏東"],"_climbing":["攀岩","抱石","上攀","速度攀","速度攀登","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石攀岩"],"_cityAlias":["縣市","縣","市","地區","都市","城市","區","區域"],"_peClothes":["運動衣","運動褲","運動服","瑜珈褲","單車褲"],"_rockTypes":["jug","pinch","sloper","edge","crimp","pocket","flat","horn","volume"],"_appearance":["樣子","模樣"],"_climbingGym":["岩館","攀岩館","攀岩場","抱石館","抱石場館","抱石場","岩場","上攀館","上攀場","上攀場館"],"_climbingTop":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","上攀館","上攀場館","上攀岩館","先鋒攀岩館"],"_taiwanAlias":["全台","全臺","全台各地","台灣","臺灣","全臺各地"],"_taiwanCities":["雲林","嘉義","台南","高雄","屏東","花蓮","台東","基隆","台北","桃園","新竹","宜蘭","新北","苗栗","台中","彰化","南投"],"_climbingEquip":["裝","裝備","岩粉","粉袋","攀岩粉袋","粉球","止滑粉","攀岩粉","攀岩粉袋","岩點刷","攀岩刷","鎂粉球","鎂粉","碳酸鎂粉"],"_climbingSpeed":["速度攀","速度攀登","速度攀岩館","速度攀登場館"],"_topRopingEquip":["手套","確保手套","垂降手套","耐磨手套","安全吊帶","確保器","安全扣","快扣","安全扣環","吊帶"],"_climbingBoulder":["抱石","抱石攀岩","抱石館","抱石場館","抱石場"],"_climbingGeneralGym":["岩館","攀岩館","攀岩場","攀岩場館"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_chat:
        print("[chat] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[你]喜歡[攀岩]嗎？":
        if args[1] in userDefinedDICT["_climbing"]:
            resultDICT["func_chat"] = "當然！"
        else:
            resultDICT["func_chat"] = "那什麼？你喜歡嗎？"
        pass

    if utterance == "[你]愛[攀岩][麻]":
        if args[1] in userDefinedDICT["_climbing"]:
            resultDICT["func_chat"] = "當然！"
        else:
            resultDICT["func_chat"] = "那什麼？你喜歡嗎？"
        pass

    if utterance == "[我]不喜歡[上攀]":
        if args[1] in userDefinedDICT["_climbing"]:
            resultDICT["func_chat"] = "為什麼？"
        else:
            resultDICT["func_chat"] = "那什麼？"
        pass

    if utterance == "[抱石][好玩]嗎":
        if args[0] in userDefinedDICT["_climbing"]:
            resultDICT["func_chat"] = args[1]
        else:
            resultDICT["func_chat"] = "那什麼？"
        pass

    if utterance == "[攀岩][好無聊]！":
        if args[1] in userDefinedDICT["_climbing"]:
            resultDICT["func_chat"] = "為什麼？"
        else:
            resultDICT["chat"] = "那什麼？"
        pass
    if utterance == "[攀岩]":
        if args[1] in userDefinedDICT["_climbing"] or args[1] in userDefinedDICT["_climbingGym"] or args[1] in userDefinedDICT["_climbingEquip"] or args[1] in userDefinedDICT["_topRopingEquip"] or args[1] in userDefinedDICT["_rockTypes"]:
            resultDICT["func_chat"] = "想問什麼呢？"
        else:
            resultDICT["func_chat"] = "這似乎跟攀岩沒有關係呢"
    return resultDICT