#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for body_part
    
    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict
    
    Output:
        resultDICT    dict
"""

DEBUG_body_part = True
userDefinedDICT = {}
ChildLIST =["小孩","兒子","女兒"]
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_body_part:
        print("[body_part] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "上[顎]腫一塊":
        # write your code here
        resultDICT["bodypart"]=args[0]        
        pass

    if utterance == "[先前]有[耳朵][內部]疼痛":
        # write your code here
        resultDICT["bodypart"]=args[1]
        pass

    if utterance == "[口腔][上][顎]有[血][絲]":
        # write your code here
        resultDICT["bodypart"]=args[2]
        pass

    if utterance == "[喉嚨]卡卡":
        # write your code here
        resultDICT["bodypart"]=args[0]
        pass

    if utterance == "[喉部][兩側]還是會不[舒服]":
        # write your code here
        resultDICT["bodypart"]=args[0]
        pass

    if utterance == "[嘴][上][長黑斑]":
        # write your code here
        if "風池穴" in inputSTR:
            resultDICT["bodypart"]="家醫"
        else:
            resultDICT["bodypart"]=args[0]
        pass

    if utterance == "[我][下][腹]痛[很久]":
        # write your code here
        resultDICT["bodypart"]=args[2]
        pass

    if utterance == "[我][喉嚨]痛到[耳朵]":
        # write your code here
        resultDICT["bodypart"]=args[1]
        pass

    if utterance == "[我][外][陰部]長肉":
        # write your code here
        resultDICT["bodypart"]=args[2]
        pass

    if utterance == "[我]左側[風池穴]附近[經絡處]摸到[硬塊]":
        # write your code here
        resultDICT["bodypart"]=args[1]
        pass

    if utterance == "[我][心臟]亂跳":
        # write your code here
        resultDICT["bodypart"]=args[1]
        pass

    if utterance == "[我]昨天晚上[突然]發現[臉頰]下[方]靠近[脖子]的那個[地方]摸到一顆[腫塊]":
        # write your code here
        resultDICT["bodypart"]=args[2]
        pass

    if utterance == "[我]最近這一年[多][容易][小腿痠]":
        # write your code here
        resultDICT["bodypart"]=args[3]
        pass

    if utterance == "[我][有時][頭]會[突然]暈一下":
        # write your code here
        resultDICT["bodypart"]=args[2]
        pass

    if utterance == "[我][瓣膜]鬆掉":
        # write your code here
        resultDICT["bodypart"]=args[1]
        pass

    if utterance == "[我][胸口]和[喉嚨][依舊]疼痛":
        # write your code here
        resultDICT["bodypart"]=args[1]
        pass

    if utterance == "[我][舌頭][側邊]已經破洞兩個[多]禮拜了":
        # write your code here
        resultDICT["bodypart"]=args[2]
        pass

    if utterance == "[我]覺得[頭]稍微暈暈的":
        # write your code here
        resultDICT["bodypart"]=args[1]
        pass

    if utterance == "[我][雙腿][無力]":
        # write your code here
        resultDICT["bodypart"]=args[1]
        if "壓力" in inputSTR and ("大" in inputSTR):
            resultDICT["symptom"] = "身心"
        if "手" in inputSTR and ("打斷" in inputSTR):
            resultDICT["bodypart"] = "骨"        
        pass

    if utterance == "[我]感覺[小拇指][快]脫落":
        # write your code here
        resultDICT["bodypart"]=args[1]
        pass

    if utterance == "[我]扁[條線]化膿":
        # write your code here
        resultDICT["bodypart"]=args[1]
        pass


    if utterance == "[我]擦[屁股]有[血]":
        # write your code here
        resultDICT["bodypart"]=args[1]
        pass

    if utterance == "[我]有[點][胸][悶]":
        # write your code here
        resultDICT["bodypart"]=args[2]
        pass

    if utterance == "[我]稍微[頸椎][僵直]":
        # write your code here
        resultDICT["bodypart"]=args[1]
        pass

    if utterance == "[我]開始[心跳]跳[很快]":
        # write your code here
        resultDICT["bodypart"]=args[1]
        pass

    if utterance == "[早上]擤[鼻涕][也]是[綠色]":
        # write your code here
        resultDICT["bodypart"]=args[1]
        pass

    if utterance == "[眉間]下[方]還沒到[眼睛]的[地方]會痛":
        # write your code here
        resultDICT["bodypart"]=args[2]
        pass

    if utterance == "[眼睛][經常]不[舒服]":
        # write your code here
        resultDICT["bodypart"]=args[0]
        pass

    if utterance == "[耳朵]有[聲音]":
        # write your code here
        resultDICT["bodypart"]=args[0]
        pass

    if utterance == "[脖子]一顆[硬硬][小小]的":
        # write your code here
        resultDICT["bodypart"]=args[0]
        pass

    if utterance == "[頭]很痛":
        # write your code here
        resultDICT["bodypart"]=args[0]
        pass

    if utterance == "[頸部]有腫塊":
        # write your code here
        resultDICT["bodypart"]=args[0]
        pass

    if utterance == "[頸部]長了[腫塊]":
        # write your code here
        resultDICT["bodypart"]=args[0]
        pass

    if utterance == "[鼻子][裡面]感覺[很緊繃]":
        # write your code here
        resultDICT["bodypart"]=args[0]
        pass

    if utterance == "[鼻子]開始會[長期]鼻塞":
        # write your code here
        resultDICT["bodypart"]=args[0]
        pass

    if utterance == "[鼻樑][兩側]會痛":
        # write your code here
        resultDICT["bodypart"]=args[0]
        pass

    if utterance == "[鼻腔內]有東西":
        # write your code here
        resultDICT["bodypart"]=args[0]
        pass

    if utterance == "吞嚥[不適]":
        # write your code here
        if "吞嚥" in inputSTR: 
            resultDICT["symptom"]="耳鼻喉"
        pass

    if utterance == "從[兩三年][前]就會頭暈還伴隨耳鳴，[胃]痛和失眠":
        # write your code here
        resultDICT["bodypart"]=args[2]
        pass

    if utterance == "轉動[脖子]會不[舒服]":
        # write your code here
        resultDICT["bodypart"]=args[0]
        pass

    if utterance == "我[兒子][肚子]不[舒服]":
         # args [兒子, 肚子, 舒服]
        resultDICT["child"]=args[0]
        resultDICT["bodypart"]=args[1]
        pass
    
    if utterance == "[肚子]不[舒服]":
        # write your code here
        resultDICT["bodypart"]=args[0]
        pass    
    
    if utterance == "[脖子][一顆]硬硬的":
        # args [脖子, 一顆]
        resultDICT["bodypart"]=args[0]
        pass 
    
    if utterance == "我[有時][頭]會稍微暈一下":
        # args [有時, 頭] 
        resultDICT["bodypart"]=args[1]
        
    if utterance == "我[最近][一年]多容易[小腿]酸":
        # args [最近, 一年, 小腿] 
        resultDICT["bodypart"]=args[2]
    
    if utterance == "我[心臟]痛痛的":
        # args [心臟]
        resultDICT["bodypart"]=args[0]
    if utterance == "[背]很酸":
        # args [背] 
        resultDICT["bodypart"]=args[0]
    if utterance == "[眼][前]有小黑影":
        # args [眼, 前]    
        resultDICT["bodypart"]=args[0]
    if utterance == "我[上][臂]痠痛":
        # args [上, 臂]
        resultDICT["bodypart"]=args[1]
    
    if utterance == "[我][牙齒]痛":
        resultDICT["bodypart"]=args[1]
        # args [我, 牙齒] 
    if utterance == "我[骨頭]裂了":
        # args [骨頭]
        resultDICT["bodypart"]=args[0]

            
  

    return resultDICT