#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for 429_tb1

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_429_tb1 = True
userDefinedDICT = {"副詞": ["任意", "隨意", "擅自", "隨便"], "動詞": ["過來", "過戶"], "名詞": ["房東", "房客"], "家電": ["抽油煙機", "電風扇", "電冰箱", "飲水機", "除濕機"], "房間配備": ["木地板", "壁紙", "自來水", "Wifi", "單人床墊", "床頭櫃", "單人床"], "法律用語": ["租金", "押租金", "修繕義務", "租賃契約", "出租人", "承租人", "次承租人", "轉租人"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_429_tb1:
        print("[429_tb1] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["confirm429tb1_BOOL"] = None
    
    if utterance == "[上面]寫房東要負責":
        resultDICT["confirm429tb1_BOOL"] = False

    if utterance == "有":
        resultDICT["confirm429tb1_BOOL"] = True        

    if utterance == "沒有":
        resultDICT["confirm429tb1_BOOL"] = False        

    if utterance == "約好房東要負責修繕":
        resultDICT["confirm429tb1_BOOL"] = False

    if utterance == "房東要修":
        resultDICT["confirm429tb1_BOOL"] = False

    if utterance == "房東要負責修":
        resultDICT["confirm429tb1_BOOL"] = False

    if utterance == "說好[他]要負責修":
        resultDICT["confirm429tb1_BOOL"] = False

    return resultDICT