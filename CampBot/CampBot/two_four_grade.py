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
import time
try:
    from intentTWOFOUR import Loki_fei4uuong4you1hwei4
    from intentTWOFOUR import Loki_gwo4ye4
    from intentTWOFOUR import Loki_hang2qyan2
    from intentTWOFOUR import Loki_ke4cheng2
    from intentTWOFOUR import Loki_shi2jyan1
    from intentTWOFOUR import Loki_ying2dwei4lei4xying2
    from intentTWOFOUR import Loki_bao3xyan3
    from intentTWOFOUR import Loki_fei4uuong4twei4fei4
    from intentTWOFOUR import Loki_di4dyan3
    from intentTWOFOUR import Loki_fen1zu3
    from intentTWOFOUR import Loki_an1quuan2cwo4shi1
    from intentTWOFOUR import Loki_hwen4lying2
    from intentTWOFOUR import Loki_te4shu1xuu1qyou2
    from intentTWOFOUR import Loki_ying2dwei4shou1hwo4
    from intentTWOFOUR import Loki_gweng4can1
    from intentTWOFOUR import Loki_hwo2dweng4ji4lu4
    from intentTWOFOUR import Loki_bao4mying2
    from intentTWOFOUR import Loki_ying2dwei4nei4rweng2
    from intentTWOFOUR import Loki_fei4uuong4xi4jye2
    from intentTWOFOUR import Loki_pyin3zhi2
    from intentTWOFOUR import Loki_age  
except:
    from .intent import Loki_fei4uuong4you1hwei4
    from .intent import Loki_gwo4ye4
    from .intent import Loki_hang2qyan2
    from .intent import Loki_ke4cheng2
    from .intent import Loki_shi2jyan1
    from .intent import Loki_ying2dwei4lei4xying2
    from .intent import Loki_bao3xyan3
    from .intent import Loki_fei4uuong4twei4fei4
    from .intent import Loki_di4dyan3
    from .intent import Loki_fen1zu3
    from .intent import Loki_an1quuan2cwo4shi1
    from .intent import Loki_hwen4lying2
    from .intent import Loki_te4shu1xuu1qyou2
    from .intent import Loki_ying2dwei4shou1hwo4
    from .intent import Loki_gweng4can1
    from .intent import Loki_hwo2dweng4ji4lu4
    from .intent import Loki_bao4mying2
    from .intent import Loki_zheng3jyou4wan2juu4dao3
    from .intent import Loki_tan4swo3sheng1tai4dao3
    from .intent import Loki_fei4uuong4xi4jye2
    from .intent import Loki_pyin3zhi2


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
try:
    accountInfo = json.load(open(os.path.join(os.path.dirname(__file__), "account.info"), encoding="utf-8"))
    USERNAME = accountInfo["username"]
    LOKI_KEY = accountInfo["loki_key_twofour"]
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
            lokiResultDICT = {}
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # fei4uuong4you1hwei4
                if lokiRst.getIntent(index, resultIndex) == "fei4uuong4you1hwei4":
                    lokiResultDICT = Loki_fei4uuong4you1hwei4.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # gwo4ye4
                if lokiRst.getIntent(index, resultIndex) == "gwo4ye4":
                    lokiResultDICT = Loki_gwo4ye4.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # hang2qyan2
                if lokiRst.getIntent(index, resultIndex) == "hang2qyan2":
                    lokiResultDICT = Loki_hang2qyan2.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # ke4cheng2
                if lokiRst.getIntent(index, resultIndex) == "ke4cheng2":
                    lokiResultDICT = Loki_ke4cheng2.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # shi2jyan1
                if lokiRst.getIntent(index, resultIndex) == "shi2jyan1":
                    lokiResultDICT = Loki_shi2jyan1.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # ying2dwei4lei4xying2
                if lokiRst.getIntent(index, resultIndex) == "ying2dwei4lei4xying2":
                    lokiResultDICT = Loki_ying2dwei4lei4xying2.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # bao3xyan3
                if lokiRst.getIntent(index, resultIndex) == "bao3xyan3":
                    lokiResultDICT = Loki_bao3xyan3.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # fei4uuong4twei4fei4
                if lokiRst.getIntent(index, resultIndex) == "fei4uuong4twei4fei4":
                    lokiResultDICT = Loki_fei4uuong4twei4fei4.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # di4dyan3
                if lokiRst.getIntent(index, resultIndex) == "di4dyan3":
                    lokiResultDICT = Loki_di4dyan3.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # fen1zu3
                if lokiRst.getIntent(index, resultIndex) == "fen1zu3":
                    lokiResultDICT = Loki_fen1zu3.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # an1quuan2cwo4shi1
                if lokiRst.getIntent(index, resultIndex) == "an1quuan2cwo4shi1":
                    lokiResultDICT = Loki_an1quuan2cwo4shi1.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # hwen4lying2
                if lokiRst.getIntent(index, resultIndex) == "hwen4lying2":
                    lokiResultDICT = Loki_hwen4lying2.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # te4shu1xuu1qyou2
                if lokiRst.getIntent(index, resultIndex) == "te4shu1xuu1qyou2":
                    lokiResultDICT = Loki_te4shu1xuu1qyou2.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # ying2dwei4shou1hwo4
                if lokiRst.getIntent(index, resultIndex) == "ying2dwei4shou1hwo4":
                    lokiResultDICT = Loki_ying2dwei4shou1hwo4.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # gweng4can1
                if lokiRst.getIntent(index, resultIndex) == "gweng4can1":
                    lokiResultDICT = Loki_gweng4can1.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # hwo2dweng4ji4lu4
                if lokiRst.getIntent(index, resultIndex) == "hwo2dweng4ji4lu4":
                    lokiResultDICT = Loki_hwo2dweng4ji4lu4.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # bao4mying2
                if lokiRst.getIntent(index, resultIndex) == "bao4mying2":
                    lokiResultDICT = Loki_bao4mying2.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # fei4uuong4xi4jye2
                if lokiRst.getIntent(index, resultIndex) == "fei4uuong4xi4jye2":
                    lokiResultDICT = Loki_fei4uuong4xi4jye2.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                # pyin3zhi2
                if lokiRst.getIntent(index, resultIndex) == "pyin3zhi2":
                    lokiResultDICT = Loki_pyin3zhi2.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)
                    
                # age
                if lokiRst.getIntent(index, resultIndex) == "age":
                    lokiResultDICT = Loki_age.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)
                
                # ying2dwei4nei4rweng2
                if lokiRst.getIntent(index, resultIndex) == "ying2dwei4nei4rweng2":
                    lokiResultDICT = Loki_ying2dwei4nei4rweng2.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), lokiResultDICT, refDICT)

                


            # save lokiResultDICT to resultDICT
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
    for i in range(0, len(inputLIST)):
        print(inputLIST[i])
        resultDICT = runLoki(['{}'.format(inputLIST[i])])
        print(resultDICT["response"])
        
    
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)
        

    if "msg" in resultDICT:
        print(resultDICT["msg"])

