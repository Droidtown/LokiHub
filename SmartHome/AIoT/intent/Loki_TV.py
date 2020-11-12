#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for TV
    
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

tvDICT = {
    "channel": {
        "filter": {
            "assign": ["第", ""],
            "plus": ["下", "後"],
            "minus": ["上", "前"],
            "foot": ["台", "臺"]
        }
    },
    "volume": {
        "modifier_plus": ["大聲", "大", "不夠", "不足"],
        "modifier_minus": ["小聲", "小", "吵"]
    }
}

powerPat = re.compile("(電視(機)?|[Tt][Vv])$")
channelEntityPat = re.compile("((.*)?(卡通|[劇台臺]|節目|頻道))$")
channelPat = re.compile("[第下後上前台臺]")
volumeEntityPat = re.compile("(聲音|音量|喇叭)$")
volumePat = re.compile("((?<!不)([大小](聲)?)|吵)$")
unitPat = re.compile("[些點格]$")
degreePat = re.compile("[太很好]|非常")

DEBUG_TV = True

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(pattern, utterance, args):
    if DEBUG_TV:
        print("[TV] {} ===> {}\n{}\n".format(utterance, args, pattern))

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

def getVolume(inputSTR):
    """從字串轉成音量值"""
    m = [x.group() for x in volumePat.finditer(inputSTR)]
    volume = 0
    if m:
        if m[0] in tvDICT["volume"]["modifier_plus"]:
            volume = 2
        elif m[0] in tvDICT["volume"]["modifier_minus"]:
            volume = -2
        if degreePat.search(inputSTR):
            volume *= 2
    return volume

def getChannel(inputSTR):
    """從字串轉成頻道"""
    if type(inputSTR) is int:
        return inputSTR
    else:
        numberSTR = channelPat.sub("", inputSTR)
        number = getNumberFromLv3(numberSTR)
        determiner = inputSTR[:inputSTR.find(numberSTR)]
        channel = 0
        if number:
            if determiner in tvDICT["channel"]["filter"]["assign"]:
                channel = number
            elif determiner in tvDICT["channel"]["filter"]["plus"]:
                channel = number
            elif determiner in tvDICT["channel"]["filter"]["minus"]:
                channel = -number
        return channel

def controlTV(resultDICT, entity, value, num):
    if channelEntityPat.search(entity):
        channel = getChannel(num)
        if channel != 0:
            resultDICT["channel"] = channel

    if powerPat.search(entity) or volumeEntityPat.search(entity):
        if value == "":
            resultDICT["volume"] = num
        else:
            volume = getVolume(value)
            if volume != 0:
                resultDICT["set_volume"] = volume * num

    return resultDICT

