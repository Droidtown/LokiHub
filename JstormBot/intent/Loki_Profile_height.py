#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Profile_height

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
with open('../web_crawler/ProfileDICT.json', 'r') as f:
    ProfileDICT=json.load(f)

DEBUG_Profile_height = True
userDefinedDICT = {"age": ["年長", "年幼"], "嵐": ["嵐", "ARASHI", "Arashi", "ARS", "Ars"], "粉": ["粉", "粉紅"], "date": ["年", "月", "日", "號", "周年"], "TOKIO": ["TOKIO", "東京小子", "T團"], "color": ["紅", "橙", "黃", "綠", "藍", "紫", "天藍"], "Jstorm": ["Jstorm", "J strom", "jstorm", "j storm", "JS", "js"], "黃綠": ["黃綠", "淺綠", "草綠", "淡綠"], "KAT-TUN": ["KAT-TUN", "KATTUN", "KT"], "城島茂": ["隊長", "城島茂", "城島", "茂", "茂茂"], "大野智": ["大野智", "隊長", "リーダー", "智智", "阿智", "野智", "大野", "智ちゃん", "智哥", "智くん"], "松本潤": ["松本潤", "松本", "潤", "J", "MJ", "潤潤", "弟弟", "潤監督", "總監", "潤總監", "阿潤", "潤ちゃん", "潤くん"], "櫻井翔": ["櫻井翔", "櫻井", "翔", "翔翔", "阿翔", "翔哥", "翔ちゃん", "翔くん"], "薮宏太": ["薮宏太", "薮", "宏太", "薮ちゃん", "薮くん", "薮さん", "やぶ", "阿薮", "薮先生", "薮帝王", "帝王", "やぶぶ"], "anniversary": ["結成日", "結成", "出道", "出道日", "生日"], "memberColor": ["代表色", "應援色", "成員色", "メンバーカラー", "顏色"], "上田竜也": ["上田竜也", "上田", "竜也", "上田龍也", "龍也", "老大", "吳愛達", "阿龍", "龍龍"], "中丸雄一": ["中丸雄一", "中丸", "雄一", "丸子"], "中島裕翔": ["中島裕翔", "中島", "裕翔", "yuto", "瘋兔子", "島哥", "副隊長", "yutti", "ゆってぃ"], "亀梨和也": ["亀梨和也", "亀梨", "和也", "龜梨", "龜梨和也", "龜龜", "亀亀", "卡咩", "Kame", "kame"], "二宮和也": ["二宮和也", "二宮", "和也", "NINO", "尼尼", "和總", "尼諾米", "NINOMI", "NINOちゃん"], "伊野尾慧": ["伊野尾慧", "伊野尾", "慧", "慧慧", "伊野尾ちゃん", "蘑菇", "阿慧", "慧哥", "慧老師"], "八乙女光": ["八乙女光", "八乙女", "光", "hika", "HIKA", "ひかる", "ひか", "やおちゃん", "阿光", "光光", "小光", "仙女", "小仙女"], "国分太一": ["國分", "太一", "國分太一", "国分太一", "国分"], "山田涼介": ["山田涼介", "山田", "涼介", "小涼", "小甜", "阿涼", "團霸", "yama"], "有岡大貴": ["有岡大貴", "有岡", "大貴", "阿貴", "貴貴", "大醬", "大ちゃん"], "松岡昌宏": ["松岡昌宏", "松岡", "昌宏", "松兄"], "相葉雅紀": ["相葉雅紀", "相葉", "雅紀", "愛拔", "大兔子", "相葉ちゃん"], "知念侑李": ["知念侑李", "知念", "侑李", "念念", "阿念", "小惡魔", "小野智", "Chi", "ちぃ", "ちっちゃん", "ねんち", "ちぃー", "知念くん", "知念ちゃん"], "髙木雄也": ["高木雄也", "髙木雄也", "雄也", "高木", "髙木", "yuya", "大雄", "大熊", "海", "ゆうちゃん", "髙木くん", "高木くん"], "Hey! Say! JUMP": ["Hey! Say! JUMP", "平成跳", "hsj", "HSJ", "JUMP", "跳跳", "醬噗"]}

nicknameLIST=userDefinedDICT['城島茂']+userDefinedDICT['国分太一']+userDefinedDICT['松岡昌宏']+userDefinedDICT['大野智']+userDefinedDICT['松本潤']+userDefinedDICT['櫻井翔']+userDefinedDICT['二宮和也']+userDefinedDICT['相葉雅紀']+userDefinedDICT['上田竜也']+userDefinedDICT['中丸雄一']+userDefinedDICT['亀梨和也']+userDefinedDICT['薮宏太']+userDefinedDICT['八乙女光']+userDefinedDICT['伊野尾慧']+userDefinedDICT['山田涼介']+userDefinedDICT['有岡大貴']+userDefinedDICT['中島裕翔']+userDefinedDICT['知念侑李']+userDefinedDICT['髙木雄也']
groupLIST=userDefinedDICT['TOKIO']+userDefinedDICT['嵐']+userDefinedDICT['KAT-TUN']+userDefinedDICT['Hey! Say! JUMP']


tokio=['国分太一','城島茂','松岡昌宏']
arashi=['相葉雅紀','松本潤','二宮和也','大野智','櫻井翔']
kattun=['亀梨和也','上田竜也','中丸雄一']
jump=['山田涼介','知念侑李','中島裕翔','有岡大貴','髙木雄也','伊野尾慧','八乙女光','薮宏太']



# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Profile_height:
        print("[Profile_height] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    
    if utterance == "[KT]的誰[最高]":
        if args[0] in groupLIST and args[1][-1] in '高矮':
            heightLIST=[]
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    group=k
            for n in range(0,len(ProfileDICT[group])):
                heightLIST.append(ProfileDICT[group][n]['height'])
            
            if args[1][-1] == '高':
                tallest=heightLIST.index(max(heightLIST))
                resultDICT['Group']=group
                resultDICT['member']=ProfileDICT[group][tallest]['JName']
                resultDICT['request']=str(ProfileDICT[group][tallest]['height'])+"cm"
            else: #args[1][-1] == '矮'
                shortest=heightLIST.index(min(heightLIST))
                resultDICT['Group']=group
                resultDICT['member']=ProfileDICT[group][shortest]['JName']
                resultDICT['request']=str(ProfileDICT[group][shortest]['height'])+"cm"
            
    if utterance == "[最大]隻":
        if args[0][-1] in '大小':
            if args[0][-1] =='大':
                resultDICT['request']='height.max'
                
            else: #args[1][-1] == '小'
                resultDICT['request']='height.min'

    if utterance == "[最高]":
        if args[0][-1] in '高矮':
            if args[0][-1] =='高':
                resultDICT['request']='height.max'
            else: #args[1][-1] == '矮'
                resultDICT['request']='height.min'

    if utterance == "[最高]到[最矮]":
        if args[0][-1] and args[1][-1] in '高矮':
            if args[0][-1] =='高':
                resultDICT['request']='height.sort.HtoL'
            else: #args[1][-1] == '矮'
                resultDICT['request']='height.sort.LtoH'

    if utterance == "誰[最高]":
        if args[0][-1] in '高矮':
            if args[0][-1] =='高':
                resultDICT['request']='height.max'
            else: #args[1][-1] == '矮'
                resultDICT['request']='height.min'

    if utterance == "[KT]誰[最矮]":
        if args[0] in groupLIST and args[1][-1] in '高矮':
            heightLIST=[]
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    group=k
            for n in range(0,len(ProfileDICT[group])):
                heightLIST.append(ProfileDICT[group][n]['height'])
            
            if args[1][-1] == '高':
                tallest=heightLIST.index(max(heightLIST))
                resultDICT['Group']=group
                resultDICT['member']=ProfileDICT[group][tallest]['JName']
                resultDICT['request']=str(ProfileDICT[group][tallest]['height'])+'cm'
                
            else: #args[1][-1] == '矮'
                shortest=heightLIST.index(min(heightLIST))
                resultDICT['Group']=group
                resultDICT['member']=ProfileDICT[group][shortest]['JName']
                resultDICT['request']=str(ProfileDICT[group][shortest]['height'])+'cm'

    if utterance == "[他]多高":
        resultDICT['request']='height'

    if utterance == "[太一]多高":
        if args[0] in nicknameLIST:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    name=k
            
            if name in tokio:
                for n in range(0,len(ProfileDICT['TOKIO'])):
                    if ProfileDICT['TOKIO'][n]['JName'] == name:
                        resultDICT['Group']="TOKIO"
                        resultDICT['member']=name
                        resultDICT['request']=str(ProfileDICT['TOKIO'][n]['height'])+'cm'
                        
            if name in arashi:
                for n in range(0,len(ProfileDICT['嵐'])):
                    if ProfileDICT['嵐'][n]['JName'] == name:
                        resultDICT['Group']="嵐"
                        resultDICT['member']=name
                        resultDICT['request']=str(ProfileDICT['嵐'][n]['height'])+'cm'
            
            if name in kattun:
                for n in range(0,len(ProfileDICT['KAT-TUN'])):
                    if ProfileDICT['KAT-TUN'][n]['JName'] == name:
                        resultDICT['Group']="KAT-TUN"
                        resultDICT['member']=name
                        resultDICT['request']=str(ProfileDICT['KAT-TUN'][n]['height'])+'cm'
                        
            if name in jump:
                for n in range(0,len(ProfileDICT['Hey! Say! JUMP'])):
                    if ProfileDICT['Hey! Say! JUMP'][n]['JName'] == name:
                        resultDICT['Group']="Hey! Say! JUMP"
                        resultDICT['member']=name
                        resultDICT['request']=str(ProfileDICT['Hey! Say! JUMP'][n]['height'])+'cm'

    if utterance == "[太一]的[身高]是多少":
        if args[0] in nicknameLIST:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    name=k
            
            if name in tokio:
                for n in range(0,len(ProfileDICT['TOKIO'])):
                    if ProfileDICT['TOKIO'][n]['JName'] == name:
                        resultDICT['Group']="TOKIO"
                        resultDICT['member']=name
                        resultDICT['request']=str(ProfileDICT['TOKIO'][n]['height'])+'cm'
                        
            if name in arashi:
                for n in range(0,len(ProfileDICT['嵐'])):
                    if ProfileDICT['嵐'][n]['JName'] == name:
                        resultDICT['Group']="嵐"
                        resultDICT['member']=name
                        resultDICT['request']=str(ProfileDICT['嵐'][n]['height'])+'cm'
            
            if name in kattun:
                for n in range(0,len(ProfileDICT['KAT-TUN'])):
                    if ProfileDICT['KAT-TUN'][n]['JName'] == name:
                        resultDICT['Group']="KAT-TUN"
                        resultDICT['member']=name
                        resultDICT['request']=str(ProfileDICT['KAT-TUN'][n]['height'])+"cm"
                        
            if name in jump:
                for n in range(0,len(ProfileDICT['Hey! Say! JUMP'])):
                    if ProfileDICT['Hey! Say! JUMP'][n]['JName'] == name:
                        resultDICT['Group']="Hey! Say! JUMP"
                        resultDICT['member']=name
                        resultDICT['request']=str(ProfileDICT['Hey! Say! JUMP'][n]['height'])+'cm'

    return resultDICT