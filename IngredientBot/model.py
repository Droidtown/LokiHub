#!/user/bin/env python
# -*- coding: utf-8 -*-

import re
import json
import logging
import pandas as pd
from random import choice
from datetime import datetime

import Loki

inSeasonDICT = json.load(open("./info/inSeason.json", encoding="utf-8")) 
IngredientRelatedDICT = json.load(open("./info/ingredient.json", encoding="utf-8"))

reject_msg = ["討厭", "還有呢", "有甚麼別的食材", "有什麼別的食材", "有甚麼別的", "有什麼別的", "還有什麼？", "還有什麼", "有什麼其他的"]
capability_msg = ["你會什麼", "你會做啥", "你可以做什麼"]
all_ingr_msg = ["所有當季食材"]
inseason_msg = ["當季食材有啥"]
msgLIST = reject_msg + capability_msg + all_ingr_msg + inseason_msg

def checkInSeason(ingredient):
    # 檢查目標是否為當季食材
    currentMonth = datetime.now().month
    ingr_inseasonLIST = inSeasonDICT[str(currentMonth)+"月"]

    if ingredient in ingr_inseasonLIST["蔬菜"]+ingr_inseasonLIST["水果"]+ingr_inseasonLIST["海鮮"]:
        return True
    else:
        return False

def getInSeason(rejectLIST, time, type):
    # 查詢指定時間食材/蔬菜/水果/海鮮
    if time in ["現在", "目前", "今天"]:
        month = str(datetime.now().month)+"月"
    elif time in ["春天", "春季"]:
        month = "春天"
    elif time in ["夏天", "夏季"]:
        month = "夏天"
    elif time in ["秋天", "秋季"]:
        month = "秋天"
    elif time in ["冬天", "冬季"]:
        month = "冬天"
    elif "11月" in time or "十一月" in time:
        month = "11月"
    elif "12月" in time or "十二月" in time:
        month = "12月"
    elif "1月" in time or "一月" in time:
        month = "1月"
    elif "2月" in time or "二月" in time:
        month = "2月"
    elif "3月" in time or "三月" in time:
        month = "3月"
    elif "4月" in time or "四月" in time:
        month = "4月"
    elif "5月" in time or "五月" in time:
        month = "5月"
    elif "6月" in time or "六月" in time:
        month = "6月"
    elif "7月" in time or "七月" in time:
        month = "7月"
    elif "8月" in time or "八月" in time:
        month = "8月"
    elif "9月" in time or "九月" in time:
        month = "9月"
    elif "10月" in time or "十月" in time:
        month = "10月"
    else:
        month = str(datetime.now().month)+"月"

    if "蔬菜" in type:
        type = "蔬菜"
    elif "水果" in type:
        type = "水果"
    elif "海鮮" in type:
        type = "海鮮"
    else:
        type = choice(["蔬菜", "水果", "海鮮"])

    if month in ["春天", "夏天", "秋天", "冬天"]:
        if month == "春天":
            ingr_inseasonLIST = inSeasonDICT["2月"][type] + inSeasonDICT["3月"][type] + inSeasonDICT["4月"][type]
        elif month == "夏天":
            ingr_inseasonLIST = inSeasonDICT["5月"][type] + inSeasonDICT["6月"][type] + inSeasonDICT["7月"][type]
        elif month == "秋天":
            ingr_inseasonLIST = inSeasonDICT["8月"][type] + inSeasonDICT["9月"][type] + inSeasonDICT["10月"][type]
        elif month == "冬天":
            ingr_inseasonLIST = inSeasonDICT["11月"][type] + inSeasonDICT["12月"][type] + inSeasonDICT["1月"][type]
    else:
        ingr_inseasonLIST = inSeasonDICT[month][type]
    ingr_inseason_excludeLIST = [x for x in ingr_inseasonLIST if x not in rejectLIST]

    return choice(ingr_inseason_excludeLIST), month, type

