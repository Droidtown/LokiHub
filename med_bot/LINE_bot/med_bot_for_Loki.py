#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 2.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No Match Intent!"
                }
            ]
        }
"""

import requests
from account_info import accountInfoDICT
from reference import departmentDICT
from reference import emergencyLIST
from reference import otherLIST
import logging
logging.basicConfig(level=logging.DEBUG)

try:
    from intent import Loki_body_part
    from intent import Loki_symptom
except:
    from .intent import Loki_body_part
    from .intent import Loki_symptom


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = accountInfoDICT["USERNAME"]
LOKI_KEY = accountInfoDICT["LOKI_KEY"]

# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []

        try:
            result = requests.post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": INTENT_FILTER
            })

            if result.status_code == requests.codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "Connect failed."
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST):
    resultDICT = {}
    lokiRst = LokiResult(inputLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # Emergency
                if lokiRst.getIntent(index, resultIndex) == "Emergency":
                    resultDICT = Loki_Emergency.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # Gender
                if lokiRst.getIntent(index, resultIndex) == "Gender":
                    resultDICT = Loki_Gender.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # body_part
                if lokiRst.getIntent(index, resultIndex) == "body_part":
                    resultDICT = Loki_body_part.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # symptom
                if lokiRst.getIntent(index, resultIndex) == "symptom":
                    resultDICT = Loki_symptom.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT



#根據部位或症狀查詢科別，回傳科別字串
def FindDepartment(inputSTR): 
    medDICT = {"dept":[]}
    resultDICT = runLoki([inputSTR])
    logging.debug(f"show resultDICT {resultDICT}")
    #print(f"{resultDICT} first")
    try:     
        for e in departmentDICT.keys():
            logging.debug(f"here - bodypart")
            #print("here 1")
            if resultDICT["bodypart"]  in departmentDICT[e]:
                medDICT["dept"].append(e)
                logging.debug(f"show medDICT {medDICT['dept']}bodypart")
                #print(f"{medDICT['dept']} ver 1")
    except:
        logging.debug("here bodypart not pass")
        pass 
    try:
        for e in departmentDICT.keys():
            logging.debug("here - symptom")
            #print("here 2 ")
            #print(departmentDICT.keys())
            if resultDICT["symptom"] in departmentDICT[e]:
                medDICT["dept"].append(e)
                logging.debug(f"show medDICT {medDICT['dept']} symptom")
                #print(f"{medDICT['dept']} ver 2")
    except:
        logging.debug("here symptom not pass")
        #print("here 3")
        pass
    
    if medDICT["dept"] == []:
        for e in departmentDICT.keys():
            for x in departmentDICT[e]:
                if x in inputSTR:
                    medDICT["dept"].append(e)
                else:
                    pass

    if any (eme in inputSTR for eme in emergencyLIST):
        medDICT["dept"].append("立即打119")
    
    if medDICT["dept"] == []:
        medDICT["dept"].append("試試看家醫科")    
    
    if len(medDICT["dept"]) == 2 and medDICT["dept"][0] == medDICT["dept"][1]:
        medDICT["dept"].append(medDICT["dept"][0])

    if len(medDICT["dept"]) == 2 and medDICT["dept"][0] != medDICT["dept"][1]:
        medDICT["dept"].append(["dept"][0]+"或"+medDICT["dept"][1])
    return medDICT["dept"][0]
    


# in this function, we set a dictionary for each response
# a special key 'result' is set to the dictionary which appears when the user mentions about their children
def Result(inputSTR):
    dep=FindDepartment(inputSTR)
    if any(other in inputSTR for other in otherLIST ):
        if any(e in inputSTR for e in ["咬","啄","抓"]):
            responseDICT = {"msg": "請去{}\n12歲以下孩童請去小兒科".format(dep)}
        else:
            responseDICT = {"msg": "你確定是人類嗎？ 目前只有建制人的醫療分科\n如果真的是人類請去{}\n12歲以下孩童請去小兒科".format(dep)}
    elif "試試" in dep:
        responseDICT = {"msg": "請多說說你不舒服的地方，要不然你可以試看看家醫科\n12歲以下孩童請去小兒科"}
    else:
        responseDICT = {"msg": "請去{}\n12歲以下孩童請去小兒科".format(dep)}
    return responseDICT    
        
        
    
if __name__ == "__main__":
    inputSTR = "我心情鬱悶"
    print(Result(inputSTR))