from asyncio.windows_events import NULL
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

"""
    由於 LOKI 和 Articut 衝突問題，先把 LOKI 中的 tags(<>) 給去除
"""
def RemoveLokiTags(input):
    return re.findall(r'<[^<]*>([^<>]*)</[^<]*>', input)


"""
    回覆格式
"""
def SpendThriftReply(resultDICT):
    replySTR = ""
    try:
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
        
        # 幣值錯誤
        elif resultDICT["intent"] == "error_currency":
            replySTR += "你敗家到連金錢的單位都搞不清楚了嗎...我只聽得懂 '台幣'，或是 '錢', '元' 這種金錢代稱喔"
        # 其他錯誤
        elif resultDICT["intent"] == "error":
            replySTR += "出現錯誤:" + resultDICT["err_msg"] + "。\n你這敗家子給我去好好讀使用說明書:("
    except:
        replySTR = "不知道怎麼搞的，不過你敗家到我不知道你在幹嘛呢..."

    return replySTR

# region function_of_time
"""
string GetCurrentDate()
拿到當前的日期
    return "yyyy-mm-dd"
"""
def GetCurrentDate():
    return str(time.localtime().tm_year) + "-" + str(time.localtime().tm_mon) + "-" + str(time.localtime().tm_mday)

"""
string TransformTime():
用 Articut lv3(語意分析) 將中文時間轉換成指定日期 yyyy-mm-dd
    return "yyyy-mm-dd"
"""
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
def TransformDate(inputSTR):
    try:
        articut = Articut(account, articut_key, level="lv3")
        articutResultDICT = articut.parse(inputSTR)

        return articutResultDICT["time"][0][0]["datetime"][0:10]

    except:
        return GetCurrentDate()

""" 
List GetTimeSpan():
用 Articut lv3 將中文時間轉換成指定時間區間
    return ["yyyy-mm-dd", "yyyy-mm-dd"]
"""
def GetTimeSpan(inputSTR, failedLIST=[]):
    try:
        articut = Articut(account, articut_key, level="lv3")
        
        # Articut 沒辦法處理的時間格式會被丟到這邊處理
        if inputSTR == "_articut_failed_":
            # 用現在的時間去推算
            articutResultDICT = articut.parse("現在")
            timespan = articutResultDICT["time"][0][0]["time_span"]
            
            if failedLIST[0] == "這個":                    
                # 月
                if failedLIST[1] in ["月", "月份"]:
                    startDate = ToZeroString(timespan["year"][0]) + "-" + ToZeroString(timespan["month"][0]) + "-" + "01"
                    endDate = ToZeroString(timespan["year"][1]) + "-" + ToZeroString(timespan["month"][1]) + "-" + "31"
                
                # 週
                elif failedLIST[1] in ["週","周"]:
                    # 如果上週有包含上個月
                    if timespan["day"][0] - timespan["weekday"][0] < 1:
                        # 再用一次Articut去抓取上個月的時間
                        lastMonthDICT = articut.parse("上個月")
                        lastMonthTime = lastMonthDICT["time"][0][0]["time_span"]
                        startDate = ToZeroString(timespan["year"][1]) + "-" + ToZeroString(lastMonthTime["month"][1]) + "-" + ToZeroString(lastMonthTime["day"][1]+(timespan["day"][0] - timespan["weekday"][0]) + 1)
                    else:
                        startDate = ToZeroString(timespan["year"][0]) + "-" + ToZeroString(timespan["month"][0]) + "-" + ToZeroString(timespan["day"][0] - timespan["weekday"][0] + 1)
                    endDate = ToZeroString(timespan["year"][1]) + "-" + ToZeroString(timespan["month"][1]) + "-" + ToZeroString(timespan["day"][0])
                
                # 日
                elif failedLIST[1] in ["日", "天"]:
                    startDate = ToZeroString(timespan["year"][0]) + "-" + ToZeroString(timespan["month"][0]) + "-" + ToZeroString(timespan["day"][0])
                    endDate = ToZeroString(timespan["year"][1]) + "-" + ToZeroString(timespan["month"][1]) + "-" + ToZeroString(timespan["day"][1])
                
        else:        
            articutResultDICT = articut.parse(inputSTR)
            
            timespan = articutResultDICT["time"][0][0]["time_span"]
            startDate = ToZeroString(timespan["year"][0]) + "-" + ToZeroString(timespan["month"][0]) + "-" + ToZeroString(timespan["day"][0])
            endDate = ToZeroString(timespan["year"][1]) + "-" + ToZeroString(timespan["month"][1]) + "-" + ToZeroString(timespan["day"][1])

        return [startDate, endDate]

    # 出現錯誤就回傳今天
    except:
        return [GetCurrentDate(),GetCurrentDate()]

