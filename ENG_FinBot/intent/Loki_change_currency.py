#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for change_currency

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import re

DEBUG_change_currency = True
userDefinedDICT = {"Currency":["US Dollar","US Dollars","Korean Won","pound","pounds","New Taiwan dollars","euros"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_change_currency:
        print("[change_currency] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "How [much] is [$100 USD] [in] [Taiwan] ?  ":
        resultDICT["src"]="".join(re.findall(r'[A-Za-z ]+', args[1]))
        resultDICT["tgt"]=args[3]
        resultDICT["amt"]=re.sub(r"[^\d\.]", "", args[1])

    if utterance == "How [much] is [100 USD] [in] [NTD]":
        resultDICT["src"]="".join(re.findall(r'[A-Za-z ]+', args[1]))
        resultDICT["tgt"]=args[3]
        resultDICT["amt"]=re.sub(r"[^\d\.]", "", args[1])

    if utterance == "How [much] is [100 USD] [to] [New Taiwan dollar] ?  ":
        resultDICT["src"]="".join(re.findall(r'[A-Za-z ]+', args[1]))
        resultDICT["tgt"]=args[3]
        resultDICT["amt"]=re.sub(r"[^\d\.]", "", args[1])

    if utterance == "May [I] exchange this [into] [Korean Won]?":
        resultDICT["src"]= None
        resultDICT["tgt"]= args[2]
        resultDICT["amt"]= None

    if utterance == "[I] would like [to] exchange [50 USD] [into] [euros]":
        resultDICT["src"]="".join(re.findall(r'[A-Za-z ]+', args[2]))
        resultDICT["tgt"]=args[4]
        resultDICT["amt"]=re.sub(r"[^\d\.]", "", args[2])

    if utterance == "[I] would like [to] exchange [some] [USD] [into] [pounds] , please.":
        resultDICT["src"]=args[3]
        resultDICT["tgt"]=args[5]
        resultDICT["amt"] = None

    if utterance == "How [much] is [100] [EUR] [into] [TWD]":
        resultDICT["src"]=args[2]
        resultDICT["tgt"]=args[4]
        resultDICT["amt"]=args[1]

    if utterance == "[I] would like [to] exchange [50 USD] [to] [New Taiwan dollars].":
        resultDICT["src"]="".join(re.findall(r'[A-Za-z ]+', args[2]))
        resultDICT["tgt"]=args[4]
        resultDICT["amt"]=re.sub(r"[^\d\.]", "", args[2])

    if utterance == "How [much] is [100 USD] [into] [MXN]":
        resultDICT["src"]="".join(re.findall(r'[A-Za-z ]+', args[1]))
        resultDICT["tgt"]=args[3]
        resultDICT["amt"]=re.sub(r"[^\d\.]", "", args[2])

    if utterance == "[I] want [to] exchange [50 Korean won] [into] [New Taiwan dollars]":
        resultDICT["src"]="".join(re.findall(r'[A-Za-z ]+', args[2]))
        resultDICT["tgt"]=args[4]
        resultDICT["amt"]=re.sub(r"[^\d\.]", "", args[2])

    if utterance == "[I] would like [to] exchange [5000 Canadian dollars] [to] [New Taiwan Dollars]":
        resultDICT["src"]="".join(re.findall(r'[A-Za-z ]+', args[2]))
        resultDICT["tgt"]=args[4]
        resultDICT["amt"]=re.sub(r"[^\d\.]", "", args[2])

    if utterance == "Hi , [I] would like [to] exchange [some] [American] [dollars]":
        resultDICT["src"]= args[3] + " " + args[4]
        resultDICT["tgt"]= None
        resultDICT["amt"]= None
    if utterance == "Hi , [I] would like [to] exchange [some] [pounds]":
        resultDICT["src"]=args[3]
        resultDICT["tgt"]=None
        resultDICT["amt"]=None

    if utterance == "[I] want [to] exchange [5000 korean wons] [in] [Taiwan]":
        resultDICT["src"]="".join(re.findall(r'[A-Za-z ]+', args[2]))
        resultDICT["tgt"]=args[4]
        resultDICT["amt"]=re.sub(r"[^\d\.]", "", args[2])

    if utterance == "What is [50 pesos] [in] [NTD]":
        resultDICT["src"]="".join(re.findall(r'[A-Za-z ]+', args[0]))
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=re.sub(r"[^\d\.]", "", args[0])

    if utterance == "[I] want [to] exchange [52300000.0 USD] [to] [NTD]":
        resultDICT["src"]="".join(re.findall(r'[A-Za-z ]+', args[2]))
        resultDICT["tgt"]=args[4]
        resultDICT["amt"]=re.sub(r"[^\d\.]", "", args[2])

    if utterance == "[I] want [to] exchange [three] [point] [five million USD] [in] [NTD]":
        resultDICT["src"]= args[2] + args[3] + args[4]
        resultDICT["tgt"]=args[4]
        resultDICT["amt"]= args[2] + args[3] + args[4]

    if utterance == "May [I] exchange [300 US dollars] [into] [Korean Won]?":
        resultDICT["src"]= "".join(re.findall(r'[A-Za-z ]+', args[1]))
        resultDICT["tgt"]= args[3]
        resultDICT["amt"]= re.sub(r"[^\d\.]", "", args[1])

    if utterance == "Can [I] exchange [300 US dollars] [into] [New Taiwan dollar]":
        resultDICT["src"]= "".join(re.findall(r'[A-Za-z ]+', args[1]))
        resultDICT["tgt"]= args[3]
        resultDICT["amt"]= re.sub(r"[^\d\.]", "", args[1])

    if utterance == "Can [I] swap [three hundred forty five pesos] [into] [NTD]":
        resultDICT["src"]= "".join(re.findall(r'[A-Za-z ]+', args[1]))
        resultDICT["tgt"]= args[3]
        resultDICT["amt"]= re.sub(r"[^\d\.]", "", args[1])

    if utterance == "[Hello] , [I] would like [to] exchange [50] [pounds]":
        resultDICT["src"]= args[4]
        resultDICT["tgt"]= None
        resultDICT["amt"]= args[3]

    if utterance == "[I] would like [to] exchange [50] [pounds]":
        resultDICT["src"]= args[3]
        resultDICT["tgt"]= None
        resultDICT["amt"]= args[2]

    if utterance == "[I] wanted [to] exchange [523000000 USD] [to] [NTD]":
        resultDICT["src"]="".join(re.findall(r'[A-Za-z ]+', args[2]))
        resultDICT["tgt"]=args[4]
        resultDICT["amt"]=re.sub(r"[^\d\.]", "", args[2])

    if utterance == "[I] want [to] exchange [some] [USD] [into] [NTD] , please":
        resultDICT["src"]="".join(re.findall(r'[A-Za-z ]+', args[3]))
        resultDICT["tgt"]=args[5]
        resultDICT["amt"]= None

    if utterance == "[I] would like [to] exchange [three] [point] [three four canadian dollars] [in] [United States]":
        resultDICT["src"]= args[2] + args[3] + args[4]
        resultDICT["tgt"]=args[6]
        resultDICT["amt"]= args[2] + args[3] + args[4]


    if utterance == "Could [I] exchange [three] [point] [four five pesos] [in] [Taiwan]":
        resultDICT["src"]= args[1] + args[2] + args[3]
        resultDICT["tgt"]=args[5]
        resultDICT["amt"]= args[1] + args[2] + args[3]

    if utterance == "Could [I] exchange [300 pesos] [to] [NTD]":
        resultDICT["src"]= "".join(re.findall(r'[A-Za-z ]+', args[1]))
        resultDICT["tgt"]=args[3]
        resultDICT["amt"]= re.sub(r"[^\d\.]", "", args[1])

    return resultDICT