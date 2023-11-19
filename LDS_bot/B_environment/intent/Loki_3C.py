#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for 3C

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os
from ArticutAPI import Articut
import re

account_info = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "account.info"), encoding="utf-8"))
articut = Articut(account_info["username"], account_info["api_key"])
DEBUG_age = True
CHATBOT_MODE = True

DEBUG_3C = True
CHATBOT_MODE = True

userDefinedDICT = {}
# try:
#     userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
# except Exception as e:
#     print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
# if CHATBOT_MODE:
#     try:
#         responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_3C.json"), encoding="utf-8"))
#     except Exception as e:
#         print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_3C:
        print("[3C] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "一天大概30分鐘":
        if CHATBOT_MODE:
            result = articut.parse(inputSTR, level="lv3")
            if len(result["time"][0]) != 0 and "分鐘" in inputSTR:
                num = result["time"][0][0]["time_span"]["minute"][0] // 60
            elif len(result["time"][0]) != 0 and "小時" in inputSTR:
                num = result["time"][0][0]["time_span"]["hour"][0]
            if num >= 2:
                resultDICT["3c"] = True
            else:
                resultDICT["3c"] = False
            resultDICT["response"] = "好的。關於孩子的一些基本資訊都蒐集完畢，接著要針對孩子平常的行為表現作更深入的了解囉。"

        else:
            # write your code here
            pass

    if utterance == "每天大概使用平板電腦30分鐘。":
        if CHATBOT_MODE:
            result = articut.parse(inputSTR, level="lv3")
            if len(result["time"][0]) != 0 and "分鐘" in inputSTR:
                num = result["time"][0][0]["time_span"]["minute"][0] // 60
            elif len(result["time"][0]) != 0 and "小時" in inputSTR:
                num = result["time"][0][0]["time_span"]["hour"][0]
            if num >= 2:
                resultDICT["3c"] = True
            else:
                resultDICT["3c"] = False
            resultDICT["response"] = "好的。關於孩子的一些基本資訊都蒐集完畢，接著要針對孩子平常的行為表現作更深入的了解囉。"
        else:
            # write your code here
            pass

    if utterance == "每天用平板大概30分鐘":
        if CHATBOT_MODE:
            result = articut.parse(inputSTR, level="lv3")
            if len(result["time"][0]) != 0 and "分鐘" in inputSTR:
                num = result["time"][0][0]["time_span"]["minute"][0] // 60
            elif len(result["time"][0]) != 0 and "小時" in inputSTR:
                num = result["time"][0][0]["time_span"]["hour"][0]
            if num >= 2:
                resultDICT["3c"] = True
            else:
                resultDICT["3c"] = False
            resultDICT["response"] = "好的。關於孩子的一些基本資訊都蒐集完畢，接著要針對孩子平常的行為表現作更深入的了解囉。"
        else:
            # write your code here
            pass

    return resultDICT