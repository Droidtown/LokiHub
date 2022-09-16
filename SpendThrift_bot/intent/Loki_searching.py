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
    userDefinedDICT = {"_key":["收入","支出","記帳狀況"],"_park":["六福村","九族文化村","義大","義大世界"],"_money":["支出總額","支出費用","總金額","總額","費用","金錢","錢"]}



intent = "searching"

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_searching:
        print("[searching] {} ===> {}".format(inputSTR, utterance))

def getResult(userID, inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "查詢[收入]":
        if args[0] in ["支出"]:
            result = fun.GetDataByCondition(userID, "cost")
        elif args[0] in ["收入"]:
            result = fun.GetDataByCondition(userID, "earn")
        elif args[0] in ["記帳狀況"]:
            result = fun.GetDataByCondition(userID, "all")
        
        # 錯誤
        if result == "error":
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = "錯誤"
        #
        else:
            resultDICT["intent"] = intent
            resultDICT["search_result"] = result
        pass
    


    return resultDICT