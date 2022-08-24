#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for spend_adv

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

from function import getAdvArgs

DEBUG_spend_adv = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_key":["收入","支出","記帳狀況"],"_park":["六福村","九族文化村","義大","義大世界"],"money":["支出總額","支出費用","總金額","總額","費用","金錢","錢"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_spend_adv:
        print("[spend_adv] {} ===> {}".format(inputSTR, utterance))


# 這個意圖的名字
intent = "spend_adv"

def getResult(inputSTR, utterance, args, resultDICT):
    # debugInfo(inputSTR, utterance)
    
    if utterance == "去全聯支出3000":
        pass

    if utterance == "去全聯花了3000":
        # write your code here
        pass

    if utterance == "去六福村支出3000":
        # write your code here
        pass

    if utterance == "去六福村花了3000":
        # write your code here
        pass

    if utterance == "去台北支出3000":
        # write your code here
        pass

    if utterance == "去台北花了3000":
        # write your code here
        pass

    if utterance == "支出3000":
        pass

    if utterance == "昨天去全聯支出3000":
        # write your code here
        pass

    if utterance == "昨天去全聯花了3000":
        # write your code here
        pass

    if utterance == "昨天去六福村支出3000":
        """
            3: 時間
            9: 地點
            12: 補充說明
            16: 金額
        """
        status, result = getAdvArgs(intent, utterance, inputSTR, [3,9,12,16])
        
        if status == True:
            resultDICT["intent"] = intent
            resultDICT["time"] = result[0]        # 時間
            resultDICT["description"] = result[1] # 地點(先當說明用)
            resultDICT["amount"] = result[3]      # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass

    if utterance == "昨天去六福村花了3000":
        # write your code here
        pass

    if utterance == "昨天去台北支出3000":
        # write your code here
        pass

    if utterance == "昨天去台北花了3000":
        # write your code here
        pass

    if utterance == "昨天支出3000": 
        pass

    if utterance == "昨天花了3000":
        pass

    if utterance == "花了3000":
        # write your code here
        pass

    return resultDICT