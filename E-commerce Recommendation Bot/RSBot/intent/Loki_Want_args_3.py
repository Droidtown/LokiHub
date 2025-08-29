#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Want_args_3

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict,
        pattern       str

    Output:
        resultDICT    dict
"""

from importlib.util import module_from_spec
from importlib.util import spec_from_file_location
from random import sample
import json
import os
from Get_reply import reply_maker

INTENT_NAME = "Want_args_3"
CWD_PATH = os.path.dirname(os.path.abspath(__file__))

def import_from_path(module_name, file_path):
    spec = spec_from_file_location(module_name, file_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

MODULE_DICT = {
    "Account": import_from_path("RSBot_lib_Account", os.path.join(os.path.dirname(CWD_PATH), "lib/Account.py")),
    "LLM": import_from_path("RSBot_lib_LLM", os.path.join(os.path.dirname(CWD_PATH), "lib/LLM.py"))
}
"""
Account Variables
[Variable] BASE_PATH         => path of root
[Variable] LIB_PATH          => path of lib folder
[Variable] INTENT_PATH       => path of intent folder
[Variable] REPLY_PATH        => path of reply folder
[Variable] ACCOUNT_DICT      => account.info
[Variable] ARTICUT           => ArticutAPI (Usage: ARTICUT.parse()。 #ArticutAPI Required.)
[Variable] USER_DEFINED_FILE => path of UserDefined
[Variable] USER_DEFINED_DICT => UserDefined data
"""
REPLY_PATH = MODULE_DICT["Account"].REPLY_PATH
ACCOUNT_DICT = MODULE_DICT["Account"].ACCOUNT_DICT
ARTICUT = MODULE_DICT["Account"].ARTICUT
USER_DEFINED_FILE = MODULE_DICT["Account"].USER_DEFINED_FILE
USER_DEFINED_DICT = MODULE_DICT["Account"].USER_DEFINED_DICT
getLLM = MODULE_DICT["LLM"].getLLM

# userDefinedDICT (Deprecated)
# Replace with USER_DEFINED_DICT of Account variable.
#userDefinedDICT = {}
#try:
#    userDefinedDICT = json.load(open(os.path.join(CWD_PATH, "USER_DEFINED.json"), encoding="utf-8"))
#except:
#    pass

replyDICT = {}
replyPathSTR = os.path.join(REPLY_PATH, "reply_{}.json".format(INTENT_NAME))
if os.path.exists(replyPathSTR):
    try:
        replyDICT = json.load(open(replyPathSTR, encoding="utf-8"))
    except Exception as e:
        print("[ERROR] reply_{}.json => {}".format(INTENT_NAME, str(e)))
CHATBOT = True if replyDICT else False

# Debug message
def debugInfo(inputSTR, utterance):
    if ACCOUNT_DICT["debug"]:
        print("[{}] {} ===> {}".format(INTENT_NAME, inputSTR, utterance))

def getReply(utterance, args):
    replySTR = ""
    try:
        replySTR = sample(replyDICT[utterance], 1)[0]
        if args:
            replySTR = replySTR.format(*args)
    except:
        pass

    return replySTR

def getReply2(args, refDICT):
    for arg in args:
        refDICT["items"].append(arg)
    replySTR = reply_maker(refDICT)
    return replySTR

getResponse = getReply
def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern="", toolkitDICT={}):
    debugInfo(inputSTR, utterance)
    if utterance == "I would buy a hp touch screen laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would buy a two in one laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would choose a HP envy line up laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would choose a mid range laptop, probebly an Acer.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would choose an Apple MacBook Air.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would hope to buy another, more recently Macbook Pro model.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would like a lightweight touchscreen laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would like to buy a light weight laptop, since I travel often.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would look at buying a mac or a dell laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would pick a macbook pro laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would prefer a Hewlett Packard laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would prefer a laptop In the color space grey.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would want a thin, lightweight laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would want it to run a Windows operating system.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I'd also like it do have a light up keyboard.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I'd like to get a Microsoft Surface laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I'd prefer an SSD and at least 8Gb of RAM":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I’d buy the Apple Mac laptop as i usually always purchase Apple products":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    return resultDICT


if __name__ == "__main__":
    from pprint import pprint

    resultDICT = getResult("I would buy a two in one laptop.", "I would buy a two in one laptop.", [], {}, {})
    pprint(resultDICT)