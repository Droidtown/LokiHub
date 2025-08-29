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
    "server": "https://nlu.droidtown.co",
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
        "user": "answer the question '{{INPUT}}'.",
        "resp_header": [
            "My database does not contain relevant information, but online sources indicate that..."
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
    #from ArticutAPI_EN import Articut
    from importlib.util import module_from_spec
    from importlib.util import spec_from_file_location
    if ACCOUNT_DICT["username"] and ACCOUNT_DICT["api_key"]:
        spec = spec_from_file_location("ArticutAPI", os.path.join(LIB_PATH, "Articut.py"))
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        ARTICUT = module.Articut(username=ACCOUNT_DICT["username"], apikey=ACCOUNT_DICT["api_key"],
                          version=ACCOUNT_DICT["version"], url=ACCOUNT_DICT["server"])
except:
    pass

try:
    USER_DEFINED_FILE = os.path.join(INTENT_PATH, "USER_DEFINED.json")
    USER_DEFINED_DICT = json.load(open(USER_DEFINED_FILE, encoding="utf-8"))
except:
    USER_DEFINED_FILE = ""
    USER_DEFINED_DICT = {}