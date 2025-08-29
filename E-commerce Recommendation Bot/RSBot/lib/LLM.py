#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import Counter
from importlib.util import module_from_spec
from importlib.util import spec_from_file_location
from random import choice
from requests import post
from time import sleep
import math
import os

def import_from_path(module_name, file_path):
    spec = spec_from_file_location(module_name, file_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

CWD_PATH = os.path.dirname(os.path.abspath(__file__))
MODULE_DICT = {
    "Account": import_from_path("RSBot_lib_Account", os.path.join(CWD_PATH, "Account.py"))
}
"""
Account Variables
[Variable] BASE_PATH         => path of root
[Variable] LIB_PATH          => path of lib folder
[Variable] INTENT_PATH       => path of intent folder
[Variable] REPLY_PATH        => path of reply folder
[Variable] ACCOUNT_DICT      => account.info
[Variable] ARTICUT           => ArticutAPI (Usage: ARTICUT.parse()。 #ArticutAPI Required.)
[Variable] USER_DEFINED_FILE => path of UserDefined
[Variable] USER_DEFINED_DICT => UserDefined data
"""
ACCOUNT_DICT = MODULE_DICT["Account"].ACCOUNT_DICT
ARTICUT = MODULE_DICT["Account"].ARTICUT
USER_DEFINED_FILE = MODULE_DICT["Account"].USER_DEFINED_FILE

def getCopyToaster(inputSTR, count=3):
    resultLIST = []
    if ACCOUNT_DICT["username"] and ACCOUNT_DICT["copytoaster_key"]:
        url = f"{ACCOUNT_DICT['server']}/CopyToaster/API/V2/"
        payload = {
            "username": ACCOUNT_DICT["username"],
            "copytoaster_key": ACCOUNT_DICT["copytoaster_key"],
            "input_str": inputSTR,
            "count": count
        }

        for category in ACCOUNT_DICT["copytoaster_category"]:
            payload["category"] = category
            while True:
                try:
                    response = post(url, json=payload).json()
                    if response["status"]:
                        if response["progress_status"] == "completed":
                            for r in response["result_list"]:
                                resultLIST.append(r["document"].split(">>\\n")[1])
                                break
                    else:
                        print(f"[getCopyToaster] Category: {category} => {response['msg']}")
                        break
                except Exception as e:
                    print(f"[getCopyToaster] {str(e)}")
                    break

                sleep(1.2)

    return resultLIST

def getLokiLLM(inputSTR, referenceSTR=""):
    responseSTR = ""
    sourceSTR = ""
    if ACCOUNT_DICT["chatbot_prompt"]:
        url = f"{ACCOUNT_DICT['server']}/Loki_EN/Call/"
        payload = {
            "username": ACCOUNT_DICT["username"],
            "loki_key": ACCOUNT_DICT["loki_key"],
            "intent": list(ACCOUNT_DICT["chatbot_prompt"])[0],
            "func": "run_alias",
            "data": {
                "messages": []
            }
        }
        if ACCOUNT_DICT["llm_prompt"]["system"]:
            payload["data"]["messages"].append({"role": "system", "content": ACCOUNT_DICT["llm_prompt"]["system"]})
        if ACCOUNT_DICT["llm_prompt"]["assistant"]:
            payload["data"]["messages"].append({"role": "assistant", "content": ACCOUNT_DICT["llm_prompt"]["assistant"]})

        headerSTR = ""
        if referenceSTR and type(referenceSTR) == str:
            contentSTR = f"You will use the facts below as reference and only the facts below:\n{referenceSTR}\n"
            if "{{INPUT}}" in ACCOUNT_DICT["llm_prompt"]["user"]:
                contentSTR += ACCOUNT_DICT["llm_prompt"]["user"].replace("{{INPUT}}", inputSTR)
            else:
                contentSTR += inputSTR

            payload["data"]["messages"].append({"role": "user", "content": contentSTR})
            sourceSTR = "RAG_reply"
        else:
            contentSTR = inputSTR
            if "{{INPUT}}" in ACCOUNT_DICT["llm_prompt"]["user"]:
                contentSTR = ACCOUNT_DICT["llm_prompt"]["user"].replace("{{INPUT}}", inputSTR)

            payload["data"]["messages"].append({"role": "user", "content": contentSTR})
            sourceSTR = "LLM_reply"
            try:
                headerSTR = choice(ACCOUNT_DICT["llm_prompt"]["resp_header"])
            except:
                headerSTR = "My database does not contain relevant information, but online sources indicate that..."

        try:
            result = post(url, json=payload).json()
            if result["status"]:
                responseSTR = result["result_list"][0]["message"]["content"]
                if headerSTR:
                    responseSTR = f"{headerSTR}\n{responseSTR}"
            else:
                print(f"[getLokiLLM] {result['msg']}")
        except Exception as e:
            print(f"[getLokiLLM] {str(e)}")

    return responseSTR, sourceSTR

def callLLM(inputSTR):
    copyToasterResultLIST = getCopyToaster(inputSTR)
    if copyToasterResultLIST:
        referenceSTR = "\n".join(copyToasterResultLIST)
    else:
        referenceSTR = ""

    llmResultSTR, sourceSTR = getLokiLLM(inputSTR, referenceSTR=referenceSTR)
    return llmResultSTR, sourceSTR

def counterCosineSimilarity(count1DICT, count2DICT):
    terms = set(count1DICT).union(count2DICT)
    dotprod = sum(count1DICT.get(k, 0) * count2DICT.get(k, 0) for k in terms)
    magA = math.sqrt(sum(count1DICT.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(count2DICT.get(k, 0)**2 for k in terms))
    similarity = dotprod / (magA * magB) if magA and magB else 0
    return similarity

def getCosineSimilarityUtterance(inputSTR, utteranceDICT, featureLIST=ACCOUNT_DICT["utterance_feature"]):
    scoreDICT = {
        "intent": "",
        "utterance": "",
        "score": 0
    }
    if ARTICUT:
        atcResultDICT = ARTICUT.parse(inputSTR, userDefinedDictFILE=USER_DEFINED_FILE)
        if atcResultDICT["status"]:
            wordLIST = getWord(atcResultDICT, featureLIST)
            wordCountDICT = dict(Counter([x.strip().lower() for x in wordLIST]))
            for intent_s, utterance_d in utteranceDICT.items():
                for utterance_s, count_d in utterance_d.items():
                    utteranceCountDICT = getWordCount(count_d, featureLIST)
                    score = counterCosineSimilarity(utteranceCountDICT, wordCountDICT)
                    if score > scoreDICT["score"]:
                        scoreDICT["intent"] = intent_s
                        scoreDICT["utterance"] = utterance_s
                        scoreDICT["score"] = score

    return scoreDICT

def getCosineSimilarity(input1STR, input2STR, featureLIST=ACCOUNT_DICT["utterance_feature"], userDefinedDictFILE=USER_DEFINED_FILE):
    score = 0
    if ARTICUT:
        # [input1STR result, input2STR result]
        atcResultLIST = [ARTICUT.parse(input1STR, userDefinedDictFILE=userDefinedDictFILE),
                         ARTICUT.parse(input2STR, userDefinedDictFILE=userDefinedDictFILE)]
        if all(x["status"] for x in atcResultLIST):
            wordCountLIST = []
            for atcResultDICT in atcResultLIST:
                wordLIST = getWord(atcResultDICT, featureLIST)
                wordCountLIST.append(dict(Counter([x.strip().lower() for x in wordLIST])))

            score = counterCosineSimilarity(wordCountLIST[0], wordCountLIST[1])

    return score

def getWord(atkResult, featureLIST):
    wordLIST = []
    #if "contentword" in featureLIST:
        #wordLIST.extend([x[2] for x in sum(ARTICUT.getContentWordLIST(atkResult), [])])
    #else:
        #if "verb" in featureLIST:
            #wordLIST.extend([x[2] for x in sum(ARTICUT.getVerbStemLIST(atkResult), [])])
        #if "noun" in featureLIST:
            #wordLIST.extend([x[2] for x in sum(ARTICUT.getNounStemLIST(atkResult), [])])

    for x in sum(atkResult["result_obj"], []):
        if "contentword" in featureLIST:
            if x["pos"] in ["ACTION_verb", "VerbP", "ENTITY_noun", "ENTITY_nounHead", "ENTITY_nouny",
                            "ENTITY_oov", "UserDefined", "MODIFIER", "ModifierP", "DegreeP"]:
                wordLIST.append(x["text"])
                continue
        if x["pos"] in ["ACTION_verb", "VerbP"]:
            if "verb" in featureLIST:
                wordLIST.append(x["text"])
        if x["pos"] in ["ENTITY_noun", "ENTITY_nounHead", "ENTITY_nouny", "ENTITY_oov", "UserDefined"]:
            if "noun" in featureLIST:
                wordLIST.append(x["text"])
        if x["pos"] in ["UserDefined"]:
            if any(k in featureLIST for k in ["noun", "userdefined"]) and "contentword" not in featureLIST:
                wordLIST.append(x["text"])
        if x["pos"] in ["MODIFIER", "ModifierP"]:
            if "modifier" in featureLIST and "contentword" not in featureLIST:
                wordLIST.append(x["text"])
        if x["pos"] in ["TIME_holiday", "TIME_justtime", "TIME_day", "TIME_week", "TIME_month", "TIME_season", "TIME_year", "TIME_decade"]:
            if "time" in featureLIST:
                wordLIST.append(x["text"])
        if x["pos"] in ["LOCATION", "KNOWLEDGE_addUS", "KNOWLEDGE_routeUS"]:
            if "location" in featureLIST:
                wordLIST.append(x["text"])
        if x["pos"] in ["ENTITY_person"]:
            if "person" in featureLIST:
                wordLIST.append(x["text"])
        if x["pos"] in ["MODIFIER_color"]:
            if "person" in featureLIST:
                wordLIST.append(x["text"])
        if x["pos"] in ["IDIOM"]:
            if "idiom" in featureLIST:
                wordLIST.append(x["text"])

    return wordLIST

def getWordCount(countDICT, featureLIST):
    resultDICT = {}

    for feature in featureLIST:
        if feature in ["noun", "verb", "userdefined", "modifier"] and "contentword" in featureLIST:
            continue

        for word, count in countDICT[feature].items():
            if word not in resultDICT:
                resultDICT[word] = 0
            resultDICT[word] += count

    return resultDICT

def getLLM(system="", assistant="", user=""):
    resultSTR = ""
    if ACCOUNT_DICT["chatbot_prompt"]:
        url = f"{ACCOUNT_DICT['server']}/Loki_EN/Call/"
        payload = {
            "username": ACCOUNT_DICT["username"],
            "loki_key": ACCOUNT_DICT["loki_key"],
            "intent": list(ACCOUNT_DICT["chatbot_prompt"])[0],
            "func": "run_alias",
            "data": {
                "messages": []
            }
        }
        if system:
            payload["data"]["messages"].append({"role": "system", "content": system})
        if assistant:
            payload["data"]["messages"].append({"role": "assistant", "content": assistant})
        if user:
            payload["data"]["messages"].append({"role": "user", "content": user})

        if payload["data"]["messages"]:
            try:
                result = post(url, json=payload).json()
                if result["status"]:
                    resultSTR = result["result_list"][0]["message"]["content"]
                else:
                    print(f"[getLLM] {result['msg']}")
            except Exception as e:
                print(f"[getLLM] {str(e)}")

    return resultSTR


if __name__ == "__main__":
    inputSTR = ""
    resultSTR, sourceSTR = callLLM(inputSTR)
    print(sourceSTR, resultSTR)