def ToZeroString(number):
    if number < 10:
        return "0" + str(number)
    else:
        return str(number)
# endregion


"""
bool CorrectCurrency(string, list[string])
判斷幣值是否正確
"""
def CorrectCurrency(inputSTR, currencyLIST):
    if inputSTR not in currencyLIST:
        return False
    return True



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
def GetDataByCondition(userID="testUser", condition="all", timespan=[]):
    # open csv
    with open("./user_data/" + userID + ".csv", 'r', encoding="utf-8") as f:
        # read data
        reader = csv.reader(f)

        # get data by condition
        totalMoney = 0


        for row in reader:
            # 忽略欄位說明(第一列)
            if row[0] == "time":
                continue
            
            # 搜尋條件有包含時間
            if timespan != []:
                # 不再要求的時間範圍內就直接跳過
                if row[0] < timespan[0] or row[0] > timespan[1]:
                    continue
                
                # 收入
                if condition == "earn":
                    if row[1] == "earn_adv":    # 收入的 intent 名稱
                        totalMoney += int(row[2])

                # 支出        
                elif condition == "cost":
                    if row[1] == "spend_adv":   # 支出的 intent 名稱
                        totalMoney += int(row[2])

                            
                # 總額
                elif condition == "all":
                    if row[1] == "earn_adv":    # 收入的 intent 名稱
                        totalMoney += int(row[2])
                    elif row[1] == "spend_adv":   # 支出的 intent 名稱
                        totalMoney -= int(row[2])
                
                # error
                else:
                    return "error"
                
            # 沒有時間條件，直接計算
            else:
                # 收入
                if condition == "earn":
                    if row[1] == "earn_adv":    # 收入的 intent 名稱
                        totalMoney += int(row[2])

                # 支出        
                elif condition == "cost":
                    if row[1] == "spend_adv":   # 支出的 intent 名稱
                        totalMoney += int(row[2])

                            
                # 總額
                elif condition == "all":
                    if row[1] == "earn_adv":    # 收入的 intent 名稱
                        totalMoney += int(row[2])
                    elif row[1] == "spend_adv":   # 支出的 intent 名稱
                        totalMoney -= int(row[2])
                
                # error
                else:
                    return "error"
        return totalMoney


"""
從 LOKI API 得到符合意圖的 regex
並使用 Articut 處理斷詞結果拿到參數
參考：https://api.droidtown.co/document/?python#Loki_7
"""
def GetAdvArgs(inputSTR, rePAT, groupIndexLIST):
    # 把對應的 regex 先編譯
    pat = re.compile(rePAT)

    # 將輸入丟進 articut 斷詞
    articut = Articut(account, articut_key, level="lv2")
    articutResultDICT = articut.parse(inputSTR, userDefinedDictFILE="./intent/USER_DEFINED.json")

    # 將輸入用 re 比較
    patGroups = re.search(pat, articutResultDICT["result_pos"][0])
    args = []
    
    # for i in articutResultDICT["result_pos"]:
    #     print(i)

    # 把我們要的參數拿出來
    try:
        for i in groupIndexLIST:
            args.append(patGroups.group(i))
        return (True, args)
    # 在拿取參數的過程中發生錯誤
    except:
        return (False, "")