def getResult(pattern, utterance, args, resultDICT, input_str):
    debugInfo(pattern, utterance, args)
    if utterance == "回[上一台]":
        channel = getChannel(args[0])
        if channel != 0:
            resultDICT["set_channel"] = channel

    if utterance in ["調[大聲]", "轉[大聲]", "開[大聲]", "關[小聲]"]:
        volume = getVolume(args[0])
        if volume != 0:
            resultDICT["set_channel"] = volume

    if utterance in ["調[大聲][一些]", "調[大聲][一點]",
                     "轉[大聲][一些]", "轉[大聲][一點]",
                     "開[大聲][一些]", "開[大聲][一點]",
                     "關[小聲][一點]", "關[小聲][一些]"]:
        volume = getVolume(args[0])
        if volume != 0:
            num = getNumber(args[1])
            resultDICT["set_channel"] = volume * num

    if utterance in ["轉到[第50台]", "轉到[50台]"]:
        channel = getChannel(args[0])
        if channel != 0:
            resultDICT["channel"] = channel

    if utterance in ["開[聲音]", "把[電視]打開", "[電視]打開"]:
        if powerPat.search(args[0]) or channelEntityPat.search(args[0]):
            resultDICT["tv"] = True
        if volumeEntityPat.search(args[0]):
            resultDICT["volume"] = 10

    if utterance in ["關[聲音]", "把[電視]關掉", "[電視]關掉"]:
        if powerPat.search(args[0]) or channelEntityPat.search(args[0]):
            resultDICT["tv"] = False
        if volumeEntityPat.search(args[0]):
            resultDICT["volume"] = 0

    if utterance in ["有[些]吵", "有[點]吵"]:
        resultDICT["set_volume"] = -2

    if utterance == "[第50台]":
        channel = getChannel(args[0])
        if channel != 0:
            resultDICT["channel"] = channel

    if utterance == "想要看[電視]":
        if powerPat.search(args[0]) or channelEntityPat.search(args[0]):
            resultDICT["tv"] = True

    if utterance == "聽不[清楚]":
        if re.search("(清[楚晰])$", args[0]):
            resultDICT["set_volume"] = 2

    if utterance in ["聽不見", "聽不到"]:
        resultDICT["set_volume"] = 2

    if utterance == "[音量]調[30]":
        resultDICT = controlTV(resultDICT, args[0], "", getNumber(args[1]))

    if utterance in ["[電視]調[大聲]", "[電視]轉[大聲]", "[電視]開[大聲]",
                     "[音量]調[小][一些]", "[音量]調[小][一點]", "[電視]關[小聲]"]:
        resultDICT = controlTV(resultDICT, args[0], args[1], 1)

    if utterance == "[電視][太大聲]":
        resultDICT = controlTV(resultDICT, args[0], args[1], -1)

    if utterance == "[頻道][50]":
        resultDICT = controlTV(resultDICT, args[0], "", getNumber(args[1]))

    if utterance == "[電視]好吵":
        resultDICT = controlTV(resultDICT, args[0], "好吵", 1)

    if utterance in ["[音量][小聲][一些]", "[音量][小聲][一點]"]:
        resultDICT = controlTV(resultDICT, args[0], args[1], getNumber(args[-1]))

    if utterance == "[聲音][不夠][大聲]":
        if re.search("不[足夠]$", args[1]):
            resultDICT = controlTV(resultDICT, args[0], args[-1], 1)
        if re.search("[忽突]然$", args[1]):
            resultDICT = controlTV(resultDICT, args[0], args[-1], -1)

    if utterance == "[上一台]":
        channel = getChannel(args[0])
        if channel != 0:
            resultDICT["set_channel"] = channel

    if utterance in ["不想看[第50台]", "不想看這一台"]:
        resultDICT["set_channel"] = 1

    if utterance == "不要開[電視]":
        if powerPat.search(args[0]) or channelEntityPat.search(args[0]):
            resultDICT["tv"] = False
        if volumeEntityPat.search(args[0]):
            resultDICT["volume"] = 0

    if utterance == "不要關[電視]":
        if powerPat.search(args[0]) or channelEntityPat.search(args[0]):
            resultDICT["tv"] = True
        if volumeEntityPat.search(args[0]):
            resultDICT["volume"] = 10

    if utterance == "不要[太大聲]":
        volume = getVolume(args[0])
        if volume != 0:
            resultDICT["set_volume"] = -volume

    if utterance == "不要[靜音]":
        if args[0] in ["靜音"]:
            resultDICT["volume"] = 10
        else:
            volume = getVolume(args[0])
            if volume != 0:
                resultDICT["set_volume"] = -volume

    if utterance == "[靜音]":
        if args[0] in ["靜音"]:
            resultDICT["volume"] = 0
        else:
            volume = getVolume(args[0])
            if volume != 0:
                resultDICT["set_volume"] = volume

    if utterance == "[第50][頻道]":
        resultDICT = controlTV(resultDICT, args[1], "", args[0])

    if utterance == "轉台":
        resultDICT["set_channel"] = 1

    return resultDICT