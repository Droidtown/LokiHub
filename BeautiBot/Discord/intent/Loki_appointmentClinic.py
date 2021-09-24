#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for appointmentClinic

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_appointmentClinic = True
userDefinedDICT = {"bodypart": ["毛", "腋", "腋下", "腿", "小腿", "大腿", "膝蓋", "腳", "腳趾", "腳背", "比基尼線", "私密處", "手", "手臂", "上手臂", "下手臂", "全手", "手指", "手背", "臉", "全臉", "鬍子", "眉心", "唇周", "下巴", "頸", "前頸", "後頸", "胸", "胸部", "腹", "腹部", "子母線", "背", "上背", "下背", "臀", "臀部", "乳暈", "胳肢窩", "陰", "陰部"], "location": ["忠孝敦化", "南西"], "medicalCondition": ["藥物過敏", "凝血功能障礙", "蟹足腫", "免疫疾病", "糖尿病", "癲癇", "懷孕", "哺乳中", "抗生素"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_appointmentClinic:
        print("[appointmentClinic] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[忠孝敦化]":
        if args[0] not in userDefinedDICT["location"]:
            pass   
        else:
            resultDICT["appointmentClinic"] = args[0]
        pass

    if utterance == "[我]要[忠孝敦化]":
        if "要" in inputSTR:
            if args[1] not in userDefinedDICT["location"]:
                pass  
            else:            
                resultDICT["appointmentClinic"] = args[1]
        pass

    if utterance == "[我]要約在[忠孝敦化]的診所":
        if "要約" in inputSTR:
            resultDICT["appointmentClinic"] = args[1]
        pass

    if utterance == "[忠孝敦化][可以]嗎":
        if args[0] not in userDefinedDICT["location"]:
            pass  
        else:        
            resultDICT["appointmentClinic"] = args[0]        
        pass

    if utterance == "[忠孝敦化]診所":
        if "診所" in inputSTR:
            resultDICT["appointmentClinic"] = args[0]
        pass

    if utterance == "[忠孝敦化]診所[可以]嗎":
        if "診所" in inputSTR:
            resultDICT["appointmentClinic"] = args[0]  
        pass

    if utterance == "[忠孝敦化]診所比較方便":
        if "診所" in inputSTR:
            resultDICT["appointmentClinic"] = args[0]  
        pass

    if utterance == "[我]想預約[忠孝敦化]診所":
        if "預約" in inputSTR:
            resultDICT["appointmentClinic"] = args[1]
        pass

    if utterance == "[我]想預約[忠孝敦化]診所做除毛":
        if "預約" in inputSTR:
            resultDICT["appointmentClinic"] = args[1]
            resultDICT["request"] = True  
        pass

    if utterance == "[我]想預約[忠孝敦化]診所的除毛療程":
        if "預約" in inputSTR:
            resultDICT["appointmentClinic"] = args[1]
            resultDICT["request"] = True  
        pass

    if utterance == "[我]想預約[忠孝敦化]診所除毛":
        if "預約" in inputSTR:
            resultDICT["appointmentClinic"] = args[1]
            resultDICT["request"] = True  
        pass

    if utterance == "[我]要[忠孝敦化]診所":
        if "診所" in inputSTR:
            resultDICT["appointmentClinic"] = args[1]
        pass

    if utterance == "[我]想改[忠孝敦化]":
        if "改" in inputSTR:
            if args[1] not in userDefinedDICT["location"]:
                pass  
            else:
                resultDICT["appointmentClinic"] = args[1]
        pass

    if utterance == "[我]想改[忠孝敦化]診所":
        if "改" in inputSTR and "診所" in inputSTR:
            resultDICT["appointmentClinic"] = args[1]
        pass
    
    return resultDICT