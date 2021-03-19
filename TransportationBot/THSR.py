#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import subprocess
import json

# Windows 須下載 curl 套件
# https://curl.haxx.se/windows/
#CURL_PATH = "D:\Applications\curl\curl-7.67.0-win64-mingw\bin\curl.exe"    # Windows 範例
CURL_PATH = ""  # MacOSX / Linux 留空

def getCurl(curl, url):
    # curl
    resultSTR = subprocess.check_output([curl, "-X", "GET", url]).decode("utf-8")
    resultDICT = json.loads(resultSTR)
    return resultDICT

def getTrainTicketPrice():
    """
    GET /v2/Rail/THSR/ODFare
    取得票價資料
    """
    TrainTicketPriceUrl = "https://ptx.transportdata.tw/MOTC/v2/Rail/THSR/ODFare?$format=JSON"
    resultDICT = getCurl(curl, TrainTicketPriceUrl)
    return resultDICT

def getTimeTable():
    """
    /v2/Rail/THSR/GeneralTimetable
    取得所有車次的定期時刻表資料
    """
    timetableUrl = "https://ptx.transportdata.tw/MOTC/v2/Rail/THSR/GeneralTimetable?$format=JSON"
    resultDICT = getCurl(curl, timetableUrl)
    return resultDICT

if __name__ == "__main__":
    # curl 路徑
    curl = "curl"
    if CURL_PATH != "":
        curl = CURL_PATH

    with open("THRS_ticketPrice.json", "w", encoding = "utf-8") as f:
        result = getTrainTicketPrice()
        json.dump(result, f, ensure_ascii = False)

    with open("THRS_timetable.json", "w", encoding = "utf-8") as f:
        result = getTimeTable()
        json.dump(result, f, ensure_ascii = False)
    