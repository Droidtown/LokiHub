#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for IPC_Number

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_IPC_Number = True
userDefinedDICT = {"D": ["設計", "d"], "I": ["發明", "i"], "M": ["新型", "m"], "G06Q_020_24": ["信用方案", "信用", "後付", "pay after", "24"], "G06Q_020_26": ["轉帳方案", "轉帳", "現付", "pay now", "26"], "G06Q_020_28": ["預付方案", "預付", "pay before", "28"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_IPC_Number:
        print("[IPC_Number] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "G06Q-020[24]":
        if args[0] in userDefinedDICT["G06Q_020_24"]:
            resultDICT["IPC_Number"] = "G06Q_020_24"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[0] in userDefinedDICT["G06Q_020_26"]:
            resultDICT["IPC_Number"] = "G06Q_020_26"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[0] in userDefinedDICT["G06Q_020_28"]:
            resultDICT["IPC_Number"] = "G06Q_020_28"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        else:
            pass

    if utterance == "[24]":
        if args[0] in userDefinedDICT["G06Q_020_24"]:
            resultDICT["IPC_Number"] = "G06Q_020_24"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[0] in userDefinedDICT["G06Q_020_26"]:
            resultDICT["IPC_Number"] = "G06Q_020_26"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[0] in userDefinedDICT["G06Q_020_28"]:
            resultDICT["IPC_Number"] = "G06Q_020_28"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        else:
            pass       
        
    if utterance == "[可以]找到[預付]的嗎":
        if args[1] in userDefinedDICT["G06Q_020_24"]:
            resultDICT["IPC_Number"]= "G06Q_020_24"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[1] in userDefinedDICT["G06Q_020_26"]:
            resultDICT["IPC_Number"] = "G06Q_020_26"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[1] in userDefinedDICT["G06Q_020_28"]:
            resultDICT["IPC_Number"] = "G06Q_020_28"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        else:
            pass

    if utterance == "[後付]的有哪些專利":
        if args[0] in userDefinedDICT["G06Q_020_24"]:
            resultDICT["IPC_Number"] = "G06Q_020_24"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[0] in userDefinedDICT["G06Q_020_26"]:
            resultDICT["IPC_Number"] = "G06Q_020_26"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[0] in userDefinedDICT["G06Q_020_28"]:
            resultDICT["IPC_Number"] = "G06Q_020_28"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        else:
            pass 

    if utterance == "[我]想要比對跟[轉帳][相關]的專利":
        if args[1] in userDefinedDICT["G06Q_020_24"]:
            resultDICT["IPC_Number"]= "G06Q_020_24"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[1] in userDefinedDICT["G06Q_020_26"]:
            resultDICT["IPC_Number"] = "G06Q_020_26"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[1] in userDefinedDICT["G06Q_020_28"]:
            resultDICT["IPC_Number"] = "G06Q_020_28"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        else:
            pass

    if utterance == "[我]要找[預付]的":
        if args[1] in userDefinedDICT["G06Q_020_24"]:
            resultDICT["IPC_Number"]= "G06Q_020_24"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[1] in userDefinedDICT["G06Q_020_26"]:
            resultDICT["IPC_Number"] = "G06Q_020_26"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[1] in userDefinedDICT["G06Q_020_28"]:
            resultDICT["IPC_Number"] = "G06Q_020_28"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        else:
            pass

    if utterance == "[轉帳]的有嗎":
        if args[0] in userDefinedDICT["G06Q_020_24"]:
            resultDICT["IPC_Number"] = "G06Q_020_24"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[0] in userDefinedDICT["G06Q_020_26"]:
            resultDICT["IPC_Number"] = "G06Q_020_26"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[0] in userDefinedDICT["G06Q_020_28"]:
            resultDICT["IPC_Number"] = "G06Q_020_28"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        else:
            pass 

    if utterance == "查[現付]的[相關]專利":
        if args[0] in userDefinedDICT["G06Q_020_24"]:
            resultDICT["IPC_Number"] = "G06Q_020_24"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[0] in userDefinedDICT["G06Q_020_26"]:
            resultDICT["IPC_Number"] = "G06Q_020_26"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[0] in userDefinedDICT["G06Q_020_28"]:
            resultDICT["IPC_Number"] = "G06Q_020_28"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        else:
            pass 

    if utterance == "跟[預付]系統有關的是誰":
        if args[0] in userDefinedDICT["G06Q_020_24"]:
            resultDICT["IPC_Number"] = "G06Q_020_24"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[0] in userDefinedDICT["G06Q_020_26"]:
            resultDICT["IPC_Number"] = "G06Q_020_26"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        elif args[0] in userDefinedDICT["G06Q_020_28"]:
            resultDICT["IPC_Number"] = "G06Q_020_28"
            resultDICT["msg"] = "您想找什麼類別? (設計、發明、新型)"
        else:
            pass 

    if utterance == "[我]想比對[轉帳]類別[下]跟[發明][相關]的專利":
        confusion = []
        for a in args[1:4]:
            if a in userDefinedDICT["G06Q_020_24"]:
                confusion.append("G06Q_020_24")
            if a in userDefinedDICT["G06Q_020_26"]:
                confusion.append("G06Q_020_26")
            if a in userDefinedDICT["G06Q_020_28"]:
                confusion.append("G06Q_020_28")
        if len(confusion) > 1:
            resultDICT["msg"] = "很抱歉，我不太清楚。請您再說明一次想比對哪個領域的專利文本，謝謝!"
        elif len(confusion) == 1:
            resultDICT["IPC_Number"] = confusion[0]
        else:
            pass
        
    return resultDICT