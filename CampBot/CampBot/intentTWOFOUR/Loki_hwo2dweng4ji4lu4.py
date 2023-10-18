#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for hwo2dweng4ji4lu4

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

DEBUG_hwo2dweng4ji4lu4 = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/replytwofour/reply_hwo2dweng4ji4lu4.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_hwo2dweng4ji4lu4:
        print("[hwo2dweng4ji4lu4] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[活動]的[相片]要怎麼看":
        if args[1].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format("活動", args[1])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass

    if utterance == "了解[孩子]參與[狀況]":
        if args[1] in userDefinedDICT["問題"]:
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format(args[0], args[1])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass

    if utterance == "得知[孩子]參與[狀況]":
        if args[1] in userDefinedDICT["問題"] and args[0] in userDefinedDICT["小孩"]:
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format(args[0], args[1])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass


    if utterance == "想看[活動][相片]":
        if args[1].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format("活動", args[1])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass

    if utterance == "想要看[活動][照片]要去哪裡找":
        if args[1].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format("活動", args[1])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass

    if utterance == "找到[活動]的[相片]":
        if args[1].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format("活動", args[1])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass


    if utterance == "提供[活動]的[相片]":
        if args[1].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format("活動", args[1])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass


    if utterance == "更新[活動][照片]":
        if args[1].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format("活動", args[1])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass


    if utterance == "有[活動]拍攝的[圖片]":
        if args[1].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format("活動", args[1])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass


    if utterance == "有[活動][照片]":
        if args[1].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format("活動", args[1])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass


    if utterance == "有沒[有][活動]所拍攝的[相片]":
        if args[2].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format("活動", args[2])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass


    if utterance == "有沒[有][活動]的[照片]":
        if args[2].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format("活動", args[2])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass


    if utterance == "有沒[有][照片]":
        if args[1].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format(args[1])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass


    if utterance == "有[照片]":
        if args[0].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format(args[0], args[0])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass

    if utterance == "看[我][小孩]的[照片]":
        if args[2].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format(args[1], args[2])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass


    if utterance == "看到[活動][照片]":
        if args[1].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format("活動", args[1])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass


    if utterance == "看我[女兒]的[照片]":
        if args[1].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format(args[0], args[1])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass


#新增
    if utterance == "更新[每天]的[活動][照片]":
       # args ["每天", "孩子", "相片"]
        if args[2].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format("活動", args[2])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass
        
    if utterance == "[照片]要去哪裡看":
              # args ["相片"]        
        if args[0].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format(args[0], args[0])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass        

    if utterance == "[會]幫[小朋友]拍照":
        if args[1] in userDefinedDICT["小孩"]:
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format(args[1])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass        

    if utterance == "會不[會]幫忙拍照":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

   

   

    

  

    if utterance == "[活動]的[相片]":
        if args[1].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format("活動", args[2])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass
   
   

    

    if utterance == "看[照片]":
        if args[0].endswith("片"):
            if CHATBOT_MODE:
               
                    
                tmpReplySTR = getResponse(utterance, args).format("活動", args[2])
                resultDICT["response"] = tmpReplySTR
               
                    
            else: pass
           
        else:
            # write your code here
            pass

    if utterance == "了解孩子參與狀況":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "得知孩子參與狀況":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "想要看活動照片要去哪裡找":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "找到活動的相片":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "提供活動的相片":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "更新[每天]的活動照片":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "更新活動照片":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有沒[有]活動所拍攝的相片":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有沒[有]活動的照片":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有沒[有]照片":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有活動拍攝的圖片":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有活動照片":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有照片":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "活動的相片要怎麼看":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "看到活動照片":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[相片]要怎麼看":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "了解[孩子]參與狀況":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "得知[孩子]參與狀況":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "幫[小孩]拍照":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "有沒[有][活動]的[相片]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "幫[小孩]拍照":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "更新[每天]的[活動][相片]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "更新[活動][相片]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT