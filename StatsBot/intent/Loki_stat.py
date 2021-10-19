#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for stat

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_stat = True
userDefinedDICT = {"年": ["球季", "賽季"], "助攻": ["assist"], "單場": ["一場", "一場球", "單場球", "單場次"], "平均": ["場均"], "得分": ["score"], "抄截": ["抄球", "搶斷", "steal"], "最多": ["最高"], "搶籃板": ["籃板", "rebound", "籃板球"], "紐約人": ["紐約人隊", "紐約尼克隊", "紐約尼克", "紐約"], "丹佛金塊": ["丹佛金塊隊", "金塊", "金塊隊", "丹佛"], "猶他爵士": ["猶他爵士隊", "爵士", "爵士隊", "猶他"], "金州勇士": ["金州勇士隊", "勇士", "勇士隊"], "侯斯頓火箭": ["侯斯頓火箭隊", "火箭", "火箭隊", "休士頓火箭隊", "休士頓火箭", "休士頓"], "夏洛特山貓": ["夏洛特山貓隊", "山貓", "山貓隊", "夏洛特黃蜂隊", "夏洛特"], "多倫多速龍": ["多倫多速龍隊", "速龍", "速龍隊", "多倫多暴龍隊", "暴龍隊", "多倫多"], "奧蘭多魔術": ["奧蘭多魔術隊", "魔術", "魔術隊", "奧蘭多"], "孟菲斯灰熊": ["孟菲斯灰熊隊", "灰熊", "灰熊隊", "曼斐斯灰熊隊", "孟菲斯"], "底特律活塞": ["底特律活塞隊", "活塞", "活塞隊", "底特律"], "新澤西籃網": ["新澤西籃網隊", "籃網", "籃網隊", "布魯克林籃網隊", "紐澤西籃網隊", "新澤西", "布魯克林"], "洛杉磯快艇": ["洛杉磯快艇隊", "快艇", "快艇隊"], "洛杉磯湖人": ["洛杉磯湖人隊", "湖人", "湖人隊"], "芝加哥公牛": ["芝加哥公牛隊", "公牛", "公牛隊", "芝加哥"], "華盛頓巫師": ["華盛頓巫師隊", "巫師", "巫師隊", "華盛頓"], "達拉斯小牛": ["達拉斯小牛隊", "小牛", "小牛隊", "達拉斯獨行俠隊", "獨行俠隊", "達拉斯"], "邁亞密熱火": ["邁亞密熱火隊", "熱火", "熱火隊", "邁亞密"], "阿特蘭大鷹": ["阿特蘭大鷹隊", "鷹隊", "亞特蘭大老鷹", "亞特蘭大老鷹隊", "老鷹隊", "亞特蘭大"], "鳳凰城太陽": ["鳳凰城太陽隊", "太陽", "太陽隊", "鳳凰城"], "克里夫蘭騎士": ["克里夫蘭騎士隊", "騎士", "騎士隊", "克里夫蘭"], "印第安納溜馬": ["印第安納溜馬隊", "溜馬", "溜馬隊", "印第安那溜馬隊", "印第安納"], "密爾沃基公鹿": ["密爾沃基公鹿隊", "公鹿", "公鹿隊", "密爾瓦基公鹿隊", "密爾瓦基"], "新奧爾良黃蜂": ["新奧爾良黃蜂隊", "黃蜂", "黃蜂隊", "紐奧良黃蜂隊", "紐奧良鵜鶘隊", "鵜鶘", "鵜鶘隊", "紐奧良"], "明尼蘇達木狼": ["明尼蘇達木狼隊", "木狼", "木狼隊", "明尼蘇達灰狼隊", "灰狼隊", "明尼蘇達"], "波特蘭拓荒者": ["波特蘭拓荒者隊", "拓荒者", "拓荒者隊", "波特蘭"], "西雅圖超音速": ["西雅圖超音速隊", "超音速", "超音速隊"], "費城七十六人": ["費城七十六人隊", "七十六人", "七六人", "七十六人隊", "七六人隊", "費城76人隊", "76人隊", "費城"], "奧克拉荷馬雷霆": ["奧克拉荷馬雷霆隊", "雷霆", "雷霆隊", "奧克拉荷馬"], "波士頓塞爾特人": ["波士頓塞爾特人隊", "塞爾特人", "塞爾特人隊", "波士頓塞爾蒂克隊", "塞爾蒂克隊", "波士頓"], "聖安東尼奧馬刺": ["聖安東尼奧馬刺隊", "馬刺", "馬刺隊", "聖安東尼奧"], "薩克拉門托帝王": ["薩克拉門托帝王隊", "帝王", "帝王隊", "沙加緬度國王隊", "國王", "國王隊", "沙加緬度"]}

statDICT = {'pts':['得分', '得幾分', '得多少分'], 
            'reb':['籃板', '搶籃板', '搶幾個籃板', '搶多少籃板'], 
            'ast':['助攻', '助攻幾次'], 
            'blk':['阻攻', '火鍋', '火鍋幾個', '蓋火鍋', '搧帽', '蓋帽'], 
            'stl':['抄截']}


def get_stat(resultDICT, elem):
    """Get target stats"""
    for key in statDICT.keys():
        if elem in statDICT[key]:
            resultDICT['stat'].append(key)
    return resultDICT

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_stat:
        print("[stat] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT['stat'] = []
    if utterance == "一場[得分]平均":
        resultDICT['level'] = 'avg'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "一場最多[得分]":
        resultDICT['level'] = 'single'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "一場最高[得分]":
        resultDICT['level'] = 'single'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "一場球最多[得分]":
        resultDICT['level'] = 'single'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "一場球最高[得分]":
        resultDICT['level'] = 'single'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "單場[得分]平均":
        resultDICT['level'] = 'avg'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "單場最多[得分]":
        resultDICT['level'] = 'single'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "單場最高[得分]":
        resultDICT['level'] = 'single'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "單場次最多[得分]":
        resultDICT['level'] = 'single'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "單場次最高[得分]":
        resultDICT['level'] = 'single'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "單場球最多[得分]":
        resultDICT['level'] = 'single'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "單場球最高[得分]":
        resultDICT['level'] = 'single'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "場均[得分]":
        resultDICT['level'] = 'avg'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "平均[得分]":
        resultDICT['level'] = 'avg'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "每一場[得分]平均":
        resultDICT['level'] = 'avg'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "每場[得分]平均":
        resultDICT['level'] = 'avg'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "平均[籃板]最多":
        resultDICT['level'] = 'avg'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "平均[籃板]最高":
        resultDICT['level'] = 'avg'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "單場[籃板]最多":
        resultDICT['level'] = 'single'
        resultDICT = get_stat(resultDICT, args[0])
        pass

    if utterance == "單場[籃板]最高":
        resultDICT['level'] = 'single'
        resultDICT = get_stat(resultDICT, args[0])
        pass


    return resultDICT