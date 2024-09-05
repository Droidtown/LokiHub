#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for interest_adv (async version)

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict,
        pattern       str

    Output:
        resultDICT    dict
"""

import json
import os
from random import sample
import asyncio

DEBUG = False
CHATBOT_MODE = False

userDefinedDICT = {}
responseDICT = {}

async def load_json_async(filepath):
    try:
        async with aiofiles.open(filepath, mode="r", encoding="utf-8") as f:
            return json.loads(await f.read())
    except Exception as e:
        print(f"[ERROR] Failed to load {filepath} => {e}")
        return {}

async def init_dictionaries():
    global userDefinedDICT, responseDICT
    userDefinedPath = os.path.join(os.path.dirname(__file__), "USER_DEFINED.json")
    replyPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_interest_adv.json")

    userDefinedDICT = await load_json_async(userDefinedPath)
    
    if CHATBOT_MODE:
        responseDICT = await load_json_async(replyPath)

async def debugInfo(inputSTR, utterance):
    if DEBUG:
        print(f"[interest_adv] {inputSTR} ===> {utterance}")

async def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)
    return resultSTR

async def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    await debugInfo(inputSTR, utterance)
    
    if utterance == "他很喜歡當導師":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我一直都喜歡學習如何有效溝通和說服他人":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我一直都對人工智慧的技術充滿好奇":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我一直都對處理問題很有興趣":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我一直都很喜歡處理問題":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我享受創作文字和故事":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我喜歡參加戶外活動，探索自然":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我喜歡學習如何製作數位內容":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我對創新思維和解決方案很感興趣":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我對哲學和倫理學有濃厚的興趣":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我對心理學的理論有濃厚的興趣":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我對思維模式的研究感興趣":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我對數據分析有強烈的好奇心":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我對文化交流和全球化現象感興趣":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我對機器學習的應用感到興奮":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我對環境保護和可持續發展感興趣":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我對說服他人很感興趣":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我對醫學和健康科學感興趣":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我很喜歡物理":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT
    
    if utterance == "我喜歡運動":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我從大學時起就對人工智慧的技術充滿好奇":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我從高中時起就對處理問題很有興趣":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我從高中時起就很喜歡學習如何有效溝通和說服他人":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我從高中時起就很喜歡處理問題":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我熱衷於學習新的藝術技巧":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我熱衷於探索人類行為":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我熱衷於閱讀科幻小說":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT

    if utterance == "我越來越享受在這發掘知識的過程中":
        if CHATBOT_MODE:
            resultDICT["response"] = await getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT["source"] = utterance
            return resultDICT
