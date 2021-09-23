#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Security_Deposit

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Security_Deposit = True
userDefinedDICT = {"副詞": ["任意", "隨意", "擅自", "隨便"], "動詞": ["過來", "過戶", "出租", "承租", "租"], "名詞": ["房東", "房客", "押金", "凶宅"], "家電": ["抽油煙機", "電風扇", "電冰箱", "飲水機", "除濕機"], "房間配備": ["木地板", "壁紙", "自來水", "Wifi", "單人床墊", "床頭櫃", "單人床", "天花板"], "法律用語": ["租金", "押租金", "修繕義務", "租賃契約", "出租人", "承租人", "次承租人", "轉租人"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Security_Deposit:
        print("[Security_Deposit] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["confirm_Security_Deposit_BOOL"] = None
   
    if utterance == "[我]想要拿回[我]的押金":
        resultDICT["confirm_Security_Deposit_BOOL"] = True
        
   
    if utterance == "[我]的押金被房東扣了":
        resultDICT["confirm_Security_Deposit_BOOL"] = True

   
    if utterance == "[故意]不退還押金":
        resultDICT["confirm_Security_Deposit_BOOL"] = True

   
    if utterance == "[遲遲]未收到押金":
        resultDICT["confirm_Security_Deposit_BOOL"] = True

   
    if utterance == "不退[我]押金":
        resultDICT["confirm_Security_Deposit_BOOL"] = True

   
    if utterance == "不還[我]押金":
        resultDICT["confirm_Security_Deposit_BOOL"] = True

   
    if utterance == "亂扣[我]押金":
        resultDICT["confirm_Security_Deposit_BOOL"] = True
        
   
    if utterance == "吃掉[我]的押金":
        resultDICT["confirm_Security_Deposit_BOOL"] = True

  
    if utterance == "惡意亂扣[我]押金":
        resultDICT["confirm_Security_Deposit_BOOL"] = True

   
    if utterance == "扣[我][兩個月]押金":
        resultDICT["confirm_Security_Deposit_BOOL"] = True

   
    if utterance == "扣[我]押金":
        resultDICT["confirm_Security_Deposit_BOOL"] = True

   
    if utterance == "把押金拿回來":
        resultDICT["confirm_Security_Deposit_BOOL"] = True

    
    if utterance == "押金還在房東那":
        resultDICT["confirm_Security_Deposit_BOOL"] = True

   
    if utterance == "拿回[我]的押金":
        resultDICT["confirm_Security_Deposit_BOOL"] = True

   
    if utterance == "拿回押金":
        resultDICT["confirm_Security_Deposit_BOOL"] = True

    return resultDICT