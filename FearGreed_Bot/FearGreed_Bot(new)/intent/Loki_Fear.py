#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Fear

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Fear = True
userDefinedDICT = {"AUX": ["了", "吧"], "Who": ["他", "內資", "大大", "我", "投信", "投資人", "當沖客", "短線客", "鮑爾"], "adv": ["一切", "下", "不", "不過", "並", "久違", "代表", "以", "以來", "先", "前幾名", "勿", "只有", "可能", "和", "回來", "基本上", "壟罩", "大於", "已經", "很多", "怎樣", "拼命", "最後", "有", "有些", "比", "氣氛籠罩", "沒地方", "為", "為主", "目前", "看來", "稍微", "與", "裡", "請勿", "讓", "越", "較", "近", "這", "過去了", "附近", "需"], "低": ["低", "低於", "低檔", "低點", "底部", "新低", "最低點"], "盤": ["夜盤", "大盤", "尾盤", "早盤", "盤", "盤後"], "高": ["新高", "高", "高檔"], "K線": ["D", "K", "KD", "MACD", "半年線", "均線", "季線", "月線", "短線", "趨勢線", "頸線"], "Noun": ["QE", "上檔", "中國", "中繼", "之後", "交易日", "交易量", "代表", "個股", "價差", "區間", "可惜", "台指期", "多空", "套牢區", "守", "宣布", "小心", "市場預期", "年會", "應有的", "成交量", "成長股", "技術性", "技術面", "投資", "控管", "收盤", "新", "期貨", "機會", "正式", "氣氛", "水位", "波段", "海盜船", "現在", "空手", "籌碼", "聯準會", "行情", "許多", "護盤", "變", "買賣量", "走勢", "量能", "開始", "附近", "隔日沖", "震幅"], "Time": ["2個多月", "8/20", "一日", "下一波", "下禮拜一", "九天", "今天", "今日", "前三天", "半年", "多年", "幾天", "明天", "昨天", "昨日", "未來", "本週五", "每天", "短期", "第四季", "近期", "隔日"], "Unit": ["20%", "一根腳", "三種", "個", "前幾名", "口", "日", "月", "條", "次", "波", "第1根", "第二", "量", "點"], "Verb": ["下降", "不買", "估計", "做", "出現", "創", "反彈", "同步", "向上攻", "告訴", "回測", "坐", "增加", "壓回", "宣洩", "小幅", "帶領", "復原", "扭轉", "承接", "拉", "挑戰", "提醒", "撐價", "撿", "操作", "收", "收斂", "攻堅", "放大", "明顯", "朝向", "歐美", "決定", "注意", "減少", "玩", "略增", "看待", "看得出", "突破", "等待", "籠罩", "縮減", "續增", "翻", "股市", "記得", "購買", "走", "走跌", "跌", "跟隨", "跳空", "躺", "進入", "進駐", "逼近", "遭遇", "醞釀", "重新", "開始", "降低", "降到", "降幅", "面臨"], "Verbs": ["上升", "升空", "嗄空", "套現", "昇空", "追高"], "中立": ["守住"], "怕屎": ["怕死"], "盤整": ["不確定性", "不穩定", "平盤", "平緩", "整理", "調整", "震盪"], "股票": ["股"], "航運": ["航運股", "航運類股"], "觀察": ["停看聽", "看", "觀望"], "賣到": ["賣倒"], "開高": ["開很高", "開高走低"], "Subjects": ["LCD", "五日線", "亞股", "元氣", "台指", "台股", "大豆", "季線", "官股", "成績", "早盤", "期貨", "毛利", "玉米期貨", "盤後", "科技股", "美聯儲", "美股", "聯準會", "股市", "自營", "芝加哥期貨交易所(CBOT)", "銅價", "除權息", "面板股", "頸線"], "NegativeN": ["不好", "不幸", "不是", "不會", "不要", "尚未", "沒"], "PositiveN": ["好", "好棒棒", "好獲利", "就對了", "有", "有望", "符合"], "台積電": ["台積"], "市占率": ["市佔率"], "弱多頭": ["修正", "出量", "回穩", "守的住", "小漲", "拉上來", "拉回", "支撐", "收漲", "有利", "站穩", "解套"], "弱空頭": ["反壓", "只跌", "大風大浪", "守不住", "小跌", "止跌", "虧損", "遇壓", "量縮"], "強多頭": ["上攻", "佈倉", "做多", "反彈", "向上", "回升", "多方", "多頭", "大漲", "布局", "往上", "急拉", "攻上", "漲停", "漲幅", "猛追", "看好", "站上", "紅柱體", "續漲", "翻多", "翻紅", "融資", "變成", "買", "買滿", "買盤", "買超", "買進", "賺", "追", "追高", "順勢"], "強空頭": ["下彎", "下殺", "下跌", "偏空", "大跌", "套牢", "快跑", "急跌", "盤跌", "空單", "融斷", "要崩了", "賣", "賣壓", "賣超", "走弱", "跌幅", "跌深深", "跌破", "跌超過", "連跌", "長空"], "Adjectives": ["不好", "久", "人山人海", "做好", "像", "再次", "前進", "多數", "多的", "大", "好幾倍", "容易", "小", "少", "帥啦", "強", "快", "慢慢", "成功", "成為", "持續", "擠得", "正常", "沒人", "溫和", "特別", "繼續", "衝啦", "謹慎", "連續", "順利"], "Conjunction": ["一定", "不再", "不然", "不管你", "中", "也", "也是", "了", "仍", "仍是", "以上", "但", "但是", "再", "則是", "剛", "又", "及", "反而", "只會", "只要", "可以", "哪", "嗎", "在", "坦白說", "如果", "將", "就", "就是", "屆時", "往往", "很", "後", "從", "所以", "才", "接下來", "是", "時候", "會", "有", "有完沒完", "有所", "比較", "為", "現在", "當", "的", "盡量", "相當", "相當於", "算", "純屬", "絕對是", "至少", "若", "被", "要", "請", "逐漸", "這是", "連", "遇到", "還是", "還會", "還有", "那", "都", "都是", "都要"], "未平倉空單": ["未平倉", "未平倉口數", "未平倉空單", "未平倉量", "總未平倉量"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Fear:
        print("[Fear] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["Fear"]=[]
    if utterance == "[下禮拜一][看來][也是]大風大浪":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[不是][要]跌超過[20%][以上][才][算][空頭][嗎]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[不然]容易震盪":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[不管你][購買][哪][一支][股票]被套牢":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[中國][經濟]增長[一直][在]放緩":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[亞股]表現[幾乎][都]不理想":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[人們]擔心最[大][消費國][中國][的][需]求":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[今天][台股][微]跌[100][點]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[今天][台股]小掉[100][點]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[今天][台股]小跌[100][點]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[今天][台股]微掉[100][點]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[今天][台股]跌[100][點]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[今天][航運股]轉[弱]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[今天]尚未站穩[月線]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[今天]開高走低[收][平盤][附近]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[今日][遭遇]下彎[的][月線][反壓]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[今日][開高][後][技術性]壓回收斂漲幅":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[代表][多數][的][短線客][當沖客][的]買賣量[一定]有所降低":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[但]可惜[開高走低]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[個股]隔日沖[進駐]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[共同][成為][外資]的提款機":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[剛][復原][的][台股]還會震盪":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[只][能][不][停地]變賣[有]獲利[的]標記[套現]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[只會]盤跌[走勢]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[只有][本週五][收盤][不再]跌破[16983]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[只要][融資][餘額]降幅大於[大盤]跌幅":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[台積][尾盤][會]殺尾":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[台股][微]跌[100][點]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[台股][超詭異]虛漲":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[台股]小掉[100][點]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[台股]小跌[100][點]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[台股]微掉[100][點]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[台股]沒量[硬]拉[雞][盤]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[台股]跌[100][點]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[向上攻][堅]難度不小":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[地緣政治]局勢緊張":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[坦白說]也不會融斷":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[外資]空單[水位][不][續增][的][話]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[外資]賣超[159.1億]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[多空][都要]很小心":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[夜盤]要崩了[快跑]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[大盤][逐漸]逼近頸線":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[大盤]受限於[量][價架][構]欠[佳]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[如果][有]賣壓出現":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[屆時][會][較]偏空[看待]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[市場]最甜美的[階段][往往][就]過去了":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[投資][朋友][記得]不要[恐慌]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[持續][向上攻][堅]難度不小":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[指數][向上攻][堅][並][站穩][月線][反壓][區][的]難度不小":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[指數][持續][向上攻][堅][並][站穩][月線][反壓][區][的]難度不小":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[指數][若][要][持續][向上攻][堅][並][站穩][月線][反壓][區][的]難度不小":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[指數][面臨][月][半年][及]下降趨勢[的][三種][壓力]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[收盤]連[月線]都沒站上":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[早盤][容易][開很高][後]倒貨":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[有]多[少][人][追高][航運][之後]跌[了][40%]忍痛停損":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[期貨][選擇權][是][外資][的]避險工具":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[未來][仍][將]持續下跌":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[每天][都][像][坐]海盜船":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[現在][大盤]走弱":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[當]沒人有[買盤]意願[承接][會][怎樣]？":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[目前][正][在][除權息][旺][季]，[根本]停券":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[目前][盤][勢]屬於短期震盪":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[看來][台股]壓力尚未解除":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[短期][還是][很]不穩定":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[短線][技術面][都][告訴][我][會]稍微震盪":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[美股][從][昨天][開始][就][進入]小幅[的]震盪":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[買賣量]有所降低":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[這][區間][是]密集套牢區":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[這是]比較不好[的][地方]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[遇到]下彎[月線][賣壓]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "[遇壓]下跌[純屬][正常][賣壓][宣洩]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "下殺[的][最低點][為][16984]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "低檔[不買]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "加權[股][價][指數終場]下跌[1.91][點]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "因擔憂[生物燃料][行業][的][豆油][需]求":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "守不住[將][回測][8/20][低點][16248.08]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "小幅衰退":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "尚未[扭轉]長空[格局]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "就是一個止跌訊號了":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "很[難][一][次][就]突破":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "很明顯外資在玩隔日沖":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "忍痛停損":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "所有[面板股][都]不要碰":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "無量的上漲經[不][起][一][點][點][的][跌][勢]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "當外資期貨現貨同步的時候":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "空軍[將]出動":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "結果[現在][持續][被]嗄空[中]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "要再[高]很[難]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "負面因素並未消失":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "近期都是量縮震幅也變小":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "這回台灣和南韓同病相憐":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "這次外資因為太看好中國":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "連跌[九天]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "進而拖累[需]求":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "銅價已下跌[百分之五]以上":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "長空[中][的][反彈][開始]":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "難度不小":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "難度大":
        resultDICT["Fear"].append(10)
        pass

    if utterance == "風險控管要做好":
        resultDICT["Fear"].append(10)
        pass

    return resultDICT