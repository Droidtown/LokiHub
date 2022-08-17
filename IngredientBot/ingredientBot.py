#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#哈囉

from requests import post
from requests import codes
import math
import re
try:
    from intent import Loki_CheckInSeason
    from intent import Loki_taboo
    from intent import Loki_reject
    from intent import Loki_selection
    from intent import Loki_price
    from intent import Loki_recipe
    from intent import Loki_InSeason
    from intent import Loki_capability
    from intent import Loki_all_ingre
    from intent import Loki_accept
except:
    from .intent import Loki_CheckInSeason
    from .intent import Loki_taboo
    from .intent import Loki_reject
    from .intent import Loki_selection
    from .intent import Loki_price
    from .intent import Loki_recipe
    from .intent import Loki_InSeason
    from .intent import Loki_capability
    from .intent import Loki_all_ingre
    from .intent import Loki_accept

import json

accountDICT = json.load(open("account.info", encoding="utf-8"))
LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = accountDICT["username"]
LOKI_KEY = accountDICT["apikey_ing"]
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
       #"key": []
    }
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # CheckInSeason
                if lokiRst.getIntent(index, resultIndex) == "CheckInSeason":
                    resultDICT = Loki_CheckInSeason.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # taboo
                if lokiRst.getIntent(index, resultIndex) == "taboo":
                    resultDICT = Loki_taboo.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # reject
                if lokiRst.getIntent(index, resultIndex) == "reject":
                    resultDICT = Loki_reject.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # selection
                if lokiRst.getIntent(index, resultIndex) == "selection":
                    resultDICT = Loki_selection.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # price
                if lokiRst.getIntent(index, resultIndex) == "price":
                    resultDICT = Loki_price.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # recipe
                if lokiRst.getIntent(index, resultIndex) == "recipe":
                    resultDICT = Loki_recipe.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # InSeason
                if lokiRst.getIntent(index, resultIndex) == "InSeason":
                    resultDICT = Loki_InSeason.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # capability
                if lokiRst.getIntent(index, resultIndex) == "capability":
                    resultDICT = Loki_capability.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # all_ingre
                if lokiRst.getIntent(index, resultIndex) == "all_ingre":
                    resultDICT = Loki_all_ingre.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), 
            resultDICT)

                # accept
                if lokiRst.getIntent(index, resultIndex) == "accept":
                    resultDICT = Loki_accept.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

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
                resultDICT[k].extend(lokiResultDICT[k])

    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

    if "msg" in resultDICT:
        print(resultDICT["msg"])

def testIntent():
    # CheckInSeason
    print("[TEST] CheckInSeason")
    inputLIST = ['烏魚子是當季食材嗎','烏魚子是不是當季食材？']
    testLoki(inputLIST, ['CheckInSeason'])
    print("")

    # taboo
    print("[TEST] taboo")
    inputLIST = ['杏仁 禁忌','杏仁跟什麼相剋','杏仁可以跟什麼一起吃','杏仁的食用禁忌有哪些','杏仁與什麼食物相剋？','杏仁跟什麼不能一起吃','和杏仁相剋的食物有哪些','杏仁不可以跟什麼一起吃','螃蟹跟柿子可以一起吃嗎']
    testLoki(inputLIST, ['taboo'])
    print("")

    # reject
    print("[TEST] reject")
    inputLIST = ['還有嗎？','有沒有別的','還推薦什麼','還有什麼？','再來點別的？','我不喜歡芭樂','我不想吃芭樂','可以說點別的嗎？','不要讓我看到芭樂！']
    testLoki(inputLIST, ['reject'])
    print("")

    # selection
    print("[TEST] selection")
    inputLIST = ['怎麼挑山藥？','茄子挑選方法','青椒怎麼看？','肉類如何挑選？','要怎麼選芭樂？','新鮮肉品怎麼挑？','買茄子如何挑選？','如何挑選新鮮肉品？','山藥如何挑選才好吃？','什麼樣的芭樂比較好吃？','火龍果表皮有皺褶正常嗎？','如何區分新鮮與不新鮮的魚?','馬鈴薯是軟的好還是硬的好？','馬鈴薯軟一點好還是硬一點好？']
    testLoki(inputLIST, ['selection'])
    print("")

    # price
    print("[TEST] price")
    inputLIST = ['一盒蛋多少','皮蛋多少錢','蘋果怎麼賣','一塊肉怎麼賣','一條魚多少錢','我要買一盒皮蛋','瘦肉一斤多少錢','現在一盒皮蛋要多少錢','請告訴我一盒蛋多少錢','我想買一盒蛋需要帶多少錢','現在一條白鯧的價格是多少']
    testLoki(inputLIST, ['price'])
    print("")

    # recipe
    print("[TEST] recipe")
    inputLIST = ['芭樂 料理','芭樂要怎麼弄','芭樂該怎麼弄','蘋果相關的料理','烏魚子可以怎麼做','皮蛋可以用烤的嗎','芭樂可以做成什麼','芭樂可以做成什麼料理','請問烏魚子該怎麼料理','我想知道蘋果相關的料理','我想知道蘋果能做什麼料理']
    testLoki(inputLIST, ['recipe'])
    print("")

    # InSeason
    print("[TEST] InSeason")
    inputLIST = ['現在有什麼','現在有甚麼海鮮','現在的當季水果','皮蛋是當季的嗎','目前盛產甚麼水果','現在有什麼水果好吃','現在有什麼當季食材','現在有甚麼水果好吃','現在當季水果有哪些','現在當季食材有哪些','現在該吃哪些水果？','現在當季的水果是什麼','現在當季的蔬菜有哪些','現在有甚麼當季水果好吃','現在有甚麼好吃的當季水果']
    testLoki(inputLIST, ['InSeason'])
    print("")


if __name__ == "__main__":
    # 測試所有意圖
    testIntent()

    # 測試其它句子
    filterLIST = []
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST)            # output => ["今天天氣"]
    resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST, splitLIST) # output => ["今天天氣", "後天氣象"]
    resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"], filterLIST)      # output => ["今天天氣", "後天氣象"]