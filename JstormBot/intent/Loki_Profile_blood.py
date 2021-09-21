#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Profile_blood

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Profile_blood = True
userDefinedDICT = {"age": ["年長", "年幼"], "嵐": ["嵐", "ARASHI", "Arashi", "ARS", "Ars"], "粉": ["粉", "粉紅"], "date": ["年", "月", "日", "號", "周年"], "TOKIO": ["TOKIO", "東京小子", "T團"], "color": ["紅", "橙", "黃", "綠", "藍", "紫", "天藍"], "Jstorm": ["Jstorm", "J strom", "jstorm", "j storm", "JS", "js"], "黃綠": ["黃綠", "淺綠", "草綠", "淡綠"], "KAT-TUN": ["KAT-TUN", "KATTUN", "KT"], "城島茂": ["隊長", "城島茂", "城島", "茂", "茂茂"], "大野智": ["大野智", "隊長", "リーダー", "智智", "阿智", "野智", "大野", "智ちゃん", "智哥", "智くん"], "松本潤": ["松本潤", "松本", "潤", "J", "MJ", "潤潤", "弟弟", "潤監督", "總監", "潤總監", "阿潤", "潤ちゃん", "潤くん"], "櫻井翔": ["櫻井翔", "櫻井", "翔", "翔翔", "阿翔", "翔哥", "翔ちゃん", "翔くん"], "薮宏太": ["薮宏太", "薮", "宏太", "薮ちゃん", "薮くん", "薮さん", "やぶ", "阿薮", "薮先生", "薮帝王", "帝王", "やぶぶ"], "anniversary": ["結成日", "結成", "出道", "出道日", "生日"], "memberColor": ["代表色", "應援色", "成員色", "メンバーカラー", "顏色"], "上田竜也": ["上田竜也", "上田", "竜也", "上田龍也", "龍也", "老大", "吳愛達", "阿龍", "龍龍"], "中丸雄一": ["中丸雄一", "中丸", "雄一", "丸子"], "中島裕翔": ["中島裕翔", "中島", "裕翔", "yuto", "瘋兔子", "島哥", "副隊長", "yutti", "ゆってぃ"], "亀梨和也": ["亀梨和也", "亀梨", "和也", "龜梨", "龜梨和也", "龜龜", "亀亀", "卡咩", "Kame", "kame"], "二宮和也": ["二宮和也", "二宮", "和也", "NINO", "尼尼", "和總", "尼諾米", "NINOMI", "NINOちゃん"], "伊野尾慧": ["伊野尾慧", "伊野尾", "慧", "慧慧", "伊野尾ちゃん", "蘑菇", "阿慧", "慧哥", "慧老師"], "八乙女光": ["八乙女光", "八乙女", "光", "hika", "HIKA", "ひかる", "ひか", "やおちゃん", "阿光", "光光", "小光", "仙女", "小仙女"], "国分太一": ["國分", "太一", "國分太一", "国分太一", "国分"], "山田涼介": ["山田涼介", "山田", "涼介", "小涼", "小甜", "阿涼", "團霸", "yama"], "有岡大貴": ["有岡大貴", "有岡", "大貴", "阿貴", "貴貴", "大醬", "大ちゃん"], "松岡昌宏": ["松岡昌宏", "松岡", "昌宏", "松兄"], "相葉雅紀": ["相葉雅紀", "相葉", "雅紀", "愛拔", "大兔子", "相葉ちゃん"], "知念侑李": ["知念侑李", "知念", "侑李", "念念", "阿念", "小惡魔", "小野智", "Chi", "ちぃ", "ちっちゃん", "ねんち", "ちぃー", "知念くん", "知念ちゃん"], "髙木雄也": ["高木雄也", "髙木雄也", "雄也", "高木", "髙木", "yuya", "大雄", "大熊", "海", "ゆうちゃん", "髙木くん", "高木くん"], "Hey! Say! JUMP": ["Hey! Say! JUMP", "平成跳", "hsj", "HSJ", "JUMP", "跳跳", "醬噗"]}

import json
with open('D:\HAO\Hao的研所\實習\LokiHub\JstormBot\web_crawler\ProfileDICT.json', 'r') as f:
    ProfileDICT=json.load(f)
    
nicknameLIST=userDefinedDICT['城島茂']+userDefinedDICT['国分太一']+userDefinedDICT['松岡昌宏']+userDefinedDICT['大野智']+userDefinedDICT['松本潤']+userDefinedDICT['櫻井翔']+userDefinedDICT['二宮和也']+userDefinedDICT['相葉雅紀']+userDefinedDICT['上田竜也']+userDefinedDICT['中丸雄一']+userDefinedDICT['亀梨和也']+userDefinedDICT['薮宏太']+userDefinedDICT['八乙女光']+userDefinedDICT['伊野尾慧']+userDefinedDICT['山田涼介']+userDefinedDICT['有岡大貴']+userDefinedDICT['中島裕翔']+userDefinedDICT['知念侑李']+userDefinedDICT['髙木雄也']
groupLIST=userDefinedDICT['TOKIO']+userDefinedDICT['嵐']+userDefinedDICT['KAT-TUN']+userDefinedDICT['Hey! Say! JUMP']


