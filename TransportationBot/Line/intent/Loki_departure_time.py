#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for departure_time

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""
from ArticutAPI import ArticutAPI
articut = ArticutAPI.Articut()
from datetime import datetime
dt = datetime.now()
import dateparser
from ref_data import PMLIST, AroundLIST, AfterLIST, BeforeLIST
DEBUG_departure_time = True
userDefinedDICT = {"大": ["大人", "成人"], "小": ["小孩", "孩童"]}

def amountSTRConvert(inputSTR):
    resultDICT={}
    resultDICT = articut.parse(inputSTR, level="lv3")
    return resultDICT['number']

def timeSTRConvert(inputSTR):
    resultDICT = {}
    resultDICT = articut.parse(inputSTR, level="lv3")
    return resultDICT

def format_convert(PM, time_STR):
    if bool([p for p in PMLIST if p in PM]):
        time_STR = time_STR + "PM"
        dt1 = dateparser.parse(time_STR)
        time = datetime.strftime(dt1, '%H:%M')
        return time
    else:
        return time_STR

def format_identifier(time_STR):
    if dt.strftime("%p") == "PM":
        time_STR = time_STR + "PM"
        dt1 = dateparser.parse(time_STR)
        time_STR = datetime.strftime(dt1, '%H:%M')
        return time_STR
    else:
        return time_STR

