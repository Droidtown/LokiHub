#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for symptom
    
    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict
    
    Output:
        resultDICT    dict
"""

DEBUG_symptom = True
userDefinedDICT = {}

import re 

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_symptom:
        print("[symptom] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我]一直拉肚子":
        # write your code here
        if "拉肚子" in inputSTR:
            resultDICT["symptom"] = "腸胃"
        pass

    if utterance == "[我]一直跑廁所":
        # write your code here
        if "跑廁所" in inputSTR:
            resultDICT["symptom"] = "腸胃"         
        pass

    if utterance == "[我]上[廁所]的[頻率]增加":
        # write your code here
        resultDICT["symptom"] = "泌尿"
        pass

    if utterance == "[我][大]便出血[絲]":
        # write your code here
        resultDICT["symptom"] = "腸胃"
        pass

    if utterance == "[我]晚上要睡著會忘記呼吸":
        # write your code here
        if "忘記" in inputSTR and "呼吸" in inputSTR:
            resultDICT["symptom"] = "耳鼻喉" 
        pass

    if utterance == "[我][最近][一直]咳嗽":
        # write your code here
        if "咳嗽" in inputSTR :
            resultDICT["symptom"] = "家醫"        
        pass

    if utterance == "[我]每日[一][腹瀉]":
        # write your code here
        resultDICT["symptom"] = args[2]
        pass

    if utterance == "[我][賀爾蒙]失調":
        # write your code here
        resultDICT["symptom"] = args[1]
        pass

    if utterance == "[我]做過[心導管手術]":
        # write your code here
        resultDICT["symptom"] = args[1]
        pass

    if utterance == "[我]坐著有暈眩的[感覺]":
        # write your code here
        if "暈眩" in inputSTR:
            resultDICT["symptom"] = "耳鼻喉"
        pass

    if utterance == "[我]想吐":
        # write your code here
        if "吐" in inputSTR:
            resultDICT["symptom"] = "家醫"
        if "痣" in inputSTR:
            resultDICT["symptom"] = "皮膚"
        if "驗傷" in inputSTR:
            resultDICT["symptom"] = "急診"
        if "孕" in inputSTR:
            resultDICT["symptom"] = "婦產"
        pass

    if utterance == "[我]拉肚子":
        # write your code here
        resultDICT["symptom"]="腸胃"
        pass

    if utterance == "[我]會[忽然]抖一下":
        # write your code here
        if "抖" in inputSTR:
            resultDICT["symptom"]="神經內"
        pass

    if utterance == "[我]會喘":
        # write your code here
        if "喘" in inputSTR:
            resultDICT["symptom"]="耳鼻喉"
        pass

    if utterance == "[我]會放[臭屁]":
        # write your code here
        if "屁" in inputSTR:
            resultDICT["symptom"] = "腸胃"    
        pass

    if utterance == "[我]有[高血壓][心臟病]":
        # write your code here
        resultDICT["symptom"] = args[1]
        pass

    if utterance == "[我]有心悸":
        # write your code here
        if "心悸" in inputSTR:
            resultDICT["symptom"] = "心臟"         
        pass

    if utterance == "[我]無法行走":
        # write your code here
        resultDICT["symptom"] = "家醫"
        pass

    if utterance == "[我]發燒感冒":
        # write your code here
        if "發燒" in inputSTR or "感冒" in inputSTR:
            resultDICT["symptom"] = "家醫"        
        pass

    if utterance == "[我]要驗[B][肝]":
        # write your code here
        if args[2] in inputSTR and args[3] in inputSTR:
            resultDICT["symptom"] ="一般內" 
        pass

    if utterance == "[我]要驗孕":
        # write your code here
        if "孕" in inputSTR:
            resultDICT["symptom"] = "婦產"
        if "驗傷" in inputSTR: 
            resultDICT["symptom"] = "急診"
        pass

    if utterance == "[我]覺得缺氧":
        # write your code here
        if "缺氧" in inputSTR:
            resultDICT["symptom"] = "胸腔內" 
        pass

    if utterance == "[我]食慾不振會[噁心]":
        # write your code here
        if "食慾不振" in inputSTR:
            resultDICT["symptom"] = "家醫"
        if "瘋" in inputSTR:
            resultDICT["symptom"] = "身心"
        pass
    
    if utterance == "[我人]會暈":
        # write your code here
        if "暈" in inputSTR and "暈倒" not in inputSTR:
            resultDICT["symptom"] = "頭暈" 
        if "暈倒" in inputSTR: 
            resultDICT["symptom"] = "急診"
        pass
    if utterance == "我持續頭暈快[兩個月]":
        # args [兩個月] 
        if "頭暈" in inputSTR:
            resultDICT["symptom"] = "頭暈"  
    if utterance == "我暈眩":
        # args []
        if "暈眩" in inputSTR:
            resultDICT["symptom"] = "頭暈"
    if utterance == "發燒了":
        if "發燒" in inputSTR:
            resultDICT["symptom"] = "家醫"
    if utterance == "感冒了":
        if "感冒" in inputSTR:
            resultDICT["symptom"] = "家醫" 
    if utterance == "我有點[疲勞]":
        resultDICT["symptom"] = args[0]
    if utterance == "頭痛":
        # args []
        if "乳房" in inputSTR:
            resultDICT["symptom"] = "婦產"
        if "頭痛" in inputSTR:
            resultDICT["symptom"] = "頭痛"
        if "雞眼" in inputSTR:
            resultDICT["symptom"] = "皮膚"
        if "屁眼" in inputSTR:
            resultDICT["symptom"] = "肝膽腸胃"
        if "馬眼" in inputSTR:
            resultDICT["symptom"] = "泌尿"
        
    if utterance == "黃疸":
        # args []
        resultDICT["symptom"] = "腸胃"
    if utterance == "流鼻血":
        # args []
        resultDICT["symptom"] = "家醫"
    if utterance == "高血壓":
        # args []
        resultDICT["symptom"] = "一般內科"
    if utterance == "過敏":
        # args []   
        resultDICT["symptom"] = "家醫"
    if utterance == "我有[脂肪瘤]":
        # args [脂肪瘤]
        resultDICT["symptom"] = args[0]
    if utterance == "我[一直]長[痘痘]":
        # args [一直, 痘痘]
        resultDICT["symptom"] = args[1]
    
    if utterance == "瘋了":
        # args []
        if "瘋" in inputSTR:
            resultDICT["symptom"] = "身心"
            
    if utterance == "[我]禿了":
        # args [朋友]
        if "禿" in inputSTR:
            resultDICT["symptom"] = "皮膚" 
    
    if utterance == "[我]骨折了":
        # args [我]
        if "骨折" in inputSTR:
            resultDICT["symptom"] = "骨科" 
    
    if utterance == "[我]痘痘長滿臉":
        # args [我]
        if "痘痘" in inputSTR:
            resultDICT["symptom"] = "皮膚"
    
    if utterance == "[我]痘痘長滿手":
        # args [我]
        if "痘痘" in inputSTR:
            resultDICT["symptom"] = "皮膚"    
    
    if utterance == "[我]痘痘長滿背":
        # args [我]
        if "痘痘" in inputSTR:
            resultDICT["symptom"] = "皮膚"    

    if utterance == "[我]痘痘長滿腳":
        # args [我]
        if "痘痘" in inputSTR:
            resultDICT["symptom"] = "皮膚" 
    if utterance == "[我]好憂鬱":
        # args [我]
        if "憂鬱" in inputSTR:
            resultDICT["symptom"] = "身心"
    if utterance == "[我]好難過":
        # args [我]            
        if "難過" in inputSTR:
            resultDICT["symptom"] = "身心"            
    if utterance == "[我]好想哭":
        # args [我]
        if "哭" in inputSTR:
            resultDICT["symptom"] = "身心"        
    if utterance == "[我]心情不好":
        # args [我]
        if "心情不好" in inputSTR:
            resultDICT["symptom"] = "身心"           
    if utterance == "[我]的右手沒感覺":
        # args [我, 右手]
        if "沒感覺" in inputSTR:
            resultDICT["symptom"] = "神經內"
    if utterance == "我[腳]沒感覺":
        # args [腳]
        if "沒感覺" in inputSTR and (args[1] == "腳" or args[1] == "手" or args[1] == "手指"):
            resultDICT["symptom"] = "神經內"
    if utterance == "[我]的[腳]沒感覺":
        # args [] 
        if "沒感覺" in inputSTR and (args[1] == "腳" or args[1] == "手" or args[1] == "手指"):
            resultDICT["symptom"] = "神經內"
    if utterance == "[我]指尖沒感覺":
        # args [我]
        if "沒感覺" in inputSTR:
            resultDICT["symptom"] = "神經內"
    if utterance == "[我]心痛":
        # args [我] 
        if "心痛" in inputSTR:
            resultDICT["symptom"] = "心臟內"
        if "尿尿" in inputSTR:
            resultDICT["symptom"] = "泌尿"
        if "心跳" in inputSTR and ("慢" in inputSTR):
            resultDICT["symptom"] = "心臟內"
        if "雞眼" in inputSTR:
            resultDICT["symptom"] = "皮膚"
        if "屁眼" in inputSTR:
            resultDICT["symptom"] = "直腸外科"
        if "馬眼" in inputSTR:
            resultDICT["symptom"] = "泌尿"
            
            
    if utterance == "手術傷口復發了":
        # args [] 
        if "手術傷口" in inputSTR and "復發" in inputSTR:
            resultDICT["symptom"] = "外"
            
    if utterance == "[我]眼睛脫窗了":
        # args [我]
        if "眼睛" in inputSTR:
            resultDICT["symptom"] = "眼睛"
    
    if utterance == "[我]看不到[路]":
        # args [我, 路]
        if "看" in inputSTR:
            resultDICT["symptom"] = "眼睛"        
    if utterance == "[我][晚上]看不到[路]":
        # args [我, 晚上, 路] 
        if "看" in inputSTR and ("晚上" in inputSTR or "早上" in inputSTR or "清晨" in inputSTR or "中午" in inputSTR, "半夜" in inputSTR):
            resultDICT["symptom"] = "眼睛"        
    if utterance == "[我][晚上]看不見[路]":
        # args [我, 晚上, 路] 
        if "看" in inputSTR:
            resultDICT["symptom"] = "眼睛"        
    if utterance == "[我]看不見[路]":
        # args [我, 路] 
        if "看" in inputSTR and ("晚上" in inputSTR or "早上" in inputSTR or "清晨" in inputSTR or "中午" in inputSTR, "半夜" in inputSTR):
            resultDICT["symptom"] = "眼睛"  
    if utterance == "[我]中彈了":
        # args [我]
        if "中彈" in inputSTR:
            resultDICT["symptom"] = "急診"
    if utterance == "[我]好累":
        # args [我] 
        if "好累" in inputSTR:
            resultDICT["symptom"] =  "家醫" 
    if utterance == "[我]血尿":
        # args [我]
        if "血尿" in inputSTR:
            resultDICT["symptom"] =  "泌尿" 
    if utterance == "[我]小便有血":
        # args [我]
        if "小便" in inputSTR:
            resultDICT["symptom"] =  "泌尿" 
    if utterance == "[我]心跳[好快]":
        # args [我]
        if "心跳" in inputSTR and ("快" in inputSTR or "慢" in inputSTR):
            resultDICT["symptom"] =  "心臟內" 
    if utterance == "[我]心跳有點[慢]":
        # args [我]
        if "心跳" in inputSTR and ("慢" in inputSTR or "快" in inputSTR):
            resultDICT["symptom"] =  "心臟內" 
    if utterance == "[我]心跳[很慢]":
        # args [我, 很慢] 
        if "心跳" in inputSTR and ("慢" in inputSTR or "快" in inputSTR):
            resultDICT["symptom"] =  "心臟內" 
    if utterance == "[我]懷孕了":
        # args [我] 
        if "懷孕" in inputSTR:
            resultDICT["symptom"] = "婦產"
    if utterance == "[我]有蜂窩性組織炎":
        # args [我]
        if "蜂窩性組織炎" in inputSTR:
            resultDICT["symptom"] = "感染"
        
    if utterance == "[我]有膽結石":
        # args [我]  
        if "膽結石" in inputSTR:
            resultDICT["symptom"] = "消化內"
    if utterance == "[我][胸部]有硬塊":
        # args [我, 胸部] 
        if "硬塊" in inputSTR:
            resultDICT["symptom"] = "外"
    if utterance == "[我]記不起來[路]":
        # args [我, 路]
        if "記不起" in inputSTR:
            resultDICT["symptom"] = "老人醫學"

    if utterance == "我[爸爸]失智":
        # args [爸爸]
        if "失智" in inputSTR:
            resultDICT["symptom"] = "老人醫學"
    
    if utterance == "[我]失智":
        # args [我] 
        if "失智" in inputSTR:
            resultDICT["symptom"] = "老人醫學"
    if utterance == "[我]壓力[好大]":
        # args [我, 好大]
        if "壓力" in inputSTR and ("大" in inputSTR):
            resultDICT["symptom"] = "身心" 
    if utterance == "[鼻子][剛剛]被打斷了":
        # args [剛剛]
        if args[0] == "鼻子" and "被打斷" in inputSTR:
            resultDICT["symptom"] = "整形外"
        if (args[0] == "手" or args[0]== "腳") and "被打斷" in inputSTR:
            resultDICT["symptom"] = "骨"
    if utterance == "[我]長雞眼了":
        # args [我]
        if "雞眼" in inputSTR: 
            resultDICT["symptom"] = "皮膚"
    if utterance == "[我]被[狗狗]咬":
        # args [我, 狗狗]
        if ("狗狗" == args[1] or "狗" == args[1] or "貓" in args[1] or "鳥" in args[1]) and ("咬" in inputSTR or "抓" in inputSTR or "啄" in inputSTR):
            resultDICT["symptom"] = "感染"
    if utterance == "[我]被[貓]抓":
        # args [我, 貓] 
        if ("狗狗" == args[1] or "狗" == args[1] or "貓" in args[1] or "鳥" in args[1]) and ("咬" in inputSTR or "抓" in inputSTR or "啄" in inputSTR):
            resultDICT["symptom"] = "感染"
    if utterance == "[我]被[鳥]啄":
        # args [我, 鳥] 
        if "鳥" == args[1] or "烏鴉" == args[1] or "鴿子" == args[1] or "鵝" == args[1]:
            resultDICT["symptom"] = "感染"
    return resultDICT