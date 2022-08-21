import re
import os, sys
import csv

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

