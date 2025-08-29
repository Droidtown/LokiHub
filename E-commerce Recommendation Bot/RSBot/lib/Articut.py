#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from requests import post
from time import sleep
import json
import sys

class Articut():
    MAX_LEN = 5000
    RETRY_COUNT = 1
    RETRY_DELAY = 10 # 10 sec
    fileSizeMb = 10    # 10 MB
    fileSizeLimit = fileSizeMb * 1024 * 1024

    def __init__(self, username="", apikey="", version="latest", level="lv2", url="https://nlu.droidtown.co"):
        self.username = username
        self.apikey = apikey
        self.version = version
        self.level = level
        self.url = url

    def parse(self, inputSTR, userDefinedDictFILE=None):
        url = "{}/Articut_EN/API/".format(self.url)
        payload = {"username": self.username,
                   "api_key": self.apikey,
                   "version": self.version,
                   "level": self.level}

        if userDefinedDictFILE:
            try:
                userDefinedFile = json.load(open(userDefinedDictFILE, "r", encoding="utf-8"))
                if sys.getsizeof(json.dumps(userDefinedFile)) <= self.fileSizeLimit:
                    if type(userDefinedFile) == dict:
                        payload["user_defined_dict_file"] = userDefinedFile
                    else:
                        print("User Defined File must be dict type.")
                        return {"status": False, "msg": "UserDefinedDICT Parsing ERROR. Please check your the format and encoding."}
                else:
                    print("Maximum file size limit is {} MB.".format(self.fileSizeMb))
                    return {"status": False, "msg": "Maximum UserDefinedDICT file size exceeded! (UserDefinedDICT file shall be samller than {} MB.)".format(self.fileSizeMb)}
            except Exception as e:
                print("User Defined File Loading Error.")
                print(str(e))
                return {"status": False, "msg": "UserDefinedDICT Parsing ERROR. Please check your the format and encoding"}

        resultDICT = {}
        count = 0
        inputLIST = self._getInputLIST(inputSTR)
        for x in inputLIST:
            payload["input_str"] = x
            retry_count = 0
            while True:
                try:
                    responseDICT = post(url, json=payload)
                    if responseDICT.status_code == 200:
                        responseDICT = responseDICT.json()
                        if not responseDICT["status"]:
                            return responseDICT

                        if resultDICT:
                            resultDICT["exec_time"] += responseDICT["exec_time"]
                            if "word_count_balance" in responseDICT:
                                resultDICT["word_count_balance"] = responseDICT["word_count_balance"]
                            resultDICT["result_obj"].extend(responseDICT["result_obj"])
                            resultDICT["result_pos"].extend(responseDICT["result_pos"])
                            resultDICT["result_segmentation"] += "/{}".format(responseDICT["result_segmentation"])
                        else:
                            resultDICT = responseDICT
                        count += len(x)
                    else:
                        return responseDICT

                    break

                except Exception as e:
                    # 最多嘗試 RETRY_COUNT 次
                    if retry_count < self.RETRY_COUNT:
                        retry_count += 1
                        sleep(self.RETRY_DELAY)
                    else:
                        return {"status": False, "msg": "Connection timeout."}

        return resultDICT

    def _getInputLIST(self, inputSTR):
        '''
        取得長度不大於 MAX_LEN 的 input 列表
        '''
        BREAK_LIST = ["。", "？", "！", "?", "!", "\n"]

        inputLIST = []
        while True:
            if len(inputSTR) > self.MAX_LEN:
                tempSTR = inputSTR[:self.MAX_LEN]
                index = 0
                for x in BREAK_LIST:
                    lastIndex = tempSTR.rfind(x) + 1
                    if lastIndex > index:
                        index = lastIndex
                if index == 0:
                    index = self.MAX_LEN
                inputLIST.append(inputSTR[:index])
                inputSTR = inputSTR[index:]
            else:
                inputLIST.append(inputSTR)
                break

        return inputLIST