def time_check(hour, minute):
    if hour < 24 and hour > 1:
        if minute < 60 and minute >= 0:
            return True
    else:
        return False

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_departure_time:
        print("[departure_time] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[7]:[46]台北到台南":
        # write your code here
        hour = int(args[0])
        if args[1][0] != "0":
            minute = int(args[1])
        else:
            minute = int(args[1][1])
        if time_check(hour, minute):
            dt = args[0] + ":" + args[1]
            resultDICT ['departure_time'] = format_identifier(dt)
        else:
            resultDICT ['departure_time'] = ""
        pass

    if utterance == "[9]:[30]出發":
        # write your code here
        hour = int(args[0])
        if args[1][0] != "0":
            minute = int(args[1])
        else:
            minute = int(args[1][1])
        if time_check(hour, minute):
            dt = args[0] + ":" + args[1]
            resultDICT ['departure_time'] = format_identifier(dt)
        else:
            resultDICT ['departure_time'] = ""
        pass

    if utterance == "[七點][四十六分]台北往台南":
        # write your code here
        datetime = timeSTRConvert(args[0]+args[1])["time"]
        dt = datetime[0][0]["datetime"][-8:-3] #抓articutAPI中time的時間（後八格）
        resultDICT['departure_time'] = format_identifier(dt)
        pass

    if utterance == "[七點][四十六分]往台南":
        # write your code here
        datetime = timeSTRConvert(args[0]+args[1])["time"]
        dt = datetime[0][0]["datetime"][-8:-3] #抓articutAPI中time的時間（後八格）
        resultDICT['departure_time'] = format_identifier(dt)
        pass

    if utterance == "[三十分]出發":
        # write your code here
        if len(args) == 1:  
            if args[0][-1] in "分一二三四五六七八九十":
                hour = dt.strftime("%H")
                minute = amountSTRConvert(args[0][0:2])[args[0][0:2]]
                resultDICT['departure_time'] = "{}:{}".format(hour, minute)
            else: 
                datetime = timeSTRConvert(args[0][0:2])["time"]
                dt = datetime[0][0]["datetime"][-8:-3]
                resultDICT['departure_time'] = format_identifier(dt)
        pass

    if utterance == "[下午][三點][五十][之後]":
        # write your code here
        datetime = timeSTRConvert(args[1] + args[2])['time']
        time_STR = datetime[0][0]["datetime"][-8:-3]
        resultDICT['departure_time'] = format_convert(args[0], time_STR)
        pass

    if utterance == "[下午][三點][五十分]到台南":
        # write your code here
        datetime = timeSTRConvert(args[1] + args[2])['time']
        time_STR = datetime[0][0]["datetime"][-8:-3]
        resultDICT['departure_time'] = format_convert(args[0], time_STR)
        pass

    if utterance == "[下午][三點之後]":
        # write your code here
        datetime = timeSTRConvert(args[1][0:2])['time']
        time_STR = datetime[0][0]["datetime"][-8:-3]
        resultDICT['departure_time'] = format_convert(args[0], time_STR)
        pass

    if utterance == "[九點][半]出發":
        # write your code here
        datetime = timeSTRConvert(args[0]+args[1])["time"]
        time_STR = datetime[0][0]["datetime"][-8:-3]
        resultDICT['departure_time'] = format_identifier(time_STR)
        pass

    if utterance == "[五十分]到台南":
        # write your code here
        if len(args) == 1:  
            if args[0][-1] in "分一二三四五六七八九十":
                hour = dt.strftime("%H")
                minute = amountSTRConvert(args[0][0:2])[args[0][0:2]]
                resultDICT['departure_time'] = "{}:{}".format(hour, minute)
            else: # 只有時
                datetime = timeSTRConvert(args[0])["time"]
                resultDICT['departure_time'] = datetime[0][0]["datetime"][-8:-3]     
        pass

    if utterance == "[五十分]從台北到台中":
        # write your code here
        if len(args) == 1:  
            if args[0][-1] in "分一二三四五六七八九十":
                hour = dt.strftime("%H")
                minute = amountSTRConvert(args[0][0:2])[args[0][0:2]]
                resultDICT['departure_time'] = "{}:{}".format(hour, minute)
            else: # 只有時
                datetime = timeSTRConvert(args[0][0:2])["time"]
                resultDICT['departure_time'] = datetime[0][0]["datetime"][-8:-3]     
        pass

    if utterance == "[五十分]從台北回台中":
        if len(args) == 1:  
            if args[0][-1] in "分一二三四五六七八九十":
                hour = dt.strftime("%H")
                minute = amountSTRConvert(args[0][0:2])[args[0][0:2]]
                resultDICT['departure_time'] = "{}:{}".format(hour, minute)
            else: # 只有時
                datetime = timeSTRConvert(args[0][0:2])["time"]
                time_STR = datetime[0][0]["datetime"][-8:-3] 
                resultDICT['departure_time'] = format_identifier(time_STR)  # 這裡會有問題：「我要下午九點以後從台北回台南」的args[0]是九點以後，所以無法抓到是上午還是下午
        pass

    if utterance == "[五點][五十分]從台北到台中":
        # write your code here
        datetime = timeSTRConvert(args[0]+args[1])["time"]
        time_STR = datetime[0][0]["datetime"][-8:-3]
        resultDICT['departure_time'] = format_identifier(time_STR)
        pass

    if utterance == "[早上][九點][四十]分[之前]":
        # write your code here
        datetime = timeSTRConvert(args[1] + args[2])['time']
        time_STR = datetime[0][0]["datetime"][-8:-3]
        resultDICT['departure_time'] = format_convert(args[0], time_STR)
        pass

    if utterance == "[早上][五點][半]台北到左營":
        # write your code here
        datetime = timeSTRConvert(args[1] + args[2])['time']
        time_STR = datetime[0][0]["datetime"][-8:-3]
        resultDICT['departure_time'] = format_convert(args[0], time_STR)
        pass

    if utterance == "[早上][八點][三十分]出發":
        # write your code here
        datetime = timeSTRConvert(args[1] + args[2])['time']
        time_STR = datetime[0][0]["datetime"][-8:-3]
        resultDICT['departure_time'] = format_convert(args[0], time_STR)
        pass

    if utterance == "[早上][八點]出發":
        # write your code here
        datetime = timeSTRConvert(args[1][:2])['time']
        time_STR = datetime[0][0]["datetime"][-8:-3]
        resultDICT['departure_time'] = format_convert(args[0], time_STR)
        pass

    if utterance == "[下午][三點]台北到台中":
        datetime = timeSTRConvert(args[1])['time']
        time_STR = datetime[0][0]["datetime"][-8:-3]
        resultDICT['departure_time'] = format_convert(args[0], time_STR)

    return resultDICT