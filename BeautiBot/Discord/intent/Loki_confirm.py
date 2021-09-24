#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for confirm

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_confirm = True
userDefinedDICT = {"bodypart": ["毛", "腋", "腋下", "腿", "小腿", "大腿", "膝蓋", "腳", "腳趾", "腳背", "比基尼線", "私密處", "手", "手臂", "上手臂", "下手臂", "全手", "手指", "手背", "臉", "全臉", "鬍子", "眉心", "唇周", "下巴", "頸", "前頸", "後頸", "胸", "胸部", "腹", "腹部", "子母線", "背", "上背", "下背", "臀", "臀部", "乳暈", "胳肢窩", "陰", "陰部"], "location": ["忠孝敦化", "南西"], "medicalCondition": ["藥物過敏", "凝血功能障礙", "蟹足腫", "免疫疾病", "糖尿病", "癲癇", "懷孕", "哺乳中", "抗生素"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_confirm:
        print("[confirm] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "不好":
        if "不對" in inputSTR:
            resultDICT["confirm"] = False
        else:
            resultDICT["confirm"] = False
        pass

    if utterance == "不是":
        if "不是的" in inputSTR:
            resultDICT["confirm"] = False
        else:
            resultDICT["confirm"] = False
        pass

    if utterance == "不確定":
        if "不正確" in inputSTR:
            resultDICT["confirm"] = False
        else:
            resultDICT["confirm"] = False
        pass

    if utterance == "好":
        if "正確" in inputSTR:
            resultDICT["confirm"] = True
        elif "對" in inputSTR:
            resultDICT["confirm"] = True
        else:
            resultDICT["confirm"] = True
        pass

    if utterance == "好的":
        resultDICT["confirm"] = True
        pass

    if utterance == "恩恩":
        if "恩" in inputSTR or "嗯" in inputSTR:
            resultDICT["confirm"] = True
        else:
            resultDICT["confirm"] = True
        pass

    if utterance == "摁":
        resultDICT["confirm"] = True
        pass

    if utterance == "摁摁":
        if "嗯嗯" in inputSTR:
            resultDICT["confirm"] = True
        else:
            resultDICT["confirm"] = True
        pass

    if utterance == "是":
        if "是的" in inputSTR:
            resultDICT["confirm"] = True
        else:
            resultDICT["confirm"] = True
        pass

    if utterance == "有":
        resultDICT["confirm"] = True
        pass

    if utterance == "沒有":
        resultDICT["confirm"] = False
        pass

    return resultDICT