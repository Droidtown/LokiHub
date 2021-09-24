#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for appointmentTime

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_appointmentTime = True
userDefinedDICT = {"bodypart": ["毛", "腋", "腋下", "腿", "小腿", "大腿", "膝蓋", "腳", "腳趾", "腳背", "比基尼線", "私密處", "手", "手臂", "上手臂", "下手臂", "全手", "手指", "手背", "臉", "全臉", "鬍子", "眉心", "唇周", "下巴", "頸", "前頸", "後頸", "胸", "胸部", "腹", "腹部", "子母線", "背", "上背", "下背", "臀", "臀部", "乳暈", "胳肢窩", "陰", "陰部"], "location": ["忠孝敦化", "南西"], "medicalCondition": ["藥物過敏", "凝血功能障礙", "蟹足腫", "免疫疾病", "糖尿病", "癲癇", "懷孕", "哺乳中", "抗生素"]}

import re
import json
from ArticutAPI import Articut
with open("account.info.py", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())
articut = Articut(username = accountDICT["username"], apikey = accountDICT["articut_api_key"])

def timeSTRConvert(inputSTR):
    resultDICT = {}
    resultDICT = articut.parse(inputSTR, level="lv3")
    return resultDICT

from datetime import datetime
dt = datetime.now()

def format_identifier(time_STR):   #只有把時間格式轉成00:00，沒有處理日期格式
    if dt.strftime("%p") == "PM":
        time_STR = time_STR + "PM"
        #dt1 = dateparser.parse(time_STR)
        dt1 = datetime.strptime(str(time_STR),"%Y-%m-%d %H:%M:%S.%f")
        time_STR = datetime.strftime(dt1, '%H:%M')
        return time_STR   #16:00
    else:
        return time_STR

def time_check(hour, minute):
    if hour < 21 and hour > 11:
        if minute < 60 and minute >= 0:
            return True
    else:
        return False


# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_appointmentTime:
        print("[appointmentTime] {} ===> {}".format(inputSTR, utterance))
        
