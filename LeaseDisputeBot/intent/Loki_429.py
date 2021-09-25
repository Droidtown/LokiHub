#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for 429

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_429 = True
userDefinedDICT = {"副詞": ["任意", "隨意", "擅自", "隨便"], "動詞": ["過來", "過戶"], "名詞": ["房東", "房客"], "家電": ["抽油煙機", "電風扇", "電冰箱", "飲水機", "除濕機"], "房間配備": ["木地板", "壁紙", "自來水", "Wifi", "單人床墊", "床頭櫃", "單人床"], "法律用語": ["租金", "押租金", "修繕義務", "租賃契約", "出租人", "承租人", "次承租人", "轉租人"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_429:
        print("[429] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["confirm429_BOOL"] = None
    
    if utterance == "[他][只]說過[幾天][會][過來]了解":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[他]說[他][之後][會][過來]看看":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[他]說[以前][都]沒有這樣":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[冷氣]不[能]運轉":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[地板]腐爛":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[房間]漏水":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[木地板]腐蝕":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[東西]壞了":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[東西]壞掉":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[東西]損壞":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[牆壁]發霉滲水":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[磁磚]碎裂":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[紗窗]有破[洞]":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[紗窗]破掉":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[電風扇]故障":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "修繕":
        resultDICT["confirm429_BOOL"] = True 

    if utterance == "有[白蟻]腐蝕":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "沒有熱水":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "跟房東反應[他][都]擺爛不處理":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[我]的[房間][一直]在漏水":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[房東][都]不來修":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[房東][都]不修理":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[房東][都]不處理":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[房東][都]不解決":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[房東]叫我[自己]修":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "[房東]說[反正][我][也]不[會]用到":
        resultDICT["confirm429_BOOL"] = True

    if utterance == "壁癌":
        resultDICT["confirm429_BOOL"] = True

    return resultDICT