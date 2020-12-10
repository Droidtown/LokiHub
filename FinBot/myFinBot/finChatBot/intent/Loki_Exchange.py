#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Exchange
    
    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict
    
    Output:
        resultDICT    dict
"""

DEBUG_Exchange = True
userDefinedDICT = {"歐元":"EUR",
                 "美金":"USD",
                 "日圓":"JPY",
                 "台幣":"TWD",
                 "臺幣":"TWD",
                 "英鎊":"GBP",
                 "法郎":"CHF",
                 "澳幣":"AUD",
                 "港幣":"HKD",
                 "泰銖":"THB"}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Exchange:
        print("[Exchange] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    if utterance == "[100元][美金]可以兌換[台幣]多少":
        resultDICT["source"] = args[1]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[0]
        pass

    if utterance == "[100元][美金]可以兌換多少[台幣]":
        resultDICT["source"] = args[1]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[0]
        pass

    if utterance == "[100元][美金]要[台幣]多少":
        resultDICT["source"] = args[1]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[0]
        pass

    if utterance == "[100元][美金]要多少[台幣]":
        resultDICT["source"] = args[1]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[0]
        pass

    if utterance == "[100台幣]換[美金]":
        resultDICT["source"] = [x for x in userDefinedDICT if x in args[0]][0]
        resultDICT["target"] = args[1]
        resultDICT["amount"] = args[0]
        pass

    if utterance == "[100美金]能換多少[台幣]":
        resultDICT["source"] = [x for x in userDefinedDICT if x in args[0]][0]
        resultDICT["target"] = args[1]
        resultDICT["amount"] = args[0]
        pass

    if utterance == "[100美金]要[台幣]多少":
        resultDICT["source"] = [x for x in userDefinedDICT if x in args[0]][0]
        resultDICT["target"] = args[1]
        resultDICT["amount"] = args[0]
        pass

    if utterance == "[100美金]要多少[台幣]":
        resultDICT["source"] = [x for x in userDefinedDICT if x in args[0]][0]
        resultDICT["target"] = args[1]
        resultDICT["amount"] = args[0]
        pass

    if utterance == "[今天][美金]兌換[台幣]是多少":
        resultDICT["source"] = args[1]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = None
        pass

    if utterance == "[美金][100]要[台幣]多少":
        resultDICT["source"] = args[0]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[1]
        pass

    if utterance == "[美金][100]要多少[台幣]":
        resultDICT["source"] = args[0]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[1]
        pass

    if utterance == "[美金][100元]可以兌換[台幣]多少":
        resultDICT["source"] = args[0]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[1]
        pass

    if utterance == "[美金][100元]可以兌換多少[台幣]":
        resultDICT["source"] = args[0]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[1]
        pass

    if utterance == "[美金][100元]要[台幣]多少":
        resultDICT["source"] = args[0]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[1]
        pass

    if utterance == "[美金][100元]要多少[台幣]":
        print("IN")
        resultDICT["source"] = args[0]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[1]
        pass

    if utterance == "我想要[100元][美金]":
        resultDICT["source"] = args[1]
        resultDICT["target"] = None
        resultDICT["amount"] = args[0]
        pass

    if utterance == "我想要[美金][100元]":
        resultDICT["source"] = args[0]
        resultDICT["target"] = None
        resultDICT["amount"] = args[1]
        pass

    if utterance == "我想買[100元][美金]":
        resultDICT["source"] = args[1]
        resultDICT["target"] = None
        resultDICT["amount"] = args[0]
        pass

    if utterance == "我想買[美金][100元]":
        resultDICT["source"] = args[0]
        resultDICT["target"] = None
        resultDICT["amount"] = args[1]
        pass

    if utterance == "[美金][100元]是多少[法郎]":
        resultDICT["source"] = args[0]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[1]
        pass

    return resultDICT