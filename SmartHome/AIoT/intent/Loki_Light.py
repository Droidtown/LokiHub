#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Light
    
    Input:
        pattern       str,
        utterance     str,
        args          str[],
        resultDICT    dict
    
    Output:
        resultDICT    dict
"""

import re

lightDICT = {
    "brighten": ["亮", "高"],
    "darken":["暗", "黑", "低"]
}

entityPat = re.compile("(發光二極體|LED|光線|亮度|電燈|燈光|{房間|客房|書房|臥房|臥室|客廳|廁所|餐廳|廚房|陽台}|({房間|客房|書房|臥房|臥室|客廳|廁所|餐廳|廚房|陽台})?燈)$")

DEBUG_Light = True

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(pattern, utterance, args):
    if DEBUG_Light:
        print("[Light] {} ===> {}\n{}\n".format(utterance, args, pattern))

def optionInterpreter(inputSTR):
    '''
    詮釋究竟要如何調整燈光：
    + : 調亮一度
    ++: 全亮
    - : 調暗一度
    --: 全暗
    '''
    if set(inputSTR).intersection(lightDICT["brighten"]):
        if "全" in inputSTR:
            result = "++"
        else:
            result = "+"
    elif set(inputSTR).intersection(lightDICT["darken"]):
        if "全" in inputSTR:
            result = "--"
        else:
            result = "-"
    else:
        result = ""
    return result

def getResult(pattern, utterance, args, resultDICT, input_str):
    debugInfo(pattern, utterance, args)
    if utterance in ["調[亮][一些]", "調[亮][一點]"]:
        action = optionInterpreter(args[0])
        if action:
            resultDICT["action"] = action

    if utterance == "開[電燈]":
        if entityPat.search(args[0]):
            resultDICT["action"] = "++"

    if utterance == "開燈":
        resultDICT["action"] = "++"

    if utterance == "關[電燈]":
        if entityPat.search(args[0]):
            resultDICT["action"] = "--"

    if utterance == "關燈":
        resultDICT["action"] = "--"

    if utterance in ["有[些][亮]", "有[點][亮]"]:
        if args[1] in lightDICT["brighten"]:
            resultDICT["action"] = "-"
        if args[1] in lightDICT["darken"]:
            resultDICT["action"] = "+"

    if utterance in ["把[燈]調[亮][一些]", "把[燈]調[亮][一點]"]:
        if entityPat.search(args[0]):
            action = optionInterpreter(args[1])
            if action:
                resultDICT["action"] = action

    if utterance == "[太亮]了":
        if "非常" in args[0]:
            if "亮" in args[0]:
                resultDICT["action"] = "--"
            if "暗" in args[0]:
                resultDICT["action"] = "++"
        else:
            if "亮" in args[0]:
                resultDICT["action"] = "-"
            if "暗" in args[0]:
                resultDICT["action"] = "+"

    if utterance == "想要看[書]":
        if re.search("((.*)?(書([本籍])?|雜誌|小說|繪本))$", args[0]):
            resultDICT["action"] = "++"

    if utterance == "[燈]打開":
        if entityPat.search(args[0]):
            resultDICT["action"] = "++"

    if utterance in ["看不到", "看不見"]:
        resultDICT["action"] = "+"

    if utterance in ["看不[清楚]"]:
        if args[0] in ["清楚", "清晰"]:
            resultDICT["action"] = "+"

    if utterance == "看[不太]到":
        if args[0] in ["不太"]:
            resultDICT["action"] = "+"

    if utterance in ["[亮度]調[高][一些]", "[燈光]調[暗][一點]", "[燈]開[亮][一些]", "[燈]開[亮][一點]"]:
        if entityPat.search(args[0]):
            action = optionInterpreter(args[1])
            if action:
                resultDICT["action"] = action

    if utterance == "[亮度]調高[一點]":
        if entityPat.search(args[0]):
            resultDICT["action"] = "+"

    if utterance == "[燈]關掉":
        if entityPat.search(args[0]):
            resultDICT["action"] = "--"

    if utterance == "[燈]沒開":
        if entityPat.search(args[0]):
            if "沒開" in input_str:
                resultDICT["action"] = "++"
            elif [True for x in ["別開", "不開", "不要開"] if x in input_str]:
                resultDICT["action"] = "--"

    if utterance == "[燈]沒關":
        if entityPat.search(args[0]):
            if "沒關" in input_str:
                resultDICT["action"] = "--"
            elif [True for x in ["別關", "不關", "不要關"] if x in input_str]:
                resultDICT["action"] = "++"

    if utterance == "[亮度][不夠]":
        if entityPat.search(args[0]):
            if args[1] in ["不足", "不夠"]:
                resultDICT["action"] = "+"

    if utterance == "[燈光][不夠][亮]":
        if entityPat.search(args[0]):
            if args[1] in ["不夠"]:
                action = optionInterpreter(args[2])
                if action:
                    resultDICT["action"] = action

    if utterance == "[燈][全]開":
        if entityPat.search(args[0]):
            resultDICT["action"] = "++"

    if utterance == "[燈][全]關":
        if entityPat.search(args[0]):
            resultDICT["action"] = "--"

    if utterance == "伸手不見五指":
        resultDICT["action"] = "++"

    if utterance == "好刺眼":
        resultDICT["action"] = "-"

    if utterance == "不要開[電燈]":
        if entityPat.search(args[0]):
            if "沒開" in input_str:
                resultDICT["action"] = "++"
            else:
                resultDICT["action"] = "--"

    if utterance == "不要開燈":
        if "沒開" in input_str:
            resultDICT["action"] = "++"
        else:
            resultDICT["action"] = "--"

    if utterance == "不要關[電燈]":
        if entityPat.search(args[0]):
            if "沒關" in input_str:
                resultDICT["action"] = "--"
            else:
                resultDICT["action"] = "++"

    if utterance == "不要關燈":
        if "沒關" in input_str:
            resultDICT["action"] = "--"
        else:
            resultDICT["action"] = "++"

    if utterance == "[太]刺眼":
        resultDICT["action"] = "-"

    if utterance in ["[再亮][一些]", "[再亮][一點]"]:
        action = optionInterpreter(args[0])
        if action:
            resultDICT["action"] = action

    if utterance == "[全][亮]":
        action = optionInterpreter(args[0]+args[1])
        if action:
            resultDICT["action"] = action

    if utterance == "[不夠][亮]":
        if re.search("不[足夠]$", args[0]):
            action = optionInterpreter(args[1])
            if action:
                resultDICT["action"] = action

    return resultDICT