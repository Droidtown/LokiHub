#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Profile_born

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Profile_born = True
userDefinedDICT = {"age": ["年長", "年幼"], "嵐": ["嵐", "ARASHI", "Arashi", "ARS", "Ars"], "粉": ["粉", "粉紅"], "date": ["年", "月", "日", "號", "周年"], "TOKIO": ["TOKIO", "東京小子", "T團"], "color": ["紅", "橙", "黃", "綠", "藍", "紫", "天藍"], "Jstorm": ["Jstorm", "J strom", "jstorm", "j storm", "JS", "js"], "黃綠": ["黃綠", "淺綠", "草綠", "淡綠"], "KAT-TUN": ["KAT-TUN", "KATTUN", "KT"], "城島茂": ["隊長", "城島茂", "城島", "茂", "茂茂"], "大野智": ["大野智", "隊長", "リーダー", "智智", "阿智", "野智", "大野", "智ちゃん", "智哥", "智くん"], "松本潤": ["松本潤", "松本", "潤", "J", "MJ", "潤潤", "弟弟", "潤監督", "總監", "潤總監", "阿潤", "潤ちゃん", "潤くん"], "櫻井翔": ["櫻井翔", "櫻井", "翔", "翔翔", "阿翔", "翔哥", "翔ちゃん", "翔くん"], "薮宏太": ["薮宏太", "薮", "宏太", "薮ちゃん", "薮くん", "薮さん", "やぶ", "阿薮", "薮先生", "薮帝王", "帝王", "やぶぶ"], "anniversary": ["結成日", "結成", "出道", "出道日", "生日"], "memberColor": ["代表色", "應援色", "成員色", "メンバーカラー", "顏色"], "上田竜也": ["上田竜也", "上田", "竜也", "上田龍也", "龍也", "老大", "吳愛達", "阿龍", "龍龍"], "中丸雄一": ["中丸雄一", "中丸", "雄一", "丸子"], "中島裕翔": ["中島裕翔", "中島", "裕翔", "yuto", "瘋兔子", "島哥", "副隊長", "yutti", "ゆってぃ"], "亀梨和也": ["亀梨和也", "亀梨", "和也", "龜梨", "龜梨和也", "龜龜", "亀亀", "卡咩", "Kame", "kame"], "二宮和也": ["二宮和也", "二宮", "和也", "NINO", "尼尼", "和總", "尼諾米", "NINOMI", "NINOちゃん"], "伊野尾慧": ["伊野尾慧", "伊野尾", "慧", "慧慧", "伊野尾ちゃん", "蘑菇", "阿慧", "慧哥", "慧老師"], "八乙女光": ["八乙女光", "八乙女", "光", "hika", "HIKA", "ひかる", "ひか", "やおちゃん", "阿光", "光光", "小光", "仙女", "小仙女"], "国分太一": ["國分", "太一", "國分太一", "国分太一", "国分"], "山田涼介": ["山田涼介", "山田", "涼介", "小涼", "小甜", "阿涼", "團霸", "yama"], "有岡大貴": ["有岡大貴", "有岡", "大貴", "阿貴", "貴貴", "大醬", "大ちゃん"], "松岡昌宏": ["松岡昌宏", "松岡", "昌宏", "松兄"], "相葉雅紀": ["相葉雅紀", "相葉", "雅紀", "愛拔", "大兔子", "相葉ちゃん"], "知念侑李": ["知念侑李", "知念", "侑李", "念念", "阿念", "小惡魔", "小野智", "Chi", "ちぃ", "ちっちゃん", "ねんち", "ちぃー", "知念くん", "知念ちゃん"], "髙木雄也": ["高木雄也", "髙木雄也", "雄也", "高木", "髙木", "yuya", "大雄", "大熊", "海", "ゆうちゃん", "髙木くん", "高木くん"], "Hey! Say! JUMP": ["Hey! Say! JUMP", "平成跳", "hsj", "HSJ", "JUMP", "跳跳", "醬噗"]}

import json
with open('D:\HAO\Hao的研所\實習\LokiHub\JstormBot\web_crawler\ProfileDICT.json', 'r') as f:
    ProfileDICT=json.load(f)
    
nicknameLIST=userDefinedDICT['城島茂']+userDefinedDICT['国分太一']+userDefinedDICT['松岡昌宏']+userDefinedDICT['大野智']+userDefinedDICT['松本潤']+userDefinedDICT['櫻井翔']+userDefinedDICT['二宮和也']+userDefinedDICT['相葉雅紀']+userDefinedDICT['上田竜也']+userDefinedDICT['中丸雄一']+userDefinedDICT['亀梨和也']+userDefinedDICT['薮宏太']+userDefinedDICT['八乙女光']+userDefinedDICT['伊野尾慧']+userDefinedDICT['山田涼介']+userDefinedDICT['有岡大貴']+userDefinedDICT['中島裕翔']+userDefinedDICT['知念侑李']+userDefinedDICT['髙木雄也']
groupLIST=userDefinedDICT['TOKIO']+userDefinedDICT['嵐']+userDefinedDICT['KAT-TUN']+userDefinedDICT['Hey! Say! JUMP']
placeDICT={"北海道":"北海道","青森":"青森県","岩手":"岩手県","宮城":"宮城県","秋田":"秋田県","山形":"山形県","茨城":"茨城県","栃木":"栃木県","群馬":"群馬県","埼玉":"埼玉県","千葉":"千葉県","東京":"東京都","神奈川":"神奈川県","新潟":"新潟県","富山":"富山県","石川":"石川県","福井":"福井県","山梨":"山梨県","長野":"長野県","岐阜":"岐阜県","靜岡":"靜岡県","愛知":"愛知県","三重":"三重県","滋賀":"滋賀県","京都":"京都府","大阪":"大阪府","兵庫":"兵庫県","奈良":"奈良県","和歌山":"和歌山県","鳥取":"鳥取県","岡山":"岡山県","島根":"島根県","廣島":"廣島県","山口":"山口県","德島":"德島県","香川":"香川県","愛媛":"愛媛県","高知":"高知県","福岡":"福岡県","佐賀":"佐賀県","長崎":"長崎県","熊本":"熊本県","長崎":"長崎県","大分":"大分県","宮崎":"宮崎県","鹿兒島":"鹿兒島県","沖繩":"沖繩県"}


tokio=['国分太一','城島茂','松岡昌宏']
arashi=['相葉雅紀','松本潤','二宮和也','大野智','櫻井翔']
kattun=['亀梨和也','上田竜也','中丸雄一']
jump=['山田涼介','知念侑李','中島裕翔','有岡大貴','髙木雄也','伊野尾慧','八乙女光','薮宏太']


