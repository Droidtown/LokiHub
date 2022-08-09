#!/user/bin/env python
# -*- coding: utf-8 -*-

import json
import pandas as pd
from datetime import datetime
import re
import logging
from random import choice

import ingredientBot as iB

inSeasonDICT = json.load(open("./info/inSeason.json", encoding="utf-8")) 
IngredientRelatedDICT = json.load(open("./info/ingredient.json", encoding="utf-8"))


def checkInSeason(ingredient):
    currentMonth = datetime.now().month
    ingr_inseasonLIST = inSeasonDICT[str(currentMonth)+"月"]

    if ingredient in ingr_inseasonLIST:
        return True
    else:
        return False

def inSeason(rejectLIST):
    currentMonth = datetime.now().month
    ingr_inseasonLIST = inSeasonDICT[str(currentMonth)+"月"]
    ingr_inseason_excludeLIST = [x for x in ingr_inseasonLIST if x not in rejectLIST]
    #print(ingr_inseason_excludeLIST)

    return choice(ingr_inseason_excludeLIST)

def price(ingredient):
    table = pd.read_html("http://www.tapmc.com.taipei/")
    table[0].columns = ['品名', '品種', '上價', '中價', '下價']

    priceDICT={}
    for index,row in table[0].iterrows():
        tmp=[]
        tmp.append(row["上價"])
        tmp.append(row["中價"])
        tmp.append(row["下價"])
        name = str(row["品名"]) + "(" + str(row["品種"]) + ")"
        priceDICT[name]=tmp

    ingr_priceDICT={}
    for key in priceDICT.keys():
        if ingredient in key:
            ingr_priceDICT[key]=priceDICT[key]

    return ingr_priceDICT

def recipe(ingredient):
    if ingredient in IngredientRelatedDICT:
        return IngredientRelatedDICT[ingredient]["作法"]
    else:
        return {}
    
def taboo(ingredient):
    if ingredient in IngredientRelatedDICT:
        return IngredientRelatedDICT[ingredient]["禁忌"]
    else:
        return {}

def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = iB.runLoki(inputLIST, filterLIST)

    return resultDICT

def model(mscDICT):
    resulDICT = getLokiResult(mscDICT["msgSTR"])
    logging.info("Loki 回傳的結果: {}".format(resulDICT))
    
    if len(resulDICT) > 0: #有找到對應的intent

        #intent = check，想確認這項食材是不是當季
        if "check" in resulDICT.keys():
            if checkInSeason(resulDICT["ingredient"]):
                mscDICT["replySTR"] = resulDICT["ingredient"] + "是當季食材沒錯！"
            else:
                mscDICT["replySTR"] = resulDICT["ingredient"] + "不是當季食材哦~"

        #intent = price，想知道這項食材的價格
        if "price" in resulDICT.keys():
            if datetime.today().weekday() == 0: #星期一休市
                mscDICT["replySTR"] = "今日休市"
            else:
                ingr_priceDICT = price(resulDICT["ingredient"])
                if len(ingr_priceDICT) > 0:
                    replySTR = ""
                    for key in ingr_priceDICT:
                        replySTR = replySTR + key + "的今日價格：{}元(上價)，{}元(中價)，{}元(下價)".format(ingr_priceDICT[key][0], ingr_priceDICT[key][1], ingr_priceDICT[key][2]) + "\n"

                    mscDICT["replySTR"] = replySTR
                else:
                    mscDICT["replySTR"] = "查不到這個品項的價錢 QAQ"
        
        #intent = inseason，想知道現在有哪些當季食材
        if "inseason" in resulDICT.keys():
            ingr_inseason = inSeason(mscDICT["rejectLIST"])
            mscDICT["ingr_inseason"] = ingr_inseason
            mscDICT["replySTR"] = ingr_inseason + "是現在的當季食材哦！"

        #intent = reject
        if "reject" in resulDICT.keys():
            if "reject_ingr" in resulDICT.keys():
                reject_ingr = resulDICT["reject_ingr"]
            else:
                reject_ingr = mscDICT["ingr_inseason"]
            mscDICT["rejectLIST"].append(reject_ingr)
            ingr_inseason = inSeason(mscDICT["rejectLIST"])

            mscDICT["replySTR"] = "那麼" + ingr_inseason + "如何？"

        #intent = recipe，想知道這項食材有什麼作法
        if "recipe" in resulDICT.keys():
            recipeResult = recipe(resulDICT["ingredient"])
            if len(recipeResult) > 0:
                mscDICT["replySTR"] = recipeResult
            else:
                mscDICT["replySTR"] = "查不到這種食材的作法 QAQ"

        #intent = taboo
        if "taboo" in resulDICT.keys():
            result_taboo = taboo(resulDICT["ingredient"])
            if len(result_taboo)> 0:
                mscDICT["replySTR"] = result_taboo
            else:
                mscDICT["replySTR"] = "這邊沒有記載這項食材的禁忌 QAQ"

            mscDICT["replySTR"] = ingr_inseason
            
    else: #沒有對應的句型
        if mscDICT["msgSTR"].lower() in ["哈囉","嗨","你好","您好","hi","hello", "早安", "午安", "晚安", "早"]:
            mscDICT["replySTR"] = "嗨嗨 o(^▽^)o"
        else:
            mscDICT["replySTR"] = "你說啥呢"
    
    return mscDICT