def getPrice(ingredient):
    # 查詢食材的市場價格
    table = pd.read_html("http://www.tapmc.com.taipei/")
        
    if(len(table[0].columns)) != 5: return {}

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

def getRecipe(ingredient):
    # 查詢食材的作法
    if ingredient in IngredientRelatedDICT:
        return IngredientRelatedDICT[ingredient]["作法"]
    else:
        return {}
    
def getTaboo(ingredient):
    # 查詢食材的作法
    if ingredient in IngredientRelatedDICT:
        return IngredientRelatedDICT[ingredient]["禁忌"]
    else:
        return {}
    
def getSelection(ingredient):
    # 查詢食材的挑選方法
    if ingredient in IngredientRelatedDICT:
        return IngredientRelatedDICT[ingredient]["挑法"]
    else:
        return {}

def getRecommend():
    # 查詢一道料理
    random_ingr = choice(list(IngredientRelatedDICT.keys()))
    recommend = choice(IngredientRelatedDICT[random_ingr]["作法"])

    return recommend, random_ingr

def getSeason(ingredient):
    # 查詢食材的產季
    season = []
    for month in inSeasonDICT.keys():
        for type in inSeasonDICT[month].keys():
            if ingredient in inSeasonDICT[month][type]:
                season.append(month)
    season = sorted(list(set(season)))

    return season

def getAllIngr(time, type):
    # 查詢指定時間的所有食材/蔬菜/水果/海鮮
    if time in ["現在", "目前", "今天"]:
        month = str(datetime.now().month)+"月"
    elif time in ["春天", "春季"]:
        month = "春天"
    elif time in ["夏天", "夏季"]:
        month = "夏天"
    elif time in ["秋天", "秋季"]:
        month = "秋天"
    elif time in ["冬天", "冬季"]:
        month = "冬天"
    elif "11月" in time or "十一月" in time:
        month = "11月"
    elif "12月" in time or "十二月" in time:
        month = "12月"
    elif "1月" in time or "一月" in time:
        month = "1月"
    elif "2月" in time or "二月" in time:
        month = "2月"
    elif "3月" in time or "三月" in time:
        month = "3月"
    elif "4月" in time or "四月" in time:
        month = "4月"
    elif "5月" in time or "五月" in time:
        month = "5月"
    elif "6月" in time or "六月" in time:
        month = "6月"
    elif "7月" in time or "七月" in time:
        month = "7月"
    elif "8月" in time or "八月" in time:
        month = "8月"
    elif "9月" in time or "九月" in time:
        month = "9月"
    elif "10月" in time or "十月" in time:
        month = "10月"
    else:
        month = str(datetime.now().month)+"月"

    if "蔬菜" in type:
        type = "蔬菜"
    elif "水果" in type:
        type = "水果"
    elif "海鮮" in type:
        type = "海鮮"
    else:
        type = "食材"


    if month in ["春天", "夏天", "秋天", "冬天"]:
        if month == "春天":
            if type == "食材":
                all_ingr_inseasonLIST = inSeasonDICT["2月"]["蔬菜"] + inSeasonDICT["2月"]["水果"] + inSeasonDICT["2月"]["海鮮"] + inSeasonDICT["3月"]["蔬菜"] + inSeasonDICT["3月"]["水果"] + inSeasonDICT["3月"]["海鮮"] + inSeasonDICT["4月"]["蔬菜"] + inSeasonDICT["4月"]["水果"] + inSeasonDICT["4月"]["海鮮"]
            else:
                all_ingr_inseasonLIST = inSeasonDICT["2月"][type] + inSeasonDICT["3月"][type] + inSeasonDICT["4月"][type]
        elif month == "夏天":
            if type == "食材":
                all_ingr_inseasonLIST = inSeasonDICT["5月"]["蔬菜"] + inSeasonDICT["5月"]["水果"] + inSeasonDICT["5月"]["海鮮"] + inSeasonDICT["6月"]["蔬菜"] + inSeasonDICT["6月"]["水果"] + inSeasonDICT["6月"]["海鮮"] + inSeasonDICT["7月"]["蔬菜"] + inSeasonDICT["7月"]["水果"] + inSeasonDICT["7月"]["海鮮"]
            else:
                all_ingr_inseasonLIST = inSeasonDICT["5月"][type] + inSeasonDICT["6月"][type] + inSeasonDICT["7月"][type]
        elif month == "秋天":
            if type == "食材":
                all_ingr_inseasonLIST = inSeasonDICT["8月"]["蔬菜"] + inSeasonDICT["8月"]["水果"] + inSeasonDICT["8月"]["海鮮"] + inSeasonDICT["9月"]["蔬菜"] + inSeasonDICT["9月"]["水果"] + inSeasonDICT["9月"]["海鮮"] + inSeasonDICT["10月"]["蔬菜"] + inSeasonDICT["10月"]["水果"] + inSeasonDICT["10月"]["海鮮"]
            else:
                all_ingr_inseasonLIST = inSeasonDICT["8月"][type] + inSeasonDICT["9月"][type] + inSeasonDICT["10月"][type]
        elif month == "冬天":
            if type == "食材":
                all_ingr_inseasonLIST = inSeasonDICT["11月"]["蔬菜"] + inSeasonDICT["11月"]["水果"] + inSeasonDICT["11月"]["海鮮"] + inSeasonDICT["12月"]["蔬菜"] + inSeasonDICT["12月"]["水果"] + inSeasonDICT["12月"]["海鮮"] + inSeasonDICT["1月"]["蔬菜"] + inSeasonDICT["1月"]["水果"] + inSeasonDICT["1月"]["海鮮"]
            else:
                all_ingr_inseasonLIST = inSeasonDICT["11月"][type] + inSeasonDICT["12月"][type] + inSeasonDICT["1月"][type]
    else:
        if type == "食材":
            all_ingr_inseasonLIST = inSeasonDICT[month]["蔬菜"] + inSeasonDICT[month]["水果"] + inSeasonDICT[month]["海鮮"]
        else:
            all_ingr_inseasonLIST = inSeasonDICT[month][type]

    return all_ingr_inseasonLIST, month, type


