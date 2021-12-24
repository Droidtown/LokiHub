#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki Template For Python3

    [URL] https://nlu.droidtown.co/Loki/BulkAPI/

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
from word2number import w2n
import rapidjson as json
import os
import re
import logging
logging.basicConfig(level=logging.INFO)

import requests
from moneyCode import moneyDICT
from requests import post
from requests import codes
import math
try:
    from intent import Loki_change_currency
except:
    from .intent import Loki_change_currency

BASEPATH = os.path.abspath(os.path.dirname(__file__))
userDICT = json.load(open("account.info".format(BASEPATH), encoding="utf-8"))
LOKI_URL = "https://nlu.droidtown.co/Loki/BulkAPI/"
USERNAME = userDICT["username"]
LOKI_KEY = userDICT["finBot_key"]

# 意圖過濾器說明  Intention filter meaning
# INTENT_FILTER = []        => 比對全部的意圖 (預設) Compare all the intentions (Default)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖 Only compare the intentions in INTENT_FILTER
INTENT_FILTER = []

class LokiResult():
    status = False
    message = ""
    version = ""
    lokiResultLIST = []

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
        #If filterLIST is empty, then the default INTENT_FILTER would be used
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "{} Connection failed.".format(result.status_code)
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

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

def runLoki(inputLIST, filterLIST=[]):
    resultDICT = {}
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # change_currency
                if lokiRst.getIntent(index, resultIndex) == "change_currency":
                    resultDICT = Loki_change_currency.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

    if "msg" in resultDICT:
        print(resultDICT["msg"])

def testIntent():
    # change_currency
    print("[TEST] change_currency")
    inputLIST = ['How much is 100 USD in NTD','How much is $100 USD in Taiwan? ','How much is 100 US dollars in NTD','May I change this into Korean Won?','I would like to change 50 USD into euros','How much is 100 USD to New Taiwan dollar? ','I\'d like to exchange fifty pounds into NTD.','I\'d like to change fifty USD into euros, please.','I would like to change some USD into pounds, please.']
    testLoki(inputLIST, ['change_currency'])
    print("")


def get_key(val):
    '''
    To search the dictionary key with its value
    '''
    for key, value in moneyDICT .items():
        for i in value:
            if i == val:
                return key
    return "key doesn't exist"

def getMoneyCode(inputSTR):
    '''
    Change the usually money
    '''
    upperCaseSTR = inputSTR.upper()
    for key, value in moneyDICT.items():
        if get_key(upperCaseSTR) == key:
            result = get_key(upperCaseSTR)
            return result

def ListToString(MyInput):
    """
    To change list into string
    """
    if isinstance(MyInput,str):
        return(MyInput)
    else:
        return(MyInput[0])

def text2int (textnum, numwords={}):
    '''
    Change text to number, and still have the text
    '''
    if not numwords:
        units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):  numwords[word] = (1, idx)
        for idx, word in enumerate(tens):       numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

    ordinal_words = {'first':1, 'second':2, 'third':3, 'fifth':5, 'eighth':8, 'ninth':9, 'twelfth':12}
    ordinal_endings = [('ieth', 'y'), ('th', '')]

    textnum = textnum.replace('-', ' ')

    current = result = 0
    curstring = ""
    onnumber = False
    for word in textnum.split():
        if word in ordinal_words:
            scale, increment = (1, ordinal_words[word])
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
            onnumber = True
        else:
            for ending, replacement in ordinal_endings:
                if word.endswith(ending):
                    word = "%s%s" % (word[:-len(ending)], replacement)

            if word not in numwords:
                if onnumber:
                    curstring += repr(result + current) + " "
                curstring += word + " "
                result = current = 0
                onnumber = False
            else:
                scale, increment = numwords[word]

                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0
                onnumber = True

    if onnumber:
        curstring += repr(result + current)

    return curstring

def bigSmalltextNumtoFloat(inputSTR):
    if ('million' in inputSTR) or ('billion' in inputSTR) or ("trillion" in inputSTR):
        big_num = ['million', 'billion', 'trillion']
        for big in big_num:
            if big in inputSTR:
                inputSTR_sub = re.sub(big, "SEP", inputSTR)
                inputSTR_sub = text2int(inputSTR_sub)
                inputSTR_sub = re.sub(" point ", ".", inputSTR_sub)
                numSTR = re.sub('[^\d+\.]', "", inputSTR_sub)
                input_subLIST = inputSTR_sub.split("SEP")
                no_numLIST = re.sub('[\d+\.]', '',input_subLIST[0])
                if big == "million":
                    NUM_result = float(numSTR) * 1000000
                if big == "billion":
                    NUM_result = float(numSTR) * 1000000000
                if big == "trillion":
                    NUM_result = float(numSTR) * 1000000000000
                result = no_numLIST.strip(" ") + " " + str(NUM_result) + " " + input_subLIST[1].strip(" ")
                logging.debug(result + "RESULT big number")
                return result
    else:
        inputSTR = text2int(inputSTR)
        inputSTR = re.sub(" point ", ".", inputSTR)
        return inputSTR

def getIntAfterPoint(inputSTR):
    try:
        if re.search(r'(million)|(billion)|(trillion)', inputSTR):
            num_afterPointSTR = re.search(r'(?<=point ).+(?=(million)|(billion)|(trillion))', inputSTR)
            num_afterPointSTR = num_afterPointSTR.group().strip(" ")
            num_afterPointLIST = num_afterPointSTR.split(" ")
            int_afterPointLIST = []
            for num in num_afterPointLIST:
                int_afterPointLIST.append(text2int(num))
                num_joined = "".join(int_afterPointLIST)
                num2intSTR = re.sub(num_afterPointSTR, num_joined, inputSTR)
            num2intSTR = num2intSTR + " "
        elif re.search(r'(million)|(billion)|(trillion)', inputSTR) == None:
            num_afterPointSTR = re.search(r'(?<=point ).+(?=[ ])', inputSTR)
            num_afterPointSTR = num_afterPointSTR.group().strip(" ")
            num_afterPointLIST = num_afterPointSTR.split(" ")
            int_afterPointLIST = []
            for num in num_afterPointLIST:
                int_afterPointLIST.append(text2int(num))
                num_joined = " ".join(int_afterPointLIST)
                num2intSTR = re.sub(num_afterPointSTR, num_joined, inputSTR)
            num2intSTR = num2intSTR + " "
    except:
        num2intSTR = inputSTR
    return num2intSTR



def getExchange(inputSTR):
    """
    Read the inputSTR and exchange the currency
    """

    #inputLIST = [inputSTR]
    if "point" in inputSTR:
        inputSTR = getIntAfterPoint(inputSTR)
        inputLIST = [bigSmalltextNumtoFloat(inputSTR)]
    else:
        inputLIST = [text2int(inputSTR)]
    logging.debug(inputLIST)
    resultDICT = runLoki(inputLIST)
    logging.info(resultDICT)

    #Check whether this is a valid pattern in loki
    if resultDICT == {}:
        print("Sorry! We don't have this pattern")
        return False

    #Check wether source currency, target currency and amount are there
    if resultDICT["src"] == None:
        print("With what currency would you like to exchange?")
    else:
        source_1 = ListToString(resultDICT["src"])
        source_1 = source_1.strip(" ")
        logging.debug(source_1 + " " + "source 1")
    if resultDICT['tgt'] == None:
        print("To which currency would you like?")
    else:
        target_1 = ListToString(resultDICT["tgt"])
        logging.debug(target_1 + " " + "target 1")
    if resultDICT["amt"] == None:
        print("How much would you like to exchange?")
        return False
    elif resultDICT['amt'] == '':
        amount_1 = w2n.word_to_num(resultDICT["src"][0])
    else:
        logging.debug(resultDICT["amt"])
        amount_1 = ListToString(resultDICT["amt"])
    logging.debug(amount_1+ " " + "amount 1")

    #Change cents into US dollars (all cents are considered as US dollar)
    source_1 = source_1.upper()
    if source_1 in [("CENT"),("CENTS"), ("PENNIES"), ("PENNY")]:
        amount_1 = float(amount_1)*0.01
        logging.debug(str(amount_1)+ " " + "amount 2")


    #get the change rate
    response = requests.get("https://tw.rter.info/capi.php")
    rateDICT = response.json()
    logging.debug(getMoneyCode(source_1))
    Source= "USD"+getMoneyCode(source_1)
    logging.debug(Source)
    Target = "USD"+getMoneyCode(target_1)
    logging.debug(Target)
    Amount = float(amount_1)
    logging.debug(Amount)

    #search in dictionary
    Source_rate = rateDICT[Source]["Exrate"]
    #print(Source_rate)
    Target_rate = rateDICT[Target]["Exrate"]
    #print(Target_rate)

    #Exchange!
    Result = Amount*(Target_rate/Source_rate)
    Last_Result = str(round(Result, 2)) +  " " + getMoneyCode(target_1)

    if target_1 in [("cent"), ("CENT"), ("Cent"),("cents"), ("CENTS"), ("Cents")]:
        Result_centFLOAT = Result*100
        Last_Result = str(round(Result_centFLOAT, 2)) +  " " + target_1
    return Amount,  getMoneyCode(source_1), Last_Result

if __name__ == "__main__":
    ## 測試所有意圖 Test all the intention
    ##testIntent()

    # 測試其它句子 Test other sentences
    inputSTR = "Could I exchange 300 pennies to NTD"


    try:
        exchangeSTR = getExchange(inputSTR)
        logging.debug(exchangeSTR[0])
        logging.debug(exchangeSTR[1])
        logging.debug(exchangeSTR[2])
        if isinstance(exchangeSTR[2], str):
            print("You could exchange" + " "+ str(exchangeSTR[0]) + " "+ exchangeSTR[1] + " to " +  exchangeSTR[2])
    except:
        print("Please check again")


    #測試通過 Pass the test
    # How much is 100 USD in NTD
    #How much is 100 EUR into TWD
    #How much is $100 USD in Taiwan?
    #How much is 100 US dollars in NTD
    #May I change this into Korean Won?
    #I would like to change 50 USD into euros
    #How much is 100 USD to New Taiwan dollar?
    #I would like to change 50 USD to New Taiwan dollars.
    #How much is 100 USD into MXN
    #How much is 100 US dollars in NTD
    #I would like to change some USD into pounds, please.
