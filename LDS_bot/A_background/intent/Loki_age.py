#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for age

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
from ArticutAPI import Articut
import json
import os

account_info = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "account.info"), encoding="utf-8"))
articut = Articut(account_info["username"], account_info["api_key"])
DEBUG_age = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
# if CHATBOT_MODE:
#     try:
#         responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_age.json"), encoding="utf-8"))
#     except Exception as e:
#         print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_age:
        print("[age] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[1]歲":
        if CHATBOT_MODE:
            resultDICT["response"] = "{}歲啊。\n那麼孩子出生時是否足月呢？".format(args[0])
            resultDICT["age"] = articut.parse(args[0], level="lv3")["number"][args[0]]*12
        else:
            # write your code here
            pass

    if utterance == "[1]歲[2]個月":
        if CHATBOT_MODE:
            resultDICT["response"] = "{}歲{}個月啊。\n那麼孩子出生時是否足月呢？".format(args[0], args[1])
            resultDICT["age"] = articut.parse(args[0], level="lv3")["number"][args[0]]*12 + articut.parse(args[1], level="lv3")["number"][args[1]]
        else:
            pass

    if utterance == "[1]足歲":
        if CHATBOT_MODE:
            resultDICT["response"] = "{}歲啊。\n那麼孩子出生時是否足月呢？".format(args[0])
            resultDICT["age"] = articut.parse(args[0], level="lv3")["number"][args[0]]*12
        else:
            # write your code here
            pass

    if utterance == "[1]足歲[2]個月":
        if CHATBOT_MODE:
            resultDICT["response"] = "{}歲{}個月啊。\n那麼孩子出生時是否足月呢？".format(args[0], args[1])
            resultDICT["age"] = articut.parse(args[0], level="lv3")["number"][args[0]]*12 + articut.parse(args[1], level="lv3")["number"][args[1]]
        else:
            # write your code here
            pass

    if utterance == "虛歲[1]歲":
        if CHATBOT_MODE:
            num = articut.parse(args[0], level="lv3")["number"][args[0]]
            if num == 1:
                resultDICT["response"] = "那孩子現在幾個月大了呢？"
            else:
                resultDICT["response"] = "虛歲{}歲啊。\n那麼孩子出生時是否足月呢？".format(args[0])
                resultDICT["age"] = (num-1)*12
        else:
            # write your code here
            pass

    if utterance == "[2]個月":
        if CHATBOT_MODE:
            resultDICT["response"] = "{}個月啊。\n那麼孩子出生時是否足月呢？".format(args[0])
            resultDICT["age"] = articut.parse(args[0], level="lv3")["number"][args[0]]
        else:
            # write your code here
            pass

    if utterance == "據推測，年齡約為1歲。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT