#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 3.0 Template For Python3

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

from requests import post
from requests import codes
import math
import re
import json
import rockClimbingFunc
import pandas as pd
try:
    from intent import Loki_gym_name
    from intent import Loki_gym_city
    from intent import Loki_whatIs
    from intent import Loki_location
    from intent import Loki_equipment_price
    from intent import Loki_equipment_whereGet
    from intent import Loki_gym_howMany
    from intent import Loki_rules
    from intent import Loki_gym_time
    from intent import Loki_chat
    from intent import Loki_equipment_list
    from intent import Loki_equipment_yesNo
    from intent import Loki_gym_distance
    from intent import Loki_gym_yesNo
    from intent import Loki_rock
    from intent import Loki_gym_price
except:
    from .intent import Loki_gym_name
    from .intent import Loki_gym_city
    from .intent import Loki_whatIs
    from .intent import Loki_location
    from .intent import Loki_equipment_price
    from .intent import Loki_equipment_whereGet
    from .intent import Loki_gym_howMany
    from .intent import Loki_rules
    from .intent import Loki_gym_time
    from .intent import Loki_chat
    from .intent import Loki_equipment_list
    from .intent import Loki_equipment_yesNo
    from .intent import Loki_gym_distance
    from .intent import Loki_gym_yesNo
    from .intent import Loki_rock
    from .intent import Loki_gym_price

accountDICT = json.load(open("account.info", encoding= "utf-8"))
LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = accountDICT["username"]
LOKI_KEY = accountDICT["lokiKey"]
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

def runLoki(inputLIST, filterLIST=[]):
    # 將 intent 會使用到的 key 預先設爲空列表
    resultDICT = {
        "_person_loc":"", # gym city, gym price
        "_what_is":"",
        "_gym_name": "",
    }
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # gym_name
                if lokiRst.getIntent(index, resultIndex) == "gym_name":
                    resultDICT = Loki_gym_name.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # whatIs
                if lokiRst.getIntent(index, resultIndex) == "whatIs":
                    resultDICT = Loki_whatIs.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # location
                if lokiRst.getIntent(index, resultIndex) == "location":
                    resultDICT = Loki_location.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # equipment_price
                if lokiRst.getIntent(index, resultIndex) == "equipment_price":
                    resultDICT = Loki_equipment_price.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # equipment_whereGet
                if lokiRst.getIntent(index, resultIndex) == "equipment_whereGet":
                    resultDICT = Loki_equipment_whereGet.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # gym_howMany
                if lokiRst.getIntent(index, resultIndex) == "gym_howMany":
                    resultDICT = Loki_gym_howMany.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # rules
                if lokiRst.getIntent(index, resultIndex) == "rules":
                    resultDICT = Loki_rules.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # gym_time
                if lokiRst.getIntent(index, resultIndex) == "gym_time":
                    resultDICT = Loki_gym_time.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # chat
                if lokiRst.getIntent(index, resultIndex) == "chat":
                    resultDICT = Loki_chat.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # equipment_list
                if lokiRst.getIntent(index, resultIndex) == "equipment_list":
                    resultDICT = Loki_equipment_list.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # equipment_yesNo
                if lokiRst.getIntent(index, resultIndex) == "equipment_yesNo":
                    resultDICT = Loki_equipment_yesNo.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # gym_distance
                if lokiRst.getIntent(index, resultIndex) == "gym_distance":
                    resultDICT = Loki_gym_distance.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # gym_city
                if lokiRst.getIntent(index, resultIndex) == "gym_city":
                    resultDICT = Loki_gym_city.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)
                
                # gym_yesNo
                if lokiRst.getIntent(index, resultIndex) == "gym_yesNo":
                    resultDICT = Loki_gym_yesNo.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # rock
                if lokiRst.getIntent(index, resultIndex) == "rock":
                    resultDICT = Loki_rock.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # gym_price
                if lokiRst.getIntent(index, resultIndex) == "gym_price":
                    resultDICT = Loki_gym_price.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def execLoki(content, filterLIST=[], splitLIST=[]):
    """
    input
        content       STR / STR[]    要執行 loki 分析的內容 (可以是字串或字串列表)
        filterLIST    STR[]          指定要比對的意圖 (空列表代表不指定)
        splitLIST     STR[]          指定要斷句的符號 (空列表代表不指定)
                                     * 如果一句 content 內包含同一意圖的多個 utterance，請使用 splitLIST 切割 content

    output
        resultDICT    DICT           合併 runLoki() 的結果，請先設定 runLoki() 的 resultDICT 初始值

    e.g.
        splitLIST = ["！", "，", "。", "？", "!", ",", "
", "；", "　", ";"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？")                      # output => ["今天天氣"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？", splitLIST=splitLIST) # output => ["今天天氣", "後天氣象"]
        resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"])                # output => ["今天天氣", "後天氣象"]
    """
    contentLIST = []
    if type(content) == str:
        contentLIST = [content]
    if type(content) == list:
        contentLIST = content

    resultDICT = {}
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
            lokiResultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)
            if "msg" in lokiResultDICT:
                return lokiResultDICT

            # 將 lokiResultDICT 結果儲存至 resultDICT
            for k in lokiResultDICT:
                if k not in resultDICT:
                    resultDICT[k] = []
                resultDICT[k].extend([lokiResultDICT[k]])

    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

    if "msg" in resultDICT:
        print(resultDICT["msg"])