def getIngredient(resultDICT, mscDICT):
    # 取得食材
    if "ingredient" in resultDICT.keys():
        ingredient = resultDICT["ingredient"]
    else:
        ingredient = mscDICT["ingredient"]   #如果回覆中未提到甚麼食材，以上一次提供的當季食材當作本次的食材

    return ingredient


def getLokiResult(inputSTR):
    # 取得 Loki 回傳的結果
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = Loki.runLoki(inputLIST, filterLIST)

    return resultDICT

def model(mscDICT):
    """
    接收針對 User 紀錄的多輪對話資訊 (mscDICT)，
    根據訊息內容的意圖 (intent) 做相對應的處理，將處理結果記錄在 mscDICT 回傳。

    多輪對話資訊 (mscDICT) 所記錄的參數：
        Argument        Type         Description
        ---------------------------------------------------------
        updatetime      (datetime)   第一次傳送訊息的時間
        msgSTR          (str)        本次訊息內容
        intent          (str list)   本次訊息內容的意圖
        ingredient      (str)        本次訊息內容提及的的食材
        time            (str)        本次訊息內容提及的時間資訊
        type            (str)        本次訊息內容提及的食材種類
        rejectLIST      (str list)   整個對話過程提及過討厭的食材
        replySTR        (str)        本次回覆的內容
        reject_inse     (bool)       本次拒絕的是否為"食材"
        reject_reco     (bool)       本次拒絕的是否為"推薦料理"
    """

    # 將訊息內容傳送給 Loki 處理，得到結果
    resultDICT = getLokiResult(mscDICT["msgSTR"])
    logging.info("Loki 回傳的結果: {}".format(resultDICT))
    
    #有找到對應的intent
    if len(resultDICT) > 0 or mscDICT["msgSTR"] in msgLIST: 
        #intent = check，想確認這項食材是不是當季的
        if "check" in resultDICT.keys():
            ingr = getIngredient(resultDICT, mscDICT)
            
            if checkInSeason(ingr):
                mscDICT["replySTR"] = resultDICT["ingredient"] + "是當季食材沒錯！"
            else:
                mscDICT["replySTR"] = resultDICT["ingredient"] + "不是當季食材哦~"

            #紀錄
            mscDICT["ingredient"] = ingr

        #intent = inseason，想知道現在有哪些當季食材
        if "inseason" in resultDICT.keys() or mscDICT["msgSTR"] in inseason_msg:
            if "time" in resultDICT.keys():
                time = resultDICT["time"]
            else:
                time = ""
            if "type" in resultDICT.keys():
                type = resultDICT["type"]
            else:
                type = ""
            
            ingr_inseason, res_time, res_type = getInSeason(mscDICT["rejectLIST"], time, type)

            if type == "" or  type == "食材":
                if time == "":
                    mscDICT["replySTR"] = "現在的{}很好吃哦！".format(ingr_inseason)
                else:
                    mscDICT["replySTR"] = "{}的{}很好吃哦！".format(res_time, ingr_inseason)
            else:
                if time == "":
                    mscDICT["replySTR"] = "你喜歡吃{}呀？現在的{}很好吃哦！".format(res_type, ingr_inseason)
                else:
                    mscDICT["replySTR"] = "你喜歡吃{}呀？{}的{}很好吃哦！".format(res_type, res_time, ingr_inseason)

            #紀錄
            mscDICT["ingredient"] = ingr_inseason
            mscDICT["time"] = res_time
            mscDICT["type"] = res_type

        #intent = reject，拒絕上輪提供的食材/料理，再另外提供一道食材/料理
        if "reject" in resultDICT.keys() or mscDICT["msgSTR"] in reject_msg:
            
            #上輪拒絕的是"料理"
            if ('recommend' in mscDICT["intent"] or mscDICT["reject_reco"] == True) and 'inseason' not in mscDICT["intent"]:
                recommend_result, ingr = getRecommend()

                replySTR0 = "那麼{}你覺得如何？".format(recommend_result)
                replySTR1 = "再給你另外一道，{}料理：{}".format(ingr, recommend_result)
                replyLIST = [replySTR0, replySTR1]

                mscDICT["replySTR"] = choice(replyLIST)

                mscDICT["reject_reco"] = True
                mscDICT["reject_inse"] = False
            
             #上輪拒絕的是"食材"
            else:
                reject_ingr = getIngredient(resultDICT, mscDICT)
                mscDICT["rejectLIST"].append(reject_ingr)  #紀錄使用者reject過的食材

                #再提供另一個當季食材
                if mscDICT["time"] == "":
                    time = "現在"
                else:
                    time = mscDICT["time"]
                
                if mscDICT["type"] == "":
                    type = choice(["蔬菜", "水果", "海鮮"])
                else:
                    type = mscDICT["type"]

                ingr_inseason, res_time, res_type = getInSeason(mscDICT["rejectLIST"], time, type)

                replySTR0 = "恩恩，那麼{}如何？".format(ingr_inseason)
                replySTR1 = "了解，其他像{}也不錯哦，".format(ingr_inseason)
                replySTR00 = "它能用來做成很多不一樣的料理哦。"
                replySTR01 = "不知道最近{}多少錢？".format(ingr_inseason)
                replySTR10 = "它的挑選方法很有趣哦。"
                replySTR11 = "但要注意它有一些搭配禁忌。"
                replyLIST0 = [replySTR0, replySTR1]
                replyLIST1 = [replySTR00, replySTR01, replySTR10, replySTR11]

                mscDICT["replySTR"] = choice(replyLIST0) + choice(replyLIST1)

                #紀錄
                mscDICT["ingredient"] = ingr_inseason
                mscDICT["time"] = res_time
                mscDICT["type"] = res_type
                mscDICT["reject_inse"] = True
                mscDICT["reject_reco"] = False

        #intent = price，想知道這項食材的價格
        if "price" in resultDICT.keys():
            ingr = getIngredient(resultDICT, mscDICT)
            
            close_time0 = datetime.strptime(str(datetime.now().date())+'0:00', '%Y-%m-%d%H:%M')
            close_time1 =  datetime.strptime(str(datetime.now().date())+'7:30', '%Y-%m-%d%H:%M')
            n_time = datetime.now()
            n_weekday = datetime.today().weekday()

            if n_weekday == 0:
                mscDICT["replySTR"] = "星期一休市"
            
            elif close_time0 < n_time and n_time < close_time1:
                mscDICT["replySTR"] = "食材尚在運送拍賣中"

            else:
                ingr_priceDICT = getPrice(ingr)
                if len(ingr_priceDICT) > 0:
                    replySTR = ""
                    for key in ingr_priceDICT:
                        replySTR = replySTR + key + "的今日價格：{}元(上價)，{}元(中價)，{}元(下價)".format(ingr_priceDICT[key][0], ingr_priceDICT[key][1], ingr_priceDICT[key][2]) + "\n"

                    mscDICT["replySTR"] = replySTR
                else:
                    mscDICT["replySTR"] = "查不到{}的價錢！".format(ingr)

            #紀錄
            mscDICT["ingredient"] = ingr

        #intent = recipe，想知道這項食材有什麼作法
        if "recipe" in resultDICT.keys():
            ingr = getIngredient(resultDICT, mscDICT)
            recipe_result = getRecipe(ingr)
            if len(recipe_result) > 0:
                recipeGroup = "、".join(recipe_result)
                
                replySTR0 = "{}，這些都是{}的料理，你可以做看看。".format(recipeGroup, ingr)
                replySTR1 = "{}可以這樣料理：{}".format(ingr, recipeGroup)
                replySTR2 = "{}，你想做哪一道{}料理？".format(recipeGroup, ingr)
                replyLIST = [replySTR0, replySTR1, replySTR2]

                mscDICT["replySTR"] = choice(replyLIST)
            else:
                mscDICT["replySTR"] = "查不到{}的作法！".format(ingr)

            #紀錄
            mscDICT["ingredient"] = ingr

        #intent = taboo，想知道這項食材有什麼禁忌
        if "taboo" in resultDICT.keys():
            ingr = getIngredient(resultDICT, mscDICT)
            taboo_result = getTaboo(ingr)
            if len(taboo_result) > 0:
                mscDICT["replySTR"] = taboo_result
            else:
                mscDICT["replySTR"] = "這邊沒有記載{}的禁忌！".format(ingr)
              
            #紀錄
            mscDICT["ingredient"] = ingr

        #intent = selection，想知道這項食材有什麼挑選方法
        if "selection" in resultDICT.keys():
            ingr = getIngredient(resultDICT, mscDICT)
            selection_result = getSelection(ingr)
            if len(selection_result) > 0:
                mscDICT["replySTR"] = selection_result
            else:
                mscDICT["replySTR"] = "查不到{}的挑選方法！".format(ingr)

            #紀錄
            mscDICT["ingredient"] = ingr

        #intent = recommend，想被推薦一道料理
        if "recommend" in resultDICT.keys():
            recommend_result, ingr = getRecommend()

            replySTR0 = "可以試試看{}".format(recommend_result)
            replySTR1 = "給你這個，{}料理：{}".format(ingr, recommend_result)
            replyLIST = [replySTR0, replySTR1]

            mscDICT["replySTR"] = choice(replyLIST)

        #intent = capability，想知道能詢問bot什麼問題
        if "capability" in resultDICT.keys() or mscDICT["msgSTR"] in capability_msg:
            mscDICT["replySTR"] = "我知道現在的當季食材有什麼，還有一些關於食材的資訊，像是價格、挑選方法或是禁忌，還有它可以做成什麼料理..."

        #intent = which_season，想了解某個食材的產季
        if "which_season" in resultDICT.keys():
            ingr = getIngredient(resultDICT, mscDICT)
            ws_result = getSeason(ingr)
            if len(ws_result) > 0:
                group = "、".join(ws_result)

                replySTR0 = "{}是{}的產季，你喜歡吃{}嗎？".format(group, ingr, ingr)
                replySTR1 = "{}的產季是{}，{}能做成好多不同的料理。".format(ingr, group, ingr)
                replyLIST = [replySTR0, replySTR1]

                mscDICT["replySTR"] = choice(replyLIST)
            else:
                mscDICT["replySTR"] = "查不到{}的產季！".format(ingr)

            #紀錄
            mscDICT["ingredient"] = ingr

        #intent = all_ingr，想知道所有的當季食材
        if "all_ingr" in resultDICT.keys() or mscDICT["msgSTR"] in all_ingr_msg:
            if "time" in resultDICT.keys():
                time = resultDICT["time"]
            else:
                time = ""
            if "type" in resultDICT.keys():
                type = resultDICT["type"]
            else:
                type = ""

            all_ingrLIST, res_time, res_type = getAllIngr(time, type)

            all_ingrGroup = "、".join(all_ingrLIST)
            if type == "":
                if time == "":
                    mscDICT["replySTR"] = "這些全是現在的當季食材：{}".format(all_ingrGroup)
                else:
                    mscDICT["replySTR"] = "這些全是{}的當季食材：{}".format(res_time, all_ingrGroup)
            else:
                if time == "":
                    mscDICT["replySTR"] = "這些全是現在的當季{}：{}".format(res_type, all_ingrGroup)
                else:
                    mscDICT["replySTR"] = "這些全是{}的當季{}：{}".format(res_time, res_type, all_ingrGroup)

        #紀錄本次的intent
        mscDICT["intent"] = []
        for key in resultDICT.keys():
            if key not in ['ingredient', 'time' 'type']:
                mscDICT["intent"].append(key)

    else: #沒有找到對應的intent

        #intent = 向bot打招呼
        if mscDICT["msgSTR"].lower() in ["哈囉","嗨","你好","您好","hi","hello", "早安", "午安", "晚安", "早", "hihi", "hey", "安安"]:
            
            currentMonth = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
            type = choice(["蔬菜", "水果", "海鮮"])            
            ingr_inseason = choice(inSeasonDICT[str(currentMonth)+"月"][type])

            mscDICT["replySTR"] = "嗨，我是小幫手，你喜歡" + ingr_inseason + "嗎？"

            #紀錄
            mscDICT["ingredient"] = ingr_inseason
            mscDICT["time"] = "現在"
            mscDICT["type"] = type

        #intent = accept，表示接受
        elif mscDICT["msgSTR"].lower() in ["ok", "了解","好哦","好喔","沒問題","可以", "喜歡", "喜歡ㄟ", "好ㄟ"]:
            if "reject" in mscDICT["intent"]:
                mscDICT["replySTR"] = "你可以問我更多關於{}的資訊哦 ^_^".format(mscDICT["ingredient"])
            else:
                if mscDICT["ingredient"] == "":
                    mscDICT["replySTR"] = "歡迎問我關於食材的問題哦 ^_^"
                else:
                    mscDICT["replySTR"] = "你可以問我更多關於{}的資訊哦 ^_^".format(mscDICT["ingredient"])
        
        #default
        else: 
            mscDICT["replySTR"] = choice(["好喔", "好的Ok", "繼續問我更多食材問題吧"])
    
        #紀錄本次的intent
        mscDICT["intent"] = []

    return mscDICT

