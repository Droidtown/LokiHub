#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for AC
    
    Input:
        pattern       str,
        utterance     str,
        args          str[],
        resultDICT    dict
    
    Output:
        resultDICT    dict
"""

import os
import re
import json
from requests import post

try:
    infoPath = "{}/account.info".format(os.path.dirname(os.path.abspath(__file__))).replace("/SmartHome/AIoT/intent", "")
    infoDICT = json.load(open(infoPath, "r"))
    USERNAME = infoDICT["username"]
    API_KEY = infoDICT["api_key"]
except:
    # HINT: 在這裡填入您在 https://api.droidtown.co 的帳號、Articut 的 API_Key 以及 Loki 專案的 Loki_Key
    USERNAME = ""
    API_KEY = ""

acDICT = {
    "fan": {
        "modifier_plus": ["強", "大", "高"],
        "modifier_minus": ["弱", "小", "低"]
    },
    "temperature": {
        "modifier_plus": ["熱", "高"],
        "modifier_minus": ["冷", "低", "涼"]
    }
}

powerPat = re.compile("(冷氣(機)?|空調)$")
fanEntityPat = re.compile("(風[量速]?)$")
fanPat = re.compile("((?<!不)[強弱大小高低])$")
fanUnitPat = re.compile("格$")
tempEntityPat = re.compile("(溫度|[室氣]溫|天氣)$")
tempPat = re.compile("((?<!不)[冷熱高低涼])$")
tempUnitPat = re.compile("度$")
unitPat = re.compile("(((小)?時)|[度檔格些點])$")
degreePat = re.compile("[太很好]|非常")

DEBUG_AC = True

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(pattern, utterance, args):
    if DEBUG_AC:
        print("[AC] {} ===> {}\n{}\n".format(utterance, args, pattern))

def getNumberFromLv3(inputSTR):
    """將字串型態的數字轉換成數字型態"""
    try:
        response = post("https://api.droidtown.co/Articut/API/", json={
            "username": USERNAME,
            "api_key": API_KEY,
            "input_str": inputSTR,
            "level": "lv3"
        }).json()
        if response["status"]:
            return response["number"][inputSTR]
    except:
        pass
    return None

def getNumber(inputSTR):
    """將數字的單位移除，並轉換成數字型態"""
    if type(inputSTR) is int:
        return inputSTR
    else:
        numberSTR = unitPat.sub("", inputSTR)
        number = getNumberFromLv3(numberSTR)
        return number

def getTime(inputSTR):
    """取得 x 小時的時間 (number/HR)，並轉成數字型態回傳"""
    number = getNumber(inputSTR)
    if "時" in inputSTR:
        return number
    #elif "分" in inputSTR:
        #return round(number / 60, 2)
    else:
        return 0

def getFanSpeed(inputSTR):
    """從字串轉成風速值"""
    m = [x.group() for x in fanPat.finditer(inputSTR)]
    speed = 0
    if m:
        if m[0] in acDICT["fan"]["modifier_plus"]:
            speed = 1
        elif m[0] in acDICT["fan"]["modifier_minus"]:
            speed = -1
        if degreePat.search(inputSTR):
            speed *= 2
    return speed

def getTemperature(inputSTR):
    """從字串轉成溫度的調整值"""
    m = [x.group() for x in tempPat.finditer(inputSTR)]
    temp = 0
    if m:
        if m[0] in acDICT["temperature"]["modifier_plus"]:
            temp = 1
        elif m[0] in acDICT["temperature"]["modifier_minus"]:
            temp = -1
        if degreePat.search(inputSTR):
            temp *= 2
    return temp

def controlAC(resultDICT, entity, value, num):
    if powerPat.search(entity):
        if value != "":
            if tempPat.search(value):
                temp = getTemperature(value)
                if temp != 0:
                    resultDICT["set_temperature"] = temp * num
            elif fanPat.search(value):
                fan_speed = getFanSpeed(value)
                if fan_speed != 0:
                    resultDICT["set_fan_speed"] = fan_speed * num

    if fanEntityPat.search(entity):
        if value == "":
            resultDICT["fan_speed"] = num
        else:
            if fanPat.search(value):
                fan_speed = getFanSpeed(value)
                if fan_speed != 0:
                    resultDICT["set_fan_speed"] = fan_speed * num
            else:
                resultDICT["set_fan_speed"] = num

    if tempEntityPat.search(entity):
        if value == "":
            resultDICT["temperature"] = num
        else:
            if tempPat.search(value):
                temp = getTemperature(value)
                if temp != 0:
                    resultDICT["set_temperature"] = temp * num
            else:
                resultDICT["set_temperature"] = num

    return resultDICT


def getResult(pattern, utterance, args, resultDICT, input_str):
    debugInfo(pattern, utterance, args)
    if utterance == "升[一度]":
        resultDICT["set_temperature"] = getNumber(args[0])

    if utterance in ["定時[1小時]", "定時[1小時]關", "預約[1小時]", "預約[1小時]關"]:
        resultDICT["time"] = getTime(args[0])

    if utterance in ["定時[1小時][後]開", "預約[1小時][後]開"]:
        if args[-1] in ["後"]:
            pass

    if utterance in ["定時[1小時][後]關", "預約[1小時][後]關"]:
        if args[-1] in ["後"]:
            resultDICT["time"] = getTime(args[0])

    if utterance in ["覺得有[點][冷]", "好像有[一些][冷]", "好像有[一點][冷]"]:
        temp = -getTemperature(args[1])
        if temp != 0:
            resultDICT["set_temperature"] = temp

    if utterance == "調[高][一度]":
        if tempUnitPat.search(args[1]):
            temp = getTemperature(args[0])
            if temp != 0:
                resultDICT["set_temperature"] = temp * getNumber(args[1])
        elif fanUnitPat.search(args[1]):
            fan_speed = getFanSpeed(args[0])
            if fan_speed != 0:
                resultDICT["set_fan_speed"] = fan_speed * getNumber(args[1])
        elif tempPat.search(args[0]):
            temp = getTemperature(args[0])
            if temp != 0:
                resultDICT["set_temperature"] = temp * getNumber(args[1])
        elif fanPat.search(args[0]):
            fan_speed = getFanSpeed(args[0])
            if fan_speed != 0:
                resultDICT["set_fan_speed"] = fan_speed * getNumber(args[1])

    if utterance in ["開[冷氣]", "[冷氣]打開"]:
        if powerPat.search(args[0]):
            resultDICT["ac"] = True

    if utterance in ["關[冷氣]", "[冷氣]關掉"]:
        if powerPat.search(args[0]):
            resultDICT["ac"] = False

    if utterance == "降[一度]":
        if tempUnitPat.search(args[0]):
            resultDICT["set_temperature"] = -getNumber(args[0])
        if fanUnitPat.search(args[0]):
            resultDICT["set_fan"] = -getNumber(args[0])

    if utterance == "[溫度]升[高][一些]":
        resultDICT = controlAC(resultDICT, args[0], args[1], getNumber(args[-1]))

    if utterance == "[溫度]升高[一點]":
        resultDICT = controlAC(resultDICT, args[0], "高", getNumber(args[1]))

    if utterance in ["想要吹[冷氣]", "想要開[冷氣]"]:
        if powerPat.search(args[0]):
            resultDICT["ac"] = True

    if utterance == "想要關[冷氣]":
        if powerPat.search(args[0]):
            resultDICT["ac"] = False

    if utterance == "[冷氣]調[太強]":
        resultDICT = controlAC(resultDICT, args[0], args[1], -1)

    if utterance in ["[冷氣]調[強][一些]", "[冷氣]調[強][一點]"]:
        resultDICT = controlAC(resultDICT, args[0], args[1], getNumber(args[-1]))

    if utterance == "[溫度]調到[20度]":
        resultDICT = controlAC(resultDICT, args[0], "", getNumber(args[1]))

    if utterance == "[溫度]調高[一點]":
        resultDICT = controlAC(resultDICT, args[0], "高", getNumber(args[1]))

    if utterance == "[冷氣]轉[太強]":
        resultDICT = controlAC(resultDICT, args[0], args[1], -1)

    if utterance in ["[冷氣]轉[強][一些]", "[冷氣]轉[強][一點]"]:
        resultDICT = controlAC(resultDICT, args[0], args[1], getNumber(args[-1]))

    if utterance == "[溫度]轉高[一點]":
        resultDICT = controlAC(resultDICT, args[0], "高", getNumber(args[1]))

    if utterance == "[冷氣]開[太強]":
        resultDICT = controlAC(resultDICT, args[0], args[1], -1)

    if utterance in ["[冷氣]開[強][一些]", "[冷氣]開[強][一點]"]:
        resultDICT = controlAC(resultDICT, args[0], args[1], getNumber(args[-1]))

    if utterance in ["[冷氣]關[小][一些]", "[冷氣]關[小][一點]"]:
        resultDICT = controlAC(resultDICT, args[0], args[1], getNumber(args[-1]))

    if utterance in ["[溫度]降低[一些]", "[溫度]降低[一點]"]:
        resultDICT = controlAC(resultDICT, args[0], "低", getNumber(args[1]))

    if utterance == "[溫度][太高]":
        if args[1] != "好像":
            resultDICT = controlAC(resultDICT, args[0], args[1], -1)

    if utterance == "[溫度][20度]":
        resultDICT = controlAC(resultDICT, args[0], "", getNumber(args[1]))

    if utterance == "[溫度][不夠][低]":
        if re.search("不[夠足]$", args[1]):
            resultDICT = controlAC(resultDICT, args[0], args[-1], 1)

    if utterance in ["有[些][冷]", "有[點][冷]"]:
        fan_speed = -getFanSpeed(args[1])
        if fan_speed != 0:
            resultDICT["set_fan_speed"] = fan_speed
        temp = -getTemperature(args[1])
        if temp != 0:
            resultDICT["set_temperature"] = temp

    if utterance == "舒眠[1小時]":
        resultDICT["time"] = getTime(args[0])

    if utterance == "[這裡][好冷]":
        if re.search("[這那]裡$", args[0]):
            fan_speed = -getFanSpeed(args[1])
            if fan_speed != 0:
                resultDICT["set_fan_speed"] = fan_speed
            temp = -getTemperature(args[1])
            if temp != 0:
                resultDICT["set_temperature"] = temp

    if utterance == "[很熱]":
        #fan_speed = -getFanSpeed(args[0])
        #if fan_speed != 0:
            #resultDICT["set_fan_speed"] = fan_speed
        temp = -getTemperature(args[0])
        if temp != 0:
            resultDICT["set_temperature"] = temp

    if utterance == "調[高][一檔]":
        fan_speed = getFanSpeed(args[0])
        if fan_speed != 0:
            resultDICT["set_fan_speed"] = fan_speed * getNumber(args[1])
        temp = getTemperature(args[0])
        if temp != 0:
            resultDICT["set_temperature"] = temp * getNumber(args[1])

    return resultDICT