def testIntent():
    # an1quuan2cwo4shi1
    print("[TEST] an1quuan2cwo4shi1")
    inputLIST = ['不適','不舒服','會受傷','有危險','發生危險','碰上危險','確保安全','受傷怎麼辦','會不會受傷','有安全措施','有防護措施','身體有狀況','如何處理受傷','出現危險的情況','受傷了該怎麼辦','有什麼安全措施','有安全保護措施','有沒有安全措施','有相關的安全措施','在你們那受傷怎麼辦']
    testLoki(inputLIST, ['an1quuan2cwo4shi1'])
    print("")
    time.sleep(60)

    # bao4mying2
    print("[TEST] bao4mying2")
    inputLIST = ['如何報名','想要參加','想要報名','詢問報名','去哪裡報名','幫小孩報名','想報名參加','有興趣參加','要怎麼報名','如何報名參加','如何進行報名','想讓小孩參加','報名方式是什麼','希望給小孩報名','給我家小孩報名','幫我姊姊的姐姐報名','幫我姐姐的小孩報名','幫我小孩的姐姐報名','幫我小孩的小孩報名']
    testLoki(inputLIST, ['bao4mying2'])
    print("")
    time.sleep(60)

    # fei4uuong4twei4fei4
    print("[TEST] fei4uuong4twei4fei4")
    inputLIST = ['退費','辦退費','可以退費','想要退費','申請退費','辦理退費','是全額退費','比例怎麼算','可不可以退費','退費怎麼辦理','退費比例政策','退費比例規定','是否可以退費？','比例該怎麼算？','退款比例的原則','退費比例怎麼算','退費比例的標準','退費要如何進行','退費要怎麼辦理','怎樣計算退費比例？','比例要如何計算呢？','退費的比例該如何計算？','比例的計算方式是什麼呢？']
    testLoki(inputLIST, ['fei4uuong4twei4fei4'])
    print("")
    time.sleep(60)

    # fei4uuong4xi4jye2
    print("[TEST] fei4uuong4xi4jye2")
    inputLIST = ['多貴','多少錢','費用為何?','費用是多少','費用要多少','價格是多少錢?','費用需要多少錢?','費用有包含教材嗎','會不會有額外的費用','是否會有其他的花費？','教材有包含在費用裡嗎？','是否會產生額外的費用？','費用裡有沒有包含教材？','教材是否已納入費用之中？','費用是否已經包括了教材？','教材是否已經被納入費用了？','會不會有額外需支付的費用？','是否會有額外的金額需要支付？','教材是不是已經包含在費用中了？']
    testLoki(inputLIST, ['fei4uuong4xi4jye2'])
    print("")
    time.sleep(60)

    # fei4uuong4you1hwei4
    print("[TEST] fei4uuong4you1hwei4")
    inputLIST = ['有優待','有優惠','可以打折','團報優惠','提供優惠','有折扣嗎','給個優惠','可否打個折','團報有優惠','有什麼優惠','有優惠方案','有打折優惠','有沒有優惠','有沒有打折','給一點折扣','團報優惠是什麼','團報會比較便宜','團報有比較便宜','提供任何折扣方案','有提供折扣或優惠','有優惠方案可供選擇']
    testLoki(inputLIST, ['fei4uuong4you1hwei4'])
    print("")
    time.sleep(60)

    # hang2qyan2
    print("[TEST] hang2qyan2")
    inputLIST = ['進入親師群','被加入親師群','有營隊行前通知','提供營隊行前通知','被邀請加入親師群','何時會被納入親師群','告知營隊行前的通知','提供營隊行前的通知','營隊行前任務是什麼','有沒有營隊行前的通知','營隊行前的工作有哪些','營隊行前需要做什麼準備','營隊開始前需要準備什麼','進入營隊前要做哪些準備','進入營隊前須要準備什麼','營隊行前需做哪些準備工作','營隊行前要完成的任務有哪些','參加營隊前應該做哪些準備事項','營隊行前應該要做什麼準備工作','營隊行前須要完成的事情是什麼','進營隊之前應該先作哪些準備的安排']
    testLoki(inputLIST, ['hang2qyan2'])
    print("")
    time.sleep(60)

    # hwen4lying2
    print("[TEST] hwen4lying2")
    inputLIST = ['是同年','同年齡？','是相同年紀','分組都是混齡','包含不同年齡層','以不同年齡混合分組','年紀小會不會跟不上','同組的孩子是否都是同年齡','同組的小孩都會是同年紀嗎','年紀小的孩子會不會玩不起來?','年紀比較大的孩子會不會無聊?','年齡較大的孩子是否會感到無聊','較大年紀的孩子是否會感到無聊','年紀小的小孩能不能融入這個活動','年紀比較大的孩子會不會覺得無聊','年紀比較大的小孩可能會感到無趣','年紀比較大的小孩會不會感到無聊','年紀小的孩子是否能跟得上活動的節奏','在分組時不同年齡的人是不是都混合在一起']
    testLoki(inputLIST, ['hwen4lying2'])
    print("")
    time.sleep(60)

    # hwo2dweng4ji4lu4
    print("[TEST] hwo2dweng4ji4lu4")
    inputLIST = ['有照片','有沒有照片','有活動照片','想看活動相片','更新活動照片','看到活動照片','找到活動的相片','提供活動的相片','會不會幫忙拍照','會幫小朋友拍照','照片要去哪裡看','看我女兒的照片','看我小孩的照片','了解孩子參與狀況','得知孩子參與狀況','有沒有活動的照片','有活動拍攝的圖片','更新每天的活動照片','活動的相片要怎麼看','有沒有活動所拍攝的相片','想要看活動照片要去哪裡找']
    testLoki(inputLIST, ['hwo2dweng4ji4lu4'])
    print("")
    time.sleep(60)

    # ke4cheng2
    print("[TEST] ke4cheng2")
    inputLIST = ['有教材','有戶外活動','有沒有教材','了解營隊課表','安排戶外活動','知道營隊課表','什麼是同樂會?','同樂會在幹嘛?','有哪些戶外活動','空課指的是什麼','同樂會在做什麼?','要參加同樂會嗎?','安排一些戶外活動','詢問關於營隊課表','午休的時候會做什麼','知道營隊的課程內容','中午休息時間會做什麼','午休時會做哪些事情呢','午休時間通常會做什麼','中午休息時通常會做什麼','中午休息時都會做什麼事','午休的時候會做什麼事情','中午休息時間會進行哪些活動','中午休息時間都會做什麼事情','詢問有關營隊的課程時間和安排']
    testLoki(inputLIST, ['ke4cheng2'])
    print("")
    time.sleep(60)

    # pyin3zhi2
    print("[TEST] pyin3zhi2")
    inputLIST = ['是小班制','班級人數','什麼是玩伴','帶幾個小孩','玩伴是什麼','師生比是多少','控制教學品質','玩伴在做什麼','確保教師素質','管理教學品質','維護教學品質','如何把關教學品質','如何確保教學品質','師生比例是多少？','確保營隊師資品質','老師和學生的比例','師生之間的比例是多少']
    testLoki(inputLIST, ['pyin3zhi2'])
    print("")
    time.sleep(60)

    # shi2jyan1
    print("[TEST] shi2jyan1")
    inputLIST = ['結束','開始','幾點結束','幾點開始','接送時間','帶小孩回家','帶小孩過去','幾點開始接','送小孩過去','什麼時候回家','什麼時候開始','把小孩送過去','甚麼時候結束','幾點可以接小孩','接送時間是幾點','甚麼時候會結束','結束時間是幾點','結束需要到幾點','可以在哪個時段接','可以在幾點之後接','可以接小孩的時間','幾點要送小孩過去','什麼時候可以接小孩','什麼時候送小孩過去','什麼時間可以接小孩','把小孩送過去的時間','營隊期間的接送時間','什麼時候可以去接小孩','活動時間是幾點到幾點','需要在幾點被送到那裡','開始與結束時間是幾點到幾點','活動進行的時段是從幾點到幾點']
    testLoki(inputLIST, ['shi2jyan1'])
    print("")
    time.sleep(60)

    # ying2dwei4lei4xying2
    print("[TEST] ying2dwei4lei4xying2")
    inputLIST = ['推薦營隊','參加什麼營','想了解營隊','有什麼不同','有什麼差別?','參加哪個營隊','有適合的營隊','營隊是在幹嘛','適合什麼營隊','推薦適合的營隊','有哪些營隊適合','主要的活動內容是','可以學才藝的營隊','報名參加哪個營隊','有什麼營隊可參加','有什麼適合的營隊','有哪些營隊能夠報名','針對2年級是在做什麼?','有哪幾個營隊可以參加','有多少種營隊可以選擇','可以參加的營隊有哪些？','有哪些營隊是可以報名的','兩個營隊各自的特色是什麼?','兩個營隊可以都解釋給我聽嗎?']
    testLoki(inputLIST, ['ying2dwei4lei4xying2'])
    print("")
    time.sleep(60)

    # gweng4can1
    print("[TEST] gweng4can1")
    inputLIST = ['會餓','吃不飽','帶零食','有點心','肚子餓','訂午餐','供應午餐','提供午餐','自備午餐','午餐吃什麼','帶零食進去','早餐怎麼辦','會餓怎麼辦','有沒有點心','中午會吃什麼','把零食帶進去','自行攜帶午餐','早餐是自己解決','早餐是自行解決','有沒有點心吃？']
    testLoki(inputLIST, ['gweng4can1'])
    print("")
    time.sleep(60)

    # tan4swo3sheng1tai4dao3
    print("[TEST] tan4swo3sheng1tai4dao3")
    inputLIST = ['探索生態島在幹嘛','探索生態島的細節','探索生態島在做什麼','探索生態島的詳細內容','有探索生態島的課表嗎','探索生態島是在做什麼的','探索生態島的特色是什麼','探索生態島都在戶外活動嗎']
    testLoki(inputLIST, ['tan4swo3sheng1tai4dao3'])
    print("")
    time.sleep(60)

    # di4dyan3
    print("[TEST] di4dyan3")
    inputLIST = ['會在哪裡','知道地點','確定地點','辦在哪裡','只有在台北','地點在哪裡','地點在哪邊','地點位於哪裡','得知具體位置','會在哪裡舉行','知道確切位置','取得地點的資訊','地點在哪個位置','會在台北的哪裡','得知地點的具體情況','地點的具體位置是哪裡']
    testLoki(inputLIST, ['di4dyan3'])
    print("")
    time.sleep(60)

    # age
    print("[TEST] age")
    inputLIST = ['2','8歲','國一','小二','二年級','初中二年級']
    testLoki(inputLIST, ['age'])
    print("")
    time.sleep(60)

    # bao3xyan3
    print("[TEST] bao3xyan3")
    inputLIST = ['有保險','保什麼險','包含保險','投什麼險','投保保險','提供保險','負責保險','購買保險','投什麼保險','有沒有投保險','投保了什麼保險','需要自己保保險','在保險方面做了哪些準備','在保險方面有怎樣的安排']
    testLoki(inputLIST, ['bao3xyan3'])
    print("")
    time.sleep(60)

    # ying2dwei4shou1hwo4
    print("[TEST] ying2dwei4shou1hwo4")
    inputLIST = ['有收穫','學到什麼','得到什麼','有什麼收穫','有沒有收穫','獲得的東西','能學到什麼','培養什麼實力','學到哪些東西','獲得什麼經驗','獲得哪些收穫','累積什麼經驗','獲得怎樣的知識','能夠學到些什麼','能獲得哪些知識']
    testLoki(inputLIST, ['ying2dwei4shou1hwo4'])
    print("")
    time.sleep(60)

    # fen1zu3
    print("[TEST] fen1zu3")
    inputLIST = ['分在一組','劃分小組','安排分組','怎麼分組','進行分組','分在不同組','是老師分組','老師會分組','與好友同組','誰會負責分組','跟朋友同一組','老師要進行分組','分組方法是怎樣的','分組的方式是什麼','由老師來進行分組']
    testLoki(inputLIST, ['fen1zu3'])
    print("")
    time.sleep(60)

    # gwo4ye4
    print("[TEST] gwo4ye4")
    inputLIST = ['會過夜','晚上會住哪裡','有過夜的安排','有過夜的營隊','有安排過夜的營隊','過夜的營隊有哪些','有提供過夜活動的營隊','參加哪些提供過夜的營隊','所有的營隊都會在夜晚過夜','有哪些提供過夜住宿的營隊','有哪些營隊可以讓孩子過夜']
    testLoki(inputLIST, ['gwo4ye4'])
    print("")
    time.sleep(60)

    # te4shu1xuu1qyou2
    print("[TEST] te4shu1xuu1qyou2")
    inputLIST = ['吃素','吃藥','不能吃','有急事','有其他問題','有急事找誰','有特殊需求','有臨時狀況','臨時有事情','有額外的問題','暫時有緊急事項','有其他問題怎麼辦','突發情況需要找誰','臨時有狀況要找誰']
    testLoki(inputLIST, ['te4shu1xuu1qyou2'])
    print("")
    time.sleep(60)


