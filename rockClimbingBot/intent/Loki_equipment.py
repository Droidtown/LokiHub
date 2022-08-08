#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for equipment

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

DEBUG_equipment = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_can":["可以","可","適合"],"_what":["什麼","哪些","什麼東西","哪些東西","哪種","哪幾間"],"_midTW":["苗栗","台中","彰化","南投"],"_pants":["褲子","褲","長褲","短褲","運動褲","瑜珈褲"],"_rocks":["岩點","石頭","手點","點"],"_rules":["規則","規範","法則","守則","規定"],"_shoes":["岩鞋","鞋子","攀岩鞋","抱石鞋","鞋"],"_sides":["東部","北部","南部","西部","中部"],"_which":["哪幾間","哪間","哪一間","哪些","哪個"],"_eastTW":["花蓮","台東"],"_levels":["難度","等級","階級"],"_clothes":["衣服","長袖","短袖","衣著","服裝","長袖衣服","上衣","短袖衣服","長袖上衣","短袖上衣","衣褲"],"_northTW":["基隆","台北","桃園","新竹","宜蘭","新北"],"_southTW":["雲林","嘉義","台南","高雄","屏東"],"_climbing":["攀岩","抱石","上攀","速度攀","速度攀登","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石攀岩"],"_cityAlias":["縣市","縣","市","地區","都市","城市","區","區域"],"_peClothes":["運動衣","運動褲","運動服","瑜珈褲","單車褲"],"_rockTypes":["jug","pinch","sloper","edge","crimp","pocket","flat","horn","volume"],"_appearance":["樣子","模樣"],"_climbingGym":["岩館","攀岩館","攀岩場","抱石館","抱石場館","抱石場","岩場","上攀館","上攀場","上攀場館"],"_climbingTop":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","上攀館","上攀場館","上攀岩館","先鋒攀岩館"],"_taiwanAlias":["全台","全臺","全台各地","台灣","臺灣","全臺各地"],"_taiwanCities":["雲林","嘉義","台南","高雄","屏東","花蓮","台東","基隆","台北","桃園","新竹","宜蘭","新北","苗栗","台中","彰化","南投"],"_climbingEquip":["裝","裝備","岩粉","粉袋","攀岩粉袋","粉球","止滑粉","攀岩粉","攀岩粉袋","岩點刷","攀岩刷","鎂粉球","鎂粉","碳酸鎂粉"],"_climbingSpeed":["速度攀","速度攀登","速度攀岩館","速度攀登場館"],"_topRopingEquip":["手套","確保手套","垂降手套","耐磨手套","安全吊帶","確保器","安全扣","快扣","安全扣環","吊帶"],"_climbingBoulder":["抱石","抱石攀岩","抱石館","抱石場館","抱石場"],"_climbingGeneralGym":["岩館","攀岩館","攀岩場","攀岩場館"]}

gymsInfo = pd.read_csv('climbingGym.csv', encoding = 'utf-8')
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_equipment:
        print("[equipment] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[可以]不買[裝備]嗎":
        if args[1] in userDefinedDICT["_climbingEquip"] or args[1] in userDefinedDICT["_shoes"]:
            resultDICT['func_equip'] = '可以哦！通常場館都會提供租借'
        elif args[1] in userDefinedDICT["pe_clothes"]:
            resultDICT['func_equip'] = '還是買一下會比較安全哦'
        elif args[1] in userDefinedDICT["top_roping_equip"]:
            resultDICT['func_equip'] = '如果常常上攀，推薦購買!'
        elif "帽" in args[1]:
            resultDICT["func_equip"] = '進行室內攀岩的話不需要哦'
        else:
            resultDICT['func_equip'] = '當然可以！攀岩不需要這個'
        pass

    if utterance == "[可以]穿[牛仔褲][攀岩]嗎":
        if args[1] not in userDefinedDICT['_pants'] and args[1] not in userDefinedDICT['_clothes'] and args[1] not in userDefinedDICT['pe_clothes']:
            resultDICT['func_equip'] = '最好不要，這樣會提高受傷機率'
        else:
            resultDICT['func_equip'] = '可以！穿'+args[1]+args[2]+'當然沒問題'
        pass

    if utterance == "[岩粉][可以]去哪買？":
        if args[0] in userDefinedDICT["_climbingEquip"]:
            resultDICT['func_equip'] = '通常岩館都有賣，也可易逛逛戶外休閒用品店或網路商店'
        elif args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT['func_equip'] = '通常可以上攀的岩館都有賣，也可易逛逛戶外休閒用品店或網路商店'
        elif arg[0] in userDefinedDICT["_shoes"] or arg[0] in userDefinedDICT["pe_clothes"]:
            resultDICT['func_equip'] = '戶外休閒用品店、迪卡儂，或是運動類型網路商店都有賣哦'
        else:
            resultDICT['func_equip'] = '這超出我能力範圍了'
        pass

    if utterance == "[岩粉]哪裡買得到？":
        if args[0] in userDefinedDICT["_climbingEquip"]:
            resultDICT['func_equip'] = '通常岩館都有賣，也可易逛逛戶外休閒用品店或網路商店'
        elif args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT['func_equip'] = '通常可以上攀的岩館都有賣，也可易逛逛戶外休閒用品店或網路商店'
        elif arg[0] in userDefinedDICT["shoes"] or arg[0] in userDefinedDICT["pe_clothes"]:
            resultDICT['func_equip'] = '戶外休閒用品店、迪卡儂，或是運動類型網路商店都有賣哦'
        else:
            resultDICT['func_equip'] = '這超出我能力範圍了'
        pass

    if utterance == "[岩鞋][大概]多少[錢]？":
        if args[0] in userDefinedDICT["_shoes"]:
            resultDICT['func_money'] = args[0]+'價錢介於1000~5000不等，可依預算和偏好考量入手鞋款'
        elif args[0] in userDefinedDICT["_climbingEquip"]:
            resultDICT['func_money'] = args[0]+'價錢大多低於1000，喜歡抱石可考慮入手哦'
        elif args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT['func_money'] = args[0]+'的價位大約是800~2000左右，建議對上攀真的很有興趣再入手'
        else:
            resultDICT['func_money'] = '這我不知道噎'  
        pass

    if utterance == "[攀岩][一定]要穿[運動服]嗎":
        if args[0] not in userDefinedDICT["_climbing"] or args[0] not in userDefinedDICT["_climbingGym"]:
            resultDICT["func_equip"] = "攀岩以外的我不太了解耶"
            pass
        if args[2] in userDefinedDICT["clothes"] or args[2] in userDefinedDICT["pants"] :
            resultDICT["func_equip"] = '建議穿著運動衣褲，才能降低受傷的機率'
        elif args[2] in userDefinedDICT["shoes"]:
            resultDICT["func_equip"] = '攀岩時會要求穿上岩鞋，比較好爬也確保安全'
        else:
            resultDICT["func_equip"] = '沒有一定'
        pass

    if utterance == "[攀岩]要帶什麼": #e.g.2 去岩館要帶什麼
        if args[0] in userDefinedDICT["_climbing"] or args[0] in userDefinedDICT["_climbinGym"] :
            resultDICT['func_equip'] = '穿著方便運動的衣褲，帶著水壺、緊急藥品和期待的心情，就可以開始'+args[0]+"囉！"
        else:
            resultDICT['func_equip'] = '這個超出我的能力範圍了'
        pass

    if utterance == "[攀岩]要準備什麼":
        if args[0] in userDefinedDICT["_climbing"] or args[0] in userDefinedDICT["_climbinGym"] :
            resultDICT['func_equip'] = '穿著方便運動的衣褲，帶著水壺、緊急藥品和期待的心情，就可以開始'+args[0]+"囉！"
        else:
            resultDICT['func_equip'] = '這個超出我的能力範圍了'
        pass

    if utterance == "[攀岩]要穿[長褲]還[短褲]？":
        if (args[1] in userDefinedDICT["_pants"] and args[2] in userDefinedDICT["_pants"]) or (args[1] in userDefinedDICT["_clothes"] and args[2] in userDefinedDICT["_clothes"]) or (args[1] in userDefinedDICT["_peClothes"] and args[2] in userDefinedDICT["_peClothes"]):
            resultDICT["func_equip"] = "都可以哦！只要是方便運動的衣著都好"
        elif "鞋" in args[1] and "鞋" in args[2]: # and ((args[1] not in userDefinedDICT["_shoes"] and args[2] in userDefinedDICT["_shoes"]) or (args[2] not in userDefinedDICT["_shoes"] and args[1] in userDefinedDICT["_shoes"])):
            resultDICT["func_equip"] = "一般室內攀岩會要求穿著岩鞋哦"
        else:
            resultDICT["func_equip"] = "建議穿著方便運動的服裝"
        pass

    if utterance == "[攀岩]要穿什麼":
        if args[0] in userDefinedDICT["_climbing"] or args[0] in userDefinedDICT["_climbinGym"] :
            resultDICT['func_equip'] = '穿著方便運動的衣褲，帶著水壺、緊急藥品和期待的心情，就可以開始'+args[0]+"囉！"
        else:
            resultDICT['func_equip'] = '這個超出我的能力範圍了'
        pass

    if utterance == "[攀岩]要買[鞋子]嗎":
        if args[0] not in userDefinedDICT["_climbing"] or args[0] not in userDefinedDICT["_climbingGym"]:
            resultDICT["func_equip"] = "攀岩以外的我不太了解耶"
            pass
        resultDICT["func_equip"] = '若是攀岩新手的話，可以直接穿運動衣褲進場哦！對攀岩有興趣後再慢慢入手鞋子、岩粉等裝備也不遲!'
        pass

    if utterance == "[攀岩]需要穿[運動褲]嗎":
        if args[0] not in userDefinedDICT["_climbing"]:
            resultDICT["func_equip"] = '這我不知道噎'
            pass
        if args[1] in userDefinedDICT["_peClothes"]:
            resultDICT["func_equip"] = '穿著比較安全哦'
        else:
            resultDICT["func_equip"] = '不用哦'
        pass

    if utterance == "[衣著]有限制嗎？":
        if args[0] in userDefinedDICT["_clothes"] or args[0] in userDefinedDICT["_pants"] :
            resultDICT["func_equip"] = '建議穿著運動衣褲，才能降低受傷的機率'
        elif args[0] in userDefinedDICT["_shoes"]:
            resultDICT["func_equip"] = '攀岩時會要求穿上岩鞋，比較好爬也確保安全'
        else:
            resultDICT["func_equip"] = '應該是沒有'
        pass

    if utterance == "哪些[裝備][一定]要買":
        resultDICT["func_equip"] = '若是攀岩新手的話，可以直接穿運動衣褲進場哦！對攀岩有興趣後再慢慢入手鞋子、岩粉等裝備也不遲!'
        pass

    if utterance == "穿[短袖][可以][攀岩]嗎":
        if args[0] not in userDefinedDICT["_climbing"] or args[0] not in userDefinedDICT["_climbingGym"]:
            resultDICT["func_equip"] = "攀岩以外的我不太了解耶"
            pass
        if args[0] in userDefinedDICT["_clothes"] or args[0] in userDefinedDICT["_pants"] :
            resultDICT["func_equip"] = '可以哦！只要是方便運動的穿著都可以'
        elif "鞋" in args[0] and args[0] not in userDefinedDICT["_shoes"]:
            resultDICT["func_equip"] = '攀岩時會要求穿上岩鞋，比較好爬也確保安全'
        elif "帽" in args[0]:
            resultDICT["func_equip"] = "室內攀岩用不到哦"
        else:
            resultDICT["func_equip"] = '最好不要，這樣會提高受傷機率'
        pass

    if utterance == "穿[短袖][可以]去[攀岩]嗎":
        if args[0] not in userDefinedDICT["_climbing"] or args[0] not in userDefinedDICT["_climbingGym"]:
            resultDICT["func_equip"] = "攀岩以外的我不太了解耶"
            pass
        if args[0] in userDefinedDICT["_clothes"] or args[0] in userDefinedDICT["_pants"] :
            resultDICT["func_equip"] = '可以哦！只要是方便運動的穿著都可以'
        elif "鞋" in args[0] and args[0] not in userDefinedDICT["_shoes"]:
            resultDICT["func_equip"] = '攀岩時會要求穿上岩鞋，比較好爬也確保安全'
        elif "帽" in args[0]:
            resultDICT["func_equip"] = "室內攀岩用不到哦"
        else:
            resultDICT["func_equip"] = '最好不要，這樣會提高受傷機率'
        pass

    return resultDICT