#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for confirm_check

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_confirm_check = True
userDefinedDICT = {"AZ": ["AZ", "AstraZeneca", "az", "牛津", "牛津/阿斯利康", "阿斯利康", "阿斯特捷利康"], "dose": ["第一劑", "第三劑", "第二劑"], "blank": [""], "Taiwan": ["全台", "全台灣", "全國", "全島", "全臺", "全臺各地", "全臺灣", "台灣", "本國", "本島", "臺灣"], "Medigen": ["Medigen", "medigen", "高端"], "Moderna": ["Moderna", "莫德納", "moderna"], "leftover": ["剩量", "剩餘", "剩餘分佈", "剩餘分布", "剩餘情形", "剩餘數", "剩餘數字", "剩餘狀況", "剩餘資料", "剩餘量", "庫存"], "location": ["Changhua", "Changhua County", "Chiayi", "Chiayi City", "Chiayi County", "Hsinchu", "Hsinchu City", "Hsinchu County", "Hualian", "Hualian County", "Ilan", "Ilan County", "Kaohsiung", "Kaohsiung City", "Kaohsiung County", "Keelung", "Keelung City", "Kinmen", "Kinmen County", "Lianjiang", "Lianjiang County", "Matsu", "Matsu Islands", "Mazu", "Miaoli", "Miaoli County", "Nantou", "Nantou County", "New Taipei", "New Taipei City", "Penghu", "Penghu County", "Pescadores", "Pescadores Islands", "Pingtung", "Pingtung County", "Quemoy", "Quemoy Island", "TPE", "Taibei", "Taibei City", "Taichung", "Taichung City", "Taichung County", "Tainan", "Tainan City", "Tainan County", "Taipei", "Taipei City", "Taitung", "Taitung County", "Taoyuan", "Taoyuan City", "Taoyuan County", "Xinbei", "Xinbei City", "Yunlin", "Yunlin County", "changhua", "changhua county", "chiayi", "chiayi city", "chiayi county", "hsinchu", "hsinchu city", "hsinchu county", "hualian", "hualian county", "ilan", "ilan county", "kaohsiung", "kaohsiung city", "kaohsiung county", "keelung", "keelung city", "kinmen", "kinmen county", "lianjiang", "lianjiang county", "matsu", "matsu islands", "mazu", "miaoli", "miaoli county", "nantou", "nantou county", "new taipei", "new taipei city", "penghu", "penghu county", "pescadores", "pescadores islands", "pingtung", "pingtung county", "quemoy", "quemoy island", "taibei city", "taichung", "taichung city", "taichung county", "tainan", "tainan city", "tainan county", "taipei", "taipei city", "taitung", "taitung county", "taoyuan", "taoyuan city", "taoyuan county", "tpe", "xinbei", "xinbei city", "yunlin", "yunlin county", "中市", "北市", "南市", "南投", "南投縣", "台中", "台中市", "台中縣", "台北", "台北市", "台北縣", "台南", "台南市", "台南縣", "台東", "台東縣", "嘉市", "嘉縣", "嘉義", "嘉義市", "嘉義縣", "基隆", "基隆市", "天龍", "天龍國", "宜蘭", "宜蘭縣", "屏東", "屏東縣", "彰化", "彰化縣", "彰縣", "新北", "新北市", "新竹", "新竹市", "新竹縣", "桃園", "桃園市", "桃園縣", "桃市", "澎湖", "澎湖縣", "竹市", "竹縣", "臺中", "臺中市", "臺中縣", "臺北", "臺北市", "臺北縣", "臺南", "臺南市", "臺南縣", "臺東", "臺東縣", "花蓮", "花蓮縣", "苗栗", "苗栗縣", "連江", "連江縣", "金門", "金門縣", "雲林", "雲林縣", "雲縣", "馬祖", "馬祖列島", "馬祖列嶼", "高市", "高雄", "高雄市", "高雄縣"], "syn_verb": ["出現", "有"], "group_num": ["第一類", "第七類", "第三類", "第九類", "第二類", "第五類", "第八類", "第六類", "第十類", "第四類"], "第一劑": ["第 1 劑", "第 1劑", "第1 劑", "第1劑", "第１劑"], "第二劑": ["第 2 劑", "第 2劑", "第2 劑", "第2劑", "第２劑"], "information": ["最新資訊", "資訊"], "side_effect": ["副作用"], "updated_info": ["最新", "目前"], "vaccine_verb": ["", "打完", "打過", "接種", "注射"], "Pfizer-BioNTech": ["BIOTECH", "BNT", "BioTech", "Biotech", "Pfizer-BioNTech", "biotech", "bnt", "上海復興", "上海復興BNT", "輝瑞"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_confirm_check:
        print("[confirm_check] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance) 
    resultDICT["completed"] = False
    # if utterance == "不是":
    #     if len(inputSTR) < 3:
    #         resultDICT["completed"]= False
    #     pass

    # if utterance == "好":
    #     if len(inputSTR) < 2:
    #         resultDICT["completed"]= True
    #     pass

    # if utterance == "是":
    #     if len(inputSTR) < 2:
    #         resultDICT["completed"] = True
    #     pass

    # if utterance == "有":
    #     if len(inputSTR) < 2:
    #         resultDICT["completed"] = True
    #     pass

    if utterance == "沒有":
        if len(inputSTR) < 3:
            resultDICT["completed"] = True
        pass

    return resultDICT