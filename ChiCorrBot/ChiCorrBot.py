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
                   'sent1':'當兩人在來往時，需加上「在一起」這個詞，語意比較完整；「性格」通常描述較長久的特質，如果是說短期的狀態，不應該使用。',
                   'gexing':'個性+很堅強，例如她的個性很堅強。',
                   'faceToface':'要表達實體課程，可以說「面對面的課」。',
                   'contract':'怕+傳染給+人+疾病，例如怕傳染給朋友感冒。',
                   'sent2':'「學習」代表整件事情，不需要再加「的事情」。',
                   'same':'表示事物一樣時，可使用「相同」，反之，則為「不相同」。',
                   'content':'「聽說過」的訊息來源是未知的人，如果訊息來源是事物，則可使用「提到」。',
                   'det':'分類詞前要加上「這」、「那」、數量，例如「這個」、「那個」、「三個」、「五個」。',
                   'shen':'「神」不能放在名詞前，可以放在名詞後，例如這個人太神了。',
                   'sentiment':'當你要描述一個人的情緒時，可以直接使用名詞或代名詞，不需要加「人」。',
                   'change':'「change into sth.」為「變成某人(某物)」；「change sth.」為「改變某事」。',
                   'youMod':'「有」加上名詞可當作形容詞使用，例如有錢的、有精神的等等。',
                   'memory':'「回憶」為記得過往的事物，並帶有正面或負面的情緒；「記憶」則是單純記得過往的事物，不帶情緒。',
                   'better':'「更好的」不能當作動詞，如果是讓某事變得更好，可使用「改善」。',
                   'sent3':'「記得」為單純記憶存在腦中；「想起」為回想某事物。如果「看對眼」是「喜歡」的意思，是一種俚俗的用法，建議可使用「喜歡」。',
                   'part':'表示多數，可使用「大部分」；表示某區域的某部分，則直接使用「地方」。',
                   'lie':'「說謊」為動詞；「謊話」為名詞。',
                   'gen':'「跟」後需加人，例如跟爸媽、跟朋友等等。',
                   'recently':'動詞前可加「最近」來表示近期做的事情。',
                   'sent4':'缺少「的」。',
                   'never':'「從不」前面不需加「都」。',
                   'often':'「常常」的否定句為「不常」，沒有「不常常」的說法。',
                   'youYiSi':'「有意思」是一種覺得某事物有趣的說法。',
                   'time':'季節或是特定時間後加「的時候」，讓語意更加完整。',
                   'solution':'「得到解決」的「解決」為名詞，如果要描述特定問題，建議說法為「得到某某問題的解決方法」；如果把「解決」當成動詞使用，可以說成「解決某某問題」。',
                   'dao':'「到」+地點，例如到校、到家、到公司。',
                   'explanation':'「解釋」加上介詞「對」某人，例如解釋對我的影響；「說明」、「描述」等皆是相同用法。',
                   'result':'因為某個狀況或事件，而受到影響。',
                   'say':'「動詞+一+動詞」，例如聊一聊、說一說、看一看。',
                   'liao':'「聊」+話題或事物，例如聊衣服、聊鞋子；「聊天」可當作名詞或動詞，但後面不加話題或事物，例如我們一起聊天。',
                   'again':'「再」+動詞，表示該動作重複；「過」+動詞，表示該動作已發生。',
                   'before':'「在+動詞+以前」描述該動作前的狀況。',
                   'sent5':'「的」前不能加「了」。',
                   'sent6':'句型為「對+某人事物+帶來影響」，例如對生活帶來影響。',
                   'dou':'用法為「都+動詞」或「都是+名詞」，沒有「都就是」的說法。',
                   'sent7':'用法為「還+動詞+不到」，例如還買不到、還吃不到。',
                   'you':'「有」+形容詞＋名詞，例如有好吃的食物、有漂亮的風景。',
                   'rang':'「讓」+人，例如讓弟弟去公園玩。',
                   'etc':'表達「諸如此類」的說法有「等」、「之類的」，例如某某等活動、某某之類的活動。',
                   'because':'「因為」為說明某件事的原因；「應為」為應該是。',
                   'embarrassed':'形容家庭狀況不會使用「尷尬」這個詞，可改用「感到不好意思」。',
                   'sent8':'「拿走」+物，例如拿走蛋糕、拿走書；「新冠肺炎」是一種疾病問題，可使用「解決新冠肺炎的問題」來表達。',
                   'experience':'「經歷」為動詞，「經驗」為名詞。',
                   'zui':'「最」+形容詞＋的，例如最開心的、最可愛的。',
                   'word':'句子裡有錯字或詞彙錯誤。',
                   'need':'「不用」為不需要。',
                   'favorite':'「最喜歡的」+事物+是，例如最喜歡的書籍是、最喜歡的地方是。',

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

    #testLIST = ['他有多顆糖','看起來那個小孩反思','觀光在美國','還許多學生無視學校的校園的規範','他會報告健康飲食對這三個部分怎麼樣','我的心情不是很壞','我們怕給朋友新冠肺炎','少部分的臺灣人民的生活都變壞了']
    testLIST = ['馬上變成了台灣人的生活、經濟、政治']
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