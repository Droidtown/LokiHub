#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Type

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Type = True
userDefinedDICT = {"D": ["設計", "d"], "I": ["發明", "i"], "M": ["新型", "m"], "G06Q_020_24": ["信用方案", "信用", "後付", "pay after", "24"], "G06Q_020_26": ["轉帳方案", "轉帳", "現付", "pay now", "26"], "G06Q_020_28": ["預付方案", "預付", "pay before", "28"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Type:
        print("[Type] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我]要看[發明]":
        if args[1].lower() in userDefinedDICT["D"]:
            resultDICT["Type"] = "_D"
            resultDICT["msg"] = "您想找什麼領域? (信用方案、轉帳方案、預付方案)"
        elif args[1].lower() in userDefinedDICT["I"]:
            resultDICT["Type"] = "_I"
            resultDICT["msg"] = "您想找什麼領域? (信用方案、轉帳方案、預付方案)"
        elif args[1].lower() in userDefinedDICT["M"]:
            resultDICT["Type"] = "_M"
            resultDICT["msg"] = "您想找什麼領域? (信用方案、轉帳方案、預付方案)"
        else:
            pass

    if utterance == "[發明]":
        if args[0].lower() in userDefinedDICT["D"]:
            resultDICT["Type"] = "_D"
            resultDICT["msg"] = "您想找什麼領域? (信用方案、轉帳方案、預付方案)"
        elif args[0].lower() in userDefinedDICT["I"]:
            resultDICT["Type"] = "_I"
            resultDICT["msg"] = "您想找什麼領域? (信用方案、轉帳方案、預付方案)"
        elif args[0].lower() in userDefinedDICT["M"]:
            resultDICT["Type"] = "_M"
            resultDICT["msg"] = "您想找什麼領域? (信用方案、轉帳方案、預付方案)"
        else:
            pass

    if utterance == "有[發明]的嗎":
        if args[0].lower() in userDefinedDICT["D"]:
            resultDICT["Type"] = "_D"
            resultDICT["msg"] = "您想找什麼領域? (信用方案、轉帳方案、預付方案)"
        elif args[0].lower() in userDefinedDICT["I"]:
            resultDICT["Type"] = "_I"
            resultDICT["msg"] = "您想找什麼領域? (信用方案、轉帳方案、預付方案)"
        elif args[0].lower() in userDefinedDICT["M"]:
            resultDICT["Type"] = "_M"
            resultDICT["msg"] = "您想找什麼領域? (信用方案、轉帳方案、預付方案)"
        else:
            pass

    if utterance == "查找[發明]":
        if args[0].lower() in userDefinedDICT["D"]:
            resultDICT["Type"] = "_D"
            resultDICT["msg"] = "您想找什麼領域? (信用方案、轉帳方案、預付方案)"
        elif args[0].lower() in userDefinedDICT["I"]:
            resultDICT["Type"] = "_I"
            resultDICT["msg"] = "您想找什麼領域? (信用方案、轉帳方案、預付方案)"
        elif args[0].lower() in userDefinedDICT["M"]:
            resultDICT["Type"] = "_M"
            resultDICT["msg"] = "您想找什麼領域? (信用方案、轉帳方案、預付方案)"
        else:
            pass

    if utterance == "[M]":
        if args[0].lower() in userDefinedDICT["D"]:
            resultDICT["Type"] = "_D"
            resultDICT["msg"] = "您想找什麼領域? (信用方案、轉帳方案、預付方案)"
        elif args[0].lower() in userDefinedDICT["I"]:
            resultDICT["Type"] = "_I"
            resultDICT["msg"] = "您想找什麼領域? (信用方案、轉帳方案、預付方案)"
        elif args[0].lower() in userDefinedDICT["M"]:
            resultDICT["Type"] = "_M"
            resultDICT["msg"] = "您想找什麼領域? (信用方案、轉帳方案、預付方案)"
        else:
            pass

    if utterance == "[我]想比對[轉帳]類別[下]跟[發明][相關]的專利":
        confusion = []
        for a in args[1:4]:
            if a.lower() in userDefinedDICT["D"]:
                confusion.append("_D")
            if a.lower() in userDefinedDICT["I"]:
                confusion.append("_I")
            if a.lower() in userDefinedDICT["M"]:
                confusion.append("_M")   
        if len(confusion) > 1:
            resultDICT["msg"] = "很抱歉，我不太清楚。請您再說明一次想比對哪個領域的專利文本，謝謝!"
        elif len(confusion) == 1:
            resultDICT["Type"] = confusion[0]  
        else:
            pass             
            
    return resultDICT