#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB_PATH = os.path.join(BASE_PATH, "lib")
INTENT_PATH = os.path.join(BASE_PATH, "intent")
REPLY_PATH = os.path.join(BASE_PATH, "reply")

ACCOUNT_DICT = {
    "debug": True,
    "server": "https://api.droidtown.co",
    "username": "",
    "api_key": "",
    "version": "latest",
    "loki_key": "",
    "loki_project": "",
    "copytoaster_key": "",
    "copytoaster_category": [],
    "llm_prompt": {
        "system": "You are an assistant.",
        "assistant": "",
        "user": "answer the question '{{INPUT}}' in Mandarin Chinese used in Taiwan.",
        "resp_header": [
            "我的資料庫沒有相關的資料，但網路資料顯示..."
        ]
    },
    "chatbot_mode": False,
    "chatbot_prompt": {},
    "utterance_count": {},
    "utterance_feature": ["verb", "noun"],
    "utterance_threshold": 0.4
}

try:
    accountInfo = json.load(open(os.path.join(BASE_PATH, "account.info"), encoding="utf-8"))
    ACCOUNT_DICT.update(accountInfo)
    del accountInfo
except:
    pass

ARTICUT = None
try:
    from ArticutAPI import Articut
    if ACCOUNT_DICT["username"] and ACCOUNT_DICT["api_key"]:
        ARTICUT = Articut(username=ACCOUNT_DICT["username"], apikey=ACCOUNT_DICT["api_key"],
                          version=ACCOUNT_DICT["version"], url=ACCOUNT_DICT["server"])
except:
    pass

try:
    USER_DEFINED_FILE = os.path.join(INTENT_PATH, "USER_DEFINED.json")
    USER_DEFINED_DICT = json.load(open(USER_DEFINED_FILE, encoding="utf-8"))
except:
    USER_DEFINED_FILE = ""
    USER_DEFINED_DICT = {}