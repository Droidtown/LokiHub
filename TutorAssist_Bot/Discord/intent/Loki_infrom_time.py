#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for infrom_time

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
from ArticutAPI import Articut
import os
import re
from datetime import datetime

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["articut_key"])

DEBUG_infrom_time = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asNoun":["連假","線上","進班","遠距","面對面","愉快","線下","到班","實體課程"],"_asOkay":["ok","OK","oK","Ok","Okay","okay","OKAY"],"_asTime":["小時半"],"_asVerb":["改一下","討論一下","調整一下"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_infrom_time:
        print("[infrom_time] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["inform_time"]={}
    if utterance == "[8].-[10].":
        if resultDICT["intentLIST"] == [] and len(inputSTR)<= 13:
            resultDICT["intentLIST"].append("inform_time")
            if len(inputSTR.split("-")) == 2:
                resultDICT["inform_time"]["inform_time_time"] = args[0]+"到"+args[1]
            elif len(inputSTR.split("/")) == 2:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0]+"月"+args[1]+"日", level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
            else:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        else:
            if len(inputSTR.split("-")) == 2:
                resultDICT["inform_time"]["inform_time_time"] = args[0]+"到"+args[1]
            elif len(inputSTR.split("/")) == 2:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0]+"月"+args[1]+"日", level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
            else:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        

    if utterance == "[8].到[10].":
        if resultDICT["intentLIST"] == [] and len(inputSTR)<= 13:
            resultDICT["intentLIST"].append("inform_time")
            try:
                resultDICT["inform_time"]["inform_time_time"] = args[0]+"到"+args[1]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        else:
            try:
                resultDICT["inform_time"]["inform_time_time"] = args[0]+"到"+args[1]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        
                

    if utterance == "[8]:[30]-[10].":
        if resultDICT["intentLIST"] == [] and len(inputSTR)<= 13:
            resultDICT["intentLIST"].append("inform_time")
            try:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR.split("-")[0]+"到"+inputSTR.split("-")[1]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        else:
            try:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR.split("-")[0]+"到"+inputSTR.split("-")[1]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        
        

    if utterance == "[8]:[30]-[10]:[30]":
        if resultDICT["intentLIST"] == [] and len(inputSTR)<= 13:
            resultDICT["intentLIST"].append("inform_time")
            try:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR.split("-")[0]+"到"+inputSTR.split("-")[1]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        else:
            try:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR.split("-")[0]+"到"+inputSTR.split("-")[1]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        
                

    if utterance == "[8]:[30]到[10].":
        if resultDICT["intentLIST"] == [] and len(inputSTR)<= 13:
            resultDICT["intentLIST"].append("inform_time")
            try:
                resultDICT["inform_time"]["inform_time_time"] = args[0]+":"+args[1]+"到"+args[2]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        else:
            try:
                resultDICT["inform_time"]["inform_time_time"] = args[0]+":"+args[1]+"到"+args[2]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        
                

    if utterance == "[8]:[30]到[10]:[30]":
        if resultDICT["intentLIST"] == [] and len(inputSTR)<= 13:
            resultDICT["intentLIST"].append("inform_time")
            try:
                resultDICT["inform_time"]["inform_time_time"] = args[0]+":"+args[1]+"到"+args[2]+":"+args[3]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        else:
            try:
                resultDICT["inform_time"]["inform_time_time"] = args[0]+":"+args[1]+"到"+args[2]+":"+args[3]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        
                

    if utterance == "[八月][三十]":
        if resultDICT["intentLIST"] == [] and len(inputSTR)<= 13:
            resultDICT["intentLIST"].append("inform_time")
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0]+args[1]+"日", level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        else:
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0]+args[1]+"日", level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        
    
    if utterance == "[八月][三十]的[10].-[12].":
        if resultDICT["intentLIST"] == [] and len(inputSTR)<= 13:
            resultDICT["intentLIST"].append("inform_time")
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0]+args[1]+"日", level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())+"的"+args[2]+"到"+args[3]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        else:
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0]+args[1]+"日", level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())+"的"+args[2]+"到"+args[3]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR            
        

    if utterance == "[八月][三十]的[10].到[12].":
        if resultDICT["intentLIST"] == [] and len(inputSTR)<= 13:
            resultDICT["intentLIST"].append("inform_time")
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0]+args[1]+"日", level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())+"的"+args[2]+"到"+args[3]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        else:
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0]+args[1]+"日", level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())+"的"+args[2]+"到"+args[3]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR            
        

    if utterance == "[八月][三十]的[10]:[30]-[12].":
        if resultDICT["intentLIST"] == [] and len(inputSTR)<= 13:
            resultDICT["intentLIST"].append("inform_time")
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0]+args[1]+"日", level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())+"的"+args[2]+":"+args[3]+"到"+args[4]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        else:
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0]+args[1]+"日", level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())+"的"+args[2]+":"+args[3]+"到"+args[4]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR            
        

    if utterance == "[八月][三十]的[10]:[30]-[12]:[00]":
        if resultDICT["intentLIST"] == [] and len(inputSTR)<= 13:
            resultDICT["intentLIST"].append("inform_time")
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0]+args[1]+"日", level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())+"的"+args[2]+":"+args[3]+"到"+args[4]+":"+args[5]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        else:
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0]+args[1]+"日", level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())+"的"+args[2]+":"+args[3]+"到"+args[4]+":"+args[5]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR            
        

    if utterance == "[八月][三十]的[10]:[30]到[12].":
        if resultDICT["intentLIST"] == [] and len(inputSTR)<= 13:
            resultDICT["intentLIST"].append("inform_time")
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0]+args[1]+"日", level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())+"的"+args[2]+":"+args[3]+"到"+args[4]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        else:
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0]+args[1]+"日", level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())+"的"+args[2]+":"+args[3]+"到"+args[4]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR            
        

    if utterance == "[八月][三十]的[10]:[30]到[12]:[00]":
        if resultDICT["intentLIST"] == [] and len(inputSTR)<= 13:
            resultDICT["intentLIST"].append("inform_time")
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0]+args[1]+"日", level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())+"的"+args[2]+":"+args[3]+"到"+args[4]+":"+args[5]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        else:
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0]+args[1]+"日", level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())+"的"+args[2]+":"+args[3]+"到"+args[4]+":"+args[5]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR            
        

    if utterance == "[八月三十日]的[10].-[12].":
        if resultDICT["intentLIST"] == [] and len(inputSTR)<= 13:
            resultDICT["intentLIST"].append("inform_time")
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())+"的"+args[1]+"到"+args[2]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        else:
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())+"的"+args[1]+"到"+args[2]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        

    if utterance == "[八月三十日]的[10].到[12].":
        if resultDICT["intentLIST"] == [] and len(inputSTR)<= 13:
            resultDICT["intentLIST"].append("inform_time")
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())+"的"+args[1]+"到"+args[2]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        else:
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())+"的"+args[1]+"到"+args[2]
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        

    if utterance == "[八點]-[十點]":
        if resultDICT["intentLIST"] == [] and len(inputSTR)<= 13:
            resultDICT["intentLIST"].append("inform_time")
            if len(inputSTR.split("-")) == 2:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR.split("-")[0]+"到"+inputSTR.split("-")[1]
            elif len(inputSTR.split("/")) == 2:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR.split("/")[0]+"月"+inputSTR.split("/")[1]+"日"
            else:
                try:
                    resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
                except:
                    resultDICT["inform_time"]["inform_time_time"] = inputSTR
        else:
            if len(inputSTR.split("-")) == 2:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR.split("-")[0]+"到"+inputSTR.split("-")[1]
            elif len(inputSTR.split("/")) == 2:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR.split("/")[0]+"月"+inputSTR.split("/")[1]+"日"
            else:
                try:
                    resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
                except:
                    resultDICT["inform_time"]["inform_time_time"] = inputSTR

    if utterance == "[八點]到[十點]":
        if resultDICT["intentLIST"] == [] and len(inputSTR)<= 13:
            resultDICT["intentLIST"].append("inform_time")
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        else:
            try:
                resultDICT["inform_time"]["inform_time_time"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
            except:
                resultDICT["inform_time"]["inform_time_time"] = inputSTR
        
        pass

    return resultDICT