tokio=['国分太一','城島茂','松岡昌宏']
arashi=['相葉雅紀','松本潤','二宮和也','大野智','櫻井翔']
kattun=['亀梨和也','上田竜也','中丸雄一']
jump=['山田涼介','知念侑李','中島裕翔','有岡大貴','髙木雄也','伊野尾慧','八乙女光','薮宏太']


def find_blood(group,blood):
    '''
    輸入:團名,血型
    輸出:人名
    '''
    name=[]
    for n in range(0,len(ProfileDICT[group])):
        if ProfileDICT[group][n]['Blood'].replace('型',"") == blood:
            name.append(ProfileDICT[group][n]['JName'])
        else:
            name.append('no')
    print(name)
    length=len(name)
    x=0
    while x < length:
        if name[x] == 'no':
            del name[x]
            x-= 1
            length -= 1
        x+=1
    if name == []:
        name = 'no'
    return name

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Profile_blood:
        print("[Profile_blood] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    bloodLIST=[]
    memberLIST=[]
    
    if utterance == "[KT]各是什麼[血型]":
        if args[0] in groupLIST and args[1] in '血型':
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    group=k
            
            if group == 'TOKIO':
                for n in range(0,len(tokio)):
                    bloodLIST.append(ProfileDICT['TOKIO'][n]['Blood'])    
                    memberLIST.append(ProfileDICT['TOKIO'][n]['JName'])    
                    
                resultDICT['Group']='TOKIO'
                resultDICT['member']=memberLIST
                resultDICT['request']=bloodLIST
                
            if group == '嵐':
                for n in range(0,len(arashi)):
                    bloodLIST.append(ProfileDICT['嵐'][n]['Blood']) 
                    memberLIST.append(ProfileDICT['嵐'][n]['JName']) 
                    
                resultDICT['Group']='嵐'
                resultDICT['member']=memberLIST
                resultDICT['request']=bloodLIST
                
            if group == 'KAT-TUN':
                for n in range(0,len(kattun)):
                    bloodLIST.append(ProfileDICT['KAT-TUN'][n]['Blood']) 
                    memberLIST.append(ProfileDICT['KAT-TUN'][n]['JName']) 
                resultDICT['Group']='KAT-TUN'
                resultDICT['member']=memberLIST
                resultDICT['request']=bloodLIST
                
            if group == 'Hey! Say! JUMP':
                for n in range(0,len(jump)):
                    bloodLIST.append(ProfileDICT['Hey! Say! JUMP'][n]['Blood']) 
                    memberLIST.append(ProfileDICT['Hey! Say! JUMP'][n]['JName']) 
                resultDICT['Group']='Hey! Say! JUMP'
                resultDICT['member']=memberLIST
                resultDICT['request']=bloodLIST
                
                
    if utterance == "[KT]有[O]型嗎":
        if args[0] in groupLIST and args[1] in 'ABO':
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    group=k
            
            member=find_blood(group, args[1])
            if member == 'no':
                resultDICT['Group']=group
                resultDICT['member']='no'
                resultDICT['request']=args[1]+'型'
            else:
                resultDICT['Group']=group
                resultDICT['member']=member
                resultDICT['request']=args[1]+'型'
            

    if utterance == "[KT]誰是[O]型":
        if args[0] in groupLIST and args[1] in 'ABO':
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    group=k
            
            member=find_blood(group, args[1])
            if member == 'no':
                resultDICT['Group']=group
                resultDICT['member']='no'
                resultDICT['request']=args[1]+'型'
            else:
                resultDICT['Group']=group
                resultDICT['member']=member
                resultDICT['request']=args[1]+'型'

    if utterance == "[知念侑李]是什麼[血型]":
        if args[0] in nicknameLIST and args[1] in '血型':
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    name=k
            
            if name in tokio:
                resultDICT['Group']='TOKIO'
                resultDICT['member']=name
                for n in range(0,len(tokio)):
                    if ProfileDICT['TOKIO'][n]['JName']==name:
                        resultDICT['request']=ProfileDICT['TOKIO'][n]['Blood']
            if name in arashi:
                resultDICT['Group']='嵐'
                resultDICT['member']=name
                for n in range(0,len(arashi)):
                    if ProfileDICT['嵐'][n]['JName']==name:
                        resultDICT['request']=ProfileDICT['嵐'][n]['Blood']
            if name in kattun:
                resultDICT['Group']='KAT-TUN'
                resultDICT['member']=name
                for n in range(0,len(kattun)):
                    if ProfileDICT['KAT-TUN'][n]['JName']==name:
                        resultDICT['request']=ProfileDICT['KAT-TUN'][n]['Blood']
            if name in jump:
                resultDICT['Group']='Hey! Say! JUMP'
                resultDICT['member']=name
                for n in range(0,len(jump)):
                    if ProfileDICT['Hey! Say! JUMP'][n]['JName']==name:
                        resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][n]['Blood']

    if utterance == "誰是[O]型":
        if args[0] in 'ABO':
            resultDICT['request']=args[0]+'型'

    return resultDICT