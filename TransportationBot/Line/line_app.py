#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
$ pip3 install flask
"""

import datetime
dt = datetime.datetime
from flask import Flask
from flask import request
from flask import jsonify
import json
from line_sdk import Linebot
import logging
from ref_data import stationLIST, animalLIST, TaiwanLIST, AroundLIST, BeforeLIST, nowLIST, AfterLIST
import time
from TransportationBot import runLoki

LINE_ACCESS_TOKEN   = "B75494DO0qrlKXCfNrGZwbw1PcTdF4AB9Y7J7qHhajML3G+KGZ6RS5D2MrvomkqqBecqbzGV2b8SHkZ+q1ACLdqwuiDfH083Drm0xBJ+JAzpqPp5ybC1lRFhNeryfRp7szU79BjZV0DNLOPoI0Dh6wdB04t89/1O/w1cDnyilFU="
LINE_CHANNEL_SECRET = "a4a04fd9bddfdf479b24ac4a5f07e998"

app = Flask(__name__)
def deleter(input_STR):
    for before in BeforeLIST:
        input_STR = input_STR.replace(before, "")
    for after in AfterLIST:
        input_STR = input_STR.replace(after, "")
    for around in AroundLIST:
        input_STR = input_STR.replace(around, "")
    return input_STR
def loadJson(filename):
    with open(filename,"r") as f:
        result = json.load(f)
    return result
def ticketTime(message): 
    inputLIST = [message]
    resultDICT = runLoki(inputLIST)
    departure = resultDICT['departure'] #str
    destination = resultDICT['destination'] #str
    if 'departure_time' in resultDICT:
        logging.debug('departure time in resultDICT')
        time = resultDICT['departure_time']
    elif 'destination_time' in resultDICT:
        logging.debug('destination time in resultDICT')
        time = resultDICT['destination_time'] #check if the time is correctly put in resultDICT
    else:
        logging.debug('Take the present time')
        time = dt.now().strftime('%H:%M')
    dtMessageTime = dt.strptime(time, "%H:%M") #datetime object
    departureTimeList=list()
    timeTable = loadJson("THSR_timetable.json") #DICT
    for station in stationLIST:
        if departure == station['stationName']:
            logging.debug('Departure sequence = 0 recorded')
            departureSeq = station['stationSeq'] #Normally departureSequence & destinationSeq will be object of integer
        if destination == station['stationName']:
            logging.debug('destination sequence recorded')
            destinationSeq = station['stationSeq']
    if departureSeq < destinationSeq: 
        # check if it's going north or south. 
        # While departureSeq < destinationSeq, then it's going south.
        direction = 0
        for trainSchedule in timeTable:
            if direction == trainSchedule['GeneralTimetable']['GeneralTrainInfo']['Direction']: # Check json
                logging.debug('direction checked')
                for trainStop in trainSchedule['GeneralTimetable']['StopTimes']:
                    if departure == trainStop['StationName']['Zh_tw']:
                        logging.debug('departure name checked')
                        if 'DepartureTime' in trainStop:
                            dtDepartureTime = dt.strptime(trainStop['DepartureTime'], "%H:%M")
                            if dtDepartureTime > dtMessageTime:
                                departureTime = dt.strftime(dtDepartureTime, "%H:%M")
                                departureTimeList.append(departureTime) 
    if departureSeq > destinationSeq:
        # While departureSeq < destinationSeq, then it's going south.
        direction = 1
        for trainSchedule in timeTable:
            if direction == trainSchedule['GeneralTimetable']['GeneralTrainInfo']['Direction']: #check json
                logging.debug('direction = 1 checked')
                for trainStop in trainSchedule['GeneralTimetable']['StopTimes']:
                    if departure == trainStop['StationName']['Zh_tw']:
                        logging.debug('destination name checked')
                        if 'DepartureTime' in trainStop:
                            dtDepartureTime = dt.strptime(trainStop['DepartureTime'], "%H:%M")
                            if dtDepartureTime > dtMessageTime:
                                departureTime = dt.strftime(dtDepartureTime, "%H:%M")
                                departureTimeList.append(departureTime)                            
    departureTimeList.sort()
    return "以下是您指定時間可搭乘最接近的班次時間： {}".format(departureTimeList[0])
def ticketTimeAround(message): 
    inputLIST = [message]
    resultDICT = runLoki(inputLIST)
    departure = resultDICT['departure'] #str
    destination = resultDICT['destination'] #str
    if 'departure_time' in resultDICT:
        logging.debug('departure time in resultDICT')
        time = resultDICT['departure_time']
    elif 'destination_time' in resultDICT:
        logging.debug('destination time in resultDICT')
        time = resultDICT['destination_time'] #check if the time is correctly put in resultDICT
    else:
        logging.debug('Take the present time')
        time = dt.now().strftime('%H:%M')
    dtMessageTime = dt.strptime(time, "%H:%M") #datetime object
    messageTimeAround = dt.strftime(dtMessageTime + datetime.timedelta(hours=-1), "%H:%M")
    dtMessageTimeAround = dt.strptime(messageTimeAround,"%H:%M")    
    departureTimeList = list()
    departureTimeAroundList = list()
    timeTable = loadJson("THSR_timetable.json") #DICT
    for station in stationLIST:
        if departure == station['stationName']:
            logging.debug('Departure sequence = 0 recorded')
            departureSeq = station['stationSeq'] #Normally departureSequence & destinationSeq will be object of integer
        if destination == station['stationName']:
            logging.debug('destination sequence recorded')
            destinationSeq = station['stationSeq']
    if departureSeq < destinationSeq: 
        # check if it's going north or south. 
        # While departureSeq < destinationSeq, then it's going south.
        direction = 0
        for trainSchedule in timeTable:
            if direction == trainSchedule['GeneralTimetable']['GeneralTrainInfo']['Direction']: # Check json
                logging.debug('direction checked')
                for trainStop in trainSchedule['GeneralTimetable']['StopTimes']:
                    if departure == trainStop['StationName']['Zh_tw']:
                        logging.debug('departure name checked')
                        if 'DepartureTime' in trainStop:
                            dtDepartureTime = dt.strptime(trainStop['DepartureTime'], "%H:%M") # convert to datetime format
                            if dtDepartureTime > dtMessageTime:
                                departureTime = dt.strftime(dtDepartureTime, "%H:%M") # convert to string format
                                departureTimeList.append(departureTime)
                            if dtDepartureTime > dtMessageTimeAround and dtDepartureTime < dtMessageTime:
                                departureTimeAround = dt.strftime(dtDepartureTime, "%H:%M")
                                departureTimeAroundList.append(departureTimeAround)
    if departureSeq > destinationSeq:
        # While departureSeq < destinationSeq, then it's going south.
        direction = 1
        for trainSchedule in timeTable:
            if direction == trainSchedule['GeneralTimetable']['GeneralTrainInfo']['Direction']: #check json
                logging.debug('direction = 1 checked')
                for trainStop in trainSchedule['GeneralTimetable']['StopTimes']:
                    if departure == trainStop['StationName']['Zh_tw']:
                        logging.debug('destination name checked')
                        if 'DepartureTime' in trainStop:
                            dtDepartureTime = dt.strptime(trainStop['DepartureTime'], "%H:%M")
                            if dtDepartureTime > dtMessageTime:
                                departureTime = dt.strftime(dtDepartureTime, "%H:%M")
                                departureTimeList.append(departureTime)
                            if dtDepartureTime > dtMessageTimeAround and dtDepartureTime < dtMessageTime:
                                departureTimeAround = dt.strftime(dtDepartureTime, "%H:%M")
                                departureTimeAroundList.append(departureTimeAround)                            
    departureTimeList.sort()
    departureTimeAroundList.sort(reverse = True)
    return "以下是您{}附近可搭乘的班次時間：{} 以及 {}".format(resultDICT['departure_time'], departureTimeList[0], departureTimeAroundList[0])
def ticketTimeBefore(message): 
    inputLIST = [message]
    resultDICT = runLoki(inputLIST)
    departure = resultDICT['departure'] #str
    destination = resultDICT['destination'] #str
    if 'departure_time' in resultDICT:
        logging.debug('departure time in resultDICT')
        time = resultDICT['departure_time']
    elif 'destination_time' in resultDICT:
        logging.debug('destination time in resultDICT')
        time = resultDICT['destination_time'] #check if the time is correctly put in resultDICT
    else:
        logging.debug('Take the present time')
        time = dt.now().strftime('%H:%M')
    dtMessageTime = dt.strptime(time, "%H:%M") #datetime object
    departureTimeList = list()
    timeTable = loadJson("THSR_timetable.json") #DICT
    for station in stationLIST:
        if departure == station['stationName']:
            logging.debug('Departure sequence = 0 recorded')
            departureSeq = station['stationSeq'] #Normally departureSequence & destinationSeq will be object of integer
        if destination == station['stationName']:
            logging.debug('destination sequence recorded')
            destinationSeq = station['stationSeq']
    if departureSeq < destinationSeq: 
        # check if it's going north or south. 
        # While departureSeq < destinationSeq, then it's going south.
        direction = 0
        for trainSchedule in timeTable:
            if direction == trainSchedule['GeneralTimetable']['GeneralTrainInfo']['Direction']: # Check json
                logging.debug('direction checked')
                for trainStop in trainSchedule['GeneralTimetable']['StopTimes']:
                    if departure == trainStop['StationName']['Zh_tw']:
                        logging.debug('departure name checked')
                        if 'DepartureTime' in trainStop:
                            dtDepartureTime = dt.strptime(trainStop['DepartureTime'], "%H:%M") # convert to datetime format
                            if dtDepartureTime < dtMessageTime:
                                departureTime = dt.strftime(dtDepartureTime, "%H:%M") # convert to string format
                                departureTimeList.append(departureTime)
    if departureSeq > destinationSeq:
        # While departureSeq < destinationSeq, then it's going south.
        direction = 1
        for trainSchedule in timeTable:
            if direction == trainSchedule['GeneralTimetable']['GeneralTrainInfo']['Direction']: #check json
                logging.debug('direction = 1 checked')
                for trainStop in trainSchedule['GeneralTimetable']['StopTimes']:
                    if departure == trainStop['StationName']['Zh_tw']:
                        logging.debug('destination name checked')
                        if 'DepartureTime' in trainStop:
                            dtDepartureTime = dt.strptime(trainStop['DepartureTime'], "%H:%M")
                            if dtDepartureTime < dtMessageTime:
                                departureTime = dt.strftime(dtDepartureTime, "%H:%M")
                                departureTimeList.append(departureTime)                       
    departureTimeList.sort(reverse = True)
    print(departureTimeList)
    if len(departureTimeList) == 0:
        return "糟糕，已經沒有班次了，趕快去搭台鐵，或是找飯店吧！"
    else:
        return "以下是您{}之前可搭乘的班次時間：{}".format(resultDICT['departure_time'], departureTimeList[0])
def ticketPrice(message):
    inputLIST = [message]
    resultDICT = runLoki(inputLIST)
    departure = resultDICT['departure']
    destination = resultDICT['destination']
    if 'adultAmount' in resultDICT:
        logging.debug('adult exist')
        adultAmount = resultDICT['adultAmount']
    else:
        logging.debug('no adult')
        adultAmount = 0
    if 'childrenAmount' in resultDICT:
        logging.debug('children exist')
        childrenAmount = resultDICT['childrenAmount']
    else:
        logging.debug('no children')
        childrenAmount = 0
    priceInfo = loadJson('THSR_ticketPrice.json') #DICT
    for i in priceInfo:
        if departure == i['OriginStationName']['Zh_tw'] and destination == i['DestinationStationName']['Zh_tw']:
            logging.debug('station name match')
            for fareType in i['Fares']:
                if fareType['TicketType'] == "標準":
                    logging.debug('standard detected')
                    adultPrice = fareType['Price']
                    childrenPrice = 0.5*adultPrice
    totalPrice = str(adultAmount*adultPrice + childrenAmount*childrenPrice)
    totalAmount = adultAmount + childrenAmount
    totalPrice = totalPrice.rstrip('0').rstrip('.')
    return "從{}到{}的{}張標準座位總共是{}元喔".format(departure, destination, totalAmount, totalPrice)
def ticketPriceBusiness(message):
    inputLIST = [message]
    resultDICT = runLoki(inputLIST)
    departure = resultDICT['departure']
    destination = resultDICT['destination']
    if 'adultAmount' in resultDICT:
        adultAmount = resultDICT['adultAmount']
        logging.debug('adult exist')
    else:
        logging.debug('no adult')
        adultAmount = 0
    if 'childrenAmount' in resultDICT:
        logging.debug('children exist')
        childrenAmount = resultDICT['childrenAmount']
    else:
        logging.debug('no children')
        childrenAmount = 0
    priceInfo = loadJson('THSR_ticketPrice.json') #DICT
    for i in priceInfo:
        if departure == i['OriginStationName']['Zh_tw'] and destination == i['DestinationStationName']['Zh_tw']:
            for fareType in i['Fares']:
                if fareType['TicketType'] == "商務":
                    adultPrice = fareType['Price']
                    childrenPrice = 0.5*adultPrice
    totalPrice = str(adultAmount*adultPrice + childrenAmount*childrenPrice)
    totalAmount = adultAmount + childrenAmount
    totalPrice = totalPrice.rstrip('0').rstrip('.')
    return "從{}到{}的{}張商務艙總共是{}元喔".format(departure, destination, totalAmount, totalPrice)
def ticketPriceFree(message):
    inputLIST = [message]
    resultDICT = runLoki(inputLIST)
    departure = resultDICT['departure']
    destination = resultDICT['destination']
    if 'adultAmount' in resultDICT:
        logging.debug('adult exist')
        adultAmount = resultDICT['adultAmount']
    else:
        logging.debug('no adult')
        adultAmount = 0
    if 'childrenAmount' in resultDICT:
        logging.debug('children exist')
        childrenAmount = resultDICT['childrenAmount']
    else:
        logging.debug('no children')
        childrenAmount = 0
    priceInfo = loadJson('THSR_ticketPrice.json') #DICT
    for i in priceInfo:
        if departure == i['OriginStationName']['Zh_tw'] and destination == i['DestinationStationName']['Zh_tw']:
            for fareType in i['Fares']:
                if fareType['TicketType'] == "自由":
                    adultPrice = fareType['Price']
                    if adultPrice % 2 != 0:
                        childrenPrice = 0.5 * adultPrice - 2.5
                    else:
                        childrenPrice = 0.5 * adultPrice
    totalPrice = str(adultAmount*adultPrice + childrenAmount*childrenPrice)
    totalAmount = adultAmount + childrenAmount
    totalPrice = totalPrice.rstrip('0').rstrip('.')
    return "從{}到{}的{}張自由座總共是{}元喔".format(departure, destination, totalAmount, totalPrice)


@app.route("/Milano/", methods=["GET", "POST"])
def webhook():
    # GET
    if request.method == "GET":
        return jsonify({"status": True, "msg": "Line Webhook Success."})

    # POST
    elif request.method == "POST":
        body = request.get_data(as_text=True)
        signature = request.headers["X-Line-Signature"] #解密

        # Line
        linebot = Linebot(LINE_ACCESS_TOKEN, LINE_CHANNEL_SECRET)

        # dataLIST = [{status, type, message, userID, replyToken, timestamp}] #送上來的東西
        dataLIST = linebot.parse(body, signature)
        for dataDICT in dataLIST:
            if dataDICT["status"]:
                if dataDICT["type"] == "message": #若回應訊息類別是訊息（or sticker）
                    # Send Message // replyToken是確認聊天室
                    if dataDICT["message"] == '出來':
                        linebot.respText(dataDICT["replyToken"], "若想「查詢票價」，請告訴我您要從哪裡到哪裡，共有幾個大人幾個小孩?\n（若您有特殊需求，請在輸入時註明「商務」或「自由」，謝謝。）\n若想「查詢班次」，請告訴我您什麼時候要從哪裡出發到哪裡?") #回應的內容
                        return
                    if dataDICT["message"] == '謝謝':
                        linebot.respText(dataDICT["replyToken"], "期待下次再幫你忙喔！")
                    #token是確認不要回應錯
                    #傳送在Line裡的句子是存在dataDICT["message"]裡
                    #response = message(dataDICT["message"])
                    #linebot.respText(dataDICT["replyToken"], response)
                    #message()的回應是runLoki return回來的訊息
                    else:
                        inputSTR = deleter(dataDICT["message"])
                        inputLIST = [inputSTR]
                        resultDICT = runLoki(inputLIST)
                        if set(animalLIST).intersection(set(inputSTR)):
                            linebot.respText(dataDICT["replyToken"], "原則上高鐵不允許帶攜帶動物進入，但如果您要攜帶寵物上高鐵的話，請您要確認高鐵公司已同意其為不妨害公共安全的動物，且完固包裝於長、寬、高尺寸小於 55 公分、45公分、38公分之容器內，無糞便、液體漏出之虞。")
                        if 'adultAmount' in resultDICT or 'childrenAmount' in resultDICT:
                            if '商務' in inputSTR:
                                paxDICT = {"station": {"departure": "", "destination": ""}, "adultAmount": 0, "childrenAmount": 0}
                                if 'departure' in resultDICT:
                                    paxDICT['station']['departure'] = resultDICT['departure']
                                if 'destination' in resultDICT:
                                    paxDICT['station']['destination'] = resultDICT['destination']
                                if 'adultAmount' in resultDICT:
                                    paxDICT['adultAmount'] = resultDICT['adultAmount']
                                if 'childrenAmount' in resultDICT:
                                    paxDICT['childrenAmount'] = resultDICT['childrenAmount']
                                if paxDICT['station']['departure'] == "高雄" or paxDICT['station']['destination'] == "高雄":
                                    response = "高鐵沒有高雄站只有左營站喔"
                                    linebot.respText(dataDICT["replyToken"], response)
                                    return
                                if paxDICT['station']['departure'] == "":
                                    response = "要記得說你從哪出發，還有要去哪裡喔！"
                                    linebot.respText(dataDICT["replyToken"], response)                        
                                    return
                                if paxDICT['station']['destination'] == "":
                                    response = "要記得說你要去哪裡喔！"
                                    linebot.respText(dataDICT["replyToken"], response)
                                    return
                                if paxDICT['adultAmount'] == 0 and paxDICT['childrenAmount'] == 0:
                                    response = "有幾位大人幾位小孩要記得說喔！"
                                    linebot.respText(dataDICT["replyToken"], response)                        
                                    return
                                if paxDICT['station']['departure'] == paxDICT['station']['destination']:
                                    response = "呃，你已經在目的地了喔！"
                                    linebot.respText(dataDICT["replyToken"], response)
                                    return
                                if paxDICT['station']['departure'] not in TaiwanLIST or paxDICT['station']['destination'] not in TaiwanLIST:
                                    if paxDICT['station']['departure'] not in TaiwanLIST:
                                        departure = paxDICT['station']['departure']
                                        response = "高鐵目前在{}沒有站喔！".format(departure)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                                    elif paxDICT['station']['destination'] not in TaiwanLIST:
                                        destination = paxDICT['station']['destination']
                                        response = "高鐵目前在{}沒有站喔！".format(destination)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                                    else:
                                        departure = paxDICT['station']['departure']
                                        destination = paxDICT['station']['destination']
                                        response = "高鐵目前在{}跟{}都沒有站喔！".format(departure, destination)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                                print(resultDICT)
                                linebot.respText(dataDICT["replyToken"], ticketPriceBusiness(inputSTR))
                                del paxDICT
                            elif '自由' in inputSTR:
                                paxDICT = {"station": {"departure": "", "destination": ""}, "adultAmount": 0, "childrenAmount": 0}
                                if 'departure' in resultDICT:
                                    paxDICT['station']['departure'] = resultDICT['departure']
                                if 'destination' in resultDICT:
                                    paxDICT['station']['destination'] = resultDICT['destination']
                                if 'adultAmount' in resultDICT:
                                    paxDICT['adultAmount'] = resultDICT['adultAmount']
                                if 'childrenAmount' in resultDICT:
                                    paxDICT['childrenAmount'] = resultDICT['childrenAmount']
                                if paxDICT['station']['departure'] == "高雄" or paxDICT['station']['destination'] == "高雄":
                                    response = "高鐵沒有高雄站只有左營站喔"
                                    linebot.respText(dataDICT["replyToken"], response)
                                    return
                                if paxDICT['station']['departure'] == "":
                                    response = "要記得說你從哪出發，還有要去哪裡喔！"
                                    linebot.respText(dataDICT["replyToken"], response)                        
                                    return
                                if paxDICT['station']['destination'] == "":
                                    response = "要記得說你要去哪裡喔！"
                                    linebot.respText(dataDICT["replyToken"], response)
                                    return
                                if paxDICT['adultAmount'] == 0 and paxDICT['childrenAmount'] == 0:
                                    response = "有幾位大人幾位小孩要記得說喔！"
                                    linebot.respText(dataDICT["replyToken"], response)                        
                                    return
                                if paxDICT['station']['departure'] == paxDICT['station']['destination']:
                                    response = "呃，你已經在目的地了喔！"
                                    linebot.respText(dataDICT["replyToken"], response)
                                    return
                                if paxDICT['station']['departure'] not in TaiwanLIST or paxDICT['station']['destination'] not in TaiwanLIST:
                                    if paxDICT['station']['departure'] not in TaiwanLIST:
                                        departure = paxDICT['station']['departure']
                                        response = "高鐵目前在{}沒有站喔！".format(departure)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                                    elif paxDICT['station']['destination'] not in TaiwanLIST:
                                        destination = paxDICT['station']['destination']
                                        response = "高鐵目前在{}沒有站喔！".format(destination)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                                    else:
                                        departure = paxDICT['station']['departure']
                                        destination = paxDICT['station']['destination']
                                        response = "高鐵目前在{}跟{}都沒有站喔！".format(departure, destination)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                                print(resultDICT)
                                linebot.respText(dataDICT["replyToken"], ticketPriceFree(inputSTR))
                                del paxDICT
                            else: #'標準'
                                paxDICT = {"station": {"departure": "", "destination": ""}, "adultAmount": 0, "childrenAmount": 0}
                                if 'departure' in resultDICT:
                                    paxDICT['station']['departure'] = resultDICT['departure']
                                if 'destination' in resultDICT:
                                    paxDICT['station']['destination'] = resultDICT['destination']
                                if 'adultAmount' in resultDICT:
                                    paxDICT['adultAmount'] = resultDICT['adultAmount']
                                if 'childrenAmount' in resultDICT:
                                    paxDICT['childrenAmount'] = resultDICT['childrenAmount']
                                if paxDICT['station']['departure'] == "高雄" or paxDICT['station']['destination'] == "高雄":
                                    response = "高鐵沒有高雄站只有左營站喔"
                                    linebot.respText(dataDICT["replyToken"], response)
                                    return
                                if paxDICT['station']['departure'] == "":
                                    response = "要記得說你從哪出發，還有要去哪裡喔！"
                                    linebot.respText(dataDICT["replyToken"], response)                        
                                    return
                                if paxDICT['station']['destination'] == "":
                                    response = "要記得說你要去哪裡喔！"
                                    linebot.respText(dataDICT["replyToken"], response)
                                    return
                                if paxDICT['adultAmount'] == 0 and paxDICT['childrenAmount'] == 0:
                                    response = "有幾位大人幾位小孩要記得說喔！"
                                    linebot.respText(dataDICT["replyToken"], response)                        
                                    return
                                if paxDICT['station']['departure'] == paxDICT['station']['destination']:
                                    response = "呃，你已經在目的地了喔！"
                                    linebot.respText(dataDICT["replyToken"], response)
                                    return
                                if paxDICT['station']['departure'] not in TaiwanLIST or paxDICT['station']['destination'] not in TaiwanLIST:
                                    if paxDICT['station']['departure'] not in TaiwanLIST:
                                        departure = paxDICT['station']['departure']
                                        response = "高鐵目前在{}沒有站喔！".format(departure)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                                    elif paxDICT['station']['destination'] not in TaiwanLIST:
                                        destination = paxDICT['station']['destination']
                                        response = "高鐵目前在{}沒有站喔！".format(destination)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                                    else:
                                        departure = paxDICT['station']['departure']
                                        destination = paxDICT['station']['destination']
                                        response = "高鐵目前在{}跟{}都沒有站喔！".format(departure, destination)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                                print(resultDICT)
                                linebot.respText(dataDICT["replyToken"], ticketPrice(inputSTR))
                                del paxDICT
                        elif bool([n for n in nowLIST if n in dataDICT["message"]]): #現在時間
                            paxDICT = {"station": {"departure": "", "destination": ""}}
                            if 'departure' in resultDICT:
                                paxDICT['station']['departure'] = resultDICT['departure']
                            if 'destination' in resultDICT:
                                paxDICT['station']['destination'] = resultDICT['destination']
                            if 'departure_time' in resultDICT:
                                paxDICT['departure_time'] = resultDICT['departure_time']
                            if paxDICT['station']['departure'] == "高雄" or paxDICT['station']['destination'] == "高雄":
                                response = "高鐵沒有高雄站只有左營站喔"
                                linebot.respText(dataDICT["replyToken"], response)
                                return
                            if paxDICT['station']['departure'] == "":
                                response = "要記得說你從哪出發，還有要去哪裡喔！"
                                linebot.respText(dataDICT["replyToken"], response)                        
                                return
                            if paxDICT['station']['destination'] == "":
                                response = "要記得說你要去哪裡喔！"
                                linebot.respText(dataDICT["replyToken"], response)
                                return
                            if paxDICT['station']['departure'] == paxDICT['station']['destination']:
                                response = "呃，你已經在目的地了喔！"
                                linebot.respText(dataDICT["replyToken"], response)
                                return
                            if paxDICT['station']['departure'] not in TaiwanLIST or paxDICT['station']['destination'] not in TaiwanLIST:
                                    if paxDICT['station']['departure'] not in TaiwanLIST:
                                        departure = paxDICT['station']['departure']
                                        response = "高鐵目前在{}沒有站喔！".format(departure)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                                    elif paxDICT['station']['destination'] not in TaiwanLIST:
                                        destination = paxDICT['station']['destination']
                                        response = "高鐵目前在{}沒有站喔！".format(destination)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                                    else:
                                        departure = paxDICT['station']['departure']
                                        destination = paxDICT['station']['destination']
                                        response = "高鐵目前在{}跟{}都沒有站喔！".format(departure, destination)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                            print(resultDICT)
                            linebot.respText(dataDICT["replyToken"], ticketTime(inputSTR))
                            del paxDICT
                        elif bool([a for a in AroundLIST if a in dataDICT["message"]]): # 時間附近
                            paxDICT = {"departure_time": "", "station": {"departure": "", "destination": ""}}
                            if 'departure' in resultDICT:
                                paxDICT['station']['departure'] = resultDICT['departure']
                            if 'destination' in resultDICT:
                                paxDICT['station']['destination'] = resultDICT['destination']
                            if 'departure_time' in resultDICT:
                                paxDICT['departure_time'] = resultDICT['departure_time']
                            if paxDICT['station']['departure'] == "高雄" or paxDICT['station']['destination'] == "高雄":
                                response = "高鐵沒有高雄站只有左營站喔"
                                linebot.respText(dataDICT["replyToken"], response)
                                return
                            if paxDICT['station']['departure'] == "":
                                response = "要記得說你從哪出發，還有要去哪裡喔！"
                                linebot.respText(dataDICT["replyToken"], response)                        
                                return
                            if paxDICT['station']['destination'] == "":
                                response = "要記得說你要去哪裡喔！"
                                linebot.respText(dataDICT["replyToken"], response)
                                return
                            if paxDICT['station']['departure'] == paxDICT['station']['destination']:
                                response = "呃，你已經在目的地了喔！"
                                linebot.respText(dataDICT["replyToken"], response)
                                return
                            if paxDICT['station']['departure'] not in TaiwanLIST or paxDICT['station']['destination'] not in TaiwanLIST:
                                    if paxDICT['station']['departure'] not in TaiwanLIST:
                                        departure = paxDICT['station']['departure']
                                        response = "高鐵目前在{}沒有站喔！".format(departure)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                                    elif paxDICT['station']['destination'] not in TaiwanLIST:
                                        destination = paxDICT['station']['destination']
                                        response = "高鐵目前在{}沒有站喔！".format(destination)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                                    else:
                                        departure = paxDICT['station']['departure']
                                        destination = paxDICT['station']['destination']
                                        response = "高鐵目前在{}跟{}都沒有站喔！".format(departure, destination)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                            print(resultDICT)
                            linebot.respText(dataDICT["replyToken"], ticketTimeAround(inputSTR))
                            del paxDICT
                        elif bool([b for b in BeforeLIST if b in dataDICT["message"]]): # 時間之前
                            paxDICT = {"departure_time": "", "station": {"departure": "", "destination": ""}}
                            if 'departure' in resultDICT:
                                paxDICT['station']['departure'] = resultDICT['departure']
                            if 'destination' in resultDICT:
                                paxDICT['station']['destination'] = resultDICT['destination']
                            if 'departure_time' in resultDICT:
                                paxDICT['departure_time'] = resultDICT['departure_time']
                            if paxDICT['station']['departure'] == "高雄" or paxDICT['station']['destination'] == "高雄":
                                response = "高鐵沒有高雄站只有左營站喔"
                                linebot.respText(dataDICT["replyToken"], response)
                                return
                            if paxDICT['station']['departure'] == "":
                                response = "要記得說你從哪出發，還有要去哪裡喔！"
                                linebot.respText(dataDICT["replyToken"], response)                        
                                return
                            if paxDICT['station']['destination'] == "":
                                response = "要記得說你要去哪裡喔！"
                                linebot.respText(dataDICT["replyToken"], response)
                                return
                            if paxDICT['station']['departure'] == paxDICT['station']['destination']:
                                response = "呃，你已經在目的地了喔！"
                                linebot.respText(dataDICT["replyToken"], response)
                                return
                            if paxDICT['station']['departure'] not in TaiwanLIST or paxDICT['station']['destination'] not in TaiwanLIST:
                                    if paxDICT['station']['departure'] not in TaiwanLIST:
                                        departure = paxDICT['station']['departure']
                                        response = "高鐵目前在{}沒有站喔！".format(departure)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                                    elif paxDICT['station']['destination'] not in TaiwanLIST:
                                        destination = paxDICT['station']['destination']
                                        response = "高鐵目前在{}沒有站喔！".format(destination)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                                    else:
                                        departure = paxDICT['station']['departure']
                                        destination = paxDICT['station']['destination']
                                        response = "高鐵目前在{}跟{}都沒有站喔！".format(departure, destination)
                                        linebot.respText(dataDICT["replyToken"], response)
                                        return
                            print(resultDICT)
                            linebot.respText(dataDICT["replyToken"], ticketTimeBefore(inputSTR))
                            del paxDICT                      
                        else: # 時間之後
                            paxDICT = {"departure_time": "", "station": {"departure": "", "destination": ""}}
                            if 'departure' in resultDICT:
                                paxDICT['station']['departure'] = resultDICT['departure']
                            if 'destination' in resultDICT:
                                paxDICT['station']['destination'] = resultDICT['destination']
                            if 'departure_time' in resultDICT:
                                paxDICT['departure_time'] = resultDICT['departure_time']
                            if paxDICT['station']['departure'] == "高雄" or paxDICT['station']['destination'] == "高雄":
                                response = "高鐵沒有高雄站只有左營站喔"
                                linebot.respText(dataDICT["replyToken"], response)
                                return
                            if paxDICT['station']['departure'] == "":
                                response = "要記得說你從哪出發，還有要去哪裡喔！"
                                linebot.respText(dataDICT["replyToken"], response)                        
                                return
                            if paxDICT['station']['destination'] == "":
                                response = "要記得說你要去哪裡喔！"
                                linebot.respText(dataDICT["replyToken"], response)
                                return
                            if paxDICT['station']['departure'] == paxDICT['station']['destination']:
                                response = "呃，你已經在目的地了喔！"
                                linebot.respText(dataDICT["replyToken"], response)
                                return
                            if paxDICT['station']['departure'] not in TaiwanLIST or paxDICT['station']['destination'] not in TaiwanLIST:
                                if paxDICT['station']['departure'] not in TaiwanLIST:
                                    departure = paxDICT['station']['departure']
                                    response = "高鐵目前在{}沒有站喔！".format(departure)
                                    linebot.respText(dataDICT["replyToken"], response)
                                    return
                                elif paxDICT['station']['destination'] not in TaiwanLIST:
                                    destination = paxDICT['station']['destination']
                                    response = "高鐵目前在{}沒有站喔！".format(destination)
                                    linebot.respText(dataDICT["replyToken"], response)
                                    return
                                else:
                                    departure = paxDICT['station']['departure']
                                    destination = paxDICT['station']['destination']
                                    response = "高鐵目前在{}跟{}都沒有站喔！".format(departure, destination)
                                    linebot.respText(dataDICT["replyToken"], response)
                                    return
                            print(resultDICT)
                            linebot.respText(dataDICT["replyToken"], ticketTime(inputSTR))
                            del paxDICT
        return jsonify({"status": True, "msg": "Line Webhook Success."})

    # OTHER
    else:
        return jsonify({"status": False, "msg": "HTTP_405_METHOD_NOT_ALLOWED"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8003)