def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我]想預約[星期一下午四點]":
        #先處理中文日期
        datetime = timeSTRConvert(args[1])["time"]
        if datetime[0][0]["time_span"]["weekday"][0] == 7: #週日公休
            resultDICT['appointmentDay'] = False
        else:
            weekday = datetime[0][0]["datetime"][-19:-9] #抓articutAPI中time的日期 2021-09-13
            resultDICT['appointmentDay'] = weekday
        #再判斷時間是否在營業時間內
        hour = int(datetime[0][0]["datetime"][-8:-6])
        minute = int(datetime[0][0]["datetime"][-5:-3])
        if time_check(hour, minute):
            resultDICT ['appointmentTime'] = datetime[0][0]["datetime"][-8:-3]
        else:
            resultDICT ['appointmentTime'] = False
        pass
    
    
    if utterance == "[星期一下午四點]":
        #先處理中文日期
        datetime = timeSTRConvert(args[0])["time"]
        if datetime[0][0]["time_span"]["weekday"][0] == 7:
            resultDICT['appointmentDay'] = False
        else:
            weekday = datetime[0][0]["datetime"][-19:-9]
            resultDICT['appointmentDay'] = weekday
        #再判斷時間是否在營業時間內
        hour = int(datetime[0][0]["datetime"][-8:-6])
        minute = int(datetime[0][0]["datetime"][-5:-3])
        if time_check(hour, minute):
            resultDICT ['appointmentTime'] = datetime[0][0]["datetime"][-8:-3]
        else:
            resultDICT ['appointmentTime'] = False
        pass


    if utterance == "[星期一][16]:[00]":
        #先處理中文日期
        datetime = timeSTRConvert(args[0])["time"]
        if datetime[0][0]["time_span"]["weekday"][0] == 7:
            resultDICT['appointmentDay'] = False
        else:
            weekday = datetime[0][0]["datetime"][-19:-9]
            resultDICT['appointmentDay'] = weekday
        #再處理數字時間
        timeLIST = re.findall(r'[0-9]+:[0-9]+', inputSTR)
        timeSTR = "".join(timeLIST) #16:00
        #判斷時間是否在營業時間內 
        hour = int(timeSTR.split(":")[0])
        minute = int(timeSTR.split(":")[1])
        if time_check(hour, minute):
            resultDICT ['appointmentTime'] = timeSTR
        else:
            resultDICT ['appointmentTime'] = False  
        pass


    if utterance == "[可以][星期一][16]:[00]嗎":
        #先處理中文日期
        datetime = timeSTRConvert(args[1])["time"]
        if datetime[0][0]["time_span"]["weekday"][0] == 7:
            resultDICT['appointmentDay'] = False
        else:
            weekday = datetime[0][0]["datetime"][-19:-9]
            resultDICT['appointmentDay'] = weekday
        #再處理數字時間
        timeLIST = re.findall(r'[0-9]+:[0-9]+', inputSTR)
        timeSTR = "".join(timeLIST) #16:00
        #判斷時間是否在營業時間內 
        hour = int(timeSTR.split(":")[0])
        minute = int(timeSTR.split(":")[1])
        if time_check(hour, minute):
            resultDICT ['appointmentTime'] = timeSTR
        else:
            resultDICT ['appointmentTime'] = False   
        pass
    
    
    if utterance == "[可以][星期一下午四點]嗎":
        #先處理中文日期
        datetime = timeSTRConvert(args[1])["time"]
        if datetime[0][0]["time_span"]["weekday"][0] == 7:
            resultDICT['appointmentDay'] = False
        else:
            weekday = datetime[0][0]["datetime"][-19:-9]
            resultDICT['appointmentDay'] = weekday
        #再判斷時間是否在營業時間內
        hour = int(datetime[0][0]["datetime"][-8:-6])
        minute = int(datetime[0][0]["datetime"][-5:-3])
        if time_check(hour, minute):
            resultDICT ['appointmentTime'] = datetime[0][0]["datetime"][-8:-3]
        else:
            resultDICT ['appointmentTime'] = False
        pass
    
    if utterance == "[星期一][16]:[00][可以]嗎":
        #先處理中文日期
        datetime = timeSTRConvert(args[0])["time"]
        if datetime[0][0]["time_span"]["weekday"][0] == 7:
            resultDICT['appointmentDay'] = False
        else:
            weekday = datetime[0][0]["datetime"][-19:-9]
            resultDICT['appointmentDay'] = weekday
        #再處理數字時間
        timeLIST = re.findall(r'[0-9]+:[0-9]+', inputSTR)
        timeSTR = "".join(timeLIST) #16:00
        #判斷時間是否在營業時間內 
        hour = int(timeSTR.split(":")[0])
        minute = int(timeSTR.split(":")[1])
        if time_check(hour, minute):
            resultDICT ['appointmentTime'] = timeSTR
        else:
            resultDICT ['appointmentTime'] = False   
        pass
    
    if utterance == "[星期一下午四點][可以]嗎":
        #先處理中文日期
        datetime = timeSTRConvert(args[0])["time"]
        if datetime[0][0]["time_span"]["weekday"][0] == 7:
            resultDICT['appointmentDay'] = False
        else:
            weekday = datetime[0][0]["datetime"][-19:-9]
            resultDICT['appointmentDay'] = weekday
        #再判斷時間是否在營業時間內
        hour = int(datetime[0][0]["datetime"][-8:-6])
        minute = int(datetime[0][0]["datetime"][-5:-3])
        if time_check(hour, minute):
            resultDICT ['appointmentTime'] = datetime[0][0]["datetime"][-8:-3]
        else:
            resultDICT ['appointmentTime'] = False
        pass


    if utterance == "[我]想預約[星期一下午四點]做除毛":
        resultDICT["request"] = True  
        #先處理中文日期
        datetime = timeSTRConvert(args[1])["time"]
        if datetime[0][0]["time_span"]["weekday"][0] == 7:
            resultDICT['appointmentDay'] = False
        else:
            weekday = datetime[0][0]["datetime"][-19:-9]
            resultDICT['appointmentDay'] = weekday
        #再判斷時間是否在營業時間內
        hour = int(datetime[0][0]["datetime"][-8:-6])
        minute = int(datetime[0][0]["datetime"][-5:-3])
        if time_check(hour, minute):
            resultDICT ['appointmentTime'] = datetime[0][0]["datetime"][-8:-3]
        else:
            resultDICT ['appointmentTime'] = False
        pass


    if utterance == "[我]想預約[星期一下午四點]的時段做除毛":
        resultDICT["request"] = True  
        #先處理中文日期
        datetime = timeSTRConvert(args[1])["time"]
        if datetime[0][0]["time_span"]["weekday"][0] == 7:
            resultDICT['appointmentDay'] = False
        else:
            weekday = datetime[0][0]["datetime"][-19:-9]
            resultDICT['appointmentDay'] = weekday
        #再判斷時間是否在營業時間內
        hour = int(datetime[0][0]["datetime"][-8:-6])
        minute = int(datetime[0][0]["datetime"][-5:-3])
        if time_check(hour, minute):
            resultDICT ['appointmentTime'] = datetime[0][0]["datetime"][-8:-3]
        else:
            resultDICT ['appointmentTime'] = False
        pass
    

    if utterance == "[我]想預約[星期一下午四點]的時段的除毛":
        resultDICT["request"] = True  
        #先處理中文日期
        datetime = timeSTRConvert(args[1])["time"]
        if datetime[0][0]["time_span"]["weekday"][0] == 7:
            resultDICT['appointmentDay'] = False
        else:
            weekday = datetime[0][0]["datetime"][-19:-9]
            resultDICT['appointmentDay'] = weekday
        #再判斷時間是否在營業時間內
        hour = int(datetime[0][0]["datetime"][-8:-6])
        minute = int(datetime[0][0]["datetime"][-5:-3])
        if time_check(hour, minute):
            resultDICT ['appointmentTime'] = datetime[0][0]["datetime"][-8:-3]
        else:
            resultDICT ['appointmentTime'] = False
        pass
    

    if utterance == "[我]想預約[星期一下午四點]的除毛門診":
        resultDICT["request"] = True  
        #先處理中文日期
        datetime = timeSTRConvert(args[1])["time"]
        if datetime[0][0]["time_span"]["weekday"][0] == 7:
            resultDICT['appointmentDay'] = False
        else:
            weekday = datetime[0][0]["datetime"][-19:-9]
            resultDICT['appointmentDay'] = weekday
        #再判斷時間是否在營業時間內
        hour = int(datetime[0][0]["datetime"][-8:-6])
        minute = int(datetime[0][0]["datetime"][-5:-3])
        if time_check(hour, minute):
            resultDICT ['appointmentTime'] = datetime[0][0]["datetime"][-8:-3]
        else:
            resultDICT ['appointmentTime'] = False
        pass
    

    if utterance == "[我]想預約[星期一下午四點]除毛":
        resultDICT["request"] = True  
        #先處理中文日期
        datetime = timeSTRConvert(args[1])["time"]
        if datetime[0][0]["time_span"]["weekday"][0] == 7:
            resultDICT['appointmentDay'] = False
        else:
            weekday = datetime[0][0]["datetime"][-19:-9]
            resultDICT['appointmentDay'] = weekday
        #再判斷時間是否在營業時間內
        hour = int(datetime[0][0]["datetime"][-8:-6])
        minute = int(datetime[0][0]["datetime"][-5:-3])
        if time_check(hour, minute):
            resultDICT ['appointmentTime'] = datetime[0][0]["datetime"][-8:-3]
        else:
            resultDICT ['appointmentTime'] = False
        pass
    
    
    if utterance == "[我]想預約[星期一下午四點]的時段的除毛療程":
        resultDICT["request"] = True  
        #先處理中文日期
        datetime = timeSTRConvert(args[1])["time"]
        if datetime[0][0]["time_span"]["weekday"][0] == 7:
            resultDICT['appointmentDay'] = False
        else:
            weekday = datetime[0][0]["datetime"][-19:-9]
            resultDICT['appointmentDay'] = weekday
        #再判斷時間是否在營業時間內
        hour = int(datetime[0][0]["datetime"][-8:-6])
        minute = int(datetime[0][0]["datetime"][-5:-3])
        if time_check(hour, minute):
            resultDICT ['appointmentTime'] = datetime[0][0]["datetime"][-8:-3]
        else:
            resultDICT ['appointmentTime'] = False
        pass

    if utterance == "[我]想預約[星期一下午四點]的除毛療程":
        resultDICT["request"] = True  
        #先處理中文日期
        datetime = timeSTRConvert(args[1])["time"]
        if datetime[0][0]["time_span"]["weekday"][0] == 7:
            resultDICT['appointmentDay'] = False
        else:
            weekday = datetime[0][0]["datetime"][-19:-9]
            resultDICT['appointmentDay'] = weekday
        #再判斷時間是否在營業時間內
        hour = int(datetime[0][0]["datetime"][-8:-6])
        minute = int(datetime[0][0]["datetime"][-5:-3])
        if time_check(hour, minute):
            resultDICT ['appointmentTime'] = datetime[0][0]["datetime"][-8:-3]
        else:
            resultDICT ['appointmentTime'] = False
        pass  
    
    if utterance == "[我]想改[星期一][16]:[00]":
        if "改" in inputSTR:
            #先處理中文日期
            datetime = timeSTRConvert(args[1])["time"]
            if datetime[0][0]["time_span"]["weekday"][0] == 7:
                resultDICT['appointmentDay'] = False
            else:
                weekday = datetime[0][0]["datetime"][-19:-9]
                resultDICT['appointmentDay'] = weekday
            #再處理數字時間
            timeLIST = re.findall(r'[0-9]+:[0-9]+', inputSTR)
            timeSTR = "".join(timeLIST) #16:00
            #判斷時間是否在營業時間內 
            hour = int(timeSTR.split(":")[0])
            minute = int(timeSTR.split(":")[1])
            if time_check(hour, minute):
                resultDICT ['appointmentTime'] = timeSTR
            else:
                resultDICT ['appointmentTime'] = False  
        pass           

    if utterance == "[我]想改[星期一下午四點]":
        if "改" in inputSTR:
            #先處理中文日期
            datetime = timeSTRConvert(args[1])["time"]
            if datetime[0][0]["time_span"]["weekday"][0] == 7:
                resultDICT['appointmentDay'] = False
            else:
                weekday = datetime[0][0]["datetime"][-19:-9]
                resultDICT['appointmentDay'] = weekday
            #再判斷時間是否在營業時間內
            hour = int(datetime[0][0]["datetime"][-8:-6])
            minute = int(datetime[0][0]["datetime"][-5:-3])
            if time_check(hour, minute):
                resultDICT ['appointmentTime'] = datetime[0][0]["datetime"][-8:-3]
            else:
                resultDICT ['appointmentTime'] = False
        pass

    if utterance == "[16]:[00]":
        #處理數字時間
        timeLIST = re.findall(r'[0-9]+:[0-9]+', inputSTR)
        timeSTR = "".join(timeLIST) #16:00
        #判斷時間是否在營業時間內 
        hour = int(timeSTR.split(":")[0])
        minute = int(timeSTR.split(":")[1])
        if time_check(hour, minute):
            resultDICT ['appointmentTime'] = timeSTR
        else:
            resultDICT ['appointmentTime'] = False   
        pass

    if utterance == "[16]:[00][可以]嗎":
        #處理數字時間
        timeLIST = re.findall(r'[0-9]+:[0-9]+', inputSTR)
        timeSTR = "".join(timeLIST) #16:00
        #判斷時間是否在營業時間內 
        hour = int(timeSTR.split(":")[0])
        minute = int(timeSTR.split(":")[1])
        if time_check(hour, minute):
            resultDICT ['appointmentTime'] = timeSTR
        else:
            resultDICT ['appointmentTime'] = False   
        pass
    
    return resultDICT
