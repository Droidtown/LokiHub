import re
import os, sys
from sre_constants import GROUPREF_UNI_IGNORE
import csv
import datetime, time
from ArticutAPI import Articut
from requests import post

# set path
path_current = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path_current)
os.chdir(path_current)



url = "https://api.droidtown.co/Loki/API/"
# TODO: account.info
account = "ss96083@gmail.com"
articut_key = "NRLknK9bqwxLWVcHMM!%QHvpiUMqKB+"
loki_key = "BbcY-sJJE-bmc&^s!wZuXCxmzoLeHUh"


"""_summary_
"""
def SpendThriftReply(resultDICT):
    replySTR = ""
    # 查詢
    if resultDICT["intent"] == "searching":
        replySTR = "查詢結果為 {} 元".format(resultDICT["search_result"])
    
    
    # 進階收入
    if resultDICT["intent"] == "earn_adv":
        # 沒有地點和說明
        if resultDICT["location"] == "" and resultDICT["description"] == "":
            replySTR += "{} 賺到了 {} 元。".format(resultDICT["time"], resultDICT["amount"])
        # 沒說明
        elif resultDICT["description"] == "":
            replySTR += "{} 去 {} 賺到了 {} 元。".format(resultDICT["time"], resultDICT["location"], resultDICT["amount"])
        # 沒地點
        elif resultDICT["location"] == "":
            replySTR += "{} 賺到了 {} 元，因為 {}。".format(resultDICT["time"], resultDICT["amount"], resultDICT["description"])
        # 全部都有
        else:
            replySTR += "{} 去 {} 賺到了 {} 元，因為 {}。".format(resultDICT["time"], resultDICT["location"], resultDICT["amount"], resultDICT["description"])
    
    
        """
            收入超過一定數目：增加特別的提示語
        """
        amount = int(resultDICT["amount"])
        # 10000 元以上
        if amount > 10000:
            replySTR += "\n看來你想通了呢...歡迎來到正常的人世界，恭喜你脫離敗家子的可悲生活：)"        
        # 1000元以上
        elif amount > 5000:
            replySTR += "\n幹得不錯！再過 50 年你就可以買一台二手車了呢。"        
        # 1000元以上
        elif amount > 1000:
            replySTR += "\n好好保持，繼續下去你就不會被房債，卡債和稅務壓垮了。"
    
    # 進階支出
    if resultDICT["intent"] == "spend_adv":
        # 沒有地點和說明
        if resultDICT["location"] == "" and resultDICT["description"] == "":
            replySTR += "{} 花費了 {} 元。".format(resultDICT["time"], resultDICT["amount"])
        # 沒說明
        elif resultDICT["description"] == "":
            replySTR += "{} 去 {} 花費了 {} 元。".format(resultDICT["time"], resultDICT["location"], resultDICT["amount"])
        # 沒地點
        elif resultDICT["location"] == "":
            replySTR += "{} 花費了 {} 元，因為 {}。".format(resultDICT["time"], resultDICT["amount"], resultDICT["description"])
        # 全部都有
        else:
            replySTR += "{} 去 {} 花費了 {} 元，因為 {}。".format(resultDICT["time"], resultDICT["location"], resultDICT["amount"], resultDICT["description"])


        """
            支出超過一定數目：增加特別的提示語
        """
        amount = int(resultDICT["amount"])
        # 10000 元以上
        if amount > 10000:
            replySTR += "\n我的天，你沒救了...\n沒關係，你就繼續當你的敗家子，到時候缺錢我可不會借你。"                
        # 1000元以上
        elif amount > 1000:
            replySTR += "\n你這個臭敗家子！給我克制一點，不然你就等著去吃土吧>:("
    

    # 錯誤
    elif resultDICT["intent"] == "error":
        replySTR += "出現錯誤:" + resultDICT["err_msg"] + "。\n你這敗家子給我去好好讀使用說明書:("

    return replySTR


"""
string GetCurrentDate()
拿到當前的日期
    return "yyyy/mm/dd"
"""
def GetCurrentDate():
    return str(time.localtime().tm_year) + "-" + str(time.localtime().tm_mon) + "-" + str(time.localtime().tm_mday)



"""
string TransformTime():
用 Articut lv3(語意分析) 將中文時間轉換成 yyyy-mm-dd
    return "yyyy-mm-dd"
"""
def TransformDate(inputSTR):
    # 去 LOKI 取得這個 utterance 的 regex
    # region ArticutLV3
    """
    {   'person': [[]], 'event': [[]], 'time': [[{'absolute': False, 'datetime': '2022-08-24 00:00:00', 'text': '昨天',
        'time_span': {'year': [2022, 2022], 'month': [8, 8], 'weekday': [3, 3], 'day': [24, 24], 'hour': [0, 23], 'minute': [0, 59], 'second': [0, 59], 'time_period': 'night'}}]],
        'site': [[]], 'entity': [[]], 'number': {'300': 300}, 'user_defined': [[]], 'utterance': ['ㄗㄨㄛˊ ㄊㄧㄢ /ㄏㄨㄚ ㄌㄜ˙ /300'],
        'input': [[0, 7]], 'unit': {'300': ''}, 'exec_time': 0.03658628463745117, 'level': 'lv3', 'version': 'v256', 'status': True, 'msg': 'Success!',
        'word_count_balance': 0
    }
    """
    # endregion
    articut = Articut(account, articut_key, level="lv3")
    articutResultDICT = articut.parse(inputSTR)
    return articutResultDICT["time"][0][0]["datetime"][0:10]



"""
void SaveAccoutToCSV(json, username)
將 .json 轉成 .csv 並存入 [username].csv 中
"""
def SaveAccountToCSV(data, userID='testUser'):
    """
    把 data 轉成 .csv 格式
    """
    # 時間
    result = data["time"]
    
    # 模式
    result += "," + data["intent"]
    
    # 金額
    result += "," + data["amount"]
    
    # 地點
    result += "," + data["location"]
    
    # 理由
    result += "," + data["description"]
    
    
        
    # 結束
    result +=  "\n"    
    
    # initialize
    if not os.path.exists("./user_data/" + userID + ".csv"):
        with open("./user_data/" + userID + ".csv", 'w', encoding="utf-8") as f:
            f.write("time, mode, amount, location, description\n" + result)
            f.close()

    else:
        with open("./user_data/" + userID + ".csv", 'a', encoding="utf-8") as f:
            f.write(result)
            f.close()


"""
int GetDataByCondition(username, condition)
從 [username].csv 中讀取資料，並根據 condition 的模式做判斷
    - all: 全部的記帳資料
    - earn: 收入(金額>0)
    - cost: 支出(金額<0)

return 查詢情況的統計金額
"""
def GetDataByCondition(userID="testUser", condition="all"):
    # open csv
    with open("./user_data/" + userID + ".csv", 'r', encoding="utf-8") as f:
        # read data
        reader = csv.reader(f)

        # get data by condition
        totalMoney = 0


        for row in reader:
            # 忽略欄位說明(第一列)
            if row[0] == "time":
                pass
            
            # 收入
            elif condition == "earn":
                if row[1] == "earn_adv":    # 收入的 intent 名稱
                    totalMoney += int(row[2])

            
            # 支出        
            elif condition == "cost":
                if row[1] == "spend_adv":   # 支出的 intent 名稱
                    totalMoney += int(row[2])

                        
            # 管他的
            elif condition == "all":
                 totalMoney += int(row[2])

            
            # error
            else:
                return "error"
        return totalMoney


"""
從 LOKI API 得到符合意圖的 regex
並使用 Articut 處理斷詞結果拿到參數
參考：https://api.droidtown.co/document/?python#Loki_7
"""
def GetAdvArgs(intent, utterance, inputSTR, groupIndexLIST):
    payload = {     
        "username": account,
        "loki_key": loki_key,
        "input_str": utterance
    }
    
    # 去 LOKI 取得這個 utterance 的 regex
    # region responseExample
    """
    {
        "status": true,
        "msg": "Success!",
        "version": "v193",
        "word_count_balance": 99988,
        "results": [
            {"intent": "Exchange",
            "pattern": "<KNOWLEDGE_currency>[^<]*?</KNOWLEDGE_currency>(<MODAL>[^<]*?</MODAL>)?((<ACTION_verb>[^<不]*?[換][^<不]*?</ACTION_verb>)|(<VerbP>[^<不]*?[換][^<不]*?</VerbP>))<CLAUSE_HowQ>[^<]*?</CLAUSE_HowQ><ENTITY_UserDefined>[^<]*?</ENTITY_UserDefined>",
            "utterance": "[100美金]能換多少[台幣]",
            "argument": ["100美金", "台幣"]}
        ]
    }
    """
    # endregion
    response = post(url, json=payload).json()
    
    # success
    if response["status"] == True:
        
        # 將輸入丟進 articut 斷詞
        articut = Articut(account, articut_key, level="lv2")
        articutResultDICT = articut.parse(inputSTR)
       
        # 要對應到指定的意圖
        for i in range(len(response["results"])):
            if response["results"][i]["intent"] == intent:
                pat = re.compile(response["results"][i]["pattern"])

        # print(articutResultDICT["result_pos"][0])
        # print(pat)

        # 將輸入用 re 比較
        patGroups = re.search(pat, articutResultDICT["result_pos"][0])
        args = []
        
        # 把我們要的參數拿出來
        for i in groupIndexLIST:
            args.append(patGroups.group(i))
        return (response["status"], args)
    # error
    else:
        return (response["status"], response["msg"])


