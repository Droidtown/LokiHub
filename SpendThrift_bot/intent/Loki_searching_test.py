#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for searching_test

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
import sys
import csv

# set path
path_current = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(path_current))
os.chdir(path_current)

# from SpendThrift_bot import GetDataByCondition

DEBUG_searching_test = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_key":["收入","支出","記帳狀況"],"_park":["六福村","九族文化村","義大","義大世界"],"money":["支出總額","支出費用","總金額","總額","費用","金錢","錢"]}

# 從 [username].csv 中讀取資料
def GetDataByCondition(username="testUser", condition="all"):
    # open csv
    with open("./user_data/" + username + ".csv", 'r', encoding="utf-8") as f:
        # read data
        reader = csv.reader(f)

        # get data by condition
        totalMoney = 0

        # 管他的
        if condition == "all":
            for row in reader:
                # 忽略欄位說明
                if row[0] == "amount":
                    pass
                # 計算
                else:
                    totalMoney += int(row[0])

        # 收入
        elif condition == "earn":
            for row in reader:
                # 忽略欄位說明
                if row[0] == "amount":
                    pass
                # 計算
                else:
                    if int(row[0]) > 0:
                        totalMoney += int(row[0])
        # 收入
        elif condition == "cost":
            for row in reader:
                # 忽略欄位說明
                if row[0] == "amount":
                    pass
                # 計算
                else:
                    if int(row[0]) < 0:
                        totalMoney += int(row[0])
            totalMoney=0-totalMoney #暫時的

        else:
            print("你這個敗家子，連存資料都給我存錯:(")
        return totalMoney


# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_searching_test:
        print("[searching_test] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "查詢[收入]":
        # write your code here
        if args[0]=='收入':
            resultDICT['amount']=GetDataByCondition('testUser','earn')
            print('收入')
        elif args[0] == '支出':
            resultDICT['amount']=GetDataByCondition('testUser','cost')
            print('支出')
        elif args[0] == '記帳狀況':
            resultDICT['amount']=GetDataByCondition('testUser','all')
            print('記帳狀況')
        else:
            print('哈囉敗家子')

        pass

    return resultDICT