#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for bodypart

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_bodypart = True
userDefinedDICT = {"bodypart": ["毛", "腋", "腋下", "腿", "小腿", "大腿", "膝蓋", "腳", "腳趾", "腳背", "比基尼線", "私密處", "手", "手臂", "上手臂", "下手臂", "全手", "手指", "手背", "臉", "全臉", "鬍子", "眉心", "唇周", "下巴", "頸", "前頸", "後頸", "胸", "胸部", "腹", "腹部", "子母線", "背", "上背", "下背", "臀", "臀部", "乳暈", "胳肢窩", "陰", "陰部"], "location": ["忠孝敦化", "南西"], "medicalCondition": ["藥物過敏", "凝血功能障礙", "蟹足腫", "免疫疾病", "糖尿病", "癲癇", "懷孕", "哺乳中", "抗生素"]}

    
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_bodypart:
        print("[bodypart] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    
    if utterance == "[腿]":
        if args[0] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:
            resultDICT["bodypart"] = args[0]
            resultDICT["request"] = True
            resultDICT["confirm"] = ""
            
    if utterance == "[腿]毛[太長]了想除毛":
        if args[0] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:        
            resultDICT["bodypart"] = args[0]
            resultDICT["request"] = True
            resultDICT["confirm"] = ""
        pass

    if utterance == "[腿]毛太長了":
        if args[0] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[0]
            resultDICT["request"] = ""
            resultDICT["confirm"] = ""
        pass

    if utterance == "[腿]毛太長了想除[腿]毛":
        if args[0] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[0]
            resultDICT["request"] = True
            resultDICT["confirm"] = ""
        pass

    if utterance == "[腿]毛好長":
        if args[0] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[0]
            resultDICT["request"] = ""
            resultDICT["confirm"] = ""
        pass

    if utterance == "[腿]毛好長想除[腿]毛":
        if args[0] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[0]
            resultDICT["request"] = True
            resultDICT["confirm"] = ""
        pass

    if utterance == "[腿]毛好長想除毛":
        if args[0] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[0]
            resultDICT["request"] = True
            resultDICT["confirm"] = ""
        pass

    if utterance == "想除[腿]毛[腿]毛太長了":
        if args[0] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[0]
            resultDICT["request"] = True
            resultDICT["confirm"] = ""
        pass

    if utterance == "想除[腿]毛[腿]毛好長":
        if args[0] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[0]
            resultDICT["request"] = True
            resultDICT["confirm"] = ""
        pass

    if utterance == "[腿][可以]嗎":
        if args[0] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[0]
            resultDICT["request"] = True
            resultDICT["confirm"] = ""
        pass

    return resultDICT