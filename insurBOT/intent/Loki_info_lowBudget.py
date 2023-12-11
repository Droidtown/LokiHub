#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for info_lowBudget

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

DEBUG_info_lowBudget = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_info_lowBudget.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_info_lowBudget:
        print("[info_lowBudget] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "低預算":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
            # if 'acc_con' in resultDICT:
            #     resultDICT['acc_con'].append("low")
            # if 'life_con' in resultDICT:
            #     resultDICT['life_con'].append("low")
            # else:
            #     resultDICT['life_con'] = []
            #     resultDICT['life_con'].append("low")
            #     resultDICT['acc_con'] = []
            #     resultDICT['acc_con'].append("low")
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "保一般的":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")




            # elif 'life_con' in resultDICT:
            #     resultDICT['life_con'].append("low")
            # else:
            #     resultDICT['life_con'] = []
            #     resultDICT['life_con'].append("low")
            #     resultDICT['acc_con'] = []
            #     resultDICT['acc_con'].append("low")
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "小資方案":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "小額":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
            # if 'acc_con' in resultDICT:
            #     if 'high' not in resultDICT['acc_con']:
            #         resultDICT['acc_con'].append("low")
            # elif 'life_con' in resultDICT:
            #     if 'high' not in resultDICT['acc_con']:
            #         resultDICT['acc_con'].append("low")
            # else:  
            #     resultDICT['life_con'] = []
            #     resultDICT['life_con'].append("low")
            #     resultDICT['acc_con'] = []
            #     resultDICT['acc_con'].append("low")
                if not resultDICT['type']:
                    resultDICT['low'] = True
            

    if utterance == "比較低":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True

    if utterance == "預算不多":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "預算少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "預算比較少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "預算沒那麼多":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "不想花太多錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "基礎保障":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "沒那麼多預算":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
            # if "life" in resultDICT['type']:
            #     resultDICT['life_con'] = []
            #     resultDICT['life_con'].append("low")
            # if "accident" in resultDICT['type']:
            #     resultDICT['acc_con'] = []
            #     resultDICT['acc_con'].append("low")
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "花費少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "花費比較少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
            # if "life" in resultDICT['type']:
            #     resultDICT['life_con'] = []
            #     resultDICT['life_con'].append("low")
            # if "accident" in resultDICT['type']:
            #     resultDICT['acc_con'] = []
            #     resultDICT['acc_con'].append("low")
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "錢不好賺":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "錢太難賺":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "錢很難賺":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
            # if 'acc_con' in resultDICT:
            #     resultDICT['acc_con'].append("low")
            # elif 'life_con' in resultDICT:
            #     resultDICT['life_con'].append("low")
            # else:
            #     resultDICT['life_con'] = []
            #     resultDICT['life_con'].append("low")
            #     resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "價格實惠":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == " 壓力大":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "很窮":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "沒什麼預算":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "沒有什麼預算":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "不太有錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "不怎麼富裕":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "不想支出那麼多":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "不想要這麼貴":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            else:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "不是很寬裕":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "快要吃土了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "經濟狀況有點拮据":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "降低經濟壓力":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
                
            if not resultDICT['type']:
                resultDICT['low'] = True
            

    if utterance == "不要太貴的險":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")
            

    if utterance == "有點窮":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if 'acc_con' in resultDICT:
                resultDICT['acc_con'].append("low")
            elif "acc_con" not in resultDICT:
                resultDICT['acc_con'] = []
                resultDICT['acc_con'].append("low")
            
            if 'life_con' in resultDICT:
                resultDICT['life_con'].append("low")
            elif "life_con" not in resultDICT:
                resultDICT['life_con'] = []
                resultDICT['life_con'].append("low")

    return resultDICT