if __name__ == "__main__":
   

    inputLIST = ["有適合的營隊嗎?"]
    
    resultDICT = runLoki(inputLIST)
    print(resultDICT)
    
    # 測試所有意圖
    
    #testIntent()      
    
    '''



    # 測試其它句子
    filterLIST = []
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    inputSTR = ["我要吃炸雞"]
    resultDICT = runLoki(inputSTR)
    print(resultDICT["response"][0])    
    # 設定參考資料
    refDICT = {
        #"key": []
    }
<<<<<<< .merge_file_Rd79Cg
    #resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST=filterLIST, refDICT=refDICT)                      # output => {"key": ["今天天氣"]}
    #resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST=filterLIST, splitLIST=splitLIST, refDICT=refDICT) # output => {"key": ["今天天氣", "後天氣象"]}
    #resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"], filterLIST=filterLIST, refDICT=refDICT)                # output => {"key": ["今天天氣", "後天氣象"]}    #resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"], filterLIST=filterLIST, refDICT=refDICT)                # output => {"key": ["今天天氣", "後天氣象"]}
=======
    resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST=filterLIST, refDICT=refDICT)                      # output => {"key": ["今天天氣"]}
    resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST=filterLIST, splitLIST=splitLIST, refDICT=refDICT) # output => {"key": ["今天天氣", "後天氣象"]}
    resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"], filterLIST=filterLIST, refDICT=refDICT)                # output => {"key": ["今天天氣", "後天氣象"]}
    
    
    '''
