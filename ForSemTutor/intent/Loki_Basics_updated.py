#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Basics

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Basics = True
userDefinedDICT = {"lambda": [""], "動詞": ["verb"], "句子": ["S", "sentence"], "名詞": ["noun"], "短語": [""], "形容詞": ["adj", "adjective"], "全稱量詞": ["for all", "universal quantifier"], "及物動詞": ["transitive verb", "及物"], "存在量詞": ["there is", "existential quantifier"], "專有名詞": ["proper noun", "專有", "專名"], "普通名詞": ["countable noun", "可數", "普通"], "不及物動詞": ["intransitive verb", "不及物"], "屬性形容詞": ["attribute adjective", "屬性"], "謂語形容詞": ["predicate adjective", "謂語"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Basics:
        print("[Basics] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[全稱量詞]的意思是什麼":
        resultDICT['term'] = args[0]
        resultDICT['action'] = 'DefineTerm'

    if utterance == "[全稱量詞]的語意是什麼":
        resultDICT['term'] = args[0]
        resultDICT['action'] = 'DefineTerm'

    if utterance == "[名詞]是做什麼的":
        resultDICT['term'] = args[0]
        resultDICT['action'] = 'DefineTerm'

    if utterance == "[名詞]是幹什麼的":
        resultDICT['term'] = args[0]
        resultDICT['action'] = 'DefineTerm'

    if utterance == "什麼是[全稱量詞]的意思":
        resultDICT['term'] = args[0]
        resultDICT['action'] = 'DefineTerm'

    if utterance == "什麼是[全稱量詞]的語意":
        resultDICT['term'] = args[0]
        resultDICT['action'] = 'DefineTerm'

    if utterance == "[不及物]":
        # write your code here
        pass

    return resultDICT