#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for recheck

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
import re

DEBUG_recheck = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
# if CHATBOT_MODE:
#     try:
#         responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_recheck.json"), encoding="utf-8"))
#     except Exception as e:
#         print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_recheck:
        print("[recheck] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

disease = r"聽損|視障|視覺障礙|自閉|自閉症|智能不足|精神疾病"
relative = r"|".join(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "third_degree_relative.txt"), encoding="utf-8").read().split("\n"))

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "唇顎裂":
        if CHATBOT_MODE:
            if re.search(disease, inputSTR):
                resultDICT["genetic_disease"] = True
            else:
                resultDICT["genetic_disease"] = False
        else:
            # write your code here
            pass

    if utterance == "爸爸":
        if CHATBOT_MODE:
            if re.search(relative, inputSTR):
                resultDICT["genetic_disease"] = True
            else:
                resultDICT["genetic_disease"] = False
        else:
            # write your code here
            pass

    return resultDICT