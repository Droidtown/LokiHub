#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import discord
import datetime
dt = datetime.datetime
import json
import logging
from ref_data import stationLIST, animalLIST, TaiwanLIST, AroundLIST, callLIST, byeLIST, nowLIST, AfterLIST, BeforeLIST
from TransportationBot import runLoki
import time

logging.basicConfig(level=logging.DEBUG)

DISCORD_TOKEN=""
DISCORD_GUILD="Droidtown Linguistics Tech."
BOT_NAME = "幫你買票機器人"

# Documention
# https://discordpy.readthedocs.io/en/latest/api.html#client

client = discord.Client()
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
    if len(departureTimeList) == 0:
        return "糟糕，已經沒有班次了，趕快去搭台鐵，或是找飯店吧！"
    else:
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
    if len(departureTimeList) == 0:
        return "糟糕，已經沒有班次了，趕快去搭台鐵，或是找飯店吧！"
    else:
        return "以下是您{}附近可搭乘的班次時間： {} 以及 {}".format(resultDICT['departure_time'], departureTimeList[0], departureTimeAroundList[0])
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
    totalPrice = totalPrice.rstrip('0').rstrip('.')
    totalAmount = adultAmount + childrenAmount
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
    totalPrice = totalPrice.rstrip('0').rstrip('.')
    totalAmount = adultAmount + childrenAmount
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
    totalPrice = totalPrice.rstrip('0').rstrip('.')
    totalAmount = adultAmount + childrenAmount
    return "從{}到{}的{}張自由座總共是{}元喔".format(departure, destination, totalAmount, totalPrice)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == DISCORD_GUILD:
            break
    print(f'{BOT_NAME}bot has connected to Discord!')
    print(f'{guild.name}(id:{guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print("message.content", message.content)
    if "<@!{}>".format(client.user.id) in message.content:
        paxDICT = {}
        client_message = message.content.replace("<@!{}> ".format(client.user.id), "")
        if any (e == client_message for e in callLIST ): # 呼叫
            logging.debug('initiator succeed')
            response = "<@!{}>".format(message.author.id) + "\n若想「查詢票價」，請告訴我您要從哪裡到哪裡，共有幾個大人幾個小孩?\n（若您有特殊需求，請在輸入時註明「商務」或「自由」，謝謝。）\n若想「查詢班次」，請告訴我您什麼時候要從哪裡出發到哪裡?"
            await message.channel.send(response)
            return
        if any (e == client_message for e in byeLIST ): # 結束
            response = "<@!{}>".format(message.author.id) + "祝您旅途愉快！😊"
            await message.channel.send(response)
            return
        else:
            inputSTR = deleter(client_message)
            inputLIST = [inputSTR]
            resultDICT = runLoki(inputLIST)
            if set(animalLIST).intersection(set(inputSTR)):
                response = "<@!{}>".format(message.author.id) + "原則上高鐵不允許帶攜帶動物進入，但如果您要攜帶寵物上高鐵的話，請您要確認高鐵公司已同意其為不妨害公共安全的動物，且完固包裝於長、寬、高尺寸小於 55 公分、45公分、38公分之容器內，無糞便、液體漏出之虞。"
                await message.channel.send(response)
            if 'adultAmount' in resultDICT or 'childrenAmount' in resultDICT: # 票價問題
                if '商務' in message.content: # 商務艙票價
                    logging.debug('business class')
                    if str(message.author.id) not in paxDICT:
                        paxDICT[str(message.author.id)] = {"station": {"departure": "", "destination": ""}, "adultAmount": 0, "childrenAmount": 0}
                    if 'departure' in resultDICT:
                        paxDICT[str(message.author.id)]['station']['departure'] = resultDICT['departure']
                    if 'destination' in resultDICT:
                        paxDICT[str(message.author.id)]['station']['destination'] = resultDICT['destination']
                    if 'adultAmount' in resultDICT:
                        paxDICT[str(message.author.id)]['adultAmount'] = resultDICT['adultAmount']
                    if 'childrenAmount' in resultDICT:
                        paxDICT[str(message.author.id)]['childrenAmount'] = resultDICT['childrenAmount']
                    if paxDICT[str(message.author.id)]['station']['departure'] == "高雄" or paxDICT[str(message.author.id)]['station']['destination'] == "高雄":
                        response = "<@!{}>".format(message.author.id) + "高鐵沒有高雄站只有左營站喔"
                        await message.channel.send(response)
                        return
                    if paxDICT[str(message.author.id)]['station']['departure'] == "":
                        response = "<@!{}>".format(message.author.id) + "要記得說你從哪出發，還有要去哪裡喔！"
                        await message.channel.send(response)
                        return
                    if paxDICT[str(message.author.id)]['station']['destination'] == "":
                        response = "<@!{}>".format(message.author.id) + "要記得說你要去哪裡喔！"
                        await message.channel.send(response)
                        return
                    if paxDICT[str(message.author.id)]['adultAmount'] == 0 and paxDICT[str(message.author.id)]['childrenAmount'] == 0:
                        response = "<@!{}>".format(message.author.id) + "有幾位大人幾位小孩要記得說喔！"
                        await message.channel.send(response)
                        return
                    if paxDICT[str(message.author.id)]['station']['departure'] == paxDICT[str(message.author.id)]['station']['destination']:
                        response = "<@!{}>".format(message.author.id) + "呃，你已經在目的地了喔！"
                        await message.channel.send(response)
                        return
                    if paxDICT[str(message.author.id)]['station']['departure'] not in TaiwanLIST or paxDICT[str(message.author.id)]['station']['destination'] not in TaiwanLIST:
                        if paxDICT[str(message.author.id)]['station']['departure'] not in TaiwanLIST:
                            departure = paxDICT[str(message.author.id)]['station']['departure']
                            response = "<@!{}>".format(message.author.id) + "高鐵目前在{}沒有站喔！".format(departure)
                            await message.channel.send(response)
                            return
                        elif paxDICT[str(message.author.id)]['station']['destination'] not in TaiwanLIST:
                            destination = paxDICT[str(message.author.id)]['station']['destination']
                            response = "<@!{}>".format(message.author.id) + "高鐵目前在{}沒有站喔！".format(destination)
                            await message.channel.send(response)
                            return
                        else:
                            departure = paxDICT[str(message.author.id)]['station']['departure']
                            destination = paxDICT[str(message.author.id)]['station']['destination']
                            response = "<@!{}>".format(message.author.id) + "高鐵目前在{}跟{}都沒有站喔！".format(departure, destination)
                            await message.channel.send(response)
                            return
                    print(resultDICT)
                    response = "<@!{}>".format(message.author.id) + ticketPriceBusiness(inputSTR)
                    await message.channel.send(response)
                    del paxDICT[str(message.author.id)]
                elif '自由' in message.content: # 自由座票價
                    logging.debug('free type')
                    if str(message.author.id) not in paxDICT:
                        paxDICT[str(message.author.id)] = {"station": {"departure": "", "destination": ""}, "adultAmount": 0, "childrenAmount": 0}
                    if 'departure' in resultDICT:
                        paxDICT[str(message.author.id)]['station']['departure'] = resultDICT['departure']
                    if 'destination' in resultDICT:
                        paxDICT[str(message.author.id)]['station']['destination'] = resultDICT['destination']
                    if 'adultAmount' in resultDICT:
                        paxDICT[str(message.author.id)]['adultAmount'] = resultDICT['adultAmount']
                    if 'childrenAmount' in resultDICT:
                        paxDICT[str(message.author.id)]['childrenAmount'] = resultDICT['childrenAmount']
                    if paxDICT[str(message.author.id)]['station']['departure'] == "高雄" or paxDICT[str(message.author.id)]['station']['destination'] == "高雄":
                        response = "<@!{}>".format(message.author.id) + "高鐵沒有高雄站只有左營站喔"
                        await message.channel.send(response)
                        return
                    if paxDICT[str(message.author.id)]['station']['departure'] == "":
                        response = "<@!{}>".format(message.author.id) + "要記得說你從哪出發，還有要去哪裡喔！"
                        await message.channel.send(response)
                        return
                    if paxDICT[str(message.author.id)]['station']['destination'] == "":
                        response = "<@!{}>".format(message.author.id) + "要記得說你要去哪裡喔！"
                        await message.channel.send(response)
                        return
                    if paxDICT[str(message.author.id)]['adultAmount'] == 0 and paxDICT[str(message.author.id)]['childrenAmount'] == 0:
                        response = "<@!{}>".format(message.author.id) + "有幾位大人幾位小孩要記得說喔！"
                        await message.channel.send(response)
                        return
                    if paxDICT[str(message.author.id)]['station']['departure'] == paxDICT[str(message.author.id)]['station']['destination']:
                        response = "<@!{}>".format(message.author.id) + "呃，你已經在目的地了喔！"
                        await message.channel.send(response)
                        return
                    if paxDICT[str(message.author.id)]['station']['departure'] not in TaiwanLIST or paxDICT[str(message.author.id)]['station']['destination'] not in TaiwanLIST:
                        if paxDICT[str(message.author.id)]['station']['departure'] not in TaiwanLIST:
                            departure = paxDICT[str(message.author.id)]['station']['departure']
                            response = "<@!{}>".format(message.author.id) + "高鐵目前在{}沒有站喔！".format(departure)
                            await message.channel.send(response)
                            return
                        elif paxDICT[str(message.author.id)]['station']['destination'] not in TaiwanLIST:
                            destination = paxDICT[str(message.author.id)]['station']['destination']
                            response = "<@!{}>".format(message.author.id) + "高鐵目前在{}沒有站喔！".format(destination)
                            await message.channel.send(response)
                            return
                        else:
                            departure = paxDICT[str(message.author.id)]['station']['departure']
                            destination = paxDICT[str(message.author.id)]['station']['destination']
                            response = "<@!{}>".format(message.author.id) + "高鐵目前在{}跟{}都沒有站喔！".format(departure, destination)
                            await message.channel.send(response)
                            return
                    print(resultDICT)
                    response = "<@!{}>".format(message.author.id) + ticketPriceFree(inputSTR)                  
                    await message.channel.send(response)
                    del paxDICT[str(message.author.id)]
                else: #'標準艙票價' 
                    logging.debug('standard type')
                    if str(message.author.id) not in paxDICT:
                        paxDICT[str(message.author.id)] = {"station": {"departure": "", "destination": ""}, "adultAmount": 0, "childrenAmount": 0}
                    if 'departure' in resultDICT:
                        paxDICT[str(message.author.id)]['station']['departure'] = resultDICT['departure']
                    if 'destination' in resultDICT:
                        paxDICT[str(message.author.id)]['station']['destination'] = resultDICT['destination']
                    if 'adultAmount' in resultDICT:
                        paxDICT[str(message.author.id)]['adultAmount'] = resultDICT['adultAmount']
                    if 'childrenAmount' in resultDICT:
                        paxDICT[str(message.author.id)]['childrenAmount'] = resultDICT['childrenAmount']
                    if paxDICT[str(message.author.id)]['station']['departure'] == "高雄" or paxDICT[str(message.author.id)]['station']['destination'] == "高雄":
                        response = "<@!{}>".format(message.author.id) + "高鐵沒有高雄站只有左營站喔"
                        await message.channel.send(response)
                        return
                    if paxDICT[str(message.author.id)]['station']['departure'] == "":
                        response = "<@!{}>".format(message.author.id) + "要記得說你從哪出發，還有要去哪裡喔！"
                        await message.channel.send(response)
                        return
                    if paxDICT[str(message.author.id)]['station']['destination'] == "":
                        response = "<@!{}>".format(message.author.id) + "要記得說你要去哪裡喔！"
                        await message.channel.send(response)
                        return
                    if paxDICT[str(message.author.id)]['adultAmount'] == 0 and paxDICT[str(message.author.id)]['childrenAmount'] == 0:
                        response = "<@!{}>".format(message.author.id) + "有幾位大人幾位小孩要記得說喔！"
                        await message.channel.send(response)
                        return
                    if paxDICT[str(message.author.id)]['station']['departure'] == paxDICT[str(message.author.id)]['station']['destination']:
                        response = "<@!{}>".format(message.author.id) + "呃，你已經在目的地了喔！"
                        await message.channel.send(response)
                        return
                    if paxDICT[str(message.author.id)]['station']['departure'] not in TaiwanLIST or paxDICT[str(message.author.id)]['station']['destination'] not in TaiwanLIST:
                        if paxDICT[str(message.author.id)]['station']['departure'] not in TaiwanLIST:
                            departure = paxDICT[str(message.author.id)]['station']['departure']
                            response = "<@!{}>".format(message.author.id) + "高鐵目前在{}沒有站喔！".format(departure)
                            await message.channel.send(response)
                            return
                        elif paxDICT[str(message.author.id)]['station']['destination'] not in TaiwanLIST:
                            destination = paxDICT[str(message.author.id)]['station']['destination']
                            response = "<@!{}>".format(message.author.id) + "高鐵目前在{}沒有站喔！".format(destination)
                            await message.channel.send(response)
                            return
                        else:
                            departure = paxDICT[str(message.author.id)]['station']['departure']
                            destination = paxDICT[str(message.author.id)]['station']['destination']
                            response = "<@!{}>".format(message.author.id) + "高鐵目前在{}跟{}都沒有站喔！".format(departure, destination)
                            await message.channel.send(response)
                            return
                    print(resultDICT)
                    response = "<@!{}>".format(message.author.id) + ticketPrice(inputSTR)
                    await message.channel.send(response)
                    del paxDICT[str(message.author.id)]
            elif bool([n for n in nowLIST if n in client_message]): # 現在時間
                logging.debug('time checked')
                if str(message.author.id) not in paxDICT:
                    paxDICT[str(message.author.id)] = {"station": {"departure": "", "destination": ""}}
                if 'departure' in resultDICT:
                    paxDICT[str(message.author.id)]['station']['departure'] = resultDICT['departure']
                if 'destination' in resultDICT:
                    paxDICT[str(message.author.id)]['station']['destination'] = resultDICT['destination']
                if paxDICT[str(message.author.id)]['station']['departure'] == "高雄" or paxDICT[str(message.author.id)]['station']['destination'] == "高雄":
                    response = "<@!{}>".format(message.author.id) + "高鐵沒有高雄站只有左營站喔"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['station']['departure'] == "":
                    response = "<@!{}>".format(message.author.id) + "要記得說你從哪出發，還有要去哪裡喔！"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['station']['destination'] == "":
                    response = "<@!{}>".format(message.author.id) + "要記得說你要去哪裡喔！"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['station']['departure'] == paxDICT[str(message.author.id)]['station']['destination']:
                    response = "<@!{}>".format(message.author.id) + "呃，你已經在目的地了喔！"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['station']['departure'] not in TaiwanLIST or paxDICT[str(message.author.id)]['station']['destination'] not in TaiwanLIST:
                    if paxDICT[str(message.author.id)]['station']['departure'] not in TaiwanLIST:
                        departure = paxDICT[str(message.author.id)]['station']['departure']
                        response = "<@!{}>".format(message.author.id) + "高鐵目前在{}沒有站喔！".format(departure)
                        await message.channel.send(response)
                        return
                    elif paxDICT[str(message.author.id)]['station']['destination'] not in TaiwanLIST:
                        destination = paxDICT[str(message.author.id)]['station']['destination']
                        response = "<@!{}>".format(message.author.id) + "高鐵目前在{}沒有站喔！".format(destination)
                        await message.channel.send(response)
                        return
                    else:
                        departure = paxDICT[str(message.author.id)]['station']['departure']
                        destination = paxDICT[str(message.author.id)]['station']['destination']
                        response = "<@!{}>".format(message.author.id) + "高鐵目前在{}跟{}都沒有站喔！".format(departure, destination)
                        await message.channel.send(response)
                        return
                print(resultDICT)
                response = "<@!{}>".format(message.author.id) + ticketTime(inputSTR)
                await message.channel.send(response)
                del paxDICT[str(message.author.id)]
            elif bool([a for a in AroundLIST if a in client_message]): # 時間附近
                if str(message.author.id) not in paxDICT:
                    paxDICT[str(message.author.id)] = {"departure_time": "", "station": {"departure": "", "destination": ""}}
                if 'departure_time' in resultDICT:
                    paxDICT[str(message.author.id)]['departure_time'] = resultDICT['departure_time']
                if 'departure' in resultDICT:
                    paxDICT[str(message.author.id)]['station']['departure'] = resultDICT['departure']
                if 'destination' in resultDICT:
                    paxDICT[str(message.author.id)]['station']['destination'] = resultDICT['destination']
                if paxDICT[str(message.author.id)]['station']['departure'] == "高雄" or paxDICT[str(message.author.id)]['station']['destination'] == "高雄":
                    response = "<@!{}>".format(message.author.id) + "高鐵沒有高雄站只有左營站喔"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['departure_time'] == "":
                    response = "<@!{}>".format(message.author.id) + "要記得加入你的出發時間，並確認時間有沒有打對喔！"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['station']['departure'] == "":
                    response = "<@!{}>".format(message.author.id) + "要記得說你從哪出發，還有要去哪裡喔！"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['station']['destination'] == "":
                    response = "<@!{}>".format(message.author.id) + "要記得說你要去哪裡喔！"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['station']['departure'] == paxDICT[str(message.author.id)]['station']['destination']:
                    response = "<@!{}>".format(message.author.id) + "呃，你已經在目的地了喔！"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['station']['departure'] not in TaiwanLIST or paxDICT[str(message.author.id)]['station']['destination'] not in TaiwanLIST:
                    if paxDICT[str(message.author.id)]['station']['departure'] not in TaiwanLIST:
                        departure = paxDICT[str(message.author.id)]['station']['departure']
                        response = "<@!{}>".format(message.author.id) + "高鐵目前在{}沒有站喔！".format(departure)
                        await message.channel.send(response)
                        return
                    elif paxDICT[str(message.author.id)]['station']['destination'] not in TaiwanLIST:
                        destination = paxDICT[str(message.author.id)]['station']['destination']
                        response = "<@!{}>".format(message.author.id) + "高鐵目前在{}沒有站喔！".format(destination)
                        await message.channel.send(response)
                        return
                    else:
                        departure = paxDICT[str(message.author.id)]['station']['departure']
                        destination = paxDICT[str(message.author.id)]['station']['destination']
                        response = "<@!{}>".format(message.author.id) + "高鐵目前在{}跟{}都沒有站喔！".format(departure, destination)
                        await message.channel.send(response)
                        return
                print(resultDICT)
                response = "<@!{}>".format(message.author.id) + ticketTimeAround(inputSTR)
                await message.channel.send(response)
                del paxDICT[str(message.author.id)]
            elif bool([b for b in BeforeLIST if b in client_message]): # 時間之前
                if str(message.author.id) not in paxDICT:
                    paxDICT[str(message.author.id)] = {"departure_time": "", "station": {"departure": "", "destination": ""}}
                if 'departure_time' in resultDICT:
                    paxDICT[str(message.author.id)]['departure_time'] = resultDICT['departure_time']
                if 'departure' in resultDICT:
                    paxDICT[str(message.author.id)]['station']['departure'] = resultDICT['departure']
                if 'destination' in resultDICT:
                    paxDICT[str(message.author.id)]['station']['destination'] = resultDICT['destination']
                if paxDICT[str(message.author.id)]['station']['departure'] == "高雄" or paxDICT[str(message.author.id)]['station']['destination'] == "高雄":
                    response = "<@!{}>".format(message.author.id) + "高鐵沒有高雄站只有左營站喔"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['departure_time'] == "":
                    response = "<@!{}>".format(message.author.id) + "要記得加入你的出發時間，並確認時間有沒有打對喔！"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['station']['departure'] == "":
                    response = "<@!{}>".format(message.author.id) + "要記得說你從哪出發，還有要去哪裡喔！"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['station']['destination'] == "":
                    response = "<@!{}>".format(message.author.id) + "要記得說你要去哪裡喔！"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['station']['departure'] == paxDICT[str(message.author.id)]['station']['destination']:
                    response = "<@!{}>".format(message.author.id) + "呃，你已經在目的地了喔！"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['station']['departure'] not in TaiwanLIST or paxDICT[str(message.author.id)]['station']['destination'] not in TaiwanLIST:
                    if paxDICT[str(message.author.id)]['station']['departure'] not in TaiwanLIST:
                        departure = paxDICT[str(message.author.id)]['station']['departure']
                        response = "<@!{}>".format(message.author.id) + "高鐵目前在{}沒有站喔！".format(departure)
                        await message.channel.send(response)
                        return
                    elif paxDICT[str(message.author.id)]['station']['destination'] not in TaiwanLIST:
                        destination = paxDICT[str(message.author.id)]['station']['destination']
                        response = "<@!{}>".format(message.author.id) + "高鐵目前在{}沒有站喔！".format(destination)
                        await message.channel.send(response)
                        return
                    else:
                        departure = paxDICT[str(message.author.id)]['station']['departure']
                        destination = paxDICT[str(message.author.id)]['station']['destination']
                        response = "<@!{}>".format(message.author.id) + "高鐵目前在{}跟{}都沒有站喔！".format(departure, destination)
                        await message.channel.send(response)
                        return
                print(resultDICT)
                response = "<@!{}>".format(message.author.id) + ticketTimeBefore(inputSTR)
                await message.channel.send(response)
                del paxDICT[str(message.author.id)]
            else: # 時間之後
                logging.debug('time checked')
                if str(message.author.id) not in paxDICT:
                    paxDICT[str(message.author.id)] = {"departure_time": "", "station": {"departure": "", "destination": ""}}
                if 'departure_time' in resultDICT:
                    paxDICT[str(message.author.id)]['departure_time'] = resultDICT['departure_time']
                if 'departure' in resultDICT:
                    paxDICT[str(message.author.id)]['station']['departure'] = resultDICT['departure']
                if 'destination' in resultDICT:
                    paxDICT[str(message.author.id)]['station']['destination'] = resultDICT['destination']
                if paxDICT[str(message.author.id)]['station']['departure'] == "高雄" or paxDICT[str(message.author.id)]['station']['destination'] == "高雄":
                    response = "<@!{}>".format(message.author.id) + "高鐵沒有高雄站只有左營站喔"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['departure_time'] == "":
                    response = "<@!{}>".format(message.author.id) + "要記得加入你的出發時間，並確認時間有沒有打對喔！"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['station']['departure'] == "":
                    response = "<@!{}>".format(message.author.id) + "要記得說你從哪出發，還有要去哪裡喔！"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['station']['destination'] == "":
                    response = "<@!{}>".format(message.author.id) + "要記得說你要去哪裡喔！"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['station']['departure'] == paxDICT[str(message.author.id)]['station']['destination']:
                    response = "<@!{}>".format(message.author.id) + "呃，你已經在目的地了喔！"
                    await message.channel.send(response)
                    return
                if paxDICT[str(message.author.id)]['station']['departure'] not in TaiwanLIST or paxDICT[str(message.author.id)]['station']['destination'] not in TaiwanLIST:
                    if paxDICT[str(message.author.id)]['station']['departure'] not in TaiwanLIST:
                        departure = paxDICT[str(message.author.id)]['station']['departure']
                        response = "<@!{}>".format(message.author.id) + "高鐵目前在{}沒有站喔！".format(departure)
                        await message.channel.send(response)
                        return
                    elif paxDICT[str(message.author.id)]['station']['destination'] not in TaiwanLIST:
                        destination = paxDICT[str(message.author.id)]['station']['destination']
                        response = "<@!{}>".format(message.author.id) + "高鐵目前在{}沒有站喔！".format(destination)
                        await message.channel.send(response)
                        return
                    else:
                        departure = paxDICT[str(message.author.id)]['station']['departure']
                        destination = paxDICT[str(message.author.id)]['station']['destination']
                        response = "<@!{}>".format(message.author.id) + "高鐵目前在{}跟{}都沒有站喔！".format(departure, destination)
                        await message.channel.send(response)
                        return
                print(resultDICT)
                response = "<@!{}>".format(message.author.id) + ticketTime(inputSTR)
                await message.channel.send(response)
                del paxDICT[str(message.author.id)]
    elif "bot 點名" in message.content:
        response = "有！"
        await message.channel.send(response)
client.run(DISCORD_TOKEN)