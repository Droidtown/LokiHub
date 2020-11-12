#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Question
    
    Input:
        pattern       str,
        utterance     str,
        args          str[],
        resultDICT    dict
    
    Output:
        resultDICT    dict
"""

import re

entityDICT = {
    "action": ["房間", "客房", "書房", "臥房", "臥室", "客廳", "廁所", "餐廳", "廚房", "陽台"],
    "ac": ["冷氣", "冷氣機", "空調"],
    "tv": ["電視", "電視機", "TV"]
}

actionPat = re.compile("(發光二極體|LED|光線|亮度|電燈|燈光|{房間|客房|書房|臥房|臥室|客廳|廁所|餐廳|廚房|陽台}|({房間|客房|書房|臥房|臥室|客廳|廁所|餐廳|廚房|陽台})?燈)$")
tvPat = re.compile("((.*)?(卡通|[劇台臺]|節目|頻道)|電視(機)?|[Tt][Vv])$")
acPat = re.compile("(冷氣(機)?|空調)$")


DEBUG_Question = True

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(pattern, utterance, args):
    if DEBUG_Question:
        print("[Question] {} ===> {}\n{}".format(utterance, args, pattern))

def getResult(pattern, utterance, args, resultDICT, input_str):
    debugInfo(pattern, utterance, args)

    if utterance in ["可以看[卡通]嗎", "有什麼[卡通]可以看嗎", "有什麼[卡通]嗎", "有[卡通]可以看嗎", "有[卡通]嗎"]:
        if tvPat.search(args[0]):
            resultDICT["question_tv"] = True

    if utterance in ["忘記開[冷氣]", "好像忘記開[冷氣]", "忘記開[燈]", "好像忘記開[燈]"]:
        if actionPat.search(args[0]):
            resultDICT["question_action"] = "++"
        if acPat.search(args[0]):
            resultDICT["question_ac"] = True
        if tvPat.search(args[0]):
            resultDICT["question_tv"] = True

    if utterance in ["好像沒開[冷氣]", "[冷氣]好像沒開", "沒開[冷氣]"]:
        if "沒開" in input_str:
            if actionPat.search(args[0]):
                resultDICT["question_action"] = "++"
            if acPat.search(args[0]):
                resultDICT["question_ac"] = True
            if tvPat.search(args[0]):
                resultDICT["question_tv"] = True

    if utterance in ["忘記關[冷氣]", "好像忘記關[冷氣]", "忘記關[燈]", "好像忘記關[燈]"]:
        if actionPat.search(args[0]):
            resultDICT["question_action"] = "--"
        if acPat.search(args[0]):
            resultDICT["question_ac"] = False
        if tvPat.search(args[0]):
            resultDICT["question_tv"] = False

    if utterance in ["好像沒關[冷氣]", "[冷氣]好像沒關", "沒關[冷氣]"]:
        if "沒關" in input_str:
            if actionPat.search(args[0]):
                resultDICT["question_action"] = "--"
            if acPat.search(args[0]):
                resultDICT["question_ac"] = False
            if tvPat.search(args[0]):
                resultDICT["question_tv"] = False

    if utterance in ["[燈]忘記開", "[燈]好像忘記開"]:
        if actionPat.search(args[0]):
            resultDICT["question_action"] = "++"
        if acPat.search(args[0]):
            resultDICT["question_ac"] = True
        if tvPat.search(args[0]):
            resultDICT["question_tv"] = True

    if utterance in ["[燈]忘記關", "[燈]好像忘記關"]:
        if actionPat.search(args[0]):
            resultDICT["question_action"] = "--"
        if acPat.search(args[0]):
            resultDICT["question_ac"] = False
        if tvPat.search(args[0]):
            resultDICT["question_tv"] = False

    if utterance == "想看[卡通]":
        if tvPat.search(args[0]):
            resultDICT["question_tv"] = True

    if utterance == "[燈]忘記開":
        if actionPat.search(args[0]):
            resultDICT["question_action"] = "++"
        if acPat.search(args[0]):
            resultDICT["question_ac"] = True
        if tvPat.search(args[0]):
            resultDICT["question_tv"] = True

    return resultDICT