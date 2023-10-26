#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for ying2dwei4nei4rweng2

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

DEBUG_ying2dwei4nei4rweng2 = True
CHATBOT_MODE = True

try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/replytwofour/reply_ying2dwei4nei4rweng2.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_ying2dwei4nei4rweng2:
        print("[ying2dwei4nei4rweng2] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[拯救玩具島]在做什麼":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "{}在做什麼".format(args[0])
            print(utterance)
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)           
            
        else:
            pass
    else:
        pass

    if utterance == "[拯救玩具島]在幹嘛":
        if args[0] in userDefinedDICT["as_camp"]:
            print(args[0])
            
            utterance = "{}在幹嘛".format(args[0])
            print(utterance)
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)           
            
            else:
                pass
        else:
            pass

    if utterance == "[拯救玩具島]的[詳細]內容":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "{}的[詳細]內容".format(args[0])
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)           
        
            else:
                pass
        else:
            pass

    if utterance == "[拯救玩具島]的特色是什麼":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "{}的特色是什麼".format(args[0])
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)           
            else:
                pass
        else:
            pass

    if utterance == "[拯救玩具島]的細節":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "{}的細節".format(args[0])
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)           
        
            else:
                pass
        else:
            pass

    if utterance == "有[拯救玩具島]的課表嗎":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "有{}的課表嗎".format(args[0])
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)           
        
            else:
                pass
        else:
            pass

    if utterance == "[拯救玩具島]":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "{}".format(args[0])
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[拯救玩具島][幾天]幾[夜]":
        if args[0] in userDefinedDICT["as_camp"]:
            resultDICT["response"] = "我們營隊都是五天四夜喔"
        else:
            # write your code here
            pass

    if utterance == "[拯救玩具島][都]在幹嘛":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "{}在幹嘛".format(args[0])
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[拯救玩具島]是啥":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "{}是啥".format(args[0])
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[拯救玩具島]聽起來很有趣":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "{}聽起來很有趣".format(args[0])
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "介紹一下[拯救玩具島]":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "介紹一下{}".format(args[0])
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[拯救玩具島]具有什麼[特][點]":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "{}具有什麼[特][點]".format(args[0])
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[拯救玩具島]感覺很有趣":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "{}感覺很有趣".format(args[0])
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[拯救玩具島]有哪些[獨特]之處":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "{}有哪些[獨特]之處".format(args[0])
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[拯救玩具島]聽起來[似乎][很]有意思":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "{}聽起來[似乎][很]有意思".format(args[0])
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[拯救玩具島]聽起來[相當][有趣]":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "{}聽起來[相當][有趣]".format(args[0])
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[拯救玩具島]聽起來好像挺[好玩]的":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "{}聽起來好像挺[好玩]的".format(args[0])
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[拯救玩具島]聽起來挺有意思的":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "{}聽起來挺有意思的".format(args[0])
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "分享一下[拯救玩具島]":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "分享一下{}".format(args[0])
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "談談[拯救玩具島]":
        if args[0] in userDefinedDICT["as_camp"]:
            utterance = "談談{}".format(args[0])
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass
    if utterance == "[拯救玩具島][都]在[教室]活動嗎":
        if args[0] == "拯救玩具島":
            utterance = "{}[都]在教室活動嗎".format(args[0])
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
                
        elif args[0] == "探索生態島":
            utterance = "{}[都]在教室活動嗎".format(args[0])
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)        
        else:
            # write your code here
            pass    



    return resultDICT
