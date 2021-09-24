#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Group

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
with open('..\web_crawler\ProfilePic.json', 'r') as f:
    ProfilePic=json.load(f)

with open('..\web_crawler\GroupDICT.json', 'r') as f:
    GroupDICT=json.load(f)

DEBUG_Group = True
userDefinedDICT = {"age": ["年長", "年幼"], "嵐": ["嵐", "ARASHI", "Arashi", "ARS", "Ars"], "粉": ["粉", "粉紅"], "date": ["年", "月", "日", "號", "周年"], "TOKIO": ["TOKIO", "東京小子", "T團"], "color": ["紅", "橙", "黃", "綠", "藍", "紫", "天藍"], "Jstorm": ["Jstorm", "J strom", "jstorm", "j storm", "JS", "js"], "黃綠": ["黃綠", "淺綠", "草綠", "淡綠"], "KAT-TUN": ["KAT-TUN", "KATTUN", "KT"], "城島茂": ["隊長", "城島茂", "城島", "茂", "茂茂"], "大野智": ["大野智", "隊長", "リーダー", "智智", "阿智", "野智", "大野", "智ちゃん", "智哥", "智くん"], "松本潤": ["松本潤", "松本", "潤", "J", "MJ", "潤潤", "弟弟", "潤監督", "總監", "潤總監", "阿潤", "潤ちゃん", "潤くん"], "櫻井翔": ["櫻井翔", "櫻井", "翔", "翔翔", "阿翔", "翔哥", "翔ちゃん", "翔くん"], "薮宏太": ["薮宏太", "薮", "宏太", "薮ちゃん", "薮くん", "薮さん", "やぶ", "阿薮", "薮先生", "薮帝王", "帝王", "やぶぶ"], "anniversary": ["結成日", "結成", "出道", "出道日", "生日"], "memberColor": ["代表色", "應援色", "成員色", "メンバーカラー", "顏色"], "上田竜也": ["上田竜也", "上田", "竜也", "上田龍也", "龍也", "老大", "吳愛達", "阿龍", "龍龍"], "中丸雄一": ["中丸雄一", "中丸", "雄一", "丸子"], "中島裕翔": ["中島裕翔", "中島", "裕翔", "yuto", "瘋兔子", "島哥", "副隊長", "yutti", "ゆってぃ"], "亀梨和也": ["亀梨和也", "亀梨", "和也", "龜梨", "龜梨和也", "龜龜", "亀亀", "卡咩", "Kame", "kame"], "二宮和也": ["二宮和也", "二宮", "和也", "NINO", "尼尼", "和總", "尼諾米", "NINOMI", "NINOちゃん"], "伊野尾慧": ["伊野尾慧", "伊野尾", "慧", "慧慧", "伊野尾ちゃん", "蘑菇", "阿慧", "慧哥", "慧老師"], "八乙女光": ["八乙女光", "八乙女", "光", "hika", "HIKA", "ひかる", "ひか", "やおちゃん", "阿光", "光光", "小光", "仙女", "小仙女"], "国分太一": ["國分", "太一", "國分太一", "国分太一", "国分"], "山田涼介": ["山田涼介", "山田", "涼介", "小涼", "小甜", "阿涼", "團霸", "yama"], "有岡大貴": ["有岡大貴", "有岡", "大貴", "阿貴", "貴貴", "大醬", "大ちゃん"], "松岡昌宏": ["松岡昌宏", "松岡", "昌宏", "松兄"], "相葉雅紀": ["相葉雅紀", "相葉", "雅紀", "愛拔", "大兔子", "相葉ちゃん"], "知念侑李": ["知念侑李", "知念", "侑李", "念念", "阿念", "小惡魔", "小野智", "Chi", "ちぃ", "ちっちゃん", "ねんち", "ちぃー", "知念くん", "知念ちゃん"], "髙木雄也": ["高木雄也", "髙木雄也", "雄也", "高木", "髙木", "yuya", "大雄", "大熊", "海", "ゆうちゃん", "髙木くん", "高木くん"], "Hey! Say! JUMP": ["Hey! Say! JUMP", "平成跳", "hsj", "HSJ", "JUMP", "跳跳", "醬噗"]}

groupLIST=userDefinedDICT['KAT-TUN']+userDefinedDICT['TOKIO']+userDefinedDICT['嵐']+userDefinedDICT['Hey! Say! JUMP']
Jstorm=["TOKIO","嵐","KAT-TUN","Hey! Say! JUMP"]

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Group:
        print("[Group] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[Jstorm][旗下]有哪些[團體]":
        if args[0] in userDefinedDICT['Jstorm']:
            resultDICT['Group']=Jstorm
            resultDICT['request']=len(Jstorm)
        else:
            pass

    if utterance == "[Jstorm][旗下]有幾[個][團體]":
        if args[0] in userDefinedDICT['Jstorm']:
            resultDICT['Group']=Jstorm
            resultDICT['request']=len(Jstorm)
        else:
            pass

    if utterance == "[Jstorm]有幾[團]":
        if args[0] in userDefinedDICT['Jstorm']:
            resultDICT['Group']=Jstorm
            resultDICT['request']=len(Jstorm)
        else:
            pass

    if utterance == "[出道日]是什麼[時候]":
        if args[0] == '出道日':
            resultDICT['request']='debutdate'
        elif args[0] == '結成日':
            resultDICT['request']='formationdate'

    if utterance == "[嵐]":
        if args[0] in groupLIST:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    group=k
            resultDICT['Group']=group

    if utterance == "[嵐]是[Jstorm]的嗎":
        if args[1] in userDefinedDICT['Jstorm']:
            if args[0] in groupLIST:
                for k in userDefinedDICT.keys():
                    if args[0] in userDefinedDICT[k]:
                        key=k
                if key in Jstorm:
                    resultDICT['Group']=key
                    resultDICT['request']='yes'
            else:
                resultDICT['Group']=args[0]
                resultDICT['request']='no'

    if utterance == "[旗下]有誰":
        resultDICT['Group']=Jstorm
        resultDICT['request']=ProfilePic

    if utterance == "[結成]幾[年]":
        if args[0] in ("結成","出道") and args[1] in ("年","周年","週年"):
            if  args[0]=='出道':
                resultDICT['request']='debutdate.years'
            elif args[0]=='結成':
                resultDICT['request']='formationdat.years'

    if utterance == "[結成日]是何時":
        if args[0] == '出道日':
            resultDICT['request']='debutdate'
        elif args[0] == '結成日':
            resultDICT['request']='formationdate'

    if utterance == "有哪些[團體]":
        resultDICT['Group']=Jstorm
        resultDICT['request']=ProfilePic

    if utterance == "離[出道日]還有[幾天]":
        if args[0]=='出道日':
            resultDICT['request']='debutdate.days'
        elif args[0]=='結成日':
            resultDICT['request']='formationdate.days'

    return resultDICT