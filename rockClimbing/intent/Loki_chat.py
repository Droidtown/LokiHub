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

from random import choice
import json
import os

DEBUG_chat = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_pants":["單車褲","瑜珈褲","短褲","褲子","運動褲","長褲"],"_rocks":["岩石","岩點","手點","攀岩鞋","攀岩鞋子","石頭","點"],"_shoes":["岩鞋","抱石鞋","鞋子"],"_sides":["中部","北部","南部","東部","西部"],"_tmpFix":["規則"],"_whatIs":["星光票"],"_clothes":["上衣","服裝","短袖","短袖上衣","短袖衣服","衣服","衣著","衣褲","長袖","長袖上衣","長袖衣服"],"_climbing":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石","抱石攀岩","速度攀","速度攀登"],"_cityAlias":["區域","地區","城市","縣市","都市"],"_gymsShort":["8a攀岩場","B-plus","Boulder Space","Camp 4","Corner","Dapro","K2","MegaSTONE","POGO","TheDepotCity","Up聯盟","Y17","double 8","double8","久淘","千手抱石","原岩","嗨翻","嘉義攀岩會館","圓石","圓石空間","宜蘭運動中心","小岩館","崩岩","抱石基地","攀吶","新竹紅石","水美iClimb","汐止抱石館","爬森","破舊二廠","破舊工廠","禾匠","紅石","艾思博","蕃薯藤","角岩館","風城"],"_peClothes":["單車褲","瑜珈褲","運動服","運動衣","運動褲","運動鞋"],"_rockTypes":["crimp","edge","flat","horn","jug","pinch","pocket","sloper","volume"],"_climbingGym":["上攀場","上攀場館","上攀岩館","上攀館","先鋒攀岩館","岩場","岩館","抱石場","抱石場館","抱石館","攀岩場","攀岩館","攀石場","速度攀場地","速度攀場館","速度攀岩館","速度攀登場館","速度攀登岩館"],"_taiwanAlias":["全台","全台各地","全臺","全臺各地","台灣","臺灣"],"_climbingEquip":["岩粉","岩點刷","攀岩刷","攀岩粉","攀岩粉袋","止滑粉","碳酸鎂粉","粉球","粉袋","裝","裝備","鎂粉","鎂粉球"],"_normalWearings":["一般運動鞋","牛仔褲"],"_topRopingEquip":["吊帶","垂降手套","安全吊帶","安全扣","安全扣環","快扣","手套","確保器","確保手套","耐磨手套"],"_climbingGeneralGym":["岩館","攀岩場","攀岩場館","攀岩館"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_chat:
        print("[chat] {} ===> {}".format(inputSTR, utterance))


def _reply(key):
    responseDICT = {"[你][會]攀岩嗎":["當然啊！", "會哦", "會啊！"],
                    "[你]喜歡攀岩嗎？":["當然啊！", "喜歡啊！", "很喜歡"],
                    "[你]愛攀岩[麻]": ["當然！", "Yes！", "愛"],
                    "[我]不喜歡[上攀]":["我也是","這樣啊","為什麼？","謝謝你告訴我"],
                    "[我]喜歡[抱石]":["我也是!","我也喜歡","謝謝你告訴我"],
                    "攀岩":["請問想問什麼呢？", "想問什麼呢？","有什麼想問的呢？"],
                    "攀岩[好無聊]！":["這樣啊","為啥？","為什麼呢"],
                    "[攀岩鞋子]要買多[大]？":["要親自試過才知道哦"],
                    "[抱石][好玩]嗎":["當然！","好玩呀！","你覺得呢？"]

    }
    return choice(responseDICT[key])



def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[你][會]攀岩嗎":
        if args[0][0] in ("你", "妳", "您"):
            resultDICT["chat"] = _reply(utterance)

    if utterance == "[你]喜歡攀岩嗎？":
        if args[0][0] in ("你", "妳", "您"):
            resultDICT["chat"] = _reply(utterance)

    if utterance == "[你]愛攀岩[麻]":
        if args[0][0] in ("你", "妳", "您"):
            resultDICT["chat"] = _reply(utterance)

    if utterance == "[我]不喜歡[上攀]":
        if args[0][0] in ("我", "咱") and args[1] not in userDefinedDICT["_climbing"]:
            resultDICT["chat"] = _reply(utterance)

    if utterance == "[我]喜歡[抱石]":
        if args[0][0] in ("我", "咱") and args[1] not in userDefinedDICT["_climbing"]:
            resultDICT["chat"] = _reply(utterance)

    if utterance == "[抱石]":
        resultDICT["chat"] = utterance

    if utterance == "[抱石][好玩]嗎":
        resultDICT["chat"] = _reply(utterance)

    if utterance == "[抱石]要穿[長褲]還[短褲]？":
        resultDICT["chat"] = "以方便運動為主哦！"

    if utterance == "[攀岩鞋子]要買多[大]？":
        resultDICT["chat"] = _reply(utterance)

    if utterance == "攀岩":
        resultDICT["chat"] = _reply(utterance)

    if utterance == "攀岩[好無聊]！":
        resultDICT["chat"] = _reply(utterance)

    if utterance == "攀岩要穿[長褲]還[短褲]？":
        resultDICT["chat"] = "以方便運動為主哦！"

    return resultDICT