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
    "Account": import_from_path("RSBot_lib_Account", os.path.join(CWD_PATH, "lib/Account.py")),
    "ChatbotMaker": import_from_path("RSBot_lib_ChatbotMaker", os.path.join(CWD_PATH, "lib/ChatbotMaker.py"))
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
 {setColor("Loki ChatbotMaker Reply Generation Tool", COLOR_DICT["YELLOW"])}"""

def getMenu():
    chatbotModeDICT = getChatbotModeMsg()
    menuSTR = f"""
------------------------------------------
{setColor("Task", COLOR_DICT["CYAN"])}

1. {setColor(chatbotModeDICT["text"], chatbotModeDICT["color"])}
2. Set ChatbotMaker prompt
3. Generate replies for all text content
4. {setColor("Exit", COLOR_DICT["RED"])}
------------------------------------------

Enter your choice [1~4]: """
    return menuSTR

def getChatbotModeMsg():
    return {
        "color": COLOR_DICT["RED"] if ACCOUNT_DICT["chatbot_mode"] else COLOR_DICT["GREEN"],
        "text": "Disable Chatbot mode" if ACCOUNT_DICT["chatbot_mode"] else "Enable Chatbot mode"
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
                print(setColor(f"[Success] {chatbotModeDICT['text']}", COLOR_DICT["GREEN"]))
            else:
                print(setColor(f"[Failure] {chatbotModeDICT['text']}", COLOR_DICT["RED"]))

        elif index == "2":
            promptDICT = getPrompt()
            print(f"\n{setColor('Set ChatbotMaker prompt', COLOR_DICT['CYAN'])}")
            print("------------------------------------------")
            print(f"System: {promptDICT['system']}")
            print(f"Assistant: {promptDICT['assistant']}")
            print(f"User: {promptDICT['user']}")
            print("------------------------------------------")
            while True:
                print("Edit Prompt System or not?[Y/N]: ", end="")
                status = str(input()).upper()
                if status in ["Y", "N"]:
                    if status == "Y":
                        print("System prompt: ", end="")
                        promptDICT["system"] = str(input())
                    break

            while True:
                print("Edit Prompt Assistant or not?[Y/N]: ", end="")
                status = str(input()).upper()
                if status in ["Y", "N"]:
                    if status == "Y":
                        print("Assistant prompt: ", end="")
                        promptDICT["assistant"] = str(input())
                    break

            while True:
                print("Edit Prompt User or not?[Y/N]: ", end="")
                status = str(input()).upper()
                if status in ["Y", "N"]:
                    if status == "Y":
                        print("User prompt: ", end="")
                        promptDICT["user"] = str(input())
                    break

            status = setPrompt(promptDICT)
            if status:
                print(setColor("[Success] Set ChatbotMaker prompt", COLOR_DICT["GREEN"]))
            else:
                print(setColor("[Failure] Set ChatbotMaker prompt", COLOR_DICT["RED"]))

        elif index == "3":
            print(f"\n{setColor('Generate replies for all text content', COLOR_DICT['CYAN'])}")
            print("------------------------------------------")
            status = generateReply()
            if status:
                print(setColor("[Success] Generate replies for all text content", COLOR_DICT["GREEN"]))
            else:
                print(setColor("[Failure] Generate replies for all text content", COLOR_DICT["RED"]))

        elif index == "4":
            break