def find_born(group,place):
    '''
    輸入:團名,地名
    輸出:人名
    '''
    name=[]
    if place in placeDICT.keys():
        place=placeDICT[place]
    else:
        place=place
    for n in range(0,len(ProfileDICT[group])):
        if ProfileDICT[group][n]['Born'] == place:
            name.append(ProfileDICT[group][n]['JName'])
        else:
            name.append("")
    
    nameLIST=list(filter(None, name))
            
    return nameLIST
    

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Profile_born:
        print("[Profile_born] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    
    if utterance == "[八乙女光]是[宮城]人嗎":
        if args[0] in nicknameLIST:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    name=k
            
            if args[1] in placeDICT.keys() or placeDICT.values():
                if name in tokio:
                    for n in range(0,len(tokio)):
                        if ProfileDICT['TOKIO'][n]['JName'] == name:
                            if placeDICT[args[1]] == ProfileDICT['TOKIO'][n]['Born']:
                                resultDICT['Group']='TOKIO'
                                resultDICT['member']=name
                                resultDICT['request']='yes'
                            else:
                                resultDICT['Group']='TOKIO'
                                resultDICT['member']=name
                                resultDICT['request']=ProfileDICT['TOKIO'][n]['Born']
                                
            if args[1] in placeDICT.keys() or placeDICT.values():
                if name in arashi:
                    for n in range(0,len(arashi)):
                        if ProfileDICT['嵐'][n]['JName'] == name:
                            if placeDICT[args[1]] == ProfileDICT['嵐'][n]['Born']:
                                resultDICT['Group']='嵐'
                                resultDICT['member']=name
                                resultDICT['request']='yes'
                            else:
                                resultDICT['Group']='嵐'
                                resultDICT['member']=name
                                resultDICT['request']=ProfileDICT['嵐'][n]['Born']
                                
            if args[1] in placeDICT.keys() or placeDICT.values():
                if name in kattun:
                    for n in range(0,len(kattun)):
                        if ProfileDICT['KAT-TUN'][n]['JName'] == name:
                            if placeDICT[args[1]] == ProfileDICT['KAT-TUN'][n]['Born']:
                                resultDICT['Group']='KAT-TUN'
                                resultDICT['member']=name
                                resultDICT['request']='yes'
                            else:
                                resultDICT['Group']='KAT-TUN'
                                resultDICT['member']=name
                                resultDICT['request']=ProfileDICT['KAT-TUN'][n]['Born']

                                
            if args[1] in placeDICT.keys() or placeDICT.values():
                if name in jump:
                    for n in range(0,len(jump)):
                        if ProfileDICT['Hey! Say! JUMP'][n]['JName'] == name:
                            if placeDICT[args[1]] == ProfileDICT['Hey! Say! JUMP'][n]['Born']:
                                resultDICT['Group']='Hey! Say! JUMP'
                                resultDICT['member']=name
                                resultDICT['request']='yes'
                            else:
                                resultDICT['Group']='Hey! Say! JUMP'
                                resultDICT['member']=name
                                resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][n]['Born']
           
    if utterance == "[跳跳][裡]有誰來自[東京]":
        if args[0] in groupLIST :
            if args[2] in placeDICT.keys() or placeDICT.values():
                for k in userDefinedDICT.keys():
                    if args[0] in userDefinedDICT[k]:
                        group=k
            
            if args[2] in placeDICT.keys():
                place=placeDICT[args[2]]
            if args[2] in placeDICT.values():
                place=args[2]
                
            resultDICT['Group']=group
            resultDICT['request']=place
            if find_born(group,place) != []:
                resultDICT['member']=find_born(group,place)
            else:
                resultDICT['member']='no'

    if utterance == "[跳跳][裡]有誰是[東京]人":
        if args[0] in groupLIST :
            if args[2] in placeDICT.keys() or placeDICT.values():
                for k in userDefinedDICT.keys():
                    if args[0] in userDefinedDICT[k]:
                        group=k
            
            if args[2] in placeDICT.keys():
                place=placeDICT[args[2]]
            if args[2] in placeDICT.values():
                place=args[2]
                
            resultDICT['Group']=group
            resultDICT['request']=place
            if find_born(group,place) != []:
                resultDICT['member']=find_born(group,place)
            else:
                resultDICT['member']='no'
            
    if utterance == "[高木雄也]是哪裡人":
        if args[0] in nicknameLIST:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    name=k            
                    
        if name in tokio:
           resultDICT['Group']='TOKIO'
           resultDICT['member']=name
           for n in range(len(ProfileDICT['TOKIO'])):
               if name == ProfileDICT['TOKIO'][n]['JName']:
                   resultDICT['request']=ProfileDICT['TOKIO'][n]['Born']

        if name in arashi:
            resultDICT['Group']='嵐'
            resultDICT['member']=name
            for n in range(len(ProfileDICT['嵐'])):
               if name == ProfileDICT['嵐'][n]['JName']:
                   resultDICT['request']=ProfileDICT['嵐'][n]['Born']
                                
        if name in kattun:
            resultDICT['Group']='KAT-TUN'
            resultDICT['member']=name
            for n in range(len(ProfileDICT['KAT-TUN'])):
               if name == ProfileDICT['KAT-TUN'][n]['JName']:
                   resultDICT['request']=ProfileDICT['KAT-TUN'][n]['Born']
            
        if name in jump:
            resultDICT['Group']='Hey! Say! JUMP'
            resultDICT['member']=name
            for n in range(len(ProfileDICT['Hey! Say! JUMP'])):
               if name == ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                   resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][n]['Born']

    if utterance == "誰來自[東京]":
        if args[0] in placeDICT.keys() or placeDICT.values():            
            if args[0] in placeDICT.keys():
                place=placeDICT[args[0]]
            if args[0] in placeDICT.values():
                place=args[0]
                
            resultDICT['request']=place

    if utterance == "誰是[東京]人":
        if args[0] in placeDICT.keys() or placeDICT.values():            
            if args[0] in placeDICT.keys():
                place=placeDICT[args[0]]
            if args[0] in placeDICT.values():
                place=args[0]
                
            resultDICT['request']=place

    return resultDICT