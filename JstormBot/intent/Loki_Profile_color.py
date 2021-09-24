#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Profile_color

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Profile_color = True
userDefinedDICT = {"age": ["年長", "年幼"], "嵐": ["嵐", "ARASHI", "Arashi", "ARS", "Ars"], "粉": ["粉", "粉紅"], "date": ["年", "月", "日", "號", "周年"], "TOKIO": ["TOKIO", "東京小子", "T團"], "color": ["紅", "橙", "黃", "綠", "藍", "紫", "天藍"], "Jstorm": ["Jstorm", "J strom", "jstorm", "j storm", "JS", "js"], "黃綠": ["黃綠", "淺綠", "草綠", "淡綠"], "KAT-TUN": ["KAT-TUN", "KATTUN", "KT"], "城島茂": ["隊長", "城島茂", "城島", "茂", "茂茂"], "大野智": ["大野智", "隊長", "リーダー", "智智", "阿智", "野智", "大野", "智ちゃん", "智哥", "智くん"], "松本潤": ["松本潤", "松本", "潤", "J", "MJ", "潤潤", "弟弟", "潤監督", "總監", "潤總監", "阿潤", "潤ちゃん", "潤くん"], "櫻井翔": ["櫻井翔", "櫻井", "翔", "翔翔", "阿翔", "翔哥", "翔ちゃん", "翔くん"], "薮宏太": ["薮宏太", "薮", "宏太", "薮ちゃん", "薮くん", "薮さん", "やぶ", "阿薮", "薮先生", "薮帝王", "帝王", "やぶぶ"], "anniversary": ["結成日", "結成", "出道", "出道日", "生日"], "memberColor": ["代表色", "應援色", "成員色", "メンバーカラー", "顏色"], "上田竜也": ["上田竜也", "上田", "竜也", "上田龍也", "龍也", "老大", "吳愛達", "阿龍", "龍龍"], "中丸雄一": ["中丸雄一", "中丸", "雄一", "丸子"], "中島裕翔": ["中島裕翔", "中島", "裕翔", "yuto", "瘋兔子", "島哥", "副隊長", "yutti", "ゆってぃ"], "亀梨和也": ["亀梨和也", "亀梨", "和也", "龜梨", "龜梨和也", "龜龜", "亀亀", "卡咩", "Kame", "kame"], "二宮和也": ["二宮和也", "二宮", "和也", "NINO", "尼尼", "和總", "尼諾米", "NINOMI", "NINOちゃん"], "伊野尾慧": ["伊野尾慧", "伊野尾", "慧", "慧慧", "伊野尾ちゃん", "蘑菇", "阿慧", "慧哥", "慧老師"], "八乙女光": ["八乙女光", "八乙女", "光", "hika", "HIKA", "ひかる", "ひか", "やおちゃん", "阿光", "光光", "小光", "仙女", "小仙女"], "国分太一": ["國分", "太一", "國分太一", "国分太一", "国分"], "山田涼介": ["山田涼介", "山田", "涼介", "小涼", "小甜", "阿涼", "團霸", "yama"], "有岡大貴": ["有岡大貴", "有岡", "大貴", "阿貴", "貴貴", "大醬", "大ちゃん"], "松岡昌宏": ["松岡昌宏", "松岡", "昌宏", "松兄"], "相葉雅紀": ["相葉雅紀", "相葉", "雅紀", "愛拔", "大兔子", "相葉ちゃん"], "知念侑李": ["知念侑李", "知念", "侑李", "念念", "阿念", "小惡魔", "小野智", "Chi", "ちぃ", "ちっちゃん", "ねんち", "ちぃー", "知念くん", "知念ちゃん"], "髙木雄也": ["高木雄也", "髙木雄也", "雄也", "高木", "髙木", "yuya", "大雄", "大熊", "海", "ゆうちゃん", "髙木くん", "高木くん"], "Hey! Say! JUMP": ["Hey! Say! JUMP", "平成跳", "hsj", "HSJ", "JUMP", "跳跳", "醬噗"]}

import json
with open('../web_crawler/ProfileDICT.json', 'r') as f:
    ProfileDICT=json.load(f)
    
nicknameLIST=userDefinedDICT['城島茂']+userDefinedDICT['国分太一']+userDefinedDICT['松岡昌宏']+userDefinedDICT['大野智']+userDefinedDICT['松本潤']+userDefinedDICT['櫻井翔']+userDefinedDICT['二宮和也']+userDefinedDICT['相葉雅紀']+userDefinedDICT['上田竜也']+userDefinedDICT['中丸雄一']+userDefinedDICT['亀梨和也']+userDefinedDICT['薮宏太']+userDefinedDICT['八乙女光']+userDefinedDICT['伊野尾慧']+userDefinedDICT['山田涼介']+userDefinedDICT['有岡大貴']+userDefinedDICT['中島裕翔']+userDefinedDICT['知念侑李']+userDefinedDICT['髙木雄也']
groupLIST=userDefinedDICT['TOKIO']+userDefinedDICT['嵐']+userDefinedDICT['KAT-TUN']+userDefinedDICT['Hey! Say! JUMP']

tokio=['国分太一','城島茂','松岡昌宏']
arashi=['相葉雅紀','松本潤','二宮和也','大野智','櫻井翔']
kattun=['亀梨和也','上田竜也','中丸雄一']
jump=['山田涼介','知念侑李','中島裕翔','有岡大貴','髙木雄也','伊野尾慧','八乙女光','薮宏太']

colorLIST=userDefinedDICT['color']+userDefinedDICT['粉']+userDefinedDICT['黃綠']


# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Profile_color:
        print("[Profile_color] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[代表色]是什麼":
        if args[0] in userDefinedDICT['memberColor']:
            resultDICT['request']='color'

    if utterance == "[慧慧]是什麼[顏色]":
        if args[0] in nicknameLIST and args[1] in userDefinedDICT['memberColor']:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    name=k
            if name in tokio:
                resultDICT['Group'] = 'TOKIO'
                resultDICT['member'] = name
                resultDICT['request'] = 'color'

    if utterance == "[阿智]是[藍]色嗎":
        if args[0] in nicknameLIST and args[1] in colorLIST:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    name=k
            
            if args[1] in userDefinedDICT['粉']:
                color = '粉'
            elif args[1] in userDefinedDICT['黃綠']:
                color = '黃綠'
            else:
                color = args[1]
                
            if name in tokio:
                index=tokio.index(name)
                if color == ProfileDICT['TOKIO'][index]['color']:
                    resultDICT['Group']='TOKIO'
                    resultDICT['member']=name
                    resultDICT['request']='yes'
                else:
                    resultDICT['Group']='TOKIO'
                    resultDICT['member']=name
                    resultDICT['request']=ProfileDICT['TOKIO'][index]['color']
            
            if name in arashi:
                index=arashi.index(name)
                if color == ProfileDICT['嵐'][index]['color']:
                    resultDICT['Group']='嵐'
                    resultDICT['member']=name
                    resultDICT['request']='yes'
                else:
                    resultDICT['Group']='嵐'
                    resultDICT['member']=name
                    resultDICT['request']=ProfileDICT['嵐'][index]['color']
                    
            if name in kattun:
                index=kattun.index(name)
                if color == ProfileDICT['KAT-TUN'][index]['color']:
                    resultDICT['Group']='KAT-TUN'
                    resultDICT['member']=name
                    resultDICT['request']='yes'
                else:
                    resultDICT['Group']='KAT-TUN'
                    resultDICT['member']=name
                    resultDICT['request']=ProfileDICT['KAT-TUN'][index]['color']
                    
            if name in jump:
                index=kattun.index(name)
                if color == ProfileDICT['Hey! Say! JUMP'][index]['color']:
                    resultDICT['Group']='Hey! Say! JUMP'
                    resultDICT['member']=name
                    resultDICT['request']='yes'
                else:
                    resultDICT['Group']='Hey! Say! JUMP'
                    resultDICT['member']=name
                    resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][index]['color']

    if utterance == "[雅紀]的[代表色]是[綠]色嗎":
        if args[0] in nicknameLIST and args[2] in colorLIST:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    name=k
            
            if args[2] in userDefinedDICT['粉']:
                color = '粉'
            elif args[2] in userDefinedDICT['黃綠']:
                color = '黃綠'
            else:
                color = args[2]
                
            if name in tokio:
                index=tokio.index(name)
                if color == ProfileDICT['TOKIO'][index]['color']:
                    resultDICT['Group']='TOKIO'
                    resultDICT['member']=name
                    resultDICT['request']='yes'
                else:
                    resultDICT['Group']='TOKIO'
                    resultDICT['member']=name
                    resultDICT['request']=ProfileDICT['TOKIO'][index]['color']
            
            if name in arashi:
                index=arashi.index(name)
                if color == ProfileDICT['嵐'][index]['color']:
                    resultDICT['Group']='嵐'
                    resultDICT['member']=name
                    resultDICT['request']='yes'
                else:
                    resultDICT['Group']='嵐'
                    resultDICT['member']=name
                    resultDICT['request']=ProfileDICT['嵐'][index]['color']
                    
            if name in kattun:
                index=kattun.index(name)
                if color == ProfileDICT['KAT-TUN'][index]['color']:
                    resultDICT['Group']='KAT-TUN'
                    resultDICT['member']=name
                    resultDICT['request']='yes'
                else:
                    resultDICT['Group']='KAT-TUN'
                    resultDICT['member']=name
                    resultDICT['request']=ProfileDICT['KAT-TUN'][index]['color']
                    
            if name in jump:
                index=kattun.index(name)
                if color == ProfileDICT['Hey! Say! JUMP'][index]['color']:
                    resultDICT['Group']='Hey! Say! JUMP'
                    resultDICT['member']=name
                    resultDICT['request']='yes'
                else:
                    resultDICT['Group']='Hey! Say! JUMP'
                    resultDICT['member']=name
                    resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][index]['color']

    if utterance == "各是什麼[顏色]":
        if args[0] in userDefinedDICT['memberColor']:
            resultDICT['request']='color.list'

    if utterance == "有人是[紅]色嗎":
        if args[0] in colorLIST:
            if args[0] in userDefinedDICT['粉']:
                color = '粉'
            elif args[0] in userDefinedDICT['黃綠']:
                color = '黃綠'
            else:
                color = args[0]
            resultDICT['request']=color
        else:
            resultDICT['request']='no.color'

    if utterance == "有哪些[應援色]":
        if args[0] in userDefinedDICT['memberColor']:
            resultDICT['request']='color.list'

    if utterance == "誰是[黃]色":
        if args[0] in colorLIST:
            if args[0] in userDefinedDICT['粉']:
                color = '粉'
            elif args[0] in userDefinedDICT['黃綠']:
                color = '黃綠'
            else:
                color = args[0]
            resultDICT['request']=color

    if utterance == "誰的[成員色]是[黃]色":
        if args[0] in userDefinedDICT['memberColor'] and args[1] in colorLIST:
            if args[0] in userDefinedDICT['粉']:
                color = '粉'
            elif args[0] in userDefinedDICT['黃綠']:
                color = '黃綠'
            else:
                color = args[0]
            resultDICT['request']=color

    return resultDICT