#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for side_effect
    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict
    Output:
        resultDICT    dict
"""

import json

with open("json/side_effect.json", mode="r", encoding="utf-8") as file:
    sideeffectDICT = json.loads(file.read())

with open("json/hospital_immediately.json", mode="r", encoding="utf-8") as f:
    hospitalDICT = json.loads(f.read())

DEBUG_side_effect = True
userDefinedDICT = {"AZ": ["AZ", "AstraZeneca", "az", "牛津", "牛津/阿斯利康", "阿斯利康", "阿斯特捷利康"], "dose": ["第一劑", "第三劑", "第二劑"], "blank": [""], "Taiwan": ["全台", "全台灣", "全國", "全島", "全臺", "全臺各地", "全臺灣", "台灣", "本國", "本島", "臺灣"], "Medigen": ["Medigen", "medigen", "高端"], "Moderna": ["Moderna", "莫德納", "moderna"], "leftover": ["剩量", "剩餘", "剩餘分佈", "剩餘分布", "剩餘情形", "剩餘數", "剩餘數字", "剩餘狀況", "剩餘資料", "剩餘量", "庫存"], "location": ["Changhua", "Changhua County", "Chiayi", "Chiayi City", "Chiayi County", "Hsinchu", "Hsinchu City", "Hsinchu County", "Hualian", "Hualian County", "Ilan", "Ilan County", "Kaohsiung", "Kaohsiung City", "Kaohsiung County", "Keelung", "Keelung City", "Kinmen", "Kinmen County", "Lianjiang", "Lianjiang County", "Matsu", "Matsu Islands", "Mazu", "Miaoli", "Miaoli County", "Nantou", "Nantou County", "New Taipei", "New Taipei City", "Penghu", "Penghu County", "Pescadores", "Pescadores Islands", "Pingtung", "Pingtung County", "Quemoy", "Quemoy Island", "TPE", "Taibei", "Taibei City", "Taichung", "Taichung City", "Taichung County", "Tainan", "Tainan City", "Tainan County", "Taipei", "Taipei City", "Taitung", "Taitung County", "Taoyuan", "Taoyuan City", "Taoyuan County", "Xinbei", "Xinbei City", "Yunlin", "Yunlin County", "changhua", "changhua county", "chiayi", "chiayi city", "chiayi county", "hsinchu", "hsinchu city", "hsinchu county", "hualian", "hualian county", "ilan", "ilan county", "kaohsiung", "kaohsiung city", "kaohsiung county", "keelung", "keelung city", "kinmen", "kinmen county", "lianjiang", "lianjiang county", "matsu", "matsu islands", "mazu", "miaoli", "miaoli county", "nantou", "nantou county", "new taipei", "new taipei city", "penghu", "penghu county", "pescadores", "pescadores islands", "pingtung", "pingtung county", "quemoy", "quemoy island", "taibei city", "taichung", "taichung city", "taichung county", "tainan", "tainan city", "tainan county", "taipei", "taipei city", "taitung", "taitung county", "taoyuan", "taoyuan city", "taoyuan county", "tpe", "xinbei", "xinbei city", "yunlin", "yunlin county", "中市", "北市", "南市", "南投", "南投縣", "台中", "台中市", "台中縣", "台北", "台北市", "台北縣", "台南", "台南市", "台南縣", "台東", "台東縣", "嘉市", "嘉縣", "嘉義", "嘉義市", "嘉義縣", "基隆", "基隆市", "天龍", "天龍國", "宜蘭", "宜蘭縣", "屏東", "屏東縣", "彰化", "彰化縣", "彰縣", "新北", "新北市", "新竹", "新竹市", "新竹縣", "桃園", "桃園市", "桃園縣", "桃市", "澎湖", "澎湖縣", "竹市", "竹縣", "臺中", "臺中市", "臺中縣", "臺北", "臺北市", "臺北縣", "臺南", "臺南市", "臺南縣", "臺東", "臺東縣", "花蓮", "花蓮縣", "苗栗", "苗栗縣", "連江", "連江縣", "金門", "金門縣", "雲林", "雲林縣", "雲縣", "馬祖", "馬祖列島", "馬祖列嶼", "高市", "高雄", "高雄市", "高雄縣"], "syn_verb": ["出現", "有"], "group_num": ["第一類", "第七類", "第三類", "第九類", "第二類", "第五類", "第八類", "第六類", "第十類", "第四類"], "第一劑": ["第 1 劑", "第 1劑", "第1 劑", "第1劑", "第１劑"], "第二劑": ["第 2 劑", "第 2劑", "第2 劑", "第2劑", "第２劑"], "information": ["最新資訊", "資訊"], "side_effect": ["副作用"], "updated_info": ["最新", "目前"], "vaccine_verb": ["", "打完", "打過", "接種", "注射"], "Pfizer-BioNTech": ["BIOTECH", "BNT", "BioTech", "Biotech", "Pfizer-BioNTech", "biotech", "bnt", "上海復興", "上海復興BNT", "輝瑞"]}
vaccineDICT = userDefinedDICT["AZ"] + userDefinedDICT["Moderna"] + userDefinedDICT["Pfizer-BioNTech"] + userDefinedDICT["Medigen"]

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_side_effect:
        print("[side_effect] {} ===> {}".format(inputSTR, utterance))

def formalize_name_side_effect(val, resultDICT, resultSTR, resultSTR2):
    count = 0
    for k in userDefinedDICT.keys():
        if val in userDefinedDICT[k]:
            if count == 0: 
                resultDICT[resultSTR].append(k)
                side_effect = sideeffectDICT[k]
                resultDICT[resultSTR2].append(side_effect)
                resultDICT["inquiry_type"].append("side_effect")
                # resultDICT["confirm"] = True
                count+=1
            if count > 1: 
                print(f"Name Error: Duplicate Names! ({val})")

def formalize_name_severe_side_effect(val, resultDICT, resultSTR, resultSTR2):
    count = 0
    for k in userDefinedDICT.keys():
        if val in userDefinedDICT[k]:
            if count == 0: 
                resultDICT[resultSTR].append(k)
                severe_side_effect= hospitalDICT[k]
                resultDICT[resultSTR2].append(severe_side_effect)
                resultDICT["inquiry_type"].append("severe_side_effect")
                # resultDICT["confirm"] = True
                count+=1
            if count > 1: 
                print(f"Name Error: Duplicate Names! ({val})")

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    for k in ("vaccine_shot", "side_effect", "severe_side_effect", "inquiry_type"):
        if k in resultDICT.keys():
            pass
        else:
            resultDICT[k] = []
    # print(resultDICT) #確認resultDICT是否為空資料，
    # 原本寫法是告訴你當resultdict為空時，才會繼續作業
    # 新的寫法是當k不在keys中時可以加入新的[]
    if utterance == "[az][嚴重]副作用":
        if args[1] != "": # 要使用空字串!
            formalize_name_severe_side_effect(args[0], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[1] == "":
            formalize_name_side_effect(args[0], resultDICT, "vaccine_shot", "side_effect")

    if utterance == "[az]疫苗[嚴重]副作用":
        if args[1] != "":
            formalize_name_severe_side_effect(args[0], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[1] == "":
            formalize_name_side_effect(args[0], resultDICT, "vaccine_shot", "side_effect")

    if utterance == "[打完][莫德納][後]，[出現]哪些[嚴重]副作用需要送醫":
        if args[4] != "":
            formalize_name_severe_side_effect(args[0], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[4] == "":
            formalize_name_side_effect(args[0], resultDICT, "vaccine_shot", "side_effect")

    if utterance == "[打完][莫德納]疫苗[後]，[出現]哪些[嚴重]副作用需要送醫":
        if args[4] != "":
            formalize_name_severe_side_effect(args[0], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[4] == "":
            formalize_name_side_effect(args[0], resultDICT, "vaccine_shot", "side_effect")

    if utterance == "[第一劑][az][嚴重]副作用":
        if args[2] != "":
            formalize_name_severe_side_effect(args[1], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[2] == "":
            formalize_name_side_effect(args[1], resultDICT, "vaccine_shot", "side_effect")

    if utterance == "[第一劑][az][會][有]哪些[嚴重]副作用":
        if args[4] != "":
            formalize_name_severe_side_effect(args[1], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[4] == "":
            formalize_name_side_effect(args[1], resultDICT, "vaccine_shot", "side_effect")

    if utterance == "[第一劑][az]疫苗[嚴重]副作用":
        if args[2] != "":
            formalize_name_severe_side_effect(args[1], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[2] == "":
            formalize_name_side_effect(args[1], resultDICT, "vaccine_shot", "side_effect")

    if utterance == "[第一劑][az]疫苗[會][有]哪些[嚴重]副作用":
        if args[4] != "":
            formalize_name_severe_side_effect(args[1], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[4] == "":
            formalize_name_side_effect(args[1], resultDICT, "vaccine_shot", "side_effect")

    if utterance == "請問[az]疫苗[嚴重]副作用為何":
        if args[1] != "":
            formalize_name_severe_side_effect(args[0], resultDICT, "vaccine_shot", "severe_side_effect")
        elif args[1] == "":
            formalize_name_side_effect(args[0], resultDICT, "vaccine_shot", "side_effect")
    print(resultDICT)
    return resultDICT