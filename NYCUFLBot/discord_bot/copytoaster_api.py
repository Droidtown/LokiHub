#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from requests import post
from time import sleep

import json
accountDICT = json.load(open("account.info", encoding="utf-8"))

COPYTOASTER_URL = "https://api.droidtown.co/CopyToaster/API/V2/"
COPYTOASTER_CALL_URL = "https://api.droidtown.co/CopyToaster/Call/"
USERNAME = accountDICT["username"]
COPYTOASTER_KEY = accountDICT["copytoaster_key"]
POST_INTERVAL_SEC = 5

def getCopyToasterResult(categorySTR, inputSTR, count=15):
    payloadDICT = {
        "username": "USERNAME",
        "copytoaster_key": COPYTOASTER_KEY,
        "category": categorySTR,
        "input_str": inputSTR,
        "count": count
    }

    while True:
        response = post(COPYTOASTER_URL, json=payloadDICT)
        if response.status_code == 200:
            try:
                resultDICT = response.json()
                if resultDICT["status"]:
                    if resultDICT["progress_status"] == "processing":
                        sleep(POST_INTERVAL_SEC)
                        continue
                return resultDICT
            except Exception as e:
                return {"status": False, "msg": str(e)}
        else:
            return {"status": False, "msg": "HTTP {}".format(response.status_code)}

def getInfo():
    payloadDICT = {
        "username": USERNAME,
        "loki_key": COPYTOASTER_KEY,
        "func": "get_info",
        "data": {}
    }

    response = post(COPYTOASTER_CALL_URL, json=payloadDICT)
    if response.status_code == 200:
        try:
            resultDICT = response.json()
            return resultDICT
        except Exception as e:
            return {"status": False, "msg": str(e)}
    else:
        return {"status": False, "msg": "HTTP {}".format(response.status_code)}

if __name__ == "__main__":
    from pprint import pprint

    categorySTR = "" # communication_writing_skills,doublemajor_minor_cross,grad_progam,lx_ai,minimum_credits,pre_master,required_coursework,second_language
    inputSTR = ""
    countINT = 1

    resultDICT = getCopyToasterResult(categorySTR, inputSTR, count=countINT)
    pprint(resultDICT)