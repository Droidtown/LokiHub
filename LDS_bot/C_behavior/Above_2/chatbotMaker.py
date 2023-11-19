#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Loki 4.0 Chatbot AI 回應產生器
"""

from random import sample
from requests import post
import re
import os
import json

LOKI_CALL_URL = "https://api.droidtown.co/Loki/Call/"

BASE_PATH = os.path.dirname(__file__)
UTTERANCE_PAT = re.compile("^ *if utterance == \"([^\"]+)\":", re.M)
CHAT_GPT_ORDER_PAT = re.compile("^\d+\. *")
CHAT_GPT_MARK_PAT = re.compile("^[\"「]|[\"」]$")
MESSAGE_LIMIT = 3500

accountDICT = {}
try:
    accountDICT = json.load(open(os.path.join(BASE_PATH, "account.info"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] account.info => {}".format(str(e)))

chatbotDICT = {}
try:
    chatbotDICT = json.load(open(os.path.join(BASE_PATH, "chatbot.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] chatbot.json => {}".format(str(e)))

def getResponse(intent, system, assistant, user):
    resultLIST = []
    try:
        payload = {
            "username": accountDICT["username"],
            "loki_key": accountDICT["loki_key"],
            "intent": intent,
            "func": "run_alias",
            "data": {"messages": []}
        }
        if assistant:
            for assistant_l in assistant:
                payload["data"]["messages"] = system + assistant_l + user
                result = post(LOKI_CALL_URL, json=payload).json()
                if result["status"]:
                    contentLIST = result["result_list"][0]["message"]["content"].split("\n")
                    for content in contentLIST:
                        content = CHAT_GPT_ORDER_PAT.sub("", content.strip())
                        content = CHAT_GPT_MARK_PAT.sub("", content.strip())
                        content = content.strip()
                        if content:
                            resultLIST.append(content)
                else:
                    print("[ERROR] getResponse")
                    print(result)
                    break

            if resultLIST:
                resultLIST = sample(resultLIST, int(len(resultLIST)/len(assistant)))
        else:
            payload["data"]["messages"] = system + user
            result = post(LOKI_CALL_URL, json=payload).json()
            if result["status"]:
                contentLIST = result["result_list"][0]["message"]["content"].split("\n")
                for content in contentLIST:
                    content = content.strip()
                    if content:
                        content = CHAT_GPT_ORDER_PAT.sub("", content.strip())
                        content = CHAT_GPT_MARK_PAT.sub("", content.strip())
                        content = content.strip()
                        if content:
                            resultLIST.append(content)
            else:
                print("[ERROR] getResponse")
                print(result)
    except Exception as e:
        print("[ERROR] getResponse")
        print(str(e))

    return resultLIST


if __name__ == "__main__":
    if chatbotDICT:
        # 建立 reply 資料夾
        replyPATH = os.path.join(BASE_PATH, "reply")
        if not os.path.exists(replyPATH):
            os.mkdir(replyPATH)

        # 讀取 intent utterance
        for intentSTR in chatbotDICT:
            filePath = os.path.join(BASE_PATH, "intent", "Loki_{}.py".format(intentSTR))
            if os.path.exists(filePath):
                textSTR = open(filePath, encoding="utf-8").read()
                if "CHATBOT_MODE = True" not in textSTR:
                    continue

                utteranceLIST = [gg.group(1) for gg in UTTERANCE_PAT.finditer(textSTR)]
                if utteranceLIST:
                    print("[Intent] {} generating...".format(intentSTR))
                    promptDICT = {
                        "system": [],
                        "assistant": [],
                        "user": []
                    }

                    # 讀取 prompt, document
                    intentDICT = chatbotDICT[intentSTR]
                    if intentDICT["prompt"]["system"]:
                        promptDICT["system"] = [{"role": "system", "content": intentDICT["prompt"]["system"]}]

                    if intentDICT["document"]:
                        if intentDICT["prompt"]["assistant"] == "":
                            keyLIST = ["「{{" + x + "}}」" for x in intentDICT["document"][0]["content"]]
                            intentDICT["prompt"]["assistant"] = "請閱讀內容：{{}}".format("，".join(keyLIST))

                        promptDICT["assistant"] = [[]]
                        for document_d in intentDICT["document"]:
                            contentSTR = intentDICT["prompt"]["assistant"]
                            for k in document_d["content"]:
                                contentSTR = contentSTR.replace("{{" + k + "}}", document_d["content"][k])
                            if contentSTR:
                                if promptDICT["assistant"][-1] and sum(len(assistant_d["content"]) for assistant_d in promptDICT["assistant"][-1]) + len(contentSTR) >= MESSAGE_LIMIT:
                                    promptDICT["assistant"].append([])
                                promptDICT["assistant"][-1].append({"role": "assistant", "content": contentSTR})

                    # 生成回覆
                    try:
                        resultDICT = json.load(open(os.path.join(replyPATH, "reply_{}.json".format(intentSTR)), encoding="utf-8"))
                    except:
                        resultDICT = {}
                    for utterance in utteranceLIST:
                        contentSTR = intentDICT["prompt"]["user"].replace("{{UTTERANCE}}", re.sub("[\[\]]", "", utterance))
                        if contentSTR:
                            promptDICT["user"] = [{"role": "user", "content": contentSTR}]

                            responseLIST = getResponse(intentSTR, promptDICT["system"], promptDICT["assistant"], promptDICT["user"])
                            if utterance in resultDICT:
                                resultDICT[utterance].extend(responseLIST)
                                resultDICT[utterance] = list(set(resultDICT[utterance]))
                            else:
                                resultDICT[utterance] = responseLIST
                            print("[Utterance] {}".format(utterance))

                    # 儲存 reply
                    with open(os.path.join(replyPATH, "reply_{}.json".format(intentSTR)), "w", encoding="utf-8") as replyFile:
                        json.dump(resultDICT, replyFile, ensure_ascii=False, indent=4)
                        print("[Success] reply_{}.json".format(intentSTR))

            else:
                print("[ERROR] {} is not found".format(intentSTR))
    else:
        print("[Error] Invalid Chatbot Config")
