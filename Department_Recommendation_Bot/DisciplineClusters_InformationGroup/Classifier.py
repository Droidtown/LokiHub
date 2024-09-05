#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import asyncio
import aiohttp
import json
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

LOKI_URL = "https://api.droidtown.co/Loki/API/"
LOKI_CALL_URL = "https://api.droidtown.co/Loki/Call/"
accountInfo = json.load(open(os.path.join(BASE_PATH, "..\\account.info"), encoding="utf-8"))
USERNAME = accountInfo["username"]
LOKI_KEY = "wgFv%9UXqeXqFlO+VEpAnk_lfOlaORG"
POST_INTERVAL_SEC = 5

async def getLokiTextSim(inputSTR, keywordLIST=[], featureLIST=[], count=1):
    payloadDICT = {
        "username": USERNAME,
        "loki_key": LOKI_KEY,
        "input_str": inputSTR,
        "keyword": keywordLIST,
        "feature": featureLIST,
        "count": count
    }

    async with aiohttp.ClientSession() as session:
        while True:
            async with session.post(LOKI_URL, json=payloadDICT) as response:
                if response.status == 200:
                    try:
                        resultDICT = await response.json()
                        if resultDICT["status"]:
                            if resultDICT["progress_status"] == "processing":
                                await asyncio.sleep(POST_INTERVAL_SEC)
                                continue
                        return resultDICT
                    except Exception as e:
                        return {"status": False, "msg": str(e)}
                else:
                    return {"status": False, "msg": f"HTTP {response.status}"}

async def getInfo():
    payloadDICT = {
        "username": USERNAME,
        "loki_key": LOKI_KEY,
        "func": "get_info",
        "data": {}
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(LOKI_CALL_URL, json=payloadDICT) as response:
            if response.status == 200:
                try:
                    resultDICT = await response.json()
                    return resultDICT
                except Exception as e:
                    return {"status": False, "msg": str(e)}
            else:
                return {"status": False, "msg": f"HTTP {response.status}"}

async def main():
    from pprint import pprint

    inputSTR = "我喜歡寫程式"
    keywordLIST = []
    featureLIST = []
    countINT = 1

    resultDICT = await getLokiTextSim(inputSTR, keywordLIST=keywordLIST, featureLIST=featureLIST, count=countINT)
    pprint(resultDICT)

if __name__ == "__main__":
    asyncio.run(main())
