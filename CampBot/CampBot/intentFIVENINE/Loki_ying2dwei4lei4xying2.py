#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for ying2dwei4lei4xying2

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

DEBUG_ying2dwei4lei4xying2 = True
CHATBOT_MODE = True

try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/replyfivenine/reply_ying2dwei4lei4xying2.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_ying2dwei4lei4xying2:
        print("[ying2dwei4lei4xying2] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[可以]參加的[營隊]有哪些？":
        if args[1] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "[適合]什麼[營隊]":
        if args[1] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "參加什麼[營]":
        if args[0] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass



    if utterance == "想了解[營隊]":
        if args[0] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "推薦[營隊]":
        if args[0] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "推薦[適合]的[營隊]":
        if args[1] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "有[適合]的[營隊]嗎":
        if args[1] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "有什麼[營隊][可]參加？":
        if args[0] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "有哪些[營隊]":
        if "夜" in inputSTR:
            pass
                
        elif args[0] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "有哪些[營隊][能夠]報名？":
        if args[0] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "有哪些[營隊]是[可以]報名的？":
        if args[0] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "有哪幾[個][營隊][可以]參與？":
        if args[1] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "有多少[種][營隊][可以]選擇報名？":
        if args[1] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "有多少[種][營隊][可以]選擇？":
        if args[1] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "考慮參加什麼樣的[營隊]？":
        if args[0] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "要報名參加哪個[營隊]？":
        if args[0] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "[營隊]有哪些":
        if "夜" in inputSTR:
            pass
        
        elif args[0] in userDefinedDICT["活動"]:
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有什麼[不同]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有什麼差別":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "營隊[可以][都]解釋給[我]聽":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "營隊[各自]的[特色]是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass
        
    if utterance == "[可以]學[才藝]的營隊":

        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = "關於學習{}呢,".format(args[1]) +tmpSTR 
        else:
            # write your code here
            pass


    if utterance == "[可以]學創業的營隊":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[營隊]在做什麼":
        if args[0] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "[營隊]在學什麼":
        if args[0] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "[營隊]在幹嘛":
        if args[0] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass

    if utterance == "參加何[種][營隊]活動？":
        if args[1] in userDefinedDICT["活動"]:
            
            if CHATBOT_MODE:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                # write your code here
                pass
        else:
            pass
    
    if utterance == "推薦一下營隊":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass
    
    return resultDICT