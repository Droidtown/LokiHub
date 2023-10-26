#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for hang2qyan2

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

DEBUG_hang2qyan2 = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/replytwofour/reply_hang2qyan2.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_hang2qyan2:
        print("[hang2qyan2] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "何時[會]被納入[親師群]":
        if args[1] in userDefinedDICT["親師群"]:
            
        
            if CHATBOT_MODE:
                tmpSTR = getResponse(utterance, args)
                resultDICT["response"] = tmpSTR.format(*args)             
            else:
                # write your code here
                pass
        else: pass

    if utterance == "參加[營隊][前][應該]做哪些準備事項":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")
        else:
            # write your code here
            pass

    if utterance == "告知[營隊]行前的[通知]":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")
        else:
            # write your code here
            pass

    if utterance == "提供[營隊]行前的[通知]":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")
        else:
            # write your code here
            pass

    if utterance == "提供[營隊]行前通知":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")            
        else:
            # write your code here
            pass

    if utterance == "有沒[有][營隊]行前的[通知]":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")
        else:
            # write your code here
            pass

    if utterance == "有[營隊]行前通知":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")
        else:
            # write your code here
            pass

    if utterance == "[營隊]行前[任務]是什麼":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")            
        else:
            # write your code here
            pass

    if utterance == "行前[應該]要做什麼準備工作":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")
        else:
            # write your code here
            pass

    if utterance == "行前[須]要完成的事情是什麼":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")
        else:
            # write your code here
            pass

    if utterance == "行前的工作有哪些":
        if "行前" in utterance:
            if CHATBOT_MODE:
                tmpSTR = getResponse(utterance, args)
                resultDICT["response"] = tmpSTR.format("親師群組")
            else:pass
        else:
            # write your code here
            pass

    if utterance == "行前要完成的任務有哪些":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")
        else:
            # write your code here
            pass

    if utterance == "行前需做哪些準備工作":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")
        else:
            # write your code here
            pass

    if utterance == "行前需要做什麼準備":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")
        else:
            # write your code here
            pass

    if utterance == "[營隊]開始[前]需要準備什麼":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")            
        else:
            # write your code here
            pass

    if utterance == "被加入[親師群]":
        if args[0] in userDefinedDICT["親師群"]:
            
        
            if CHATBOT_MODE:
                tmpSTR = getResponse(utterance, args)
                resultDICT["response"] = tmpSTR.format(*args)             
            else:
                # write your code here
                pass
        else: pass

    if utterance == "被邀請加入[親師群]":
        if args[0] in userDefinedDICT["親師群"]:
            
        
            if CHATBOT_MODE:
                tmpSTR = getResponse(utterance, args)
                resultDICT["response"] = tmpSTR.format(*args)             
            else:
                # write your code here
                pass
        else: pass

    if utterance == "進入[親師群]":
        if args[0] in userDefinedDICT["親師群"]:
            
        
            if CHATBOT_MODE:
                tmpSTR = getResponse(utterance, args)
                resultDICT["response"] = tmpSTR.format(*args)             
            else:
                # write your code here
                pass
        else: pass

    if utterance == "進入[營隊][前][須]要準備什麼":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")            
        else:
            # write your code here
            pass

    if utterance == "進入[營隊][前]要做哪些準備":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")            
        else:
            # write your code here
            pass

    if utterance == "[應該][先]作哪些準備的安排":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")            
        else:
            # write your code here
            pass

#新增
    

    if utterance == "[應該]做哪些":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")            
        else:
            # write your code here
            pass

    if utterance == "需要準備什麼":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")            
        else:
            # write your code here
            pass

    if utterance == "加入到[親師群]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

  
    if utterance == "行前通知":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")
        else:
            # write your code here
            pass

    if utterance == "需做哪些準備工作":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")
        else:
            # write your code here
            pass

    if utterance == "需要做什麼準備":
        if CHATBOT_MODE:
            tmpSTR = getResponse(utterance, args)
            resultDICT["response"] = tmpSTR.format("親師群組")
        else:
            # write your code here
            pass

   

    if utterance == "參加營隊[前][應該]做哪些準備事項":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "告知營隊行前的通知":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "提供營隊行前的通知":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "提供營隊行前通知":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有沒[有]營隊行前的通知":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有營隊行前通知":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "營隊行前[應該]要做什麼準備工作":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "營隊行前[須]要完成的事情是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "營隊行前任務是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "營隊行前的工作有哪些":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "營隊行前要完成的任務有哪些":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "營隊行前需做哪些準備工作":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "營隊行前需要做什麼準備":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "營隊開始[前]需要準備什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "進入營隊[前][須]要準備什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "進入營隊[前]要做哪些準備":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "進營隊[之前][應該][先]作哪些準備的安排":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[應該]做哪些準備事項":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[須]要準備什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "告知[營隊]行前的通知":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "提供[營隊]行前的通知":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有沒[有][營隊]行前的通知":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "行前任務是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT