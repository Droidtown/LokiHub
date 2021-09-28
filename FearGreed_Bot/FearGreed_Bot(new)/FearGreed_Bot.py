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

from requests import post
from requests import codes
import json
import math
try:
    from intent import Loki_Greed
    from intent import Loki_Fear
    from intent import Loki_ExtremeFear
    from intent import Loki_ExtremeGreed
    from intent import Loki_Neutral
except:
    from .intent import Loki_Greed
    from .intent import Loki_Fear
    from .intent import Loki_ExtremeFear
    from .intent import Loki_ExtremeGreed
    from .intent import Loki_Neutral


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
with open("account.info.json", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())
USERNAME = accountDICT["username"]
LOKI_KEY = accountDICT["lokikey"]
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
    resultDICT = {}
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # Greed
                if lokiRst.getIntent(index, resultIndex) == "Greed":
                    resultDICT = Loki_Greed.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # Fear
                if lokiRst.getIntent(index, resultIndex) == "Fear":
                    resultDICT = Loki_Fear.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # ExtremeFear
                if lokiRst.getIntent(index, resultIndex) == "ExtremeFear":
                    resultDICT = Loki_ExtremeFear.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # ExtremeGreed
                if lokiRst.getIntent(index, resultIndex) == "ExtremeGreed":
                    resultDICT = Loki_ExtremeGreed.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # Neutral
                if lokiRst.getIntent(index, resultIndex) == "Neutral":
                    resultDICT = Loki_Neutral.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)


if __name__ == "__main__":
    # Greed
    print("[TEST] Greed")
    inputLIST = ['K大於D','好兆頭','增 10.33%','多方優勢','尾盤翻紅','急拉尾盤','站上季線','增加 10.33%','月增 10.33%','尾盤拉上來','科技股回升','航運漲100點','請勿追漲停','較有利多方','量溫和放大','5日均線向上','站上5日均線','最後收漲21點','美股20日上漲','投信買超7.7億','拉回買就對了','指標還是多方','本波行情回升','航運昨天漲了5%','多空手腳都要快','攻上季線很有望','盤越久量能越強','科技股領軍回升','資金翻了好幾倍','這個盤後不錯吧','看好9月行情續漲','今天大盤小漲21點','今日大盤跳空開高','但是不要一次買滿','台股本波回升行情','台股本波行情回升','很多股票底部出現','所以今天順勢整理','昨天航運漲了100點','美聯儲提振了美元','航運昨天漲了100點','行情還會再往上走','讓我減少很多虧損','那現在還是多頭吧','難得站上五日線了','MACD變成紅柱體第1根','今天成功守住了16983','今天有向上攻的情形','今日大盤跳空開高後','台股在本波回升行情','慢慢佈倉買進成長股','投資人可以開始布局','昨天提醒同學勿追高','第四季就會有好獲利','總未平倉量為-19929口','該股目前已站上季線','這樣保持下去就對了','三百以下算是很便宜了','伴隨鋼鐵市況需求強勁','拼命買和賣賺價差而已','有拉回我還是會撿回來','激勵鋼鐵類股多數收漲','現在政策開始重新翻多','自營上週五就開始做多','這樣多頭格局會更確立','9月台股指數期貨漲1.3點','但今天就看得出支撐明顯','多頭的回升才算正式開始','大盤創這波低點以來新高','從底部反彈了800點的行情','有站穩頸線跟上升趨勢線','未來將持續朝向多頭前進','看了許多今天大漲的股票','讓他穩健慢慢往上走最棒','外資則是淨多單增加1082口','台股連續四個交易日反彈後','如果明天收盤再次順利守住','敦泰出貨動能可望更加強勁','等待月線及半年線拉平緩後','這頂多損失一點點報酬而已','今日早盤洗盤完有機會拉尾盤','基本上買超前幾名都是隔日沖','官股銀行也在上週五大力護盤','感謝官股銀行和自營商的護盤','所以是個股跌深深的反彈行情','相當於變成下一波反彈的醞釀','但至少成交量比昨日略增也收漲','只要目前的股價低於應有的價值','台積電則跳空上漲收復所有均線','推動毛利及獲利維持在高檔水準','隔日宣布聯準會縮減QE的可能較低','在持續多頭的情勢下都有機會解套','外資也有可能開始增加期貨的多單','絕對是布局做第二波反彈的機會點','籌碼少在中繼反彈行情中比較有機會','內資做多價差反而成為了支撐的交易量','市場對聯準會政策收緊的擔憂有所緩解','且在2022年出貨量能有機會開始明顯成長','可望在未來幾年內達到一定規模的市占率','因市場對聯準會政策收緊的擔憂有所緩解','帶領亞谷紫蝶反彈帶領歐美股市回穩向上','美聯儲將很快開始收緊貨幣政策的預期提振了美元','對美聯儲將很快開始收緊貨幣政策的預期提振了美元','突破下降趨勢線並重新站上月線及半年線後再次上攻','夜盤帥啦衝啦帶領亞谷紫蝶反彈帶領歐美股市回穩向上']
    testLoki(inputLIST, ['Greed'])
    print("")

    # Fear
    print("[TEST] Fear")
    inputLIST = ['難度大','低檔不買','小幅衰退','忍痛停損','連跌九天','難度不小','台股跌100點','空軍將出動','要再高很難','不然容易震盪','只會盤跌走勢','台股小掉100點','台股小跌100點','台股微掉100點','台股微跌100點','現在大盤走弱','進而拖累需求','外資賣超159.1億','今天台股跌100點','今天航運股轉弱','但可惜開高走低','個股隔日沖進駐','台積尾盤會殺尾','台股今天跌100點','台股超詭異虛漲','多空都要很小心','夜盤要崩了快跑','如果有賣壓出現','很難一次就突破','買賣量有所降低','風險控管要做好','今天台股小掉100點','今天台股小跌100點','今天台股微掉100點','今天台股微跌100點','今天尚未站穩月線','台股今天小掉100點','台股今天小跌100點','台股今天微掉100點','台股今天微跌100點','台股沒量硬拉雞盤','向上攻堅難度不小','地緣政治局勢緊張','坦白說也不會融斷','大盤逐漸逼近頸線','尚未扭轉長空格局','屆時會較偏空看待','未來仍將持續下跌','每天都像坐海盜船','短期還是很不穩定','負面因素並未消失','遇到下彎月線賣壓','長空中的反彈開始','下殺的最低點為16984','就是一個止跌訊號了','所有面板股都不要碰','收盤連月線都沒站上','這區間是密集套牢區','這是比較不好的地方','亞股表現幾乎都不理想','共同成為外資的提款機','剛復原的台股還會震盪','很明顯外資在玩隔日沖','投資朋友記得不要恐慌','持續向上攻堅難度不小','早盤容易開很高後倒貨','目前盤勢屬於短期震盪','看來台股壓力尚未解除','結果現在持續被嗄空中','中國經濟增長一直在放緩','今天開高走低收平盤附近','今日遭遇下彎的月線反壓','外資空單水位不續增的話','大盤受限於量價架構欠佳','近期都是量縮震幅也變小','這回台灣和南韓同病相憐','這次外資因為太看好中國','銅價已下跌百分之五以上','下禮拜一看來也是大風大浪','守不住將回測8/20低點16248.08','當外資期貨現貨同步的時候','遇壓下跌純屬正常賣壓宣洩','加權股價指數終場下跌1.91點','只有本週五收盤不再跌破16983','不管你購買哪一支股票被套牢','期貨選擇權是外資的避險工具','不是要跌超過20%以上才算空頭嗎','人們擔心最大消費國中國的需求','今日開高後技術性壓回收斂漲幅','只要融資餘額降幅大於大盤跌幅','因擔憂生物燃料行業的豆油需求','市場最甜美的階段往往就過去了','無量的上漲經不起一點點的跌勢','當沒人有買盤意願承接會怎樣？','目前正在除權息旺季，根本停券','短線技術面都告訴我會稍微震盪','只能不停地變賣有獲利的標記套現','美股從昨天開始就進入小幅的震盪','指數面臨月半年及下降趨勢的三種壓力','有多少人追高航運之後跌了40%忍痛停損','指數向上攻堅並站穩月線反壓區的難度不小','代表多數的短線客當沖客的買賣量一定有所降低','指數持續向上攻堅並站穩月線反壓區的難度不小','指數若要持續向上攻堅並站穩月線反壓區的難度不小']
    testLoki(inputLIST, ['Fear'])
    print("")

    # ExtremeFear
    print("[TEST] ExtremeFear")
    inputLIST = ['火葬場','元氣大傷','台股失守','台股急挫','台股暴跌','台股狂跌','台股重挫','歹戲拖棚','爛股一支','台股急挫5%','台股暴跌5%','台股狂掉5%','台股狂跌5%','台股重挫5%','台積電遭摜壓','台股失守月線','台股急挫100點','台股暴跌100點','台股狂掉100點','台股狂跌100點','台股重挫100點','美股全數走跌','這回元氣大傷','大盤急跌2000點','不怕屎就盡量融資','拖累美股全數走跌','過陣子離開股市好了','在大盤急跌2000點之後','台股急挫百點失守月線','大家不怕屎就盡量融資','早上根本就是歹戲拖棚','大豆期貨跌至七周半最低','玉米期貨觸及三周半最低','台股最後一盤急挫百點失守月線','他們最後會把股票賣倒台股崩盤為止','等於是在不知不覺中把自己推入中國的火葬場','芝加哥期貨交易所(CBOT)大豆期貨跌至七周半最低','芝加哥期貨交易所(CBOT)大豆期貨週五跌至七周半最低']
    testLoki(inputLIST, ['ExtremeFear'])
    print("")

    # ExtremeGreed
    print("[TEST] ExtremeGreed")
    inputLIST = ['大漲','一路發','基本面佳','高檔猛追','各位都大漲','這還有紙箱','台指狂拉200點','大盤漲那麼多','恭喜各位大漲','擠得沒地方躺','航運類股大漲','航運類股暴漲','航運類股狂拉','航運類股狂漲','公園裡人山人海','前三天暴漲700點','恭喜各位都大漲','成績相當不容易','這還有多的紙箱','今天大盤漲那麼多','我這還有多的紙箱','昨天航運類股大漲','航運類股大漲700點','航運類股狂漲700點','今天恭喜各位都大漲','前三天大漲了近700點','前三天暴漲了近700點','前三天狂漲了近700點','國內的成績相當不容易']
    testLoki(inputLIST, ['ExtremeGreed'])
    print("")

    # Neutral
    print("[TEST] Neutral")
    inputLIST = ['一日行情','持續觀察','提高警覺','明天小心','需特別注意','盤整平盤附近','觀望氣氛壟罩','進入調整階段','還是一日行情','觀望氣氛壟罩下','面板股都應該觀望','默默等股價表態中','對面板股都應該觀望','至少幅度不會那麼大','先空手看內資投信撐價','反彈仍是看量決定一切','幾十年來價格始終如一','對所有面板股都應該觀望','我會稍微停看聽觀察一下','持續觀察是否有波段漲幅','現在仍很多投資人在觀望17000','很多股票幾十年來價格始終如一','估計指數會在此點與月線間盤整震盪','也代表市場資金在觀望鮑爾的談話內容','所以這邊我還是要提醒大家有些不確定性','若不幸回測此低點需特別注意是否守的住']
    testLoki(inputLIST, ['Neutral'])
    print("")

    # 輸入其它句子試看看
    inputLIST = ["台股狂跌100點"]
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print(resultDICT)
    print("Result => {}".format(resultDICT))