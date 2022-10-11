#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for searching

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

# local import
import function as fun


DEBUG_searching = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_key":["收入","支出","記帳狀況"],"_park":["六福村","九族文化村","義大","義大世界"],"_money":["錢","台幣","元"],"_income_key":["收入"],"_allcome_key":["記帳","財富"],"_outcome_key":["支出","消費","花費"]}



intent = "searching"

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_searching:
        print("[searching] {} ===> {}".format(inputSTR, utterance))

def getResult(userID, inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    if utterance == "查詢[收入]":
        if args[0] in userDefinedDICT["_outcome_key"]:
            result = fun.GetDataByCondition(userID, "cost")
        elif args[0] in userDefinedDICT["_income_key"]:
            result = fun.GetDataByCondition(userID, "earn")
        elif args[0] in userDefinedDICT["_allcome_key"]:
            result = fun.GetDataByCondition(userID, "all")

    if utterance == "[我][今年][總共]花了多少[錢]":
        if not fun.CorrectCurrency(args[3],userDefinedDICT["_money"]):
            result = "error_currency"
        else:
            result = fun.GetDataByCondition(userID, "cost", fun.GetTimeSpan(args[1]))

    if utterance == "[我][今年][總共]賺了多少[錢]":
        if not fun.CorrectCurrency(args[3],userDefinedDICT["_money"]):
            result = "error_currency"
        result = fun.GetDataByCondition(userID, "earn", fun.GetTimeSpan(args[1]))

    if utterance == "[我][總共]花了多少[錢]":
        if not fun.CorrectCurrency(args[2],userDefinedDICT["_money"]):
            result = "error_currency"
        result = fun.GetDataByCondition(userID, "cost")

    if utterance == "[我][總共]賺了多少[錢]":
        if not fun.CorrectCurrency(args[2],userDefinedDICT["_money"]):
            result = "error_currency"
        result = fun.GetDataByCondition(userID, "earn")

    if utterance == "[我][這個][月][總共]花了多少[錢]":
        if not fun.CorrectCurrency(args[4],userDefinedDICT["_money"]):
            result = "error_currency"
        result = fun.GetDataByCondition(userID, "cost", fun.GetTimeSpan("_articut_failed_",[args[1],args[2]]))

    if utterance == "[我][這個][月][總共]賺了多少[錢]":
        if not fun.CorrectCurrency(args[4],userDefinedDICT["_money"]):
            result = "error_currency"
        result = fun.GetDataByCondition(userID, "earn", fun.GetTimeSpan("_articut_failed_", [args[1],args[2]]))

    if utterance == "查詢[今日][收入]":
        if args[1] in userDefinedDICT["_outcome_key"]:
            result = fun.GetDataByCondition(userID, "cost", fun.GetTimeSpan(args[0]))
        elif args[1] in userDefinedDICT["_income_key"]:
            result = fun.GetDataByCondition(userID, "earn", fun.GetTimeSpan(args[0]))
        elif args[1] in userDefinedDICT["_allcome_key"]:
            result = fun.GetDataByCondition(userID, "all", fun.GetTimeSpan(args[0]))

    if utterance == "查詢[今日][總][收入]":
        if args[2] in userDefinedDICT["_outcome_key"]:
            result = fun.GetDataByCondition(userID, "cost", fun.GetTimeSpan(args[0]))
        elif args[2] in userDefinedDICT["_income_key"]:
            result = fun.GetDataByCondition(userID, "earn", fun.GetTimeSpan(args[0]))
        elif args[2] in userDefinedDICT["_allcome_key"]:
            result = fun.GetDataByCondition(userID, "all", fun.GetTimeSpan(args[0]))

    if utterance == "查詢[總][收入]":
        if args[1] in userDefinedDICT["_outcome_key"]:
            result = fun.GetDataByCondition(userID, "cost")
        elif args[1] in userDefinedDICT["_income_key"]:
            result = fun.GetDataByCondition(userID, "earn")
        elif args[1] in userDefinedDICT["_allcome_key"]:
            result = fun.GetDataByCondition(userID, "all")
            
    if utterance == "查詢[這個][月][收入]":
        if args[2] in userDefinedDICT["_outcome_key"]:
            result = fun.GetDataByCondition(userID, "cost", fun.GetTimeSpan(args[0]+args[1]))
        elif args[2] in userDefinedDICT["_income_key"]:
            result = fun.GetDataByCondition(userID, "earn", fun.GetTimeSpan(args[0]+args[1]))
        elif args[2] in userDefinedDICT["_allcome_key"]:
            result = fun.GetDataByCondition(userID, "all", fun.GetTimeSpan(args[0]+args[1]))

    if utterance == "查詢[這個][月][總][收入]":
        if args[3] in userDefinedDICT["_outcome_key"]:
            result = fun.GetDataByCondition(userID, "cost", fun.GetTimeSpan(args[0]+args[1]))
        elif args[3] in userDefinedDICT["_income_key"]:
            result = fun.GetDataByCondition(userID, "earn", fun.GetTimeSpan(args[0]+args[1]))
        elif args[3] in userDefinedDICT["_allcome_key"]:
            result = fun.GetDataByCondition(userID, "all", fun.GetTimeSpan(args[0]+args[1]))

    if utterance == "[我][上個月][總共]花了多少[錢]":
        if not fun.CorrectCurrency(args[3],userDefinedDICT["_money"]):
            result = "error_currency"
        result = fun.GetDataByCondition(userID, "cost", fun.GetTimeSpan(args[1]))

    if utterance == "[我][上個月][總共]賺了多少[錢]":
        if not fun.CorrectCurrency(args[3],userDefinedDICT["_money"]):
            result = "error_currency"
        result = fun.GetDataByCondition(userID, "earn", fun.GetTimeSpan(args[1]))

    if utterance == "查詢[我][上週五]的[收入]":
        if args[2] in userDefinedDICT["_outcome_key"]:
            result = fun.GetDataByCondition(userID, "cost", fun.GetTimeSpan(args[1]))
        elif args[2] in userDefinedDICT["_income_key"]:
            result = fun.GetDataByCondition(userID, "earn", fun.GetTimeSpan(args[1]))
        elif args[2] in userDefinedDICT["_allcome_key"]:
            result = fun.GetDataByCondition(userID, "all", fun.GetTimeSpan(args[1]))

    if utterance == "查詢[我][這個][月]的[收入]":
        if args[3] in userDefinedDICT["_outcome_key"]:
            result = fun.GetDataByCondition(userID, "cost", fun.GetTimeSpan(args[1]+args[2]))
        elif args[3] in userDefinedDICT["_income_key"]:
            result = fun.GetDataByCondition(userID, "earn", fun.GetTimeSpan(args[1]+args[2]))
        elif args[3] in userDefinedDICT["_allcome_key"]:
            result = fun.GetDataByCondition(userID, "all", fun.GetTimeSpan(args[1]+args[2]))

    if utterance == "查詢[我]的[收入]":
        if args[1] in userDefinedDICT["_outcome_key"]:
            result = fun.GetDataByCondition(userID, "cost")
        elif args[1] in userDefinedDICT["_income_key"]:
            result = fun.GetDataByCondition(userID, "earn")
        elif args[1] in userDefinedDICT["_allcome_key"]:
            result = fun.GetDataByCondition(userID, "all")
    
    
    """
    處理結果
    """
    # 錯誤
    # 幣值錯誤
    if result == "error_currency":
        resultDICT["intent"] = result
        resultDICT["err_msg"] = "錯誤"
    # 其他錯誤
    elif result == "error":
        resultDICT["intent"] = "error"
        resultDICT["err_msg"] = "錯誤"
    # 結果
    else:
        resultDICT["intent"] = intent
        resultDICT["search_result"] = result

    return resultDICT