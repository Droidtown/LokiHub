
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
from requests import post
from requests import codes

def information(symbol):
    URL = "https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID="+ symbol 
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    r = requests.post(url=URL,headers=headers)
    html =BeautifulSoup(r.content, "html.parser")
    
    result_infoDICT = {}
    
    table = html.findAll("table")[40]
    table_row_name=table.findAll("tr")[1]
    td_name = table_row_name.findAll("td")[1]
    name = td_name.text
    result_infoDICT["name"] = name
    
    
    table_row_industry=table.findAll("tr")[2]
    td_industry=table_row_industry.findAll("td")[1]
    industry=td_industry.text
    result_infoDICT["industry"] = industry
    

    table_row_value=table.findAll("tr")[4]
    td_value = table_row_value.findAll("td")[3]
    value = td_value.text
    result_infoDICT["value"] = value    


    table_row_business=table.findAll("tr")[14]
    td_business = table_row_business.findAll("td")[0]
    business = td_business.text
    result_infoDICT["business"] = business    
    
    return result_infoDICT
    

def growth(symbol):
    URL = "https://goodinfo.tw/StockInfo/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID="+ symbol 
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    r = requests.post(url=URL,headers=headers)
    html =BeautifulSoup(r.content, "html.parser")
    
    result_growthDICT = {}
    
    table = html.findAll("table")[16]
    table_row_quarter=table.findAll("tr")[0]
    th_quarter = table_row_quarter.findAll("th")[1]
    quarter = th_quarter.text    
    result_growthDICT["quarter"] = quarter    
    
    table_row_revenue=table.findAll("tr")[14]
    td_revenue = table_row_revenue.findAll("td")[1]
    revenue_YOY = td_revenue.text
    result_growthDICT["revenue_YOY"] = revenue_YOY
    
    table_row_gross_profit = table.findAll("tr")[15]
    td_gross_profit = table_row_gross_profit.findAll("td")[1]
    gross_profit_YOY = td_gross_profit.text
    result_growthDICT["gross_profit_YOY"] = gross_profit_YOY
    

    table_row_operating_income=table.findAll("tr")[16]
    td_operating_income = table_row_operating_income.findAll("td")[1]
    operating_income_YOY = td_operating_income.text
    result_growthDICT["operating_income_YOY"] = operating_income_YOY
    
    table_row_NIBT=table.findAll("tr")[17]
    td_NIBT = table_row_NIBT.findAll("td")[1]
    NIBT_YOY = td_NIBT.text
    result_growthDICT["NIBT_YOY"] = NIBT_YOY

    table_row_NI=table.findAll("tr")[18]
    td_NI = table_row_NI.findAll("td")[1]
    NI_YOY = td_NI.text
    result_growthDICT["NI_YOY"] = NI_YOY
    
    table_row_EPS=table.findAll("tr")[20]
    td_EPS = table_row_EPS.findAll("td")[1]
    EPS_YOY = td_EPS.text
    result_growthDICT["EPS_YOY"] = EPS_YOY
    
    table_row_total_assets_growth=table.findAll("tr")[50]
    td_total_assets_growth = table_row_total_assets_growth.findAll("td")[1]
    total_assets_growth = td_total_assets_growth.text
    result_growthDICT["total_assets_growth"] = total_assets_growth
    
    return result_growthDICT

def profitability(symbol):
    URL = "https://goodinfo.tw/StockInfo/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID="+ symbol 
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    r = requests.post(url=URL,headers=headers)
    html =BeautifulSoup(r.content, "html.parser")
    
    result_profitabilityDICT = {}
    
    table = html.findAll("table")[16]
    table_row_quarter=table.findAll("tr")[0]
    th_quarter = table_row_quarter.findAll("th")[1]
    quarter = th_quarter.text    
    result_profitabilityDICT["quarter"] = quarter
    
    table_row_GPM=table.findAll("tr")[1]
    td_GPM = table_row_GPM.findAll("td")[1]
    GPM = td_GPM.text
    result_profitabilityDICT["GPM"] = GPM
    
   
    table_row_OPM=table.findAll("tr")[2]
    td_OPM = table_row_OPM.findAll("td")[1]
    OPM = td_OPM.text    
    result_profitabilityDICT["OPM"] = OPM
    

    table_row_PTPM=table.findAll("tr")[3]
    td_PTPM = table_row_PTPM.findAll("td")[1]
    PTPM = td_PTPM.text    
    result_profitabilityDICT["PTPM"] = PTPM
    

    table_row_NPM=table.findAll("tr")[4]
    td_NPM = table_row_NPM.findAll("td")[1]
    NPM = td_NPM.text    
    result_profitabilityDICT["NPM"] = NPM

    table_row_EPS=table.findAll("tr")[7]
    td_EPS = table_row_EPS.findAll("td")[1]
    EPS = td_EPS.text    
    result_profitabilityDICT["EPS"] = EPS
    
    table_row_NASPS=table.findAll("tr")[8]
    td_NASPS = table_row_NASPS.findAll("td")[1]
    NASPS = td_NASPS.text    
    result_profitabilityDICT["NASPS"] = NASPS
    
    table_row_ROW=table.findAll("tr")[9]
    td_ROE = table_row_ROW.findAll("td")[1]
    ROE = td_ROE.text    
    result_profitabilityDICT["ROE"] = ROE    
    
    table_row_ROA=table.findAll("tr")[11]
    td_ROA = table_row_ROA.findAll("td")[1]
    ROA = td_ROA.text    
    result_profitabilityDICT["ROA"] = ROA   
    
    return result_profitabilityDICT

def safety(symbol):
    URL = "https://goodinfo.tw/StockInfo/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID="+ symbol 
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    r = requests.post(url=URL,headers=headers)
    html =BeautifulSoup(r.content, "html.parser")
    
    result_safetyDICT = {}
    
    table = html.findAll("table")[16]
    table_row_quarter=table.findAll("tr")[75]
    th_quarter = table_row_quarter.findAll("td")[1]
    quarter = th_quarter.text
    result_safetyDICT["quarter"] = quarter
    
    table_row_CR=table.findAll("tr")[76]
    td_CR = table_row_CR.findAll("td")[1]
    CR = td_CR.text 
    result_safetyDICT["CR"] = CR
    
    table_row_QR=table.findAll("tr")[77]
    td_QR = table_row_QR.findAll("td")[1]
    QR = td_QR.text 
    result_safetyDICT["QR"] = QR    
    
   
    table_row_current_ratio=table.findAll("tr")[78]
    td_current_ratio = table_row_current_ratio.findAll("td")[1]
    current_ratio = td_current_ratio.text 
    result_safetyDICT["current_ratio"] = current_ratio   
    

    table_row_ICR=table.findAll("tr")[79]
    td_ICR = table_row_ICR.findAll("td")[1]
    ICR = td_ICR.text 
    result_safetyDICT["ICR"] = ICR    
    
    table_row_OCFR=table.findAll("tr")[80]
    td_OCFR = table_row_OCFR.findAll("td")[1]
    OCFR = td_OCFR.text 
    result_safetyDICT["OCFR"] = OCFR    

    table_row_DR=table.findAll("tr")[56]
    td_DR = table_row_DR.findAll("td")[1]
    DR = td_DR.text 
    result_safetyDICT["DR"] = DR    

    
    return result_safetyDICT

    
    
    
    
    
    
    
    
    