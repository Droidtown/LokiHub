#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for earn_adv

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

# local import
import function as fun

DEBUG_earn_adv = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_key":["收入","支出","記帳狀況"],"_park":["六福村","九族文化村","義大","義大世界"],"_money":["支出總額","支出費用","總金額","總額","費用","金錢","錢"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_earn_adv:
        print("[earn_adv] {} ===> {}".format(inputSTR, utterance))


# 這個意圖的名字
intent = "earn_adv"

"""
對照 utterance 拿到參數
getResult() 多了第一個參數 userID，以使用者的 ID 作為檔案名稱記賬
"""
def getResult(userID, inputSTR, utterance, rePAT, resultDICT):
    debugInfo(inputSTR, utterance)
    print(rePAT)
    if utterance == "去全聯收入3000":
        """
            5: 地點
            7: 說明
            11: 金額
        """
        status, result = fun.GetAdvArgs(inputSTR, rePAT, [5,7,11])
        
        if status == True:
            argsLoc = fun.RemoveLokiTags(result[0])
            reasonLoc = ""
            for i in argsLoc:
                reasonLoc += i
            argsDesc = fun.RemoveLokiTags(result[1])
            reasonDesc = ""
            for i in argsDesc:
                reasonDesc += i
            
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.GetCurrentDate()   # 時間
            resultDICT["location"] = argsLoc            # 地點
            resultDICT["description"] = reasonDesc      # 說明
            resultDICT["amount"] = result[2]            # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "去全聯賺了3000":
        """
            5: 地點
            7: 說明
            11: 金額
        """
        status, result = fun.GetAdvArgs(inputSTR, rePAT, [5,7,11])
        
        if status == True:
            argsLoc = fun.RemoveLokiTags(result[0])
            reasonLoc = ""
            for i in argsLoc:
                reasonLoc += i
            argsDesc = fun.RemoveLokiTags(result[1])
            reasonDesc = ""
            for i in argsDesc:
                reasonDesc += i
            
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.GetCurrentDate()   # 時間
            resultDICT["location"] = reasonLoc          # 地點
            resultDICT["description"] = reasonDesc      # 說明
            resultDICT["amount"] = result[2]            # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "去六福村收入3000":
        """
            3: 地點
            7: 金額
        """ 
        status, result = fun.GetAdvArgs(inputSTR, rePAT, [3,7])

        if status == True:
            args = fun.RemoveLokiTags(result[0])
            reason = ""
            for i in args:
                reason += i

            resultDICT["intent"] = intent
            resultDICT["time"] = fun.GetCurrentDate()   # 時間
            resultDICT["location"] = ""         # 地點
            resultDICT["description"] = reason          # 說明
            resultDICT["amount"] = result[1]        # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
 
        pass
    

    if utterance == "去六福村賺了3000":
        """
            3: 地點
            7: 金額
        """ 
        status, result = fun.GetAdvArgs(inputSTR, rePAT, [3,7])

        if status == True:
            args = fun.RemoveLokiTags(result[0])
            reason = ""
            for i in args:
                reason += i

            resultDICT["intent"] = intent
            resultDICT["time"] = fun.GetCurrentDate()   # 時間
            resultDICT["location"] =""              # 地點
            resultDICT["description"] = reason      # 說明
            resultDICT["amount"] = result[1]        # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
 
        pass
        


    if utterance == "去台北收入3000":
        """
            4: 地點
            6: 說明
            10: 金額
        """
        status, result = fun.GetAdvArgs(inputSTR, rePAT, [4,6,10])
        
        if status == True:
            args = fun.RemoveLokiTags(result[1])
            reason = ""
            for i in args:
                reason += i
            
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.GetCurrentDate()   # 時間
            resultDICT["location"] = result[0]          # 地點
            resultDICT["description"] = reason          # 說明
            resultDICT["amount"] = result[2]            # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "去台北賺了3000":
        """
            4: 地點
            6: 說明
            10: 金額
        """
        status, result = fun.GetAdvArgs(inputSTR, rePAT, [4,6,10])
        
        if status == True:
            args = fun.RemoveLokiTags(result[1])
            reason = ""
            for i in args:
                reason += i
            
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.GetCurrentDate()   # 時間
            resultDICT["location"] = result[0]          # 地點
            resultDICT["description"] = reason          # 說明
            resultDICT["amount"] = result[2]            # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "收入3000":
        """
            4: 金額
        """
        status, result = fun.GetAdvArgs(inputSTR, rePAT, [4])
        
        if status == True:
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.GetCurrentDate()   # 時間
            resultDICT["location"] = ""                 # 地點
            resultDICT["description"] = ""              # 說明
            resultDICT["amount"] = result[0]            # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "昨天去全聯收入3000":
        """
            3: 時間
            9: 地點
            11: 說明
            15: 金額
        """
        status, result = fun.GetAdvArgs(inputSTR, rePAT, [3,9,11,15])
        
        if status == True:
            argsLoc = fun.RemoveLokiTags(result[1])
            reasonLoc = ""
            for i in argsLoc:
                reasonLoc += i
            argsDesc = fun.RemoveLokiTags(result[2])
            reasonDesc = ""
            for i in argsDesc:
                reasonDesc += i
            
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.TransformDate(result[0])   # 時間
            resultDICT["location"] = reasonLoc                  # 地點
            resultDICT["description"] = reasonDesc              # 說明
            resultDICT["amount"] = result[3]                    # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    
    

    if utterance == "昨天去全聯賺了3000":
        """
            3: 時間
            9: 地點
            11: 說明
            15: 金額
        """
        status, result = fun.GetAdvArgs(inputSTR, rePAT, [3,9,11,15])
        
        if status == True:
            argsLoc = fun.RemoveLokiTags(result[1])
            reasonLoc = ""
            for i in argsLoc:
                reasonLoc += i
            argsDesc = fun.RemoveLokiTags(result[2])
            reasonDesc = ""
            for i in argsDesc:
                reasonDesc += i
            
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.TransformDate(result[0])          # 時間
            resultDICT["location"] = reasonLoc                         # 地點
            resultDICT["description"] = reasonDesc                     # 說明
            resultDICT["amount"] = result[3]                           # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "昨天收入3000":
        """
            3: 時間
            5: 說明
            9: 金額
        """
        status, result = fun.GetAdvArgs(inputSTR, rePAT, [3,5,9])
        
        if status == True:
            args = fun.RemoveLokiTags(result[1])
            reason = ""
            for i in args:
                reason += i
            
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.TransformDate(result[0])   # 時間
            resultDICT["location"] = ""                         # 地點 
            resultDICT["description"] = reason                  # 說明
            resultDICT["amount"] = result[2]                    # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "昨天賺了3000":
        """
            3: 時間
            5: 說明
            9: 金額
        """
        status, result = fun.GetAdvArgs(inputSTR, rePAT, [3,5,9])
        
        if status == True:
            args = fun.RemoveLokiTags(result[1])
            reason = ""
            for i in args:
                reason += i
            
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.TransformDate(result[0])   # 時間
            resultDICT["location"] = ""                         # 地點
            resultDICT["description"] = reason                  # 說明
            resultDICT["amount"] = result[2]                    # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "賺了3000":
        """
            4: 金額
        """
        status, result = fun.GetAdvArgs(inputSTR, rePAT, [4])
        
        if status == True:
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.GetCurrentDate()   # 時間
            resultDICT["location"] = ""                 # 地點
            resultDICT["description"] = ""              # 說明
            resultDICT["amount"] = result[0]            # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "昨天去六福村收入3000":
        # 因為 Articut 不會把 "收入" 算成動詞，因此會斷詞錯誤
        """
            3: 時間
            7: 地點
            8: 說明
            12: 金額
        """
        status, result = fun.GetAdvArgs(inputSTR, rePAT, [3,7,8,12])
        
        if status == True:
            argsLoc = fun.RemoveLokiTags(result[1])
            reasonLoc = ""
            for i in argsLoc:
                reasonLoc += i
            argsDesc = fun.RemoveLokiTags(result[2])
            reasonDesc = ""
            for i in argsDesc:
                reasonDesc += i              
            
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.TransformDate(result[0])   # 時間
            resultDICT["location"] = reasonLoc                  # 地點
            resultDICT["description"] = reasonDesc              # 說明
            resultDICT["amount"] = result[3]                    # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass

    if utterance == "昨天去六福村賺了3000":
        # 進不來 :(
        # resultDICT["intent"] = "error"
        # resultDICT["err_msg"] = "不知道怎麼著但你成功進入我們無法進入的領域了！你成功證明了自己不是一個敗家子:)"
        # pass
        
        """
            3: 時間
            7: 地點
            8: 說明
            12: 金額
        """
        status, result = fun.GetAdvArgs(inputSTR, rePAT, [3,7,8,12])
        
        if status == True:
            argsLoc = fun.RemoveLokiTags(result[1])
            reasonLoc = ""
            for i in argsLoc:
                reasonLoc += i
            argsDesc = fun.RemoveLokiTags(result[2])
            reasonDesc = ""
            for i in argsDesc:
                reasonDesc += i              
            
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.TransformDate(result[0])   # 時間
            resultDICT["location"] = reasonLoc                  # 地點
            resultDICT["description"] = reasonDesc              # 說明
            resultDICT["amount"] = result[3]                    # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "昨天去台北收入3000":
        """
            3: 時間
            8: 地點
            10: 說明
            14: 金額
        """
        status, result = fun.GetAdvArgs(inputSTR, rePAT, [3,8,10,14])
        
        if status == True:
            argsLoc = fun.RemoveLokiTags(result[1])
            reasonLoc = ""
            for i in argsLoc:
                reasonLoc += i
            argsDesc = fun.RemoveLokiTags(result[2])
            reasonDesc = ""
            for i in argsDesc:
                reasonDesc += i
            
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.TransformDate(result[0])   # 時間
            resultDICT["location"] = reasonLoc                  # 地點
            resultDICT["description"] = reasonDesc              # 說明
            resultDICT["amount"] = result[3]                    # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "昨天去台北賺了3000":
        """
            3: 時間
            10: 地點
            12: 說明
            16: 金額
        """
        status, result = fun.GetAdvArgs(inputSTR, rePAT, [3,10,12,16])
        
        if status == True:
            argsLoc = fun.RemoveLokiTags(result[1])
            reasonLoc = ""
            for i in argsLoc:
                reasonLoc += i
            argsDesc = fun.RemoveLokiTags(result[2])
            reasonDesc = ""
            for i in argsDesc:
                reasonDesc += i
            
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.TransformDate(result[0])   # 時間
            resultDICT["location"] = reasonLoc                  # 地點
            resultDICT["description"] = reasonDesc              # 說明
            resultDICT["amount"] = result[3]                    # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass


    # 分析完畢，儲存結果
    if resultDICT["intent"] != "error":
        fun.SaveAccountToCSV(resultDICT, userID)

    elif resultDICT["intent"] == "error" and resultDICT["err_msg"] == "":
        resultDICT["err_msg"] = "不知道你幹了什麼敗家子的行為，反正我看不懂"

    return resultDICT