def testIntent():
    # gym_name
    print("[TEST] gym_name")
    inputLIST = ['中部岩館有哪些','台中岩館有哪些','台中有哪些岩館','東部有哪些岩館','南部上攀可以去哪','台北哪裡可以抱石','台北哪裡可以攀岩','臺中上攀可以去哪','中部上攀可以去哪裡','台中上攀可以去哪裡','台中攀岩可以去哪裡','台中有哪些上攀岩館','哪幾間岩館有速度攀','東部攀岩可以去哪裡','東部有哪些上攀岩館','那東部有哪些岩館呢','台北哪些地方可以攀岩','台北哪些岩館可以上攀','台北有名的岩館','東部哪些岩館可以抱石','東部有名的岩館']
    testLoki(inputLIST, ['gym_name'])
    print("")

    # whatIs
    print("[TEST] whatIs")
    inputLIST = ['jug是什麼？','攀岩是什麼','那是什麼？','什麼是攀岩？','什麼是星光票？','星光票的意思是？']
    testLoki(inputLIST, ['whatIs'])
    print("")

    # equipment_price
    print("[TEST] equipment_price")
    inputLIST = ['岩鞋多貴？','岩鞋很貴嗎？','岩鞋要價多少？','岩鞋要多少錢？','租岩鞋要花多少','多少錢租得到岩鞋','岩鞋大概多少錢？','買岩鞋要花多少？','多少錢可以租到岩鞋','多少錢買得到岩鞋？','多少錢能買得到岩鞋？','花多少才租得到岩鞋？','花多少才買得到岩鞋？','買岩鞋需要花到四個小朋友嗎？']
    testLoki(inputLIST, ['equipment_price'])
    print("")

    # gym_city
    print("[TEST] gym_city")
    inputLIST = ['紅石資訊','紅石電話','double 8在哪裡','紅石聯絡方式','紅石電話號碼','double 8在哪個縣市','哪裡有速度攀場館','東部哪裡有速度攀','中部哪裡有上攀岩館','新竹紅石的地址是？','新竹紅石的電話多少','台灣哪些縣市有岩館呢','哪個縣市有速度攀場館','我需要新竹紅石的電話','新竹紅石的電話是幾號','可以給我double 8的地址嗎','可以告訴我double 8的地址嗎','可以給我double 8岩館的地址嗎','可以告訴我double 8岩館的地址嗎']
    testLoki(inputLIST, ['gym_city'])
    print("")

    # equipment_whereGet
    print("[TEST] equipment_whereGet")
    inputLIST = ['哪裡可以租岩粉','哪裡可以買岩粉','哪裡租得到岩粉','哪裡買得到岩粉','哪裡可以買到岩粉','岩粉可以去哪買？','岩粉哪裡買得到？','你知道岩粉要去哪買嗎','岩粉哪裡可以租得到？','岩粉哪裡可以買得到？','你知道可以去哪買岩粉嗎','你知道岩粉哪裡租得到嗎','你知道岩粉哪裡買得到嗎']
    testLoki(inputLIST, ['equipment_whereGet'])
    print("")

    # gym_howMany
    print("[TEST] gym_howMany")
    inputLIST = ['新竹有多少岩館','新竹有幾間岩館','東部有多少岩館','東部有幾間岩館']
    testLoki(inputLIST, ['gym_howMany'])
    print("")

    # location
    print("[TEST] location")
    inputLIST = ['台中','我在台中','我在東部','台北市大安區','猩猩縣豬豬市悟淨路141號','我在猩猩縣豬豬市悟淨路141號']
    testLoki(inputLIST, ['location'])
    print("")

    # rules
    print("[TEST] rules")
    inputLIST = ['攀岩有規則嗎','抱石要注意什麼','攀岩有哪些規則','上攀的規則是什麼','上攀的規則有哪些','上攀要小心什麼？','攀岩有難度之分嗎','攀岩的規則是什麼','攀岩的規則有哪些','奧運的攀岩規則','上攀有什麼要注意的？','上攀有哪些要小心的？','怎麼知道我是哪個等級','要怎麼知道自己的等級']
    testLoki(inputLIST, ['rules'])
    print("")

    # gym_time
    print("[TEST] gym_time")
    inputLIST = ['多早開','幾點開','啥時開門','幾時營業','幾時開門','幾時關門','幾點營業','幾點開門','幾點關？','平常幾點開','什麼時候開門','今天有開嗎？','營業時間是？','今天有營業嗎？','營業時間是幾點？','營業時間幾點到幾點？']
    testLoki(inputLIST, ['gym_time'])
    print("")

    # chat
    print("[TEST] chat")
    inputLIST = ['你愛攀岩麻','你會攀岩嗎','我喜歡抱石','抱石好玩嗎','我不喜歡上攀','攀岩好無聊！','你喜歡攀岩嗎？']
    testLoki(inputLIST, ['chat'])
    print("")

    # equipment_list
    print("[TEST] equipment_list")
    inputLIST = ['抱石要帶什麼','抱石要穿什麼','攀岩要帶什麼','攀岩要穿什麼','要買哪些裝備','抱石要準備什麼','攀岩要準備什麼','哪些裝備一定要買','抱石需要哪些裝備','攀岩需要哪些裝備','上攀要準備多少裝備','抱石要先買哪些裝備','抱石需要買哪些裝備','攀岩要先買哪些裝備','攀岩要準備多少裝備','攀岩需要買哪些裝備','抱石有服裝上的規定嗎','攀岩有服裝上的規定嗎','抱石需要先買好哪些裝備','攀岩需要先買好哪些裝備','抱石有什麼是要先買好的？','攀岩有什麼是要先買好的？','攀岩鞋子要買多大？','抱石要穿長褲還短褲？','攀岩要穿長褲還短褲？']
    testLoki(inputLIST, ['equipment_list'])
    print("")

    # equipment_yesNo
    print("[TEST] equipment_yesNo")
    inputLIST = ['要帶岩粉嗎','岩粉必須買嗎','必須買岩粉嗎','有dress code嗎？','可以不買裝備嗎','可以穿運動鞋嗎','岩粉有需要買嗎','抱石要買鞋子嗎','攀岩要買鞋子嗎','衣著有限制嗎？','去岩館要帶岩粉嗎','安全吊帶租得到嘛','安全吊帶買得到嘛','岩鞋岩館租得到嗎','岩館可以買鞋子嗎','岩館買得到鞋子嗎','抱石租得到鞋子嗎','攀岩租得到鞋子嗎','有規定要穿什麼嗎','穿短袖可以抱石嗎','穿短袖可以攀岩嗎','岩鞋在岩館買得到嗎','抱石可以穿短袖嗎？','抱石需要穿運動褲嗎','攀岩可以穿短袖嗎？','攀岩需要穿運動褲嗎','新手有需要買裝備嗎','穿短袖可以去攀岩嗎','可以穿牛仔褲抱石嗎？','可以穿牛仔褲攀岩嗎？','抱石一定要穿運動服嗎','攀岩一定要穿運動服嗎','上攀裝備會不會很難買？','攀岩裝備會不會很難買？','可以穿一般運動鞋去抱石嗎','可以穿一般運動鞋去攀岩嗎']
    testLoki(inputLIST, ['equipment_yesNo'])
    print("")

    # gym_distance
    print("[TEST] gym_distance")
    inputLIST = ['哪裡可以上攀','哪裡可以攀岩','哪裡有速度攀','有哪些岩館呢','附近有岩館嗎','上攀可以去哪裡','想攀岩可以去哪','我附近有岩館嗎','攀岩可以去哪裡','有推薦的岩館麻','哪間岩館離我最近','想抱石可以去哪裡','我附近有什麼岩館','要抱石可以去哪裡','想攀先鋒攀可以去哪','比較近的岩館有哪些','推薦一些距離近的岩館','推薦哪些距離近的岩館','推薦幾間距離近的岩館','離我最近的岩館是哪間','離我最近的岩館有哪些','離我媽最近的岩館有哪些','離我家最近的岩館是哪間','離我近的岩館有比較推薦的嗎']
    testLoki(inputLIST, ['gym_distance'])
    print("")

    # gym_yesNo
    print("[TEST] gym_yesNo")
    inputLIST = ['原岩倒了嗎','Dapro在台中嗎','東部有岩館嗎','苗栗有岩館嗎','苗栗能攀岩嗎','紅石假日有開嗎','紅石可以抱石嗎','苗栗可以上攀嗎','原岩假日有營業嗎','原岩新竹有分店嗎']
    testLoki(inputLIST, ['gym_yesNo'])
    print("")

    # rock
    print("[TEST] rock")
    inputLIST = ['jug長怎樣','pinch怎麼抓','岩點有哪些','jug有什麼特色','jug長什麼樣子','岩點有哪幾種','jug的特色是什麼','sloper可以怎麼爬','最不好抓的點是','最好爬的是哪種','爬jug要注意什麼','最好抓的是哪種點','最難抓的點是哪個','最不好抓的點是哪個']
    testLoki(inputLIST, ['rock'])
    print("")

    # gym_price
    print("[TEST] gym_price")
    inputLIST = ['Y17很貴嗎？','抱石會很貴嗎','攀岩會很貴嗎','紅石一次多少','紅石票價多少','去抱石一次多少','去攀岩一次多少','抱石一次多少錢','攀岩一次多少錢','去一次岩館多少錢','去攀一次岩多少錢','去攀岩一次多少錢','抱石通常要花多少','攀岩通常要花多少','紅石攀岩一次多少','double 8一個人多少錢','紅石攀岩一天多少錢','去double8攀岩一次多少','double 8攀岩一次多少錢']
    testLoki(inputLIST, ['gym_price'])
    print("")


if __name__ == "__main__":
    # 測試所有意圖
    testIntent()

    # 測試其它句子
    filterLIST = []
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    #resultDICT = execLoki("攀岩的規則是什麼？")
    #print(resultDICT)
    #resultDICT = execLoki("攀岩有規則嗎？")
    #print(resultDICT)
    #resultDICT = execLoki("台南哪裡有岩館？")
    #print(resultDICT)
    #resultDICT = execLoki("中部上攀可以去哪")
    #print(resultDICT)
    resultDICT = execLoki(["中部上攀可以去哪裡"])
    print(resultDICT)
    resultDICT = execLoki(["去double 8攀岩一次多少錢"])
    print(resultDICT)    
    resultDICT = execLoki(["double 8攀岩一次多少錢"])
    print(resultDICT)    
    resultDICT = execLoki(["double 8假日幾點開"])
    print(resultDICT)
    resultDICT = execLoki(["平日double 8營業時間是"])
    print(resultDICT)
    resultDICT = execLoki(["double 8假日幾點關門"])
    print(resultDICT)