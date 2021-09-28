#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Greed

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Greed = True
userDefinedDICT = {"AUX": ["了", "吧"], "Who": ["他", "內資", "大大", "我", "投信", "投資人", "當沖客", "短線客", "鮑爾"], "adv": ["一切", "下", "不", "不過", "並", "久違", "代表", "以", "以來", "先", "前幾名", "勿", "只有", "可能", "和", "回來", "基本上", "壟罩", "大於", "已經", "很多", "怎樣", "拼命", "最後", "有", "有些", "比", "氣氛籠罩", "沒地方", "為", "為主", "目前", "看來", "稍微", "與", "裡", "請勿", "讓", "越", "較", "近", "這", "過去了", "附近", "需"], "低": ["低", "低於", "低檔", "低點", "底部", "新低", "最低點"], "盤": ["夜盤", "大盤", "尾盤", "早盤", "盤", "盤後"], "高": ["新高", "高", "高檔"], "K線": ["D", "K", "KD", "MACD", "半年線", "均線", "季線", "月線", "短線", "趨勢線", "頸線"], "Noun": ["QE", "上檔", "中國", "中繼", "之後", "交易日", "交易量", "代表", "個股", "價差", "區間", "可惜", "台指期", "多空", "套牢區", "守", "宣布", "小心", "市場預期", "年會", "應有的", "成交量", "成長股", "技術性", "技術面", "投資", "控管", "收盤", "新", "期貨", "機會", "正式", "氣氛", "水位", "波段", "海盜船", "現在", "空手", "籌碼", "聯準會", "行情", "許多", "護盤", "變", "買賣量", "走勢", "量能", "開始", "附近", "隔日沖", "震幅"], "Time": ["2個多月", "8/20", "一日", "下一波", "下禮拜一", "九天", "今天", "今日", "前三天", "半年", "多年", "幾天", "明天", "昨天", "昨日", "未來", "本週五", "每天", "短期", "第四季", "近期", "隔日"], "Unit": ["20%", "一根腳", "三種", "個", "前幾名", "口", "日", "月", "條", "次", "波", "第1根", "第二", "量", "點"], "Verb": ["下降", "不買", "估計", "做", "出現", "創", "反彈", "同步", "向上攻", "告訴", "回測", "坐", "增加", "壓回", "宣洩", "小幅", "帶領", "復原", "扭轉", "承接", "拉", "挑戰", "提醒", "撐價", "撿", "操作", "收", "收斂", "攻堅", "放大", "明顯", "朝向", "歐美", "決定", "注意", "減少", "玩", "略增", "看待", "看得出", "突破", "等待", "籠罩", "縮減", "續增", "翻", "股市", "記得", "購買", "走", "走跌", "跌", "跟隨", "跳空", "躺", "進入", "進駐", "逼近", "遭遇", "醞釀", "重新", "開始", "降低", "降到", "降幅", "面臨"], "Verbs": ["上升", "升空", "嗄空", "套現", "昇空", "追高"], "中立": ["守住"], "怕屎": ["怕死"], "盤整": ["不確定性", "不穩定", "平盤", "平緩", "整理", "調整", "震盪"], "股票": ["股"], "航運": ["航運股", "航運類股"], "觀察": ["停看聽", "看", "觀望"], "賣到": ["賣倒"], "開高": ["開很高", "開高走低"], "Subjects": ["LCD", "五日線", "亞股", "元氣", "台指", "台股", "大豆", "季線", "官股", "成績", "早盤", "期貨", "毛利", "玉米期貨", "盤後", "科技股", "美聯儲", "美股", "聯準會", "股市", "自營", "芝加哥期貨交易所(CBOT)", "銅價", "除權息", "面板股", "頸線"], "NegativeN": ["不好", "不幸", "不是", "不會", "不要", "尚未", "沒"], "PositiveN": ["好", "好棒棒", "好獲利", "就對了", "有", "有望", "符合"], "台積電": ["台積"], "市占率": ["市佔率"], "弱多頭": ["修正", "出量", "回穩", "守的住", "小漲", "拉上來", "拉回", "支撐", "收漲", "有利", "站穩", "解套"], "弱空頭": ["反壓", "只跌", "大風大浪", "守不住", "小跌", "止跌", "虧損", "遇壓", "量縮"], "強多頭": ["上攻", "佈倉", "做多", "反彈", "向上", "回升", "多方", "多頭", "大漲", "布局", "往上", "急拉", "攻上", "漲停", "漲幅", "猛追", "看好", "站上", "紅柱體", "續漲", "翻多", "翻紅", "融資", "變成", "買", "買滿", "買盤", "買超", "買進", "賺", "追", "追高", "順勢"], "強空頭": ["下彎", "下殺", "下跌", "偏空", "大跌", "套牢", "快跑", "急跌", "盤跌", "空單", "融斷", "要崩了", "賣", "賣壓", "賣超", "走弱", "跌幅", "跌深深", "跌破", "跌超過", "連跌", "長空"], "Adjectives": ["不好", "久", "人山人海", "做好", "像", "再次", "前進", "多數", "多的", "大", "好幾倍", "容易", "小", "少", "帥啦", "強", "快", "慢慢", "成功", "成為", "持續", "擠得", "正常", "沒人", "溫和", "特別", "繼續", "衝啦", "謹慎", "連續", "順利"], "Conjunction": ["一定", "不再", "不然", "不管你", "中", "也", "也是", "了", "仍", "仍是", "以上", "但", "但是", "再", "則是", "剛", "又", "及", "反而", "只會", "只要", "可以", "哪", "嗎", "在", "坦白說", "如果", "將", "就", "就是", "屆時", "往往", "很", "後", "從", "所以", "才", "接下來", "是", "時候", "會", "有", "有完沒完", "有所", "比較", "為", "現在", "當", "的", "盡量", "相當", "相當於", "算", "純屬", "絕對是", "至少", "若", "被", "要", "請", "逐漸", "這是", "連", "遇到", "還是", "還會", "還有", "那", "都", "都是", "都要"], "未平倉空單": ["未平倉", "未平倉口數", "未平倉空單", "未平倉量", "總未平倉量"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Greed:
        print("[Greed] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["Greed"]=[]
    if utterance == "K大於D":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[5][日]均線向上":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[9][月][台股][指數][期貨]漲[1.3][點]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[MACD]變成紅柱體[第1根]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[三百][以][下]算[是]很便宜了":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[今天][大盤]小漲[21][點]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[今天][有]向上攻[的][情形]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[今天]成功守住[了][16983]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[今日][大盤][跳空]開高":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[今日][大盤]跳空開高後":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[今日]早盤洗盤完有機會拉尾盤":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[但][今天][就][看得出]支撐明顯":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[但][至少][成交量]比昨日略增[也][收漲]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[但是]不要一次買滿":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[內資][做多][價差][反而][成為][了]支撐[的][交易量]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[可]望[在][未來]幾[年內]達到[一定][規模][的][市占率]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[台積電]則[跳空]上漲[收]復所[有][均線]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[台股][在]本[波]回升[行情]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[台股][連續][四][個][交易日]反彈[後]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[台股]小漲[100][點]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[台股]本[波]回升行情":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[台股]本[波]行情回升":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[在][持續][多頭][的][情勢][下][都]有機會解套":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[基本上]買超[前幾名][都是]隔日沖":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[外資][也][有][可能]開始增加[期貨][的]多單":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[外資][則是][淨多單]增加[1082][口]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[多方]優勢":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[多頭][的]回升[才][算][正式]開始":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[夜盤][帥啦][衝啦][帶領][亞谷][紫蝶][反彈][帶領][歐美][股市]回穩向上":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[大盤]創[這][波][低點][以來]新高":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[如果][明天][收盤][再次]順利守住":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[官股][銀行][也][在][上週五][大][力]護盤":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[尾盤]拉上來":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[尾盤]翻紅":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[市場]對[聯準會][政策][收][緊][的]擔憂有所緩解":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[帶領][亞谷][紫蝶][反彈][帶領][歐美][股市]回穩[向上]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[很多][股票]底部出現":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[從][底部]反彈[了][800]點[的][行情]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[慢慢][佈倉]買進成長股":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[所以][今天]順勢整理":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[所以][是][個股][跌深深][的]反彈[行情]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[投信]買超[7.7億]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[投資人]可以開始布局":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[拉回]買就對了":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[拼命]買和賣賺價差而已":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[敦泰]出貨動[能][可]望更加強勁":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[昨天][提醒][同學]勿追高":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[昨天][航運]漲[了][100]點":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[最後]收漲[21][點]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[月]增[ 10.33%]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[未來][將]持續[朝向][多頭]前進":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[現在][政策]開始[重新]翻多":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[相當於][變成][下一波]反彈[的][醞釀]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[看][了][許多][今天]大漲[的][股票]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[科技股]回升":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[科技股]領軍回升":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[突破][下降][趨勢線][並][重新][站上]月線[及][半年線][後][再次]上攻":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[第四季][就][會]有好獲利":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[等待]月線[及]半年線拉平緩[後]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[籌碼][少][在][中繼]反彈[行情][中][比較]有機會":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[絕對是][布局][做][第二][波]反彈[的]機會點":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[美聯儲][將][很][快][開始][收][緊][貨幣][政策][的]預期提振[了][美元]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[美聯儲]提振[了][美元]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[美股][20][日]上漲":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[自營][上週五][就]開始做多":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[航運][昨天]漲[了][5%]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[航運]漲[100][點]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[行情]還會[再]往上[走]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[該][股][目前]已站上[季線]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[請勿]追漲停":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[讓][他]穩健[慢慢]往上[走][最棒]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[讓][我]減少[很多]虧損":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[資金]翻[了]好幾倍":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[較]有利[多方]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[這][個][盤後]不[錯][吧]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[這][樣]保持下去就對了":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[這][樣]多頭格局[會][更]確立":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[這][頂多]損失[一][點][點][報酬]而已":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[那]現在[還是]多頭[吧]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[量]溫和放大":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[隔日][宣布][聯準會][縮減]QE[的][可能]較低":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "[難]得站上[五日線][了]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "且[在][2022年]出貨[量能][有][機會][開始]明顯成長":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "伴隨[鋼鐵][市]況需求強勁":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "只要[目前][的][股][價][低於][應有的]價值":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "增[ 10.33%]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "增加[10.33%]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "多空手腳都要快":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "好[兆頭]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "急拉[尾盤]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "感謝[官股][銀行][和][自營][商][的]護盤":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "指標[還是]多方":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "推動[毛利][及]獲利維持[在]高檔[水準]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "攻上[季線][很]有望":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "有拉回[我][還是][會][撿][回來]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "有站穩[頸線]跟[上升][趨勢線]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "本[波]行情回升":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "激勵[鋼鐵][類][股][多數][收漲]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "盤[越][久]量能越強":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "看好[9][月][行情]續漲":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "站上[5][日][均線]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "站上[季線]":
        resultDICT["Greed"].append(10)
        pass

    if utterance == "總未平倉量[為]-[19929][口]":
        resultDICT["Greed"].append(10)
        pass

    return resultDICT