#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for badminton

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_badminton = True
userDefinedDICT = {"丸佳浩": [""], "世界大賽": [""], "坂本勇人": [""], "岡本和真": [""]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_badminton:
        print("[badminton] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[110年][第一次][全國][羽球]排名[賽]於[今天]在[台北][體育館]點燃[戰火]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[21]比[15]取勝":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[21]比[19]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[4][強賽][小天]將碰[上][香港][好手][伍家朗]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[6][平][後][周天成][連][下][3分]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[BWF][世界]巡迴[賽][泰國][站首站][12日]將開打":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[YONEX][泰國][羽球]公開[賽][今天]進行各組[8][強賽]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[一口氣]連拿[5分][站][上]領先":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[一度]陷入[3]比[7][落後]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[世界][球后][戴資穎]重返[國際][賽舞台]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[世界][球王]、[日本][名將][桃田賢][斗][原訂][車禍][後][首度]回歸[國際賽]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[世界][羽球][聯盟]（[BWF]）[1月]在[泰國][曼谷]舉行[3場][賽事]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[世界]排名[第10]的[馬來西亞][男單][一哥][李梓嘉]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[世界]排名[第2]的[周天成][前][兩][輪][分別]擊敗[泰國][印尼][好手]挺進[8][強]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[世界]排名[第2]的[周天成]以直落[二]橫掃[謝薩]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[中國隊][日前][也]已宣布退出在[泰國]舉行的[3]站[賽事]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[中華民國][羽球][協會]和達克運動合作":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[也]分享了[一段][比賽][中][途]從換[球器]拿[新球]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[也]是[青少][年選手]邁向[職業][球員]的認證敲門[磚]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[也]讓[她]必須停頓[幾秒]確認[後]才回到[場][上]發球":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[也]讓[她]忍不住發文表示":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[也]讓[對手]追至[只差][1分]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[也]讓[小天]以[21]比[19]有驚無險拿下[對手]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[今天]在[泰國][曼谷]進行第[3天][賽事]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[今天]碰[上][大會][第8][種子]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[今天]開局[小天][暖機][稍慢]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[他][同樣][也]已報名參加[泰國][賽]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[他]在[新年]第[一天][剛]許下奪[金]的[願望]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[先]下[一][城]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[先]以[21]比[16]拿下":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[全國][羽球]排名[賽][一年]舉辦[兩次]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[兩][人]會[繼續]為了晉級奮戰":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[原訂][首][戰對手]為[泰國][選手柯實]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[去年]拿下[第八名]的[李芳任]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[只]是[歷]時[長達][1小時]的[比賽]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[可惜]「[羽球王子]」[王子維]歷經[3局][苦戰][後]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[可惜]未能挑戰[成功]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[台]將這次有[4組][人馬]參加[泰國][賽]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[台灣][羽球][一哥][周天成][今天]在[泰國][羽球]公開[賽男][單][次][輪]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[台灣][羽球][一哥][周天成][今天]碰[上][世界]排名[第10]的[馬來西亞][李梓嘉]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[大會][首日][甲][組賽][事][僅]有混雙[項目]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[對手][一顆][長球]壓在[底線][上]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[對手]從領先打到[落後]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[小天]下[一輪][對手]是[大會][第8][種子]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[小天]以[3][勝]略占[上][風]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[小天]又是在[2]比[3][微幅][落後]下展開[強力]反撲":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[小天]在[比賽][最後]以[20]比[18]取得[聽牌]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[小天]雖提出挑戰":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[戰]況[也][一][路膠]著至[比賽][尾盤]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[戴資穎][今天]搭[機][前]全副武裝":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[戴資穎][明]將在[16][強]面對[南韓][好手][金佳恩]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[戴資穎][昨]在[泰國][賽首輪]擊敗[世界]排名[129]的[地主][小將]本[雅帕]（[Benyapa][Aimsaard]）搶下[好采頭]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[所][幸]接下來[他][及時]回神":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[所][幸]接下來[對方]在[網][前]回擊時[出]拍過[猛]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[日前][剛]在[日本][全][國錦][標賽]復出":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[日媒][今天]報導":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[日本][羽球][協會][也]決定不派選[手]參賽":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[日本隊]將[全部]退出[泰國][賽]。":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[昨][戴資穎]拿[新球]的[時候]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[昨]在超級[1000][系列][泰國]公開[賽]直落[二]晉級":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[最終僅]用[43分鐘]以直落[二]取勝":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[李芳任][也]表示[他]會[盡全][力]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[根據日][媒Sponichi][Annex][今天]報導":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[桃田賢][斗][原訂]在[成田][機場][搭機]準備前往[泰國]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[桃田賢][斗][去年][1月]在[馬來西亞][大師][賽]封王[後]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[桃田賢][斗]接受[武漢][肺炎]檢測[結果]為[陽性]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[桃田賢][斗]高居[泰國][賽頭號][種子]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[楊景][惇][延續氣勢]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[楊景][惇]拿下第[7分][後]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[楊景][惇]第[三度]合拍":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[次局][前][段][雙方]展開拉鋸":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[次局]開賽[雙方]展開[激烈]纏鬥":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[此後]在[一][路]領先的[情況][下]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[瞬間]取得[8]比[0]領先":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[程琪雅]對[上][亞][柏林][上][凱]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[第1局]以[21]比[15]拿下":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[第2局][後半段]在接發球時發生失誤":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[總][獎金][100萬美元]的[泰國][羽球]公開[賽]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[自己]連拿[6分]逆轉":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[設備]卻要倒不[倒]的[畫面]。":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[語氣]難掩[無奈]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[賽][後][楊景][惇]提到":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[賽][後][程琪雅]笑說[兩][人]發揮比想像[中][好]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[選手][都]是透過換[球器]拿取[新球]。":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[選手]要換[新球][都]是向發球[審]拿[球]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[雙方]過去[5次]交手":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[雙方]過去[5次]交鋒":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[雙方]過去對決[3次]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[順利]摘下[8][強][門票]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[順利]晉級[8][強]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[首局][周天成]較為[慢熱]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[首局][後][段]展開反撲":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[首次]搭檔的[陳政寬]／[程琪雅]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "[首輪]對[上][合庫][邱相榤][劉巧芸]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "不過[他][緊]咬分[差]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "不過[她]仍保持[平常][心]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "不過受到[疫情]影響":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "且[最近][2次]交手[都]贏":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "且[近期]取得[2]連勝的[狀態]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "並取得對戰[4]連勝":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "仍[全力]緊咬[比數]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "仍以[21]比[14]獲勝":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "以[1]比[2][惜敗][香港][名將][伍家朗]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "但[她]穩住[陣腳]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "但[近期]卻是苦吞對戰[2]連敗":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "但在[機場]接受[武漢][肺炎]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "但是[今天][默契]發揮還算[順利]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "努力打好[每][一場][比賽]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "勇奪[男單][3]連[霸]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "包括[2]站超級[1000][系列]的[亞洲]公開[賽]以及[年終賽]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "包括[世界][球后][戴資穎]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "化解[平][手窘境]展開[強][勁攻勢]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "卻在[今天]傳出確診的[消息]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "取得[10][勝][6][敗]對戰[優勢]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "吸引高達[近][1800位][選手]參賽":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "因此[許]多[羽][球][好手]躍躍欲試":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "在[15]比[17]凍結住[對手]取[分機會]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "在[當地]發生[車禍]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "在懊惱[自己]打不好時":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "報名[人數]創下[新高]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "將[球][直接]掃出[邊線][外]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "對[此]小戴[也]忍不住表示":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "小戴[今]除在[個人][Imstagram]貼出[自己]的[超][水準美技][外]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "小戴尚未嘗過[敗績]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "已啟程前往[泰國]備戰":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "找[機會]回擊":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "把[自己]的[責任]做[好]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "提[前]止步":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "搶下[4][強][門票]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "是[世界][羽球]巡迴[賽]超級[1000][系列]的[頂級][大賽]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "是[國內][年度][最高級][別]的[羽球][個人賽]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "是[職業][球員][年度][國內]排名競賽與[國手]選拔的[舞台]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "更在[比賽][中][段]取得[最大]的[15]比[9]領先":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "本次[全國][羽球]排名[賽]不開放[觀眾]進場":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "檢測[結果]為[陽性]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "為了避免[多餘肢體]接觸":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "然而[泰國][賽場][邊]的換[球器]架設的[方式][可能]有待加強":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "爭奪[決][賽門][票]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "直落[二]橫掃[世界]排名[第18]的[印尼][好][手謝薩]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "看看[我]給[它]的[眼神]說了什麼":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "確定無[緣][泰國][賽]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "穿[上]防疫[裝備]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "考量[全球][疫情情況]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "而[她][先前]因為[腳]受傷休息[一陣子]沒有[比賽]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "而[小天][始終]維持[3分][以內]的[微幅]領先[優勢]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "而面對[今年][7月]登場的[東京][奧運]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "與搭檔[李芳任][也][較少][機會]可以[一起]練習":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "要倒不[倒]的":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "讓[第一次]打混雙的[學][弟][體力]稍嫌[不足]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "透過達克運動[Youtube][頻道]提供直播服務":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "這次重回[國際][舞台]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "過去[周天成]與[伍家朗][16度]交手":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "還[頻頻]用大對[角]展開進攻":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "那個拿[球]的還不忘跟[我]開開玩笑":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "開局陷入[2]比[5]的[落後]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "開賽[雙方][五度][戰成][平手]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "除了[日本隊]退出[泰國][賽]外":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "雖[中間]仍有[三次]被[對手][連續]得分":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "雖然[之前][很少]練習":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    if utterance == "靠著[一波][13]比[1][攻勢逆勢][超前]":
        # write your code here
        resultDICT["badminton"] = resultDICT["badminton"] + 1

    return resultDICT