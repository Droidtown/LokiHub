#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for money

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

DEBUG_money = True
CHATBOT_MODE = True

argDICT = {
    "me": ("我"),
    "myself": ("我","自己"),
    "stingy": ("小氣","吝嗇","摳","ㄎㄡ"),
    "3rd_person": ("他","她","對方"),
    "equal": ("相當","一樣","差不多"),
    "child": ("小孩","孩子","女兒","兒子")
}

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_money.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_money:
        print("[money] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一個月][只有][2萬多元]的[收入]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[他][真]的[都]沒在存錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[他]太守財奴了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[另一半][很]愛計較":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[另一半]手頭[緊]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[另一半]沒錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[另一半]經濟[拮据]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][一直]跟[我]借錢":
        if CHATBOT_MODE:
            if args[2] in argDICT["myself"]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方][只]喜歡[我]的[錢]":
        if CHATBOT_MODE:
            if args[2] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][只]在乎[我]的[錢]":
        if CHATBOT_MODE:
            if args[2] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][只]對[我][錢包][裡]的[東西][感]興趣":
        if CHATBOT_MODE:
            if args[2] in argDICT["me"]:        
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][只]對[我]的[財產][感]興趣":
        if CHATBOT_MODE:
            if args[2] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][只]對[我]的[錢][感]到心動":
        if CHATBOT_MODE:
            if args[2] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][只]對[我]的[錢]有興趣":
        if CHATBOT_MODE:
            if args[2] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][只]愛[我]的[錢]":
        if CHATBOT_MODE:
            if args[2] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][只]看中[我]的[財力]":
        if CHATBOT_MODE:
            if args[2] in argDICT["myself"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][只]追求[我]的[金錢]":
        if CHATBOT_MODE:
            if args[2] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][會]偷[家][裡]的錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方][都]不帶錢包":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方][錢]賺得[很少]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]一事無成":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]一無所有":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]不存錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]不幫忙付錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]不願意aa":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]不願意跟[我]aa":
        if CHATBOT_MODE:
            if args[1] in argDICT["myself"]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]什麼[都]要[我]付錢":
        if CHATBOT_MODE:
            if args[2] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]借錢不還":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]出門不帶錢包":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]口袋[空空]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]堅持AA":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]堅持生":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]太[小氣]":
        if CHATBOT_MODE:
            if args[1] in argDICT["stingy"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]對[金錢][太]計較":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]對花費非常[吝嗇]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]小氣過頭":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]希望跟[我]借錢":
        if CHATBOT_MODE:
            if args[1] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]很刻薄":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]很摳":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]很窮":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]想跟[我]借錢":
        if CHATBOT_MODE:
            if args[1] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]打算跟[我]借錢":
        if CHATBOT_MODE:
            if args[1] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]捨不[得]花錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]收入[不多]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]收入[很低]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]是守財奴":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]是窮光蛋":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]月收[只有][25k]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]月薪[28k]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]月薪少得[可憐]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]欠錢不還":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]沒[房]沒[車]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]沒存款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]沒有儲蓄":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]沒錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]當[我]atm":
        if CHATBOT_MODE:
            if args[1] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]當[我]提款機":
        if CHATBOT_MODE:
            if args[1] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]經濟[狀況][很差]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]經濟[狀況]不[好]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]薪水[不高]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]要[我]買[房子]":
        if CHATBOT_MODE:
            if args[1] in argDICT["myself"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]要[我]買房":
        if CHATBOT_MODE:
            if args[1] in argDICT["myself"]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]說[房租]要AA":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[對方]連保險套[也]要和[我]分攤":
        if CHATBOT_MODE:
            if args[2] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]連保險套[都]要和[我]平分":
        if CHATBOT_MODE:
            if args[2] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[對方]連買保險套[都]要[我]分攤":
        if CHATBOT_MODE:
            if args[2] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[我]賺的是[我][男友][兩倍]":
        if CHATBOT_MODE:
            if args[0] in argDICT["myself"] and args[1] in argDICT["myself"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[月收入][僅][2萬多元]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[月薪][僅]有[2萬多]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[第一次][見面]誰付錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "[第一次][見面]誰要付錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "不想讓[對方]覺得[都]是[他]在負擔":
        if CHATBOT_MODE:
            if args[2] in argDICT["3rd_person"] or args[2] == args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "借了[對方]好幾[十萬]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "借了[對方]幾[十萬]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "勸[對方]不要花費超過[自己]經濟[能力]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "同居還不付[房租]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "因為[我]沒在用網路吃到飽":
        if CHATBOT_MODE:
            if args[0] in argDICT["myself"]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "因為[我]沒有網路吃到飽":
        if CHATBOT_MODE:
            if args[0] in argDICT["myself"]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "因為經濟[問題]想提分手":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "因為經濟[能力][自卑]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "因為經濟[能力]分手":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "感情[都]是建立在金錢關係[上]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "月入[只有][2萬]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "月收[只有][2萬多]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "月收入[只有][2萬多]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "有[一定]的經濟[能力][才能]給[對方]好的[未來]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "每個月[只有][2萬多]的[薪水]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "沒[辦法]回送[金額][相當]的[禮物]":
        if CHATBOT_MODE:
            if args[2] in argDICT["equal"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "沒[錢]養[小孩]":
        if CHATBOT_MODE:
            if args[1] in argDICT["child"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "約[見面]誰付錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "約[見面]誰要付錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "覺得[我]是[一直]花[他]錢的[女生]":
        if CHATBOT_MODE:
            if args[0] in argDICT["myself"]:
                resultDICT["response"] = getResponse(utterance, args).format(*args)
        else:
            # write your code here
            pass

    if utterance == "跟[對方]的經濟[非常懸殊]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "連保險套[都]要AA":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "連保險套[都]要跟[我]AA":
        if CHATBOT_MODE:
            if args[1] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "連保險套[錢][都]要AA":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "連保險套[錢][都]要跟[我]AA":
        if CHATBOT_MODE:
            if args[2] in argDICT["me"]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "連保險套的[錢][也]要AA":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "連保險套的開銷[也]要AA":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT