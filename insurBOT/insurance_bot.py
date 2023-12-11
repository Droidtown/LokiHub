#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 4.0 Template For Python3

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
                    "msg": "No matching Intent."
                }
            ]
        }
"""

from requests import post
from requests import codes
import json
import math
import os
import re
import sys
try:
    from intent import Loki_feature
    from intent import Loki_feature_v2
    from intent import Loki_info_lowBudget
    from intent import Loki_info_traffic
    from intent import Loki_insur_life
    from intent import Loki_insur_accident
    from intent import Loki_insur_travel
    from intent import Loki_info_days
    from intent import Loki_way_to_pay2
    from intent import Loki_info_job
    from intent import Loki_info_highBudget
    from intent import Loki_benefit
    from intent import Loki_way_to_pay
    from intent import Loki_info_indentity
    from intent import Loki_age
    from intent import Loki_travel_period
    from intent import Loki_change_person
    from intent import Loki_acc_benefit
    from intent import Loki_life_period
    from intent import Loki_no_offer
    from intent import Loki_strange
    from intent import Loki_switch_insur
except:
    from .intent import Loki_feature
    from .intent import Loki_feature_v2
    from .intent import Loki_info_lowBudget
    from .intent import Loki_info_traffic
    from .intent import Loki_insur_life
    from .intent import Loki_insur_accident
    from .intent import Loki_insur_travel
    from .intent import Loki_info_days
    from .intent import Loki_way_to_pay2
    from .intent import Loki_info_job
    from .intent import Loki_info_highBudget
    from .intent import Loki_benefit
    from .intent import Loki_way_to_pay
    from .intent import Loki_info_indentity
    from .intent import Loki_age
    from .intent import Loki_travel_period
    from .intent import Loki_change_person
    from .intent import Loki_acc_benefit
    from .intent import Loki_life_period
    from .intent import Loki_no_offer
    from .intent import Loki_strange
    from .intent import Loki_switch_insur


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
try:
    accountInfo = json.load(open(os.path.join(os.path.dirname(__file__), "account.info"), encoding="utf-8"))
    USERNAME = accountInfo["username"]
    LOKI_KEY = accountInfo["loki_key"]
except Exception as e:
    print("[ERROR] AccountInfo => {}".format(str(e)))
    USERNAME = ""
    LOKI_KEY = ""

# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []
INPUT_LIMIT = 20

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
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
                    if "word_count_balance" in result:
                        self.balance = result["word_count_balance"]
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

def runLoki(inputLIST, filterLIST=[], refDICT={}):
    resultDICT = refDICT
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            lokiResultDICT = {"type":[]}
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # feature
                if lokiRst.getIntent(index, resultIndex) == "feature":
                    lokiResultDICT = Loki_feature.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # feature_v2
                if lokiRst.getIntent(index, resultIndex) == "feature_v2":
                    lokiResultDICT = Loki_feature_v2.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # info_lowBudget
                if lokiRst.getIntent(index, resultIndex) == "info_lowBudget":
                    lokiResultDICT = Loki_info_lowBudget.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # info_traffic
                if lokiRst.getIntent(index, resultIndex) == "info_traffic":
                    lokiResultDICT = Loki_info_traffic.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # insur_life
                if lokiRst.getIntent(index, resultIndex) == "insur_life":
                    lokiResultDICT = Loki_insur_life.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)


                # insur_accident
                if lokiRst.getIntent(index, resultIndex) == "insur_accident":
                    lokiResultDICT = Loki_insur_accident.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # insur_travel
                if lokiRst.getIntent(index, resultIndex) == "insur_travel":
                    lokiResultDICT = Loki_insur_travel.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getPattern(index, resultIndex), lokiResultDICT, refDICT)
                    if "accident" in lokiResultDICT:
                        lokiResultDICT['type'].remove('accident')
                    if "life" in lokiResultDICT:
                        lokiResultDICT['type'].remove("life")
                # info_days
                if lokiRst.getIntent(index, resultIndex) == "info_days":
                    lokiResultDICT = Loki_info_days.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getPattern(index, resultIndex), lokiResultDICT, refDICT)

                # way_to_pay2
                if lokiRst.getIntent(index, resultIndex) == "way_to_pay2":
                    lokiResultDICT = Loki_way_to_pay2.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # info_job
                if lokiRst.getIntent(index, resultIndex) == "info_job":
                    lokiResultDICT = Loki_info_job.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)


                # info_highBudget
                if lokiRst.getIntent(index, resultIndex) == "info_highBudget":
                    lokiResultDICT = Loki_info_highBudget.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # benefit
                if lokiRst.getIntent(index, resultIndex) == "benefit":
                    lokiResultDICT = Loki_benefit.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)


                # way_to_pay
                if lokiRst.getIntent(index, resultIndex) == "way_to_pay":
                    lokiResultDICT = Loki_way_to_pay.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # info_indentity
                if lokiRst.getIntent(index, resultIndex) == "info_indentity":
                    lokiResultDICT = Loki_info_indentity.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # age
                if lokiRst.getIntent(index, resultIndex) == "age":
                    lokiResultDICT = Loki_age.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # travel_period
                if lokiRst.getIntent(index, resultIndex) == "travel_period":
                    lokiResultDICT = Loki_travel_period.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)
                
                # change_person
                if lokiRst.getIntent(index, resultIndex) == "change_person":
                    lokiResultDICT = Loki_change_person.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getPattern(index, resultIndex), lokiResultDICT, refDICT)
                
                # acc_benefit
                if lokiRst.getIntent(index, resultIndex) == "acc_benefit":
                    lokiResultDICT = Loki_acc_benefit.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)
                
                # life_period
                if lokiRst.getIntent(index, resultIndex) == "life_period":
                    lokiResultDICT = Loki_life_period.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # no_offer
                if lokiRst.getIntent(index, resultIndex) == "no_offer":
                    lokiResultDICT = Loki_no_offer.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)                
                
                # strange
                if lokiRst.getIntent(index, resultIndex) == "strange":
                    lokiResultDICT = Loki_strange.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # switch_insur
                if lokiRst.getIntent(index, resultIndex) == "switch_insur":
                    lokiResultDICT = Loki_switch_insur.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

            # save lokiResultDICT to resultDICT
            resultDICT = {"type":[]}
            for k in lokiResultDICT:
                if type(lokiResultDICT[k]) == list: 
                    resultDICT[k] = lokiResultDICT[k]
                else:
                    resultDICT[k] = [lokiResultDICT[k]]
    else:
        resultDICT["msg"] = lokiRst.getMessage()
    return resultDICT

def execLoki(content, filterLIST=[], splitLIST=[], refDICT={}):
    """
    input
        content       STR / STR[]    要執行 loki 分析的內容 (可以是字串或字串列表)
        filterLIST    STR[]          指定要比對的意圖 (空列表代表不指定)
        splitLIST     STR[]          指定要斷句的符號 (空列表代表不指定)
                                     * 如果一句 content 內包含同一意圖的多個 utterance，請使用 splitLIST 切割 content
        refDICT       DICT           參考內容

    output
        resultDICT    DICT           合併 runLoki() 的結果

    e.g.
        splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？")                      # output => ["今天天氣"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？", splitLIST=splitLIST) # output => ["今天天氣", "後天氣象"]
        resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"])                # output => ["今天天氣", "後天氣象"]
    """
    resultDICT = refDICT
    if resultDICT is None:
        resultDICT = {}

    contentLIST = []
    if type(content) == str:
        contentLIST = [content]
    if type(content) == list:
        contentLIST = content

    if contentLIST:
        if splitLIST:
            # 依 splitLIST 做分句切割
            splitPAT = re.compile("[{}]".format("".join(splitLIST)))
            inputLIST = []
            for c in contentLIST:
                tmpLIST = splitPAT.split(c)
                inputLIST.extend(tmpLIST)
            # 去除空字串
            while "" in inputLIST:
                inputLIST.remove("")
        else:
            # 不做分句切割處理
            inputLIST = contentLIST

        # 依 INPUT_LIMIT 限制批次處理
        for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
            resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST=filterLIST, refDICT=refDICT)
            if "msg" in resultDICT:
                break

    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

    if "msg" in resultDICT:
        print(resultDICT["msg"])

def testIntent():
    # feature
    print("[TEST] feature")
    inputLIST = ['何謂壽險保障商品','有什麼是壽險保障商品','新iCarry傷害保險有什麼優點','新iCarry傷害保險有何特點？','新iCarry傷害保險的特色為何','心e路平安傷害保險有何優點','心e路平安傷害保險有何特色','心e路平安傷害保險有何特點','新iCarry傷害保險有哪些特點？','新iCarry傷害保險的優點是什麼','心e路平安傷害保險有哪些好處','心e路平安傷害保險的優點為何','說說心e路平安傷害保險的優點','說說心e路平安傷害保險的特色','說說心e路平安傷害保險的特點','新iCarry傷害保險具有哪些特點？','新iCarry傷害保險的特點是什麼？','新iCarry傷害保險的特點有哪些？','告訴我心e路平安傷害保險的優點','告訴我心e路平安傷害保險的特色','告訴我心e路平安傷害保險的特點','哪些是心e路平安傷害保險的優點','哪些是心e路平安傷害保險的特色','哪些是心e路平安傷害保險的特點','心e路平安傷害保險的優點有哪些','心e路平安傷害保險的好處是什麼','心e路平安傷害保險的特色是什麼','心e路平安傷害保險的特色有哪些','想知道心e路平安傷害保險的優點','想知道心e路平安傷害保險的特色','想知道心e路平安傷害保險的特點','心e路平安傷害保險是有什麼優點?','心e路平安傷害保險是有什麼特色?','心e路平安傷害保險是有什麼特點?','心e路平安傷害保險會有哪些優點?','心e路平安傷害保險會有哪些特色?','心e路平安傷害保險會有哪些特點?','新iCarry傷害保險有哪些主要特點？','有哪些是心e路平安傷害保險的優點','有哪些是心e路平安傷害保險的特色','有哪些是心e路平安傷害保險的特點','新iCarry傷害保險有哪些特色和優勢？','心e路平安傷害保險的優點可以告訴我嗎','心e路平安傷害保險的特色可以告訴我嗎','心e路平安傷害保險的特點可以告訴我嗎']
    testLoki(inputLIST, ['feature'])
    print("")

    # feature_v2
    print("[TEST] feature_v2")
    inputLIST = ['壽險的特色','是會有哪些特色','特色是會有哪些']
    testLoki(inputLIST, ['feature_v2'])
    print("")

    # info_lowBudget
    print("[TEST] info_lowBudget")
    inputLIST = ['小額','低預算','比較低','預算少','保一般的','小資方案','預算不多','預算比較少','預算沒那麼多']
    testLoki(inputLIST, ['info_lowBudget'])
    print("")

    # info_traffic
    print("[TEST] info_traffic")
    inputLIST = ['通勤方式','在假日期間','與交通有關','在假日的時候','搭乘大眾運輸']
    testLoki(inputLIST, ['info_traffic'])
    print("")

    # insur_life
    print("[TEST] insur_life")
    inputLIST = ['壽險','買新房','一家之主','單親家庭','怕留給家人','是一位父親','保便宜的壽險','隔代教養家庭','擔心自己的家人','是一位單親媽媽','只有一個人在賺錢','為家裡的經濟支柱','給家人多一份保障','使家庭生活陷入困境','死後想要給家人保障']
    testLoki(inputLIST, ['insur_life'])
    print("")

    # insur_accident
    print("[TEST] insur_accident")
    inputLIST = ['恢復','意外險','上學過程','在外奔走','工作考量','考量工作','應對突發狀況','日常生活不便','降低經濟壓力','保便宜的意外險','幫忙負擔醫療費','我的工作較危險','高危險性的工作','工作遇到一些事故','覺得意外無處不在','獲得廣泛的意外保障','讓我在工作的時候有保障']
    testLoki(inputLIST, ['insur_accident'])
    print("")

    # insur_travel
    print("[TEST] insur_travel")
    inputLIST = ['出去玩','旅平險','於國外旅行','於德國旅行','是一個海鷗族','保便宜的旅平險','保旅遊相關的險','到新竹參加活動']
    testLoki(inputLIST, ['insur_travel'])
    print("")

    # info_days
    print("[TEST] info_days")
    inputLIST = ['一天','德國一年','於德國旅行一年']
    testLoki(inputLIST, ['info_days'])
    print("")

    # way_to_pay2
    print("[TEST] way_to_pay2")
    inputLIST = ['付款選項有哪些','有哪些支付方式','可以用什麼方式付款','是否可以用街口繳費','可以採用哪些支付方式','可以用街口電子支付嗎','可以選擇哪些結算方式','街口電子支付可以用嗎']
    testLoki(inputLIST, ['way_to_pay2'])
    print("")

    # info_job
    print("[TEST] info_job")
    inputLIST = ['內勤','是捕魚的','為一工人','從事服務業','職業是漁夫','是一位服務員','以種植蔬果為生','在外商公司上班']
    testLoki(inputLIST, ['info_job'])
    print("")

    # info_highBudget
    print("[TEST] info_highBudget")
    inputLIST = ['有家庭','加倍保障','多點保障','多一點保障','涵蓋範圍廣','理賠比較多','工作危險性高']
    testLoki(inputLIST, ['info_highBudget'])
    print("")

    # benefit
    print("[TEST] benefit")
    inputLIST = ['會給付','給付項目','怎麼樣理賠','有哪些保障','給付的項目']
    testLoki(inputLIST, ['benefit'])
    print("")

    # way_to_pay
    print("[TEST] way_to_pay")
    inputLIST = ['用現金付款','用line pay繳費']
    testLoki(inputLIST, ['way_to_pay'])
    print("")

    # info_indentity
    print("[TEST] info_indentity")
    inputLIST = ['捕魚','上班族','低收入戶','家庭主婦','經濟弱勢','經濟有困難']
    testLoki(inputLIST, ['info_indentity'])
    print("")

    # age
    print("[TEST] age")
    inputLIST = ['20歲','我20','20足歲','到50歲','從20歲','我今年20','20歲到50歲']
    testLoki(inputLIST, ['age'])
    print("")

    # travel_period
    print("[TEST] travel_period")
    inputLIST = ['留學10天','遊學10天','赴德180天','出國玩10天','去國外10天','去日本10天','國內玩10天','國外玩10天','國外出差10天','國外旅遊10天','在台灣玩10天','打工度假10天','要去國外10天']
    testLoki(inputLIST, ['travel_period'])
    print("")


if __name__ == "__main__":
    # 測試所有意圖
    #testIntent()
    # inputSTR = "我想要去印度一星期，我33歲"
    # resultDICT = execLoki(inputSTR)
    inputSTR = ""
    #我想要去去韓國旅行一星期，我33歲
    while inputSTR != "s":
        inputSTR = input("sentence")
        resultDICT = execLoki(inputSTR)
        print(resultDICT, '\n\n')