#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from importlib.util import module_from_spec
from importlib.util import spec_from_file_location
import json
import os

def import_from_path(module_name, file_path):
    spec = spec_from_file_location(module_name, file_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

CWD_PATH = os.path.dirname(os.path.abspath(__file__))
MODULE_DICT = {
    "Account": import_from_path("whats_in_my_fridge_lib_Account", os.path.join(CWD_PATH, "lib/Account.py")),
    "ChatbotMaker": import_from_path("whats_in_my_fridge_lib_ChatbotMaker", os.path.join(CWD_PATH, "lib/ChatbotMaker.py"))
}
"""
Account 變數清單
[變數] BASE_PATH         => 根目錄位置
[變數] LIB_PATH          => lib 目錄位置
[變數] INTENT_PATH       => intent 目錄位置
[變數] REPLY_PATH        => reply 目錄位置
[變數] ACCOUNT_DICT      => account.info 內容
[變數] ARTICUT           => ArticutAPI (用法：ARTICUT.parse()。 #需安裝 ArticutAPI.)
[變數] USER_DEFINED_FILE => 使用者自定詞典的檔案路徑
[變數] USER_DEFINED_DICT => 使用者自定詞典內容
"""
BASE_PATH = MODULE_DICT["Account"].BASE_PATH
ACCOUNT_DICT = MODULE_DICT["Account"].ACCOUNT_DICT
COLOR_DICT = MODULE_DICT["ChatbotMaker"].COLOR_DICT
setColor = MODULE_DICT["ChatbotMaker"].setColor
generateReply = MODULE_DICT["ChatbotMaker"].generateReply


LOGO = f"""------------------------------------------
     ##        #######  ##    ## ####
     ##       ##     ## ##   ##   ##
     ##       ##     ## ##  ##    ##
     ##       ##     ## #####     ##
     ##       ##     ## ##  ##    ##
     ##       ##     ## ##   ##   ##
     ########  #######  ##    ## ####
------------------------------------------
      {setColor("Loki ChatbotMaker 回覆產生工具", COLOR_DICT["YELLOW"])}"""

def getMenu():
    chatbotModeDICT = getChatbotModeMsg()
    menuSTR = f"""
------------------------------------------
{setColor("任務清單", COLOR_DICT["CYAN"])}

1. {setColor(chatbotModeDICT["text"], chatbotModeDICT["color"])}
2. 設置 ChatbotMaker Prompt
3. 產生所有文本內容的回覆
4. {setColor("離開", COLOR_DICT["RED"])}
------------------------------------------

請輸入要執行的任務編號[1~4]："""
    return menuSTR

def getChatbotModeMsg():
    return {
        "color": COLOR_DICT["RED"] if ACCOUNT_DICT["chatbot_mode"] else COLOR_DICT["GREEN"],
        "text": "停用 Chatbot 模式" if ACCOUNT_DICT["chatbot_mode"] else "啟用 Chatbot 模式"
    }

def getPrompt():
    promptDICT = {
        "system": "",
        "assistant": "",
        "user": "",
        "resp_header": [],
    }
    if "llm_prompt" in ACCOUNT_DICT:
        for k in promptDICT:
            if k in ACCOUNT_DICT["llm_prompt"]:
                promptDICT[k] = ACCOUNT_DICT["llm_prompt"][k]

    return promptDICT

def setPrompt(promptDICT):
    for k in promptDICT:
        if k in ACCOUNT_DICT["llm_prompt"]:
            ACCOUNT_DICT["llm_prompt"][k] = promptDICT[k]

    return saveAccount()

def saveAccount():
    try:
        json.dump(ACCOUNT_DICT, open(os.path.join(BASE_PATH, "account.info"), "w", encoding="utf-8"), ensure_ascii=False, indent=4)
        return True
    except:
        return False


if __name__ == "__main__":
    print(LOGO)
    while True:
        print(getMenu(), end="")
        index = str(input())
        if index == "1":
            chatbotModeDICT = getChatbotModeMsg()
            ACCOUNT_DICT["chatbot_mode"] = not ACCOUNT_DICT["chatbot_mode"]
            status = saveAccount()
            if status:
                print(setColor(f"[完成] {chatbotModeDICT['text']}", COLOR_DICT["GREEN"]))
            else:
                print(setColor(f"[失敗] {chatbotModeDICT['text']}", COLOR_DICT["RED"]))

        elif index == "2":
            promptDICT = getPrompt()
            print(f"\n{setColor('設置 ChatbotMaker Prompt', COLOR_DICT['CYAN'])}")
            print("------------------------------------------")
            print(f"System: {promptDICT['system']}")
            print(f"Assistant: {promptDICT['assistant']}")
            print(f"User: {promptDICT['user']}")
            print("------------------------------------------")
            while True:
                print("是否調整 Prompt System?[Y/N]: ", end="")
                status = str(input()).upper()
                if status in ["Y", "N"]:
                    if status == "Y":
                        print("System prompt: ", end="")
                        promptDICT["system"] = str(input())
                    break

            while True:
                print("是否調整 Prompt Assistant?[Y/N]: ", end="")
                status = str(input()).upper()
                if status in ["Y", "N"]:
                    if status == "Y":
                        print("Assistant prompt: ", end="")
                        promptDICT["assistant"] = str(input())
                    break

            while True:
                print("是否調整 Prompt User?[Y/N]: ", end="")
                status = str(input()).upper()
                if status in ["Y", "N"]:
                    if status == "Y":
                        print("User prompt: ", end="")
                        promptDICT["user"] = str(input())
                    break

            status = setPrompt(promptDICT)
            if status:
                print(setColor("[完成] 設置 ChatbotMaker Prompt", COLOR_DICT["GREEN"]))
            else:
                print(setColor("[失敗] 設置 ChatbotMaker Prompt", COLOR_DICT["RED"]))

        elif index == "3":
            print(f"\n{setColor('產生所有文本內容的回覆', COLOR_DICT['CYAN'])}")
            print("------------------------------------------")
            status = generateReply()
            if status:
                print(setColor("[完成] 產生所有文本內容的回覆", COLOR_DICT["GREEN"]))
            else:
                print(setColor("[失敗] 產生所有文本內容的回覆", COLOR_DICT["RED"]))

        elif index == "4":
            break