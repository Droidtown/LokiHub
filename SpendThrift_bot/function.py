import re
import os, sys
from sre_constants import GROUPREF_UNI_IGNORE
import csv
from ArticutAPI import Articut
from requests import post

# set path
path_current = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path_current)
os.chdir(path_current)



"""
void SaveAccoutToCSV(json, username)
將 .json 轉成 .csv 並存入 [username].csv 中
"""
def SaveAccountToCSV(data, username='testUser.csv'):
    """
    把 data 轉成 .csv 格式
    """
    # 金額
    result = data["amount"]
    
    # 時間
    result += ", " + data["time"]
        
    # 結束
    result +=  "\n"    
    
    # initialize
    if not os.path.exists("./user_data/" + username + ".csv"):
        with open("./user_data/" + username + ".csv", 'w', encoding="utf-8") as f:
            f.write("amount, time\n" + result)
            f.close()

    else:
        with open("./user_data/" + username + ".csv", 'a', encoding="utf-8") as f:
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
def GetDataByCondition(username="testUser", condition="all"):
    # open csv
    with open("./user_data/" + username + ".csv", 'r', encoding="utf-8") as f:
        # read data
        reader = csv.reader(f)

        # get data by condition
        totalMoney = 0

        # 管他的
        if condition == "all":
            for row in reader:
                # 忽略欄位說明
                if row[0] == "amount":
                    pass
                # 計算
                else:
                    totalMoney += int(row[0])

        # 收入
        elif condition == "earn":
            for row in reader:
                # 忽略欄位說明
                if row[0] == "amount":
                    pass
                # 計算
                else:
                    if int(row[0]) > 0:
                        totalMoney += int(row[0])
        # 收入
        elif condition == "cost":
            for row in reader:
                # 忽略欄位說明
                if row[0] == "amount":
                    pass
                # 計算
                else:
                    if int(row[0]) < 0:
                        totalMoney += int(row[0])
            totalMoney=0-totalMoney #暫時的

        else:
            print("你這個敗家子，連存資料都給我存錯:(")
        return totalMoney


"""
從 LOKI API 得到符合意圖的 regex
並使用 Articut 處理斷詞結果拿到參數
參考：https://api.droidtown.co/document/?python#Loki_7
"""
def getAdvArgs(intent, utterance, inputSTR, groupIndexLIST):
    url = "https://api.droidtown.co/Loki/API/"
    # TODO: account.info
    username = "ss96083@gmail.com"
    articut_key = "NRLknK9bqwxLWVcHMM!%QHvpiUMqKB+"
    loki_key = "BbcY-sJJE-bmc&^s!wZuXCxmzoLeHUh"
    payload = {     
        "username": username,
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
        articut = Articut(username, articut_key, level="lv2")
        articutResultDICT = articut.parse(inputSTR)
        
        # 要對應到指定的意圖
        for i in range(len(response["results"])):
            if response["results"][i]["intent"] == intent:
                pat = re.compile(response["results"][i]["pattern"])

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
