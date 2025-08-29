#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Want_args_2

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

INTENT_NAME = "Want_args_2"
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
    if utterance == "I would be looking at something, small, compact and lightweight.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would buy a mid price laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would choose a Macbook Pro":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would choose a dell or an HP.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would choose a laptop made by Apple as like their design.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would chose a Razer Blade right now.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would ideally like an Apple laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would like at least 8GB of memory.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would like mircosoft office.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would like my knew lap top to be an Apple one.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would like to buy a MAC book pro this time round.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would like to choose an apple laptop as a replacement.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would like to get a MacBook Pro.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would look at memory and speed and size of screen":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would most likely buy and HP laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would probably buy a Dell or HP, although if I had no budget I would buy a Mac":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would probably buy an apple laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would probably choose a macbook as a replacement laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would probably choose an Apple iMac as a replacement.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would probably pick an Apple laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would purchase a Macbook Pro.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would want a Dell laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would want a Mac book pro.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would want a Mac laptop as my replacement.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would want an SSD of at least 500 GB.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would want to buy a Mac book.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I would want to buy an apple laptop as a replacement.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I'd also prefer windows OS.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I'd get an msi laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I'd like a better and more HD screen.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I'd like to get HP or Acer, as I'm kinda loyal to these brands.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I'd probably get an ASUS or Lenovo.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I'll probably move to a hybrid laptop as a replacement.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    if utterance == "I’d like to buy an Apple laptop.":
        for arg in args:
            resultDICT["items"].append(arg)
        resultDICT["response"] = getReply2(args, refDICT)
        resultDICT["source"] = "reply"

    return resultDICT


if __name__ == "__main__":
    from pprint import pprint

    resultDICT = getResult("I'd get an msi laptop.", "I'd get an msi laptop.", [], {}, {})
    pprint(resultDICT)