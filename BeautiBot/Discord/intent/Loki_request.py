#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for request

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_request = True
userDefinedDICT = {"bodypart": ["毛", "腋", "腋下", "腿", "小腿", "大腿", "膝蓋", "腳", "腳趾", "腳背", "比基尼線", "私密處", "手", "手臂", "上手臂", "下手臂", "全手", "手指", "手背", "臉", "全臉", "鬍子", "眉心", "唇周", "下巴", "頸", "前頸", "後頸", "胸", "胸部", "腹", "腹部", "子母線", "背", "上背", "下背", "臀", "臀部", "乳暈", "胳肢窩", "陰", "陰部"], "location": ["忠孝敦化", "南西"], "medicalCondition": ["藥物過敏", "凝血功能障礙", "蟹足腫", "免疫疾病", "糖尿病", "癲癇", "懷孕", "哺乳中", "抗生素"]}

import logging
import json
from ArticutAPI import Articut
with open("account.info.py", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())
articut = Articut(username = accountDICT["username"], apikey = accountDICT["articut_api_key"])

def getPersonSTR(inputSTR):
    resultDICT = {}
    resultDICT = articut.parse(inputSTR, level="lv3")
    personSTR = resultDICT["person"][0][0][2]
    return personSTR

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
    if DEBUG_request:
        print("[request] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我]想要除[腿]":
        if args[1] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        elif "毛" in inputSTR:
            resultDICT["bodypart"] = ""
            resultDICT["request"] = True
        else:
            resultDICT["bodypart"] = args[1]
            resultDICT["request"] = True
        pass

    if utterance == "[我]想要除[腿][上]的毛":
        if args[1] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[1]
            resultDICT["request"] = True
        pass

    if utterance == "[我]想要除[腿]毛":
        if args[1] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[1]
            resultDICT["request"] = True    
        pass

    if utterance == "[我]想除[腿]":
        if args[1] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        elif "毛" in inputSTR:
            resultDICT["bodypart"] = ""
            resultDICT["request"] = True
        else:
            resultDICT["bodypart"] = args[1]
            resultDICT["request"] = True
        pass

    if utterance == "[我]想除[腿][上]的毛":
        if args[1] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[1]
            resultDICT["request"] = True 
        pass

    if utterance == "[我]想除[腿]毛":
        if args[1] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[1]
            resultDICT["request"] = True
        pass

    if utterance == "[我]想除毛":
        if "除毛" in inputSTR:
            resultDICT["bodypart"] = ""
            resultDICT["request"] = True
        pass

    if utterance == "[我]想預約[星期一下午四點][南西]診所做除毛":
        resultDICT["request"] = True 
        resultDICT["appointmentClinic"] = args[2]    
        
        datetime = timeSTRConvert(args[1])["time"]
        #先處理中文日期
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

    if utterance == "[我]想預約[星期一下午四點][南西]診所的除毛療程":
        resultDICT["request"] = True 
        resultDICT["appointmentClinic"] = args[2]
        
        datetime = timeSTRConvert(args[1])["time"]
        #先處理中文日期
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

    if utterance == "[我]想預約[星期一下午四點][南西]診所除毛":
        resultDICT["request"] = True 
        resultDICT["appointmentClinic"] = args[2]
        
        datetime = timeSTRConvert(args[1])["time"]
        #先處理中文日期
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

    if utterance == "[腿]毛太長了想除[腿]毛":
        if args[0] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[0]
            resultDICT["request"] = True  
        pass

    if utterance == "[腿]毛太長了想除毛":
        if args[0] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[0]
            resultDICT["request"] = True 
        pass

    if utterance == "[腿]毛好長想除[腿]毛":
        if args[0] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[0]
            resultDICT["request"] = True 
        pass

    if utterance == "[腿]毛好長想除毛":
        if args[0] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[0]
            resultDICT["request"] = True  
        pass

    if utterance == "想除[腿]毛[我][腿]毛太長了":
        if args[0] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[0]
            resultDICT["request"] = True  
        pass

    if utterance == "想除[腿]毛[我][腿]毛好長":
        if args[0] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:          
            resultDICT["bodypart"] = args[0]
            resultDICT["request"] = True 
        pass

    if utterance == "[可以]除哪些部位":
        resultDICT["request"] = ""       
        pass

    if utterance == "[我]就是想要除[陰]毛":
        resultDICT["bodypart"] = args[1]
        resultDICT["request"] = True 
        pass

    if utterance == "[我]想要修[陰]毛":
        resultDICT["bodypart"] = args[1]
        resultDICT["request"] = True 
        pass

    if utterance == "[我]想要剪[陰]毛":
        resultDICT["bodypart"] = args[1]
        resultDICT["request"] = True 
        pass

    if utterance == "[我]的[陰部]有除毛需求":
        resultDICT["bodypart"] = args[1]
        resultDICT["request"] = True 
        pass

    if utterance == "有哪些部位[可以]除":
        resultDICT["request"] = "" 
        pass

    if utterance == "請問[你們][只有]除毛[可以]預約嗎":
        resultDICT["request"] = "" 
        pass

    if utterance == "請問[可以]除哪些部位":
        resultDICT["request"] = "" 
        pass

    if utterance == "請問什麼[時候][可以]幫[我]排除[陰]毛":
        resultDICT["bodypart"] = args[3]
        resultDICT["request"] = True 
        pass

    if utterance == "請問有哪些部位[可以]除":
        resultDICT["request"] = "" 
        pass

    if utterance == "請幫[我]預約除[陰]毛的療程":
        resultDICT["bodypart"] = args[1]
        resultDICT["request"] = True 
        pass

    if utterance == "[我]想找[王小明]除[腿]毛":
        if args[2] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = ""
        else:
            resultDICT["bodypart"] = args[2]
            resultDICT["request"] = True             
            try:
                resultDICT['appointmentDoctor'] = getPersonSTR(inputSTR)
            except Exception as e:
                logging.error("[not pass 1] {}".format(str(e)))
        pass

    if utterance == "[我]想找[王小明]除毛":
        resultDICT["request"] = True
        try:
            resultDICT['appointmentDoctor'] = getPersonSTR(inputSTR)
        except Exception as e:
            logging.error("[not pass 2] {}".format(str(e)))        
        pass

    if utterance == "[我]想要預約[王小明]醫師的門診":
        resultDICT["request"] = True
        try:
            resultDICT['appointmentDoctor'] = getPersonSTR(inputSTR)
        except Exception as e:
            logging.error("[not pass 2-1] {}".format(str(e)))          
        pass

    if utterance == "[我]想預約[星期一下午四點][南西]診所[王小明]醫生的除毛療程":
        resultDICT["request"] = True 
        resultDICT["appointmentClinic"] = args[2]
        try:
            resultDICT['appointmentDoctor'] = getPersonSTR(inputSTR)
            
            datetime = timeSTRConvert(args[1])["time"]
            #先處理中文日期
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
        except Exception as e:
            logging.error("[not pass 3] {}".format(str(e)))        
        pass

    if utterance == "[我]想預約[星期一下午四點][南西]診所的[王小明]醫生做除毛":
        resultDICT["request"] = True 
        resultDICT["appointmentClinic"] = args[2]
        try:
            resultDICT['appointmentDoctor'] = getPersonSTR(inputSTR)
            
            datetime = timeSTRConvert(args[1])["time"]
            #先處理中文日期
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
        except Exception as e:
            logging.error("[not pass 4] {}".format(str(e)))        
        pass

    if utterance == "[我]想預約[星期一下午四點]找[王小明]醫生做除毛":
        resultDICT["request"] = True 
        try:
            resultDICT['appointmentDoctor'] = getPersonSTR(inputSTR)   
            
            datetime = timeSTRConvert(args[1])["time"]
            #先處理中文日期
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
        except Exception as e:
            logging.error("[not pass 5] {}".format(str(e)))        
        pass

    if utterance == "[我]想預約[星期一下午四點]找[王小明]醫生的除毛療程":
        resultDICT["request"] = True 
        try:
            resultDICT['appointmentDoctor'] = getPersonSTR(inputSTR)
            
            datetime = timeSTRConvert(args[1])["time"]
            #先處理中文日期
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
        except Exception as e:
            logging.error("[not pass 6] {}".format(str(e)))        
        pass

    if utterance == "[我]想預約[星期一下午四點]找[王小明]醫生除毛":
        resultDICT["request"] = True 
        try:
            resultDICT['appointmentDoctor'] = getPersonSTR(inputSTR)
            
            datetime = timeSTRConvert(args[1])["time"]
            #先處理中文日期
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
        except Exception as e:
            logging.error("[not pass 7] {}".format(str(e)))        
        pass

    if utterance == "找[王小明]醫生除[腿]毛":
        if args[1] not in userDefinedDICT["bodypart"]:
            resultDICT["bodypart"] = False
        else:          
            resultDICT["bodypart"] = args[1]
            resultDICT["request"] = True 
            try:
                resultDICT['appointmentDoctor'] = getPersonSTR(inputSTR)
            except Exception as e:
                logging.error("[not pass 8] {}".format(str(e)))            
        pass

    if utterance == "找[王小明]醫生除毛":
        resultDICT["request"] = True 
        try:
            resultDICT['appointmentDoctor'] = getPersonSTR(inputSTR)
        except Exception as e:
            logging.error("[not pass 9] {}".format(str(e)))        
        pass
    
    return resultDICT