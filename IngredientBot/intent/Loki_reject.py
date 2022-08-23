#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for reject

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
import os

DEBUG_reject = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_fruit":["火龍果"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_reject:
        print("[reject] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT, all_utt):
    debugInfo(inputSTR, utterance)

    resultDICT["reject"] = True

    if utterance == "[可以]說[點][別]的嗎？":
        # write your code here
        pass

    if utterance == "[我]不喜歡[芭樂]":
        resultDICT["ingredient"] = args[1]

    if utterance == "[我]不想吃[芭樂]":
        resultDICT["ingredient"] = args[1]

    if utterance == "不要讓[我]看到[芭樂]！":
        resultDICT["ingredient"] = args[1]

    if utterance == "再來[點][別]的？":
        # write your code here
        pass

    if utterance == "有沒[有][別]的":
        # write your code here
        pass

    if utterance == "還有什麼？":

        if "[杏仁]跟什麼相剋" in all_utt:
            resultDICT.pop("reject")
        elif "[杏仁][可以]跟什麼[一起]吃" in all_utt:
            resultDICT.pop("reject")
        elif "[杏仁]與什麼食物相剋？" in all_utt:
            resultDICT.pop("reject")
        elif "[杏仁]跟什麼不[能][一起]吃" in all_utt:
            resultDICT.pop("reject")
        elif "[杏仁]不[可以]跟什麼[一起]吃" in all_utt:
            resultDICT.pop("reject")
        else:
            pass

    if utterance == "還有嗎？":
        # write your code here
        pass

    if utterance == "[也]不喜歡":
        # write your code here
        pass

    if utterance == "[我]討厭[水蜜桃]":
        resultDICT["ingredient"] = args[1]

    if utterance == "[我]想要[別]的食材":
        # write your code here
        pass

    if utterance == "有甚麼[別]的":
        if "[芭樂]有什麼食用禁忌" in all_utt:
            resultDICT.pop("reject")
        elif "[杏仁]的食用禁忌有哪些" in all_utt:
            resultDICT.pop("reject")
        elif "和[杏仁]相剋的食物有哪些" in all_utt:
            resultDICT.pop("reject")
        elif "[芭樂]有甚麼做法" in all_utt:
            resultDICT.pop("reject")
        elif "[香菇]有甚麼作法" in all_utt:
            resultDICT.pop("reject")
        elif "[現在]有什麼" in all_utt:
            resultDICT.pop("reject")
        elif "[當季][食材]有啥" in all_utt:
            resultDICT.pop("reject")
        elif "有什麼[當季][食材]" in all_utt:
            resultDICT.pop("reject")
        elif "[現在]有甚麼[好吃]的[當季][水果]" in all_utt:
            resultDICT.pop("reject")
        elif "[現在]有甚麼[當季][水果][好吃]" in all_utt:
            resultDICT.pop("reject")
        elif "告訴[我][現在]有什麼[當季][食材]" in all_utt:
            resultDICT.pop("reject")
        elif "[現在]的[當季][食材]有哪些" in all_utt:
            resultDICT.pop("reject")
        elif "[你]知道[七月]的[當令][食材]有哪些嗎" in all_utt:
            resultDICT.pop("reject")
        elif "[我]想知道[三月]的[當令][食材]有哪些" in all_utt:
            resultDICT.pop("reject")
        else:
            pass

    if utterance == "還有[別]的嗎":
        # write your code here
        pass

    if utterance == "不是[很]喜歡ㄟ":
        # write your code here
        pass

    if utterance == "有[別]的嗎":
        # write your code here
        pass

    if utterance == "[我]想要[別]的[食材]":
        # write your code here
        pass

    if utterance == "有沒[有]推薦[別]的[食材]":
        # write your code here
        pass

    if utterance == "有甚麼[別]的[食材]":
        if "有甚麼禁忌" in all_utt:
            resultDICT.pop("reject")
        elif "[芭樂]有什麼禁忌" in all_utt:
            resultDICT.pop("reject")
        elif "[紅棗]有甚麼料理" in all_utt:
            resultDICT.pop("reject")
        elif "[葡萄]有什麼料理方式" in all_utt:
            resultDICT.pop("reject")
        elif "有什麼[水果]" in all_utt:
            resultDICT.pop("reject")
        elif "[現在]有甚麼[海鮮]" in all_utt:
            resultDICT.pop("reject")
        elif "[現在]有什麼[水果][好吃]" in all_utt:
            resultDICT.pop("reject")
        elif "有甚麼[紫甘藍]的作法" in all_utt:
            resultDICT.pop("reject")
        elif "有甚麼料理" in all_utt:
            resultDICT.pop("reject")
        else:
            pass

    return resultDICT