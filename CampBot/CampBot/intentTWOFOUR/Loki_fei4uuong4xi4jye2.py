#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for fei4uuong4xi4jye2

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

DEBUG_fei4uuong4xi4jye2 = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/replytwofour/reply_fei4uuong4xi4jye2.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_fei4uuong4xi4jye2:
        print("[fei4uuong4xi4jye2] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[價格]是多少錢?":
        
        if CHATBOT_MODE:
            
            if args[0] in userDefinedDICT["費用"]:
               
                tmpReplySTR = getResponse(utterance, args).format(args[0])
                resultDICT["response"] = tmpReplySTR
              
            else:
                pass                     
        else:
            # write your code here
            pass

    if utterance == "[教材][是]否已納入[費用]之[中]？":
        if CHATBOT_MODE:
            if args[2] in userDefinedDICT["費用"]:

                tmpReplySTR = getResponse(utterance, args).format(args[2], args[0])
                resultDICT["response"] = tmpReplySTR
                
            else:
                pass                  

        else:
            # write your code here
            pass


    if utterance == "[教材][是]否已經被納入[費用]了？":
        if CHATBOT_MODE:
            
            if args[2] in userDefinedDICT["費用"]:

                tmpReplySTR = getResponse(utterance, args).format(args[2], args[0])
                resultDICT["response"] = tmpReplySTR
                
            else:
                pass   
              
        else:
            pass  
        
    if utterance == "[教材]是不[是]已經包含在[費用][中]了？":
        if CHATBOT_MODE:
            if args[2] in userDefinedDICT["費用"]:
                tmpReplySTR = getResponse(utterance, args).format(args[2], args[0])
                resultDICT["response"] = tmpReplySTR
                
            else:
                pass                  

        else:
            # write your code here
            pass

    if utterance == "[教材]有[包]含在[費用][裡]嗎？":
        if CHATBOT_MODE:
            if args[2] in userDefinedDICT["費用"]:

                tmpReplySTR = getResponse(utterance, args).format(args[2], args[0])
                resultDICT["response"] = tmpReplySTR
                
            else:
                pass                  

        else:
            # write your code here
            pass

    if utterance == "[是]否[會]有[額外]的[金額]需要支付？":
        if CHATBOT_MODE:
            if args[3] in userDefinedDICT["費用"]:

                tmpReplySTR = getResponse(utterance, args).format(args[3])
                resultDICT["response"] = tmpReplySTR
                
            else:
                pass                  

        else:
            # write your code here
            pass

    if utterance == "[是]否[會]有其他的[花費]？":
        if CHATBOT_MODE:
            if args[2] in userDefinedDICT["費用"]:

                tmpReplySTR = getResponse(utterance, args).format(args[2])
                resultDICT["response"] = tmpReplySTR
                
            else:
                pass                  

        else:
            # write your code here
            pass

    if utterance == "[是]否[會]產生[額外]的[費用]？":
        if CHATBOT_MODE:
            if args[3] in userDefinedDICT["費用"]:

                tmpReplySTR = getResponse(utterance, args).format(args[3])
                resultDICT["response"] = tmpReplySTR
                
            else:
                pass                  

        else:
            # write your code here
            pass

    if utterance == "[費用][是]否已經包括了[教材]？":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT["費用"]:

                tmpReplySTR = getResponse(utterance, args).format(args[0], args[2])
                resultDICT["response"] = tmpReplySTR
                
            else:
                pass                  

        else:
            # write your code here
            pass

    if utterance == "[費用][裡]有沒[有][包]含[教材]？":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT["費用"]:

                tmpReplySTR = getResponse(utterance, args).format(args[0], args[4])
                resultDICT["response"] = tmpReplySTR
                
            else:
                pass                  

        else:
            # write your code here
            pass

    if utterance == "[費用]是多少":
        if CHATBOT_MODE:
            
            if args[0] in userDefinedDICT["費用"]:
               
                tmpReplySTR = getResponse(utterance, args).format(args[0])
                resultDICT["response"] = tmpReplySTR
              
            else:
                pass                     
        else:
            # write your code here
            pass

    if utterance == "[費用]有[包]含[教材]嗎":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT["費用"]:

                tmpReplySTR = getResponse(utterance, args).format(args[0], args[2])
                resultDICT["response"] = tmpReplySTR
                
            else:
                pass                  

        else:
            # write your code here
            pass
    if utterance == "[費用]有包括[教材]":
             # args ["學費", "保險"]    
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT["費用"]:

                tmpReplySTR = getResponse(utterance, args).format(args[0], args[1])
                resultDICT["response"] = tmpReplySTR
                
            else:
                pass                  

        else:
            # write your code here
            pass 

    if utterance == "[費用]為何?":
        if CHATBOT_MODE:
            
            if args[0] in userDefinedDICT["費用"]:
               
                tmpReplySTR = getResponse(utterance, args).format(args[0])
                resultDICT["response"] = tmpReplySTR
              
            else:
                pass                     
        else:
            # write your code here
            pass

    if utterance == "[費用]要多少":
        if CHATBOT_MODE:
            
            if args[0] in userDefinedDICT["費用"]:
               
                tmpReplySTR = getResponse(utterance, args).format(args[0])
                resultDICT["response"] = tmpReplySTR
              
            else:
                pass                     
        else:
            # write your code here
            pass

    if utterance == "會不[會]有[額外]的[費用]":
        if CHATBOT_MODE:
            if args[2] in userDefinedDICT["費用"]:

                tmpReplySTR = getResponse(utterance, args).format(args[2])
                resultDICT["response"] = tmpReplySTR
                
            else:
                pass                  

        else:
            # write your code here
            pass

    if utterance == "會不[會]有[額外]需支付的[費用]？":
        if CHATBOT_MODE:
            if args[2] in userDefinedDICT["費用"]:

                tmpReplySTR = getResponse(utterance, args).format(args[2])
                resultDICT["response"] = tmpReplySTR
                
            else:
                pass                  

        else:
            # write your code here
            pass

    if utterance == "[費用]需要多少錢?":
        if CHATBOT_MODE:
            
            if args[0] in userDefinedDICT["費用"]:
               
                tmpReplySTR = getResponse(utterance, args).format(args[0])
                resultDICT["response"] = tmpReplySTR
              
            else:
                pass                     
        else:
            # write your code here
            pass


    if utterance == "多少錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass
     

    if utterance == "多貴":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[是]否[會]有[額外]的金額需要支付？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[費用][是]否已經包括了教材？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[費用][裡]有沒[有][包]含教材？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[費用]有[包]含教材嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "教材[是]否已納入[費用]之[中]？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "教材[是]否已經被納入費用了？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "教材是不[是]已經包含在[費用][中]了？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "教材有[包]含在[費用][裡]嗎？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "會不[會]有[額外]的費用":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "花費需要多少錢?":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[花費]需要多少錢?":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT