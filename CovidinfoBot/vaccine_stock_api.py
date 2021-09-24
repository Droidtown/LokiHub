#!/usr/bin/env python
# -*- coding:utf-8 -*-
import covid_info_bot
import requests
import json
import pandas as pd
from pprint import pprint
import datetime as dt

vaccine_stock_url = 'https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=2001'
'''
{"id":"ID",
"a01":"日期",
"a02":"縣市別",
"a03":"總人口數",
"a04":"新增接種人次",
"a05":"累計接種人次",
"a06":"疫苗覆蓋率 (%)",
"a07":"累計配送量 (劑)",
"a08":"剩餘量 (劑)",
"a09":"剩餘量 (%)",
"a10":"AZ新增接種人次",
"a11":"AZ累計接種人次",
"a12":"AZ疫苗覆蓋率 (%)",
"a13":"AZ累計配送量 (劑)",
"a14":"AZ剩餘量 (劑)",
"a15":"AZ剩餘量 (%)",
"a16":"Moderna新增接種人次",
"a17":"Moderna累計接種人次",
"a18":"Moderna疫苗覆蓋率 (%)",
"a19":"Moderna累計配送量 (劑)"
"a20":"Moderna剩餘量 (劑)",
"a21":"Moderna剩餘量 (%)"}
'''

vaccine_stock = requests.get(url = vaccine_stock_url, verify=True)
vaccine_stock_rawDF = pd.DataFrame(vaccine_stock.json())
vaccine_stockDF = vaccine_stock_rawDF[['a01','a02','a08','a14','a20']]
vaccine_stockDF = vaccine_stockDF.loc[vaccine_stockDF.a01==vaccine_stockDF.a01[0]]
vaccine_stockDF.columns = ['date','location','all','AZ','Moderna']
#vaccine_stockDICT = json.loads()


def write_response(inputDICT):
    '''
    inputDICT

    outputDICT
    outputSTR
    
    '''
    outputSTR = ""
    vaccineStockTemplate = {
        'vaccine_shot': "",
        'location': ""
    }
    outputDICT = {}
    #try:
    if inputDICT["vaccine_shot"] != [] and inputDICT["location"] != []:
        for i in range(len(inputDICT["vaccine_shot"])):
            if inputDICT["vaccine_shot"][i] == "all":
                outputSTR += "目前還沒有統計全部疫苗的功能"
            outputDICT["date"] = dt.datetime.strptime(set(vaccine_stockDF['date'].values).pop(),"%Y-%m-%d")
            outputDICT["vaccine_shot"] = inputDICT["vaccine_shot"][i] 
            outputDICT["location"] = inputDICT['location'][i]
            outputDICT["quantity"] = vaccine_stockDF[vaccine_stockDF.location == inputDICT['location'][i]][outputDICT["vaccine_shot"]].values[0]
            outputSTR += """{}年{}月{}日為止, {} 疫苗在{}還有{}劑庫存。\n""".format(outputDICT["date"].year,outputDICT["date"].month,outputDICT["date"].day,outputDICT["vaccine_shot"],outputDICT["location"],outputDICT["quantity"]).replace("   ", "")
    else:
        outputSTR = "ERROR: number of keys do not match."
    if not outputDICT["vaccine_shot"] and outputSTR == "": outputSTR = "Vaccine type not registered."
    if not outputDICT["location"] and outputSTR == "": outputSTR = "location not registered."
    # except:
    #     print("ERROR: Input String Error.")
    return outputSTR

if __name__ == "__main__":
    inputLIST = ["請問Moderna在台北的庫存？","我要查詢AZ在台中的剩餘量"]
    filterLIST=[]
    loki_result = covid_info_bot.runLoki(inputLIST, filterLIST)
    response = write_response(loki_result)
    print(response)