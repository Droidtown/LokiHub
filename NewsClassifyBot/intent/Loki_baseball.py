#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for baseball

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_baseball = True
userDefinedDICT = {"丸佳浩": [""], "世界大賽": [""], "坂本勇人": [""], "岡本和真": [""]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_baseball:
        print("[baseball] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[2015年]轉職成[牛棚]投手[略]有進步":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[2019年][22場][先]發拿到[7][勝][5][敗]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[25.1局][只]被打[5分]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[32][歲][坂本勇人]受[年輕][人]刺激":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[不只]損失[1190美金]的[薪資]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[之後][他]出面說明[自己][心情][平靜]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[也][獲縣長][楊文科]表揚":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[也]期待[今年]會有什麼樣進階的防疫[措施]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[五峰][國小][棒球隊][前]幾次參[賽][都]在[預賽]就遭到淘汰":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[五峰][國小][棒球隊][去年][十二月]參加[原民會]主辦":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[五峰][國小]在[賽][中]發揮[完整][實力]榮獲[季軍]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[五峰][國小]屬於[偏][鄉國小]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[今年][巨人軍]加入[DeNA][潛力梶谷隆][幸]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[今年][有望]扛守護[神]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[今年]準備有[一番]作為":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[他][2018年]與[洛磯隊]簽下[3年][5200萬美元]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[他][也]坦言":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[他][早年]在[雙城藍鳥][皇][家][只]是[平庸]的[先]發投[手]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[他]在[去年]加盟[歐力士]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[他]曾在[去年][10月][28日][例][行][賽尾聲]對決[代]打的[王柏融]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[全力]打出[好球]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[分別]排名[第9][第13]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[分別]擊敗[南投][埔里]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[去年][底]跟[西川][遙輝][一起]訓練的[期間]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[去年]因為[新][冠肺炎疫情]選擇退賽":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[去年]摘下[生涯][首座][李維]拉獎":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[反]正對[手][也]接不住":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[坂本勇人]認為[棒次]沒有[太多]影響":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[坂本勇人]說":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[坂本勇人]進行[多樣]的[訓練][內容]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[家][中][2名][幼兒]的[健康]還是[很重要]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[小聯盟][9年][生涯]累計[18][勝][20][敗]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[希][金斯][主要][扛佈局]投[手角色]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[希][金斯]未[登][上][大聯盟]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[年年]增加練習量不敢怠[慢]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[成功]寫下[五峰][國小][近年]參賽[最佳][紀錄]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[我][現在][處]在[非常好]的[狀態]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[我]感覺[真]的[好多]了":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[我]相信在[去年]學到[很多][經驗]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[我]認為[棒球]在[去年]表現[良好]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[新]的[球季]來臨":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[新竹][縣長][楊文科]稱讚":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[普][萊斯][上次]在[大聯盟]出賽時還穿著[紅][襪球衣]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[普][萊斯]告訴[美媒]預計會在[今年]參加[比賽]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[普][萊斯]是[道奇招牌][球星]之[一]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[普][萊斯]透露[自己]會在[下個月]開始[春][訓]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[最後]還[錯]過[球隊]奪下[世界大賽][冠軍]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[本屆]共計[二十四隊]參賽":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[歐力士][15日]與[洋]投希[金斯]完成續約":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[歐力士]監督[中][嶋聰]有意讓[去年]的守護[神][狄克][森]轉任[先]發":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[比賽]時[他]秉持[教練]所說":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[特別]從[他][身]上學[習]增加[爆發力]的[方式]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[球隊][不斷]在[逆勢][中][茁][壯]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[球隊][也]規劃訓練[課表]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[白襪][上季]暌違[12年]重返[季][後][賽]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[白襪]以[3年][5400萬美元]簽下救援投[手韓][崔克斯][LiamHendriks]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[美媒][TheAthletic]報導":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[美聯][MVP][選票]投給[他]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[芝加哥][白襪]在[自由市場]砸了[大錢]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[賽][前]模擬[比賽狀況]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[賽揚獎][資深][左][投普萊斯][去年]加入[道奇]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[近日][更]拿下[新竹縣台][彩威力盃]選拔[賽冠軍]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "[韓][崔克斯][上季]出賽[24場]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "不過[他]肯定[大聯盟]的[防疫]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "不過[普][萊斯]認為[自己][狀況][不錯]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "不過因為[疫情]爆發選擇退賽":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "以[滑球]為輔":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "以及[球員][全心]投入練習":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "但[他]不去[多]想":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "但[疫情]卻還沒結束":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "但[直]到[2019年]才[一口氣]爆發成為[明星]投手":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "入選[MLB][第一隊]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "共奪[45次]三振":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "冒著爭議請出[名人][堂教頭]拉[魯沙][Tony][ La ][Russa][掌兵]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "出賽[41場]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "分組[預賽]以[兩][勝][一]負晉級[複賽]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "包括跑[體能]以及守備的補[強]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "即使[空白][一年]沒[比賽]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "取得[代表權]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "受[年輕][球員]影響":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "因此[希金斯][很]有[可能]接任守護[神]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "在[假日]安排[友誼賽]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "在[全][國賽]晉級[八][強]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "在[美][職體系]最[高層級]到[3][A]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "在[資源][不足]與[學][生人數][逐年]減少[情況][下]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "在[賽][中][完整]發揮[個人][球技]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "在[賽][中]全力以赴":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "在[賽中]投出[好成績]的[隊長][林承俊]說":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "在本次[賽事][中一路]過關斬將":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "增加實戰[經驗]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "失[11分]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "奪[3][勝][3][敗]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "將[滿][32][歲]的[韓][崔克斯]過去[5季]效力運動家":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "就像因[手術]要關機[一年][一樣]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "幫助運動家坐上[美][西王座]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "恢復的[時間]需要[比較多]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "成為[史][上][最高][年薪]的[牛棚]投手":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "打就對了":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "拿下[19次][中][繼][成功]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "接著是[丸佳浩]和[岡本和真]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "教練[王勝榮]直言":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "是[一種]刺激":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "最終拿[下季][軍]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "有[31次][中][繼][成功]及[15次]救援[成功]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "本[屆球隊]以[四]、[五]、[六][年級][球員]組成":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "此次擔任投手":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "比[去年]增加[2000萬日圓]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "然後[坂本勇人]扛[第2][棒]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "然後開除[總][教練倫][特利亞][RickRenteria]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "用[3顆][150公里][以上][速球]奪三振":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "監督[原][辰德]有意調整[棒次]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "累計[41.1局]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "結果[他][錯]過了[道奇]拿下[世界大賽][冠軍]的[歷史][時刻]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "經過日復一日苦練":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "練習量[年年]增加":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "能[有效]限制傳染":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "能拿到這份[佳績]實屬[不易]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "自責[分率][4.28]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "與[傳統][球隊]練習量比起來[偏短]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "表明將開始[春][訓]備戰":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "被[上][壘率][0.671][都]是[生涯][最佳]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "被[日媒]稱為":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "討[教西][川][遙輝][爆發力]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "該項[賽事]是[原鄉]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "讀[賣巨人][隊][32][歲][明星][內][野手][坂本勇人]投入[自主]訓練":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "讓[他]擔任[第一棒]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "讓[大家]認識來自[新竹縣]的[五峰][國小][棒球隊]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "跟[一年][前]或[六個月][前]相比":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "跟[年輕]時比較":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "跟[湯淺大]等[年輕][好手][一起][自主]訓練":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "這[在先]發投[手]之[中][也]算[很高]的[身價]了":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "這[歸功]於[校長][葉惠雯]及[教練]帶領[下]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "這[證明]防疫是可[行]的":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "還有傳接[球]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "還能[活動]且對[自己][身體][也]有[信心]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "關門[15次][成功][14次]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "雖接觸[棒球]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    if utterance == "雖然[他]尚未確認將於[今年][重新][回球場]":
        # write your code here
        resultDICT["baseball"] = resultDICT["baseball"] + 1

    return resultDICT