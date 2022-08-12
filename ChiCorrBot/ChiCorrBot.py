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
try:
    from intent import Loki_syntax
    from intent import Loki_semantics
    from intent import Loki_vocabulary
except:
    from .intent import Loki_syntax
    from .intent import Loki_semantics
    from .intent import Loki_vocabulary


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"

with open('./Loki_account.info', 'r', encoding='utf-8') as f:
    LokiAccount = json.loads(f.read())
USERNAME = LokiAccount['username']
LOKI_KEY = LokiAccount['Loki_key']

# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []
INPUT_LIMIT = 20

explanationDICT = {'prg':'這種情況下，你想描述的是正在進行的事件，所以需要在動詞前加「在」。',
                   'loc':'「在」後面加地點，再加動作，例如在家吃飯、在學校讀書。',
                   'hai':'「還」的用法可分為三種，還+動詞、還有+名詞、還是=或者，例如還在睡、還有學生、學生還是老師。',
                   'cleft':'這是一種強調的用法，句型為「是...的」。',
                   'huai':'「壞」是很強烈的負面評價，如果是描述不好的狀況，則使用「很差」、「很糟」等詞即可。',
                   'yingxiang':'「影響」可當作動詞或名詞使用，當動詞時，例如影響我們的生活；當名詞時，要加上介詞「對」，例如對我們生活的影響',
                   'duo':'當「多」放在(分類詞+)名詞前時，應該用「很多」。',
                   'sent1':'當兩人在來往時，需加上「在一起」這個詞，語意比較完整；「性格」通常描述較長久的特質，如果是說短期的狀態，不應該使用。'

                   }


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
                # syntax
                if lokiRst.getIntent(index, resultIndex) == "syntax":
                    resultDICT = Loki_syntax.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # semantics
                if lokiRst.getIntent(index, resultIndex) == "semantics":
                    resultDICT = Loki_semantics.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # vocabulary
                if lokiRst.getIntent(index, resultIndex) == "vocabulary":
                    resultDICT = Loki_vocabulary.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

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
    # syntax
    print("[TEST] syntax")
    inputLIST = ['根據她說','旅遊在台灣','夏天我爸爸說','他們都從不同意','學生不能來校內','我們的偶遇以前','沒是那麼對抗性','我只會聊天我的最愛','新冠肺炎給經濟影響','重要的日用品還不買','新冠肺炎很高的傳染性','我可以解釋我生活的影響','新館肺炎的防疫不太成功的','我跟我的朋友不可以聊天這本書','他們的名字不常常利用太特別的字','我們下個星期再會談論這部電視劇','我想通過寫信坦誠地跟你們聊了聊','每夏天他讓了我妹妹和我寫書報告','還許多人無視政府的新冠肺炎的規則','我生活被這個情況受到非常不好的影響','新冠肺炎疫情對美國生活有不少了的影響','最近教育和工作的變化都就是額外的壓力','大家都希望會快點得到解決這個很嚴重的問題','這導致了諸如畢業舞會、高年級學生慶祝活動、實地考察旅行等活動什麼的被取消']
    testLoki(inputLIST, ['syntax'])
    print("")

    # semantics
    print("[TEST] semantics")
    inputLIST = ['我有多本書','我看的最近','我們都不喜歡個','有一個意思的結局','這本書叫我人高興','記得我的回憶很難的','我最喜歡一天中的時間','看起來這個男孩子深思','可能記得為什麼他們對眼','我不誠信讓你們丟了面子','我們形成越來越神的關係','我坦白了每個我說假的話','人們應該合作來更好的生活','大部美國的部分選了人隔離','我看一看父母跟一起聊天了','我聽音樂的時候聽說過一幅畫','春草跟我的時候她性格更輕鬆','馬上變成了美國人的生活、經濟、政治']
    testLoki(inputLIST, ['semantics'])
    print("")

    # vocabulary
    print("[TEST] vocabulary")
    inputLIST = ['春草的性格很強','當然不是成心的','她看得很一心一意','常常有很同的看法','我的生活不是很壞','開始自己賺和化錢','你的話讓我返老還童','我的家庭經驗了很多','一年級我沒有對面的課','他們怕給家人新冠肺炎','應為記得我很簡單的生活','防疫戰術的輕重也在增加','我們的生活和經濟都變化了','我兄弟姐妹給我很深的幸福','我對我的家庭生活感到尷尬','最小些的孩子有戴口罩問題','學生可以用網路參加學習的事情','大部分的美國學生的成績都變壞了','把美國人的生活都改變了的一乾二淨','從經濟和政治到人民的人精和人際關係','我會報告新館肺炎對這三個部分怎麼樣','我希望我們可以很快得把新冠肺炎拿走了','我希望春草將來不會依靠何水遠帶來快樂','新冠肺炎確實對每一個人有真不好的影響']
    testLoki(inputLIST, ['vocabulary'])
    print("")


if __name__ == "__main__":
    # 測試所有意圖
    #testIntent()

    testLIST = ['他有多顆糖','看起來那個小孩反思','觀光在美國','還許多學生無視學校的校園的規範','他會報告健康飲食對這三個部分怎麼樣','我的心情不是很壞']
    for text in testLIST:
        resDICT = runLoki([text])
        print() #區隔runLoki的結果與建議說明
        #print(resDICT)
        print(f"那你可以說：{resDICT['suggestion']}")
        print(f"錯誤說明：{explanationDICT[resDICT['error']]}")
        print()
        print()

    # # 測試其它句子
    # filterLIST = []
    # splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    # resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST)            # output => ["今天天氣"]
    # resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST, splitLIST) # output => ["今天天氣", "後天氣象"]
    # resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"], filterLIST)      # output => ["今天天氣", "後天氣象"]