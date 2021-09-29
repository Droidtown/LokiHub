#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for ExtremeFear

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_ExtremeFear = True
userDefinedDICT = {"AUX": ["了", "吧"], "Who": ["他", "內資", "大大", "我", "投信", "投資人", "當沖客", "短線客", "鮑爾"], "adv": ["一切", "下", "不", "不過", "並", "久違", "代表", "以", "以來", "先", "前幾名", "勿", "只有", "可能", "和", "回來", "基本上", "壟罩", "大於", "已經", "很多", "怎樣", "拼命", "最後", "有", "有些", "比", "氣氛籠罩", "沒地方", "為", "為主", "目前", "看來", "稍微", "與", "裡", "請勿", "讓", "越", "較", "近", "這", "過去了", "附近", "需"], "低": ["低", "低於", "低檔", "低點", "底部", "新低", "最低點"], "盤": ["夜盤", "大盤", "尾盤", "早盤", "盤", "盤後"], "高": ["新高", "高", "高檔"], "K線": ["D", "K", "KD", "MACD", "半年線", "均線", "季線", "月線", "短線", "趨勢線", "頸線"], "Noun": ["QE", "上檔", "中國", "中繼", "之後", "交易日", "交易量", "代表", "個股", "價差", "區間", "可惜", "台指期", "多空", "套牢區", "守", "宣布", "小心", "市場預期", "年會", "應有的", "成交量", "成長股", "技術性", "技術面", "投資", "控管", "收盤", "新", "期貨", "機會", "正式", "氣氛", "水位", "波段", "海盜船", "現在", "空手", "籌碼", "聯準會", "行情", "許多", "護盤", "變", "買賣量", "走勢", "量能", "開始", "附近", "隔日沖", "震幅"], "Time": ["2個多月", "8/20", "一日", "下一波", "下禮拜一", "九天", "今天", "今日", "前三天", "半年", "多年", "幾天", "明天", "昨天", "昨日", "未來", "本週五", "每天", "短期", "第四季", "近期", "隔日"], "Unit": ["20%", "一根腳", "三種", "個", "前幾名", "口", "日", "月", "條", "次", "波", "第1根", "第二", "量", "點"], "Verb": ["下降", "不買", "估計", "做", "出現", "創", "反彈", "同步", "向上攻", "告訴", "回測", "坐", "增加", "壓回", "宣洩", "小幅", "帶領", "復原", "扭轉", "承接", "拉", "挑戰", "提醒", "撐價", "撿", "操作", "收", "收斂", "攻堅", "放大", "明顯", "朝向", "歐美", "決定", "注意", "減少", "玩", "略增", "看待", "看得出", "突破", "等待", "籠罩", "縮減", "續增", "翻", "股市", "記得", "購買", "走", "走跌", "跌", "跟隨", "跳空", "躺", "進入", "進駐", "逼近", "遭遇", "醞釀", "重新", "開始", "降低", "降到", "降幅", "面臨"], "Verbs": ["上升", "升空", "嗄空", "套現", "昇空", "追高"], "中立": ["守住"], "怕屎": ["怕死"], "盤整": ["不確定性", "不穩定", "平盤", "平緩", "整理", "調整", "震盪"], "股票": ["股"], "航運": ["航運股", "航運類股"], "觀察": ["停看聽", "看", "觀望"], "賣到": ["賣倒"], "開高": ["開很高", "開高走低"], "Subjects": ["LCD", "五日線", "亞股", "元氣", "台指", "台股", "大豆", "季線", "官股", "成績", "早盤", "期貨", "毛利", "玉米期貨", "盤後", "科技股", "美聯儲", "美股", "聯準會", "股市", "自營", "芝加哥期貨交易所(CBOT)", "銅價", "除權息", "面板股", "頸線"], "NegativeN": ["不好", "不幸", "不是", "不會", "不要", "尚未", "沒"], "PositiveN": ["好", "好棒棒", "好獲利", "就對了", "有", "有望", "符合"], "台積電": ["台積"], "市占率": ["市佔率"], "弱多頭": ["修正", "出量", "回穩", "守的住", "小漲", "拉上來", "拉回", "支撐", "收漲", "有利", "站穩", "解套"], "弱空頭": ["反壓", "只跌", "大風大浪", "守不住", "小跌", "止跌", "虧損", "遇壓", "量縮"], "強多頭": ["上攻", "佈倉", "做多", "反彈", "向上", "回升", "多方", "多頭", "大漲", "布局", "往上", "急拉", "攻上", "漲停", "漲幅", "猛追", "看好", "站上", "紅柱體", "續漲", "翻多", "翻紅", "融資", "變成", "買", "買滿", "買盤", "買超", "買進", "賺", "追", "追高", "順勢"], "強空頭": ["下彎", "下殺", "下跌", "偏空", "大跌", "套牢", "快跑", "急跌", "盤跌", "空單", "融斷", "要崩了", "賣", "賣壓", "賣超", "走弱", "跌幅", "跌深深", "跌破", "跌超過", "連跌", "長空"], "Adjectives": ["不好", "久", "人山人海", "做好", "像", "再次", "前進", "多數", "多的", "大", "好幾倍", "容易", "小", "少", "帥啦", "強", "快", "慢慢", "成功", "成為", "持續", "擠得", "正常", "沒人", "溫和", "特別", "繼續", "衝啦", "謹慎", "連續", "順利"], "Conjunction": ["一定", "不再", "不然", "不管你", "中", "也", "也是", "了", "仍", "仍是", "以上", "但", "但是", "再", "則是", "剛", "又", "及", "反而", "只會", "只要", "可以", "哪", "嗎", "在", "坦白說", "如果", "將", "就", "就是", "屆時", "往往", "很", "後", "從", "所以", "才", "接下來", "是", "時候", "會", "有", "有完沒完", "有所", "比較", "為", "現在", "當", "的", "盡量", "相當", "相當於", "算", "純屬", "絕對是", "至少", "若", "被", "要", "請", "逐漸", "這是", "連", "遇到", "還是", "還會", "還有", "那", "都", "都是", "都要"], "未平倉空單": ["未平倉", "未平倉口數", "未平倉空單", "未平倉量", "總未平倉量"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_ExtremeFear:
        print("[ExtremeFear] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["ExtremeFear"]=[]
    resultDICT["Degree"]=[]
    if utterance == "[他][們][最後][會]把[股票][賣倒][台股]崩盤為止":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台積電]遭摜壓":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台股][最後][一][盤]急挫[百][點]失守[月線]":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台股][狂]跌":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台股][狂]跌[100][點]":
        resultDICT["ExtremeFear"].append(10)
        resultDICT["Degree"]="Extreme"
        pass

    if utterance == "[台股][狂]跌[5%]":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台股]失守":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台股]失守[月線]":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台股]急挫":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台股]急挫[100][點]":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台股]急挫[5%]":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台股]急挫[百][點]失守[月線]":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台股]暴跌":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台股]暴跌[100][點]":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台股]暴跌[5%]":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台股]狂掉[100][點]":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台股]狂掉[5%]":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台股]重挫":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台股]重挫[100][點]":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[台股]重挫[5%]":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[在][大盤]急跌[2000][點][之後]":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[大][家]不怕屎[就]盡量[融資]":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[大盤]急跌[2000][點]":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[大豆][期貨]跌至[七周][半]最低":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[早上][根本][就是]歹戲拖棚":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[爛][股][一支]":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[玉米期貨]觸及[三周][半]最低":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[美股][全]數走跌":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[芝加哥期貨交易所(CBOT)][大豆][期貨][週][五]跌至[七周][半]最低":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[芝加哥期貨交易所(CBOT)][大豆][期貨]跌至[七周][半]最低":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "[這]回元氣大傷":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "不怕屎[就][盡量][融資]":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "元氣大傷":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "拖累[美股][全]數走跌":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "歹戲拖棚":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "火葬場":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "等於[是][在][不]知[不]覺[中]把[自己]推入[中國][的]火葬場":
        resultDICT["ExtremeFear"].append(10)
        pass

    if utterance == "過陣子離開[股市]好了":
        resultDICT["ExtremeFear"].append(10)
        pass

    return resultDICT